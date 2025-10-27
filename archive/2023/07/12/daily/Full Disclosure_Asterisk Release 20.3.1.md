---
title: Asterisk Release 20.3.1
url: https://seclists.org/fulldisclosure/2023/Jul/26
source: Full Disclosure
date: 2023-07-12
fetch_date: 2025-10-04T11:56:34.124634
---

# Asterisk Release 20.3.1

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# Asterisk Release 20.3.1

---

*From*: Asterisk Development Team via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 07 Jul 2023 20:10:00 +0000

---

```
The Asterisk Development Team would like to announce security release
Asterisk 20.3.1.

The release artifacts are available for immediate download at
https://github.com/asterisk/asterisk/releases/tag/20.3.1
and
https://downloads.asterisk.org/pub/telephony/asterisk

The following security advisories were resolved in this release:
https://github.com/asterisk/asterisk/security/advisories/GHSA-4xjp-22g4-9fxm

Change Log for Release 20.3.1
========================================

Links:
----------------------------------------

 - [Full ChangeLog](https://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-20.3.1.md)
 - [GitHub Diff](https://github.com/asterisk/asterisk/compare/20.3.0...20.3.1)
 - [Tarball](https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20.3.1.tar.gz)
 - [Downloads](https://downloads.asterisk.org/pub/telephony/asterisk)

Summary:
----------------------------------------

- apply_patches: Use globbing instead of file/sort.
- apply_patches: Sort patch list before applying
- pjsip: Upgrade bundled version to pjproject 2.13.1

User Notes:
----------------------------------------

- ### res_http_media_cache: Introduce options and customize
  The res_http_media_cache module now attempts to load
  configuration from the res_http_media_cache.conf file.
  The following options were added:
    * timeout_secs
    * user_agent
    * follow_location
    * max_redirects
    * protocols
    * redirect_protocols
    * dns_cache_timeout_secs

- ### format_sln: add .slin as supported file extension
  format_sln now recognizes '.slin' as a valid
  file extension in addition to the existing
  '.sln' and '.raw'.

- ### bridge_builtin_features: add beep via touch variable
  Add optional touch variable : TOUCH_MIXMONITOR_BEEP(interval)
  Setting TOUCH_MIXMONITOR_BEEP/TOUCH_MONITOR_BEEP to a valid
  interval in seconds will result in a periodic beep being
  played to the monitored channel upon MixMontior/Monitor
  feature start.
  If an interval less than 5 seconds is specified, the interval
  will default to 5 seconds.  If the value is set to an invalid
  interval, the default of 15 seconds will be used.

- ### app_senddtmf: Add SendFlash AMI action.
  The SendFlash AMI action now allows sending
  a hook flash event on a channel.

- ### res_mixmonitor: MixMonitorMute by MixMonitor ID
  It is now possible to specify the MixMonitorID when calling
  the manager action: MixMonitorMute.  This will allow an
  individual MixMonitor instance to be muted via ID.
  The MixMonitorID can be stored as a channel variable using
  the 'i' MixMonitor option and is returned upon creation if
  this option is used.
  As part of this change, if no MixMonitorID is specified in
  the manager action MixMonitorMute, Asterisk will set the mute
  flag on all MixMonitor audiohooks on the channel.  Previous
  behavior would set the flag on the first MixMonitor audiohook
  found.

- ### pbx_dundi: Add PJSIP support.
  DUNDi now supports chan_pjsip. Outgoing calls using
  PJSIP require the pjsip_outgoing_endpoint option
  to be set in dundi.conf.

- ### test.c: Fix counting of tests and add 2 new tests
  The "tests" attribute of the "testsuite" element in the
  output XML now reflects only the tests actually requested
  to be executed instead of all the tests registered.
  The "failures" attribute was added to the "testsuite"
  element.
  Also added two new unit tests that just pass and fail
  to be used for testing CI itself.

- ### cli: increase channel column width
  This change increases the display width on 'core show channels'
  amd 'core show channels verbose'
  For 'core show channels', the Channel name field is increased to
  64 characters and the Location name field is increased to 32
  characters.
  For 'core show channels verbose', the Channel name field is
  increased to 80 characters, the Context is increased to 24
  characters and the Extension is increased to 24 characters.

Upgrade Notes:
----------------------------------------

Closed Issues:
----------------------------------------

  - #193: [bug]: third-party/apply-patches doesn't sort the patch file list before applying
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](29)

### Current thread:

* **Asterisk Release 20.3.1** *Asterisk Development Team via Fulldisclosure (Jul 11)*

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