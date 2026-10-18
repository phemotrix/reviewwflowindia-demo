"""
Automated Website Quality & Lead Scoring Engine
Analyzes business websites to determine if they are missing or 'crap'
(broken, slow, unsecure, not mobile friendly, parked domain, placeholder).
"""
import time
import re
import urllib.parse
from typing import Dict, Any, List
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PARKED_DOMAIN_SIGNATURES = [
    "godaddy.com", "dan.com", "sedo.com", "namecheap.com", "domain is parked",
    "buy this domain", "this domain is for sale", "under construction",
    "coming soon", "just another wordpress site", "default web site page",
    "cgi-sys/defaultwebpage.cgi", "apache2 ubuntu default page", "welcome to nginx",
    "website is under maintenance", "powered by wix.com free", "site suspended"
]

DIRECTORY_DOMAINS = [
    "facebook.com", "instagram.com", "justdial.com", "indiamart.com",
    "sulekha.com", "tradeindia.com", "linkedin.com", "yellowpages.in"
]

def audit_business_website(website_url: str = None) -> Dict[str, Any]:
    """
    Performs multi-criteria inspection of a business website:
    - Existence & reachability
    - SSL security
    - Mobile responsiveness (viewport check)
    - Parked / Default template detection
    - Directory redirect detection
    - Speed performance
    - Computes Lead Priority Score (0-100)
    """
    # 1. No Website Case
    if not website_url or not str(website_url).strip():
        return {
            "status": "NO_WEBSITE",
            "badge": "No Website",
            "score": 100,
            "color": "#ef4444", # Red
            "is_lead": True,
            "flaws": [
                "No website listed on public listings or maps",
                "Completely invisible to online search & organic local discovery",
                "100% reliant on foot traffic or third-party aggregators"
            ],
            "details": {
                "url": None,
                "ssl": False,
                "mobile_friendly": False,
                "response_time_ms": None,
                "status_code": None
            },
            "pitch_angle": "Build a modern, lightning-fast mobile-first website with local SEO to capture neighborhood customers searching on Google."
        }

    raw_url = str(website_url).strip()
    if not raw_url.startswith(("http://", "https://")):
        url = "https://" + raw_url
    else:
        url = raw_url

    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.lower()

    # 2. Directory or Social Media Only
    for dir_dom in DIRECTORY_DOMAINS:
        if dir_dom in domain:
            return {
                "status": "CRAP_WEBSITE",
                "badge": "Directory Only",
                "score": 88,
                "color": "#f97316", # Orange
                "is_lead": True,
                "flaws": [
                    f"Uses {dir_dom.split('.')[0].title()} portal instead of an independent brand website",
                    "Competitors are promoted directly alongside the business",
                    "Zero proprietary customer data or direct brand equity"
                ],
                "details": {
                    "url": url,
                    "ssl": True,
                    "mobile_friendly": True,
                    "response_time_ms": 120,
                    "status_code": 200,
                    "is_directory": True
                },
                "pitch_angle": f"Stop paying or feeding leads to {dir_dom.split('.')[0].title()} where competitors poach your clients. Own your custom domain and direct inquiries."
            }

    # 3. Live Technical Audit
    flaws: List[str] = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    start_t = time.time()
    try:
        resp = requests.get(url, headers=headers, timeout=6.0, verify=False, allow_redirects=True)
        latency_ms = int((time.time() - start_t) * 1000)
        status_code = resp.status_code
        html_text = resp.text.lower()
    except requests.exceptions.SSLError:
        latency_ms = int((time.time() - start_t) * 1000)
        return {
            "status": "CRAP_WEBSITE",
            "badge": "Broken SSL",
            "score": 92,
            "color": "#ef4444",
            "is_lead": True,
            "flaws": [
                "Invalid or expired SSL Certificate",
                "Browsers block visitors with aggressive 'Security Risk Ahead' warnings",
                "Severely penalizes Google SEO rank"
            ],
            "details": {
                "url": url,
                "ssl": False,
                "mobile_friendly": False,
                "response_time_ms": latency_ms,
                "status_code": "SSL_ERROR"
            },
            "pitch_angle": "Fix critical security warnings that are frightening away customers when they click your site."
        }
    except requests.exceptions.Timeout:
        return {
            "status": "CRAP_WEBSITE",
            "badge": "Server Timeout",
            "score": 94,
            "color": "#ef4444",
            "is_lead": True,
            "flaws": [
                "Server fails to respond (Timeout > 6 seconds)",
                "Prospective clients abandon slow unresponsive pages",
                "Host appears misconfigured or abandoned"
            ],
            "details": {
                "url": url,
                "ssl": False,
                "mobile_friendly": False,
                "response_time_ms": 6000,
                "status_code": "TIMEOUT"
            },
            "pitch_angle": "Your website host is constantly timing out. Upgrade to modern high-speed cloud hosting with zero downtime."
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": "CRAP_WEBSITE",
            "badge": "Broken Link",
            "score": 96,
            "color": "#ef4444",
            "is_lead": True,
            "flaws": [
                "Domain unreachable or DNS failed to resolve",
                "Website produces connection refusal errors",
                "Completely dead link listed on business profile"
            ],
            "details": {
                "url": url,
                "ssl": False,
                "mobile_friendly": False,
                "response_time_ms": None,
                "status_code": "DEAD_CONNECTION"
            },
            "pitch_angle": "Your listed web link is completely dead. We can restore a live, functional presence immediately."
        }

    # Analyze Status Code
    if status_code >= 400:
        flaws.append(f"HTTP Error {status_code} returned to visitors")
    
    # Check SSL
    is_ssl = resp.url.startswith("https://")
    if not is_ssl:
        flaws.append("Unencrypted HTTP protocol (Chrome marks site as 'Not Secure')")

    # Check Latency
    if latency_ms > 3500:
        flaws.append(f"Very slow loading speed ({latency_ms} ms)")

    # Check Parked / Under Construction Domain
    is_parked = False
    for sig in PARKED_DOMAIN_SIGNATURES:
        if sig in html_text:
            is_parked = True
            flaws.append(f"Contains placeholder or parked domain signal ('{sig}')")
            break

    # Parse HTML Structure for Mobile Friendly & Content
    soup = BeautifulSoup(resp.content, "html.parser")
    viewport = soup.find("meta", attrs={"name": re.compile(r"^viewport$", re.I)})
    is_mobile_friendly = viewport is not None

    if not is_mobile_friendly:
        flaws.append("Missing mobile viewport tag (Unreadable and zoomed-out on mobile devices)")

    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    if not title or len(title) < 4:
        flaws.append("Missing or unconfigured page <title> (Critical SEO issue)")

    # Compute Final Verdict
    if status_code >= 400 or is_parked or len(flaws) >= 2 or not is_mobile_friendly:
        score = 80 + min(len(flaws) * 5, 18)
        badge = "Parked Domain" if is_parked else ("No Mobile View" if not is_mobile_friendly else "Crap Website")
        return {
            "status": "CRAP_WEBSITE",
            "badge": badge,
            "score": score,
            "color": "#f59e0b", # Amber/Orange
            "is_lead": True,
            "flaws": flaws,
            "details": {
                "url": url,
                "ssl": is_ssl,
                "mobile_friendly": is_mobile_friendly,
                "response_time_ms": latency_ms,
                "status_code": status_code,
                "page_title": title[:60]
            },
            "pitch_angle": f"Overhaul legacy site: resolve {flaws[0] if flaws else 'design issues'} and transform it into a responsive, modern sales channel."
        }
    else:
        return {
            "status": "GOOD_WEBSITE",
            "badge": "Active / Decent",
            "score": 25,
            "color": "#10b981", # Green
            "is_lead": False,
            "flaws": flaws,
            "details": {
                "url": url,
                "ssl": is_ssl,
                "mobile_friendly": is_mobile_friendly,
                "response_time_ms": latency_ms,
                "status_code": status_code,
                "page_title": title[:60]
            },
            "pitch_angle": "Offer advanced digital marketing, SEO enhancement, or booking automation."
        }
