---
title: Google Blocks 8.3B Policy-Violating Ads in 2025, Launches Android 17 Privacy Overhaul
url: https://thehackernews.com/2026/04/google-blocks-83b-policy-violating-ads.html
source: The Hacker News
date: 2026-04-17
fetch_date: 2026-04-18T04:33:45.874979
---

# Google Blocks 8.3B Policy-Violating Ads in 2025, Launches Android 17 Privacy Overhaul

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Google Blocks 8.3B Policy-Violating Ads in 2025, Launches Android 17 Privacy Overhaul](https://thehackernews.com/2026/04/google-blocks-83b-policy-violating-ads.html)

**Ravie Lakshmanan**Apr 17, 2026Artificial Intelligence / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj84jgyS7JCiumwEWR-XKLRuLv_sljuCRx-alsYQHKikYlefpZeL1Wqh3GEALkiLdX886cZVY22LQA_ETSoYLrNdEJ4115IkJtXq5v1EMvQdvU-_xS61E89OwwSWXvE-F6Lw6_DH17w0wHHnBfUgqFxsy5cI1rTzinKIgA-X3q08jMLOOci5fkkUbCeIeId/s1700-e365/google-ads-android.jpg)

Google this week [announced](https://android-developers.googleblog.com/2026/04/giving-users-clearer-choice-and-everyone-a-safer-more-trusted-app-ecosystem.html) a new set of Play policy updates to strengthen user privacy and protect businesses against fraud, even as it revealed it blocked or removed over 8.3 billion ads globally and suspended 24.9 million accounts in 2025.

The new policy updates relate to contact and location permissions in Android, allowing third-party apps to access the contact lists and a user's location in a more privacy-friendly manner. This includes a new Contact Picker, which offers a standardized, secure, and searchable interface for contact selection.

"This feature allows users to grant apps access only to the specific contacts they choose, aligning with Android's commitment to data transparency and minimized permission footprints," Google [said](https://android-developers.googleblog.com/2026/03/contact-picker-privacy-first-contact.html).

Previously, apps requiring access to a specific user's contacts relied on READ\_CONTACTS, an overly broad permission that granted apps the ability to access all contacts and their associated information. With the latest change introduced in Android 17, apps can specify which fields from a contact they need, such as phone numbers or email addresses, as opposed to reading the entire record.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

The updated policy will require all applicable apps to use the picker (or the [Android Sharesheet](https://developer.android.com/training/sharing/send)) as the main way to access users' contacts, with READ\_CONTACTS now reserved only for apps that can't function without it. It's advised to entirely remove the READ\_CONTACTS permission from the app manifest declaration if it's targeting Android versions 17 (currently in beta) and later.

"If your app requires full, ongoing access to a user's contact list to function, you must justify this need by submitting a Play Developer Declaration in the Play Console," Google noted.

The second policy change revolves around a [streamlined location button](https://android-developers.googleblog.com/2026/03/location-privacy.html) that Google has introduced in Android 17 that enables apps to request one-time access to a user's precise location. In doing so, it allows the user to make a better choice about how much information they want to share and for what duration. What's more, a persistent indicator will appear to alert a user every time a non-system app accesses their location.

To comply with this update, developers are being urged to review their apps' location usage to ensure that they are requesting the minimum amount of location data necessary for them to function.

"If your app targets Android 17 and above and uses precise location for discrete, temporary actions, implement the location button by adding the onlyForLocationButton flag in your manifest," the tech giant said. "If your app requires persistent, precise location to function, you will need to submit a Play Developer Declaration in Play Console to show why the new button or coarse location isn't sufficient for your app's core features."

The declaration form is expected to be available before October 2026, with pre-review checks in the Play Console to go live starting October 27 to identify potential contacts or location permissions policy issues.

Google is also implementing a secure way for businesses to transfer ownership of their apps through a native account transfer feature built into Play Console so as to stay protected against fraud. The company is recommending that app developers handle account ownership changes through this feature starting May 27, 2026.

"That means that unofficial transfers (like sharing login credentials or buying and selling accounts on third-party marketplaces), which leave your business vulnerable, are not permitted," it said.

### Google Takes Aim at Malvertising

The changes to the Android ecosystem come as Google [said](https://blog.google/products/ads-commerce/2025-ads-safety-report/) it's harnessing the capabilities of Gemini, its artificial intelligence (AI) model, to detect and block malicious ads on its platform. More than 99% of policy-violating ads were caught by its systems in 2025 before they were shown to users, it noted.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"Unlike earlier keyword-based systems, our latest models better understand intent, helping us spot malicious content and preemptively block it, even when it's designed to evade detection," Keerat Sharma, vice president and general manager of Ads Privacy and Safety at Google, said in a post shared with The Hacker News.

Taken together, the company removed or blocked 602 million ads and 4 million accounts that were associated with scams or scam-related activity last year. More than 4.8 billion ads were restricted, and over 480 million web pages were actioned for attempting to serve sexually explicit content, weapons promotion, online gambling, alcohol, tobacco, and malware.

In contrast, Google [suspended](https://thehackernews.com/2025/04/google-blocked-51b-harmful-ads-and.html) over 39.2 million advertiser accounts in 2024, and stopped 5.1 billion bad ads, restricted 9.1 billion ads, and blocked or restricted ads on 1.3 billion pages.

"Bad actors are using generative AI to create deceptive ads at scale, and Gemini helps us detect and block them in real time," Google said. "By the end of last year, the majority of Responsive Search Ads created in Google Ads were reviewed instantly, and harmful content was blocked at submission -- a capability we plan to bring t...