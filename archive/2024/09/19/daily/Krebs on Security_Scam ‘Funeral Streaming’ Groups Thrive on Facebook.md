---
title: Scam ‘Funeral Streaming’ Groups Thrive on Facebook
url: https://krebsonsecurity.com/2024/09/scam-funeral-streaming-groups-thrive-on-facebook/
source: Krebs on Security
date: 2024-09-19
fetch_date: 2025-10-06T18:33:43.393217
---

# Scam ‘Funeral Streaming’ Groups Thrive on Facebook

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Scam ‘Funeral Streaming’ Groups Thrive on Facebook

September 18, 2024

[25 Comments](https://krebsonsecurity.com/2024/09/scam-funeral-streaming-groups-thrive-on-facebook/#comments)

Scammers are flooding **Facebook** with groups that purport to offer video streaming of funeral services for the recently deceased. Friends and family who follow the links for the streaming services are then asked to cough up their credit card information. Recently, these scammers have branched out into offering fake streaming services for nearly any kind of event advertised on Facebook. Here’s a closer look at the size of this scheme, and some findings about who may be responsible.

![](https://krebsonsecurity.com/wp-content/uploads/2024/09/fakebookfuneral.png)

KrebsOnSecurity recently heard from a reader named George who said a friend had just passed away, and he noticed that a Facebook group had been created in that friend’s memory. The page listed the correct time and date of the funeral service, which it claimed could be streamed over the Internet by following a link that led to a page requesting credit card information.

“After I posted about the site, a buddy of mine indicated [the same thing] happened to her when her friend passed away two weeks ago,” George said.

Searching Facebook/Meta for a few simple keywords like “funeral” and “stream” reveals countless funeral group pages on Facebook, some of them for services in the past and others erected for an upcoming funeral.

All of these groups include images of the deceased as their profile photo, and seek to funnel users to a handful of newly-registered video streaming websites that require a credit card payment before one can continue. Even more galling, some of these pages request donations in the name of the deceased.

It’s not clear how many Facebook users fall for this scam, but it’s worth noting that many of these fake funeral groups attract subscribers from at least some of the deceased’s followers, suggesting those users have subscribed to the groups in anticipation of the service being streamed. It’s also unclear how many people end up missing a friend or loved one’s funeral because they mistakenly thought it was being streamed online.

![](https://krebsonsecurity.com/wp-content/uploads/2024/09/vortexvibe.png)

One of many look-alike landing pages for video streaming services linked to scam Facebook funeral groups.

George said their friend’s funeral service page on Facebook included a link to the supposed live-streamed service at **livestreamnow[.]xyz**, a domain registered in November 2023.

According to [DomainTools.com](https://www.domaintools.com), the organization that registered this domain is called “**apkdownloadweb**,” is based in Rajshahi, Bangladesh, and uses the DNS servers of a Web hosting company in Bangladesh called **webhostbd[.]net**.

A search on “apkdownloadweb” in DomainTools shows three domains registered to this entity, including **live24sports[.]xyz** and **onlinestreaming[.]xyz**. Both of those domains also used webhostbd[.]net for DNS. Apkdownloadweb has [a Facebook page](https://www.facebook.com/apkdownloadweb/?paipv=0&eav=AfZR8fNrOqm6A-vmGfCkVTafTNaCEU_fcg0bwO2N-93FU5Rcqzuw2K9taQ7yfU9srjU&_rdr), which shows a number of “live video” teasers for sports events that have already happened, and says its domain is **apkdownloadweb[.]com**.

Livestreamnow[.]xyz is currently hosted at a Bangladeshi web hosting provider named **cloudswebserver[.]com**, but historical DNS records show this website also used DNS servers from webhostbd[.]net.

The Internet address of livestreamnow[.]xyz is **148.251.54.196**, at the hosting giant Hetzner in Germany. DomainTools shows this same Internet address is home to [nearly 6,000 other domains](https://krebsonsecurity.com/wp-content/uploads/2024/09/148-251-54-196-pdns.csv) (.CSV), including hundreds that reference video streaming terms, like **watchliveon24[.]com** and **foxsportsplus[.]com**.

There are thousands of domains at this IP address that include or end in the letters “**bd**,” the country code top-level domain for Bangladesh. Although many domains correspond to websites for electronics stores or blogs about IT topics, just as many contain a fair amount of placeholder content (think “lorem ipsum” text on the “contact” page). In other words, the sites appear legitimate at first glance, but upon closer inspection it is clear they are not currently used by active businesses.

The passive DNS records for 148.251.54.196 show a surprising number of results that are basically two domain names mushed together. For example, there is **watchliveon24[.]com.playehq4ks[.]com**, which displays links to multiple funeral service streaming groups on Facebook.

![](https://krebsonsecurity.com/wp-content/uploads/2024/09/watchliveontv.png)

Another combined domain on the same Internet address — livestreaming24[.]xyz.allsportslivenow[.]com — lists dozens of links to Facebook groups for funerals, but also for virtually all types of events that are announced or posted about by Facebook users, including graduations, concerts, award ceremonies, weddings, and rodeos.

Even community events promoted by state and local police departments on Facebook are fair game for these scammers. A Facebook page maintained by the police force in Plympton, Mass. for a town social event this summer called [Plympton Night Out](https://www.facebook.com/story.php/?story_fbid=817825613867240&id=100069194260186) was quickly made into two different Facebook groups that informed visitors they could stream the festivities at either **espnstreamlive[.]co** or **skysports[.]live**.

## WHO’S BEHIND THE FAKEBOOK FUNERALS?

Recall that the registrant of livestreamnow[.]xyz — the bogus streaming site linked in the Facebook group for George’s late friend — was an organization called “Apkdownloadweb.” That entity’s domain — **apkdownloadweb[.]com** — is registered to a [**Mazidul Islam**](https://www.linkedin.com/in/mazidul-islam-274174205/) in Rajshahi, Bangladesh (this domain is also using Webhostbd[.]net DNS servers).

Mazidul Islam’s LinkedIn page says he is the organizer of a now defunct IT blog called gadgetsbiz[.]com, which DomainTools finds was registered to a **Mehedi Hasan** from Rajshahi, Bangladesh.

To bring this full circle, DomainTools finds the domain name for the DNS provider on all of the above-mentioned sites  — webhostbd[.]net — was originally registered to a **Md Mehedi**, and to the email address **webhostbd.net@gmail.com** (“MD” is a common abbreviation for Muhammad/Mohammod/Muhammed).

A search on that email address at Constella finds a breached record from the data broker Apollo.io saying its owner’s full name is **Mohammod Mehedi Hasan.** Unfortunately, this is not a particularly unique name in that region of the world.

But as luck would have it, sometime last year the administrator of apkdownloadweb[.]com managed to infect their Windows PC with password-stealing malware. We know this because the raw logs of data stolen from this administrator’s PC were indexed by the breach tracking service [Constella Intelligence](https://www.constella.ai) [full disclosure: As of this month, Constella is an advertiser on this website].

These so-called “stealer logs” are mostly generated by opportunist...