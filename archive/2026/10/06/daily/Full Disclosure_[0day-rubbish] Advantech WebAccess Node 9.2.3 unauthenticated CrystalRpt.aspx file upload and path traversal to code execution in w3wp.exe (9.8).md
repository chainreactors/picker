---
title: [0day-rubbish] Advantech WebAccess Node 9.2.3 unauthenticated CrystalRpt.aspx file upload and path traversal to code execution in w3wp.exe (9.8)
url: https://seclists.org/fulldisclosure/2026/Oct/2
source: Full Disclosure
date: 2026-10-06
fetch_date: 2026-10-07T07:55:42.015988
---

# [0day-rubbish] Advantech WebAccess Node 9.2.3 unauthenticated CrystalRpt.aspx file upload and path traversal to code execution in w3wp.exe (9.8)

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Advantech WebAccess Node 9.2.3 unauthenticated CrystalRpt.aspx file upload and path traversal to code execution in w3wp.exe (9.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 5 Oct 2026 17:52:23 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Advantech
WebAccess Node 9.2.3, the closed-source industrial SCADA/HMI web server from
Advantech (Taiwan).

Type: unrestricted file upload (CWE-434) compounded by path traversal (CWE-22), on
a page that performs no authorization decision at all (CWE-306). CWE-73 and CWE-862
also map; CWE-250/CWE-269 apply conditionally where the pool runs at high
privilege. In the WaCrpt ASP.NET Web Forms application served under
/broadweb/WaCrpt/, the fileSubmit_Click handler in bin\WaCrpt.dll concatenates two
attacker-supplied form fields into
Server.MapPath("~/report/" + projName + "_" + nodeName + "/"), gates the result on
nothing but Directory.Exists(rptDirPath), then calls FileUpload1.SaveAs(filePath)
with no extension validation - and does so before it attempts to open the file as a
Crystal Report. Reordering those two calls alone would break the chain.

The traversal rides in nodeName rather than in the uploaded filename, because
ASP.NET already strips any client-side directory from the multipart filename.
Sending nodeName = \..\..\ normalises the destination to the WaCrpt application
root, a directory that always exists, so the provisioning check is satisfied with no
report project created and no report directory present; ASP.NET request validation
inspects for HTML-dangerous sequences and not for backslash or dot-dot, so nothing
filters it. The bound is exactly two dot-dot levels - three or more are refused with
HttpException "Cannot use a leading .. to exit above the top directory".

The chain is three HTTP requests plus a follow-on GET. Request 1 harvests
__VIEWSTATE (1056 bytes) and __EVENTVALIDATION (92 bytes) while establishing the
traversed destination. Request 2 posts a 510-byte ASP.NET page as FileUpload1 with
fileSubmit=Upload; SaveAs writes it into the application root, ReportDocument.Load
then throws and the server returns HTTP 500 - a red herring, since the write already
completed. Request 3 GETs the written page, which the build manager compiles on first
request and executes inside w3wp.exe, running cmd.exe /c with captured stdout. No
credentials, no user interaction, no race window, no memory corruption, no prior
server state. A User-Agent header is mandatory: without one the CrystalDecisions
viewer control throws a NullReferenceException, the form never renders and the chain
stalls at step 1 - a trap that makes an unaffected conclusion easy to reach wrongly.

Authentication. No authorization decision exists anywhere in the application, and
that half is artifact-proven: Page_Load performs no session, cookie, token or
principal check and carries no auth filter, and its failure branch is a
Response.Redirect to the login page - a navigation aid, not an access denial. The
shipped WaCrpt Web.config declares an authentication mode but has no authorization
deny rule and no custom authentication module; there is no global.asax in the
directory; eight sibling files in the module call a session-existence check and
CrystalRpt.cs is not among them. The omission signature is decisive: addTemplate.cs,
the SECOND report-upload handler in the same module, enforces a case-insensitive
.RPT comparison while CrystalRpt.cs enforces nothing. The product has a working
mechanism - waconfig90 controllers carry an auth filter with session plus csrfToken
validation - and this page is not enrolled in it.

The one gap, stated as a gap: whether IIS delivers an anonymous request to the
WaCrpt application path lives in the site's applicationHost.config, and no such
excerpt, no installer-authored IIS fragment and no vendor documentation of that
factory setting was obtained. PR:N is published on a structural argument plus lab
reproduction, not on an extracted artifact - the product's own operator login page
cannot function unless the hosting site accepts anonymous requests, and it is served
by the same IIS site. An administrator who disabled anonymous authentication on that
path, or fronted it with an authenticating gateway, is not exposed on this vector,
and the conditional score below prices exactly that.

Scoring. All three readings the analysis priced are published:
- PRIMARY, 9.8 Critical, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- CONDITIONAL, 8.8 High, CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H, applying
  where IIS authentication is enforced on the WaCrpt application path or an
  authenticating gateway fronts it; nothing else in the finding changes.
- REJECTED, 8.1 High, CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H, considered
  because the traversal depth and the mandatory User-Agent are non-obvious and
  rejected because both are fixed constants under the attacker's control, which is
  not the CVSS 3.1 meaning of AC:H.
Scope is Unchanged deliberately: the compromise executes as the pool identity of the
vulnerable product's own web application, so the gain crosses a privilege level, not
a component's security scope. S:C on the same impact values would compute to 10.0
and is not claimed.

On scoring accuracy: the primary vector computes to ISS 0.914816, Impact under S:U of
5.873119, Exploitability 3.887043 and base 9.760161495, which the CVSS 3.1 Roundup
rule renders as 9.8. The figure the research record carried for this finding is the
figure its own vector computes, so no correction was required. We say so because
several earlier advisories in this repository carried recorded scores that did not
compute for their recorded vectors; those are being recomputed rather than copied.

Impact. Confidentiality High: full read of the product's configuration, the SCADA
project tree it serves and database connection material - these nodes routinely hold
the point list, alarm configuration and historian data for the monitored process.
Integrity High: a generic write primitive placing an attacker-named file with
attacker-chosen content into a served, script-executing directory, plus arbitrary
command execution, making product binaries, configuration, the report tree, tag and
alarm data and host state modifiable; manipulation of served HMI content, tag values
and alarm thresholds is why this is an operational-technology incident and not only
a web-application one. Availability High: the web tier, the SCADA runtime it fronts
and the host can be stopped or corrupted, removing operator visibility of the
monitored process even where the controlled process keeps running.

Execution identity caveat. The verified identity was nt authority\system with
SeTcbPrivilege, SeDebugPrivilege, SeImpersonatePrivilege and SeBackupPrivilege
enabled - the full SYSTEM set - but that was the VERIFICATION application pool,
configured in the lab as LocalSystem. No shipped pool identity is asserted: the
installer binds broadweb to DefaultAppPool and a separate helper writes the pool's
IdentityType at install time, a value that could not be resolved from static
strings. The rating does not depend on it, since C:H/I:H/...