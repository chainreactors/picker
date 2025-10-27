---
title: Japanese Spam on a Cleaned WordPress Site: The Hidden Sitemap Problem
url: https://blog.sucuri.net/2025/01/japanese-spam-on-a-cleaned-wordpress-site-the-hidden-sitemap-problem.html
source: Over Security - Cybersecurity news aggregator
date: 2025-01-17
fetch_date: 2025-10-06T20:13:20.901367
---

# Japanese Spam on a Cleaned WordPress Site: The Hidden Sitemap Problem

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Security Education](https://blog.sucuri.net/category/security-education)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Japanese Spam on a Cleaned WordPress Site: The Hidden Sitemap Problem

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* January 15, 2025

![Japanese spam on a cleaned WordPress site](https://blog.sucuri.net/wp-content/uploads/2025/01/japanese-spam-on-a-cleaned-wordpress-site-820x386.jpg)

While investigating a compromised WordPress site, we discovered a malware infection causing Japanese spam links to appear in Google search results. Although the site had been cleaned, Google was still crawling and indexing spammy URLs, which impacted the site’s SEO and credibility.

### Japanese SEO Spam: A Common Threat

Japanese SEO spam is a recurring issue that compromises websites to display spammy content in search engine results. Attackers often inject malicious URLs or sitemaps into a site’s infrastructure to manipulate its search rankings. We’ve covered similar cases in the past, including [How to Find and Fix Japanese SEO Spam](https://blog.sucuri.net/2023/09/how-to-find-fix-japanese-seo-spam.html), which outlines the broader impact of such attacks.

![Japanese SEO spam](https://blog.sucuri.net/wp-content/uploads/2025/01/japanese-seo-spam.png)

### The Problem: Japanese Spam URLs Persisting

The site owner initially reported an influx of spam links showing in Google search results, even though the site displayed no visible spam content. The Google Search Console (GSC) was reporting an increasing number of spam URLs in the format:

```
domainname/?m=XXXXXXXXX
```

These URLs were indexed as Japanese spam results, misleading users and harming the site’s reputation. Here, **XXXXXXXXX** is a random string of numbers used to generate unique spam URLs. Attempts to access these spam URLs returned 404 errors, they were still being crawled and indexed by Google, creating an SEO issue for the site owner.

### Discovery and Investigation

Since the site continued indexing spam URLs, even after cleaning Google Search Console, this indicated that either there is something cached or the malicious URLs still exist somewhere. During our investigation, we discovered a file named **spamurl.txt** in the root directory. This file was configured as a sitemap in GSC, prompting Google to crawl over 3,000 spam URLs. The number of indexed spam URLs continued to rise in GSC, signaling that the sitemap was actively enabling the spam campaign.

![crawled spam URLs](https://blog.sucuri.net/wp-content/uploads/2025/01/crawled-spam-urls.png)

The content in the **spamurl.txt** file looked like this:

![spamurl file contents](https://blog.sucuri.net/wp-content/uploads/2025/01/spamurl-file-contents.png)

### Mitigating the Spam

**Removing the Spam File:** We identified and deleted the spamurl.txt file from the site’s root directory. This immediately stopped Google from crawling the malicious URLs listed in the file.

**Updating Sitemap Settings:** The file was also [removed from the GSC sitemap configuration](https://support.google.com/webmasters/thread/14726089/how-to-delete-xml-sitemap-from-google-search-console?hl=en) to ensure it no longer influenced Google’s crawling behavior.

**Reindexing the Site:** Using the URL Inspection Tool in GSC, we submitted the site for reindexing. This helped clear the spam URLs from Google’s search index and restored the site’s SEO standing.

![remove sitemap](https://blog.sucuri.net/wp-content/uploads/2025/01/remove-sitemap.png)

### Why Did This Happen? And Key Takeaways

* Compromised Sitemap Management: Attackers leveraged the sitemap submission settings in GSC to inject the malicious spamurl.txt file and have Google crawl spam URLs.
* Persistent Spam URLs: Even after the visible spam was removed, the sitemap ensured spam links remained indexed.
* Regularly audit your sitemap files and GSC settings to identify any unauthorized additions.
* Removing malicious files is not enough; you must update GSC settings and request reindexing to clear indexed spam results.

Even after cleaning a site, Japanese spam can persist if malicious artifacts like unauthorized sitemaps are overlooked. This case highlights how attackers can persistently affect a site’s SEO and reputation even after visible spam is removed.

By exploiting sitemaps and the Google Search Console, they manipulated the site’s indexed content, causing long-term damage.

If you suspect similar activ...