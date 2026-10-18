# 🇮🇳 Bharat 3D Biz Scout — Hyperlocal 100-Sector Lead Engine

> **A real-time 3D GIS application that divides any Indian State or Metropolitan District (like Mumbai into 100 sectors) using Google Maps 3D Vector Maps, and automatically harvests & audits local businesses lacking a website or with broken/substandard websites.**

---

## ⚡ What this App Does For You

1. **3D Interactive Map of India**:
   - Covers all Indian States (Maharashtra, Karnataka, Gujarat, Tamil Nadu, Uttar Pradesh, etc.) and Major Metro Districts (Mumbai, Delhi NCR, Bengaluru, Pune, Hyderabad, Chennai, Kolkata, Ahmedabad).
   - Real 3D building extrusions, vector rendering, camera tilt (up to 67.5°), and heading rotation.

2. **Automated Sector Subdivision**:
   - Subdivides Mumbai into **100 distinct sectors** (`SEC-001` to `SEC-100`) from Colaba and Marine Drive in South Mumbai to Dahisar, Borivali, Bandra West, BKC, Andheri, and Powai.
   - Each sector features contextual landmark labeling, bounding box calculation, and interactive polygon boundaries.

3. **Multi-Source Local Business Harvester**:
   - Queries **Google Places API (New)** and live **OpenStreetMap Overpass API** across the sector.
   - Extracts business name, category, phone number, physical address, Google rating, review count, and website URL.

4. **Automated "Crap Website" Quality Auditor**:
   - Immediately runs deep technical diagnostics on each business's listed website:
     - ❌ **No Website**: High-conversion lead (100% conversion priority).
     - ⚠️ **Broken SSL**: HTTP only or expired SSL security certificates.
     - ⚠️ **No Mobile Responsiveness**: Missing `<meta name="viewport">` tag (broken on mobile phones).
     - ⚠️ **Server Timeout / Dead Connection**: 404, 500, or DNS connection failure.
     - ⚠️ **Parked / Under-Construction**: Default GoDaddy, Namecheap, cPanel, or Wix template.
     - ⚠️ **Directory-Only**: Relies only on JustDial/Facebook/IndiaMART instead of an independent website.

5. **1-Click Cold Pitch & Outreach Generator**:
   - Generates personalized, high-converting outreach scripts tailored to the exact flaw found on their site.
   - Includes **Direct WhatsApp Web button** (`wa.me`) to message the business owner immediately.
   - One-click **CSV Lead Exporter** with all contacts and audit reports.

---

## 🚀 How to Run

### Option 1: Double-Click
Double-click `run.bat` in this folder. It will launch the server and automatically open `http://localhost:8000` in your browser.

### Option 2: Terminal
```bash
python app.py
```
Open [http://localhost:8000](http://localhost:8000) in any web browser.

---

## ⚙️ Google Maps API Key Setup

The app works right out of the box!
- To activate Photorealistic Google Maps 3D vector tiles and Google Places API (New):
  1. Click **"⚙️ Google Maps Key"** in the top navigation bar.
  2. Paste your API key (or mint a free [Google Maps Demo Key](https://mapsplatform.google.com/maps-demo-key?utm_campaign=gmp_git_agentskills_v1) with no billing setup needed).
  3. Click **Save & Reload Map**.
