---
title: KL-001-2026-01: yintibao Fun Print Mobile Unauthorized Access via Context Hijacking
url: https://seclists.org/fulldisclosure/2026/Jan/12
source: Full Disclosure
date: 2026-01-08
fetch_date: 2026-01-09T03:32:01.894271
---

# KL-001-2026-01: yintibao Fun Print Mobile Unauthorized Access via Context Hijacking

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
[By Date](date.html#12)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#12)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# KL-001-2026-01: yintibao Fun Print Mobile Unauthorized Access via Context Hijacking

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 8 Jan 2026 15:03:37 -0600

---

```
KL-001-2026-01: yintibao Fun Print Mobile Unauthorized Access via Context Hijacking

Title: yintibao Fun Print Mobile Unauthorized Access via Context Hijacking
Advisory ID: KL-001-2026-001
Publication Date: 2026-01-08
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2026-001.txt

1. Vulnerability Details

     Affected Vendor: yintibao
     Affected Product: Fun Print Mobile
     Affected Version: 6.05.15
     Platform: ARM64 - Android
     CWE Classification: CWE-926: Improper Export of Android
                         Application Components
     CVE ID: CVE-2025-15464

2. Vulnerability Description

     Exported Activity allows external applications to gain
     application context and directly launch Gmail with inbox access,
     bypassing security controls.

3. Technical Description

     * Performed on Android 13 aarch64 - Samsung (Galaxy Tab A7 Lite)
     * Using Frida client on Ubuntu 24.04 LTS - Frida server on
       Samsung Rooted Device.
     * The target Activity is exported true. Which means any
       application may interact with it, given that permissions are
       provided.
     * The attacking host needs to attach the device email to the
       application; then the account can be used by the application.

     The PandoraEntry activity is exported (android:exported="true")
     and processes external intents without validation.  Below is
     the PandoraEntryActivity code:

     protected void onCreate(Bundle bundle) {
         // ... INITALIZATION CODE ...  super.onCreate(bundle);

         // BELOW EXTERNAL INTENT ACCEPTED WITHOUT VALIDATION Intent
         intent = getIntent();

         // ... PROCESSING CONTINUES WITH UNVALIDATED INTENT ...
         if (intent.hasExtra(IntentConst.START_FROM_TO_CLASS) &&
         SDK.isUniMPSDK()) {
             String stringExtra =
 intent.getStringExtra(IntentConst.START_FROM_TO_CLASS);
             if (!TextUtils.isEmpty(stringExtra) &&
 stringExtra.startsWith("io.dcloud.feature.sdk.multi")) {
                 intent.setClassName(getPackageName(), stringExtra);
 intent.removeExtra(IntentConst.START_FROM_TO_CLASS);
             }
         } else {
 intent.putExtra(IntentConst.WEBAPP_SHORT_CUT_CLASS_NAME,
             PandoraEntry.class.getName()); intent.setClass(this,
             PandoraEntryActivity.class);
         }

         //UNVALIDATED INTENT FORWARDED startActivity(intent);
         overridePendingTransition(0, 0);
     }

4. Mitigation and Remediation Recommendation

     No response from vendor. There are no known mitigations to
     end-users of the affected application version(s).

5. Credit

     This vulnerability was discovered by Felix Segoviano of
     KoreLogic, Inc.

6. Disclosure Timeline

     2025-12-01 : KoreLogic requests security contact from vendor
                  via weizhengsl () vip qq com and 277517409 () qq com.
     2025-12-08 : KoreLogic submits vulnerability details to vendor
                  via weizhengsl () vip qq com and 277517409 () qq com.
     2026-01-08 : KoreLogic public disclosure.

7. Proof of Concept

     URL: https://korelogic.com/Resources/Advisories/KL-001-2026-001.poc.js.txt
     SHA256sum: ddb3c840c94b204fbbe2931a68771ae28d8ea9c778310cfa83e218a64a41ffd5

The contents of this advisory are copyright(c) 2026
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
[OpenPGP\_signature.asc](att-12/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#12)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#12)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **KL-001-2026-01: yintibao Fun Print Mobile Unauthorized Access via Context Hijacking** *KoreLogic Disclosures via Fulldisclosure (Jan 08)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")