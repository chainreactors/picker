---
title: Finding Signal in the Noise: Lessons Learned Running a Honeypot with AI Assistance &#x5b;Guest Diary&#x5d;, (Tue, Feb 24th)
url: https://isc.sans.edu/diary/rss/32744
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-26
fetch_date: 2026-02-27T04:08:44.352821
---

# Finding Signal in the Noise: Lessons Learned Running a Honeypot with AI Assistance &#x5b;Guest Diary&#x5d;, (Tue, Feb 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32742)
* [next](/diary/32748)

# [Finding Signal in the Noise: Lessons Learned Running a Honeypot with AI Assistance [Guest Diary]](/forums/diary/Finding%2BSignal%2Bin%2Bthe%2BNoise%2BLessons%2BLearned%2BRunning%2Ba%2BHoneypot%2Bwith%2BAI%2BAssistance%2BGuest%2BDiary/32744/)

**Published**: 2026-02-24. **Last Updated**: 2026-02-26 12:21:37 UTC
**by** [Austin Bodolay](/handler_list.html#austin-bodolay) (Version: 1)

[0 comment(s)](/diary/Finding%2BSignal%2Bin%2Bthe%2BNoise%2BLessons%2BLearned%2BRunning%2Ba%2BHoneypot%2Bwith%2BAI%2BAssistance%2BGuest%2BDiary/32744/#comments)

[This is a Guest Diary by Austin Bodolay, an ISC intern as part of the SANS.edu [BACS](http://https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

Over the past several months, I have gained practical insight into the challenges of deploying and operating a honeypot, even within a relatively simple environment. This work highlighted how varying hardware, software, and network design—can significantly alter outcomes. Through this process, I observed both the value and the limitations of log collection. Comprehensive telemetry proved essential for understanding activity targeting the honeypot, yet it also became clear that improperly scoped or poorly interpreted logs can produce misleading conclusions. Prior to this research, I had almost no interaction with AI tools and struggled to identify practical ways to integrate them into my work. Throughout this experience, however, AI proved most valuable not as an automated solution, but as a collaborative aid—providing quick syntax on the CLI, offering alternative perspectives, and helping maintain analytical focus.

**Introduction**

The DShield honeypot is a sensor that pretends to be a vulnerable system exposed to the internet. It collects information from scans and attacks that are often automated, providing insight to analyst what threat actors are targeting and how. The honeypot generates a large amount of data, much of it low-value.  Deciding what is meaningful, what separate events are related, and what (if any) actions should be taken. Being able to accurately assess the data requires the right information. And in the event a true incident does occur, being able to piece together the breadcrumbs requires the data is actually there. Piecing it all together requires the right methodology. Using an AI, like [ChatGPT](https://chatgpt.com), is extremely helpful in tying these concepts together.

**The Data: What Was Collected and Why**

In the few months my [SIEM](https://github.com/bruneaug/DShield-SIEM/tree/main) has collected 8 million logs from 14,000 unique IP addresses. There is a lot of noise on the internet from automated scanners and toolkits that frequently repeat the same actions to every device willing to listen. This constant "background noise" on the internet are systems constantly scanning for what is available, what is potentially vulnerable, and what is low hanging fruit that can provide a foothold for something more. Is there an exposed administrative panel? Do these default credentials work anywhere? And if so, what does information does this hold or what does it have access to? Is this a developer? Does the system have private information worth value? The honeypot sensor provides a way to analyze this traffic to better understand what threat actors are after and how they are going after it.

The basic information that is collected on the honeypot includes source IP addresses, port, protocol, URL, and a few other metrics. The logs primarily record the traffic that was sent to the honeypot. If your router dropped the packets or failed to send them to the honeypot, the logs will not be generated to be sent to the SIEM. The NetFlow logs add a little extra information, like the direction of the packets, the byte count, and packets that were dropped before reaching the honeypot. What my current system does not show is the actual payloads in the traffic, the headers of packets, or the exploit details. ChatGPT helped identify what type of data I actually have, what types of conclusions can be drawn from this data, and methods to validate these conclusions. ChatGPT also identified dead ends early on, saving me time from going down rabbit holes by pointing out the current data will never be able to positively affirm any conclusion.

**Part One:**

I came across a log that raised some concerns. After providing simple details of the devices involved, the type of log generated, clarifying the log is on the gateway and not the SIEM, and the values recorded in the data, ChatGPT provided insights as to what likely generated this traffic and why it likely isn't an alternative event. I performed additional research to confirm this information is true.

**Interaction with ChatGPT**
![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic1.png)

![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic2.png)

![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic3.png)

**Part Two:**

Researching a unique User-Agent "libredtail-http", I began checking a high level how frequently this shows up. I noticed that in several months of logs, this User-Agent appeared for the first time on my sensor in December of 2025. There are 34 unique IP addresses that have used it, most of which have less than 100 events. Interestingly, all events occur on the same days, with up to 2 weeks of silence between the next set of events. Additionally, the URL request and payload sizes were identical among all events, regardless of the source IP address. When researching the User-Agent string "libredtail-http", I came across many articles about malware. Sharing some of the information found with ChatGPT, it quickly identified what I was likely seeing, who it is targeting, what makes an event vulnerable to the attacks, and how to protect from them. More likely than malware, what I was seeing is an automated multi-staged toolkit that is scanning the internet for vulnerable Apache servers, Linux web interfaces, and IoT devices. The source of scans is using low-cost methods to rotate through IP addresses, combined with intermittent campaign timing (burst -> idle -> burst) to reduce detection and attribution. This is likely a botnet and the goal is to enroll new systems into the botnet for additional scanners, proxies, and DDoS nodes. I then began researching this information, such as the CVE mentioned by ChatGPT, indicators of compromise (IOCs), and comparing various sources to what I have in my logs to validate the accuracy of the statements. The responses were very accurate. Had I not used ChatGPT, I would have started searching for IOCs in my logs for signs of malware mentioned in the articles and possibly wasted several hours. I likely would have come to a similar conclusion, but I admit it would have used a lot of my time.

![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic4.png)

![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic5.png)

![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic6.png)

![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic7.png)

**Interaction with ChatGPT based on findings above.**

I have found the most value comes by clearly stating what your objective is. The more details provided early on reduce vague answers.

![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic8.png)
![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic9.png)
![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic10.png)
![](https://isc.sans.edu/diaryimages/images/Austin_Bodolay_pic11.png)

**Conclusion and Lessons Learned**

Having more logs doesn't equal more answers. If a system is comprised and reaches out to a malicious serv...