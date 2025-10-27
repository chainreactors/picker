---
title: &#x5b;Guest Diary&#x5d; How Access Brokers Maintain Persistence, (Fri, Jan 24th)
url: https://isc.sans.edu/diary/rss/31600
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-25
fetch_date: 2025-10-06T20:12:52.297582
---

# &#x5b;Guest Diary&#x5d; How Access Brokers Maintain Persistence, (Fri, Jan 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31598)
* [next](/diary/31602)

# [[Guest Diary] How Access Brokers Maintain Persistence](/forums/diary/Guest%2BDiary%2BHow%2BAccess%2BBrokers%2BMaintain%2BPersistence/31600/)

**Published**: 2025-01-24. **Last Updated**: 2025-01-24 00:42:06 UTC
**by** [Joseph Flint, SANS.edu BACS Student](/handler_list.html#joseph-flint,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Guest%2BDiary%2BHow%2BAccess%2BBrokers%2BMaintain%2BPersistence/31600/#comments)

[This is a Guest Diary by Joseph Flint, an ISC intern as part of the SANS.edu BACS [1] program]

Access brokers are groups referred to that obtain initial access in compromised environments, establish persistence through different methods, and sell this access to secondary bad actor groups who contribute to follow up attacks.

CrowdStrike wrote an article outlining desired targets typically involved with compromises that were shown to come from an access broker group [2]. They broke down the top 10 targeted sectors for access brokers by percentage and found the following:

* 21% Academic
* 15% Government
* 13% Technology
* 9% Financial Services
* 9% Healthcare
* 8% Energy
* 7% Manufacturing
* 7% Industrials & Engineering
* 6% Legal
* 5% Insurance

Is your organization, or an organizations security posture you manage a part of this profile? For most Cybersecurity professionals the answer will be an overwhelming yes due to several factors including budgets for internal companies and for various audit requirements. These findings directly put environments related to these fields at risk as bad actors are looking to buy access to these environments.

Proofpoint outlined some commonly observed persistence mechanisms that are utilized by cyber criminals including a SystemBC botnet which is observed routinely in different environments I have personally worked on and across honeypot systems [3]. Many botnets are observed scanning the internet for previously infected hosts. One of these examples comes from my own honeypot. Observed traffic from a Digital Ocean hosted IP [4][5] shows web URL requests looking for this previously mentioned SystemBC directories.

**![](https://isc.sans.edu/diaryimages/images/2025-01-24_figure1.PNG)
Figure 1: Log from a received HTTP request related to SystemBC from a DShield honeypot.**

We can determine this is scanning activity as the honeypot receives several additional requests for other **`.php`** extensions related to SystemBC botnet requests:

**![](https://isc.sans.edu/diaryimages/images/2025-01-24_figure2.PNG)
Figure 2: All URLS requested from suspicious source IP.**

We can see **`/1.php`** which appears suspicious, **`/password.php`**, **`/systembc/password.php`**, a **`/geoip`** directory which may be related to making the system call back to determine location after compromise.

The SystemBC botnet is utilized often by these access broker groups as it is considered a SOCKS5 proxy [6] which contributes to anonymity and masking activity by the original traffic senders.

Now that we have seen an example, how can we properly detect the activity and protect our environments? Firstly, these types of scans occur across the internet constantly. Its widespread across the internet and even benign sources will still scan random hosts. One such example is the Shodan project [7]. This advertises itself as the search engine for the Internet of Everything and accomplishes this by internet wide vulnerability scans. While the ethics behind pointing out vulnerabilities on random hosts across the internet is questionable, if no intrusions take place, it is in a legal grey area.

The news is not all bad, as there are protective measures that can be taken to monitor the activity. Some consideration can be made for the following defensive mechanisms:

* Endpoint Detection and Response (EDR)
* Network Intrusion Detection Systems (NIDS/IDS)
* Device hardening

IDS solutions will often also have rules that check for scanning activity that match known botnet signatures. One well known example of IDS is Snort! This IDS out of the box does not provide SystemBC specific rules [8], however open-source projects make this easier to automate pulling new published rules. One example of this is the pulledpork project [9]. On the website for snort, we see Download rule options allowing you to do it manually [10].

**![](https://isc.sans.edu/diaryimages/images/2025-01-24_figure3.PNG)
Figure 3: Snort rules relevant to various SystemBC detections.**

As we can see from the example, there are detections in place that look to capture various aspects of typical SystemBC traffic. By making use of these various rules, we can better detect abnormal behavior that can be indicative of botnet C2 beaconing.

As proof of concept, I wanted to run this for the request that we received. As observed in figure 3, most rules are for outbound traffic to catch the beaconing to the C2 server. To be proactive, let’s see if we can find a way to capture this web request. I began by downloading the community rules for snort [11]. Unfortunately, after following the set up and unzipping the rules they show no findings for submissions regarding SystemBC.

**![](https://isc.sans.edu/diaryimages/images/2025-01-24_figure4.PNG)
Figure 4: No findings for SystemBC rules by default in our attempted community rules.**

For the sake of brevity, I wanted to ensure this one the only rule present and utilized a separate rule configuration.

**![](https://isc.sans.edu/diaryimages/images/2025-01-24_figure5.PNG)
Figure 5: Display of the rule I established to catch inbound /systembc/password.php requests.**

In this example, the rule is basic because we’re looking for a very specific request. The **`EXTERNAL_NET`** and **`HOME_NET`** variables denoted with the “**`$`**” will be related to how your environment is set up and the IP addresses you utilize. We add an alert message as well as the content we’re looking for, in this case the URL in question.

After some troubleshooting and replaying the packet capture from the initial log we can see Snort detects the traffic and populates our alert.

**![](https://isc.sans.edu/diaryimages/images/2025-01-24_figure6.PNG)
Figure 6: Alert generated after using our PCAP and evaluating it against our Snort rule.**

Typically, we can feed this into a SIEM of our choosing and have this generate an alert that a security analyst can verify for. While this is a basic step, additional changes can be made in the rule to reduce false positives and tune the alert if it becomes too noisy by checking for successful requests.

An additional consideration should be made that with static detections in place, if the bad actors alter their requests and how the malware operates, we will have to create additional rules. In general, it is best to keep the rules as general as possible, without causing too many false positives.

Another option for preventing initial infection is system hardening. The Center for Internet Security has published benchmarks for recommended baseline settings to establish a good security posturing for devices [12]. They cover many different operating systems and can give us a good starting point.

**![](https://isc.sans.edu/diaryimages/images/2025-01-24_figure7.PNG)
Figure 7: Example image of the CIS website with benchmark security recommendations.**

Equally important is the implementation of a good EDR product to monitor our environment. While network telemetry is key in finding C2 beaconing [13], what about the signs that come from end point metrics? Being able to see what commands are being run, what file directories are being created, files being modified, can all lead to malware detections and even shine light on what initial breach patterns are being observed as t...