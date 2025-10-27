---
title: Introduction to Zeek Log Analysis
url: https://www.blackhillsinfosec.com/introduction-to-zeek-log-analysis-wrap/
source: Black Hills Information Security
date: 2025-01-14
fetch_date: 2025-10-06T20:10:40.767846
---

# Introduction to Zeek Log Analysis

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

13
Jan
2025

[Webcast Wrap-Up](https://www.blackhillsinfosec.com/category/webcast-wrap-up/), [Webcasts](https://www.blackhillsinfosec.com/category/webcasts/)
[log analysis](https://www.blackhillsinfosec.com/tag/log-analysis/), [Netowrk Security](https://www.blackhillsinfosec.com/tag/netowrk-security/), [network traffic](https://www.blackhillsinfosec.com/tag/network-traffic/), [Zeek](https://www.blackhillsinfosec.com/tag/zeek/), [Zeek Logs](https://www.blackhillsinfosec.com/tag/zeek-logs/)

# [Introduction to Zeek Log Analysis](https://www.blackhillsinfosec.com/introduction-to-zeek-log-analysis-wrap/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/WC_wrap-up_W0013.png)

*This webcast was originally published on December 19, 2024.*

In this video, Troy Wojewoda discusses the intricacies of Zeek log analysis, focusing on how this network security monitoring system can be used to understand traffic and analyze logs effectively. Troy provides insights into different log types, explains the unique identifiers used by Zeek, and shares tips on how to leverage these logs for network forensics and threat detection. Whether you’re new to Zeek or looking to deepen your understanding, this webcast aims to shed light on how Zeek can enhance your network security monitoring strategy.

* Zeek is a powerful network security monitoring tool that provides detailed insights into network traffic and can be used for intrusion detection, forensic analysis, and auditing.
* Placement of network security monitoring tools like Zeek is critical for capturing accurate and useful data, with different network positions offering unique visibility into potential threats.
* Zeek logs a wide range of network protocols and events, offering extensive data for analysis, including connection attempts, file transfers, and protocol-specific activities such as DNS and HTTP.

## Highlights

## Full Video

## Transcript

**Jason Blanchard**

Hello, everybody, and welcome to today’s Black Hills Information Security webcast. My name is Jason Blanchard, and I am the content community director here at Black Hills. And today we got Troy Wojewoda. I almost said it wrong.

Troy Wojewoda. and so Troy’s gonna be talking about Zeek Analysis, right?

**Troy Wojewoda**

Log analysis.

**Jason Blanchard**

Yeah, Zeek log analysis. So the way that this works is we reach out to all the testers and technical people on our team and we say, hey, what would you like to share with the community? Here’s some open time slots.

And so Troy wanted to talk about this. And so Troy has a passion for this. He’s excited about this. And so for the next 50 minutes or so, he’s going to talk about all the things that he thinks would be valuable for you to know.

If you have questions at any time, feel free to ask them inside Zoom, or if you have questions, you can ask them inside Discord in the live chat section. so that way, potentially the community can answer your question before we ever get a chance to get to it.

it takes a community for us all to come together. And then lastly, if you ever need a pen test, active SOC or ANTISOC or continuous pen testing or incident response, or if you need anything related to cyber security in any way whatsoever, you can reach out to Black Hills Information Security.

And we would love to talk to you about that. We’re not, what we don’t pressure. There’s no pressure. We, just want to talk to you and find out what you need. Now with that, Troy, it is all yours.

I’m going to head backstage. If you need anything at any time, I will pop back in and help. And to the rest of the community, thanks so much for joining us today and I’ll see you in a little bit.

**Troy Wojewoda**

Thanks, Jason. And welcome. Welcome to the last webcast of 2024 for Black Hills Information Security. My name is Troy Wojewoda, and as Jason said, I’m going to be talking about Zeek logs, the analysis of Zeek logs, and really an introduction, to the log framework that zeek, the, network security monitoring system produces.

And so I actually got this idea to do, put this webcast together for one of the SOC analysts, that we were talking, we were analyzing all the data and the telemetry coming in into the active SOC that BHIS has.

one of the analysts was basically saying it would be really nice to have an introductory, material for going over Z logs. And so I was like, oh, so this is a perfect opportunity to do this webcast to introduce those of you have, maybe you’re familiar with Zeek, maybe you’re hearing about Zeek for the first time, maybe you use Zeek for a while, but not have really got a handle of the log analysis portion of what the network security monitoring solution does.

And so this ...