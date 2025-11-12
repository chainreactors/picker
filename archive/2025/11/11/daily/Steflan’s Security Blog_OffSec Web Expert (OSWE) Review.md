---
title: OffSec Web Expert (OSWE) Review
url: https://steflan-security.com/offsec-web-expert-oswe-review/?utm_source=rss&utm_medium=rss&utm_campaign=offsec-web-expert-oswe-review
source: Steflan’s Security Blog
date: 2025-11-11
fetch_date: 2025-11-12T03:13:11.832380
---

# OffSec Web Expert (OSWE) Review

* [Home](https://steflan-security.com)
* [CTF Walkthroughs](https://steflan-security.com/category/walkthrough/)
  + [Hack The Box](https://steflan-security.com/category/walkthrough/hack-the-box/)
  + [TryHackMe](https://steflan-security.com/category/walkthrough/tryhackme/)
  + [VulnHub](https://steflan-security.com/category/walkthrough/vulnhub/)
* [Guides](https://steflan-security.com/category/guides/)
  + [Enumeration](https://steflan-security.com/category/guides/enumeration/)
  + [Privilege Escalation](https://steflan-security.com/category/guides/privilegeescalation/)
    - [Linux](https://steflan-security.com/category/guides/privilegeescalation/linux/)
    - [Windows](https://steflan-security.com/category/guides/privilegeescalation/windows/)
  + [Web](https://steflan-security.com/category/guides/web/)
  + [Buffer Overflow](https://steflan-security.com/category/guides/bufferoverflow/)
    - [Stack Buffer Overflow](https://steflan-security.com/category/guides/bufferoverflow/stack-buffer-overflow/)
* [Reviews](https://steflan-security.com/category/reviews/)
  + [Certifications](https://steflan-security.com/category/reviews/certifications/)
  + [Training Labs](https://steflan-security.com/category/reviews/training-platforms/)
  + [Learning Material](https://steflan-security.com/category/reviews/learning-material/)
* [Resources](https://steflan-security.com/category/resources/)
  + [Cheat Sheets](https://steflan-security.com/category/resources/cheatsheet/)
  + [Checklists](https://steflan-security.com/category/resources/checklists/)
* [About](https://steflan-security.com/about-us/)

[![Steflan’s Security Blog](https://steflan-security.com/wp-content/uploads/2021/03/cropped-Logo.png)](https://steflan-security.com)

![](https://i0.wp.com/steflan-security.com/wp-content/uploads/2025/11/OSWE.png?fit=1024%2C409&ssl=1)

[Certifications](https://steflan-security.com/category/reviews/certifications/), [Learning Material](https://steflan-security.com/category/reviews/learning-material/), [Reviews](https://steflan-security.com/category/reviews/), [Training Labs](https://steflan-security.com/category/reviews/training-platforms/)

# OffSec Web Expert (OSWE) Review

November 11, 2025
| by Stefano Lanaro
| [Leave a comment](https://steflan-security.com/offsec-web-expert-oswe-review/#respond)

## Introduction

The OffSec Web Expert (OSWE) is an web application penetration testing certification offered by Offsec that teaches advanced web attacks and exploits, with an emphasis of performing white-box engagements and source code review.

It comes with the Advanced Web Attacks and Exploitation (AWAE) video and text course and it’s one of the major advanced certifications in the penetration testing world. In this review I take the time to talk about my personal experience with this course, the learning material and resources I used to prepare etc.

**Contents**
hide

[1
Introduction](#Introduction)

[2
Background](#Background)

[3
Exam Preparation](#Exam_Preparation)

[4
The WEB-300 Course](#The_WEB-300_Course)

[5
The WEB-300 Challenge Labs](#The_WEB-300_Challenge_Labs)

[6
External Preparation Resources](#External_Preparation_Resources)

[7
Tips & Tricks](#Tips_Tricks)

[8
The Exam](#The_Exam)

[9
My Exam Experience](#My_Exam_Experience)

[10
Conclusion](#Conclusion)

## Background

I had been wanting to complete OSWE in a while, but I always felt somewhat intimidated by the challenge of the exam, but since my OSEP exam was three years ago, I felt like it was finally time.

I did not do any specific preparation prior to starting the course, as I already had 5+ years of experience in web testing and I felt pretty confident I had a solid grasp on all the main attacks and techniques.

## Exam Preparation

To prepare for the exam I used various resources, both part of the course and external. As much as the course material is more than enough to pass, and you shouldn’t find any attack or technique in the exam that wasn’t mentioned in the course, I wouldn’t exclusively rely on it.

The course content can feel somewhat rushed at times, so it is definitely useful to have some extra challenge, especially when it comes to deep diving into source code and finding vulnerabilities manually.

## The WEB-300 Course

The learning material provided with the course covers a wide range of web attacks and vulnerabilities, such as deserialization, SQL injection, cross-site scripting, client and server-side request forgery, XML external entity injection, prototype pollution, template injection, command injection and more.

I purchased three months of lab access, at first I wasn’t sure whether it would be enough, however after chatting with a few colleagues who had already attended the course, and considering my existing experience, I didn’t feel like I needed any more time.

I started by going through all the modules within the course, watching the videos and reading the corresponding text, completing and documenting all the exercises. I would copy all code snippets, commands or other information that I thought was relevant in my Obsidian notes.

Unlike other courses, WEB-300 does not have a section for each topic, but instead it uses case studies from previously identified vulnerabilities to showcase them. While confusing at first, I really liked this approach as it put the student in the shoes of a bug bounty hunter or researcher looking for vulnerabilities in large enterprise-style applications.

Due to the large code base of the applications, and in the interest of time, the process of identifying the vulnerabilities illustrated throughout the course may feel sloppy and rushed at times, for example searching for SQL statements to identify potential injections, but totally skipping the manually process that eventually led to such discovery. I totally understand why this approach was followed, however a less experienced tester may feel a little bit lost.

I recommend completing and documenting all of the exercises as they will be a good way to put the techniques learned into practice and solidify your knowledge. The code used throughout the learning objectives will also come in handy during the practice labs as well as the exam. The extra mile exercises may feel tedious and even pointless at times, however they definitely provided some good value for me. Some of them even included finding vulnerabilities in off-the-shelf applications.

While I don’t think the content is anywhere near perfect or cutting edge, especially considering some of Offsec’s competitors, it definitely provided me with a huge amount of value and practice.

It took me about one and a half months to complete all of the modules, and after that, I got started with the WEB-300 labs.

## The WEB-300 Challenge Labs

The labs were comprised of seven standalone web applications, plus a couple of modules part of the learning content that required flags to be submitted as part of challenges. Six of the applications were white-box, with one being black-box and slightly more CTF-style.

This was definitely the most interesting part of the entire course, as you get to play around with vulnerable applications that feel realistic, unlike most CTF challenges out there. The code was relatively well written, and I could tell that some real work had been put in them.

I suggest to try and complete as many of these as you can if you want to have a good chance at passing the exam, as they will somewhat simulate the exam experience. Some of them include multiple paths, so if you think you may have missed them I would recommend going back and trying to find them all.

Make sure you carefully document each of the steps you performed during the challenges and all of the code used, as these could come in handy later on, as well as they will get you in the habit of always taking notes and screenshots of your steps.

With your lab access, you also get access to the Discord and the official forum where you can discuss the challenges with other ...