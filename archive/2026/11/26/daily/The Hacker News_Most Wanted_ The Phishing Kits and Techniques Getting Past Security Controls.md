---
title: Most Wanted: The Phishing Kits and Techniques Getting Past Security Controls
url: https://thehackernews.com/2026/11/most-wanted-phishing-kits-and.html
source: The Hacker News
date: 2026-11-26
fetch_date: 2026-11-27T10:17:34.650191
---

# Most Wanted: The Phishing Kits and Techniques Getting Past Security Controls

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Most Wanted: The Phishing Kits and Techniques Getting Past Security Controls](https://thehackernews.com/2026/11/most-wanted-phishing-kits-and.html)

**The Hacker News**Nov 26, 2026Identity Security / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOYXUiExbrrmBGGBgTjOFcDJSrLYJuITQwZY-l1mOzzkes21-mR0My9ikeCM7cI6VDXuBIE9BZPnKazemiuZf7A4w_xeeMy_IUUlNVTKX3PmW-Xt7FA9UI8JoICZDPW4ZWSspztPv_Mo4Zf7G_fXEw_phMe4uc89O38ugIlQJJKmc6VD7QN3NzU0n0SQU/s1700-nu-rw-lo-l85-e365/push-most.jpg)

Every phishing attack has to get past email security, web filtering, and safe browsing before it reaches an employee. Some kits manage that far more often than others, and those are the kits that security teams need to know about.

At Push Security, we measure this as **breakthrough rate**: The share of attacks that get past email security, web gateways, and safe browsing to reach the user.

## **How an attack breaks through**

Every browser-based attack starts with a lure, and each control in its path sees only part of the attack:

* **Email security:** Half of the attacks we see never touch email. The lure arrives through a search ad, a chat message, social media, a calendar invite, or a QR code. The rest come from trusted senders and services, so they pass reputation checks.
* **Web gateways:** The pages sit on trusted hosting and are assembled in the browser. The domains rotate every few days, so reputation data lags behind them.
* **Safe browsing and scanners:** Bot checks and cloaking show scanners a harmless page. A new domain isn't on any blocklist yet.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9CiS9QFJ_Qq7H-SYOIrtdKPjy_tDrr2p2cs6aZJc-8twBMJFdVySj7R7l74JJnJxy-z3rMj7jedYtBQP2NFE4_WitTxd-ehsLF4N3nMr20OHnHHEckCq2JA7vR5J8rlUkfbAjtAzl9mLqYDwFWxlJCVoS4g2baM9wQrc4cDORipKaNxJlyYJSE6UPuA4/s1700-nu-rw-lo-l85-e365/02-attack-path.png) |
| How a phishing attack gets past email, URL, DNS, web gateway, and scanner controls before it reaches the user in the browser. |

When the page loads in the user's browser and the user interacts with it, that's a breakthrough. Breakthrough rate counts those attacks, not attempts.

This changes how to read upstream data. A kit with a high breakthrough rate is one that upstream controls are missing. A low count in email or proxy logs doesn't prove that a kit is rare, because the kit may be getting past those controls without a trace.

Our upcoming webinar reveals the five kits with the highest breakthrough rates. Here's an early look at the number one kit.

> [Save your spot for the webinar](https://pushsecurity.com/webinar/most-wanted-phishing-kits?utm_campaign=58429501-Push%27s%20Most%20Wanted%20Webinar&utm_source=the-hacker-news&utm_medium=article)

## **DOMDIFFER: Google's real sign-in page, mirrored from the attacker's browser**

From August to October 2026, one kit ranked first by breakthrough rate every month. DOMDIFFER, an AiTM phishing kit that targets corporate Google and Microsoft accounts, broke through 2-4x as often as the next kit each month. DOM mirroring, the mechanism it uses under the hood, also happens to be the newest and fastest-growing way for a kit to relay a sign-in.

We first saw DOMDIFFER in February 2026. DOMDIFFER is our name for the kit (it hasn't yet been linked to a known phishing-as-a-service brand). We believe it grew out of NakedPages, a reverse proxy kit, and the two kits share infrastructure in several places. DOMDIFFER went quiet in the spring, came back over the summer, and has held the top rating since August. Most of its detections in that time came from fake calendar event lures.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcypfeuzdR_4LJYhi5nWdfcY0P1HGE3arG1oEWB6NPnRjNTOVrHSpku4JQ0lB9FhfeK70nTXbwQBqmWa3pntMc0KJxd_r63S_6I2_3TRlA3VL822m4RhJJ0W_T68LWtfS1dFihZzr3mZaFLcKSCtE6T-57MJpsj6D68p6OERCTJBuIbt35zJKfW0kIZgg/s1700-nu-rw-lo-l85-e365/03-domdiffer-hostnames.jpg) |
| New hostnames per month for three NakedPages variants and DOMDIFFER, from our threat intelligence. |

One real DOMDIFFER attack starts with a fake Google Voice notification about a new voicemail.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4glY6EMhlxnJWwuORo8zHju6mRnjvB9xNfdIbxvM3DTTiVIzhxsGmRRSP4kT6kKIPlgtysl0JTOTRjpikJBVsYMIPL4xGokST-FMGqbKZ5QWTilqqT3-iamQIzICG6jNjtJetugODW9eDJdAuthrHAW7fVQ9jC6UZ0W7ZM3QEsK-MIhrvYucbtfxbC48/s1700-nu-rw-lo-l85-e365/04-domdiffer-voicemail-lure.png) |
| The lure for one DOMDIFFER attack: A fake Google Voice voicemail notification. |

The link passes a bot check that turns scanners away. The victim then sees what looks exactly like Google's sign-in page. It isn't a screenshot or a static copy. It's Google's real page, mirrored from the attacker's browser.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPXc7QeljZAD9Na2SgvtuCF26wNl0zguG6ULC-guN1wCc00cO7N-iuGLR9rkUhEtqGuTnSsISbYoR7YUgc0TDuE1L90RDaM7LvL8vQVGpvYGZqJpq1RiVShYhXliIK9EjUKsbgftbHy6QKjWcdm-G4HGxIQdE3F3mlrFyHwhzIXERt2aY3U0dL7OLuq9I/s1700-nu-rw-lo-l85-e365/05-domdiffer-mirrored-signin.png) |
| Google's sign-in page, mirrored from the attacker's browser by DOMDIFFER. |

On the surface, this looks like fairly standard phishing: A notification lure, a bot check gate, then a sign-in page. What makes DOMDIFFER particularly effective lies beneath the surface.

### **TL;DR: DOM mirroring**

AiTM kits relay a sign-in in one of four ways: Reverse proxy, replica page, pixel streaming, and DOM mirroring. In DOM mirroring, the attacker's own browser does the real sign-in. It sends the page's structure (the DOM) to the victim's browser, which rebuilds a working copy. Because a real browser does the sign-in, the kit sends Google genuine browser signals and handles new sign-in steps without needing extra code.

Replica pa...