---
title: Gyazo Breach Exposes 23.62 Million User Records and 490 Million Image Metadata Records
url: https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html
source: The Hacker News
date: 2026-09-17
fetch_date: 2026-09-18T06:53:39.938781
---

# Gyazo Breach Exposes 23.62 Million User Records and 490 Million Image Metadata Records

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Gyazo Breach Exposes 23.62 Million User Records and 490 Million Image Metadata Records](https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html)

**Swati Khandelwal**Sep 17, 2026Data Breach / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjo_VMcM5A8FocwrVqXOjmk-BvMd3D_JA6RIur9wT4Gca5jQjiLLinldpcu3u2hWmJQeJZg5nhVRBwxHe2y0BHg1TZEd046RkPLatyX5JN-7_WtuRyPMX3VnMCAs7tfCYOSghFuBCUT6HFyCBH-bLeAPWlAj9TPtAn1sitCktd2vp_pJr6VtzHd2_EFDpo/s1700-nu-rw-lo-l85-e365/gyazo.jpg)

A security breach at **Gyazo**, Helpfeel's image-sharing service, exposed about 23.62 million user records, including email addresses and password hashes, the Kyoto-based company said in a [notice](https://corp.helpfeel.com/en/news/news-20260916) published Wednesday.

It also exposed about 490 million image metadata records, mostly for images from January 2019 or earlier, including the IDs that make up Gyazo image links.

Helpfeel said those IDs could be used to view the images without permission, and that it has temporarily disabled viewing of some of them.

Helpfeel asked every Gyazo user to change their password and to change it on any other service that uses the same or a similar one. It also asked users to watch for suspicious emails or messages related to the incident.

The attacker gained access through a vulnerability in Gyazo's image upload server, ran arbitrary commands on Helpfeel's systems, and accessed Gyazo's database, the company said. It has not said what kind of flaw it was.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Helpfeel said no payment information, including credit card numbers, was exposed. The exposed user records can include the following, and the fields present vary from user to user:

* Name (any text the user entered, such as a name or nickname)
* Email address
* Password hash
* User ID
* Device ID
* Login session ID
* X (formerly Twitter) integration token, if the account was connected
* Email address used for Google single sign-on (SSO), if connected
* Profile information
* Language preference
* Registration date and time
* Last login date and time
* Subscription plan
* Billing status (no credit card numbers or other payment details)
* Usage statistics

The 23.62 million figure counts records. Helpfeel said they include anonymous accounts with no registered email address, and that they are still working out how many people had their personal information exposed.

Helpfeel said it has reviewed the exposed authentication data and taken "the necessary measures, including invalidation and restrictions." It did not say which items were invalidated.

Gyazo normally [emails a verification code](https://help.gyazo.com/Two-step%20login%20verification-5ed8969fc1eca80023e84383) when a login comes from a new IP address, a check that runs at login. Helpfeel has not said whether the exposed session IDs remain valid.

Every Gyazo capture gets a link built from a 32-character image ID. Gyazo's [help pages](https://help.gyazo.com/Is_Gyazo_safe%3F-5de75e1e040e1d0017df4359) say a capture stays private until its link is shared, that anyone who has the link can see it, and that the ID is long enough that a link "can't be guessed." For a capture at the default setting, the link is the only thing protecting it, and the leaked image IDs are the part of the link that makes it unguessable.

Free accounts can browse only their 10 most recent captures on Gyazo's site, but Gyazo says older captures are not deleted and [remain accessible](https://help.gyazo.com/Free_users_have_image_viewing_restrictions-619f1f90855387001d0792e9) to anyone with the URL.

The affected metadata records are mostly for images registered in January 2019 or earlier and make up about 14.4% of Helpfeel's image-related data, the company said.

Metadata for a further 2.4 million images was pulled separately using what Helpfeel called "specific filtering criteria." It has not said what the filter was, whether the two sets overlap, or whether the second set includes newer images.

Helpfeel listed these fields, plus other related information:

* Image ID, the information used to build the image URL
* IP address used for the upload
* User-Agent
* EXIF location data, if the image contained it
* OCR text extracted from the image
* Image title
* Source URL and other metadata
* Hashed passphrase for private images

Helpfeel said it temporarily disabled viewing of some images to prevent further harm, and that its investigation has not found any loss of image data. It has not said which images are disabled, or how a user can tell whether their captures are in the affected sets.

The attacker also obtained a list identifying private images, Helpfeel said, and the company said it "cannot rule out the possibility that the third party may have viewed some private images."

On Gyazo, a private capture can mean one set to ["Only me,"](https://help.gyazo.com/Set%20the%20privacy%20settings%20of%20the%20image-65f263d37b2cc7002425974d) which the help pages say cannot be viewed even by someone who knows the link, or one locked with a password. Both settings are available only on paid plans, and Helpfeel has not said which it means or how such images could have been viewed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

The OCR text field comes from a Gyazo feature that reads the text in a user's captures, allowing them to search it. Gyazo's [help pages](https://help.gyazo.com/OCR_scan-5de75e1e040e1d0017df4382) describe it as a paid feature that users enable themselves and that then scans all the account's images. The same pages say, "Only you can see OCR results."

Helpfeel said it noticed suspicious activity on the evening of September 11, Japan time. By the early hours of September 12, it had blocked the access routes it had identified, cut the attacker's connections, and fixed the vulnerability...