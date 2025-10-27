---
title: WP-CLI: How to Install WordPress via SSH
url: https://blog.sucuri.net/2022/11/wp-cli-how-to-install-wordpress-via-ssh.html
source: Sucuri Blog
date: 2022-11-23
fetch_date: 2025-10-03T23:28:39.198893
---

# WP-CLI: How to Install WordPress via SSH

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# WP-CLI: How to Install WordPress via SSH

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* November 22, 2022

![WP-CLI: How to Install WordPress via SSH](https://blog.sucuri.net/wp-content/uploads/2022/11/BlogPost_Feature-Image_1490x700_WP-CLI-How-to-Install-WordPress-via-SSH-820x386.png)

Sure, there are tons of one-click installers floating around for WordPress. But they’re not always the most secure option — and *can* still be tedious to use, especially if you need to update default configurations after installation. But what if I told you there’s a simple and reliable way to manage and **install WordPress using WP-CLI over SSH**?

In today’s post, we’ll cover the basics of connecting to your server and installing WordPress core over [SSH (Secure Shell)](https://blog.sucuri.net/2023/09/what-is-secure-shell-ssh-how-to-use-it-security-best-practices.html). So, let’s dive into one of the most secure and convenient ways to install WordPress on your web server!

**Contents:**

* [**Connect to the server via SSH**](#connect-with-ssh)
* [**Install WP-CLI**](#install-wp-cli)
* [**Create a WordPress directory**](#create-directory)
* [**Download and configure WordPress**](#download-wordpress)
* [**Change permissions for wp-config.php**](#change-permissions)
* [**Configure wp-config.php**](#configure-wp-config-php)
* [**Enable file uploads**](#enable-file-uploads)
* [**Clear command history**](#clear-history)
* [**Video tutorial**](#video)
* [**Additional resources**](#resources)

## Is SSH really more secure than FTP?

Using terminal to access and install WordPress isn’t just convenient — it has another added bonus: SSH authenticates and encrypts all connections. And since the SSH protocol encrypts the commands and data transfers to and from your server, it does a better job keeping your website’s server connection private than regular FTP (File Transfer Protocol) clients.

FTP has been around since before the evolution of public networks and wasn’t designed with security in mind. While FTP clients may be convenient, there are some disadvantages to using them — including the fact that files, usernames, and passwords are sent in plain text. Any data that’s transferred using an unencrypted protocol is subject to possible eavesdropping, which could put your system or data at risk.

SSH, on the other hand, was born after a [sniffing attack was performed on the HelSinki University of Technology](https://www.oreilly.com/library/view/ssh-the-secure/0596008953/ch01s05.html) and users realized they needed a more secure method of transferring data. This client-server based protocol works by using authentication methods and encrypting remote connections for users and processes.

Furthermore, FTP is only able to perform basic file operations and transfer files from one destination to another. But SSH provides secure access to the server shell, allowing you to perform and execute a full range of server commands. It also supports extra functionalities such as monitoring running services or applications and transferring or modifying files.

```
If these SSH instructions are a little intimidating, consider using SFTP (Secure File Transfer Protocol) over regular FTP.

SFTP is a file transfer protocol that uses SSH encryption to securely transfer files between systems. It comes as a standard part of SSH version 2.0 and most FTP clients support it.
```

## How to install WordPress using WP-CLI

Before we get started, make sure you have the following:

* SSH access and key pairs
* Server details

You’ll also want to ensure you have defined the necessary information for your **wp-config.php** file, too.

Next, let’s review the steps to install WordPress using WP-CLI.

### 1 – Connect to your website’s root over SSH

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
* Enter your **username** and **password**

![Windows Putty Client](https://blog.sucuri.net/wp-content/uploads/2022/11/putty_client-1.png)

### 2 – Install WP-CLI

Once ...