---
title: SEC Consult SA-20230117-1 :: Pre-authenticated Remote Code Execution via Java frontend and QDS endpoint in @OpenText Content Server component of OpenText Extended ECM
url: https://seclists.org/fulldisclosure/2023/Jan/13
source: Full Disclosure
date: 2023-01-21
fetch_date: 2025-10-04T04:31:13.523958
---

# SEC Consult SA-20230117-1 :: Pre-authenticated Remote Code Execution via Java frontend and QDS endpoint in @OpenText Content Server component of OpenText Extended ECM

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20230117-1 :: Pre-authenticated Remote Code Execution via Java frontend and QDS endpoint in @OpenText Content Server component of OpenText Extended ECM

---

*From*: "SEC Consult Vulnerability Lab, Research via Fulldisclosure" <fulldisclosure () seclists org>
*Date*: Tue, 17 Jan 2023 13:44:57 +0000

---

```
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
the key `_REQUEST` of the incoming data. Normally this parameter is set by the
HTTP frontend (e.g. the `CGI` binary `cs.exe` or `Java` application servlet) to
`llweb`.

There is a bug in the `Java` application server, found in
`%OT_BASE%/application/cs.war`, which allows an attacker to actually set the
value of the key `_REQUEST` to an arbitrary value and bypass the authorization
checks.

Most of the endpoints cannot be called, because they require specific data types
of the incoming data, which can not be controlled by the attacker. Only strings
are supported. But a few endpoints can be called which allow an attacker to create
files or execute arbitrary code on the server.

Proof of concept:
-----------------
1) Pre-authenticated Remote Code Execution via Java frontend and QDS endpoint (CVE-2022-45927)
To be able to set the value of the `_REQUEST` parameter the attacker has to
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
8:10:5,'COMMENT'='created','ContentType'=?,'CREATEDATE'=D/2022/9/28:8:10:5,'CREATEDBY'=1000,'DataID'=51982,'DATELASTMODIFY'=D/2022/9/28:8:10:5,'EXATT1'=?,'EXATT2'=?,'EXTENDEDDATA'=?,'GROUPPERM'=128,'location'=E648871951,'MAJOR'=?,'MAXVERSION'=-1,'MINOR'=?,'Name'='qds-create-poc.txt','nextURL'=E648871951,'Node'=A<1,?,'AssignedTo'=?,'CacheExpiration'=0,'Catalog'=0,'ChildCount'=0,'CreateDate'=D/2022/9/28:8:10:5,'CreatedBy'=1000,'DataID'=51982,'DataType'=?,'DateAssigned'=?,'DateCompleted'=?,'DateDue'=?,'DateEffective'=?,'DateExpiration'=?,'DateStarted'=?,'DCategory'=?,'DComment'='created','Deleted'=0,'ExAtt1'=?,'ExAtt2'=?,'ExtendedData'=?,'ExternalCreateDate'=?,'ExternalCreatorID'=?,'ExternalModifyDate'=?,'ExternalSourceID'=?,'GIF'=?,'GPermissions'=128,'GroupID'=999,'GUID'='@[537A1229-E0F5-45EE-A3F2-D7F91EE6CBBC]','Major'=?,'MaxVers'=-1,'Minor'=?,'ModifiedBy'=1000,'ModifyDate'=D/2022/9/28:8:10:5,'Multilingual'=V{<'LanguageCode','Name','DComment'><'de','qds-create-poc.txt','created'>},'Name'='qds-create-poc.txt','Ordering'=?,'OriginDataID'=0,'OriginOwnerID'=0,'OwnerID'=-2004,'ParentID'=2004,'PermID'=?,'Priority'=?,'ReleaseRef'=?,'Reserved'=0,'ReservedBy'=0,'ReservedDate'=?,'SPermissions'=16777215,'Status'=?,'SubType'=144,'UPermissions'=16777215,'UserID'=1000,'VersionNum'=1,'WPermissions'=128>,'OK'=true,'ORDERING'=?,'ORIGINALID'=0,'ORIGINALVOLID'=0,'PARENTID'=2004,'PERMISSIONS'=-2130706433,'PermsOK'=true,'Public'=false,'RELEASEREF'=?,'RESERVED'=0,'RESERVEDBY'=0,'RESERVEDDATE'=?,'SUBTYPE'=144,'SYSTEMPERM'=16777215,'USERID'=1000,'USERPERM'=16777215,'VERSION'=A<1,?,'DataSize'=6,'DocID'=51982,'ExternalCreateDate'=?,'ExternalCreatorID'=?,'ExternalModifyDate'=?,'ExternalSourceID'=?,'FileCDate'=D/2022/9/28:8:10:5,'...