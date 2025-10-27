---
title: Asterisk Release certified-18.9-cert5
url: https://seclists.org/fulldisclosure/2023/Jul/27
source: Full Disclosure
date: 2023-07-12
fetch_date: 2025-10-04T11:56:35.290707
---

# Asterisk Release certified-18.9-cert5

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# Asterisk Release certified-18.9-cert5

---

*From*: Asterisk Development Team via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 07 Jul 2023 19:39:14 +0000

---

```
The Asterisk Development Team would like to announce security release
Certified Asterisk 18.9-cert5.

The release artifacts are available for immediate download at
https://github.com/asterisk/asterisk/releases/tag/certified-18.9-cert5
and
https://downloads.asterisk.org/pub/telephony/certified-asterisk

The following security advisories were resolved in this release:
https://github.com/asterisk/asterisk/security/advisories/GHSA-4xjp-22g4-9fxm

Change Log for Release certified-18.9-cert5
========================================

Links:
----------------------------------------

 - [Full ChangeLog](https://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-certified-18.9-cert5.md)
 - [GitHub Diff](https://github.com/asterisk/asterisk/compare/certified-18.9-cert4...certified-18.9-cert5)
 - [Tarball](https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-certified-18.9-cert5.tar.gz)
 - [Downloads](https://downloads.asterisk.org/pub/telephony/asterisk)

Summary:
----------------------------------------

- apply_patches: Use globbing instead of file/sort.
- apply_patches: Sort patch list before applying
- bundled_pjproject: Backport security fixes from pjproject 2.13.1
- .github: Updates for AsteriskReleaser
- res_musiconhold: avoid moh state access on unlocked chan
- utils: add lock timestamps for DEBUG_THREADS
- .github: Back out triggering PROpenedOrUpdated by label
- .github: Move publish docs to new file CreateDocs.yml
- .github: Remove result check from PROpenUpdateGateTests
- .github: Fix use of 'contains'
- .github: Add recheck label test to additional jobs
- .github: Fix recheck label typos
- .github: Fix recheck label manipulation
- .github: Allow PR submit checks to be re-run by label
- res_pjsip_session: Added new function calls to avoid ABI issues.
- test_statis_endpoints:  Fix channel_messages test again
- test_stasis_endpoints.c: Make channel_messages more stable
- build: Fix a few gcc 13 issues
- .github: Rework for merge approval
- AMI: Add CoreShowChannelMap action.
- .github: Fix issues with cherry-pick-reminder
- indications: logging changes
- .github Ignore error when adding reviewrs to PR
- .github: Update field descriptions for AsteriskReleaser
- .github: Change title of AsteriskReleaser job
- .github: Don't add cherry-pick reminder if it's already present
- .github: Fix quoting in PROpenedOrUpdated
- .github: Add cherry-pick reminder to new PRs
- core: Cleanup gerrit and JIRA references. (#40) (#61)
- .github: Tweak improvement issue type language.
- .github: Tweak new feature language, and move feature requests elsewhere.
- .github: Fix staleness check to only run on certain labels.
- .github: Add AsteriskReleaser
- cel: add local optimization begin event
- .github: Fix CherryPickTest to only run when it should
- .github: Fix reference to CHERRY_PICK_TESTING_IN_PROGRESS
- .github: Remove separate set labels step from new PR
- .github: Refactor CP progress and add new PR test progress
- .github: Add cherry-pick test progress labels
- .github: Update issue templates
- .github: Remove unnecessary parameter in CherryPickTest
- Initial GitHub PRs
- Initial GitHub Issue Templates
- test.c: Fix counting of tests and add 2 new tests
- res_mixmonitor: MixMonitorMute by MixMonitor ID
- format_sln: add .slin as supported file extension
- bridge_builtin_features: add beep via touch variable
- cli: increase channel column width
- app_senddtmf: Add option to answer target channel.
- app_directory: Add a 'skip call' option.
- app_read: Add an option to return terminator on empty digits.
- app_directory: add ability to specify configuration file

User Notes:
----------------------------------------

- ### AMI: Add CoreShowChannelMap action.
  New AMI action CoreShowChannelMap has been added.

- ### cel: add local optimization begin event
  The new AST_CEL_LOCAL_OPTIMIZE_BEGIN can be used
  by itself or in conert with the existing
  AST_CEL_LOCAL_OPTIMIZE to book-end local channel optimizaion.

- ### app_read: Add an option to return terminator on empty digits.
  A new option 'e' has been added to allow Read() to return the
  terminator as the dialed digits in the case where only the terminator
  is entered.

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

- ### app_directory: Add a 'skip call' option.
  A new option 's' has been added to the Directory() application that
  will skip calling the extension and instead set the extension as
  DIRECTORY_EXTEN channel variable.

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

- ### app_senddtmf: Add option to answer target channel.
  A new option has been added to SendDTMF() which will answer the
  specified channel if it is not already up. If no channel is specified,
  the current channel will be answered instead.

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

- ### cel: add local optimization begin event
  The existing AST_CEL_LOCAL_OPTIMIZE can continue
  to be used as-is and the AST_CEL_LOCAL_OPTIMIZE_BEGIN ev...