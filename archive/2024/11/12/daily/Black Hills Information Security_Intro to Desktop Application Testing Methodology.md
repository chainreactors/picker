---
title: Intro to Desktop Application Testing Methodology
url: https://www.blackhillsinfosec.com/intro-to-desktop-application-testing-methodology-wrapup/
source: Black Hills Information Security
date: 2024-11-12
fetch_date: 2025-10-06T19:19:10.823052
---

# Intro to Desktop Application Testing Methodology

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

11
Nov
2024

[Webcast Wrap-Up](https://www.blackhillsinfosec.com/category/webcast-wrap-up/)
[Craig Vincent](https://www.blackhillsinfosec.com/tag/craig-vincent/), [Desktop Application Testing](https://www.blackhillsinfosec.com/tag/desktop-application-testing/), [DLL Hijacking](https://www.blackhillsinfosec.com/tag/dll-hijacking/), [penetration testing](https://www.blackhillsinfosec.com/tag/penetration-testing/), [Pentesting](https://www.blackhillsinfosec.com/tag/pentesting/)

# [Intro to Desktop Application Testing Methodology](https://www.blackhillsinfosec.com/intro-to-desktop-application-testing-methodology-wrapup/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/WC_wrap-up_W0009.png)

*This webcast was originally published on October 24, 2024.*

In this video, experts delve into the intricacies of desktop application penetration testing methodologies. They discuss various techniques to thoroughly evaluate application security, including memory analysis, DLL hijacking, and network analysis. The conversation also highlights the importance of creating a comprehensive testing strategy and the value of documenting findings during the testing process.

* The webinar discussed a comprehensive approach to pen testing desktop applications, emphasizing the importance of understanding the application thoroughly before diving into complex reverse engineering tasks.
* The presenter advocates for a detailed scoping process during a pen test to ensure that all relevant components and potential vulnerabilities are within the scope of the test.
* The importance of reporting as you go was highlighted as a key methodology in pen testing, facilitating a seamless documentation process and ensuring thoroughness.

## Highlights

## Full Video

## Transcript

**Craig Vincent**

Yeah. So who am I? Obviously, I guess I test a lot. I didn’t know that, but I do a lot of pen tests. I study computer science, computer security and math.

In college, that’s kind of how I got into infosec in terms of learning, security stuff from technical perspective. And they also kind of point us and they’re like, hey, there’s a thing called defcon.

There’s this, Linux distro with all these hacking tools on it kind of point us in the right direction for where to go for resources to learn on our own. when I graduated, I started working, pretty much right away as a software developer.

Didn’t really like writing software all that much. So I was like, well, I know this computer security stuff. Like, let me get good at that and try to get a job doing that. And initially I wanted to be, a malware analyst because, like, the whole stuxnet thing happened recently.

I think I read Countdown to Zero Day, like right when it came out. And I was like, man, that sounds really cool. I want to learn that. And so you learn by doing it.

So I, like, had my home lab and I was doing reverse engineering stuff. I think it was open security training info, or DOT info, was a website that had a lot of, like, reverse, engineering, binary analysis, webcasts, and kind of, like, trainings.

And it was all free and on YouTube. And so I went through all that and then I started doing, like, reverse mes and Crackmes and looking at some, like, older, like, malware samples. And I was like, okay, I’m getting okay at this.

And then I was like, I really don’t like this. I don’t want to do this anymore than I want to do software development. So I was like, I hadn’t really considered pen testing. I used to think that, like, those guys are boring.

They just run scanners and stuff and then write a report about it. And then I saw Security Weekly. There was this guy on there who had a pen test company, and he’s talking about pen test Puppy mills and how it doesn’t have to be like that, that.

And I was like, okay, let me try that. So it was back to square one. home lab, intentionally vulnerable VMs, like a damn vulnerable web app, like, just learning hacking skills, right?

So that led to me getting a security job doing red teaming. And then right after that, I came to Black Hills, and I’ve been here ever since.

Other things you can get me to not shut up about are golf, football, swimming. So if you ever want to hang out at the con or something to talk about stuff and get me to not shut up, those are all good starters.

So as Jason mentioned, this is not a, a vuln research, like zero day exploit development, like reverse engineering talk, right?

Because that’s what I. That was my initial thing. I was like, they’re like, hey, Craig, we got this test. It’s a desktop application. And I was like, okay, well, what’s the expectation there, right? And initially I kind of panicked because I was like thinking.

I was lik...