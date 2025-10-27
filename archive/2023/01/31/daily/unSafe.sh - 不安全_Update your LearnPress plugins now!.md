---
title: Update your LearnPress plugins now!
url: https://buaq.net/go-147282.html
source: unSafe.sh - 不安全
date: 2023-01-31
fetch_date: 2025-10-04T05:13:08.323440
---

# Update your LearnPress plugins now!

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Update your LearnPress plugins now!

It’s time for a reminder to ensure all of your WordPress plugins are fu
*2023-1-30 20:15:0
Author: [www.malwarebytes.com(查看原文)](/jump-147282.htm)
阅读量:24
收藏*

---

It’s time for a reminder to ensure all of your WordPress plugins are fully up to date (or removed, if you don't need them). Bleeping Computer reports that [as many as 75,000 WordPress sites](https://www.bleepingcomputer.com/news/security/75k-wordpress-sites-impacted-by-critical-online-course-plugin-flaws/) may be open to several flaws in a plugin called LearnPress. Worse, the update tally for users of the plugin [isn't doing particularly well](https://wordpress.org/plugins/learnpress/advanced/), with a big slice of site owners still to update.

If you own or operate a website there is a very good chance it uses WordPress. More than [40 precent of websites](https://w3techs.com/technologies/overview/content_management) use a version of it, and it's used on more websites that all other website Content Management Systems (CMS) combined. One of the reasons it's so popular is that it can be easily extended by adding plugins, of which there are tens of thousands.

Provided it is kept up to date and protected by two-factor authentication, WordPress itself is quite secure. Because of that, in recent years threat actors have focussed on exploiting it via vulnerabilities in plugins rather than attacking it directly.

LearnPress is a WordPress plugin used for creating and selling courses online, with extra paid options available for additional features. This is something which would no doubt have been popular over the pandemic, and indeed up to the present day, as companies continue to lean heavily on online and remote services only.

A ripe target, then, for exploitation and targeted attacks.

Somewhere in the region of 100,000 sites [make use of the LearnPress plugin](https://patchstack.com/articles/multiple-critical-vulnerabilities-fixed-in-learnpress-plugin-version/), all of which will need to [upgrade to LearnPress 4.2.0](https://wordpress.org/plugins/learnpress/) if they haven't already.

The vulnerabilities are:

* [CVE-2022-47615](https://cve.report/CVE-2022-47615), an unauthenticated Local File Inclusion vulnerability that allows remote viewing of local files on a web server, which could lead to API keys, credentials, and other secrets being exposed.
* [CVE-2022-45808](https://cve.report/CVE-2022-45808) and [CVE-2022-45820](https://cve.report/CVE-2022-45820), a pair of SQL injection vulnerabilities that could result in data modification, code execution, and more.

Patchstack discovered the three issues between the November 30, 2022 and December 4, 2022, with initial outreach on the same day as the first discovery, and subsequent details passed on over the following days. The issues were patched on December 20.

This is a fairly speedy turnaround compared to some of the other timeline notifications we’ve seen for plugins. Indeed, it’s not uncommon to not hear back from a developer at all and discover the plugin has been abandoned. (If you ever find yourself dealing with an abandoned plugin, you’ll need to untangle your site from it, which can cause [additional complications and headaches](https://www.malwarebytes.com/blog/news/2022/12/abandoned-android-apps-pack-a-vulnerability-punch) for the site admin.)

Just to reiterate, upgrading your LearnPress install to version 4.2.0 is the way to lock these particular vulnerabilities down. With this done, you shouldn’t have any more concerns.

As for your plugins generally, this may be the perfect time to have a quick spring clean of your site and see which plugins you need and which ones you don’t:

* **Update existing plugins**. If you use WordPress you can check if you have any plugins that need updating by logging in to your site and going to **Dashboard** > **Updates.** (The **Themes** and **Plugins** menu items will also have red circles next to them if any need updating.) Update everything.
* **Turn on automatic updates for plugins**. By default, WordPress does not update plugins automatically. You can [enable this on a per-plugin basis](https://www.wpbeginner.com/plugins/how-to-enable-automatic-updates-for-wordpress-plugins/) by going to the **Plugins** screen and clicking **Enable auto-updates** next to each plugin.
* **Remove unsupported plugins**. Go to the **Plugins** screen and click **View details** for each plugin. This screen shows you the last version of WordPress the plugin was tested with, and when it was last updated. It will also display an alert if it thinks the plugin is no longer supported.
* Remove unnecessary plugins. Check out how many plugins and themes you have installed on your site. Do you need them all? Can any of them be removed or replaced? Generally, fewer is better.

If you can’t make enough time available to keep on top of theme and plugins, don't let not doing it become an option: Pay somebody to do it for you.

Stay safe out there!

---

文章来源: https://www.malwarebytes.com/blog/news/2023/01/update-your-learnpress-plugins-now
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)