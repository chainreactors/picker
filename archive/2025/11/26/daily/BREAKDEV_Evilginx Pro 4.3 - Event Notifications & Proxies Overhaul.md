---
title: Evilginx Pro 4.3 - Event Notifications & Proxies Overhaul
url: https://breakdev.org/evilginx-pro-4-3/
source: BREAKDEV
date: 2025-11-26
fetch_date: 2025-11-27T03:11:13.232038
---

# Evilginx Pro 4.3 - Event Notifications & Proxies Overhaul

[![BREAKDEV](https://breakdev.org/content/images/2022/08/breakdev_logo_with_title.png)](https://breakdev.org)

* [Home](https://breakdev.org/)
* [Evilginx Pro](https://evilginx.com)
* [Evilginx Mastery](https://academy.breakdev.org/evilginx-mastery)
* [Tools](https://github.com/kgretzky)
* [Contact](https://breakdev.org/contact/)

[evilginx](/tag/evilginx/)

 Featured

# Evilginx Pro 4.3 - Event Notifications & Proxies Overhaul

The newest 4.3 update delivers real-time event notifications, an overhaul of the tunnelling proxy system and a new CSS canary token evasion.

* [![Kuba Gretzky](/content/images/size/w100/2022/08/avatar512.png)](/author/kuba/)

#### [Kuba Gretzky](/author/kuba/)

Nov 26, 2025
• 4 min read

![Evilginx Pro 4.3 - Event Notifications & Proxies Overhaul](/content/images/size/w2000/2025/11/evilginx-pro-43-update.png)

I'm proud to announce that another major update to **Evilginx Pro** has just been released!

This update includes multiple bug fixes and introduces new features that were heavily requested. I strongly hope you will make great use of them!

This time, I've finished documenting the new features beforehand, and the guides are already available in the [online documentation](https://help.evilginx.com).

Let's dive in!

## New Features

Here are the highlights of this update:

### Event Notifications

![](https://breakdev.org/content/images/2025/11/notify-demo.gif)

Event notifications DEMO

This feature has been requested for a long time. The **4.3** update introduces real-time notifications, which can trigger for the following events in Evilginx:

* Lure URL was clicked.
* The visitor passed Botguard validation and arrived at the phishing page.
* Credential was captured.
* Session tokens were captured.

Notifications can be sent via [Slack](https://slack.com/) messages, [Pushover](https://pushover.net/) push notifications, or the most versatile option: **webhook requests** in JSON format.

Webhook event notifications allow you to use the data captured by Evilginx to build your own custom tooling. It will enable you to receive captured data in real time.

Use the retrieved data to generate phishing engagement reports or for lateral movement using the captured credentials and session tokens.

All that is required is an HTTP/HTTPS server written in Python, Go, or any other language you are comfortable with. The event data will be sent from the Evilginx server in JSON format as an HTTP request to the URL of your choosing.

You can find the complete documentation with usage examples in the official documentation:

[Read the Event Notification documentation](https://help.evilginx.com/pro/usage/notify)

### Tunnelling Proxies

The proxy feature has been left abandoned for quite some time, and it badly needed an update.

A few months ago, I realised the JA4 signature spoofing would stop working when routing Evilginx connections through a proxy. Since I had to fix how the proxies are implemented in **Evilginx Pro**, I decided to give the feature a complete overhaul.

The tunnelling proxy overhaul now allows you to manage multiple proxy servers on a single server and assign them to route connections server-wide, only for specific phishlets, or only to particular lures.

These options should provide enough flexibility to evade geolocation-based access controls and prevent CAPTCHA prompts when connections are routed through particular countries during your phishing engagements.

You can find the complete documentation with usage examples in the official documentation:

[Read the Tunnelling Proxies documentation](https://help.evilginx.com/pro/usage/proxy)

### Improved CSS canary token evasion

Thanks to [Rad Kawar](https://x.com/rad9800) (check out his new tool [Deceptiq](https://deceptiq.com/)!), I was informed that CSS canary tokens made by [Thinkst Canary](https://canary.tools/) added a bit of obfuscation to the `url(...)` block, through escaping random characters with hex values, like:

```
body {
    background: url('abcdefg.\63loudfr\6fnt\2enet/012345/cGhpc2guZG9tYWluLmNvbQ%3D%3D/img.gif') !important;
}
```

Escaped URL pointing to the canary token

Here is the function, which handles the generation of escaped canary token URLs:

![](https://breakdev.org/content/images/2025/11/image.png)

The randomly escaped string would pretty effectively fool string rewriting implemented in phishlets, which looked for a string `.cloudfront.net` to replace it with something else to prevent the canary token from calling home:

```
sub_filters:
  - {triggers_on: 'aadcdn.msftauthimages.net', orig_sub: 'aadcdn', domain: 'msftauthimages.net', search: '\.cloudfront\.net', replace: '.nowhere.local', mimes: ['text/css']} # disable canary tokens loaded from .cloudfront.net domain
```

String filtering in a phishlet

The Pro version in the **4.3** update will now detect all URLs in proxied CSS files, including the "obfuscated" (escaped) ones, which may carry canary tokens, and it will unescape them, so that you can freely replace them with `sub_filters`.

### Other improvements

There are multiple quality-of-life improvements included with this update, including:

* Ability to uninstall servers with `servers uninstall` command.
* Lure ID is now visible in the list of captured sessions, so you know which session originated from which lure.
* Phishlets now support a `port` parameter in `proxy_hosts` entries, allowing you to target websites hosted on ports other than the standard TCP `443`.
* Fixed server deployment for the latest versions of Debian and Ubuntu. The deployments will now work correctly for systems running the new `sysctl` version, which reads configuration files from the `/etc/sysctl.d/` directory.
* The Gophish click event no longer triggers on URL clicks. Instead, it triggers once Botguard validates the connection and after the redirector redirects to the phishing page.

Check out the complete changelog below:

[Evilginx Pro 4.3 - CHANGELOG](https://help.evilginx.com/pro/changelog#430-2025-11-26)

## Closing thoughts

I strongly hope you enjoy this update, and the new event notifications feature allows you to create epic custom tooling integrated with your Evilginx phishing campaigns.

The next thing I'll be working on is the new **Phishlets V2** format, which is long overdue. The work has already started, and I have big plans to overhaul Evilginx to become an extremely versatile reverse proxy tool.

Another project I've started looking into is how Evilginx phishing links can be hosted on a CDN. Stay tuned for that, as I may release a quick blog post about it once I figure out a working setup.

If you haven't already, make sure to apply and join our [BREAKDEV RED community for red teamers](https://red.breakdev.org/join). Our secure Discord server is a great place to discuss everything related to cybersecurity, and I'd love to see you there!

If you're already using ****Evilginx Pro**** and would like something improved or added, feel free to let me know via email, Twitter [@mrgretzky,](https://x.com/mrgretzky) or [LinkedIn](https://www.linkedin.com/in/kubagretzky/).

Happy phishing! 🪝🐟

[Learn more about Evilginx Pro](https://evilginx.com)

[![Evilginx Pro 4.2 - Anti-phishing evasions and more!](/content/images/size/w600/2025/08/evilginx-pro-42-update.png)](/evilginx-pro-4-2/)

[Featured

## Evilginx Pro 4.2 - Anti-phishing evasions and more!

The latest update includes a complete proxy engine rewrite, new anti-phishing evasions, added support for new DNS providers, custom hostnames for lure URLs, better Gophish integration and more!](/evilginx-pro-4-2/)

Aug 14, 2025
—
17 min read

[![Evilginx Pro is finally here!](/content/images/size/w600/2025/03/evilginx_pro_release_cover.png)](/evilginx-pro-release/)

[Featured

## Evilginx Pro is finally here!

After over two years of development, Evilginx Pro reverse proxy phishing framework for red teams is finally live!](/evilginx-pro-release/)

Mar 12, 2025
—
9 min read

[![Evilginx 3.3 - Go & ...