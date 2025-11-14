---
title: Russian Hackers Create 4,300 Fake Travel Sites to Steal Hotel Guests' Payment Data
url: https://thehackernews.com/2025/11/russian-hackers-create-4300-fake-travel.html
source: The Hacker News
date: 2025-11-13
fetch_date: 2025-11-14T03:13:41.828827
---

# Russian Hackers Create 4,300 Fake Travel Sites to Steal Hotel Guests' Payment Data

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Russian Hackers Create 4,300 Fake Travel Sites to Steal Hotel Guests' Payment Data](https://thehackernews.com/2025/11/russian-hackers-create-4300-fake-travel.html)

**Nov 13, 2025**Ravie LakshmananOnline Fraud / Payment Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNhnn_FN1YzknlukZNSETlpsGEWJunJd8RntQwlE18t1lnZfUv4tbHe_CJkkLPVlZsRTU3_mz2Tfc1hsiCwmm2o-WcAz5zlXQqja_tPqI9__l8xz7MZDJC3rqW17VKFA3sy5v5Vyjd5UuqiytOPADhVEW7ZtFU2Uw7GobK91GhWnm7Bei_mTBMhLs83TQW/s790-rw-e365/travel-sites.jpg)

A Russian-speaking threat behind an ongoing, mass phishing campaign has registered [more than 4,300 domain names](https://github.com/netcraftcom/public-iocs/blob/main/2025-11%20hotel%20phishing%20IOCs.csv) since the start of the year.

The [activity](https://www.netcraft.com/blog/thousands-of-domains-target-hotel-guests-in-massive-phishing-campaign), per Netcraft security researcher Andrew Brandt, is designed to target customers of the hospitality industry, specifically hotel guests who may have travel reservations with spam emails. The campaign is said to have begun in earnest around February 2025.

Of the 4,344 domains tied to the attack, 685 domains contain the name "Booking", followed by 18 with "Expedia," 13 with "Agoda," and 12 with "Airbnb," indicating an attempt to target all popular booking and rental platforms.

"The ongoing campaign employs a sophisticated phishing kit that customizes the page presented to the site visitor depending on a unique string in the URL path when the target first visits the website," Brandt said. "The customizations use the logos from major online travel industry brands, including Airbnb and Booking.com."

The attack begins with a phishing email urging recipients to click on a link to confirm their booking within the next 24 hours using a credit card. Should they take the bait, the victims are taken to a fake site instead after initiating a chain of redirects. These bogus sites follow consistent naming patterns for their domains, featuring phrases like confirmation, booking, guestcheck, cardverify, or reservation to give them an illusion of legitimacy.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The pages support 43 different languages, allowing the threat actors to cast a wide net. The page then instructs the victim to pay a deposit for their hotel reservation by entering their card information. In the event that any user directly attempts to access the page without a unique identifier called AD\_CODE, they are greeted with a blank page. The bogus sites also feature a fake CAPTCHA check that mimics Cloudflare to deceive the target.

"After the initial visit, the AD\_CODE value is written to a cookie, which ensures that subsequent pages present the same impersonated branding appearance to the site visitor as they click through pages," Netcraft said. This also means that changing the "AD\_CODE" value in the URL produces a page targeting a different hotel on the same booking platform.

As soon as the card details, along with the expiration data and CVV number, are entered, the page attempts to process a transaction in the background, while an "support chat" window appears on the screen with steps to complete a supposed "3D Secure verification for your credit card" to secure against fake bookings.

The identity of the threat group behind the campaign remains unknown, but the use of Russian for source code comments and debugger output either alludes to their provenance or is an attempt to cater to prospective customers of the phishing kit who may be looking to customize it to suit their needs.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGps1FF8sBCEHAab2x0bjbqCh_yzKBNavjnU6_7a8PF5rsnF-hePdgluqxCJrp3XjvraFIdf-5o9NcyVsqD8yI0cBBoEtLdu2T9SeV_QjlOtpX7KDIGtAgYk9qorAV_BapPQp74QYXWqtZ4H7csbjxnQg3Zp2Q3ADlORXSx0F9KKxTWBHV0TXvv6s-_Djd/s790-rw-e365/codeode.jpg)

The disclosure comes days after Sekoia [warned](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html) of a large-scale phishing campaign targeting the hospitality industry that lures hotel managers to ClickFix-style pages and harvest their credentials by deploying malware like PureRAT and then approach hotel customers via WhatsApp or emails with their reservation details and confirm their booking by clicking on a link.

Interestingly, one of the indicators shared by the French cybersecurity company – guestverifiy5313-booking[.]com/67122859 – matches the domain pattern registered by the threat actor (e.g., verifyguets71561-booking[.]com), raising the possibility that these two clusters of activity could be related. The Hacker News has reached out to Netcraft for comment, and we will update the story if we hear back.

In recent weeks, large-scale phishing campaigns have also [impersonated](https://cyble.com/blog/multi-brand-phishing-campaign-harvests-credentials/) multiple brands like Microsoft, Adobe, WeTransfer, FedEx, and DHL to steal credentials by distributing HTML attachments through email. The embedded HTML files, once launched, display a fake login page while JavaScript code captures credentials entered by the victim and sends them directly to attacker-controlled Telegram bots, Cyble said.

The campaign has mainly targeted a wide range of organizations across Central and Eastern Europe, particularly in the Czech Republic, Slovakia, Hungary, and Germany.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

"The attackers distribute phishing emails posing as legitimate customers or business partners, requesting quotations or invoice confirmations," the company pointed out. "This regional focus is evident through targeted recipient domains belonging to local enterprises, distributors, government-linked entities, and hospitality firms that routinely process RFQs and supplier communications."

Furthermore, phishing kits have been put to use in a large-scale campaig...