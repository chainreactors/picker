---
title: Unfurl v2025.02 Released
url: https://dfir.blog/unfurl-parses-obfuscated-ip-addresses/
source: Instapaper: Unread
date: 2025-02-20
fetch_date: 2025-10-06T20:52:30.687954
---

# Unfurl v2025.02 Released

[![dfir.blog](https://dfir.blog/content/images/2019/01/logo.png)](https://dfir.blog)

* [Unfurl](https://dfir.blog/unfurl/)
* [Hindsight](https://dfir.blog/hindsight/)
* [Visualizations](https://dfir.blog/tag/visualizations/)
* [Open Source](https://dfir.blog/tag/open-source/)
* [Presentations & Interviews](https://dfir.blog/tag/media/)

[Unfurl](/tag/unfurl/)

# Unfurl v2025.02 Released

Unfurl v2025.02 adds parsing of obfuscated IP addresses, more Bluesky timestamps, and more!

* [![Ryan Benson](/content/images/size/w100/2024/05/30110948-q3l_NL32.jpg)](/author/ryan/)

#### [Ryan Benson](/author/ryan/)

Feb 19, 2025
• 2 min read

![Unfurl v2025.02 Released](/content/images/size/w2000/2025/02/unfurl-deceptive-ip-address.png)

A new Unfurl release is here! v2025.02 adds new features and some fixes, including:

* Parsing of IP addresses, including encoded or obfuscated variants
* Resolving Bluesky handles to their backing identifiers (DIDs), and then looking up that DID in the plc.directory audit log to find its creation timestamp
* Bug fixes and speed enhancements for bulk parsing

This is a relatively small release; but in addition to the new features, it fixes a few bugs (see the full changelog on the [GitHub release page](https://github.com/obsidianforensics/unfurl/releases/tag/v2025.02?ref=dfir.blog)). [Get it now](https://dfir.blog/unfurl-parses-obfuscated-ip-addresses/#get-it), or read on for more details about the new features!

### Parsing of IP Addresses (in many forms)

Unfurl previously only parsed domain names, but now can correctly recognize IP addresses. Not just IPs as they most typically appear (like 8.8.8.8 or 10.0.0.1), but in other forms, which are often used by attackers to try to obscure the actual destination (like http://example.com@1157586937). Below are more supported examples (from a [Trustwave report](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/evasive-urls-in-spam/?ref=dfir.blog)); all examples point to a Google IP:

* Dotted decimal IP address: [https://216.58.199.78](https://216.58.199.78/?ref=dfir.blog) (the most common)
* Octal IP address: [https://0330.0072.0307.0116](https://216.58.199.78/?ref=dfir.blog) (convert each decimal number to octal)
* Hexadecimal IP address: [https://0xD83AC74E](https://216.58.199.78/?ref=dfir.blog) (convert each decimal number to hexadecimal)
* Integer or DWORD IP address: [https://3627730766](https://216.58.199.78/?ref=dfir.blog) (convert hexadecimal IP to integer)

![](https://dfir.blog/content/images/2025/02/unfurl-deceptive-ip-address-1.png)

Unfurl parsing a deceptive URL with a username and encoded IP address

### Parsing and Lookups of Bluesky Handles

Unfurl added support for parsing the embedded timestamps out of Bluesky post IDs ("TIDs") in the v2024.11 release; this latest release adds the ability to resolve a Bluesky handle to its underlying `did` , then consult the plc.directory audit log to see when that `did` was created.

![](https://dfir.blog/content/images/2025/02/unfurl-bsky-timestamps.png)

Unfurl parsing a bsky.app URL, showing the handle creation and the post timestamps

ℹ️

Note: both the handle resolution and reading the creation timestamp from the audit log require a remote lookup, which is disabled by default in the local Python version. You can enable it by changing the `unfurl.ini` file.

## Get it!

Those are the major items in this Unfurl release. There are more changes that didn't make it into the blog post; check out the [release notes](https://github.com/obsidianforensics/unfurl/releases/tag/v2025.02?ref=dfir.blog) for more. To get Unfurl with these latest updates, you can:

* use it online at [dfir.blog/unfurl](https://dfir.blog/unfurl/) or [unfurl.link](https://unfurl.link/?ref=dfir.blog)
* if using pip, `pip install dfir-unfurl -U` will upgrade your local Unfurl to the latest
* View the release on [GitHub](https://github.com/obsidianforensics/unfurl/releases/tag/v2025.02?ref=dfir.blog)

All features work in both the web UI and command line versions.

[![Unfurl 2025.03](/content/images/size/w600/2025/03/unfurl-google-udm-3.png)](/unfurl-parses-googe-udm-and-truth-social/)

[## Unfurl 2025.03

Unfurl v2025.03 adds new features, including
parsing Google Search's UDM parameter, support for Mastodon forks (like Truth Social), and a utility parser to "clean up" inputs.](/unfurl-parses-googe-udm-and-truth-social/)

Mar 13, 2025
3 min read

[## Hindsight v2025.03 Released!

Hindsight v2025.03 focuses on Extensions - parsing more activity and state records, highlighting Extension permissions, and making it easier to examine Manifests.](/hindsight-parses-browser-extensions/)

Mar 11, 2025
2 min read

[![Authenticating Screenshots from Netflix's Carry-On Movie](/content/images/size/w600/2025/01/carry-on-google-search-url-1.png)](/authenticating-screenshots-from-netflix-carry-on-movie/)

[## Authenticating Screenshots from Netflix's Carry-On Movie

I watch Netflix's Carry-On, notice a real Google Search URL on screen, extract lots of data points from it and "authenticate" the screenshot.](/authenticating-screenshots-from-netflix-carry-on-movie/)

Jan 13, 2025
6 min read

[dfir.blog](https://dfir.blog) © 2025

[Powered by Ghost](https://ghost.org/)