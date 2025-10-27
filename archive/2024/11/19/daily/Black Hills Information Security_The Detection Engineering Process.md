---
title: The Detection Engineering Process
url: https://www.blackhillsinfosec.com/the-detection-engineering-process-wrapup/
source: Black Hills Information Security
date: 2024-11-19
fetch_date: 2025-10-06T19:18:31.801099
---

# The Detection Engineering Process

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

18
Nov
2024

[Hayden Covington](https://www.blackhillsinfosec.com/category/author/hayden-covington/), [SOC](https://www.blackhillsinfosec.com/category/soc/)
[Alerting](https://www.blackhillsinfosec.com/tag/alerting/), [automation](https://www.blackhillsinfosec.com/tag/automation/), [detection engineering](https://www.blackhillsinfosec.com/tag/detection-engineering/), [detections](https://www.blackhillsinfosec.com/tag/detections/), [Security Operations Center](https://www.blackhillsinfosec.com/tag/security-operations-center/)

# [The Detection Engineering Process](https://www.blackhillsinfosec.com/the-detection-engineering-process-wrapup/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/WC_wrap-up_W0010.png)

*This webcast was originally published on November 8, 2024.*

In this video, Hayden Covington discusses the detection engineering process and how to apply the scientific method to improve the quality of detections. The discussion includes the steps involved in creating a high-quality detection, such as research, query building, backtesting, and continuous improvement. Hayden emphasizes the importance of structured processes, documentation, and the role of passion and enthusiasm in cybersecurity work.

* Detection engineering involves applying the scientific method to enhance the quality and consistency of detections.
* The process of creating a high-quality detection includes steps such as defining a detection story, conducting research, building a query, and continuous improvement.
* A structured detection engineering process can lead to better-defined scope, higher-quality detections, and improved overall security management.

## Highlights

## Full Video

## Transcript

**Jason Blanchard**

Hello, everybody, and welcome to today’s Black Hills Information Security webcast. My name is Jason Blanchard. I’m the content community director here at Black Hills. And if you ever need a Red Team threat hunt, active SOC, ANITSOC, or any other services we provide, you know where to find us.

But today we got– Hayden is going to talk to you about the things that Hayden wants to talk to you about. So the detection engineering process. So what happens is we reach out to each one of the people who work at, at Black Hills, the technical team, and say, would you like to give a webcast?

And a lot of times they’re like, I don’t know what to talk about. and so Hayden, I reached out and he’s like, oh, I have an idea. let me take some of the material from the class that I’m putting together, and I’m going to do that.

And so Hayden is taking material from a class that he’s designed for the Antisyphon training organization, and he’s going to today as part of a free, webcast. But Hayden is a part of our SOC.

Hayden, your life revolves around, like, detection engineering. Like, this is a thing that you do all the time, right?

**Hayden Covington**

Yes. Yeah, definitely. It’s, a lot of my time, especially as of late.

**Jason Blanchard**

Yeah. And Hayden came, on a webcast last year. It was so good not to raise expectations, not to, like, make Hayden want to, like, oh, my God, stop. but it was so good last year.

We were like, hey, you should put a class together. Like, you should come back. You should do this. And I hate that I should it all over him. but, Hayden rose to the occasion and created a, class, and he’s going to go ahead and give this webcast today.

So I’m going to head backstage. Hayden, if you need me at any time, I’ll pop back on. If you disappear for any reason, I’ll hop back on. but thank you so much for joining us. Please join us in Discord. If you haven’t checked in for Hackett yet, please do that.

we keep track of how many webcasts you attend. Once you hit 10, we send you a reward. And 20, 30, 40, and 50, we send you rewards. And we appreciate you being here. There’s a lot of places you could have been today, and you decided to come here, and we appreciate that.

All right, Hayden, it is all yours.

**Hayden Covington**

Awesome. Thank you. And so, as Jason said, a lot of this is pulled right from the course that I have. I will talk about that course some more later.

That’s at the very end. That way if you don’t want to hear about that, you only have to hear about the detection engineering which if you can’t tell, I’m kind of excited to talk about, but anyway, or to the slides, today talking about detection engineering and in my opinion how you should apply the scientific method to that process in order to get a better output.

But I’m already jumping ahead of myself so we’ll get to the first slide. who am I? Jason mentioned it a little bit. I work in the Black Hills SOC.

I’m a SOC analyst, detection engineer, security eng...