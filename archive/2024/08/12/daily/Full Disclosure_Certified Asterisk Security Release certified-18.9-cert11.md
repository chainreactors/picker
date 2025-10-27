---
title: Certified Asterisk Security Release certified-18.9-cert11
url: https://seclists.org/fulldisclosure/2024/Aug/9
source: Full Disclosure
date: 2024-08-12
fetch_date: 2025-10-06T18:02:19.249619
---

# Certified Asterisk Security Release certified-18.9-cert11

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# Certified Asterisk Security Release certified-18.9-cert11

---

*From*: Asterisk Development Team via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 08 Aug 2024 13:25:46 +0000

---

```
The Asterisk Development Team would like to announce security release
Certified Asterisk 18.9-cert11.

The release artifacts are available for immediate download at
https://github.com/asterisk/asterisk/releases/tag/certified-18.9-cert11
and
https://downloads.asterisk.org/pub/telephony/certified-asterisk

Repository: https://github.com/asterisk/asterisk
Tag: certified-18.9-cert11

## Change Log for Release asterisk-certified-18.9-cert11

### Links:

 - [Full
ChangeLog](https://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-certified-18.9-cert11.md)

 - [GitHub Diff](https://github.com/asterisk/asterisk/compare/certified-18.9-cert10...certified-18.9-cert11)
 - [Tarball](https://downloads.asterisk.org/pub/telephony/certified-asterisk/asterisk-certified-18.9-cert11.tar.gz)
 - [Downloads](https://downloads.asterisk.org/pub/telephony/certified-asterisk)

### Summary:

- Commits: 5
- Commit Authors: 2
- Issues Resolved: 4
- Security Advisories Resolved: 1
  - [GHSA-c4cg-9275-6w44](https://github.com/asterisk/asterisk/security/advisories/GHSA-c4cg-9275-6w44):
Write=originate, is sufficient permissions for code execution / System() dialplan

### User Notes:

- #### res_pjsip_config_wizard.c: Refactor load process
  The res_pjsip_config_wizard.so module can now be reloaded.

### Upgrade Notes:

### Commit Authors:

- George Joseph: (4)
- Mike Bradeen: (1)

## Issue and Commit Detail:

### Closed Issues:

  - !GHSA-c4cg-9275-6w44: Write=originate, is sufficient permissions for code execution / System() dialplan
  - 780: [bug]: Infinite loop of "Indicated Video Update", max CPU usage
  - 801: [bug]: res_stasis: Occasional 200ms delay adding channel to a bridge
  - 816: [bug]: res_pjsip_config_wizard doesn't load properly if res_pjsip is loaded first
  - 819: [bug]: Typo in voicemail.conf.sample that stops it from loading when using "make samples"

### Commits By Author:

- #### George Joseph (4):
  - manager.c: Add entries to Originate blacklist
  - bridge_softmix: Fix queueing VIDUPDATE control frames
  - voicemail.conf.sample: Fix ':' comment typo
  - res_pjsip_config_wizard.c: Refactor load process

- #### Mike Bradeen (1):
  - res_stasis: fix intermittent delays on adding channel to bridge

### Commit List:

-  res_stasis: fix intermittent delays on adding channel to bridge
-  res_pjsip_config_wizard.c: Refactor load process
-  voicemail.conf.sample: Fix ':' comment typo
-  bridge_softmix: Fix queueing VIDUPDATE control frames
-  manager.c: Add entries to Originate blacklist

### Commit Details:

#### res_stasis: fix intermittent delays on adding channel to bridge
  Author: Mike Bradeen
  Date:   2024-07-10

  Previously, on command execution, the control thread was awoken by
  sending a SIGURG. It was found that this still resulted in some
  instances where the thread was not immediately awoken.

  This change instead sends a null frame to awaken the control thread,
  which awakens the thread more consistently.

  Resolves: #801

#### res_pjsip_config_wizard.c: Refactor load process
  Author: George Joseph
  Date:   2024-07-23

  The way we have been initializing the config wizard prevented it
  from registering its objects if res_pjsip happened to load
  before it.

  * We now use the object_type_registered sorcery observer to kick
  things off instead of the wizard_mapped observer.

  * The load_module function now checks if res_pjsip has been loaded
  already and if it was it fires the proper observers so the objects
  load correctly.

  Resolves: #816

  UserNote: The res_pjsip_config_wizard.so module can now be reloaded.

#### voicemail.conf.sample: Fix ':' comment typo
  Author: George Joseph
  Date:   2024-07-24

  ...and removed an errant trailing space.

  Resolves: #819

#### bridge_softmix: Fix queueing VIDUPDATE control frames
  Author: George Joseph
  Date:   2024-07-17

  softmix_bridge_write_control() now calls ast_bridge_queue_everyone_else()
  with the bridge_channel so the VIDUPDATE control frame isn't echoed back.

  softmix_bridge_write_control() was setting bridge_channel to NULL
  when calling ast_bridge_queue_everyone_else() for VIDUPDATE control
  frames.  This was causing the frame to be echoed back to the
  channel it came from.  In certain cases, like when two channels or
  bridges are being recorded, this can cause a ping-pong effect that
  floods the system with VIDUPDATE control frames.

  Resolves: #780

#### manager.c: Add entries to Originate blacklist
  Author: George Joseph
  Date:   2024-07-22

  Added Reload and DBdeltree to the list of dialplan application that
  can't be executed via the Originate manager action without also
  having write SYSTEM permissions.

  Added CURL, DB*, FILE, ODBC and REALTIME* to the list of dialplan
  functions that can't be executed via the Originate manager action
  without also having write SYSTEM permissions.

  If the Queue application is attempted to be run by the Originate
  manager action and an AGI parameter is specified in the app data,
  it'll be rejected unless the manager user has either the AGI or
  SYSTEM permissions.

  Resolves: #GHSA-c4cg-9275-6w44

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

### Current thread:

* **Certified Asterisk Security Release certified-18.9-cert11** *Asterisk Development Team via Fulldisclosure (Aug 10)*

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

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertisin...