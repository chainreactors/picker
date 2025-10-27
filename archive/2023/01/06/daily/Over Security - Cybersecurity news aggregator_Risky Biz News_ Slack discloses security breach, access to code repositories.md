---
title: Risky Biz News: Slack discloses security breach, access to code repositories
url: https://riskybiznews.substack.com/p/risky-biz-news-slack-discloses-security
source: Over Security - Cybersecurity news aggregator
date: 2023-01-06
fetch_date: 2025-10-04T03:11:49.691710
---

# Risky Biz News: Slack discloses security breach, access to code repositories

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Slack discloses security breach, access to code repositories

### In other news: ENLBufferPwn vulnerability impacts Nintendo consoles; 3Commas eats its words after disclosing security breach; PyTorch discloses supply chain attack.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Jan 05, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

The Risky Business team is still on its holiday break, but we thought to put out this weekly edition with some of the past week's biggest infosec stories.

The biggest story, by far, even if it didn't get any media coverage, was [Slack's secret data breach disclosure](https://slack.com/intl/en-au/blog/news/slack-security-update) published just ahead of New Year's Eve.

The company said a threat actor stole "Slack employee tokens" and gained access to its GitHub source code repositories.

This happened on December 27, according to Slack, and the company disclosed the breach four days later, on December 31, so a pretty quick turnaround from detection to disclosure.

The incident is eerily similar to what [Okta disclosed](https://sec.okta.com/articles/2022/12/okta-code-repositories) ahead of Christmas when the company also found that someone used a TravisCI token to gain access to its GitHub repos. Just like Okta, Slack said the intruder didn't gain access to its main infrastructure or to any customer data.

It's unclear if the two incidents are related, as both disclosures lack fine-grained details about what's what. You can blame lawyer-speak for that.

**Post-publication edit:** Two hours after we sent out this newsletter, CircleCI also [disclosed](https://circleci.com/blog/january-4-2023-security-alert/) a major security breach, admitting that a threat actor gained access to its infrastructure and advised all users to rotate their CircleCI tokens and review their environments for unauthorized access via CircleCI integrations that may have taken place between December 21, 2022 and January 4, 2023.

In a previous newsletter, we reported that in early December, GitHub’s security team had sent out alerts to several companies about suspicious activity tied to their [Heroku](https://mastodon.social/%40kurtseifried/109474509351487448) and [TravisCI](https://twitter.com/guewenb/status/1600751900114100225) [integrations](https://twitter.com/peter_szilagyi/status/1600591604280360961). It previously did the same [in April](https://github.blog/2022-04-15-security-alert-stolen-oauth-user-tokens/) as well. With the recent CircleCI disclosure, it sure looks that at least one very determined threat actor is very enamoured with using CI/CD service providers as a way to gain access to private corporate code-hosting infrastructure.

> *Risky Business News, both the podcast and newsletter, will be resuming their regular three-times-per-week output (Monday, Wednesday, Friday) next week, starting January 9.*

### Breaches and hacks

**Twitter data leak:** On Christmas, a threat actor [put up for sale](https://www.linkedin.com/posts/alon-gal-utb_data-gdpr-database-activity-7012389466937913344-zpMO/) the public and private details of more than 400 million Twitter users that they claimed to have scraped off the site using a vulnerability in the platform's API. This week, the details of more than 235 million Twitter users were [leaked online](https://www.linkedin.com/posts/alon-gal-utb_twitter-database-breach-activity-7016314513406726145-15kV) and are accessible to anyone.

**Potsdam cyberattack:** The German city of Potsdam took its IT network offline on December 29 following a warning from the security team of the state of Brandenburg that the city's network was being targeted with a brute-force attack. [Officials said](https://www.potsdam.de/2-umfangreiche-sicherheits-tests-nach-praeventiver-abschaltung-der-internetverbindungen) they plan to reconnect their network to the internet next week following a series of security audits.

**Port of Lisbon ransomware attack:** The administration of the port of Lisbon (Portugal) suffered a [ransomware attack](https://therecord.media/port-of-lisbon-website-still-down-as-lockbit-gang-claims-cyberattack/) over Christmas. The port's activity wasn't disrupted. However, the subsequent disruptions were caused by a [planned workers' strike](https://www.theportugalnews.com/news/2022-12-30/port-strike-affecting-supply-of-essential-goods/73425).

**SickKids ransomware attack:** The LockBit ransomware gang has [apologized](https://mastodon.social/%40AlvieriD%40infosec.exchange/109609716328504540) for its attack on the Sick Kids Hospital chain and released a free decrypter to help the victim recover files without paying.

**Wabtec ransomware attack:** US rail and locomotive company Wabtec has [confirmed](https://www.wabteccorp.com/data-security-incident-update-personal-data-breach-public-communication) a ransomware attack at the hands of the LockBit ransomware gang. The incident took place in June 2022 and impacted its US, Canada, UK, and Brazil operations.

**3Commas cyber-heist:** The CEO of the 3Commas cryptocurrency platform has [confirmed](https://3commas.io/blog/notice-on-api-data-disclosure-incident) that a hacker has stolen the API keys of its users after multiple victims have claimed over the past two months that they had unauthorized access to their cryptocurrency accounts via the 3Commas platform and lost assets worth millions of USD. After news of some of these hacks started to become public, the hacker leaked 10,000 API keys on Pastebin as a way to advertise a larger batch of 100,000 keys. 3Commas came under heavy criticism for [denying the hack](https://3commas.io/blog/fake-screenshot-cloudflare-logs) for two months, claiming that users were phished rather than admitting a breach on its side.

**PyTorch supply chain incident:** The team behind the PyTorch machine learning library said it discovered a supply chain attack that impacted its nightly builds on Linux. Between December 25, 2022, and December 30, 2022, a previously safe dependency named "*torchtriton*" turned malicious and installed a binary that could collect system information and read sensitive files, the [team said](https://pytorch.org/blog/compromised-nightly-dependency/).

**T-Mobile breach settlement:** Users who've been affected by T-Mobile's 2021 data breach are eligible to receive up to $100 from a $350 million settlement. The catch—[they have weeks to make a claim](https://www.cnet.com/personal-finance/t-mobiles-350-million-data-breach-settlement-youve-got-just-weeks-to-claim-money/).

**LastPass gets sued:** LastPass has been [sued](https://www.courtlistener.com/docket/66696047/doe-individually-and-on-behalf-of-all-others-similarly-situated-v/) over its disastrous handling of the August 2022 security breach, which resulted in a second breach in [December 2022](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/), and then in...