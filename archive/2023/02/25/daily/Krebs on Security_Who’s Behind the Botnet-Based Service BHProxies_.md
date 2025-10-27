---
title: Who’s Behind the Botnet-Based Service BHProxies?
url: https://krebsonsecurity.com/2023/02/whos-behind-the-botnet-based-service-bhproxies/
source: Krebs on Security
date: 2023-02-25
fetch_date: 2025-10-04T08:06:37.488348
---

# Who’s Behind the Botnet-Based Service BHProxies?

Advertisement

[![](/b-ninjio/9.png)](https://ninjio.com/lp46d-krebs/)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Who’s Behind the Botnet-Based Service BHProxies?

February 24, 2023

[15 Comments](https://krebsonsecurity.com/2023/02/whos-behind-the-botnet-based-service-bhproxies/#comments)

A security firm has discovered that a six-year-old crafty botnet known as **Mylobot** appears to be powering a residential proxy service called **BHProxies**, which offers paying customers the ability to route their web traffic anonymously through compromised computers. Here’s a closer look at Mylobot, and a deep dive into who may be responsible for operating the BHProxies service.

![](https://krebsonsecurity.com/wp-content/uploads/2023/02/bhproxies.png)

First identified in 2017 by the security firm [Deep Instinct](https://www.deepinstinct.com/blog/meet-mylobot-a-new-highly-sophisticated-never-seen-before-botnet-thats-out-in-the-wild), Mylobot employs a number of fairly sophisticated methods to remain undetected on infected hosts, such as running exclusively in the computer’s temporary memory, and waiting 14 days before attempting to contact the botnet’s command and control servers.

Last year, researchers at **Minerva Labs** spotted the botnet [being used to blast out sextortion scams](https://minerva-labs.com/blog/mylobot-2022-so-many-evasive-techniques-just-to-send-extortion-emails/). But according to [a new report](https://www.bitsight.com/blog/mylobot-investigating-proxy-botnet) from **BitSight**, the Mylobot botnet’s main functionality has always been about transforming the infected system into a proxy.

The Mylobot malware includes more than 1,000 hard-coded and encrypted domain names, any one of which can be registered and used as control networks for the infected hosts. BitSight researchers found significant overlap in the Internet addresses used by those domains and a domain called **BHproxies[.]com**.

BHProxies sells access to “residential proxy” networks, which allow someone to rent a residential IP address to use as a relay for their Internet communications, providing anonymity and the advantage of being perceived as a residential user surfing the web. The service is currently advertising access to more than 150,000 devices globally.

“At this point, we cannot prove that BHProxies is linked to Mylobot, but we have a strong suspicion,” wrote BitSight’s **Stanislas Arnoud**.

To test their hypothesis, BitSight obtained 50 proxies from BHProxies. The researchers were able to use 48 of those 50 proxies to browse to a website they controlled — allowing them to record the true IP addresses of each proxy device.

“Among these 48 recovered residential proxies IP addresses, 28 (58.3%) of those were already present in our sinkhole systems, associated with the Mylobot malware family,” Arnoud continued. “This number is probably higher, but we don’t have a full visibility of the botnet. This gave us clear evidence that Mylobot infected computers are used by the BHProxies service.”

BitSight said it is currently seeing more than 50,000 unique Mylobot infected systems every day, and that India appears to be the most targeted country, followed by the United States, Indonesia and Iran.

“We believe we are only seeing part of the full botnet, which may lead to more than 150,000 infected computers as advertised by BHProxies’ operators,” Arnoud wrote.

## WHO’S BEHIND BHPROXIES?

The website BHProxies[.]com has been advertised for nearly a decade on the forum **Black Hat World** by the user **BHProxies**. BHProxies has authored 129 posts on Black Hat World since 2012, and their last post on the forum was in December 2022.

BHProxies initially was fairly active on Black Hat World between May and November 2012, after which it suddenly ceased all activity. The account didn’t resume posting on the forum until April 2014.

According to cyber intelligence firm [Intel 471](https://www.intel471.com), the user BHProxies also used the handle “**hassan\_isabad\_subar**” and marketed various software tools, including “Subar’s free email creator” and “Subar’s free proxy scraper.”

Intel 471’s data shows that hassan\_isabad\_subar registered on the forum using the email address **jesus.fn.christ@gmail.com**. In a June 2012 private message exchange with a website developer on Black Hat World, hassan\_isabad\_subar confided that they were working at the time to develop two websites, including the now-defunct **customscrabblejewelry.com**.

[DomainTools.com](https://www.domaintools.com) reports that customscrabblejewelry.com was registered in 2012 to a **Teresa Shotliff** in Chesterland, Ohio. A search on jesus.fn.christ@gmail.com at [Constella Intelligence](https://www.constellaintelligence.com), a company that tracks compromised databases, shows this email address is tied to an account at the fundraising platform **omaze.com,** for a **Brian Shotliff** from Chesterland, Ohio.

Reached via LinkedIn, Mr. Shotliff said he sold his BHProxies account to another Black Hat World forum user from Egypt back in 2014. Shotliff shared an April 2014 password reset email from Black Hat World, which shows he forwarded the plaintext password to the email address **legendboy2050@yahoo.com**. He also shared a PayPal receipt and snippets of Facebook Messenger logs showing conversations in March 2014 with legendboy2050@yahoo.com.

Constella Intelligence confirmed that legendboy2050@yahoo.com was indeed another email address tied to the hassan\_isabad\_subar/BHProxies identity on Black Hat World. Constella also connects legendboy2050 to Facebook and Instagram accounts for one **Abdala Tawfik** from Cairo. This user’s [Facebook page](https://www.facebook.com/abdala.tawfik/photos) says Tawfik also uses the name **Abdalla Khafagy**.

Tawfik’s [Instagram account](https://www.instagram.com/AbdalaTawfik/?fbclid=IwAR252TAYDV-MZRFSzTEzMBJ4xwNWziITiuAEylUuf2J5xhjhmzxGpoHRRDU) says he is a former operations manager at the social media network **TikTok**, as well as a former director at **Crypto.com**.

Abdalla Khafagy’s [LinkedIn profile](https://www.linkedin.com/in/abdu-abdalla-khafagy-116635168/) says he was “global director of community” at Crypto.com for about a year ending in January 2022. Before that, the resume says he was operations manager of TikTok’s Middle East and North Africa region for approximately seven months ending in April 2020.

Khafagy’s LinkedIn profile says he is currently founder of **LewkLabs**, a Dubai-based “blockchain-powered, SocialFi content monetization platform” that [last year reported funding of $3.26 million](https://www.globenewswire.com/news-release/2022/01/15/2367456/0/en/LEWK-Announces-Successful-Closing-Of-3-26M-Seed-Private-Sale.html) from private investors.

The only experience listed for Khafagy prior to the TikTok job is labeled “Marketing” at “Confidential,” from February 2014 to October 2019.

Reached via LinkedIn, Mr. Khafagy told KrebsOnSecurity that he had a Black Hat World account at some point, but that he didn’t recall ever having used an account by the name BHProxies or hassan\_isabad\_subar. Khafagy said he couldn’t remember the name of the account he had on the forum.

“I had an account that was simply hacked from me shortly after and I never bothered about it because it wasn’t mine in the first place,” he explained.

Khafagy declined to elaborate on the five-year stint in his resume marked “Confidential.” When asked...