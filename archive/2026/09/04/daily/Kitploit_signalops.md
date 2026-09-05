---
title: signalops
url: https://kitploit.com/en/tools/github/emrekybs/signalops
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:18.377622
---

# signalops

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

signalops — All-source intelligence fusion dashboard — WiFi, cellular, CCTV, ADS-B, orbital & SDR feeds unified into a single tactical map. Security research only. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/emrekybs/signalops

![](https://assets.kitploit.com/production/public/tools/54072/ddf5b344b36350f52d69502c52d06a82e044a72b519fddf7d4c840470cbda4f7-display-v1.webp)

[OSINT (Open Source Intelligence)](/en/categories/osint)[Reconnaissance](/en/categories/reconnaissance)[IoT Security](/en/categories/iot-security)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Information Gathering](/en/categories/information-gathering)[Network Security](/en/categories/network-security)[Wireless Security](/en/categories/wireless-security)[Mobile Security](/en/categories/mobile-security)[Threat Intelligence](/en/categories/threat-intelligence)[Crawler](/en/categories/crawler)[AI Security](/en/categories/ai-security)

2281 month ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![GitHub](/providers/github.png)

emrekybs/signalops

# signalops

All-source intelligence fusion dashboard — WiFi, cellular, CCTV, ADS-B, orbital & SDR feeds unified into a single tactical map. Security research only.

[View Repository](https://github.com/emrekybs/signalops)

# Signal OPS

A full-spectrum, all-source signal intelligence fusion platform for security research and training. Signal OPS pulls dozens of open collection sources — WiFi/Bluetooth/cell-tower databases, internet-exposure scanners, camera indexes, ADS-B flight feeds, satellite TLE tracking, and SDR/APRS networks — into a single tactical map and Flask API, correlating the RF, cellular, airspace, orbital, and surveillance domains into one real-time operational picture, with optional AI-assisted threat summaries layered on top.

---

## Features

* **Unified RF/OSINT scan** — one call fans out to WiFi, Bluetooth, cell-tower, IoT, camera, and aircraft sources in parallel, deduplicates, and scores results.
* **Camera discovery** — Shodan, FOFA, BinaryEdge, Windy Webcams, OpenStreetMap surveillance nodes, and Insecam, by coordinates or by country.
* **Cellular intelligence** — cell-tower lookups (WiGLE, OpenCellID) with offline MCC/MNC → operator/country resolution and IMSI-catcher / Stingray heuristics.
* **Wireless threat detection** — rogue / evil-twin access point detection and Bluetooth tracker (AirTag, Tile, SmartTag…) identification.
* **Airspace monitoring** — live ADS-B via adsb.fi and OpenSky, emergency-squawk decoding, drone heuristics, and a GPS-jamming heatmap derived from aircraft NAC-P.
* **Orbital tracking** — CelesTrak TLE ingestion with SGP4 propagation, mission classification, and SatNOGS ground-station overlay.
* **SDR & APRS** — public KiwiSDR receiver map and APRS.fi station lookups.
* **IP threat intelligence** — multi-source aggregation (ipinfo, AbuseIPDB, CriminalIP, LeakIX, ZoomEye) with a lightweight port scan and combined risk scoring.
* **Watchlist & alerts** — track specific BSSIDs, SSIDs, IPs, MACs, or ICAO hexes and get hits during scans.
* **AI analysis (optional)** — Google Gemini summarizes scan results into assessments and risk levels when a key is provided.

Almost every source is **optional**. If a key isn't set, that fetcher is skipped gracefully — the free sources (OpenStreetMap, Insecam, ipinfo.io, ADS-B, CelesTrak, KiwiSDR) work with no keys at all.

---

## Screenshots

### SIGINT Map — unified multi-source view

The main map fuses WiFi, Bluetooth, cell, camera, and aircraft layers over the same area, with toggleable overlays for OSM cameras, ALPR/Flock networks, and police precincts.

![SIGINT Map — satellite view](https://assets.kitploit.com/production/public/readmes/54072/4f9bda2f62a0f557ba4ef743896a29e106e943d874c9b0d20b07a185a4144292/231a29d9ecbb92f2eb4741e90ae7c0608a531f1d9ed9230d0db2566d390fd997-display-v1.webp)

![SIGINT Map — street view with camera / AP / cell markers](https://assets.kitploit.com/production/public/readmes/54072/3b681192deb2a37c435d5ad0c4628b0be84370621f06542a0a172bc98e3e0f9d/5f368555fb10579afe4954e89de76ccb018f6b6775ecf992dbb2aac4e79b95c3-display-v1.webp)

### Surveillance & CCTV

| Surveillance feed | CCTV discovery |
| --- | --- |
| ![Surveillance](https://assets.kitploit.com/production/public/readmes/54072/e1e4a0e5cc54ed0a2c4da4f4b7f41240430f448c78572568aed96a8c8208d837/4f0005e13f9aa907f785ee40c857a62f954f9223fc5a868a77fb8f6addaa5c3d-display-v1.webp) | ![CCTV](https://assets.kitploit.com/production/public/readmes/54072/ddf5b344b36350f52d69502c52d06a82e044a72b519fddf7d4c840470cbda4f7/bcf4996006c3406dedbf70b090c9327e71bbc9b5ff2144f6091fa22b4a313a9f-display-v1.webp) |

The surveillance list scores each device (e.g. *"Suspicion 35/100: Unauthenticated camera"*) and merges routers, TVs, and exposed cameras from WiGLE, Insecam, and OSM. The CCTV view groups discovered cameras by source with per-camera risk and live/metadata status.

### Cell Tower Intelligence & SDR / APRS

| Cell tower heatmap | SDR / APRS network |
| --- | --- |
| ![Cell towers](https://assets.kitploit.com/production/public/readmes/54072/4d95016218de7fb6d87bac939f0c7e071b185ef4e8934e630b18637c3ca48e5d/d9a707af21ecce418a0caca8e93f17f02576b489077809a993342f02ca5470e1-display-v1.webp) | ![SDR / APRS](https://assets.kitploit.com/production/public/readmes/54072/5c081781cf88ee130ac1d30f00d05a9a504b9e94311ff803f4eaaa872f61efda/67ede11614ab5c77ab2fa250dadc70f8187cfd6293b17ce1e6f7dc02dd0f63f7-display-v1.webp) |

## Cell-tower intelligence plots tower density with MCC/MNC operator lookup; the SDR view maps public KiwiSDR receivers and APRS stations with callsign lookup.

## Requirements

* Python 3.9+
* The Python packages listed below

Core dependencies:

root@kitploit:~

```
flask
requests
python-dotenv
```

Recommended (enables full functionality — caching, rate limiting, satellite propagation):

root@kitploit:~

```
cachetools        # bounded geo-cache (falls back to an unbounded dict if missing)
flask-limiter     # request rate limiting
sgp4              # satellite position propagation for /api/satellites
google-genai      # Gemini AI analysis (only if you use GEMINI_API_KEY)
```

Install everything:

root@kitploit:~

```
pip install flask requests python-dotenv cachetools flask-limiter sgp4 google-genai
```

---

## Setup

### 1. Clone and enter the project

root@kitploit:~

```
git https://github.com/emrekybs/signalops.git
unzip signalops-v1.zip
```

### 2. (Optional) create a virtual environment

root@kitploit:~

```
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

root@kitploit:~

```
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, use the `pip install` line from the Requirements section above.

### 4. Configure your environment

Copy the example file and fill in the keys you have:

root@kitploit:~

```
cp .env.example .env
```

Then open `.env` and paste in your API keys. **Every key is optional** — leave an...