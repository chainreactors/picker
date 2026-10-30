---
title: AOCR.org Referrer Spam in Google Analytics and Server Logs
url: https://www.blackmoreops.com/aocr-org-referrer-spam-google-analytics/
source: blackMORE Ops
date: 2026-10-29
fetch_date: 2026-10-30T07:56:42.938215
---

# AOCR.org Referrer Spam in Google Analytics and Server Logs

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

* [Home](https://www.blackmoreops.com/)
* [Linux](https://www.blackmoreops.com/category/systems/linux/)
  + [Linux Administration](https://www.blackmoreops.com/category/tutorials/administration/)
  + [Command Line](https://www.blackmoreops.com/category/networking/cli/)
  + [Ubuntu](https://www.blackmoreops.com/category/systems/ubuntu-linux/)
  + [Windows](https://www.blackmoreops.com/category/systems/microsoft-windows/)
* [Security](https://www.blackmoreops.com/category/security/)
  + [Hacking](https://www.blackmoreops.com/category/security/hacking/)
  + [Wi-Fi](https://www.blackmoreops.com/category/networking/wireless-lan-wi-fi/)
  + [DoS Attacks](https://www.blackmoreops.com/category/security/denial-of-service/)
  + [VPN](https://www.blackmoreops.com/category/security/virtual-private-network-vpn/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
  + [Unraid](https://www.blackmoreops.com/category/systems/unraid/)
  + [Virtualization](https://www.blackmoreops.com/category/networking/virtualization/)
  + [WordPress](https://www.blackmoreops.com/category/systems/wordpress/)
  + [Networking](https://www.blackmoreops.com/category/networking/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

* [Home](https://www.blackmoreops.com/)
* [Linux](https://www.blackmoreops.com/category/systems/linux/)
  + [Linux Administration](https://www.blackmoreops.com/category/tutorials/administration/)
  + [Command Line](https://www.blackmoreops.com/category/networking/cli/)
  + [Ubuntu](https://www.blackmoreops.com/category/systems/ubuntu-linux/)
  + [Windows](https://www.blackmoreops.com/category/systems/microsoft-windows/)
* [Security](https://www.blackmoreops.com/category/security/)
  + [Hacking](https://www.blackmoreops.com/category/security/hacking/)
  + [Wi-Fi](https://www.blackmoreops.com/category/networking/wireless-lan-wi-fi/)
  + [DoS Attacks](https://www.blackmoreops.com/category/security/denial-of-service/)
  + [VPN](https://www.blackmoreops.com/category/security/virtual-private-network-vpn/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
  + [Unraid](https://www.blackmoreops.com/category/systems/unraid/)
  + [Virtualization](https://www.blackmoreops.com/category/networking/virtualization/)
  + [WordPress](https://www.blackmoreops.com/category/systems/wordpress/)
  + [Networking](https://www.blackmoreops.com/category/networking/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

Friday, October 30, 2026

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

Search

[![blackMORE Ops](https://www.blackmoreops.com/wp-content/uploads/2025/06/Logo_tinified_400x300_20121218_073230000_iOS.webp)](https://www.blackmoreops.com/)

Search

* [Linux](https://www.blackmoreops.com/category/systems/linux/)
* [Security](https://www.blackmoreops.com/category/security/)
* [Kali Linux](https://www.blackmoreops.com/category/systems/kali-linux/)
* [Homelab](https://www.blackmoreops.com/category/unraid/)
* [AI](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)
* [How-to](https://www.blackmoreops.com/category/tutorials/how-to/)

[Home](https://www.blackmoreops.com) > [How to](https://www.blackmoreops.com/category/tutorials/how-to/) > AOCR.org Referrer Spam in Google Analytics and Server Logs

[How to](https://www.blackmoreops.com/category/tutorials/how-to/)[Security](https://www.blackmoreops.com/category/security/)

# AOCR.org Referrer Spam in Google Analytics and Server Logs

## Fake AOCR.org Referral Traffic in Google Analytics and how to find it

1 day ago

*27*

If aocr.org has appeared in your Google Analytics referral report, you are not alone and you did not get a mention from a medical college. The American Osteopathic College of Radiology is a real organisation in Missouri with no reason to link to a Kali Linux guide. What you are seeing is referrer spam, a fake referral source written into an HTTP header by a script that has never read your site.

![AOCR.org referrer spam featured image showing aocr.org as the top referrer with 253 fake referrals from 10 IP addresses](data:image/svg+xml...)

One day of external referrers from the access log. aocr.org outnumbered every search engine combined.

On this site one day of logs produced 253 requests naming aocr.org as the referrer, spread across roughly a hundred different articles, from ten different IP addresses, all using the same browser string. Those numbers are what a spoofed referral campaign looks like from the inside, and they are also how you tell it apart from a genuine mention.

![Ubuntu terminal screenshot of grep and awk commands finding aocr.org referrer spam in an nginx access log, counting 253 requests from 10 IP addresses](data:image/svg+xml...)

Counting aocr.org referrer spam in the nginx access log on Ubuntu.

Table of Contents

* [What referrer spam looks like in Google Analytics](#penci-What_referrer_spam_looks_like_in_Google_Analytics "What referrer spam looks like in Google Analytics")
* [AOCR.org referrer spam at a glance](#penci-AOCRorg_referrer_spam_at_a_glance "AOCR.org referrer spam at a glance")
* [What the server logs showed](#penci-What_the_server_logs_showed "What the server logs showed")
* [Why a radiology college name](#penci-Why_a_radiology_college_name "Why a radiology college name")
* [Find AOCR.org referrer spam in nginx logs](#penci-Find_AOCRorg_referrer_spam_in_nginx_logs "Find AOCR.org referrer spam in nginx logs")
* [Find AOCR.org referrer spam in Apache logs](#penci-Find_AOCRorg_referrer_spam_in_Apache_logs "Find AOCR.org referrer spam in Apache logs")
* [Stop it polluting Google Analytics](#penci-Stop_it_polluting_Google_Analytics "Stop it polluting Google Analytics")
* [Is referrer spam a security problem](#penci-Is_referrer_spam_a_security_problem "Is referrer spam a security problem")
* [Does it cost server resources or slow WordPress](#penci-Does_it_cost_server_resources_or_slow_WordPress "Does it cost server resources or slow WordPress")
* [When to block referrer spam](#penci-When_to_block_referrer_spam "When to block referrer spam")
* [How to block referral spam without breaking your site](#penci-How_to_block_referral_spam_without_breaking_your_site "How to block referral spam without breaking your site")
* [Frequently asked questions](#penci-Frequently_asked_questions "Frequently asked questions")
  + [Does AOCR.org referrer spam indicate a compromise](#penci-Does_AOCRorg_referrer_spam_indicate_a_compromise "Does AOCR.org referrer spam indicate a compromise")
  + [Does referrer spam affect Google rankings](#penci-Does_referrer_spam_affect_Google_rankings "Does referrer spam affect Google rankings")
  + [Will blocking the IP addresses stop it](#penci-Will_blocking_the_IP_addresses_stop_it "Will blocking the IP addresses stop it")
  + [Why is a real company name used in the referrer](#penci-Why_is_a_real_company_name_used_in_the_referrer "Why is a real company name used in the referrer")
  + [Should I disavow the links](#penci-Should_I_disavow_the_links "Should I disavow the links")
  + [How do I see referral traffic in Google Analytics 4](#penci-How_do_I_see_referral_traffic_in_Google_Analytics_4 "How do I see referral traffic in Google Analytics 4")
* [Sources](#...