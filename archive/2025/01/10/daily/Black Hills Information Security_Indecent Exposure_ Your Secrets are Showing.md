---
title: Indecent Exposure: Your Secrets are Showing
url: https://www.blackhillsinfosec.com/indecent-exposure-your-secrets-are-showing/
source: Black Hills Information Security
date: 2025-01-10
fetch_date: 2025-10-06T20:09:05.402143
---

# Indecent Exposure: Your Secrets are Showing

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

9
Jan
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [moth](https://www.blackhillsinfosec.com/category/author/moth/)
[.Net](https://www.blackhillsinfosec.com/tag/net/), [C#](https://www.blackhillsinfosec.com/tag/c/), [Cryptography](https://www.blackhillsinfosec.com/tag/cryptography/), [PowerShell](https://www.blackhillsinfosec.com/tag/powershell/), [reverse engineering](https://www.blackhillsinfosec.com/tag/reverse-engineering/)

# [Indecent Exposure: Your Secrets are Showing](https://www.blackhillsinfosec.com/indecent-exposure-your-secrets-are-showing/)

by [moth](https://github.com/0x6d6f7468)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/Secrets_header.png)

Hard-coded cryptographic secrets? In *my* commercially purchased, closed-source software? It’s more likely than you think. Like, a ***lot*** more likely.

This blog post details a true story of cryptographic secret discovery, DLL modification, password recovery, and software platform compromise. Please note that all references to specifically targeted software have been scrubbed and all cryptographically sensitive materials have been simulated for the sake of telling this story, to hopefully avoid pissing too many people off.

Now, without further ado, on to our story…

### ***That’s No Hash…***

A few years ago, I was checking Teams notifications and saw the following message sent to all testers:

> *“Hash challenge – step 1, probably identification of hash type. used hash generator, no results seemed to align. The username is `dbadmin`, the hash is `I3bnJsdcK4qwstvVaekB5CzcT7ESjmR/xpB8IKNtMFc=`. Any suggestions would be amazing” – Jordan Drysdale, 2022-07-25*

Continuing my trend of being one of BHIS’ most “nerd snipe-able” gremlins, I decided to at least give that “hash” value a quick smell test and see if I couldn’t give something useful to my good pal Jordan Drysdale. At first glance, it seemed obvious that the hash value was at least base64-encoded, so I used Python to base64 decode the value, then converted it to a hex string, before finally using the `hashid` Linux utility to determine what hash type, if any, the value could possibly be. From the `hashid` command output, it looked like the hash might have been something like SHA-256.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/1-1024x582.png)

**Conversion of Possible Hash Value**

I tossed this back to Jordan on the off chance that it would be helpful, but something about the situation had me wondering: Was this really a hash at all? Where had Jordan found this value? At this point, I was fully invested and jumped on a call with him where he showed me a config file resembling the below screenshot.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/2-1024x323.png)

**CryptKeeper Configuration File**

As alluded to in this blog post’s introduction, “CryptKeeper” here is a stand-in for a software named “[REDACTED]” that is used by [REDACTED] organizations to help them manage their [REDACTED]. You can perhaps imagine how much I would love to not have the previous sentence redacted, but alas that is not the situation we find ourselves in. Just know that, as contrived as this example might seem, it is a very close simulation of what we found in the wild on that fateful engagement.

After talking it over, Jordan and I eventually arrived at a simple conclusion: That password value wasn’t hashed, it was encrypted. This was starting to get interesting.

### ***Sneaking a Peek***

At this point, Jordan opened a tool called [dnSpy](https://github.com/dnSpy/dnSpy) and opened one of the DLL files neighboring the configuration file that we found. In reality, this resulted in a bunch of assemblies being loaded, both from the third-party software and the .NET Framework itself. After some cursory browsing, Jordan eventually searched for the word “crypt”. This returned several results, many of which seemed especially enticing.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/3-1024x555.png)

**CryptKeeper Search Results**

As we could see, there appeared to be encryption and decryption methods, as well as three methods to get key, salt, and IV values for what appeared to be AES encryption. With that in mind, we cracked open the `RadicalRijndael` class from the `CryptKeeper.Security` namespace.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/4-1024x590.png)

**Cracking a Cold One with the Boys**

Well now, what have we here? Two public methods for encryption and decryption, which themselves retrieve what appeared to be static key, salt, and IV values before calling additional helper functions. We scrolled to the bottom of the c...