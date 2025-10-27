---
title: CyberPipe v5.1 – Streamlined Profiles, Better Flexibility
url: https://bakerstreetforensics.com/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/
source: Instapaper: Unread
date: 2025-05-15
fetch_date: 2025-10-06T22:31:29.553268
---

# CyberPipe v5.1 – Streamlined Profiles, Better Flexibility

[Skip to content](#content)

[Baker Street Forensics](https://bakerstreetforensics.com/)

Where Irregulars are part of the Game

Menu

* [Blog](https://bakerstreetforensics.com/blog/)
* [Links, Resources & Swag](https://bakerstreetforensics.com/resources/)

[![](https://bakerstreetforensics.com/wp-content/uploads/2022/05/output-onlinepngtools-4.png)](https://bakerstreetforensics.com/)

![](https://bakerstreetforensics.com/wp-content/uploads/2025/05/screenshot.png?w=924&h=0&crop=1)

# CyberPipe v5.1 – Streamlined Profiles, Better Flexibility

[DFIR](https://bakerstreetforensics.com/category/dfir/), [Forensics](https://bakerstreetforensics.com/category/forensics/), [PowerShell](https://bakerstreetforensics.com/category/powershell/), [RAM](https://bakerstreetforensics.com/category/ram/), [Triage](https://bakerstreetforensics.com/category/triage/), [USB](https://bakerstreetforensics.com/category/usb/)

CyberPipe v5.1 is out with a few targeted improvements to make live response a bit smoother.

### **What’s New:**

* **Collection profiles can now be passed directly as arguments** using -CollectionProfile. No need to modify the script or hardcode anything — just run with the profile you need.
* **Improved support for saving to network shares**, ideal for remote collections triggered by EDR.
* **Better error handling and logging**, including clearer messages when tools are missing or when BitLocker key recovery fails.

The **default profile** still covers the most common triage needs:

✔️ Memory dump (RAM)

✔️ Pagefile

✔️ Volatile data (network config, hives, running procs)

✔️ System artifacts

But now, you can swap that out on the fly:

### **Usage Examples:**

```
.\CyberPipe.ps1 ## default profile, capture RAM, Pagefile, Volatile and System Files

.\CyberPipe.ps1 -CollectionProfile RAMOnly ## just the RAM

.\CyberPipe.ps1 -CollectionProfile RAMSystem ## just the RAM and System Files (triage lite)

.\CyberPipe.ps1 -CollectionProfile RAMPage ## RAM & Pagefile

.\CyberPipe.ps1 -CollectionProfile Volatile ## Just Volatile data
```

Useful for tailoring collections based on available time, scope, or system stability — especially during incident response where conditions change quickly.

CyberPipe still captures memory with DumpIt or RAM Capture, grabs volatile system data, checks for encryption, and recovers the BitLocker key when possible. But now it’s just a bit easier to tailor to the job at hand — whether you’re responding interactively or invoking it remotely via EDR integration.

As always, **no dependencies beyond what’s in the Tools folder**, and **no assumptions about the system** you’re collecting from.

See the full changelog and usage notes in the [README on GitHub](https://github.com/dwmetz/CyberPipe).

### Share this:

* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://bakerstreetforensics.com/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://bakerstreetforensics.com/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/?share=reddit)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://bakerstreetforensics.com/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/?share=bluesky)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://bakerstreetforensics.com/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/?share=mastodon)

Like Loading...

### *Related*

[May 8, 2025](https://bakerstreetforensics.com/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/) [Doug Metz](https://bakerstreetforensics.com/author/dwmetz/)[CyberPipe](https://bakerstreetforensics.com/tag/cyberpipe/), [DFIR](https://bakerstreetforensics.com/tag/dfir/), [Forensics](https://bakerstreetforensics.com/tag/forensics/), [Github](https://bakerstreetforensics.com/tag/github/), [Magnet](https://bakerstreetforensics.com/tag/magnet/), [Memory](https://bakerstreetforensics.com/tag/memory/), [PowerShell](https://bakerstreetforensics.com/tag/powershell/)

## One thought on “CyberPipe v5.1 – Streamlined Profiles, Better Flexibility”

1. Pingback: [Week 19 – 2025 – This Week In 4n6](http://thisweekin4n6.com/2025/05/11/week-19-2025/)

## Leave a comment [Cancel reply](/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/#respond)

Δ

## Post navigation

[Previous Previous post: MalChela v2.1 Released: Smoother Workflows, Easier Tool Integration](https://bakerstreetforensics.com/2025/05/02/malchela-v2-1-released-smoother-workflows-easier-tool-integration/)

[Next Next post: MalChela 2.2 “REMnux” Release](https://bakerstreetforensics.com/2025/05/21/malchela-2-2-remnux-release/)

Search for:

* [GitHub](https://github.com/dwmetz)
* [Mastodon](https://infosec.exchange/%40dwmetz)
* [Link](https://linktr.ee/dwmetz)
* [Twitter](https://twitter.com/dwmetz)
* [LinkedIn](https://www.linkedin.com/in/dwmetz/)

## Recent Posts

* [Is your USB device slowing down your forensic investigation?](https://bakerstreetforensics.com/2025/08/27/is-your-usb-device-slowing-down-your-forensic-investigation/)
  August 27, 2025
* [Enhance Threat Hunting with MITRE Lookup in MalChela 3.0.2](https://bakerstreetforensics.com/2025/08/02/enhance-threat-hunting-with-mitre-lookup-in-malchela-3-0-2/)
  August 2, 2025
* [Toby-Find: Simplifying Command-Line Forensics Tools](https://bakerstreetforensics.com/2025/07/29/toby-find-simplifying-command-line-forensics-tools/)
  July 29, 2025
* [Sharper Strings and Smarter Signals: MalChela 3.0.1](https://bakerstreetforensics.com/2025/07/28/sharper-strings-and-smarter-signals-malchela-3-0-1/)
  July 28, 2025
* [Portable Forensics with Toby: A Raspberry Pi Toolkit](https://bakerstreetforensics.com/2025/07/20/portable-forensics-with-toby-a-raspberry-pi-toolkit/)
  July 20, 2025

[Website Powered by WordPress.com](https://wordpress.com/?ref=footer_custom_powered).

* [Comment](https://bakerstreetforensics.com/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/#comments)
* Reblog
* Subscribe
  Subscribed

  + [![](https://bakerstreetforensics.com/wp-content/uploads/2022/08/image-1.jpg?w=50) Baker Street Forensics](https://bakerstreetforensics.com)

  Join 61 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fbakerstreetforensics.com%252F2025%252F05%252F08%252Fcyberpipe-v5-1-streamlined-profiles-better-flexibility%252F)
* + [![](https://bakerstreetforensics.com/wp-content/uploads/2022/08/image-1.jpg?w=50) Baker Street Forensics](https://bakerstreetforensics.com)
  + Subscribe
    Subscribed
  + [Sign up](https://wordpress.com/start/)
  + [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fbakerstreetforensics.com%252F2025%252F05%252F08%252Fcyberpipe-v5-1-streamlined-profiles-better-flexibility%252F)
  + [Copy shortlink](https://wp.me/pcr4Uh-Hh)
  + [Report this content](https://wordpress.com/abuse/?report_url=https://bakerstreetforensics.com/2025/05/08/cyberpipe-v5-1-streamlined-profiles-better-flexibility/)
  + [View post in Reader](https://wordpress.com/reader/blogs/183769753/posts/2683)
  + [Manage subscriptions](https://subscribe.wordpress.com/)
  + Collapse this bar

%d

![](https://pixel.wp.com/b.gif?v=noscript)