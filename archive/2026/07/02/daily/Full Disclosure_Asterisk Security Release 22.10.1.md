---
title: Asterisk Security Release 22.10.1
url: https://seclists.org/fulldisclosure/2026/Jul/6
source: Full Disclosure
date: 2026-07-02
fetch_date: 2026-07-03T05:49:00.134963
---

# Asterisk Security Release 22.10.1

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
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# Asterisk Security Release 22.10.1

---

*From*: Asterisk Development Team via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 25 Jun 2026 17:17:37 +0000

---

```
The Asterisk Development Team would like to announce security release
Asterisk 22.10.1.

The release artifacts are available for immediate download at
https://github.com/asterisk/asterisk/releases/tag/22.10.1
and
https://downloads.asterisk.org/pub/telephony/asterisk

Repository: https://github.com/asterisk/asterisk
Tag: 22.10.1

## Change Log for Release asterisk-22.10.1

### Links:

 - [Full ChangeLog](https://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-22.10.1.html)
 - [GitHub Diff](https://github.com/asterisk/asterisk/compare/22.10.0...22.10.1)
 - [Tarball](https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-22.10.1.tar.gz)
 - [Downloads](https://downloads.asterisk.org/pub/telephony/asterisk)

### Summary:

- Commits: 19
- Commit Authors: 6
- Issues Resolved: 0
- Security Advisories Resolved: 20
  - [GHSA-3g56-cgrh-95p5](https://github.com/asterisk/asterisk/security/advisories/GHSA-3g56-cgrh-95p5): chan_unistim
DIALPAGE digit handling can overflow phone_number and crash Asterisk
  - [GHSA-3rhj-hhw7-m6fw](https://github.com/asterisk/asterisk/security/advisories/GHSA-3rhj-hhw7-m6fw): NULL Pointer
Dereference in HTTP AMI Digest Authentication
  - [GHSA-4pgv-j3mr-3rcp](https://github.com/asterisk/asterisk/security/advisories/GHSA-4pgv-j3mr-3rcp): Reflected XSS
in Phone Provisioning HTTP Error Pages
  - [GHSA-589g-qgf8-m6mx](https://github.com/asterisk/asterisk/security/advisories/GHSA-589g-qgf8-m6mx): Stack buffer
overflow in MWI NOTIFY Message-Account parsing
  - [GHSA-746q-794h-cc7f](https://github.com/asterisk/asterisk/security/advisories/GHSA-746q-794h-cc7f): Out-of-Bounds
Read in Q.931 Information Element Parser (H.323 Addon)
  - [GHSA-8jhw-m2hg-vp3h](https://github.com/asterisk/asterisk/security/advisories/GHSA-8jhw-m2hg-vp3h): Heap Buffer
Overflow in OGG/Speex File Playback (format_ogg_speex)
  - [GHSA-8jw3-ccr9-xrmf](https://github.com/asterisk/asterisk/security/advisories/GHSA-8jw3-ccr9-xrmf): Buffer
over-read in Asterisk PJSIP MWI body parser
  - [GHSA-g8q2-p36q-94f6](https://github.com/asterisk/asterisk/security/advisories/GHSA-g8q2-p36q-94f6):
Heap-use-after-free in Asterisk PJSIP TCP/SDP handling when TCP connection closes during SDP processing
  - [GHSA-h5hv-jmgj-92q2](https://github.com/asterisk/asterisk/security/advisories/GHSA-h5hv-jmgj-92q2): CVE-2022-37325
fix is absent from current chan_ooh323 Q.931 party-number parser
  - [GHSA-j2mm-57pq-jh94](https://github.com/asterisk/asterisk/security/advisories/GHSA-j2mm-57pq-jh94): Possible RED
T.140 Generation Accumulation OOB Write
  - [GHSA-mxgm-8c6f-5p8f](https://github.com/asterisk/asterisk/security/advisories/GHSA-mxgm-8c6f-5p8f): Stack buffer
overflow in res_xmpp XMPP namespace prefix handling
  - [GHSA-ph27-3m5q-mj5m](https://github.com/asterisk/asterisk/security/advisories/GHSA-ph27-3m5q-mj5m): SQL Injection
in cel_pgsql and cel_tds via CELGenUserEvent eventtype Field
  - [GHSA-q9fr-m7g8-6ph5](https://github.com/asterisk/asterisk/security/advisories/GHSA-q9fr-m7g8-6ph5): Asterisk
app_sms.c copies externally controlled SMS lengths into fixed in-struct buffers
  - [GHSA-qf8j-jp7h-c5hx](https://github.com/asterisk/asterisk/security/advisories/GHSA-qf8j-jp7h-c5hx): Out-of-Bounds
Write in Codec2 Decoder Due to Floor/Ceil Sample Count Mismatch
  - [GHSA-r6c2-hwc2-j4mp](https://github.com/asterisk/asterisk/security/advisories/GHSA-r6c2-hwc2-j4mp): LDAP Filter
Injection in res_config_ldap via SIP Username (Unauthenticated Information Disclosure)
  - [GHSA-vfhr-r9x9-c687](https://github.com/asterisk/asterisk/security/advisories/GHSA-vfhr-r9x9-c687): Possible RED
T.140 Heap Buffer Overflow
  - [GHSA-vrfp-mg3q-3959](https://github.com/asterisk/asterisk/security/advisories/GHSA-vrfp-mg3q-3959): ARI
setChannelVar bypasses live_dangerously and permits FILE() writes
  - [GHSA-wcvv-g26m-wx5c](https://github.com/asterisk/asterisk/security/advisories/GHSA-wcvv-g26m-wx5c): ARI
REST-over-WebSocket read-only bypass allows arbitrary module path load and conditional RCE
  - [GHSA-x348-j6c9-77f3](https://github.com/asterisk/asterisk/security/advisories/GHSA-x348-j6c9-77f3): Stack Buffer
Overflow in H.323 ooTrace() via Unbounded vsprintf into Fixed 2048-byte Buffer
  - [GHSA-xgj6-2gc5-5x9c](https://github.com/asterisk/asterisk/security/advisories/GHSA-xgj6-2gc5-5x9c): ast_loggrabber
executes python script in world writable directory(`/tmp`) leading to potential privilege escalation And RCE

### User Notes:

### Upgrade Notes:

### Developer Notes:

- #### ARI: Make ARI applications respect live_dangerously.
  ARI applications can no longer call "dangerous" dialplan
  functions like DB(), FILE(), SHELL(), CURL(), STAT(), etc. without
  enabling "live_dangerously" in asterisk.conf.
  Resolves: #GHSA-vrfp-mg3q-3959

### Commit Authors:

- George Joseph: (6)
- Mike Bradeen: (3)
- Milan Kyselica: (7)
- Pengpeng Hou: (1)
- Roberto Paleari: (1)
- ThatTotallyRealMyth: (1)

## Issue and Commit Detail:

### Closed Issues:

  - !GHSA-3g56-cgrh-95p5: chan_unistim DIALPAGE digit handling can overflow phone_number and crash Asterisk
  - !GHSA-3rhj-hhw7-m6fw: NULL Pointer Dereference in HTTP AMI Digest Authentication
  - !GHSA-4pgv-j3mr-3rcp: Reflected XSS in Phone Provisioning HTTP Error Pages
  - !GHSA-589g-qgf8-m6mx: Stack buffer overflow in MWI NOTIFY Message-Account parsing
  - !GHSA-746q-794h-cc7f: Out-of-Bounds Read in Q.931 Information Element Parser (H.323 Addon)
  - !GHSA-8jhw-m2hg-vp3h: Heap Buffer Overflow in OGG/Speex File Playback (format_ogg_speex)
  - !GHSA-8jw3-ccr9-xrmf: Buffer over-read in Asterisk PJSIP MWI body parser
  - !GHSA-g8q2-p36q-94f6: Heap-use-after-free in Asterisk PJSIP TCP/SDP handling when TCP connection closes during SDP
processing
  - !GHSA-h5hv-jmgj-92q2: CVE-2022-37325 fix is absent from current chan_ooh323 Q.931 party-number parser
  - !GHSA-j2mm-57pq-jh94: Possible RED T.140 Generation Accumulation OOB Write
  - !GHSA-mxgm-8c6f-5p8f: Stack buffer overflow in res_xmpp XMPP namespace prefix handling
  - !GHSA-ph27-3m5q-mj5m: SQL Injection in cel_pgsql and cel_tds via CELGenUserEvent eventtype Field
  - !GHSA-q9fr-m7g8-6ph5: Asterisk app_sms.c copies externally controlled SMS lengths into fixed in-struct buffers
  - !GHSA-qf8j-jp7h-c5hx: Out-of-Bounds Write in Codec2 Decoder Due to Floor/Ceil Sample Count Mismatch
  - !GHSA-r6c2-hwc2-j4mp: LDAP Filter Injection in res_config_ldap via SIP Username (Unauthenticated Information
Disclosure)
  - !GHSA-vfhr-r9x9-c687: Possible RED T.140 Heap Buffer Overflow
  - !GHSA-vrfp-mg3q-3959: ARI setChannelVar bypasses live_dangerously and permits FILE() writes
  - !GHSA-wcvv-g26m-wx5c: ARI REST-over-WebSocket read-only bypass allows arbitrary module path load and conditional RCE
  - !GHSA-x348-j6c9-77f3: Stack Buffer Overflow in H.323 ooTrace() via Unbounded vsprintf into Fixed 2048-byte Buffer
  - !GHSA-xgj6-2gc5-5x9c: ast_loggrabber executes python script in world writable directory(`/tmp`) leading to
potential privilege escalation And RCE

### Commits By Author:

- #### George Joseph (6):
  -...