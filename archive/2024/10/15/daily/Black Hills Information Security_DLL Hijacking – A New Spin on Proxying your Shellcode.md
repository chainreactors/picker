---
title: DLL Hijacking – A New Spin on Proxying your Shellcode
url: https://www.blackhillsinfosec.com/dll-hijacking-a-new-spin-on-proxying-your-shellcode/
source: Black Hills Information Security
date: 2024-10-15
fetch_date: 2025-10-06T18:51:33.017838
---

# DLL Hijacking – A New Spin on Proxying your Shellcode

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

14
Oct
2024

[Informational](https://www.blackhillsinfosec.com/category/informational/), [Matthew Eidelberg](https://www.blackhillsinfosec.com/category/author/matthew-eidelberg/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/), [Webcasts](https://www.blackhillsinfosec.com/category/webcasts/)
[DLL](https://www.blackhillsinfosec.com/tag/dll/), [DLL Hijacking](https://www.blackhillsinfosec.com/tag/dll-hijacking/), [Webcast Wrap-Up](https://www.blackhillsinfosec.com/tag/webcast-wrap-up/)

# [DLL Hijacking – A New Spin on Proxying your Shellcode](https://www.blackhillsinfosec.com/dll-hijacking-a-new-spin-on-proxying-your-shellcode/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/WC_wrap-up_W0002.png)

*This webcast was originally published on October 4, 2024.*

In this video, experts delve into the intricacies of DLL hijacking and new techniques for malicious code proxying, featuring a comprehensive discussion on methodology and weaponization. The talk explores the practical application of these techniques in real-world engagements, addressing common questions from recent research releases. The speakers emphasize the importance of understanding DLL functionalities and the impact of Microsoft’s security measures, while also highlighting the effectiveness of continuous pen testing in discovering vulnerabilities.

* The webinar focused on DLL hijacking and new techniques for stealthy code execution via DLL proxying.
* Continuous Penetration Testing (CPT) allows for extensive research and development of advanced techniques tailored for hardened environments.
* The webinar emphasized the importance of simple yet effective methodologies for maintaining persistence and evading detection.

## Highlights

## Full Video

## Transcript

**Matthew Eidelberg**

So yes, this talk can be talking about DLL hijacking and some of the research I did to kind of come up with new techniques. I like to call it spin on proxying your shellcode through.

We’re actually going to be talking about the methodology that I kind of used to discover these vectors, how I weaponized it. And we’re going to be talking a lot about CPT with, Michael Allen on how we actually use this on engagement.

Because obviously it’s all well and fine to talk about the research around it, but how do you actually apply it? And that was something because we released the article in the research last week and I got a lot of questions around that.

So I’ve kind of tailored this to also address those questions. As we mentioned, a lot. this is all kind of came out of our CPT continuous testing team.

As you can see up in the top left-hand corner, you can see our little axolotl logo. With that in mind, I wanted to, before we dive into everything, kind of just level set, kind of give a prelude that, as we kind of start talking, there’s going to be a lot of terms that we are going to be saying that sound very familiar and it might be confusing, but unfortunately with DLL and DLL hijacking, side loading, all those sort of, terminologies, while they all sound different, they all kind of do something similar.

So I’m going to try to highlight as best as I can in a very brief, methodology review. So that way we all have a certain baseline of information and that’s really just to help understand, the infinite possibilities and what kind of set me down this path to start looking at these.

Obviously, when we’re tasked to look for any type of new, attacks or when we’re coming up against a long campaign, the biggest thing we have to do is look at what is known in the wild, what is getting caught, what we know is going to have a high level of risk, and then start kind of working backwards and see what can we find that’s not being talked about.

Something new or maybe something that’s maybe obscure. And one of the conversations we all had as a group was persistence, making something that we can have something last over a long period of time.

If you tuned in for the pre show banter we mentioned that, in these type of CPT operations, these gigs often go months, weeks, maybe half a year, so to speak.

So we want to kind of establish something that’s very persistent and something that won’t get us caught. So with that in mind, this is kind of how we approach this and the methodology and research I did and what I discovered.

Obviously, since we’re here to talk about DLL hijacking. What is DLL hijacking? So when we talk about DLL’s, we first have to kind of understand that a DLL is a library of functions that a process can load in that then they can call.

So the most notable one is probably NT DLL. That’s t...