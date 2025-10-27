---
title: 4.1 Release 2
url: https://binary.ninja/2024/08/16/4.1-release-2.html
source: Binary Ninja
date: 2024-08-17
fetch_date: 2025-10-06T18:04:17.490963
---

# 4.1 Release 2

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

## 4.1 Release 2

* [Jordan Wiens](https://github.com/psifertex)
* 2024-08-16
* [announcements](/tag/announcements), [stable](/tag/stable)

Much like our [4.0 re-release](https://binary.ninja/2024/05/27/4.0-update.html), we are releasing an updated 4.1 with a few additional changes. As always, you can switch to the [dev channel](https://docs.binary.ninja/guide/index.html#development-branch) to receive these fixes and more, while build 4.1.5902 released today is for those who prefer to stay on stable releases.

Issues that were fixed in this re-release include:

* Feature: Support for [GNU DWARF extensions](https://github.com/Vector35/binaryninja-api/issues/5758)
* Feature: Add support for [DWARF supplementary files](https://github.com/Vector35/binaryninja-api/issues/5423)
* Feature: Expose [ConflictSplitter APIs](https://github.com/Vector35/binaryninja/issues/808) for extensible collaboration merge conflict handling
* Fix: [Issue](https://github.com/Vector35/binaryninja-api/issues/5747) with focusing created project in remote browser
* Fix: [Issue](https://github.com/Vector35/debugger/issues/597) which caused the debugger to run slowly
* Fix: [Crash](https://github.com/Vector35/debugger/issues/594) when debugging a TTD trace
* Fix: [Issue](https://github.com/Vector35/debugger/issues/605) preventing Mapped views from being able to use TDD
* Fix: [Crash](https://github.com/Vector35/binaryninja-api/issues/5774) while using the right-click menu in the MemoryMap UI
* Fix: [Issue](https://github.com/Vector35/binaryninja-api/issues/5777) causing the size calculation of outlined memcpys to be wrong
* Fix: [Issue](https://github.com/Vector35/binaryninja-api/issues/5837) causing the plugin manager to not apply updated dependencies
* Fix: [Issue](https://github.com/Vector35/binaryninja-api/issues/5806) causing inverted conditionals on some arm64 instructions
* Fix: [Issue](https://github.com/Vector35/binaryninja-api/pull/5810) with the lifting of some MIPS instructions
* Fix: [Issue](https://github.com/Vector35/binaryninja/issues/800) in which headless Enterprise scripts released and reacquired license checkouts unnecessarily
* Fix: [Issue](https://github.com/Vector35/debugger/issues/602) affecting the display of memory while debugging
* Fix: [Issue](https://github.com/Vector35/binaryninja-api/issues/5809) preventing some function calls from showing parameters

These builds are now live on both our update servers and via our website. If youâre a Binary Ninja Free user, you can download a new installer [here](https://binary.ninja/free). If youâre a Personal, Commercial, or Enterprise user, you can request a new installer via the [license recovery page](https://binary.ninja/recover) or update your existing client.

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2025 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#d4b6bdbab5a6adbabdbabeb594a2b1b7a0bba6e7e1fab7bbb9)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)