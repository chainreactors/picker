---
title: 5.1 Release 2
url: https://binary.ninja/2025/08/14/5.1-release-2.html
source: Binary Ninja
date: 2025-08-15
fetch_date: 2025-10-07T00:48:08.323524
---

# 5.1 Release 2

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

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## 5.1 Release 2

* [Jordan Wiens](https://github.com/psifertex)
* 2025-08-14
* [announcements](/tag/announcements), [stable](/tag/stable)

![Phido as Jackal and Binjy as Riddick >](/blog/images/5.1-release/helion.jpg)

Weâre back with a small hotfix for our recent [5.1 Helion](https://binary.ninja/2025/07/24/5.1-helion.html) release. Following our usual practice for stable releases, weâve bundled together several important fixes that have come to light since the original 5.1 launch, along with a new Sidekick sidebar feature.

This release focuses on stability improvements across WARP, the debugger, and Enterprise collaboration, plus some nice UI enhancements. For users on our [development branch](https://docs.binary.ninja/guide/index.html#development-branch), these fixes are already available alongside additional features.

## UI

* **Feature**: New Sidekick sidebar widget (can be hidden by installing Sidekick or right-clicking and choosing âhideâ)
* **Improvement**: âShow Condition As Invertedâ was selectable in situations where it [should have been unavailable](https://github.com/Vector35/binaryninja-api/issues/7175)
* **Fix**: Several fixes related to the URL handling logic impacting file opening on startup

## Analysis

* **Improvement**: Support for rebased [IDB import](https://github.com/Vector35/binaryninja-api/issues/7163)
* **Improvement**: Handle ELF files with [no program headers](https://github.com/Vector35/binaryninja-api/pull/7052)
* **Fix**: Memory leak [when applying](https://github.com/Vector35/binaryninja-api/pull/7215) debuginfod metadata

## WARP

* **Fix**: WARP sometimes [clobbered](https://github.com/Vector35/binaryninja-api/issues/7194) user-type information
* **Fix**: Duplicate [setting registration](https://github.com/Vector35/binaryninja-api/issues/7184)
* **Fix**: WARP function symbols [persisted across matched functions](https://github.com/Vector35/binaryninja-api/issues/7158)
* **Improvement**: Symbol and comment [application changes](https://github.com/Vector35/binaryninja-api/pull/7244)

## Enterprise

* **Fix**: Enterprise collaboration could fail to sync with the error âfailed to read any data for fieldâ

## Debugger

* **Fix**: Crash upon [multiple restarts](https://github.com/Vector35/debugger/issues/766) with debugger enabled

## Documentation

* **Improvement**: [Better documentation](https://docs.binary.ninja/about/open-source.html#third-party-open-source) for open source Rust dependencies

These builds are now live on both our update servers and via our website. If youâre a Binary Ninja Free user, you can
download a new installer [here](https://binary.ninja/free). If youâre a Personal, Commercial, or Enterprise user, the
new build is available from the [portal](https://portal.binary.ninja/) or via a [license recovery
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

[[email protected]](/cdn-cgi/l/email-protection#dcbeb5b2bdaea5b2b5b2b6bd9caab9bfa8b3aeefe9f2bfb3b1)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)