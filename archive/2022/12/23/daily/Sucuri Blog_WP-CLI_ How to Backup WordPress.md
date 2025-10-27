---
title: WP-CLI: How to Backup WordPress
url: https://blog.sucuri.net/2022/12/wp-cli-how-to-backup-wordpress.html
source: Sucuri Blog
date: 2022-12-23
fetch_date: 2025-10-04T02:18:13.506302
---

# WP-CLI: How to Backup WordPress

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# How to Backup a WordPress Site for Free with WP-CLI

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* December 22, 2022

![How to backup WordPress with WP-CLI](https://blog.sucuri.net/wp-content/uploads/2022/12/WP-CLI-Backup-820x385.png)

Regular website backups are the foundation of a solid website security plan. In the event of data loss or malware infection, restoring a WordPress backup helps you quickly and easily recover your environment and revert it back to its last known good configuration. But what if I told you that there’s a simple and reliable way to **backup WordPress using WP-CLI over SSH** for free?

In today’s post, we’ll cover the basics of how to connect to your server and backup WordPress over [SSH](https://blog.sucuri.net/2023/09/what-is-secure-shell-ssh-how-to-use-it-security-best-practices.html) — along with some security tips to protect your backups. So, let’s dive in and examine one of the easiest (and cheapest ways) to make regular backups of your WordPress website!

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
ssh username@ssh.host.server.com
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

Next, make the file executable.

```
chmod +x wp-cli.phar
sudo mv wp-cli.phar /usr/local/bin/wp
```

You can verify that WP-CLI is properly installed by running the **wp cli version** command again. Once you’ve confirmed the installation, you’re ready to backup your WordPress database.

### 3 – Backup your WordPress database

Navigate to the root of your website. This is the main folder that contains all of the files of your domain. By default, the root folder of your website is **public\_html**.

```
cd ~/public_html
```

Type the...