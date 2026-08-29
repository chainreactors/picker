---
title: flyphish
url: https://kitploit.com/en/tools/github/virtualsamuraii/flyphish
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:31:07.425678
---

# flyphish

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

flyphish — Deploy a phishing infrastructure on the fly. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/virtualsamuraii/flyphish

![](https://assets.kitploit.com/production/public/tools/53376/5044f92c7d38e4c64ae18ba208fd228553b1d6a11285c353d4e9e44c4730e1c3-display-v1.webp)

[Cloud Infrastructure Security](/en/categories/cloud-infrastructure-security)[Phishing Tools](/en/categories/phishing-tools)[Phishing](/en/categories/phishing)[Penetration Testing](/en/categories/penetration-testing)[Red Teaming](/en/categories/red-teaming)[Email Security](/en/categories/email-security)

![GitHub](/providers/github.png)virtualsamuraii/flyphish

# flyphish

Deploy a phishing infrastructure on the fly.

[View Repository](https://github.com/virtualsamuraii/flyphish)

807351 year ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Flyphish

Flyphish is an Ansible playbook allowing cyber security consultants to deploy a phishing server in the cloud for security assessments.

The playbook installs and configures **Gophish**, **Postfix** and **OpenDKIM** on a virtual machine in the cloud. Additionally, for OPSEC purposes, the playbook removes default IOCs (SMTP headers) from Gophish and Postfix servers configurations.

# Install

## Requirements

* Make sure you have a Linux (Debian, Ubuntu or Kali) instance in the cloud (Amazon EC2, Azure VM, Google GCE...) with a public IPv4 address. Install OpenSSH and enable root access with SSH key-based authentication only.

![alt text](https://assets.kitploit.com/production/public/readmes/53376/82b12bea7b7e42013d801013bd23482ea1bcd61fd4d8b9713fa02a878843acc2/eca806ac956b74f523aedba8f2817014a1e474aa032029240b3dc240cd9b1174-display-v1.webp)

* Purchase a domain and set it's DNS records accordingly (A, MX and SPF records must point to your cloud instance's public IP address).
* Install Ansible on your own machine :

root@kitploit:~

```
sudo apt install ansible
```

## Installation steps

* Clone the repository

root@kitploit:~

```
git clone --recursively https://github.com/VirtualSamuraii/flyphish.git
```

* Put your cloud instance public IP address in the  file.

[Download Tool](https://github.com/virtualsamuraii/flyphish)

**hosts**

- Put your phishing domain in the **group\_vars/all.yml** file.

You're ready to go !

# Usage

* Run the playbook and wait for your phishing server to be deployed :

root@kitploit:~

```
ansible-playbook -i hosts playbook.yml
```

* Once finished, the playbook displays your DKIM public key. Add this key to your DKIM record in your domain's DNS zone.

![alt text](https://assets.kitploit.com/production/public/readmes/53376/5044f92c7d38e4c64ae18ba208fd228553b1d6a11285c353d4e9e44c4730e1c3/e0fddd2d3a5af069f433931ab56ba276e91e49c5f72dec2c783b8b46dde369f3-display-v1.webp)

The rest is up to you.

From now on, you can log into your cloud instance using SSH, start your Gophish server and configure it to send signed emails from your Postfix SMTP server.

# Tips

* Avoid exposing your Gophish server on internet. You can access your Gophish UI on your local machine (<https://127.0.0.1:3333>) using SSH :

root@kitploit:~

```
ssh -i ~/.ssh/id_rsa youruser@yourcloudinstance -q -C -N -L 3333:127.0.0.1:3333
```

![alt text](https://assets.kitploit.com/production/public/readmes/53376/787a7c2e4c8e1ef25dd54dcb02688d9fdf1421f58d3bc798df4d91d53f3c4404/00e172908ffbd940ad817d1d246235af0f7914bda41b6b796ca055e4aea14130-display-v1.webp)

* Most of the cloud services providers don't allow outbound traffic to SMTP port 25 for spamming reasons. Choose your provider wisely.

# TODO

* Add an SMTP redirector role
* Add a RedELK role
* Maybe automate the cloud instance creation part using Terraform