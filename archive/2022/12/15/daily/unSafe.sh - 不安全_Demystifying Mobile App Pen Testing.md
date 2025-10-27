---
title: Demystifying Mobile App Pen Testing
url: https://buaq.net/go-140018.html
source: unSafe.sh - 不安全
date: 2022-12-15
fetch_date: 2025-10-04T01:29:41.305226
---

# Demystifying Mobile App Pen Testing

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ae63b2f7dbc0f70456b77b1069029009.jpg)

Demystifying Mobile App Pen Testing

Interest in mobile app pen testing grows as organizations recognize the importance of mitigating se
*2022-12-14 20:30:0
Author: [www.nowsecure.com(查看原文)](/jump-140018.htm)
阅读量:20
收藏*

---

Interest in [mobile app pen testing](https://www.nowsecure.com/solutions/by-need/mobile-app-penetration-testing/) grows as organizations recognize the importance of mitigating security and privacy risks. Less understood and more mysterious to many, though, is how to build the skills needed to conduct manual [mobile application security testing](https://www.nowsecure.com/solutions/by-need/mobile-app-security-testing/).

To shed light on the topic, NowSecure convened a virtual panel of its expert mobile pen testers at the [NowSecure Connect 2022](https://events.bizzabo.com/NSConnect2022) AppSec and DevSecOps community event. The [NowSecure Services](https://www.nowsecure.com/solutions/by-need/mobile-app-penetration-testing/) team has more than a dozen years pen testing more than 11,000 mobile apps against [industry standards](https://www.nowsecure.com/blog/2022/08/10/how-mobile-appsec-testing-standards-speed-devsecops/) and boasts the industry’s broadest collection of the most skilled pen testers. In addition, NowSecure security analysts have helped thousands of organizations establish successful mobile app pen testing programs.

The panelists include:

* Ben Corbitt, Application Security Analyst, NowSecure
* David Mockler, Senior Application Security Analyst
* Jeremy Murphy, Senior Application Security Analyst, NowSecure
* Devin Price, Lead Application Security Analyst, NowSecure

![](https://www.nowsecure.com/wp-content/uploads/2022/12/Pen-testing-blog-panel-screenshot-960x640.png)

The group discussion highlights how mobile app pen testers got their start and honed their craft, their favorite tools for Android and iOS and [best practices for mobile app pen testing](https://www.nowsecure.com/blog/2019/06/20/best-practices-for-mobile-app-pen-testing/). *Their original conversation has been edited for length and clarity.*

**[Mockler] Do you need certification or formal education to become a mobile pen tester or break into cybersecurity?**

**[Murphy**] “No. There are plenty of free and inexpensive [resources](https://www.nowsecure.com/products/nowsecure-academy-mobile-appsec-training/) out there that can teach you everything you need to become a penetration tester. To get hired, though, certifications give potential employers a way to validate your skillset.”

**[Corbitt]** “They’re not necessarily required, but are great for building your resume and getting your foot in the door. [Certifications](https://academy.nowsecure.com/) that include a training class like a weeklong boot camp or lab requirements can be really helpful in forcing you to learn a lot in a short period of time.”

**[Price**] “I would say no. I’ve seen people join bug bounties or do technical write-ups to demonstrate to employers they know how to find security vulnerabilities within mobile applications.”

**[Murphy]** “Have a GitHub of some of your work, a blog or HackTheBox rank to show you have the skills.”

**[Mockler] How did each of you gain pen testing skills to get to where you are today?**

**[Price]** “The best resource I used first was the more senior pen testers already on my team when I joined NowSecure.Early on, I looked through older reports of what my teammates had done to get in the mindset of how to write a detailed assessment report. In my free time, I completed pen testing training courses on TryHackMe and found some security podcasts to help me understand the exploits pen testers are doing and understand the vernacular.”

**[Corbitt]** “I started as a pen tester for web apps. The company also had a mobile app and nobody at the time knew how to test it. I was voluntold to get a mobile security certification and test the app.”

**[Murphy]** “I started at the help desk. One of my coworkers said, ‘Hey dude, you should study for Certified Ethical Hacker (CEH). He told me what it was and I thought it was cool. Then I found a podcast that lit a fire underneath me — shoutout to Jack Rhysider at [*Darknet Diaries*](https://darknetdiaries.com/). It really built my passion for this field. I started on Hack The Box and built a network of pen testers. I started in the trenches and worked my way up.”

**[Mockler]** **Rolling into our next question, what kind of mobile app pen testing tools do you use?**

**[Price]** “For Android, my go-to tool for any type of static analysis or reverse engineering is JADX, a simple Dex to Java decompiler. And for the iOS counterpart, I use Hopper which is a great disassembler that lets you decompile and debug iOS applications.”

**[Corbitt]** “I really like Drozer, a tool for Android apps. It’s very outdated and hard to get working sometimes. I really wish there was a more modern supported tool that does the same thing. But it’s a great tool for quickly and easily interacting with the internals of an application.”

**[Murphy]** “The correct answer is [NowSecure Workstation](https://www.nowsecure.com/products/nowsecure-workstation/). Some of the key ones are Hopper, Ghidra, Burp Suite, Postman, JADX…reFlutter on GitHub is another good one for poking around those new Flutter apps. Obviously, [R2Frida](https://github.com/nowsecure/r2frida) is another good one we use a lot for reverse engineering.”

**[Mockler]** “We get asked quite a bit what are the best [mobile app pen testing tools](https://www.nowsecure.com/blog/2022/04/13/popular-mobile-app-security-testing-tools/) out there. It’s not necessarily what the best tools are — it’s ‘what are you trying to do?’ Depending on what type of exploit you’re going to try, you’re going to use a different tool and there’s a GitHub repo for everything.”

**[Mockler]** **We’ve discussed what tools we use. Let’s go over what we look for with them.**

**[Price]** “One of the first things I examine is the Android manifest file, because that’s going to tell me a lot about the application. For example, has the application been correctly signed with the correct key length? I’ll also look for some of the application’s content providers and look at any broadcast receivers to make sure those have been correctly exported. Has the application enabled a backup of user data? What does the application’s network security configuration look like? What are some of the rulings that have been set up for that? Think of the manifest file as the front door for pentesting when it comes to static analysis for an Android application.”

**[Corbitt]** “Drozer looks at the internals of an Android application — the activities and broadcast receivers and the like. Let’s talk about activities. If you don’t know what an activity is, think of it as a screen. If you open an Android application and it brings up a login screen, that’s an activity. And when you log in and it brings up your main menu, that’s another activity. If those activities aren’t set correctly with the proper permissions, you can directly call some activities that you weren’t meant to see without logging in first. A few years ago, there was an NFL-related app where you could subscribe to watch NFL games on your phone. There was a bug in the app where using Drozer, you could call an activity out of order to reach the section of the app where you could watch NFL games without having to login to an account or pay. You could run that activity that wasn’t set properly and watch NFL games for free. I find that really interesting, being ab...