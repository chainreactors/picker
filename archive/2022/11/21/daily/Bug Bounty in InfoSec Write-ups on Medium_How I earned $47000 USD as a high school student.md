---
title: How I earned $47000 USD as a high school student
url: https://infosecwriteups.com/how-i-earned-47000-usd-as-a-high-school-student-a9a68896b3a3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-21
fetch_date: 2025-10-03T23:19:04.002551
---

# How I earned $47000 USD as a high school student

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa9a68896b3a3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-earned-47000-usd-as-a-high-school-student-a9a68896b3a3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-earned-47000-usd-as-a-high-school-student-a9a68896b3a3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a9a68896b3a3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a9a68896b3a3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I earned $47000 USD as a high school student

[![Antonio Cheong](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*1WR-aYVime9znZL0)](https://medium.com/%40unshoulder_supersedes?source=post_page---byline--a9a68896b3a3---------------------------------------)

[Antonio Cheong](https://medium.com/%40unshoulder_supersedes?source=post_page---byline--a9a68896b3a3---------------------------------------)

6 min read

·

Nov 8, 2022

--

13

Listen

Share

*Ignore my butchered English. It’s not my first language.*

## Boring background (My life story)

Chūnibyō: A colloquial Japanese term for early teens who have delusions of grandeur. *Also a great anime.*

I was one of them, holding delusions of becoming a ‘hacker’ sporting a black hoodie with a Guy Fawkes mask covering my face. The genius villain of the movies.

Press enter or click to view image in full size

![Generic Guy Fawkes mask]()

Random image I found on Google

Yet despite my dreams, **I never really knew anything.** The most I could do was inspect element in Chrome and changing some text or get infinite cookies in Cookie Clicker.

Then came the blessing of 2020: It was the Chinese New Year and I had returned to my hometown in Malaysia. Just as my family booked the flight back to school, the pandemic struck. Flights were cancelled and we were placed under the lock-down. For a whole 6 months, I was stuck indoors.

Bored out of my mind, I began to learn ‘hacking’. I couldn’t code, and my internet was crap but what else was there to do?

With an old Macbook and Google, I began to search:

I started with wireless networks: Cracking WPA, sniffing packets, and MITM with ettercap. Why? Because I had shit internet and wanted to ‘borrow’ internet from a neighbor. Well, I failed. They had a strong password or something.

Press enter or click to view image in full size

![]()

My first Google Search (Reenacted)

A few weeks into research and I was barely touching upon Virtual Machines and ParrotOS (I didn’t know Kali Linux until much later).

Then, school started. While I was stuck abroad, my school had already opened up and soon, E-learning became the norm while the rest of my classmates were already physically there. The national borders were closed and I could not get back.

Being far away from any repercussions, I slacked off, focusing on learning ‘hacking’ rather than academics. It was during this time that I went from being a straight-A student to getting a 1% on my IGCSE mock exams for math (Time skip here. The failure was sometime in 2021).

Despite my desolate grades, I was making progress. What had once simply been a delusion had come to life. I was getting used to using Metasploit and had just completed my first coding project, a simple reverse shell written with Python sockets. A month later and I wrote a PHP site that could send fake emails from any address (patched and defunct).

Just as I was reaching the level of “script kiddie”, travel restrictions lifted and I became occupied with school work. While I did occasionally prank teachers with spoofed emails from the CIA, I learnt nothing new.

<Insert time skip>

## Finding an exploit

August 2021: IGCSE was over and it was yet another holiday. I do not remember the exact reason but I was playing with a new tool I found by the name of EggShell (A RAT). With EggShell’s shell there was a bug: Doing ^c (control+c) occasionally terminated a frozen remote process or killed the shell itself. However, if I rerun the shell quickly enough, the connection would persist. (I later found the bug but that’s irrelevant)

Curious enough, when I attempted to take a remote screenshot after the reconnection, I was able to immediately retrieve the image, seemingly without prompting for permission. However, I was unable to replicate this consistently

December 2021: Yet another holiday. This time, Christmas. I had gotten bored with the inconsistency of EggShell and returned to using Meterpreter. This time, I was trying to be discrete while pranking a friend (I know it is illegal. Please don’t arrest me. I was dumb) and ‘rm -rf’ed the dropped Trojan executable. Yet again, I was able to take screenshots without permission… and it was replicable. Upon noticing that I had found an actual exploit, I immediately Googled for how I can get money for this.

## A Rollercoaster with Apple

Guess what? Apple had a generous bug bounty system. Based on their examples, I was set for $50,000!!!

Having previous issues with disappointing my family, I told nobody. My heart was leaping out of my mouth in excitement, yet I kept silence.

With a quick low quality write up, I sent it to Apple.

A month passes: No response.

I learnt Objective-C and wrote a one click POC. Sent it off to Apple once again.

A month passed. A response.

Press enter or click to view image in full size

![]()

Their email to me

My heart came close to exploding

One month passes

No more details. My requests for updates go unanswered. I lose hope.

Two months passes

I gave up cybersecurity as my career path. Might as well just be a normal programmer.

One month passes

Press enter or click to view image in full size

![]()

Second email

Once again, I rejoyced. Perhaps it was not forgotten. I replied.

Press enter or click to view image in full size

![]()

Confirmation

I informed my parents. Maybe something will actually happen for once…

Press enter or click to view image in full size

![]()

ANONYMOUS? WTF

I was not credited. I have no idea why.

Press enter or click to view image in full size

![]()

Are you kidding me?

Six months have passed since I received this email. Credits have not been given.

I delete everything I have related to ‘hacking’. My dream was no more.

Six months passes.

Press enter or click to view image in full size

![]()

I got the award?

Press enter or click to view image in full size

![]()

I followed through the process provided. It was troublesome due to my underage ...