---
title: How to Fix the ERR_TOO_MANY_REDIRECTS Error
url: https://blog.sucuri.net/2025/11/how-to-fix-the-err_too_many_redirects-error.html
source: Sucuri Blog
date: 2025-11-13
fetch_date: 2025-11-14T03:12:25.924892
---

# How to Fix the ERR_TOO_MANY_REDIRECTS Error

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

* [Security Education](https://blog.sucuri.net/category/security-education)
* [Website Security](https://blog.sucuri.net/category/website-security)

# How to Fix the ERR\_TOO\_MANY\_REDIRECTS Error

[![](https://blog.sucuri.net/wp-content/uploads/2025/04/avatar_user_115_1745352070-60x60.jpg)](https://blog.sucuri.net/author/msinghtoor)

[Maninder Toor](https://blog.sucuri.net/author/msinghtoor)

* November 13, 2025

![How to fix the ERR_TOO_MANY_REDIRECTS Error](https://blog.sucuri.net/wp-content/uploads/2025/11/How-to-fix-the-ERR_TOO_MANY_REDIRECTS-Error-820x385.png)

Encountering the `ERR_TOO_MANY_REDIRECTS` error (also called a redirect loop error) can be frustrating, especially when your website was working fine just moments ago. This issue is common across browsers such as Chrome, Firefox, and Edge and it typically means your site has entered a redirection loop.

In this post, you’ll learn what the error means, why it occurs, ways to identify where the redirect is coming from, and how to fix it effectively – including an important section on redirect types, which often play a direct role in causing this issue.

## What is the “ERR\_TOO\_MANY\_REDIRECTS” error?

The redirect loop error occurs when a browser tries to load a page but gets caught in an endless cycle of redirects. Instead of reaching the website, your browser keeps bouncing between different URLs until it stops trying. Essentially, the site tells the browser to go to another location repeatedly, causing an infinite loop. For Example:

1. Your browser opens<http://yourdomain.com>
2. It’s redirected to<https://yourdomain.com>
3. Then redirected back to<http://yourdomain.com>
4. Loop continues…

## Error messages vary by browser:

* **Google Chrome:** This page isn’t working. example.com redirected you too many times. `ERR_TOO_MANY_REDIRECTS`
* **Firefox:** The page isn’t redirecting properly
* **Safari:** Too many redirects occurred trying to open the page
* **Edge:** This page isn’t working right now – redirected you too many times

## Different types of redirects

Here are the most common redirect types used on websites:

### 301 Redirect (Permanent):

Indicates a page has been permanently moved to a new URL. For example, if you’ve changed your website’s address or renamed a page. This type is commonly used when moving a site from http:// to https:// or from a non-www to a www version.  This tells browsers and search engines to always go to the new page and most of the SEO value from the old page is passed along.

### 302 Redirect (Temporary):

This type of redirect is used when you want to send visitors to a different page for a short time. For example, while your main page is under maintenance or you’re testing a new version of it. It tells browsers and search engines that the move isn’t permanent, so your original page stays listed in search results and keeps its ranking.

### 307 Redirect (Temporary / HSTS Redirect)

A modern version of the 302 redirect. It’s also a temporary redirect but ensures the type of request (like GET or POST) stays the same. This is important when someone is submitting a form or performing an action that shouldn’t change during the redirect.

Browsers also use an internal 307 redirect when HSTS (HTTP Strict Transport Security) is enabled. Once a browser has seen the HSTS header, it automatically upgrades all http:// requests to https:// before reaching the server, ensuring a secure connection.

### 308 Redirect (Permanent)

Similar to 301 redirect, this is for permanent moves. The difference is it also keeps the request type the same, which is useful for websites or APIs that need forms or data to be sent the same way after the move.

### Client-Side Redirects

Client-side redirects are implemented using HTML or JavaScript, such as Meta Refresh tags or JavaScript **window.location** scripts. Unlike server-side redirects, they occur in the user’s browser after the page loads.

### DNS Redirects and Domain Aliases

A DNS redirect sends a domain’s traffic to another server by changing DNS records like A or CNAME. Unlike HTTP redirects that occur after a browser connects to a web server, DNS redirects happen earlier when the domain is resolved to an IP address or alias.

A domain alias is different. It doesn’t redirect but lets multiple domain names show the same website. For example, **example.net** showing the same content as **example.com**. This is often used when a business wants several domains to open the same site.

There is some controversy around how domain aliases should be handled. While some setups rely solely on aliases to serve the same content under different domains, the simplest and most effective approach is to set up a 301 redirect from all extra domain...