---
title: OpenText Extended ECM 22.3 Java Frontend Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023010037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-23
fetch_date: 2025-10-04T04:35:23.775408
---

# OpenText Extended ECM 22.3 Java Frontend Remote Code Execution

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
|  |  | |  | | --- | | **OpenText Extended ECM 22.3 Java Frontend Remote Code Execution** **2023.01.22**  Credit:  **[Armin Stock](https://cxsecurity.com/author/Armin%2BStock/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-45927](https://cxsecurity.com/cveshow/CVE-2022-45927/ "Click to see CVE-2022-45927")**  CWE: **N/A** | |

SEC Consult Vulnerability Lab Security Advisory < 20230117-1 >
=======================================================================
title: Pre-authenticated Remote Code Execution via Java frontend
and QDS endpoint
product: OpenText™ Content Server component of OpenText™ Extended ECM
vulnerable version: 20.4 - 22.3
fixed version: 22.4
CVE number: CVE-2022-45927
impact: Critical
homepage: https://www.opentext.com
found: 2022-09-16
by: Armin Stock (Atos)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"OpenText™ Extended ECM is an enterprise CMS platform that securely governs the
information lifecycle by integrating with leading enterprise applications, such
as SAP®, Microsoft® 365, Salesforce and SAP SuccessFactors®. Bringing content
and processes together, Extended ECM provides access to information when and
where it’s needed, improves decision-making and drives operational effectiveness."
Source: https://www.opentext.com/products/extended-ecm
Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.
Vulnerability overview/description:
-----------------------------------
1) Pre-authenticated Remote Code Execution via Java frontend and QDS endpoint (CVE-2022-45927)
The `QDS` endpoints of the `Content Server` are not protected by the normal
user management functionality of the `Content Server`, but check the value of
the key `\_REQUEST` of the incoming data. Normally this parameter is set by the
HTTP frontend (e.g. the `CGI` binary `cs.exe` or `Java` application servlet) to
`llweb`.
There is a bug in the `Java` application server, found in
`%OT\_BASE%/application/cs.war`, which allows an attacker to actually set the
value of the key `\_REQUEST` to an arbitrary value and bypass the authorization
checks.
Most of the endpoints cannot be called, because they require specific data types
of the incoming data, which can not be controlled by the attacker. Only strings
are supported. But a few endpoints can be called which allow an attacker to create
files or execute arbitrary code on the server.
Proof of concept:
-----------------
1) Pre-authenticated Remote Code Execution via Java frontend and QDS endpoint (CVE-2022-45927)
To be able to set the value of the `\_REQUEST` parameter the attacker has to
send the data via a `POST` request with a `Content-Type` of `multipart/form-data`.
This results in the following execution flow:
-------------------------------------------------------------------------------
[ Details removed, will be published at a later date ]
-------------------------------------------------------------------------------
The following request (using the `CGI` frontend) results in an unauthorized
response:
-------------------------------------------------------------------------------
[ PoC removed, will be published at a later date ]
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
<!-- Response -->
<div class="cs-form-container cs-form-message-container">
<div>
<div class="cs-form-line-text cs-form-message cs-form-message-error" title="Error" id="errMsg" >
<p>
Content Server Error:
</p>
<p>
The request did not come from XXX.
</p>
</div>
</div>
</div>
-------------------------------------------------------------------------------
Whereas using the `Java` application server results in the following response:
-------------------------------------------------------------------------------
HTTP/1.1 200
A<1,?,'ErrMsg'=?,'ErrMsgDetail'=?,'OK'=true,'QDSServerList'={}>Content-Type: text/html;charset=UTF-8
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: frame-ancestors 'self'
X-UA-Compatible: IE=edge
Content-Length: 0
Date: Tue, 27 Sep 2022 13:04:47 GMT
Connection: close
-------------------------------------------------------------------------------
Create new objects:
Using this bug it is possible to create objects in the `Content Server` without
known credentials and in the context of the super-admin user ( ID `1000` ), by
calling the endpoint `[ Details removed, will be published at a later date ]`.
-------------------------------------------------------------------------------
[ PoC removed, will be published at a later date ]
-------------------------------------------------------------------------------
The new object (subType = `145` text file) is created without providing cookies
and the `owner` attribute of this object is set to `1000` (super admin):
-------------------------------------------------------------------------------
HTTP/1.1 200
A<1,?,'CATEGORY'=?,'CloneTime'=D/2022/9/28:
8:10:5,'COMMENT'='created','ContentType'=?,'CREATEDATE'=D/2022/9/28:8:10:5,'CREATEDBY'=1000,'DataID'=51982,'DATELASTMODIFY'=D/2022/9/28:8:10:5,'EXATT1'=?,'EXATT2'=?,'EXTENDEDDATA'=?,'GROUPPERM'=128,'location'=E648871951,'MAJOR'=?,'MAXVERSION'=-1,'MINOR'=?,'Name'='qds-create-poc.txt','nextURL'=E648871951,'Node'=A<1,?,'AssignedTo'=?,'CacheExpiration'=0,'Catalog'=0,'ChildCount'=0,'CreateDate'=D/2022/9/28:8:10:5,'CreatedBy'=1000,'DataID'=51982,'DataType'=?,'DateAssigned'=?,'DateCompleted'=?,'DateDue'=?,'DateEffective'=?,'DateExpiration'=?,'DateStarted'=?,'DCategory'=?,'DComment'='created','Deleted'=0,'ExAtt1'=?,'ExAtt2'=?,'ExtendedData'=?,'ExternalCreateDate'=?,'ExternalCreatorID'=?,'ExternalModifyDate'=?,'ExternalSourceID'=?,'GIF'=?,'GPermissions'=128,'GroupID'=999,'GUID'='@[537A1229-E0F5-45EE-A3F2-D7F91EE6CBBC]','Major'=?,'MaxVers'=-1,'Minor'=?,'ModifiedBy'=1000,'ModifyDate'...