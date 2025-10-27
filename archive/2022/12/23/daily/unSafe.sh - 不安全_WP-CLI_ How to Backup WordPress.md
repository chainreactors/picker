---
title: WP-CLI: How to Backup WordPress
url: https://buaq.net/go-141056.html
source: unSafe.sh - 不安全
date: 2022-12-23
fetch_date: 2025-10-04T02:17:59.900556
---

# WP-CLI: How to Backup WordPress

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

WP-CLI: How to Backup WordPress

Regular website backups are the foundation of a solid website security plan. In the eve
*2022-12-22 23:28:17
Author: [blog.sucuri.net(查看原文)](/jump-141056.htm)
阅读量:35
收藏*

---

Regular website backups are the foundation of a solid website security plan. In the event of data loss or malware infection, restoring a WordPress backup helps you quickly and easily recover your environment and revert it back to its last known good configuration. But what if I told you that there’s a simple and reliable way to **backup WordPress using WP-CLI over SSH** for free?

In today’s post, we’ll cover the basics of how to connect to your server and backup WordPress over SSH — along with some security tips to protect your backups. So, let’s dive in and examine one of the easiest (and cheapest ways) to make regular backups of your WordPress website!

**Contents:**

* **[Why should I backup my WordPress website?](#why-backup-wordpress)**
* **[How to backup your WordPress database and files](#how-to-backup-wordpress)**
* **[Video tutorial](#video-tutorial)**
* [**Additional resources**](#additional-resources)

## Why should I backup my WordPress website?

[Regular backups](https://blog.sucuri.net/2021/03/the-importance-of-website-backups.html) are crucial for any WordPress administrator. Accidents happen — often at the least convenient times.

You might forget to update your plugins, which lead to vulnerability exploits and malware in your WordPress environment. Or you might add some new code which completely *b0rks* your site.

By making regular backups of your environment — especially before applying updates, patches, site migrations, or installing new software — you can make it easier to restore your site in the event of an issue.

In short, regularly backing up your WordPress site is an important step in maintaining a secure online presence.

## How to backup your WordPress database and files

WP-CLI makes quick work of backing up your WordPress files and database. But before we get started, make sure you have the following:

* SSH access and key pairs
* Server details

Next, let’s review the steps to backup your WordPress database. If you already have [WP-CLI installed on your server](https://blog.sucuri.net/2022/11/wp-cli-how-to-install-wordpress-via-ssh.html), connect to your website’s root via SSH and skip ahead to step 3.

### 1 – Connect to your website’s docroot over SSH

First, connect to your website’s docroot over SSH. You can use terminal for Mac or Linux, and PuTTy for Windows.

#### **Mac/Linux**

* Open terminal.
* Type the following, replacing the **username** and **server** info (ssh.host.server.com) with your own:

```
ssh [email protected]
```

* Press **Enter** and type your password to authenticate.

#### **Windows**

* Open [PuTTy](https://www.putty.org/).
* Enter your server IP as your **Host Name.**
* Select **SSH.**
* Click **Open.**
* Enter your **username** and **password.**

### 2 – Install WP-CLI

Once you’ve connected to your server, you’ll want to check if WP-CLI has already been pre-installed by your host. Type the following command into terminal:

```
$ wp cli version
```

If WP-CLI is present, you should get an output that looks something like this:

```
$ wp cli version

WP-CLI 0.24.1
```

If WP-CLI has not yet been installed by your host, copy and paste the following command into the prompt and press **Enter** to install the latest version of WP-CLI.

```
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
```

And if that doesn’t work, try:

```
wget https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
```

Next, verify that WP-CLI is properly installed by running the **wp cli version** command again. Once you’ve confirmed the installation, you’re ready to backup your WordPress database.

### 3 – Backup your WordPress database

Navigate to the root of your website. This is the main folder that contains all of the files of your domain. By default, the root folder of your website is **public\_html**.

```
cd ~/public_html
```

Type the following command and press **Enter**:

```
wp db export
```

Great! You now have a backup of your database in an **.SQL** file at the root of your website.

### 4 – Compress your WordPress file system

Copying files from the server is not available in WP-CLI, but you can quickly compress all of your files including the new .SQL backup of your database.

Make sure you are in the root of your website, as we described earlier. Using the **tar** command with a few special **parameters** that make the backup better. The trailing **period at the end is very important**, as it ensures the new compressed file is saved in the same directory.

```
tar -vczf yourbackupfilename.gz .
```

If you’re a Windows user, you may find adding a zip compression option useful for your environment.

```
zip -r website.zip *
```

### 5 – Transfer your backup off-site

From here, like with any good backup, you’ll want to transfer it off the server and store it in a remote location.

You can use FileZilla with SFTP; your SSH credentials should work. If not – talk to your host.

Open the FileZilla Site Manager and enter your SFTP connection details, then move your backup file to a secure off-site location.

As a best practice, always keep a recent working copy of your WordPress files stored off your server. If a plugin conflict breaks your website, you will want to have the following ready to recover:

* Core files for your **current versions** of WordPress, plugins, and themes.
* Any custom or altered files.
* Your **wp-config.php** or database credentials.

Once your backup has been made and safely transferred off your server, you’re free to update WordPress, install a new plugin, or make important code changes without worrying about whether you’ll be able to restore your site.

**Important note:** Be sure to remove the backup completely from your server environment once you’ve transferred it to a secure off-site location. This helps prevent attackers from gaining unauthorized access to your **wp-config.php** file and other sensitive website information.

## How to backup WordPress: video tutorial

If you need a quick video tutorial, check out this video on how to backup and update WordPress with WP-CLI.

## Additional resources

WP-CLI isn’t just for backing up WordPress. This handy command-line interface can be used to download and install WordPress, manage and update plugins, and even configure multisite installations!

I encourage you to [check out the WP-CLI documentation](http://wp-cli.org/) to learn more about the wonderful world of WordPress’ command-line interface. And check out these additional resources for common WP-CLI commands and instructions.

* [WP-CLI Commands](https://developer.wordpress.org/cli/commands/)
* [How to Install WordPress via SSH](https://blog.sucuri.net/2022/11/wp-cli-how-to-install-wordpress-via-ssh.html)
* [How to connect to WordPress via SSH](https://blog.sucuri.net/2015/07/wp-cli-guide-connect-to-wordpress-via-ssh-intro.html)
* [How to manage Plugins and Themes with WP-CLI](https://blog.sucuri.net/2015/07/wp-cli-guide-secure-plugin-theme-management.html)

![](https://secure.gravatar.com/avatar/a3ef43c4765fe447a305b82f38ea7bd1?s=115&d=mm&r=g)

## Reader Interactions

文章来源: https://blog.sucuri.net/2022/12/wp-cli-how-to-backup-wordpress.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net...