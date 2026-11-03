---
title: AI Crawlers Take Everything and Send Publishers Nothing
url: https://www.blackmoreops.com/ai-crawlers-publishers-traffic/
source: blackMORE Ops
date: 2026-11-02
fetch_date: 2026-11-03T08:52:00.210064
---

# AI Crawlers Take Everything and Send Publishers Nothing

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

Tuesday, November 3, 2026

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

[Home](https://www.blackmoreops.com) > [Artificial Intelligence](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/) > AI Crawlers Take Everything and Send Publishers Nothing

[Artificial Intelligence](https://www.blackmoreops.com/category/tutorials/artificial-intelligence/)[Security](https://www.blackmoreops.com/category/security/)

# AI Crawlers Take Everything and Send Publishers Nothing

## What AI Crawlers Cost Publishers In Traffic Bandwidth And Readers

16 hours ago

*12*

AI crawlers have turned the open web into a free buffet, and publishers are paying for the food. Over six days this month, named AI crawlers asked blackmoreops.com for 16,194 pages. On one night I went through the origin access log line by line, and the number of readers those AI tools sent back to this site was zero. Not low. Zero.

![Dark data hall aisle lit blue, with the headline AI Crawlers Take Everything across the top](https://www.blackmoreops.com/wp-content/uploads/2026/10/gpu-showcase-1-server-cathedral-labelled-2048x1152-1.webp)

Illustration of the data centre aisles those crawler requests land in.

This is not a think piece built on someone else’s survey. These are my logs, on my server, for a site that has published Linux and security guides for more than a decade. Every number below comes from the Cloudflare edge or the web server itself, and every one of them points the same way. The machines read everything, the people stop arriving, and the bill stays with the person who wrote the guide.

Table of Contents

* [What the logs actually show](#penci-What_the_logs_actually_show "What the logs actually show")
* [AI crawlers now outnumber the search engines that pay the bills](#penci-AI_crawlers_now_outnumber_the_search_engines_that_pay_the_bills "AI crawlers now outnumber the search engines that pay the bills")
* [Publishers pay for every page the bots read](#penci-Publishers_pay_for_every_page_the_bots_read "Publishers pay for every page the bots read")
* [Lost clicks are lost readers, and lost readers are lost publishers](#penci-Lost_clicks_are_lost_readers_and_lost_readers_are_lost_publishers "Lost clicks are lost readers, and lost readers are lost publishers")
* [AI answers replace experience with confident guesswork](#penci-AI_answers_replace_experience_with_confident_guesswork "AI answers replace experience with confident guesswork")
* [Why blocking AI crawlers only half works](#penci-Why_blocking_AI_crawlers_only_half_works "Why blocking AI crawlers only half works")
* [What publishers can do right now](#penci-What_publishers_can_do_right_now "What publishers can do right now")
* [The bill always lands on the writer](#penci-The_bill_always_lands_on_the_writer "The bill always lands on the writer")
* [Frequently asked questions](#penci-Frequently_asked_questions "Frequently asked questions")
  + [How much traffic do AI crawlers send back to websites?](#penci-How_much_traffic_do_AI_crawlers_send_back_to_websites "How much traffic do AI crawlers send back to websites?")
  + [Do AI crawlers cost publishers money?](#penci-Do_AI_crawlers_cost_publishers_money "Do AI crawlers cost publishers money?")
  + [Should I block AI crawlers on my website?](#penci-Should_I_block_AI_crawlers_on_my_website "Should I block AI crawlers on my website?")
  + [Does robots.txt stop AI crawlers?](#penci-Does_robotstxt_stop_AI_crawlers "Does robots.txt stop AI crawlers?")
  + [Are AI answers reliable for Linux and security commands?](#penci-Are_AI_answers_reliable_for_Linux_and_security_commands "Are AI answers reliable for Linux and security commands?")
* [Sources](#penci-Sources "Sources")

## What the logs actually show

Two sources, two different views of the same traffic. The Cloudflare edge sees every request before it reaches the server. The origin log sees only what gets through.

| Measure | Value | Source |
| --- | --- | --- |
| Page requests from named AI crawlers | 16,194 in 6.2 days | Cloudflare edge |
| Average per day | About 2,600 | Cloudflare edge |
| Googlebot and Bingbot combined, same period | 10,433 | Cloudflare edge |
| AI crawler ...