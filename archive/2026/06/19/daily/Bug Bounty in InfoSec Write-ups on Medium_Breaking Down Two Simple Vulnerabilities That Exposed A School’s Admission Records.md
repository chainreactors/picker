---
title: Breaking Down Two Simple Vulnerabilities That Exposed A School’s Admission Records
url: https://infosecwriteups.com/breaking-down-two-simple-vulnerabilities-that-exposed-a-schools-admission-records-040bd636a7f3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-19
fetch_date: 2026-06-20T06:13:29.820248
---

# Breaking Down Two Simple Vulnerabilities That Exposed A School’s Admission Records

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbreaking-down-two-simple-vulnerabilities-that-exposed-a-schools-admission-records-040bd636a7f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbreaking-down-two-simple-vulnerabilities-that-exposed-a-schools-admission-records-040bd636a7f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-040bd636a7f3---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-040bd636a7f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Breaking Down Two Simple Vulnerabilities That Exposed A School’s Admission Records

[![Avyukt Security](https://miro.medium.com/v2/resize:fill:64:64/1*5jGxXKsgQjjFNintRNHdwg.jpeg)](https://medium.com/%40avyuktsec?source=post_page---byline--040bd636a7f3---------------------------------------)

[Avyukt Security](https://medium.com/%40avyuktsec?source=post_page---byline--040bd636a7f3---------------------------------------)

3 min read

·

1 day ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D040bd636a7f3&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbreaking-down-two-simple-vulnerabilities-that-exposed-a-schools-admission-records-040bd636a7f3&source=---header_actions--040bd636a7f3---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

By: Kavin Jindal ([@Klevr](https://www.linkedin.com/in/kavin-jindal))

Recently, while conducting reconnaissance on a school website, our team of security researchers at Avyukt Security found data-exposure vulnerabilities that revealed sensitive admission records containing PII (Personally Identifiable Information) such as names, emails, phone numbers, addresses, profession-related info, etc. The `/print-form.php?app_number=` endpoint was vulnerable to IDOR (Insecure Direct Object Reference), where upon entering the application number, admission records were exposed without any authorization checks. The same parameter was also vulnerable to SQL Injection and allowed dumping the whole database of records via automated tools.

Additionally, minor low-severity security flaws such as Reflected and Stored XSS, and exposure of XML-RPC and WP-Cron were also discovered.

**Note: All the discovered vulnerabilities were responsibly disclosed to the concerned institution via appropriate channels to ensure they could be remediated. No sensitive data was accessed, and no service disruption occurred during the security testing.**

## Get Avyukt Security’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

The following is a detailed breakdown of the reported findings on the website.

## -0x01: Discovery of IDOR on the Admission Registration Form

* The school website was built using WordPress and hosted a submission form for Kindergarten admissions on the `/online_form_2025` endpoint.
* After filling the form and completing the submission, the user was redirected to the `/online_form_2025/thank-you.php?app_number=[application_id]` page which showed the following.

Press enter or click to view image in full size

![]()

* The application ID fetched from the `app_number` GET parameter was being reflected on the webpage as shown.
* The parameter could be easily manipulated, and upon clicking the “Print Registration” button, the user was redirected to the `/online_form_2025/print-form.php?app_number=` endpoint where the registration form of the manipulated ID could be printed.
* The `/print-form.php` endpoint exposed over 46 columns of data per registration form as the `app_number` GET parameter was vulnerable to IDOR.
* The webpage exposed critical PII because no authorization checks were implemented to verify that the user was authorized to view the requested registration form data.

Press enter or click to view image in full size

![]()

## -0x02: Discovery of SQL Injection on the Admission Registration Form

* We tested the GET parameter `app_number` in `/online_form_2025/print-form.php?app_number=` endpoint for SQL Injection via SQLMap.
* The scan revealed that the parameter was vulnerable to UNION-based SQL Injection.
* We tested the parameter further and were successful in dumping the `[school_name]_kg_admission` database that stored all the 46 columns of every registration record in the`tbl_kg_adm_data`and `tbl_kg_secondary_data`tables.

Press enter or click to view image in full size

![]()

SQLMap output while testing ‘app\_number’ parameter to test for SQLi

**Note: All the reported vulnerabilities were responsibly disclosed to the concerned institution via appropriate channels to ensure that they are remediated. No sensitive data was accessed, and no service disruption was caused during the security testing.**

I hope you found this article worth your time. Make sure to follow Avyukt Security for more cybersecurity research and findings!

Bug Hunting

Cybersecurity

Ethical Hacking

Bug Bounty

Bug Bounty Writeup

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--040bd636a7f3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--040bd636a7f3---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--040bd636a7f3---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--040bd636a7f3---------------------------------------)

·[Last published 1 day ago](/bitsctf-2026-writeups-osint-and-steganography-forensics-challenges-b91257ca0856?source=post_page---post_publication_info--040bd636a7f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Avyukt Security](https://miro.medium.com/v2/resize:fill:96:96/1*5jGxXKsgQjjFNintRNHdwg.jpeg)](https://medium.com/%40avyuktsec?source=post_page---post_author_info--040bd636a7f3---------------...