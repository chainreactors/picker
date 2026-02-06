---
title: Command Palette Updates
url: https://binary.ninja/2026/02/05/command-palette-updates.html
source: Binary Ninja
date: 2026-02-05
fetch_date: 2026-02-06T04:08:39.828203
---

# Command Palette Updates

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

## Command Palette Updates

* [Glenn Smith](https://github.com/CouleeApps)
* 2026-02-05
* [ui](/tag/ui)

The [Command Palette](https://dev-docs.binary.ninja/guide/index.html#command-palette) is one of the primary interfaces for interacting with Binary Ninja, and has been for almost as long as Binary Ninja has existed. Now, in the upcoming [Jotunheim release](https://github.com/Vector35/binaryninja-api/milestone/29), the [Command Palette](https://dev-docs.binary.ninja/guide/index.html#command-palette) is getting more powerful! Beyond just searching menu items, you will be able to search Functions, Types, Strings, and more!

![Blob Ross =](/blog/images/command-palette/blob-ross.jpg)

## Search Analysis Objects

If you have an analysis session open, you can now search for various analysis objects directly in the Command Palette. You can start your search with different prefixes if you want to search for different types of objects:

| Prefix | Search Type |
| --- | --- |
| None | Everything |
| `@` | Functions and Symbols |
| `"` | Strings |
| `>` | Actions (previous default) |
| `t:` | Open Tabs |
| `/` | Projects |

### Search Everything

With no prefix, the Command Palette will search for any sort of action or object that matches:

![Search Everything](/blog/images/command-palette/search-everything.png)

### Search Functions and Symbols

Starting your search with `@` will let you search Functions and Symbols. Selecting one and pressing enter will navigate you to it:

![Search Functions and Symbols](/blog/images/command-palette/search-functions-symbols.png)

### Search Strings

Starting your search with `"` will let you search for strings. Selecting one and pressing enter will navigate you to it, or for the case of strcpy-outlined strings, where it gets constructed:

![Search Strings](/blog/images/command-palette/search-strings.png)

### Search Actions

Starting your search with `>` will let you search actions, similar to how the Command Palette used to work:

![Search Actions](/blog/images/command-palette/search-actions.png)

### Go to Expression

Starting your search with `=` will let you enter [an expression](https://api.binary.ninja/binaryninja.binaryview-module.html#binaryninja.binaryview.BinaryView.parse_expression), which will be calculated and shown in the results. If the value is an address within your open analysis session, pressing enter will navigate to that address:

![Go to Expression](/blog/images/command-palette/go-to-expression.png)

### Search Open Tabs

Starting your search with `t:` will let you search your open tabs, showing file names and paths if applicable:

![Search Open Tabs](/blog/images/command-palette/search-tabs.png)

### Search Project Files

On Commercial and above editions, starting your search with `/` will let you search the files in your open [projects](https://docs.binary.ninja/guide/projects.html):

![Search Project Files](/blog/images/command-palette/search-files.png)

## Conclusion

We hope that the enhanced Command Palette helps optimize your reverse engineering workflow even further, letting you navigate across the product faster, and entirely from the keyboard. We look forward to your feedback and suggestions, as we strive to make Binary Ninja the best tool for reverse engineering!

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2026 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#5d3f34333c2f24333433373c1d2b383e29322f6e68733e3230)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)