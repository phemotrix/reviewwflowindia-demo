"""
FastAPI Server for 3D India State & Sector Business Scout
Serves the 3D WebGL Google Maps interface and REST API endpoints.
"""
import os
import io
import csv
from typing import Optional, Dict, Any, List
from fastapi import FastAPI, Query, HTTPException, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config import INDIAN_REGIONS, PORT, GOOGLE_MAPS_API_KEY
from sectors import generate_sectors_for_region
from scraper import scrape_and_audit_sector
from auditor import audit_business_website

app = FastAPI(title="India 3D Sector Business Scout", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory sector business cache for high performance
SECTOR_CACHE: Dict[str, List[Dict[str, Any]]] = {}

class AuditRequest(BaseModel):
    sector: Dict[str, Any]
    api_key: Optional[str] = None

class PitchRequest(BaseModel):
    biz_name: str
    category: str
    website: Optional[str] = None
    flaws: List[str] = []

@app.get("/api/config")
def get_config():
    """Returns basic configuration and active default Google Maps API key if set."""
    return {
        "has_env_key": bool(GOOGLE_MAPS_API_KEY),
        "api_key": GOOGLE_MAPS_API_KEY
    }

@app.get("/api/regions")
def list_regions():
    """Returns available Indian states, metropolitan districts, and boundaries."""
    results = []
    for key, val in INDIAN_REGIONS.items():
        results.append({
            "key": key,
            "name": val["name"],
            "type": val["type"],
            "state": val.get("state"),
            "center": val["center"],
            "zoom": val["zoom"],
            "default_grid": val.get("default_grid", [10, 10]),
            "tilt": val.get("tilt", 55),
            "heading": val.get("heading", 0)
        })
    return {"regions": results}

@app.get("/api/sectors")
def get_sectors(
    region: str = Query("mumbai", description="Region key, e.g. mumbai, delhi_ncr, maharashtra"),
    rows: Optional[int] = Query(None),
    cols: Optional[int] = Query(None)
):
    """
    Subdivides the region into geometric sectors (e.g., 100 sectors for Mumbai).
    Returns coordinates, 3D camera presets, and status.
    """
    data = generate_sectors_for_region(region, rows, cols)
    
    # Enrich with cached stats if available
    for sec in data["sectors"]:
        sec_id = f"{region}_{sec['id']}"
        if sec_id in SECTOR_CACHE:
            cached_leads = SECTOR_CACHE[sec_id]
            no_web = sum(1 for b in cached_leads if b["lead_status"] == "NO_WEBSITE")
            crap_web = sum(1 for b in cached_leads if b["lead_status"] == "CRAP_WEBSITE")
            good_web = sum(1 for b in cached_leads if b["lead_status"] == "GOOD_WEBSITE")
            sec["status"] = "ready"
            sec["stats"] = {
                "total_businesses": len(cached_leads),
                "no_website": no_web,
                "crap_website": crap_web,
                "good_website": good_web
            }
            
    return data

@app.post("/api/sector/audit")
def audit_sector_endpoint(req: AuditRequest):
    """
    Scrapes and audits all businesses inside a specific sector.
    Returns categorized leads: No Website, Crap Website, Good Website.
    """
    sector = req.sector
    region_key = sector.get("region_key", "mumbai")
    sec_id = f"{region_key}_{sector['id']}"

    api_key = req.api_key or GOOGLE_MAPS_API_KEY or None

    # Check cache first
    if sec_id in SECTOR_CACHE:
        leads = SECTOR_CACHE[sec_id]
    else:
        leads = scrape_and_audit_sector(sector, google_api_key=api_key)
        SECTOR_CACHE[sec_id] = leads

    no_web = sum(1 for b in leads if b["lead_status"] == "NO_WEBSITE")
    crap_web = sum(1 for b in leads if b["lead_status"] == "CRAP_WEBSITE")
    good_web = sum(1 for b in leads if b["lead_status"] == "GOOD_WEBSITE")

    summary = {
        "sector_id": sector["id"],
        "locality": sector.get("locality"),
        "total_businesses": len(leads),
        "no_website": no_web,
        "crap_website": crap_web,
        "good_website": good_web,
        "hot_leads_total": no_web + crap_web,
        "leads": leads
    }
    return summary

@app.get("/api/sector/cached")
def get_cached_sector(region: str, sector_id: str):
    """Retrieves cached businesses for a sector if already audited."""
    sec_id = f"{region}_{sector_id}"
    if sec_id not in SECTOR_CACHE:
        return {"found": False, "leads": []}
    return {"found": True, "leads": SECTOR_CACHE[sec_id]}

@app.post("/api/export/csv")
def export_leads_csv(leads: List[Dict[str, Any]]):
    """Exports audited leads to downloadable CSV format."""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # CSV Header
    writer.writerow([
        "Business Name", "Category", "Lead Status", "Lead Score",
        "Phone", "Website", "Issues / Audit Flaws", "Address", "Rating", "Reviews Count", "Cold Pitch Angle"
    ])

    for b in leads:
        flaws_str = " | ".join(b.get("audit", {}).get("flaws", []))
        writer.writerow([
            b.get("name", ""),
            b.get("category", ""),
            b.get("lead_status", ""),
            b.get("lead_score", ""),
            b.get("phone", ""),
            b.get("website", ""),
            flaws_str,
            b.get("address", ""),
            b.get("rating", ""),
            b.get("reviews_count", ""),
            b.get("audit", {}).get("pitch_angle", "")
        ])

    csv_data = output.getvalue()
    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=scouted_business_leads.csv"}
    )

# Static files mount
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    print(f"Launching India 3D Sector Business Scout on http://127.0.0.1:{PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
