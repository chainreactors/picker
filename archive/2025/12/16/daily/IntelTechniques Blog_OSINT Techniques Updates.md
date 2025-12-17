---
title: OSINT Techniques Updates
url: https://inteltechniques.com/blog/2025/12/16/osint-techniques-updates/
source: IntelTechniques Blog
date: 2025-12-16
fetch_date: 2025-12-17T03:20:21.272849
---

# OSINT Techniques Updates

[Skip to content](#main)

[# IntelTechniques](https://inteltechniques.com)

[IntelTechniques Blog](https://inteltechniques.com/blog/)

* [Training](https://inteltechniques.com/training.html)
* [Services](https://inteltechniques.com/services.html)
* [Resources](https://inteltechniques.com/links.html)
* [Tools](https://inteltechniques.com/tools/)
* [Blog](https://inteltechniques.com/blog/)
* [Podcast](https://inteltechniques.com/podcast.html)
* [Magazine](https://unredactedmagazine.com)
* [Books](https://inteltechniques.com/books.html)
* [Contact](https://inteltechniques.com/contact.html)

# OSINT Techniques Updates

* [Posted on
  December 16, 2025](https://inteltechniques.com/blog/2025/12/16/osint-techniques-updates/)
* Posted in
  [OSINT](https://inteltechniques.com/blog/category/osint/)

We recently overhauled the entire OSINT VM build including the following.

Updated all steps within the install.sh script and linux.txt file for Debian 13. Only use Debian 13 for new VMs!
Modified all pip3 commands to match pip.
Transitioned many installations to pipx.

The big one:

Updated install.sh script and linux.txt file to remove all virtual environments and sudo pip usage.

Details:

This is due to changes within Debian 13 and the apps we use, allowing them to talk with each other appropriately and globally. In previous books, we just used pip to install Linux application dependencies. Security changes in Python blocked this behavior in 2024, so we had to pivot. We intended on switching to Python virtual environments (venv) which would properly isolate all of our pip installations, but that caused other problems. The various applications we installed did not work properly with fellow software which wanted them installed globally (not in venv). Since this is a VM, we made the choice to use venv to bypass Python trying to block our installations, but used sudo within venv to allow global installation. Basically, we cheated. If this were a host Linux system and you wanted to install software which might conflict with other applications, then I would not recommend this route. I would avoid using sudo within venv. For a VM which will only be used for online investigations, I had no issue with this. After the book was released, we were able to block almost all pip errors in Debian 13, so we eliminated all of the venv options from the online steps for simplicity, since they were not providing any real protection anyway.

Basically, either option works the same way, however, we always encourage readers to follow the online steps over the book. Much has been updated to reflect installation changes. If I were writing a new OSINT book today (I am not), and rebuilding the OSINT VM, I would find a way to make everything work appropriately within Python virtual environments, including a full re-write of every script. Since so many people rely on the scripts as they are, I elected to cheat with venv a bit to make things function at the time. You are correct to question this logic though.

**Summary:** If your OSINT VM is not working great, rebuild it from scratch with Debian 13 using the updated steps we have posted online. You can get these from the OSINT portal URL in your copy of OSINT Techniques, 11th edition, or the linux.txt file in the link present within the OSINT Techniques VM guide. Both are the same.

* [« Previous Post](https://inteltechniques.com/blog/2025/10/10/unredacted-magazine-issue-009/)

The RSS feed for this blog is at
<https://inteltechniques.com/blog/feed/>.

#### Recent Posts

* [OSINT Techniques Updates](https://inteltechniques.com/blog/2025/12/16/osint-techniques-updates/)
* [UNREDACTED Magazine Issue 009](https://inteltechniques.com/blog/2025/10/10/unredacted-magazine-issue-009/)
* [UNREDACTED Magazine Issue 008](https://inteltechniques.com/blog/2025/09/05/unredacted-magazine-issue-008/)
* [Extreme Privacy Update: E2EE Email Guide](https://inteltechniques.com/blog/2025/07/12/extreme-privacy-update-e2ee-email-guide/)
* [Virtual Currency Payments Return](https://inteltechniques.com/blog/2025/07/11/virtual-currency-payments-return/)
* [Extreme Privacy Update: Self-Hosted SearXNG Guide](https://inteltechniques.com/blog/2025/07/11/extreme-privacy-update-self-hosted-searxng-guide/)
* [Extreme Privacy Update: Windows 10 EOL](https://inteltechniques.com/blog/2025/07/08/extreme-privacy-update-windows-10-eol/)
* [Extreme Privacy Update: KnockKnock Script](https://inteltechniques.com/blog/2025/07/05/extreme-privacy-update-knockknock-script/)
* [OSINT Techniques Updates: inurl & Amass path](https://inteltechniques.com/blog/2025/07/05/osint-techniques-updates-inurl-amass-path/)
* [New Digital Book Provider](https://inteltechniques.com/blog/2025/04/02/new-digital-book-provider/)
* [New Ebook Updates](https://inteltechniques.com/blog/2025/04/02/new-ebook-updates/)
* [Executive EDC Bags](https://inteltechniques.com/blog/2025/01/05/executive-edc-bags/)
* [Books Updated](https://inteltechniques.com/blog/2024/11/29/books-updated/)
* [OSINT Techniques 11th Edition Now Available](https://inteltechniques.com/blog/2024/11/10/osint-techniques-11th-edition-now-available/)
* [Digital Guide Updates 2024.11.01](https://inteltechniques.com/blog/2024/11/02/digital-guide-updates-2024-11-01/)
* [Digital Guide Updates 2024.10.01](https://inteltechniques.com/blog/2024/09/30/digital-guide-updates-2024-10-01/)
* [UNREDACTED Magazine Issue 007](https://inteltechniques.com/blog/2024/09/16/unredacted-magazine-issue-007/)
* [Major Books Update](https://inteltechniques.com/blog/2024/09/12/major-books-update/)
* [Digital Guide Updates 2024.09.01](https://inteltechniques.com/blog/2024/09/01/digital-guide-updates-2024-09-01/)
* [Extreme Privacy 5th Edition Now Available](https://inteltechniques.com/blog/2024/08/08/extreme-privacy-5th-edition-now-available/)
* [Extreme Privacy 5th Edition Available Soon](https://inteltechniques.com/blog/2024/08/05/extreme-privacy-5th-edition-available-soon/)
* [Digital Guide Updates 2024.08.01](https://inteltechniques.com/blog/2024/08/01/digital-guide-updates-2024-08-01/)
* [The Next Books](https://inteltechniques.com/blog/2024/07/01/the-next-books/)
* [Digital Guide Updates 2024.07.01](https://inteltechniques.com/blog/2024/07/01/digital-guide-updates-2024-07-01/)
* [More Bad Gun Safe OPSEC](https://inteltechniques.com/blog/2024/06/07/more-bad-gun-safe-opsec/)

* Copyright © 2009-2024 IntelTechniques.com
* All Rights Reserved
* [Privacy Policy](https://inteltechniques.com/privacy.html)