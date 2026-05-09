---
title: One Missed Threat Per Week: What 25M Alerts Reveal About Low-Severity Risk
url: https://thehackernews.com/2026/05/one-missed-threat-per-week-what-25m.html
source: The Hacker News
date: 2026-05-08
fetch_date: 2026-05-09T05:09:02.619627
---

# One Missed Threat Per Week: What 25M Alerts Reveal About Low-Severity Risk

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [One Missed Threat Per Week: What 25M Alerts Reveal About Low-Severity Risk](https://thehackernews.com/2026/05/one-missed-threat-per-week-what-25m.html)

**The Hacker News**May 08, 2026Threat Detection / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUaPw5V89Ez9z5x8eFLFOhwPphGqXDQVGfd2sI-pX9Q1XTcpYlWEhFiZ6o12fzAyvtCFDQ0zs4AFlHl4HJNnjWH8hUXM9r_-oBl7YMEnU1F41Ho7DL23NJbgG4M3eoqF6CTZWqFtFcw0gOB8QfkCPW1_xQ-HwmvWr3GMzEeRFbC8SLgG5LsdnopTAHDOs/s1700-e365/ai-soc.jpg)

The dark secret of enterprise security operations is that defenders have quietly institutionalized the practice of not looking. This is not just anecdotal, but rather backed by a recent report investigating more than 25 million security alerts, including informational and low-severity, across live enterprise environments.

The dataset behind these findings includes 10 million monitored endpoints and identities, 82,000 forensic endpoint investigations including live memory scans, 180 million files analyzed, and telemetry from 7 million IP addresses, 3 million domains and URLs, and over 550,000 phishing emails.

The patterns that emerge from this data tell a consistent story. Threat actors are exploiting the predictable gaps created by constrained, severity-based security operations, and they are doing it systematically. Understanding where those gaps actually live requires looking at the full alert picture, starting with the category most teams have been conditioned to ignore.

## The 1% problem that adds up to one missed breach per week

In this analysis of 25M alerts, nearly 1% of confirmed incidents originated from alerts initially classified as low-severity or informational. On endpoints specifically, that figure climbed to nearly 2%.

At enterprise scale, percentages like these are not noise. The average organization generates approximately 450,000 alerts per year. One percent of that is roughly 54 real threats annually, about one per week, that never get investigated under a traditional SOC or MDR model. Detection did not fail. Triage economics just made investigation impossible.

These are not theoretical risks sitting at the edge of an attacker's wishlist. They are real compromises hiding in the category of alerts that operations teams have been trained to deprioritize.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIRWqvCXOoDG8bVGvt2ZAgHTDwhMjlcHRi99RdRPCtChRaB93eqkiE1hlVDdFbPxd_0txPdQuteTkzwH2FEsUABHHZpN3HxCxQ4dl5p3wRDjEesmLK2-esQDs28zgiOGfLLrBe1M2Y_FJ9q7d1L4VGyb5mW0nqxmYjNQ4IJ4cXpQaq5VjWyDuRVixBcjI/s1700-e365/info.png)

## EDR "mitigated" does not mean clean

Endpoint findings from the report deserve special attention because they challenge a foundational assumption in most security programs: that EDR remediation can be trusted at face value.

Of the 82,000 alerts that underwent live forensic memory scans, 2,600 had active infections. Of those confirmed compromised endpoints, 51% had already been marked as "mitigated" by the source EDR vendor.

In over half of confirmed endpoint compromises detected through forensic analysis, the EDR had closed the ticket and declared the threat resolved. Without memory-level forensics, those infections remain invisible. The tools most organizations rely on as their endpoint safety net are reporting clean on machines that are not clean.

The malware families found running in memory during these scans include Mimikatz, Cobalt Strike, Meterpreter, and StrelaStealer, not obscure proof-of-concept tools, but the workhorses of active criminal and nation-state operations.

## Phishing has left your email gateway behind

The phishing data in the report reflects a fundamental shift in attacker methodology that most email security architectures are not designed to catch.

Less than 6% of confirmed malicious phishing emails contained attachments. Most relied on links and language. More significantly, attackers have migrated their infrastructure onto platforms that are trusted by default: Vercel, CodePen, OneDrive, and even PayPal's own invoicing system.

One campaign documented in the report uses PayPal's legitimate payment request infrastructure to send threat emails, with callback numbers embedded in the payment notes and Unicode homoglyphs to defeat signature-based detection. The sending domain passes every standard authentication check because the mail genuinely originates from PayPal.

Cloudflare Turnstile CAPTCHA has become a reliable signal of malicious intent: sites using it were consistently more likely to be phishing pages, while Google reCAPTCHA correlated with legitimate infrastructure. Attackers are using the mechanisms built to stop bots to stop automated security scanners instead.

Four new techniques for bypassing email gateways were identified in the data: Base64 payloads hidden inside SVG image files, links embedded in PDF annotation metadata invisible to surface-level scanners, dynamically loaded phishing pages served through legitimate OneDrive shares, and DOCX files concealing archived HTML content containing QR codes. None of these is exotic. They are operational techniques being used at scale.

## Cloud telemetry shows attackers playing long games

Cloud alert data from the report shows a pronounced concentration around defense evasion and persistence tactics, with relatively few high-impact behaviors like lateral movement or privilege escalation appearing in the signal.

Attackers are being both cautious and patient. The dominant pattern is long-term access. Token manipulation, abuse of legitimate cloud features, andobfuscation to avoid triggering higher-severity detections. The goal is to remain present and undetected, not to make noise.

AWS misconfigurations compound this risk quietly. S3 accounts for roughly 70% of all cloud control violations in the dataset, with the most common issues centered on access management, server logging, and cross-account restrictions. These findings rarely tri...