---
title: How to Prevent SSH Brute Force Login Attacks
url: https://blog.sucuri.net/2023/04/how-to-prevent-ssh-brute-force-login-attacks.html
source: Sucuri Blog
date: 2023-04-21
fetch_date: 2025-10-04T11:33:36.770794
---

# How to Prevent SSH Brute Force Login Attacks

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
* [Web Pros](https://blog.sucuri.net/category/web-pros)
* [Website Security](https://blog.sucuri.net/category/website-security)

# How to Prevent SSH Brute Force Login Attacks

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* April 20, 2023

![What are SSH brute force login attacks and how to protect your server from them](https://blog.sucuri.net/wp-content/uploads/2023/04/23-BlogPost_Feature-Image_1490x700_What-are-SSH-Brute-Force-Login-Attacks--820x386.jpg)

## What is an SSH brute force attack?

A [Secure Shell (SSH)](https://blog.sucuri.net/2023/09/what-is-secure-shell-ssh-how-to-use-it-security-best-practices.html) brute force attack is a common form of attack that targets remote services, particularly unix-based servers running SSH services for secure remote connections. These attacks often involve automated tools and bots to continuously attempt common password and username combinations until they successfully gain access to a server. Excessive numbers of failed log-ins can indicate a brute-force attack on your SSH server.

## Why do attackers brute force SSH?

An attacker may be motivated to brute force SSH for a number of reasons. Brute force attacks serve as a method to discover the correct username and password combination or a hashed token — and if successful, can allow an attacker to gain unauthorized access to valuable financial information and files, disrupt services, distribute malware to other systems, or even hijack the compromised system for their own purposes. This trial-and-error approach to hacking is based on guessing credentials, file paths, or URLs, either through a logical process or by attempting all possible key combinations, often starting with the most commonly used passwords.

Bad actors often utilize [hack tools](https://blog.sucuri.net/2022/06/how-to-find-clean-up-the-anonymousfox-hack.html) to automate and expedite the brute force attack process. They may distribute the attack across multiple source locations or use malware to target protected internal accounts. Widely known tools, such as Hydra, Chaos, CrackMapExec, and PoshC2, are equipped with brute force functionalities that perform rapid attacks against different protocols.

## How to protect your server from SSH brute force attacks

To protect your server from SSH brute force attacks, there are a number of strategies you can implement to help block attempts and prevent unauthorized access.

### 1. Switch to SSH key authentication

Using the default username/password authentication for SSH can make your server more vulnerable to brute-force attacks. You can enhance security by implementing key-based SSH authentication, which uses public and private SSH key pairs. Keep the private key on the client’s computer and copy the public key to the server. SSH keys are virtually impossible to guess or compromise via brute-force.

During SSH key authentication, your server verifies if the client’s computer has a correct private key. If authentication is successful, a shell session is created and an SSH connection is established between the client and the host.

To disable password authentication, edit your SSH configuration file:

```
$ sudo vim /etc/ssh/sshd_config
```

Set the **PasswordAuthentication** parameter to **no**:

```
PasswordAuthentication no
```

Save the file and reload SSH to apply the changes:

```
$ sudo systemctl reload ssh
```

This can also be configured during the initial creation of your virtual private server, depending on the hosting provider you are using.

### 2. Limit authentication attempts

To further protect SSH against brute force attacks, you can limit the number of authentication attempts allowed per connection. This can be accomplished by adjusting the **MaxTries** variable in your **sshd\_config** file.

An authentication attempt refers to any enabled authentication method in the **sshd** configuration, such as offering a SSH key, attempting Kerberos/GSSAPI authentication, or typing a password into the authentication prompt. Each authentication attempt counts as one attempt towards accessing the server.

A recommended starting point is setting **MaxTries** to **3** to balance security and user experience.

**Important caveat:**

If your main concern is protecting against password-guessing attacks from worms and bots on other compromised systems, then reducing the **MaxAuthTries** setting may not be the best approach. Bots will continue to try to guess passwords endlessly, placing a strain on your CPU as SSH ...