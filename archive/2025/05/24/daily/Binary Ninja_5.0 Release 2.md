---
title: 5.0 Release 2
url: https://binary.ninja/2025/05/23/5.0-release-2.html
source: Binary Ninja
date: 2025-05-24
fetch_date: 2025-10-06T22:27:54.587844
---

# 5.0 Release 2

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

## 5.0 Release 2

* [Jordan Wiens](https://github.com/psifertex)
* 2025-05-23
* [announcements](/tag/announcements), [stable](/tag/stable)

While our customers with [active support](https://binary.ninja/purchase/) on the [development
branch](https://docs.binary.ninja/guide/index.html#development-branch) have access to these changes and more, we
occasionally release updated stable releases just to include a few fixes that we either did not identify during stable
release testing or those for whom a fix was scheduled after the original stable release.

This 5.0 Release 2 build improves on our recent [5.0 release](https://binary.ninja/2025/04/23/5.0-gallifrey.html) with a
few small stability improvements and fixes.

**EDIT: Release 3 (5.0.7648) was released on 2025-06-20 and includes the following updated fix:**

* **Fix**: Fix: Python APIs [that iterate](https://github.com/Vector35/binaryninja-api/issues/6020) IL functions were throwing exceptions when IL could not be loaded. This fix was requested by an enterprise customer.

The following were fixed in 5.0.7486 include:

## Core/Analysis

* **Improvement**: RTTI Processing:
  + Support for volatile typedefs and consult cv qualifiers when comparing types
  + Support NTR type in base structures
  + Handle type names emitted by GCC with a leading \*
  + Handle cxxabi vtables being referenced via RELOC\_COPY
  + Demangle more types in Itanium RTTI
  + Fixed skipping type info with stripped root type info object
  + Fixed some RTTI information being overwritten by empty class info
  + Loosened section semantic sanity checks in Itanium RTTI processing
* **Fix**: Memory leak in BNRegisterPluginCommand
* **Fix**: Memory leak in BNGetFullInfoUpdateChannels
* **Fix**: Memory leak in BNVersionInfo
* **Fix**: Memory leak in Metadata::GetKeyValueStore()
* **Fix**: Memory leaks in Component::GetGuid/GetName/GetDisplayName
* **Fix**: Memory leak in Collaboration::NotificationListener
* **Fix**: Memory leak in python Enumeration class
* **Fix**: Memory leaks in Sections, Segments, Settings, ExternalLibrary, and BackgroundTask
* **Fix**: Memory leak when calling Metadata::get\_value\_store in Rust API
* **Fix**: Crash when querying possible variable values from disassembly view
* **Fix**: Crash on close in URLHandlerThread
* **Fix**: Crash with zeroed base class descriptor in RTTI
* **Fix**: Crash with invalid vtable info when processing MSVC vftables
* **Fix**: Version info leaking channel string
* **Fix**: AssociatedDataStore behavior
* **Fix**: Data tags added via API not showing in flow graphs until refresh
* **Fix**: SetTagTypeVisibleUndoAction not properly tracking state
* **Fix**: Eliminated erroneous log message from SettingsCache when opening text-format files
* **Fix**: Catch some unhandled exceptions in UI

## DWARF

* **Fix**: Do not add binary base to function address twice when a symbol with that functionâs raw name already exists
* **Fix**: Load eh\_frame/debug\_frame from base bv instead of debug bv and make calculated cie offset ranges relative to bv start
* **Fix**: Dwarf raw name resolution not resolving specification
* **Fix**: Try to load eh\_frame/debug\_frame from both raw and normal views in dwarf import

## Thumb2

* **Fix**: Correctly set flags for mov{s} and mvn{s} instruction variants with 32-bit encodings

## Dyld Shared Cache / Mach-O

* **Improvement**: Mark Objective-C metadata-derived symbols as local instead of exported
* **Improvement**: Export Trie Parsing: Reworked to avoid recursion with vastly improved error handling
* **Fix**: Possible deadlock when loading images from the UI
* **Fix**: Potential crash when closing view with images still being added in the background through the UI
* **Fix**: Updated ref count warning to only show when above two
* **Fix**: Various fixes for Objective-C metadata processing

## UI/UX

* **Improvement**: Stack Render Layer included in the Free edition
* **Improvement**: IME methods now supported in Linux
* **Fix**: Opening [URLs](https://binary.ninja/2025/04/23/5.0-gallifrey.html#updated-url-handler) in enterprise with floating license in some situations

## Debugger

* **Improvement**: Maintain the current address in the graph view when refreshing its contents
* **Improvement**: Hide PC indicator at 0x0 in HLIL if the debugger is not active
* **Fix**: UAF crash if the user closes the tab before the launch is completed

## Documentation

* **Improvement**: Memory permissions concept section in user documentation updated
* **Fix**: Formatting and added information regarding the volatile annotation and how it impacts analysisÂ

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

[[email protected]](/cdn-cgi/l/email-protection#cfada6a1aebdb6a1a6a1a5ae8fb9aaacbba0bdfcfae1aca0a2)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)