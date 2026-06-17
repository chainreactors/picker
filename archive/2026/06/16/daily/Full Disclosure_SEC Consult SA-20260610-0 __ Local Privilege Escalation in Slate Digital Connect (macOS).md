---
title: SEC Consult SA-20260610-0 :: Local Privilege Escalation in Slate Digital Connect (macOS)
url: https://seclists.org/fulldisclosure/2026/Jun/7
source: Full Disclosure
date: 2026-06-16
fetch_date: 2026-06-17T07:04:08.132683
---

# SEC Consult SA-20260610-0 :: Local Privilege Escalation in Slate Digital Connect (macOS)

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260610-0 :: Local Privilege Escalation in Slate Digital Connect (macOS)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 10 Jun 2026 10:34:27 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260610-0 >
=======================================================================
              title: Local Privilege Escalation
            product: Slate Digital Connect (macOS)
 vulnerable version: 1.37.0
      fixed version: -
         CVE number: CVE-2026-24066, CVE-2026-24067
             impact: high
           homepage:https://app.completeaccess.audio/installers,https://slatedigital.com/
              found: 2026-01-09
                 by: Florian Haselsteiner (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Slate Digital was founded in 2008 with a mission to deliver exceptional audio
production tools to musicians, engineers, producers, and content creators. With
our extensive expertise and knowledge, we are constantly evolving to stay in
step with the changing needs of modern creatives. Our goal is to inspire and
empower individuals of all skill levels to do their best work and share it
with the world."

"Slate Digital Connect lets you install, activate, and update all Slate Digital
plugins. Whether you need a fresh install, to move to a new machine, or to grab
the latest updates, Slate Digital Connect handles downloads, licenses, and
upgrades automatically."

Source:https://slatedigital.com/about/ &https://app.completeaccess.audio/installers

Business recommendation:
------------------------
The vendor was unresponsive since January 2026 and a patch is not available.
Users of this software should contact the vendor support and demand a patch.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve
potential further security issues.

Vulnerability overview/description:
-----------------------------------
1) Local Privilege escalation by insufficient XPC Client validation (CVE-2026-24066)
The Slate Digital Connect App installs a helper tool during installation. The
helper tool namely `com.slatedigital.connect.privileged.helper.tool` is installed
into `/Library/PrivilegedHelperTools`. It offers the XPC service
`com.slatedigital.connect.privileged.helper.tool2`.

It was found that the client validation of the XPC service is insufficient.
The following snippet of the decompiled function "isValidClient" shows that
only a check regarding the subject.OU of the certificate is performed. It is
not verified that this certificate is signed by Apple.

-----------------------------------
100003050            if (_SecRequirementCreateWithString(
100003050                    @"certificate leaf[subject.OU] = "3F5JHDQ8FZ"", 0, &cf_2))
100003054                goto label_100003068;
-----------------------------------

This can be exploited by creating a self-signed certificate for code signing.
This enables attackers to craft their own self-signed certificate with the
corresponding subject.OU.

2) Insecure XPC Client validation via PID (CVE-2026-24067)
The function "isValidClient" gets the code signing information of the
connecting process by using its PID:
-----------------------------------
100002fbc        SecRequirementRef cf_2 = nullptr;
100002fcc        SecCodeRef var_28 = nullptr;
100002fd4        int32_t pid = _xpc_connection_get_pid();
100002fe0        CFAllocatorRef allocator = *(uint64_t*)_kCFAllocatorDefault;
100002ff4        CFNumberRef values = _CFNumberCreate(allocator, kCFNumberSInt32Type, &pid);
100003014        CFDictionaryRef cf = _CFDictionaryCreate(allocator, _kSecGuestAttributePid,
100003014            &values, 1, nullptr, nullptr);
100003038        bool z;
100003038
100003038        if (!_SecCodeCopyGuestWithAttributes(nullptr))
100003038            z = !var_28;
100003038        else
100003038            z = true;
100003038
10000303c        int64_t result;
10000303c        SecRequirementRef cf_1;
-----------------------------------

This is considered not secure, since it is possible to exploit this case
by exploiting PID reuse.

Proof of concept:
-----------------
1) Local Privilege escalation by insufficient XPC Client validation (CVE-2026-24066)
To exploit this issue a rogue code signing certificate must be created:
-----------------------------------
openssl genrsa -out codesign.key 4096

openssl req -new -x509 \
  -key codesign.key \
  -out codesign.crt \
  -days 3650 \
  -subj "/CN=My Self Signed Code Cert/OU=3F5JHDQ8FZ/O=Test Org/C=US" \
  -addext "keyUsage=digitalSignature" \
  -addext "extendedKeyUsage=codeSigning"

openssl pkcs12 -export \
  -inkey codesign.key \
  -in codesign.crt \
  -out codesign.p12
-----------------------------------

This codesign.p12 certificate can then be imported into the keychain.
The following C code has been crafted to exploit the PrivilegedHelperTool:
-----------------------------------
[ POC removed ]
-----------------------------------

This code was compiled by:
-----------------------------------
clang -o slateExploit main.c
-----------------------------------

and then signed with the crafted certificate created before:
-----------------------------------
codesign --sign "My Self Signed Code Cert" \
         --force \
         slateExploit
-----------------------------------

This executable can then be transferred to a target device and be executed as
shown in the screenshot ExploitProof.png

2) Insecure XPC Client validation via PID (CVE-2026-24067)
To exploit the insecure client validation via PID, the following Objective C
code can be used. The code first sends the desired XPC message and then
quickly changes the process to the benign binary, leading to the PID,
which will be used to check if the client should be allowed to connect
to the service or not, pointing to the benign client.

-----------------------------------
[ POC removed ]
-----------------------------------

The code can be compiled using clang:
-----------------------------------
clang -o slatepidexploit -framework foundation pidReuseSlate.c
-----------------------------------

The pid reuse attack will then be performed and the command defined
in the XPC message will be executed by root. This again enables several
vectors for local privilege escalation.

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
* 1.37.0

Vendor contact timeline:
------------------------
2026-01-21: Contacting vendor throughhttps://support.slatedigital.com/hc/en-us/requests/new?ticket_form_id=360000126927
2026-02-02: Contacting vendor by answering to the email received when
            creating a ticket. No response.
2026-02-24: Contacting vendor again through
tickethttps://support.slatedigital.com/hc/en-us/requests/new?ticket_fo...