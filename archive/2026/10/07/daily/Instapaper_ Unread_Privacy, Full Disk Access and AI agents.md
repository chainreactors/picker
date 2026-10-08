---
title: Privacy, Full Disk Access and AI agents
url: https://eclecticlight.co/2026/10/06/privacy-full-disk-access-and-ai-agents/
source: Instapaper: Unread
date: 2026-10-07
fetch_date: 2026-10-08T08:08:25.102921
---

# Privacy, Full Disk Access and AI agents

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [All Macs](https://eclecticlight.co/mac-problem-solving-2-2/)
* [M1-M5 Macs](https://eclecticlight.co/m1-macs-2/)
* [Troubleshooting](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Painting](https://eclecticlight.co/painting-topics-2-2/)
* [Mac Front Page](https://eclecticlight.co/category/macs/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[October 6, 2026](https://eclecticlight.co/2026/10/06/privacy-full-disk-access-and-ai-agents/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# Privacy, Full Disk Access and **AI** agents

You’ll probably have heard that Apple is urgently reviewing privacy protection in macOS, and intends enforcing stricter use of Full Disk Access in Privacy & Security settings. This article explains what’s going on, and why we all need to be concerned.

#### Privacy protection

Over the last decade threats to the privacy of our data have both changed and grown substantially. Although some reflect the rising success of stealer malware, the greatest threats to most users come from the apparently benign services and apps we use daily. Rather than abandoning us to fend for ourselves in this increasingly hostile world, Apple wants its operating systems to provide the tools we need to protect our own privacy, and has been building them in since macOS Mojave.

Protecting privacy is complex, and macOS protections have become increasingly complex with time. One of the early distinctions made was in folders and locations that apps and services have access to. Although Apple doesn’t provide a single, coherent list or account, at present the following appear to be those most frequently encountered:

* ~/Documents
* ~/Downloads
* ~/Desktop
* removable volumes
* iCloud Drive
* third-party cloud storage
* network volumes.

The first three are by far the most common in the majority of Macs, with Removable Volumes close behind. Others are more dependent on your hardware configuration, for example whether you use network shares or third-party cloud services.

[![](https://eclecticlight.co/wp-content/uploads/2026/04/privacya2.jpg)](https://eclecticlight.co/wp-content/uploads/2026/04/privacya2.jpg)

There are separate systems controlling different forms of access. When we explicitly select a file using the standard Open File dialog, we express our **intent** to read that file, and don’t need to separately grant that app access to that folder. Separate and tighter controls are applied to locations and files apps and services want to access without involving us, and that’s distinguished as occurring by **consent**, and controlled in those long lists in Privacy & Security settings.

#### Full Disk Access

Current settings are blunt tools. If you want an app to be able to crawl through folders inside your Home folder looking for particular types of extended attribute, or checking whether encoded Spotlight search can find files there, the only way is to give that app Full Disk Access.

This is common practice for Terminal, otherwise some of the commands we want to run won’t be allowed access to many folders or files. It’s also essential for backup utilities, or few of the files on our Macs would be backed up. Full Disk Access is sweeping, and gives access to some of the most sensitive data in the Home folder, such as the content of Messages and Mail.

#### AI agents

This has recently changed again with the introduction of AI agents, as available in the USA with Meta’s new app Muse. While these have some superficial similarities with features being introduced in Siri AI, there are important differences. Give Muse a goal, and it uses AI to work out how to achieve that, then runs that on your behalf. To be effective, it relies on having access to all your most private data. Muse isn’t unique, and ChatGPT agents and Microsoft Copilot assistants are rapidly heading in the same direction.

Meta [states clearly](https://www.meta.com/help/artificial-intelligence/1126304576638594/?srsltid=AU7gw4VVYeOHVgtbYsOI_ImHFU14e0PRZKcnjH8R2IpE1cCqMu6x3uMY) that “your agent can also read info from the apps on your computer, such as iMessage, Notes, Reminders, Email and Calendar”. “To let your agent use your computer, you’ll be asked to grant Muse permissions that are set and controlled by macOS, not by Meta: Full disk access, so your agent can find, read or update files. This permission covers all the files on your Mac, but your agent only uses the files and app information that you ask it to work with.”

#### Vulnerabilities

These agents, like the whole of AI, make mistakes. Muse’s documentation recognises that agents “may be inaccurate or take unexpected actions”. What you may not realise is that [you are solely responsible](https://muse.ai/terms) for those, and anything else its agents might do. Advice offered to those starting to use AI agents is to begin with “low-risk” tasks such as reading messages rather than sending them, and only giving the agent access to specific services as it needs them. The concept of low- and high-risk tasks should be ringing alarm bells.

Because of their nature, agents are also inherently vulnerable to external manipulation using techniques such as [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection), where crafted content is intentionally presented to the agent as directions that steer it away from its original intent. Muse has already had security vulnerabilities [detected and reported](https://x.com/objective_see/status/2106053368846442731) by Patrick Wardle of the Objective-See Foundation.

AI agents maintain logs of their activity, but nothing as detailed and auditable as Apple Intelligence Reports. Even if you spend time studying those logs, they can only tell you what has already happened.

#### Changes coming

Whether or not you would ever want to unleash AI agents on your Mac, Apple does need to refine Full Disk Access as a matter of urgency. But its design and engineering cannot be rushed. Merely adding to the complexity of current Privacy settings wouldn’t help users, many of whom already find privacy protection confusing and opaque.

An alternative approach would be more radical, and that would be to consider AI agents as potentially malicious code, which they are by their vendors’ own admissions. Apple would then have good grounds for refusing to notarise them, and would be obliged to exclude them from its App Stores. Despite the strength of that case, I don’t see Apple being as confrontational, and it will try instead to refine the existing Full Disk Access to encourage users to limit the damage that AI agents could do. It remains to be seen whether that proves effective.

I don’t think any of us had expected macOS Golden Gate to *restrict* what AI can do.

#### Recommendation

According to its documentation, Muse’s AI agents “may be inaccurate or take unexpected actions”, but can be trusted to “only [use] the files and app information that you ask it to work with.” And if anything does go wrong, you are solely responsible. If you are tempted to try AI agents in Muse or any other third-party product, don’t grant them Full Disk Access until Apple has fully addressed the issue of privacy.

### Share this:

* [Share on X (Opens in new window)
  X](https://eclecticlight.co/2026/10/06/privacy-full-disk-access-and-ai-agents/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2026/10/06/privacy-full-disk-access-and-ai-agents/?share=facebook)
* [Share on Reddit (Opens in new window)
  Reddit](https://eclect...