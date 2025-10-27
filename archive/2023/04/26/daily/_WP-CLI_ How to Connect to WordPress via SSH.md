---
title: WP-CLI: How to Connect to WordPress via SSH
url: https://blog.sucuri.net/2023/04/wp-cli-how-to-connect-to-wordpress-via-ssh.html
source: 
date: 2023-04-26
fetch_date: 2025-10-04T11:32:56.360804
---

# WP-CLI: How to Connect to WordPress via SSH

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

* [Web Pros](https://blog.sucuri.net/category/web-pros)
* [Website Security](https://blog.sucuri.net/category/website-security)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# WP-CLI: How to Connect to WordPress via SSH

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* April 25, 2023

![WP-CLI: How to Connect to WordPress via SSH](https://blog.sucuri.net/wp-content/uploads/2023/04/23-BlogPost_Feature-Image_1490x700_WP-CLI-Connect-to-WordPress-via-SSH-820x386.jpg)

The WordPress admin dashboard, though intuitive and feature-rich, can be time-consuming to explore. If you’re looking for a more direct approach to website management, consider giving the **WordPress Command Line Interface (WP-CLI)** a try!

WP-CLI is an efficient and powerful way to manage your WordPress installation, allowing you to update your core files and plugins, configure multisite installations, and even backup your WordPress website. The [official WP-CLI tool](https://wp-cli.org/) enables you to interact directly with your WordPress environment via text commands to a [Secure Shell (SSH) window](https://blog.sucuri.net/2023/09/what-is-secure-shell-ssh-how-to-use-it-security-best-practices.html) connected to your website’s server.

In this post, we’ll be going over the basics of how to connect to your WordPress website via SSH and WP-CLI.

## What you will need to connect via WP-CLI:

There are a number of minimum requirements you’ll need to meet in order to install WP-CLI:

* SSH login credentials
* Unix environment or SSH client
* WordPress 3.7 or later
* PHP 5.6 or later

## SSH access

To access your website over SSH you will first need to obtain your server and login credentials. This is not the same as your WordPress Dashboard (wp-admin) login; you can usually find this information by logging into your hosting company’s website or by contacting their support team.

Log in to your hosting company’s website and look for options related to SSH or Shell Access. Enable it and take note of your server and login information, which is typically in the following format:

* **Server**: server.name.com
* **User**: username
* **Password**: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

In most cases, your server will be your **website domain name** (ie. example.com). You can try searching for “SSH” in your host’s knowledge base. Depending on your host’s setup, you may need to generate a key pair, and they can guide you through that process.

```
Note: Not all hosting providers will provide their clients with SSH access to their servers.
```

## Connecting to SSH

### Mac and Linux

If you’re a Mac or Linux user, there’s no need to install an SSH client. Simply use your built-in terminal application and follow these steps to connect to your website with your new SSH credentials:

1. Open **Terminal** (built-in)
2. Type this, replacing the **username** and **server.name.com** with your own user and server:

```
ssh username@server.name.com
```

3. Enter your password.
4. When you are connected successfully, you won’t receive an error or a confirmation, just a prompt where you can start typing. You will now be at the root of your website!

You can check that you are in the root of your website by typing:

```
ls
```

This command will list the contents of the folder you are in. You should see your WordPress files in those folders (**wp-admin, wp-content, wp-includes**, etc).

### Windows

If you’re a Windows user, you’ll need to download an SSH client. I’ve included instructions for PuTTy below:

1. Download the PuTTy executable from the [official website](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
2. Install the executable on your environment.
3. Open the application.

[![Putty Configuration window for SSH](https://blog.sucuri.net/wp-content/uploads/2015/04/putty.png)](https://blog.sucuri.net/wp-content/uploads/2015/04/putty.png)

4. Enter your server in the **Host Name** and select **SSH** from the radial button.
5. Click **Open**.
6. Enter your SSH **username** and **password.**

Upon successful connection, you’ll see a prompt where you can input commands. You can check to see if you are in the root of your website by typing:

```
ls
```

This command will list the contents of the folder you are in. You should see your WordPress files in those folders (**wp-admin, wp-content, wp-includes**, etc).

## Installing WP-CLI

Once you have successfully connected to your server via SSH, copy and paste the following commands to download and install WP-CLI:

```
curl -O https://raw.githubusercontent.com/wp...