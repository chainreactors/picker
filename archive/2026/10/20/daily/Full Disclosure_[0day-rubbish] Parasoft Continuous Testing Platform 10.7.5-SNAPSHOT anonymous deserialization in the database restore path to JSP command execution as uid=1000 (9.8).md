---
title: [0day-rubbish] Parasoft Continuous Testing Platform 10.7.5-SNAPSHOT anonymous deserialization in the database restore path to JSP command execution as uid=1000 (9.8)
url: https://seclists.org/fulldisclosure/2026/Oct/31
source: Full Disclosure
date: 2026-10-20
fetch_date: 2026-10-21T06:51:04.387322
---

# [0day-rubbish] Parasoft Continuous Testing Platform 10.7.5-SNAPSHOT anonymous deserialization in the database restore path to JSP command execution as uid=1000 (9.8)

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

[![Previous](/images/left-icon-16x16.png)](30)
[By Date](date.html#31)
[![Next](/images/right-icon-16x16.png)](32)

[![Previous](/images/left-icon-16x16.png)](30)
[By Thread](index.html#31)
[![Next](/images/right-icon-16x16.png)](32)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Parasoft Continuous Testing Platform 10.7.5-SNAPSHOT anonymous deserialization in the database restore path to JSP command execution as uid=1000 (9.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 20 Oct 2026 02:31:02 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Parasoft
Continuous Testing Platform 10.7.5-SNAPSHOT, the closed-source commercial
continuous-testing, service-virtualisation and environment-management product
from Parasoft, a United States software-testing vendor headquartered in
Monrovia, California. The affected component is the em web application inside
the vendor's own container image, running on Tomcat 10.1.57 with Jasper and
Java 17. Three first-party defects compose into an unauthenticated
command-execution chain that needs two HTTP requests and nothing else: an
unfiltered ObjectInputStream over an uploaded backup archive, a licensing
filter that decides whether to run at all by testing the raw un-normalised
request URI, and a remember-me authentication service that hands an anonymous
request an authenticated administrator principal when no external security
provider has been configured.

Type and root cause. Unfiltered deserialization of attacker-controlled data,
CWE-502 primary, composed with an interpretation conflict in the licensing
filter, CWE-436 primary and co-equal with CWE-863 as its authorisation
consequence, and enabled by a fail-open authentication branch, CWE-287. The
honest count is three first-party defects rather than one, and that matters to
whoever fixes it, because the defect owners, the fixes and the independent
value to an attacker all differ.

The licensing defect. EMLicenseFilter is 175 lines and behaves as an
authorisation boundary, being what stops an unlicensed instance from serving
its administrative API. Its decision procedure reads the request URI raw at
line 165 and tests it at line 166 against a chain of exemption clauses
including endsWith("about"), endsWith("welcome"), endsWith("forgot"),
endsWith("notlicensed"), contains("/resources/") and contains("/images/"),
none of which is anchored by a separator or a segment boundary. A branch at
lines 167 to 171 additionally reassigns the whole exemption set rather than
accumulating into it when the request accepts JSON. The test has exactly one
consumer in the class: shouldNotFilter() at line 47 calling isLicenseRequired()
at line 48. So a matching URI does not weaken one decision, it suppresses the
entire doFilterInternal() body, including the /tdm/api/v guard at line 99 and
the unlicensed-instance redirect to /em/license at line 118. Because a servlet
container strips semicolon-delimited path parameters from each segment before
it performs servlet mapping, the filter and the router disagree about the
identity of one request: a target of /em/database/restore;welcome is exempted
by the filter and still routed to the restore handler by the container. That
disagreement is the textbook shape of CWE-436. Measured read-only on a live
instance, with the control that carries the argument:

    GET /em/database/currentConfig
        -> 302, Location: /em/license, zero-length body
    GET /em/database/currentConfig;welcome
        -> 200, 204 bytes, application/json;charset=utf-8, disclosing the
           schema version, the HyperSQL type, the database user and the
           jdbc:hsqldb:file URL of the platform's own database files
    GET /em/database/currentConfig;about
        -> the same 200/204, so this is the clause list and not one word
    GET /em/database/currentConfigwelcome     (no semicolon)
        -> 404, 792 bytes
    GET /em/tdm/api/v2/servers;welcome
        -> 200, 160 bytes, a well-formed serversResponse XML document with an
           empty servers element, so Jersey routed and ran the resource method
    the same pair over TLS
        -> 200/204 with the bypass and 302/0 without it, so the HTTPS
           listener is an equivalent surface and not a redirect shell

The no-semicolon control is the load-bearing row: the only variable that
changed is the presence of a semicolon path parameter, and the outcome flipped
from a licensing redirect to a 200 carrying live database configuration to a
caller who had never authenticated. The bypass is not a skeleton key, and that
was measured rather than assumed: handlers performing their own licensing
check are unaffected, the coverage-agent endpoints reading the license manager
directly and continuing to return 403 with a 90-byte unlicensed body across all
seventeen of their mappings even with the bypass applied, while a server-resource
feature gate kept returning 403 with a 94-byte body. What the bypass unlocks is
everything whose enforcement lives only in the filter, which includes the whole
/em/database subtree and the entire /em/tdm/api/v version tree. One related
first-party defect sits in the same filter and matters for detection: line 113
flushes the response output stream and line 115 then calls setStatus(403), so
licence refusals surface as HTTP 200 with a JSON body carrying status 403,
which makes them invisible to any status-based monitoring.

The deserialization defect. The restore path lands in
com.parasoft.ctp.core.database.backup.AbstractDatabaseBackup, a class of 518
lines and 19,851 bytes:

    :14   import java.io.ObjectInputStream;
    :111  ObjectInputStream ois = new ObjectInputStream(in);
    :112  int numTables = ois.readInt();
    :117  TableMetadata tableMetadata = (TableMetadata) ois.readObject();
    :126  Connection connection = this.provider.getConnection();

where in is the database.ser member of an uploaded zip. Three properties are
decisive. The cast is applied to whatever readObject() returned, so it
constrains nothing: the gadget executes during the call and the
ClassCastException is thrown afterwards. getConnection() sits nine lines
lower, so no database needs to exist, to be reachable or to accept the supplied
parameters for the payload to have already run, which makes that ordering the
cheapest structural fix available and one needing no understanding of gadget
chains. And the int read at line 112 is consumed before the object read. The
caller is the web-layer controller EMDatabaseController, 1359 lines, whose
restore handler at line 707 or 708 takes a StandardMultipartHttpServletRequest
and hard-compares zip member names against the literals "version.txt" at line
725 and "database.ser" at line 733, a shape check that says nothing about
content. The absence of any filter is not an inference from one search: in the
whole shipped product ObjectInputStream appears in 68 files with 149 occurrences
in the core tree and in 3 files in the web layer, readObject appears in 81
files, and ObjectInputFilter appears in 0 files, jdk.serialFilter in 0 files and
serialFilter in 0 files. Three zeros, across a class name, a system property and
its short alias, in an image unpacked and searched as artefacts against a
positive control of 81 files containing readObject, is a strong result: the
product has no deserialization filtering anywhere in its construction. Two
sibling readObject() calls on the same class of untrusted stream sit...