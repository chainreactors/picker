---
title: Objective-C Update
url: https://binary.ninja/2024/10/16/objectivec-update.html
source: Binary Ninja
date: 2024-10-17
fetch_date: 2025-10-06T18:51:05.148487
---

# Objective-C Update

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

## Objective-C Update

* Kat
* 2024-10-16
* [plugin](/tag/plugin), [objectivec](/tag/objectivec)

Weâve been *very* hard at work improving the experience for our iOS and macOS reverse engineers. Youâll want to [keep an eye out](https://youtube.com/%40vector35/live) for our upcoming 4.2 feature release announcement stream which includes some even juicier bits. In the meantime, hopefully this will tide you over.

This blog is a short summary of the current state of Objective-C analysis in Binary Ninja.

## Automatic Analysis

![Objective-C Loading](/blog/images/objectivecupdate/objectivec.gif)

As mentioned in our [4.1 release notes](https://binary.ninja/2024/07/17/4.1-elysium.html#macosiosobjective-c-improvements), we have changed the Objective-C analysis so that no manual workflow/plugin loading is required. Instead, all changes are now implemented as an [open source plugin](https://github.com/Vector35/workflow_objc) and changes in our open source [MachO BinaryView](https://github.com/Vector35/binaryninja-api/tree/dev/view/macho).

You can disable this via User Settings or on a per-view basis in Open with Options.

![Disable Objective-C Plugin](/blog/images/objectivecupdate/disable.png)

## Automatic Stub Inlining

More recent versions of appleâs compiler will automatically outline `_objc_msgSend` calls automatically, placing the outlined functions in the `__objc_stubs` section.

While providing some space savings, this has resulted in these binaries being much more laborious to analyze.

Binary Ninja can now automatically detect and analyze these outlined functions and fully reverse the optimization, allowing the rest of our suite to work better than ever.

![](/blog/images/objectivecupdate/objc-after.png)
![](/blog/images/objectivecupdate/objc-before.png)

### Call Rewrites

As seen in the above comparison, we also try to trace down msgSend calls and rewrite them to the appropriate function if it is located within the binary.

### Ivar Recovery

Objective-C Class instance variables are automatically recovered and names/types applied accordingly, making things easier to read through.

![Ivar Recovery](/blog/images/objectivecupdate/ivar.png)

### CFString Support

Binary Ninja has full support for the CFString spec and will automatically annotate CFString metadata, and name them accordingly, so parsing them in our IL views is easier.

![CFString List](/blog/images/objectivecupdate/cfstringlist.png)

![CFString Inline](/blog/images/objectivecupdate/cfstringinline.png)

### Category Support

Binary Ninja has full support for category methods and parses them like any other Objective-C method.

![Categories](/blog/images/objectivecupdate/categories.png)

### Architecture Improvements

Weâve added full support for ARMv7/Thumb2 binaries in addition to our existing Aarch64 support, meaning regardless of your target OS and architecture, youâre getting our full suite of analysis.

![Arch improvements](/blog/images/objectivecupdate/arch.png)

Weâre always working to improve our Objective-C analysis, and looking forward to shipping more powerful new tools to enable better capabilities for analyzing binaries from Apple platforms.

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2025 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#d3b1babdb2a1aabdbabdb9b293a5b6b0a7bca1e0e6fdb0bcbe)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)