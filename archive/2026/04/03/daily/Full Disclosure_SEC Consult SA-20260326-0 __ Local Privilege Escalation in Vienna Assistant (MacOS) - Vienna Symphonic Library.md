---
title: SEC Consult SA-20260326-0 :: Local Privilege Escalation in Vienna Assistant (MacOS) - Vienna Symphonic Library
url: https://seclists.org/fulldisclosure/2026/Apr/3
source: Full Disclosure
date: 2026-04-03
fetch_date: 2026-04-04T04:17:51.709494
---

# SEC Consult SA-20260326-0 :: Local Privilege Escalation in Vienna Assistant (MacOS) - Vienna Symphonic Library

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260326-0 :: Local Privilege Escalation in Vienna Assistant (MacOS) - Vienna Symphonic Library

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 26 Mar 2026 10:39:40 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260326-0 >
=======================================================================
              title: Local Privilege Escalation
            product: Vienna Assistant (MacOS) - Vienna Symphonic Library
 vulnerable version: 1.2.542
      fixed version: -
         CVE number: CVE-2026-24068
             impact: high
           homepage:https://www.vsl.co.at/
              found: 2026-01-10
                 by: Florian Haselsteiner (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"We make products, tools and services that enable all creators and musicians
to express their deepest emotions through technology, designed to augment
their passion for music and musicality.

Since all of us here at Vienna Symphonic Library are educated musicians,
simply passionate about music, or both, we know that every piece of work –
a song for a birthday party, a commercial jingle or a new film score –
requires your full attention and energy. That’s why we design our products
and services to alleviate the burden of unwanted tasks so that you can
concentrate on what you enjoy most and get the job done."

Source:https://www.vsl.co.at/company/vision

Business recommendation:
------------------------
The vendor was unresponsive and did not respond to any of our communication
attempts. Therefore, a patch is not available. In case you are using this
product, please approach the vendor and demand a fix.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Missing XPC Client & NSXPC endpoint validation leads to privilege escalation (CVE-2026-24068)
The VSL privileged helper does utilize NSXPC for IPC. The implementation of
the "shouldAcceptNewConnection" function, which is used by the NSXPC framework
to validate if a client should be allowed to connect to the XPC listener,
does not validate clients at all.

-----------------------------------
1000060b0    bool -[HelperTool listener:shouldAcceptNewConnection:](struct HelperTool* self, SEL sel, id listener, id
shouldAcceptNewConnection)
1000060b0    {
1000060b0        _NSLog(@"New Listener");
1000060fc        [shouldAcceptNewConnection setExportedInterface:[clsRef_NSXPCInterface
1000060fc            interfaceWithProtocol:protoRef_HelperToolProtocol]];
100006110        [shouldAcceptNewConnection setExportedObject:self];
100006120        [shouldAcceptNewConnection resume];
100006130        return 1;
1000060b0    }
-----------------------------------
This means that any process can connect to this service using the configured
protocol. A malicious process is able to call all the functions defined in
the corresponding HelperToolProtocol.

No validation is performed in the functions "writeReceiptFile" and "runUninstaller"
of the HelperToolProtocol. This allows an attacker to write files to any
location with any data as well as execute any file with any arguments.
Any process can call these functions because of the missing XPC client validation
described before. The abuse of the missing endpoint validation leads to privilege
escalation.

Proof of concept:
-----------------
1) Missing XPC Client & NSXPC endpoint validation leads to privilege escalation (CVE-2026-24068)
To exploit the missing XPC client validation an attacker only has to define the
same Objective C protocol and start a connection to the privileged helper XPC
service. The attacker can then use any function available in the defined
protocol. The HelperToolProtocol has the functions writeReceiptFile and
runUninstaller defined, which both do not perform validation of their arguments.
The function runUninstaller can be exploited to execute bash commands as root.
The following Objective C code implements the exploit:

-----------------------------------
[ PoC exploit code removed ]
-----------------------------------

The proof of concept code can be compiled using the following command:
-----------------------------------
clang -o exploit -framework Foundation ./exploit.mm
-----------------------------------

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
* 1.2.542

Vendor contact timeline:
------------------------
2026-01-21: Contacting vendor throughsupport () vsl co at; no response.
2026-02-03: Contacting vendor again throughsupport () vsl co at; no response.
2026-02-24: Vendor Website (https://www.vsl.co.at/) down.
2026-02-25: Contacted vendor throughsupport () vsl co at andoffice () vsl co at;
            no response
2026-03-24: Contacting vendor again, informing them about public release on
            26th March.
2026-03-26: Public release of advisory.

Solution:
---------
The vendor was unresponsive and did not respond to any of our communication
attempts. Therefore, a patch is not available. In case you are using this
product, please approach the vendor and demand a fix.

Workaround:
-----------
None

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos business
Europe | Asia

About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Atos business. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulnerabilities
and valid recommendation about the risk profile of new technologies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Interested to work with the experts of SEC Consult?
Send us your applicationhttps://sec-consult.com/career/

Interested in improving your cyber security with the experts of SEC Consult?
Contact our local officeshttps://sec-consult.com/contact/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mail: security-research at sec-consult dot com
Web:https://www.sec-consult.com
Blog:https://blog.sec-consult.com
X:https://x.com/sec_consult

EOF Florian Haselsteiner / @2026
```

**Attachment:
[smime.p7s](att-3/smime_p7s.bin)**
*Description:* S/MIME Cryptographic Signature

```
_______________________________________________
Sent through the Ful...