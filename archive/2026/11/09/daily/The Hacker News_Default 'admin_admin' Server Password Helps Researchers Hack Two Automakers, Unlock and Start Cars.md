---
title: Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars
url: https://thehackernews.com/2026/11/default-adminadmin-server-password.html
source: The Hacker News
date: 2026-11-09
fetch_date: 2026-11-10T09:03:25.812255
---

# Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)

**Swati Khandelwal**Nov 09, 2026Vulnerability / Automotive Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiI85M0pHHPiXe5ar2VpaGsBVRzxoYfZhpQTKgWqd8YGjK9Nyaca-z6XrGT3jT0lqh41qe-cAjb33_r7JErd7rB1CfuWkgTP_z-_IJkpQPWebz1GeEvSu9QpE5XYWRMOfhYTHmzhbkFB07hzSuV1FYARdaIWjfB_mUoX1_eMjl_3dOaSUFpTQvjt-34eQo/s1700-nu-rw-lo-l85-e365/login-car.jpg)

The login systems behind two car brands' mobile apps could be taken over completely, two security researchers found, allowing them to access any customer's account and, for an owner with a connected car, unlock the doors and start the engine.

Both apps signed customers in through **ForgeRock**, an identity platform now part of **Ping Identity**, and on those servers the researchers reached an administrator console that still used its default password.

They tested the full attack only on their own and consenting owners' cars in the United States, in February 2026, and both systems were fixed about two hours after they reported the problem.

Shubham Shah and Sam Curry published their work late last week. They had started with the apps: both brands signed customers in through the same platform, which runs in two parts: one for login and one, called **OpenIDM**, that holds customer records.

OpenIDM comes with a built-in administrator console powered by the Apache Felix tool. ForgeRock's own hardening guide tells operators to remove this console or protect it before going live because it stores its own password separately from the rest of the system. On these servers, it was still there and still used the documented default: the word admin for both the username and the password.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The console was blocked from the open internet, but the edge that guards the site and the Java software behind it read the same web address differently. By adding encoded slashes and extra characters, the researchers made the edge treat the request as a harmless static file while the server treated it as the path to the console, and the default password did the rest. The full method is in their [technical analysis](https://samcurry.net/forgerock).

Inside the console, the researchers used a built-in scheduler to run small scripts that execute their own code on the identity server. That gave them a command prompt on the machine that holds the customer records for both brands' logins.

The records sat behind the same block as the console, but the researchers' code reached them from inside the server. They changed a target account's email address and password, signed in as that customer through the normal app, and received the same access tokens the real app uses.

Those tokens were the keys to the car. Using the account's own vehicle commands, the researchers unlocked the doors and started the engine of a test car, with the owner standing next to it, then stopped the engine and locked it again.

The researchers were careful about what they had shown. They reported being able to open a session for any customer account on the affected servers, but they ran the vehicle commands only on cars they owned or were allowed to use. They said they "tested the complete chain only with US accounts and vehicles."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgBPYL8MGaFonhebJnb6roJSAsehRQi6WeCNvwFHrpMwnUk9Wsjraz7YBqh4TATjaPN1t7bslpCRxLkrQ4N-iEdB8MlOGJpM2zJRCB8zkyQORvpfoLhDaky2dQ_hbxI1vWgg6e4vn7DMD8-WG4816RwJ9OxHBSEHzKpBkATB3zKgjLke81QGVsm0YS4-g/s1700-nu-rw-lo-l85-e365/door.jpg)

Shubham Shah published a second attack on the Australian systems behind the same brands. There, the way in was different: admin credentials for the identity server had been left in the app's code, intended for a test setup. He set out the full [Australia chain](https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/) in a separate post.

With both attacks together, the researchers said, they could send unlock and engine-start commands to the brands' cars in Australia, the United States, and Canada. That second post does not give a date for when the Australian systems were fixed.

The attack left little for an owner to notice. Changing the email and password did not log the owner out of their app, and the researchers could direct the account's alerts to their own phone, keeping them off the owner's phone.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The researchers put the real email address back after the test. Neither write-up says whether anyone else found or used the path before it was closed.

### What Identity Teams Should Check

The brands' mistake was in how they ran ForgeRock, not a new bug in the product, so there is no CVE, the public ID that tracks a flaw, and no vendor advisory to follow. The console and its default password have been documented for years, and the maker's [production hardening](https://docs.pingidentity.com/pingidm/7.2/security-guide/security-remove-dev-tools.html) guide already tells operators to remove the console or change its password before going live.

For teams running the same identity software, now sold as PingIDM, two checks matter:

* Look for the Apache Felix console at /system/console, and remove it or change its default password.
* Do not count on edge or WAF path rules to hide an admin page. A path the edge and the server read differently can slip past the rules, as it did here.

The two researchers have a long record of this kind of work, usually breaking into the web systems behind the apps rather than the cars themselves. They have shown remote access to vehicles from Honda, Kia, and Subaru, among others.

A [Subaru flaw](https://thehackernews.com/2025/02/thn-weekly-re...