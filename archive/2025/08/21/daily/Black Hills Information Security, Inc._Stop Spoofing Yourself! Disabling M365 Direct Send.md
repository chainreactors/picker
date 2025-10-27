---
title: Stop Spoofing Yourself! Disabling M365 Direct Send
url: https://www.blackhillsinfosec.com/disabling-m365-direct-send/
source: Black Hills Information Security, Inc.
date: 2025-08-21
fetch_date: 2025-10-07T00:48:25.783241
---

# Stop Spoofing Yourself! Disabling M365 Direct Send

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

20
Aug
2025

[Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Hunt Teaming](https://www.blackhillsinfosec.com/category/blue-team/hunt-teaming/), [Incident Response](https://www.blackhillsinfosec.com/category/blue-team/incident-response/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/), [Patterson Cake](https://www.blackhillsinfosec.com/category/author/patterson-cake/)
[evtx](https://www.blackhillsinfosec.com/tag/evtx/), [hayabusa](https://www.blackhillsinfosec.com/tag/hayabusa/), [SOF-ELK](https://www.blackhillsinfosec.com/tag/sof-elk/)

# [Stop Spoofing Yourself! Disabling M365 Direct Send](https://www.blackhillsinfosec.com/disabling-m365-direct-send/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/PCake-Headshot-462x625-1-150x150.jpg)

| [Patterson Cake](https://www.blackhillsinfosec.com/team/patterson-cake/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/direct_send_header.png)

Remember the good ‘ol days of Zip drives, Winamp, the advent of “Office 365,” and copy machines that didn’t understand email authentication? Okay, maybe they weren’t so good! For a while there, as we migrated from on-prem Exchange to “Office 365” Exchange Online, we still needed to scan and email files from our multi-function devices, which had limited mail-delivery and authentication options. Microsoft’s solution was “Direct Send,” an automatically created, unauthenticated SMTP endpoint accepting mail for all of a tenant’s accepted domains. What could go wrong? Check out this blog post for details:  <https://www.blackhillsinfosec.com/spoofing-microsoft-365-like-its-1995/>

Although Direct Send is not new, we have seen a recent surge in threat actors abusing it, effectively “spoofing” someone inside your organization to someone else inside your organization. Lately, we’ve seen the threat actors claim that they’ve “hacked” your account to gain access to your mailbox, when in fact they’ve just sent you email as yourself via Direct Send! Thanks to Microsoft, no hacking required!

It’s important to note that while Direct Send can only be used to send to legitimate recipients within your tenant, it can also be used to “impersonate” a sender that does not exist in your tenant, as long as the domain is accepted, e.g. mail from ‘[[email protected]](/cdn-cgi/l/email-protection)’ (assuming that “yourbusiness.com” is legit and you don’t have a “Captain America” account).

This is just a side note, but if a threat actor messages you to let you know they’ve “hacked” your account, that’s often a good sign that they haven’t “hacked” your account! I’m not suggesting that you be dismissive of any such messages and/or indicators but checking Direct Send configuration should be a priority response!

Until recently, you couldn’t just disable Direct Send. You could implement an inbound connector or make some creative SPAM-detection rules, etc., but these were not trivial to configure and test, especially for a “service” that you may very well not use!

So, I have good news and bad news. Let’s start with the bad…there is no easy way to report on Direct Send utilization in your tenant (at the time of this writing, Direct Send reporting options were “in progress”). If you are uncertain as to whether or not Direct Send is being used for authorized business operations, you should conduct some internal review/discussion to identify legitimate use cases and consider implementing connectors accordingly: [Configure mail flow using connectors in Exchange Online | Microsoft Learn](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow)

Now for the good news! If you are confident that you do not have legitimate use cases for Direct Send and/or those use cases are covered by an existing connector, you can now test a new “Public Preview” command to easily disable Direct Send. As a counterpoint to the “bad news,” because of the simplicity of the command to disable Direct Send, you can also easily reenable it should you need to.

Before making any changes to your M365 tenant, I’m a huge fan of testing, documenting, changing, retesting, and updating your documentation!

To disable Direct Send, you’ll need to “enable” the “Reject Direct Send” feature. Clear as mud? Yeah, sorry…not my fault! First, you’ll need to authenticate to your tenant via Exchange Online PowerShell. General guidelines can be found here: <https://aka.ms/exov3-module>. Once you are authenticated, you can run the fo...