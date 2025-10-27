---
title: Offensive Security Wireless Attacks (WiFu) + Offensive Security Wireless (OSWP)
url: https://blog.g0tmi1k.com/2014/01/offensive-security-wireless/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:54.377814
---

# Offensive Security Wireless Attacks (WiFu) + Offensive Security Wireless (OSWP)

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Offensive Security Wireless Attacks (WiFu) + Offensive Security Wireless (OSWP)

*The views and opinions expressed on this site are those of the author. Any claim, statistic, quote or other representation about a product or service should be verified with the seller, manufacturer or provider.*

A few months back, I took [Offensive Security](https://www.offensive-security.com/)'s online course [WiFu](https://www.offensive-security.com/information-security-training/offensive-security-wireless-attacks/) course & exam [OSWP](https://www.offensive-security.com/information-security-certifications/oswp-offensive-security-wireless-professional/), as I had written up a review for [PWB/OSCP](https://blog.g0tmi1k.com/2011/07/pentesting-with-backtrack-pwb/) & [CTP/OSCE](https://blog.g0tmi1k.com/2013/08/cracking-perimeter-ctp-offensive/), I thought I would do this too. As always, everything in this post is both personal comments and my own experience with the course.

![Offsec WiFu Box](/images/offsec-wifu-boxes-medium.png "Offec WiFu")

Table of Contents

* + [Course Material](#Course.Material)
    - [Course Materials & Lab/Exam Setup](#Course.Materials..amp..Lab.Exam.Setup)
    - [Material Breakdown (WiFu)](#Material.Breakdown..WiFu.)
    - [Exam (OSWP)](#Exam..OSWP.)
  + [Reflection](#Reflection)
    - [Myths](#Myths)
    - [WPS](#WPS)
    - [Criticism](#Criticism)
  + [Is this course for me?](#Is.this.course.for.me.)
    - [So why do this course? What's the point in doing this, I know how to crack/hack WPA.](#So.why.do.this.course..What.s.the.point.in.doing.this..I.know.how.to.crack.hack.WPA.)
    - [What's wrong with the resources that are out there currently?](#What.s.wrong.with.the.resources.that.are.out.there.currently.)
  + [Summary](#Summary)
    - [Advice](#Advice)

It's not easy to create a course, especially with the amount of resources that are freely available, such as the [aircrack-ng wiki](http://www.aircrack-ng.org/doku.php) and [Security Tube's Wireless Megaprimer](http://www.securitytube.net/groups?operation=view&groupId=9). Both are good, if not great sources of knowledge that make them a valued resource, however, there is still room for WiFu - more on this later.

---

Before doing the course, I had already dabbled with 802.11 and its security, successfully cracking some WEP & WPA networks, and writing my own "wrapper" to automate the process. However, I still learnt more than a thing or two by the time I had completed the course.

Everything that I knew before the course, was self taught, which came from reading blog/forum postings, and the odd video (There are plenty of resources – and they range in quality, depth of detail and age).

Yes, I was able to learn, and teach myself for free. But, I spent time doing it, as I had to go out searching for it (which made it easier to skip over certain areas, if you didn't seek them out). There are also conflicting bits of information online (either because it's out-dated or it's "the blind leading the blind").

---

As always, with an Offsec course, all the information that you need is in one place. They have done their homework including getting the author (Mister\_X) of \_THE\_ pentesting tool for 802.11, aircrack-ng, to help write the course.

## Course Material

### Course Materials & Lab/Exam Setup

The course material is made up of a handbook/document (.PDF – 385 pages), and videos (.SWF – little under 3 and a half hours). In the handbook, there are links to external example .CAP files that Offsec is hosting, allowing you to follow alongside. There is also a custom Backtrack ISO file, which is what the course recommends you use.

---

I personally was able to progress through the entire course material in a weekend. The exercises were straight forward, and I didn't run into any issues completing them (I used an old NetGear WG614 v9 & TP-Link WR104ND for access points and [ALFA AWUS036H](https://forums.kali.org/showthread.php?3816-Working-Hardware-ALFA-AWUS036H-500mW-(Realtek-RTL8187L-rtl8187) & [Linksys WUSB54GC](https://forums.kali.org/showthread.php?3820-Working-Hardware-Linksys-WUSB54GC-v1-(Ralink-2573-USB-rt73usb) wireless cards).

Unlike PWB/CTP, there isn't a remote lab this time to connect into – you will be re-creating the labs locally. They isn't any "step by step" instructions showing you how to alter the router configurations (you sometimes see a glimpse of this in the videos), as each router's UI is different. Instead they just inform you what settings you need to place your router in for this exercise.

---

The upside to not having any remote labs, is that you are not limited to lab time, so you are able to work on it freely. However, the exam attempt that comes with the course is only valid for 120 days after you receive the course materials – which is plenty of time to get you prepared.

---

The exam however, is taken remotely. You do not VPN in (like OSCP/OSCE - which allows you to use your own hardware and software configuration), instead you SSH to a clean, ready to go, Backtrack 5 r3 machine which has *everything* you need to be able to pass the exam.

### Material Breakdown (WiFu)

*If you want to follow along yourself, you can find the [course syllabus here](http://www.offensive-security.com/documentation/wifu-syllabus.pdf).*

It begins with all with all the standards & protocols for 802.11 (with a bit of a history lesson), which moves into how a wireless networks work, the different types of WiFi.

---

Then it is chapter 3. This gives a full breakdown of 802.11 packets, as well as techniques used in the protocol, and it goes into a great amount of depth. Throughout this section, on nearly every page there is a screenshot, table, or diagram to help break up the text, and help explain the area in more depth.

I personally see it as a bit of a "dry" area, and the authors felt the same (there are words of encouragement to stick with it and understand everything that is being said here).

This is a large section (over 100 pages), as they have to cover too much in this area. This builds up a good proportion of background knowledge, showing why everything works.

Reading back on my notes for this chapter, the amount taken towards the ends does start to thin out (however I have now got the PDF to use as reference to fall back on).

---

After learning all that theory behind it, it starts to get ready for the practical. They do this by showing how to pick hardware *(note: I see this question being ask almost on a daily basis – it's a popular question!)*. Rather than just saying "get this card", they explain what to look for in a card – and which one would be best suited for the job *(spoiler alert: there isn't a single card that "is the best and does everything")*.

Quick run down, they compare: interface, signal/power, antennas & chipsets. I personally was impressed with the antennas section, showing the different signal patterns – this is something I hadn't looked into before.

---

I should say at this point, unlike PWB & CTP where you remotely VPN in, connecting to their (Offsec) labs, you need to setup and create your own locally. So, if you wish to do any of the practical you will need to purchase some of the hardware you have just researched (as its not included in the course fees). The exam however, is taken online – this is covered later.

---

Next, the course starts to teach you about how the hardware works with the software via wireless stack & drivers, which is another commonly asked about area I've seen online. They run you through the basics such as testing drivers & (manually) enabling "monitor" mode.

I would have liked to have seen more "troubleshooting" here, or a bit more advance commands to gather more information about what's going on/current setup. I mention this because it bugs me regarding people who are wanting help, but lacking detail *(however more often than not, it's ...