---
title: Threat Actors leverage Chinese SHOPOEM Platforms to spread infamous scam campaign
url: https://labs.yarix.com/2024/08/shopoem-scam-campaign/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-02
fetch_date: 2025-10-06T18:05:00.990740
---

# Threat Actors leverage Chinese SHOPOEM Platforms to spread infamous scam campaign

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Threat Actors leverage Chinese SHOPOEM Platforms to spread infamous scam campaign

* [Home](https://labs.yarix.com "Go to Home Page")
* Threat Actors leverage Chinese SHOPOEM Platforms to spread infamous scam campaign

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2024/07/copertina2-1024x445.png)

01Aug01/08/2024

## Threat Actors leverage Chinese SHOPOEM Platforms to spread infamous scam campaign

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2024-08-01T11:48:13+02:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   13 minutes

## **Introduction**

As Yarix Cyber Threat Intelligence (YCTI) team, we keep a close eye on and track phishing and scam campaigns on a daily basis. Protecting the reputation and image of client companies is one of the main goals of YCTI’s Brand Abuse team. This includes determining whether and how their officially registered trademarks are being used to spread fraudulent campaigns that deceive people into divulging their personal and financial information in what are known as “fake shops”.

Fake shops are scam websites designed to imitate a legitimate online store, often of well-known brands. They entice users with discounted goods, but after payment is made in advance, the products are never delivered. For this reason, we monitor daily to see if any newly registered domains could be used for phishing or scam activities.

Tracking and analyzing as many malicious infrastructures as possible in the early stages is one of the aims of our team, in order to compare their efficacy and proactively identify similarities ahead of time.

While investigating these kinds of websites, we discovered something quite intriguing: generally, based on the type of phishing kit or Threat Actor that initiated the campaign, we are able to determine, upon first glance, whether or not we have previously dealt with that kind of questionable site. In this instance, a number of them had the exact same layout, different from other websites we had already tracked. At that point, we really got into those sites.

Bit by bit, we found out that Threat Actors were using legitimate Chinese e-commerce platforms, such as **SHOPOEM**, to create phony websites that falsely used the official Trademarks of famous retail businesses to deceive people all over the world.

By maki­ng advertisements to market deals and discounts on social media platforms like Facebook, Instagram, and others, the Threat Actors might take advantage of these platforms and redirect users to bogus websites.

This blog article aims to explain the modus operandi of this widely used campaign, including how Threat Actors operate and why this type of operation is both risky and very successful.

## **Overview**

As previously said, we monitor daily the registration of newly registered domains to detect as soon as we can if some could potentially be used for phishing activities or scam campaigns.

In fact, during our activities, we were investigating a dubious domain that posed as the official online store of a well-known fashion brand. It was offering goods at an absurdly low price, with up to 90% off. After examining the domain, its creation date and information contained in its Whois record, it became evident that the website was a copy of the fashion brand’s original online store.

As you have understood so far, we sadly come across a lot of fake shops every day. Sometimes they have a distinct structure, whereas other times we see a particular pattern that is utilized to replicate different ones. That pattern is what makes us happy – like, big smiles happy – and lets us realize that those sites are probably made by the same Threat Actor(s). So, now is the right time to begin our more thorough investigation.

Hereafter are two examples of what a fraudulent website might look like:

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x72.jpg)

*Picture 1. Air Jordan fake shop https://www.jordanfroutlet.com/*

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x68.jpg)

*Picture 2. Kenzo fake shop https://www.kenzosale.shop/*

Are they familiar? These days, it is not that hard to come across clone websites and fraudulent stores. It is most likely one of the simplest methods Threat Actors use to take advantage of people financially. Using their shiny, deeply discounted websites, they entice users – frequently succeeding in doing so – given that anyone is drawn to deals, right? Threat Actors are well aware of it as well! And, let’s be honest, it is not always that simple to distinguish a fraudulent website from the real one, isn’t it?

## **The Investigation**

We may now proceed to discuss how we ultimately looked into the matter, having demonstrated that it is easier than we imagine to be duped.

Once we encounter the same pattern used for various fake online shops, we examine the **distinctive characteristics** that we can subsequently link to the same Threat Actors and **how** they utilize them to propagate the fraud whenever we come across the same pattern utilized for numerous phony web stores.

It was challenging to continue the study in this instance in particular because a large number of the sites appeared to be undergoing maintenance. Well, needless to say,  we didn’t give up. As a result, we found that it was a façade employed by the Threat Actors, and that if we visited the websites using a different user-agent, such as a smartphone, we could actually see the fraudulent content:

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x69.jpg)

*Picture 3. Initial page of the sites*

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x47.jpg)

*Picture 4. The same site visited with a different user-agent*

When we browse the websites, we frequently focus on the “*Contact us*” part since this is where Threat Actors usually leave email addresses they created specifically for the campaign, which they then use as customer service contact of the targeted brand.

We have examined nearly 14,000 bogus domains detected in the last two months as part of this campaign and over **1800** email addresses established by the Threat Actors and reported in these websites have been found.

Some of the email addresses the Threat Actors created for this campaign that have been discovered thus far are listed below:

* team@vipserviceonline.com
* aria@lsnservice.com
* service\_oneline@hotmail.com
* customer@rankboostpro.shop
* customer@help-centerus.com
* support@lfccq.com
* contact@smartcustomerserve.com
* support@postsales-handling.com
* support@rhosyns.com
* info@supportserving.com
* service@qddie.com
* hudockwestgaardkcfb1319@gmail.com
* support@urbancustomerserve.com
* onsale@pre-sale-service.com
* service@customerserviceteams.com
* alisup2024@hotmail.com
* qiuqiudaqiu123@gmail.com
* admin@pre-sale-service.com
* customer@bh-christmasbigsale.com
* service@questions-answers.vip
* jerseys@customersupportzone.com

Even if the e-mail addresses are meant to be for customer care, the majority of them does not have an active mail server (MX record), which prevents them from receiving emails.

By examining the website’s html code, we were able to determine that the Threat Actors were hosting their new websites on **CDN**s (Content Delivery Networks) where they probably also managed their database.

These CDNs are connected to the Chinese e-commerce platform **SHOPOEM**, which allows customers to register, develop cu...