---
title: Long-Running Web Skimming Campaign Steals Credit Cards From Online Checkout Pages
url: https://thehackernews.com/2026/01/long-running-web-skimming-campaign.html
source: The Hacker News
date: 2026-01-13
fetch_date: 2026-01-14T03:36:13.898401
---

# Long-Running Web Skimming Campaign Steals Credit Cards From Online Checkout Pages

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Long-Running Web Skimming Campaign Steals Credit Cards From Online Checkout Pages](https://thehackernews.com/2026/01/long-running-web-skimming-campaign.html)

**Jan 13, 2026**Ravie Lakshmanan Web Security / Data Theft

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVHFQIvHd3Xgz0zjrshHMJtilffEd0_azV_hpxK8GoTLQWDeGdaBZYKYitTQoFr5eqVFb3GFc4g0xz8wopdk3WBOsDKkP_7Nev4o91jQA7z1giTaO0aMVWRP4brxYXlyZ5qIxmyh7M3PkhIuL3yjQtXuMoAJm-HBgOgyV6-5ukzwQYT15woXwmFRxPoVXQ/s790-rw-e365/payment.png)

Cybersecurity researchers have discovered a major web skimming campaign that has been active since January 2022, targeting several major payment networks like American Express, Diners Club, Discover, JCB Co., Ltd., Mastercard, and UnionPay.

"Enterprise organizations that are clients of these payment providers are the most likely to be impacted," Silent Push [said](https://www.silentpush.com/blog/magecart/) in a report published today.

Digital skimming attacks refer to a category of client-side attacks in which bad actors compromise legitimate e-commerce sites and payment portals to inject malicious JavaScript code that's capable of stealthily harvesting credit card information and other personal information when unsuspecting users attempt to make a payment on checkout pages.

These attacks are classified under an umbrella term called [Magecart](https://thehackernews.com/2025/02/cybercriminals-exploit-onerror-event-in.html), which initially referred to a coalition of cybercriminal groups that targeted e-commerce sites using the Magento software, before diversifying to other products and platforms.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Silent Push said it discovered the campaign after analyzing a suspicious domain linked to a now-sanctioned bulletproof hosting provider Stark Industries (and its parent company PQ.Hosting), which has since [rebranded](https://thehackernews.com/2025/09/ukrainian-network-fdn3-launches-massive.html) to THE[.]Hosting, under the control of the Dutch entity WorkTitans B.V., is a sanctions evasion measure.

The domain in question, cdn-cookie[.]com, has been found to host highly obfuscated JavaScript payloads (e.g., "recorder.js" or "tab-gtm.js") that are loaded by web shops to facilitate credit card skimming.

The skimmer comes with features to evade detection by site administrators. Specifically, it checks the Document Object Model (DOM) tree for an element named "[wpadminbar](https://developer.wordpress.org/reference/classes/wp_admin_bar/)," a reference to a toolbar that appears in WordPress websites when logged-in administrators or users with appropriate permissions are viewing the site.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJgRKDO9vN2yNIr5fX3ngrOOqZLK95MqkKQ5skoigNgS3sGlL52833-HP8BBgUGdVivN1Uwj0MCqCCy6hiQk26epi8y3YopJBY0L6p6nbZo967j5WpGe28EQUBwQovtpH-sRVvLL0jJAZxDbCt_5L8dywmbQ6l1F0glPjmSAz7vdLbdGuRA6aTsNnV7oLM/s790-rw-e365/mazecart.jpg)

In the event the "wpadminbar" element is present, the skimmer initiates a self-destruct sequence and removes its own presence from the web page. An attempt to execute the skimmer is made every time the web page's DOM is modified, a standard behavior that occurs when users interact with the page.

That's not all. The skimmer also checks to see if Stripe was selected as a payment option, and if so, there exists an element called "wc\_cart\_hash" in the browser's [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), which it creates and sets to "true" to indicate that the victim has already been successfully skimmed.

The absence of this flag causes the skimmer to render a fake Stripe payment form that replaces the legitimate form through user interface manipulations, thereby tricking the victims into entering their credit card numbers, along with the expiration dates and Card Verification Code (CVC) numbers.

"As the victim entered their credit card details into a fake form instead of the real Stripe payment form, which was initially hidden by the skimmer when they initially filled it out, the payment page will display an error," Silent Push said. "This makes it appear as if the victim had simply entered their payment details incorrectly."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The data stolen by the skimmer extends beyond payment details to include names, phone numbers, email addresses, and shipping addresses. The information is eventually exfiltrated by means of an HTTP POST request to the server "lasorie[.]com."

Once the data transmission is complete, the skimmer erases traces of itself from the checkout page, removing the fake payment form that was created and restoring the legitimate Stripe input form. It then sets "wc\_cart\_hash" to "true" to prevent the skimmer from being run a second time on the same victim.

"This attacker has advanced knowledge of WordPress's inner workings and integrates even lesser-known features into their attack chain," Silent Push said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.co...