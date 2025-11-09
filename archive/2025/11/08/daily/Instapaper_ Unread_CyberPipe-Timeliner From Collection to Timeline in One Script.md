---
title: CyberPipe-Timeliner From Collection to Timeline in One Script
url: https://bakerstreetforensics.com/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/
source: Instapaper: Unread
date: 2025-11-08
fetch_date: 2025-11-09T03:14:49.573415
---

# CyberPipe-Timeliner From Collection to Timeline in One Script

[Skip to content](#content)

[Baker Street Forensics](https://bakerstreetforensics.com/)

Where Irregulars are part of the Game

Menu

* [Blog](https://bakerstreetforensics.com/blog/)
* [Links, Resources & Swag](https://bakerstreetforensics.com/resources/)

[![](https://bakerstreetforensics.com/wp-content/uploads/2022/05/output-onlinepngtools-4.png)](https://bakerstreetforensics.com/)

![](https://bakerstreetforensics.com/wp-content/uploads/2025/11/flow.png?w=924&h=0&crop=1)

# CyberPipe-Timeliner: From Collection to Timeline in One Script

[DFIR](https://bakerstreetforensics.com/category/dfir/), [PowerShell](https://bakerstreetforensics.com/category/powershell/), [Triage](https://bakerstreetforensics.com/category/triage/), [Windows](https://bakerstreetforensics.com/category/windows/)

You know how these things go. A colleague asks a simple question, and before you know it, you’re knee-deep in PowerShell creating something that didn’t exist a few weeks ago. That’s exactly how **CyberPipe-Timeliner** came to be.

After a recent update to [CyberPipe](https://github.com/dwmetz/CyberPipe/tree/main), someone asked whether there was a way to pipe Magnet Response collections through to something like [ForensicTimeliner](https://github.com/acquiredsecurity/forensic-timeliner). It was one of those “that should exist” moments. So I made it exist.

## A Quick History Lesson

![](https://bakerstreetforensics.com/wp-content/uploads/2025/11/pfr.jpg?w=500)

For those who haven’t been following along, CyberPipe (formerly CSIRT-Collect) has been around since my IR days. It went public in 2021 and has been steadily maintained and updated since then. The tool has proven itself useful for rapid incident response collection, and it’s evolved based on real-world needs and feedback from the community.

CyberPipe-Timeliner is its companion project—taking that collection data and turning it into something immediately actionable: a unified forensic timeline.

## What It Actually Does

The script automates the entire workflow from collection to timeline:

**Extraction** – It unpacks your Magnet Response archive, whether that’s a ZIP file or an already-extracted directory.

**Processing** – All the heavy lifting happens here using Eric Zimmerman’s EZ Tools to generate CSVs from your artifacts.

**Organization** – The CSVs get structured specifically for ForensicTimeliner compatibility, because nobody wants to spend time wrestling with file formats.

**Aggregation** – Everything merges into a consolidated timeline, giving you that unified view we’re all after.

![](https://bakerstreetforensics.com/wp-content/uploads/2025/11/cyberpipe_timeliner_screenshot.png?w=956)

## Built for Real-World Use

The script includes some practical features that came from actual use cases:

* **Date filtering** – Need to focus on a specific incident window? Use `-StartDate` and `-EndDate` to narrow your timeline to what matters.
* **Flexible input** – Point it at a ZIP file or an already-extracted collection folder. Either works.
* **Verbose and diagnostic modes** – Because sometimes you need to see exactly what’s happening under the hood.
* **Auto-generated output folders** – Timestamped folders keep your timelines organized without any extra effort.

## Getting Started

Setting it up is straightforward. You’ll need PowerShell 7+, [Eric Zimmerman’s EZ Tools](https://ericzimmerman.github.io/#!index.md), ForensicTimeliner, and Microsoft .NET SDK (v9 recommended). The [GitHub repository](https://github.com/dwmetz/CyberPipe-Timeliner) has detailed setup instructions, including handy one-liners for downloading and configuring the required tools.

Once you’re set up, a basic run looks like this:

```
.\CyberPipe-Timeliner.ps1 -InputFile "collection.zip"
```

That’s it. The script handles the rest, creating a timestamped output folder with your complete timeline.

## Why It Matters

Forensic timeline generation shouldn’t be a multi-tool, multi-step headache. CyberPipe-Timeliner takes what would normally be several manual processes and condenses them into a single automated pipeline. You collect with Magnet Response or CyberPipe, run the timeliner script, and get actionable timeline data.

It’s available now on [GitHub](https://github.com/dwmetz/CyberPipe-Timeliner), and as always, feedback and contributions are welcome. If you run into issues or have ideas for improvements, open an issue or reach out.

Sometimes the best tools come from simple questions and the willingness to build the answer.

### Share this:

* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://bakerstreetforensics.com/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://bakerstreetforensics.com/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/?share=reddit)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://bakerstreetforensics.com/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/?share=bluesky)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://bakerstreetforensics.com/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/?share=mastodon)

Like Loading...

### *Related*

[November 5, 2025November 5, 2025](https://bakerstreetforensics.com/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/) [Doug Metz](https://bakerstreetforensics.com/author/dwmetz/)[Automation](https://bakerstreetforensics.com/tag/automation/), [DFIR](https://bakerstreetforensics.com/tag/dfir/), [Forensics](https://bakerstreetforensics.com/tag/forensics/), [Github](https://bakerstreetforensics.com/tag/github/), [Magnet](https://bakerstreetforensics.com/tag/magnet/), [PowerShell](https://bakerstreetforensics.com/tag/powershell/), [Timeline](https://bakerstreetforensics.com/tag/timeline/)

## Leave a comment [Cancel reply](/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/#respond)

Δ

## Post navigation

[Previous Previous post: CyberPipe v5.3: Enhanced PowerShell Compatibility and Reliability](https://bakerstreetforensics.com/2025/11/04/cyberpipe-v5-3-enhanced-powershell-compatibility-and-reliability/)

Search for:

* [GitHub](https://github.com/dwmetz)
* [Mastodon](https://infosec.exchange/%40dwmetz)
* [Link](https://linktr.ee/dwmetz)
* [Twitter](https://twitter.com/dwmetz)
* [LinkedIn](https://www.linkedin.com/in/dwmetz/)

## Recent Posts

* [CyberPipe-Timeliner: From Collection to Timeline in One Script](https://bakerstreetforensics.com/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/)
  November 5, 2025
* [CyberPipe v5.3: Enhanced PowerShell Compatibility and Reliability](https://bakerstreetforensics.com/2025/11/04/cyberpipe-v5-3-enhanced-powershell-compatibility-and-reliability/)
  November 4, 2025
* [Streamline Digital Evidence Collection with CyberPipe 5.2](https://bakerstreetforensics.com/2025/10/16/streamline-digital-evidence-collection-with-cyberpipe-5-2/)
  October 16, 2025
* [Cross-Platform DFIR Tools: MalChelaGUI on Windows](https://bakerstreetforensics.com/2025/10/07/cross-platform-dfir-tools-malchelagui-on-windows/)
  October 7, 2025
* [Is your USB device slowing down your forensic investigation?](https://bakerstreetforensics.com/2025/08/27/is-your-usb-device-slowing-down-your-forensic-investigation/)
  August 27, 2025

[Website Powered by WordPress.com](https://wordpress.com/?ref=footer_custom_powered).

* [Comment](https://bakerstreetforensics.com/2025/11/05/cyberpipe-timeliner-from-collection-to-timeline-in-one-script/#respond)
* Reblog
* Subscribe
  Subscribed

  + [![](https://bakerstreetforensics.com/wp-content/uploads/2022/08/image-1.jpg?w=50) Baker Street Forensics](https://bakerstreetforensics.com)

  Join 61 other subscribers

  Sign me up

  + Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A...