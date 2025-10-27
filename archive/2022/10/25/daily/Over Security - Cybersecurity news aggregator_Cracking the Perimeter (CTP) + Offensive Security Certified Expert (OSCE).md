---
title: Cracking the Perimeter (CTP) + Offensive Security Certified Expert (OSCE)
url: https://blog.g0tmi1k.com/2013/08/cracking-perimeter-ctp-offensive/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:53.181747
---

# Cracking the Perimeter (CTP) + Offensive Security Certified Expert (OSCE)

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Cracking the Perimeter (CTP) + Offensive Security Certified Expert (OSCE)

*The views and opinions expressed on this site are those of the author. Any claim, statistic, quote or other representation about a product or service should be verified with the seller, manufacturer or provider.*

It's been a while *(just shy of two years)* since I did "[Penetration Testing with BackTrack (PWB) & Offensive Security Certified Professional (OSCP)](https://blog.g0tmi1k.com/2011/07/pentesting-with-backtrack-pwb/)". Over the last couple of weeks I've taken the next step with Offensive Security's training course – "[Cracking the Perimeter (CTP)](http://www.offensive-security.com/information-security-training/cracking-the-perimeter/)", which, when successfully passed, gives you "[Offensive Security Certified Expert (OSCE)](http://www.offensive-security.com/information-security-certifications/osce-offensive-security-certified-expert/)" certificate. Below are my thoughts & feelings regarding my overall experience of the course.

![Offsec CTP box](/images/offsec-ctp-boxes-medium.png "Offec CTP")

Table of Contents

* + [Myths](#Myths)
    - [Only covers exploit development](#Only.covers.exploit.development)
    - [It's old and "dated"](#It.s.old.and..dated.)
    - [The course itself is (super) hard](#The.course.itself.is..super..hard)
  + [Review](#Review)
    - [Before signing up to the course](#Before.signing.up.to.the.course)
      * [Pre-course](#Pre-course)
      * [Course](#Course)
      * [Exam](#Exam)
  + [Summary](#Summary)
  + [Advice](#Advice)
    - [To anyone thinking about doing the course](#To.anyone.thinking.about.doing.the.course)
    - [To students currently doing the course](#To.students.currently.doing.the.course)
    - [To students about to do the exam (or currently doing it!)](#To.students.about.to.do.the.exam..or.currently.doing.it..)
  + [Resources](#Resources)

## Myths

However, before going any further, I would like to dispel up a few "myths", that I've heard, over the years. These "issues" are:

* Only covers exploit development
* It's old and "dated"
* The course itself is *(super)* hard

### Only covers exploit development

**Wrong**. There are nine modules in the course ([syllabus](http://www.offensive-security.com/documentation/cracking-the-perimiter-syllabus.pdf)). These can be put into the following four sections:

* Bypassing Anti-Virus (AV)
* Exploit Development
  + "Advance" techniques
  + 0Day angle
* WAN Attacks
* Web Attacks

Above shows there is more to the course than just exploit development. However, there is more focus on that section than anything else. It's more accurate to say "the main element of the course is exploit development".

People also easily confuse "Bypassing AV" with exploit development as you are using the same set of tools to manually do the encoding - same tools, different purpose.

### It's old and "dated"

**So what?** I don't see an issue with this myself.

---

The methods and techniques that are covered in the course can still be applied today. Since the release of the course, there has been additional research into each section. As a result, there are different *(some people could argue "better")* ways to achieve the same outcome. However, being able to understand how these developments came about from the original methods, and give you an alternative technique to use, will give you a broader and deeper understanding.

---

Some of the standard tools that "everyone" uses are now different. This doesn't mean the techniques are any different. The techniques you need to learn will always be the same. This is especially true as Offensive Security (offsec) likes to show you the manual way of doing things, rather than solely relying on tools to-do the work for you. So even if the course was updated, I believe that the methods would still be the same, it would just be that the interface had changed.

### The course itself is (super) hard

PWB is a entry level course, CTP is a **intermitted course**. There are harder ones to.

---

The exploit development in PWB is a "taster" with the course material walking you through basic buffer overflows and web attacks. Offsec also have courses called "ADVANCED Windows Exploitation (AWE)" and "ADVANCED Web Attacks and Exploitation (AWAE)"; both of these other courses are even more specialized that CTP.

With that in mind, CTP is somewhere in-between with difficultly. The course starts from the basic in PWB, and stops where AWE & AWAE would take over. For example it's expected that the student knows what EIP is, but they don't need to understand any HEAP exploit techniques.

In the same respect, you'll not be doing any basic "Remote File Inclusion (RFI)", but you are not required to-do a blind "SQL Injection (SQLi)" attacks.

## Review

Now, with all that cleared up. Here is my personal experience of going through the course from start to finish. Where possible, I'll try and relate to the PWB course.

### Before signing up to the course

I followed along the tutorials from Corelan and [FuzzySecurity](http://fuzzysecurity.com/tutorials.html) to improve my exploit development skills *(found them both excellent resources for this)*. I stopped reading them when I got to the HEAP exploitation sections, as this isn't required for CTP. However, this doesn't mean:

1. You shouldn't know it – it's still good to learn.
2. If you want to use other methods that are not covered in the course, you are able to, there isn't anything stopping you.

I then moved onto the first few levels of Exploit-exercises's Fusion & Protostar. I didn't feel this was needed, but I felt it was beneficial for me as I wanted something to try out for myself without following a guide *(and it's designed to have vulnerabilities to find)*.

---

I had already done various web application attacks in designed vulnerable code, so I felt confident in this area and as a result I didn't feel that I needed to-do any extra work in this field. If you want to try some yourself, I would recommend: [DVWA](http://www.dvwa.co.uk/), [Mutillidae](http://www.irongeek.com/i.php?page=mutillidae/mutillidae-deliberately-vulnerable-php-owasp-top-10) and [WebGoat](https://www.owasp.org/index.php/Category%3AOWASP_WebGoat_Project).

---

Looking into the WAN attacks section; it's done using Cisco routers. When I was doing my CCNA certification, I spent a good amount of time doing extra things that were not technically in the course curriculum. It was a good chance for me to do things like this, that I wouldn't of had access to in my lab, plus my instructor didn't mind. For these reasons, I also didn't worry too much about the WAN attack.

---

Reading books isn't my thing, but a couple of students have recommended some and they can be found in the list of resources at the end of the page.

#### Pre-course

Before you're able to sign up for the course, there is a "filter" ([fc4.me](http://fc4.me/)). This is put in place to make sure that the student who is about to take the course is *(hopefully)* potentially capable of doing so. This barrier relates to what's required of you from the course.

---

There isn't any shame in not being able to complete this. It simply means you're not ready... yet!

If you look up the solution online, you're just cheating yourself and wasting both time and money. It's been put there for a reason. Offsec is trying to protect you from yourself *(in their own frustrating but necessary way!).*

#### Course

You are provided with the same format for your course material as with PWB, a PDF (~150 pages) and a series of videos (a little bit over 4 and a half hours).

You're also assigned your own machine. However, unlike PWB, you're assigned multiple devices (two machines and a router).

---

The course material didn't seem to match up as well as PWB (before, it felt like a transcript), for example there were certain sections which ...