---
title: Sucuri WAF Now Supports HTTP/3: A Faster and More Secure Web Experience
url: https://blog.sucuri.net/2025/01/sucuri-waf-now-supports-http-3-a-faster-and-more-secure-web-experience.html
source: Sucuri Blog
date: 2025-01-29
fetch_date: 2025-10-06T20:06:23.097657
---

# Sucuri WAF Now Supports HTTP/3: A Faster and More Secure Web Experience

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

* [Sucuri Updates](https://blog.sucuri.net/category/sucuri-updates)
* [Website Security](https://blog.sucuri.net/category/website-security)

# Sucuri WAF Now Supports HTTP/3: A Faster and More Secure Web Experience

[![](https://secure.gravatar.com/avatar/28c9f086a2ef4d4beae4637238919c78849f979bae5f3b369c9083b1ed0bffc7?s=60&d=mm&r=g)](https://blog.sucuri.net/author/klknight)

[Kyle Knight](https://blog.sucuri.net/author/klknight)

* January 28, 2025

![Sucuri WAF HTTP/3](https://blog.sucuri.net/wp-content/uploads/2025/01/WAF-HTTP3-820x385.png)

We’re excited to announce that the Sucuri [Web Application Firewall (WAF)](https://sucuri.net/website-firewall/) now supports HTTP/3, the latest version of the HTTP protocol. This upgrade brings significant performance improvements and enhanced security features to all websites protected by our WAF. The best part? It works automatically – if your visitor’s browser supports HTTP/3, they’ll immediately benefit from these improvements.

## What is HTTP/3?

HTTP/3 represents the next evolution in web communication protocols, building upon the foundations laid by HTTP/2 while addressing its key limitations. The most significant change is the switch from TCP to QUIC, a new transport protocol built on UDP. This fundamental change brings several important benefits to your website’s performance and security.

## Key Improvements Over HTTP/2

### Faster Connection Establishment

HTTP/3 combines the cryptographic and transport handshakes into a single step, significantly reducing the time needed to establish a connection. While HTTP/2 requires multiple round trips between the client and server to set up a connection, HTTP/3 can often establish secure connections in just one round trip, and even zero rounds for returning visitors.

### Better Performance Under Real-World Conditions

One of HTTP/2’s main limitations was head-of-line blocking, where a lost packet could temporarily block all other data streams. HTTP/3 eliminates this issue by implementing independent streams, ensuring that a problem with one stream doesn’t affect others. This means your website visitors will experience:

* More consistent loading times, especially on mobile networks
* Better performance when network conditions are less than ideal
* Smoother transitions when switching between networks (e.g., from WiFi to cellular)

### Enhanced Security by Default

HTTP/3 integrates TLS 1.3 by default, providing the latest security standards for all connections. This ensures that all data transferred between your visitors and your website is protected by state-of-the-art encryption.

## What This Means for Your Website

With Sucuri WAF HTTP/3 support, your website will automatically serve content using the most efficient protocol available to each visitor. Here’s what you can expect:

* Faster page loads, especially for visitors on high-latency or unreliable networks
* Improved mobile user experience with better handling of network changes
* Enhanced security through mandatory encryption
* No configuration needed – it just works

## Browser Compatibility

HTTP/3 support is already available in major browsers including Chrome, Firefox, and Edge. While Safari currently treats HTTP/3 as an experimental feature, support continues to grow across all platforms. You can use tools like [Domsignal](https://domsignal.com/http3-test) to confirm HTTP/3 is enabled on your site. Visitors using browsers that don’t support HTTP/3 will automatically fall back to HTTP/2 or HTTP/1.1, ensuring a seamless experience for everyone.

## Looking Forward

The addition of HTTP/3 support to our WAF represents our ongoing commitment to providing cutting-edge performance and security features to our customers. As web protocols continue to evolve, you can count on Sucuri to stay ahead of the curve, ensuring your website remains fast, secure, and accessible to all visitors.

No action is required on your part to enable HTTP/3 – it’s automatically available to all Sucuri WAF customers. Your visitors will immediately begin experiencing these performance improvements if their browsers support the protocol.

To learn more about how the Sucuri WAF protects and optimizes your website, visit our [knowledge base](https://docs.sucuri.net/kb-category/website-firewall/) or [chat with our team](https://sucuri.net/live-chat/).

[![](https://secure.gravatar.com/avatar/28c9f086a2ef4d4beae4637238919c78849f979bae5f3b369c9083b1ed0bffc7?s=120&d=mm&r=g)](https://blog.sucuri.net/author/klknight)

##### [Kyle Knight](https://blog.sucuri.net/author/klknight)

Kyle Knight is a Senior Technical Writer who joined the company in 2013. His responsibilities include managing various content and socials. With over a decade of experien...