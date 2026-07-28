---
title: Unauthenticated Disclosure of A/B Test Data in Convert Pro — How Two Forgotten AJAX Endpoints…
url: https://infosecwriteups.com/unauthenticated-disclosure-of-a-b-test-data-in-convert-pro-how-two-forgotten-ajax-endpoints-dbefc9c3e440?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-27
fetch_date: 2026-07-28T04:58:44.627294
---

# Unauthenticated Disclosure of A/B Test Data in Convert Pro — How Two Forgotten AJAX Endpoints…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthenticated-disclosure-of-a-b-test-data-in-convert-pro-how-two-forgotten-ajax-endpoints-dbefc9c3e440&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthenticated-disclosure-of-a-b-test-data-in-convert-pro-how-two-forgotten-ajax-endpoints-dbefc9c3e440&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dbefc9c3e440---------------------------------------)

·

1. [Background: Why This Plugin](/?source=post_page-----dbefc9c3e440---------------------------------------#2197 "Background: Why This Plugin")
2. [Understanding the Architecture](/?source=post_page-----dbefc9c3e440---------------------------------------#75f3 "Understanding the Architecture")
3. [The Vulnerability: Two Endpoints, Zero Gates](/?source=post_page-----dbefc9c3e440---------------------------------------#1244 "The Vulnerability: Two Endpoints, Zero Gates")
4. [Live Proof of Concept](/?source=post_page-----dbefc9c3e440---------------------------------------#3b1f "Live Proof of Concept")
5. [Impact Assessment](/?source=post_page-----dbefc9c3e440---------------------------------------#0603 "Impact Assessment")
6. [Disclosure Timeline](/?source=post_page-----dbefc9c3e440---------------------------------------#d2d5 "Disclosure Timeline")
7. [What This Teaches](/?source=post_page-----dbefc9c3e440---------------------------------------#ea75 "What This Teaches")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dbefc9c3e440---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

# Unauthenticated Disclosure of A/B Test Data in Convert Pro — How Two Forgotten AJAX Endpoints Leaked Every Split-Test on a Site

## **Author:** [Shikhali Jamalzade](https://medium.com/u/20557ba7487d?source=post_page---user_mention--dbefc9c3e440---------------------------------------) **GitHub:** [alisalive](https://github.com/alisalive) **LinkedIn:** [camalzads](http://linkedin.com/in/camalzads)

[![Shikhali Jamalzade](https://miro.medium.com/v2/resize:fill:64:64/1*1y98p7kVR06Fq8997mI2FQ.png)](https://alisalive.medium.com/?source=post_page---byline--dbefc9c3e440---------------------------------------)

[Shikhali Jamalzade](https://alisalive.medium.com/?source=post_page---byline--dbefc9c3e440---------------------------------------)

9 min read

·

1 day ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Ddbefc9c3e440&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthenticated-disclosure-of-a-b-test-data-in-convert-pro-how-two-forgotten-ajax-endpoints-dbefc9c3e440&source=---header_actions--dbefc9c3e440---------------------post_audio_button------------------)

Share

This is a write-up of a vulnerability I independently discovered in **Convert Pro** (WordPress.org slug: `convertpro`), an A/B testing and conversion-optimization plugin, in version 1.0.1. The bug allowed anyone on the internet, with no account and no authentication of any kind, to pull the full analytics of every A/B test a site was running or had ever run — test names, variation names, and complete view/conversion statistics — simply by requesting a URL with a sequential integer in it.

I discovered this independently and reported it to WPScan the same day. WPScan came back with a duplicate: another researcher had already reported the same root cause, and it was already in their review queue. I’m publishing this write-up anyway, because the pattern behind the bug is one I think is worth understanding on its own, separate from who ends up with the CVE credit for it.

## Background: Why This Plugin

My research methodology follows a fixed pipeline for every plugin I audit: export the trunk from the WordPress.org SVN repository, grep for every hook WordPress provides for exposing functionality externally (`wp_ajax_`, `wp_ajax_nopriv_`, `register_rest_route`, `add_menu_page`), and manually trace each candidate against a strict checklist before touching a live environment. I don't spin up a Docker proof-of-concept until static analysis has already found something real — testing dead ends wastes the one resource that actually matters in this kind of work: attention.

Convert Pro came up in a batch of A/B-testing and conversion-optimization plugins I was working through. This category is worth paying attention to because it sits at an odd intersection: these plugins store genuinely business-sensitive configuration — pricing experiments, discount strategy, campaign names — but are frequently built by small teams who treat their internal AJAX layer as “just for our own dashboard,” rather than as a public attack surface that anyone can reach directly.

Convert Pro registers a long list of AJAX actions in a single file, `includes/function.php` — creating tests, saving settings, running comparisons, fetching chart data for the admin dashboard. Most of them followed a consistent, correct pattern: `check_ajax_referer()` for CSRF protection. That consistency is exactly what made the two exceptions stand out immediately.

## Understanding the Architecture

The plugin’s primary settings-save handler looked exactly like what you’d want to see in a well-built plugin:

```
add_action('wp_ajax_convertpro_ajax_action', 'convertpro_ajax_request');
add_action('wp_ajax_nopriv_convertpro_ajax_action', 'convertpro_ajax_request');
function convertpro_ajax_request() {
    check_ajax_referer('convertpro_nonce', 'security');
    // ...
}
```

Nonce-gated, exactly as it should be — this handler runs on the frontend to record which variation a visitor saw, so it does need to be public, but at least it enforces a CSRF token before acting.

Further down the same file, two other actions were registered with the identical `wp_ajax_nopriv_` pattern, but their purpose was completely different:

```
add_action('wp_ajax_convertpro_interactions_report_ajax', 'convertpro_interactions_report_ajax');
add_action('wp_ajax_nopriv_convertpro_interactions_report_ajax', 'convertpro_interactions_report_ajax');
```

```
add_action('wp_ajax_convertpro_get_chart_data', 'convertpro_get_chart_data');
add_action('wp_ajax_nopriv_convertpro_get_chart_data', 'convertpro_get_chart_data');
```

These aren’t visitor-tracking endpoints — they’re **reporting** endpoints. They read back the data the tracking endpoints write. And they were registered exactly as public as the tracking side, with no distinction between “anyone can tell us they saw a page” and “anyone can rea...