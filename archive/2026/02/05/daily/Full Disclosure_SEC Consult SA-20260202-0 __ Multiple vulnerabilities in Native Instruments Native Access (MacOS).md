---
title: SEC Consult SA-20260202-0 :: Multiple vulnerabilities in Native Instruments Native Access (MacOS)
url: https://seclists.org/fulldisclosure/2026/Feb/4
source: Full Disclosure
date: 2026-02-05
fetch_date: 2026-02-06T04:10:23.637734
---

# SEC Consult SA-20260202-0 :: Multiple vulnerabilities in Native Instruments Native Access (MacOS)

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260202-0 :: Multiple vulnerabilities in Native Instruments Native Access (MacOS)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 2 Feb 2026 14:34:52 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260202-0 >
=======================================================================
              title: Multiple vulnerabilities
            product: Native Instruments - Native Access (MacOS)
 vulnerable version: verified up to 3.22.0
      fixed version: n/a
         CVE number: CVE-2026-24070, CVE-2026-24071
             impact: high
           homepage:https://www.native-instruments.com/en/specials/native-access/
              found: 2025-07-22
                 by: Florian Haselsteiner (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Native Instruments is a leading manufacturer of software and hardware
for computer-based audio production and DJing. In June of 2023, iZotope,
Plugin Alliance and Brainworx joined us in our mission to develop innovative,
fully-integrated solutions for every creative task, profession, and skill level."

Source:https://www.native-instruments.com/en/company/

Business recommendation:
------------------------
The vendor was unreachable and did not respond to multiple contact attempts.
No patch is available. Customers should contact the vendor and request a
patch.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Local Privilege Escalation via DYLIB Injection (CVE-2026-24070)
During the installation of the Native Access application, a privileged helper
`com.native-instruments.NativeAccess.Helper2`, which is used by Native Access
to trigger functions via XPC communication like copy-file, remove or
set-permissions, is deployed as well.

The communication with the XPC service of the privileged helper is only allowed
if the client process is signed with the corresponding certificate and
fulfills the following code signing requirement:
"anchor trusted and certificate leaf[subject.CN] = \"Developer ID Application: Native Instruments GmbH (83K5EG6Z9V)\""

The Native Access application was found to be signed with the
`com.apple.security.cs.allow-dyld-environment-variables` and
`com.apple.security.cs.disable-library-validation` entitlements leading to DYLIB
injection and therefore command execution in the context of this application.

A low privileged user can exploit the DYLIB injection to trigger functions of
the privileged helper XPC service resulting in privilege escalation by first
deleting the /etc/sudoers file and then copying a malicious version of that file
to /etc/sudoers.

2) XPC Client Validation via PID (CVE-2026-24071)
It was found that the XPC services uses the PID of the connecting client to
verify its code signature. This is considered insecure and can be exploited
by PID reuse attacks.

The connection handler function uses _xpc_connection_get_pid(arg2) as argument
for the hasValidSignature function. This value can not be trusted since it is
vulnerable to PID reuse attacks.
----------------------------------------------------------------------------
10000a60c    int64_t ___main_block_invoke(int64_t arg1, xpc_object_t arg2)

10000a630        if (_xpc_get_type(object: arg2) != __xpc_type_connection)
10000a64c            return _syslog$DARWIN_EXTSN(5, "Unexpected type")
10000a64c
10000a65c        if ((hasValidSignature(_xpc_connection_get_pid(arg2)) & 1) == 0)
10000a66c            _syslog$DARWIN_EXTSN(5, "Refused connection from client with bad signature")
10000a674            _xpc_connection_cancel(arg2)
10000a674
10000a684        _xpc_connection_set_event_handler(arg2, &___block_literal_global)
10000a694        return _xpc_connection_activate(arg2) __tailcall
----------------------------------------------------------------------------

3) No Path validation in Delete and Copy file
When triggering file copy or delete call via XPC, the service does not check if it
should be allowed to delete or copy the file. No restrictions are applied for
copying or deleting files. These missing restrictions lead to privilege escalation
due to the possibility to delete and then write to /etc/sudoers or /Library/LaunchDaemons.

This issue is not exploitable on its own without a vulnerability allowing for
connection to the privileged helper. However the other two vulnerabilities
described in this advisory allow exactly that.

Proof of concept:
-----------------
1) Local Privilege Escalation via DYLIB Injection (CVE-2026-24070)
To check for the dangerous entitlements
`com.apple.security.cs.allow-dyld-environment-variables` and
`com.apple.security.cs.disable-library-validation` the "codesign" utility of
MacOS can be used:

----------------------------------------------------------------------------
lowpriv@Users-Mac exploit % codesign -dvv --entitlements :- /Applications/Native\ Access.app/Contents/MacOS/Native\
Access
Executable=/Applications/Native Access.app/Contents/MacOS/Native Access
Identifier=com.native-instruments.nativeaccess2
[...]
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST
1.0//EN""https://www.apple.com/DTDs/PropertyList-1.0.dtd";><plist version="1.0">
        <dict>
                <key>com.apple.security.cs.allow-dyld-environment-variables</key>
                <true/>
                <key>com.apple.security.cs.allow-jit</key>
                <true/>
                <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
                <true/>
                <key>com.apple.security.cs.disable-library-validation</key>
                <true/>
        </dict>
</plist>
----------------------------------------------------------------------------

The privileged helper located at
/Library/PrivilegedHelperTools/com.native-instruments.NativeAccess.Helper2
was found to check the code signature of the XPC client before running any
action. Due to the DYLIB injection vulnerability in the Native Access executable
it is possible to execute code in the context of the process of Native Access
which has a valid signature for the needed Team ID. The XPC service exposed
multiple functions, e.g. copy-file and remove.

The following code was used to craft a malicious DYLIB, which on load connects
to the privileged helper XPC service and deletes the /etc/sudoers file as such
that it can then copy a malicious version of the sudoers file to /etc/sudoers.

[ PoC exploit code removed ]

On a Mac system with the developer tools installed the PoC library can be compiled
as follows:

----------------------------------------------------------------------------
$ clang -framework Foundation -dynamiclib -o libxpcclient.dylib libxpcclient.m
----------------------------------------------...