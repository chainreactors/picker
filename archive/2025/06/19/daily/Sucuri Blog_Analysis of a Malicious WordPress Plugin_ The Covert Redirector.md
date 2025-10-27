---
title: Analysis of a Malicious WordPress Plugin: The Covert Redirector
url: https://blog.sucuri.net/2025/06/analysis-of-a-malicious-wordpress-plugin-the-covert-redirector.html
source: Sucuri Blog
date: 2025-06-19
fetch_date: 2025-10-06T22:51:49.982698
---

# Analysis of a Malicious WordPress Plugin: The Covert Redirector

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
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Analysis of a Malicious WordPress Plugin: The Covert Redirector

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* June 18, 2025

![Analysis of a Malicious WordPress Plugin The Covert Redirector](https://blog.sucuri.net/wp-content/uploads/2025/06/Analysis-of-a-Malicious-WordPress-Plugin-The-Covert-Redirector-820x385.png)

A few weeks ago, we received a support request from a website owner who was experiencing unexpected redirects. Visitors landed on the website normally, but after about 4–5 seconds, the site redirected them to unrelated and suspicious websites. During the investigation, we discovered a malicious plugin that was responsible for this behavior, continuing the trend of [attackers using fake WordPress plugins](https://blog.sucuri.net/2025/06/fake-wordpress-caching-plugin-used-to-steal-admin-credentials.html).

So far, we have seen at least [26 websites](https://publicwww.com/websites/%22videocdnnetworkalls.monster/video/a-character-with-exotic-siren-trains-meganekko-in-violent-titjob-promo-vid-869.mp4%22/) infected with the same malicious plugin, and it appears to be spreading through pirated or [compromised installations](https://publicwww.com/websites/%22steamycomfort.fun%22/).

## What Did We Find?

The attacker named the plugin `wordpress-player.php` and listed “**WordPress Core**” as the author to deliberately mimic legitimate WordPress components and evade immediate detection by site administrators.

![suspicious plugin](https://blog.sucuri.net/wp-content/uploads/2025/06/suspicious-plugin.png)

The attacker likely used this naming to avoid suspicion. The plugin was dropped directly into the `wp-content/plugins/` directory.

## Where Was the Infection Found?

The plugin leverages the wp\_footer action hook to inject its JavaScript and HTML components directly into the footer of every page loaded on the website. The malware **avoids execution for logged-in users** (site admins/editors):

![avoiding execution for logged in users](https://blog.sucuri.net/wp-content/uploads/2025/06/avoiding-execution-for-logged-in-users.png)

## How the Malware Works?

### Hidden Video Player with Adult Content

The plugin injects a hidden HTML5 video element into the page:

![hidden video player](https://blog.sucuri.net/wp-content/uploads/2025/06/hidden-video-player.png)

The style attributes render the video player completely invisible and off-screen to the user. The autoplay and muted attributes force the video to play silently in the background.

The video source URL, **hxxps://videocdnnetworkalls**[**.**]**monster/** originates from a suspicious domain. While the explicit content of the video itself is irrelevant to the technical compromise, its presence suggests an attempt to generate fraudulent video impressions or to ensure an active media session for subsequent malicious operations.

### Connects to Attacker-Controlled WebSocket Server

The core functionality of the malware resides within its JavaScript component, which establishes a persistent WebSocket connection to a remote command and control (C2) server.

![connects to attacker controlled websocket server](https://blog.sucuri.net/wp-content/uploads/2025/06/connects-to-attacker-controlled-websocket-server.png)

This WebSocket acts like a command and control (C2) channel. It allows the attacker to:

* Track active users
* Push live instructions to browsers
* Issue redirection or playback commands

The system assigns each visitor a pseudo-random ID and uses this ID in all communications back to the attacker’s server. It helps track who’s online and manage sessions.

Once connected, the malware listens for messages from the WebSocket server and reacts accordingly. This means that the attacker can send a new URL and redirect visitors to another site and the attacker can pause or resume the hidden video.

![hidden video manipulation](https://blog.sucuri.net/wp-content/uploads/2025/06/hidden-video-manipulation.png)

## Malicious Infrastructure Used

|  |  |
| --- | --- |
| **Type** | **URL** |
| Porn video | hxxps://videocdnnetworkalls[.]monster/ |
| WebSocket C2 | wss://steamycomfort[.]fun/ws/player |

## Impact on Website Integrity and Users

This “WordPress Player” malware poses significant risks to website owners and their visitors:

* **Unauthorized Traffic Redirection:** The prim...