---
title: How to Update, Install & Remove WordPress Plugins & Themes With WP-CLI
url: https://buaq.net/go-166843.html
source: unSafe.sh - 不安全
date: 2023-06-02
fetch_date: 2025-10-04T11:46:01.971600
---

# How to Update, Install & Remove WordPress Plugins & Themes With WP-CLI

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

![](https://8aqnet.cdn.bcebos.com/eb4711e5060b6ec5714744c646a2cc17.jpg)

How to Update, Install & Remove WordPress Plugins & Themes With WP-CLI

WordPress, like other open-source content management systems, allows you to enhance your webs
*2023-6-1 23:36:53
Author: [blog.sucuri.net(查看原文)](/jump-166843.htm)
阅读量:37
收藏*

---

[![WP-CLI: How to Connect to WordPress via SSH](https://blog.sucuri.net/wp-content/uploads/2023/04/23-BlogPost_Feature-Image_1490x700_WP-CLI-Connect-to-WordPress-via-SSH-820x386.jpg)](https://blog.sucuri.net/wp-content/uploads/2023/04/23-BlogPost_Feature-Image_1490x700_WP-CLI-Connect-to-WordPress-via-SSH.jpg)

WordPress, like other open-source content management systems, allows you to enhance your website’s appearance and functionality through custom code and third-party components like plugins and themes. It’s these extensions that allow you to publish content with added functionality for your visitors and facilitate the unique look of your brand.

While the developers who build these extensions often have extensive knowledge of development best practices, security is not always their core competency — and third party components may contain known (or undiscovered) bugs and vulnerabilities that can pose a serious threat to your website. There are a plethora of ways to break a website or exploit a [plugin vulnerability](https://blog.sucuri.net/category/vulnerability-disclosure), so it’s essential to keep third party plugins and themes patched with the latest security and bug fixes to minimize risk.

WP-CLI over SSH is a great way to use the command line while keeping your connection to your website encrypted; it allows you to easily execute text commands to manage your WordPress website. In this post, we are going to take a look at the most popular ways to manage your WordPress themes and plugins securely over SSH. We assume that you have read the previous posts on [how to connect to your website via SSH](https://blog.sucuri.net/2023/04/wp-cli-how-to-connect-to-wordpress-via-ssh.html) and [installing WP-CLI.](https://blog.sucuri.net/2022/11/wp-cli-how-to-install-wordpress-via-ssh.html#install-wp-cli)

To begin, connect to your WordPress environment using SSH. Then, proceed with the following steps to securely install, update, and remove your plugins and themes.

## List installed plugins or themes and check for updates:

Maybe you want to start off by checking which plugins are installed on your WordPress site, and which components have updates available?

To check for updates and obtain a list of installed plugins and themes, leverage the following commands:

|  |  |
| --- | --- |
| **Command** | **Description** |
| wp plugin list | Shows a list of actively installed plugins along with information about available updates. |
| wp theme list | Shows a list of actively installed themes along with information about available updates. |

With these results, you’ll now have the **slugs** for any plugins installed on your website. You can use these slugs in your commands to manipulate specific plugins, such as adding and removing components from your environment.

## Manage plugins by slug with WP-CLI

If you know the slug of the plugin that you want to manage, you can use these commands to add, remove, or update plugins from your site:

|  |  |
| --- | --- |
| **Command** | **Description** |
| wp plugin install {slug} | Installs a specific plugin based on the provided slug. |
| wp plugin activate {slug} | Activates an installed plugin based on the provided slug. |
| wp plugin update {slug} | Updates an installed plugin based on the provided slug. |
| wp plugin deactivate  {slug} | Deactivates an installed plugin based on the provided slug. |
| wp plugin delete {slug} | Deletes a plugin based on the provided slug. |

## Manage themes by slug with WP-CLI

The same goes for managing themes! If you know the slug of the theme that you want to manage, you can use these commands to manage them:

|  |  |
| --- | --- |
| **Command** | **Description** |
| wp theme install {slug} | Installs a specific theme based on the provided slug. |
| wp theme activate {slug} | Activates an installed theme based on the provided slug. |
| Wp theme update {slug} | Updates an installed theme based on the provided slug. |
| wp theme deactivate  {slug} | Deactivates an installed theme based on the provided slug. |
| wp theme delete {slug} | Deletes a theme based on the provided slug. |

### Locating plugin and theme slugs

If you want to install a brand new plugin or theme but you don’t know the **slug** for it, you can find it as a directory under the WordPress.org repository URL:

![](https://blog.sucuri.net/wp-content/uploads/2015/05/plugin-pick.jpg)

![](https://blog.sucuri.net/wp-content/uploads/2015/05/theme-pick.jpg)

#### Installing a plugin with WP-CLI from a URL

You can **hover over the download button** from the plugin’s download page, **right-click** the button and **copy the ZIP file location** that the button goes to.

![Copy the download link to obtain the zip file location for a plugin](https://blog.sucuri.net/wp-content/uploads/2023/05/copy_download_link.png)

Of course, take care to **only install plugins and themes from trusted sources** because [pirated and nulled themes and plugins](https://blog.sucuri.net/2023/02/the-dangers-of-installing-nulled-wordpress-themes-and-plugins.html) are dangerous and often contain some nasty backdoors.

Hacking has become a fairly common criminal activity; new vulnerabilities are discovered on a regular basis by bad actors who read through lines and lines of code until they find something they can exploit. It’s impossible to guess exactly how many zero-day vulnerabilities exist that haven’t been disclosed yet.

## Update all plugins and themes in WordPress:

To update all actively installed plugins and themes in your environment, simply type the following commands:

|  |  |
| --- | --- |
| **Command** | **Description** |
| wp plugin update –all | Updates all plugins installed in your WordPress site. |
| wp theme update –all | Updates all themes installed in your WordPress site. |

## Reducing risk by limiting third-party plugins and themes

For every plugin and theme you add to your website, you are adding a whole directory of files that might contain a serious bug or vulnerability. This is the exact reason why you should choose additional themes and plugins for your site wisely — and always remove anything that you don’t need.

You can accomplish this directly in the WordPress console, as long as you have write access to the server and your SFTP credentials.

```
Plain FTP is an insecure communication mechanism, please leverage SFTP when it’s available.
```

## Bonus video tutorial

For additional guidance, check out this short video tutorial we’ve prepared to help you through the process. Enjoy!

[![](https://secure.gravatar.com/avatar/a3ef43c4765fe447a305b82f38ea7bd1?s=120&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

Rianna MacLeod is Sucuri’s Marketing Manager who joined the company in 2017. Her main responsibilities include ghost-writing technical content, SEO, email, and experimentation. Rianna’s professional experience spans over 10 years of technical writing and marketing. When Rianna isn’t drafting content or building templates, you might encounter her hiking in the forest or enjoying the beach. You can find her on [Twitter](https://twitter.com/riannamacleod) and [LinkedIn](https://www.linkedin.com/in/rianna-macleod/).

##### Related Tags

* [Best Practices](https://blog.sucuri.net/tag/best-practices),
* [Secure Development](https://blog.sucuri.net/ta...