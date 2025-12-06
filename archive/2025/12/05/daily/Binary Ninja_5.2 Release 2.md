---
title: 5.2 Release 2
url: https://binary.ninja/2025/12/05/5.2-release-2.html
source: Binary Ninja
date: 2025-12-05
fetch_date: 2025-12-06T03:10:15.980517
---

# 5.2 Release 2

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Binary Ninja [5.2, codename Io, is out](/2025/11/13/binary-ninja-5.2-io.html) and includes bitfield support, containers, hexagon, and much more.

# Binary Ninja Blog

## 5.2 Release 2

* [Jordan Wiens](https://github.com/psifertex)
* 2025-12-05
* [announcements](/tag/announcements), [stable](/tag/stable)

For customers who prefer to operate on stable branches, we have released an âR2â, or second release of the [Io, 5.2
release](https://binary.ninja/2025/11/13/binary-ninja-5.2-io.html). It includes multiple small stability improvements,
crash fixes, update fixes for Linux ARM builds, and fixes to WARP, DWARF, and Ghidra Import.

As always, customers with [active support](https://binary.ninja/purchase/) on the [development
branch](https://docs.binary.ninja/guide/index.html#development-branch) have access to these changes and more.

## Core/Analysis

* **Fix**: Crash due to LLIL\_REG\_STACK\_FREE\_REL accessor mixup in SSA translator
* **Fix**: MLIL\_VAR vs MLIL\_VAR\_SSA check corrected
* **Fix**: Two load/store splitting bugs in MLIL where offsets were incorrectly calculated or defaulted to 0, causing incorrect field boundaries and wrong variable splitting ([#7647](https://github.com/Vector35/binaryninja-api/issues/7647), [#7613](https://github.com/Vector35/binaryninja-api/issues/7613))
* **Fix**: Race condition when adding sections during analysis that could cause crashes when loading DSC images ([#7681](https://github.com/Vector35/binaryninja-api/issues/7681))
* **Fix**: Ensure updating flag cleared if exception thrown, preventing files from being stuck in âupdatingâ state

## Ghidra Import

* **Fix**: Not being able to create database from directly opened Ghidra project file
* **Fix**: Loading files with high IDs
* **Fix**: Loading of databases with no file contents, improve platform detection

## DWARF

* **Fix**: Prevent extra slashes in generated debuginfod urls
* **Fix**: Allow loading supplementary dwarf debug info from path in .gnu\_debugaltlink ([#7597](https://github.com/Vector35/binaryninja-api/issues/7597))
* **Fix**: Crash in dwarf export with detached NTR vtable data variable ([#7646](https://github.com/Vector35/binaryninja-api/issues/7646)

## WARP

* **Fix**: Stop propagating skipped file error when processing archives
* **Fix**: Leaking binary view on empty views ([#7674](https://github.com/Vector35/binaryninja-api/issues/7674))
* **Fix**: Unused rerun matcher checkbox when loading file on disk
* **Fix**: Container list not refreshing for dynamically added containers
* **Fix**: Explicitly create user signature directory on plugin init
* **Fix**: âhas user annotationsâ flag not persisting when opening database ([#7269](https://github.com/Vector35/binaryninja-api/issues/7269))

## UI/UX

* **Improvement**: Make project file picker columns resizable
* **Fix**: Tag type visibility changes not being reflected in the tag list ([#7662](https://github.com/Vector35/binaryninja-api/issues/7662))
* **Fix**: Tag types not being loaded properly from snapshots
* **Fix**: File lock tooltip being spammed when selecting in flow graph ([#7644](https://github.com/Vector35/binaryninja-api/issues/7644))
* **Fix**: Crash on Open with Options -> Upgrade Database -> Decline

## Enterprise/Remote

* **Fix**: âremote is not connectedâ log spam by adding connection checks before reading from remote
* **Fix**: Potential crash when switching remotes quickly after opening a file
* **Fix**: Downloading dependency files not downloading the right file

## Platform Support

* **Fix**: System CA inclusion in core download provider, fixing HTTPS downloads when system CA store contains proxy root CAs ([#7656](https://github.com/Vector35/binaryninja-api/issues/7656))
* **Fix**: Restore linux aarch64 update functionality ([#7641](https://github.com/Vector35/binaryninja-api/issues/7641))

These builds are now live on both our website and update servers. If youâre a Binary Ninja Free user, you can download a
new installer [here](https://binary.ninja/free). If youâre a Personal, Commercial, or Enterprise user, the new build is
available from the [portal](https://portal.binary.ninja/) or via a [license recovery
email](https://binary.ninja/recover). And as always, you can
[update](https://docs.binary.ninja/guide/index.html#updates) your existing client.

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2025 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#6a0803040b1813040304000b2a1c0f091e0518595f44090507)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)