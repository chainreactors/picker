---
title: Risky Biz News: Canada's tax revenue agency tries to ToS itself out of hacking liability
url: https://riskybiznews.substack.com/p/risky-biz-news-canadas-tax-revenue
source: Over Security - Cybersecurity news aggregator
date: 2023-03-09
fetch_date: 2025-10-04T09:02:56.786864
---

# Risky Biz News: Canada's tax revenue agency tries to ToS itself out of hacking liability

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Canada's tax revenue agency tries to ToS itself out of hacking liability

### In other news: DoppelPaymer ransomware gang members identified; Germany ponders Huawei & ZTE 5G ban; Israel blames Iran for recent ransomware attack.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Mar 08, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

*Today's newsletter intro was written by [Tanya Janca](https://twitter.com/shehackspurple), CEO and Founder of [We Hack Purple](https://wehackpurple.com/).*

The Canada Revenue Agency (CRA), the tax department of Canada, recently updated its terms and conditions to force taxpayers to agree that CRA is not liable if their personal information is stolen while using the My Account online service portal—which, ironically, all Canadians must use when doing their taxes and/or running their business.

The CRA's terms of use assert the agency is not liable because they have "taken all reasonable steps to ensure the security of this Web site".

Excerpt from the CRA terms statement:

> *"10. The Canada Revenue Agency has taken all reasonable steps to ensure the security of this Web site. We have used sophisticated encryption technology and incorporated other procedures to protect your personal information at all times. However, the Internet is a public network and there is the remote possibility of data security violations. In the event of such occurrences, the Canada Revenue Agency is not responsible for any damages you may experience as a result."*

Unfortunately, that is not true. After reviewing the HTTP responses from the CRA My Account login page, it's clear the agency has not configured even some of the most basic security features. For example, security protections for their cookies are not configured, nor are all the recommended security headers used.

Not only is that *not* "all reasonable steps," but the CRA is missing the very basics for securing online web applications.

The terms of use also state that users are not allowed to use "any script, robot, spider, Web crawler, screen scraper, automated query program or other automated device or any manual process to monitor or copy the content contained in any online services."

Looking at the HTTP response headers using web browser developer tools doesn't breach the terms of services, but the CRA must be well aware that internet users perform scans like this all the time.

And it's not the legitimate My Account users who are likely to be the culprits. Unfortunately for Canadians, threat actors don't read terms of use pages.

A statement like this doesn't protect anyone, except CRA, from being held responsible for failing to properly secure Canadian citizens' personal data.

The changes to the terms of service may be the result of numerous data breaches (*see below*) that have already occurred at the CRA (see below), as well as the result of a [class action lawsuit](https://www.canadianlawyermag.com/practice-areas/privacy-and-data/class-action-on-canada-revenue-agency-data-breach-certified-by-federal-court-of-canada/369432) filed against the agency last August.

* **August 2020** - [Statement from the Office of the Chief Information Officer of the Government of Canada on recent credential stuffing attacks](https://www.canada.ca/en/treasury-board-secretariat/news/2020/08/statement-from-the-office-of-the-chief-information-officer-of-the-government-canada-on-recent-credential-stuffing-attacks.html)
* **September 2020** - [Update from the Office of the Chief Information Officer of the Government of Canada on recent cyber attacks](https://www.canada.ca/en/treasury-board-secretariat/news/2020/09/update-from-the-office-of-the-chief-information-officer-of-the-government-canada-on-recent-cyber-attacks.html)
* **August 2020** - [CRA shuts down online services after thousands of accounts breached in cyberattacks](https://www.cbc.ca/news/politics/canada-revenue-agency-cra-cyberattack-1.5688163)
* **March 2021** - [CRA locking 800K Canadian taxpayers out of accounts](https://www.ctvnews.ca/canada/cra-locking-800k-canadian-taxpayers-out-of-accounts-1.5345069?cache=ihmzhdxdoji%3FcontactForm%3Dtrue)

The CRA offloading its responsibility for securing citizens' data via a benign ToS update is a worrisome development from the government agency that should be safeguarding their data in the first place.

The data that CRA holds on every single Canadian is more than enough to help threat actors steal their identity or decide who might be worth robbing or blackmailing.

If threat actors identify particular vulnerabilities in the CRA website, they could also erase or modify taxpayers' data, creating infinitely more terrifying scenarios.

 Nation states, criminal organizations, and even political rivals would be very interested in obtaining the data that the CRA is entrusted with holding on behalf of the citizens of Canada.

You can view the CRA's new terms of use [here](https://drive.google.com/file/d/15Tk3FyGiu9-TErOtM_Wccy3G-tmsI_19/view?usp=sharing).

Attempts to get the CRA to address its web security posture have been met with silence.

[![Twitter avatar for @shehackspurple](https://substackcdn.com/image/twitter_name/w_96/shehackspurple.jpg)

Tanya Janca @shehackspurple

Update: they did not respond. I have sent physical letters and emails.

![Twitter avatar for @shehackspurple](https://substackcdn.com/image/twitter_name/w_40/shehackspurple.jpg)

Tanya Janca @shehackspurple

Dear @DiLebouthillier & @CanRevAgency,
I was asked to accept terms & conditions when I logged into your site. It says if there's a cyber attack and my TAX DATA is stolen, it's not your fault and I MUST accept this risk, (see next tweet) https://t.co/Cr6F6Y6x5C](https://twitter.com/shehackspurple/status/1632263919762046979)[6:16 AM ∙ Mar 5, 2023

---

47Likes6Retweets](https://twitter.com/shehackspurple/status/1632263919762046979)

### **Breaches and hacks**

**Acer confirms hack:** Taiwanese hardware vendor Acer has [confirmed](https://www.pcmag.com/news/acer-breached-hacker-selling-access-to-160gb-of-stolen-data) a security breach after a hacker began selling more than 160GB of data they stole from one of the company's servers. According to the seller, an individual going by the name of Kernelware, the stolen data includes details about the Acer BIOS, confidential presentations, product documentation, ROM, and other binary files. Acer says the files originated from a server for repair technicians.

**Facebook's LLaMA leak:** LLaMA (Large Language Model Meta AI), a collection of large language models developed internally at Meta, was leaked on 4chan last week, marking the first time when a major tech company's proprietary AI model has leaked in full. Prior to the leak, Meta, Facebook's parent company, had provided access to the LLaMA model to select researchers from the AI community. While the leaker hid their identity using the "lla...