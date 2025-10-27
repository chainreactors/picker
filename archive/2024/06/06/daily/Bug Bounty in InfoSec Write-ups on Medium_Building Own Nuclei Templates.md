---
title: Building Own Nuclei Templates
url: https://infosecwriteups.com/building-own-nuclei-templates-c0e45ea7aac7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-06-06
fetch_date: 2025-10-06T16:55:53.323175
---

# Building Own Nuclei Templates

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc0e45ea7aac7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbuilding-own-nuclei-templates-c0e45ea7aac7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbuilding-own-nuclei-templates-c0e45ea7aac7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c0e45ea7aac7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c0e45ea7aac7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Building Own Nuclei Templates

[![Ott3rly](https://miro.medium.com/v2/resize:fill:64:64/1*3wMPJmhJUNOpqobsPBkS8g.jpeg)](https://ott3rly.medium.com/?source=post_page---byline--c0e45ea7aac7---------------------------------------)

[Ott3rly](https://ott3rly.medium.com/?source=post_page---byline--c0e45ea7aac7---------------------------------------)

8 min read

·

May 27, 2024

--

1

Listen

Share

It’s time to break the atoms! We will take a look at how it’s possible to create unique [nuclei](https://github.com/projectdiscovery/nuclei) templates! Don’t miss out, since I will show you 3 easy ways how you can build your own! Let’s increase your chance of raking that bounty cash! I have another article about the smart ways to use this tool itself, if you haven’t read that, feel free to check it out!

Press enter or click to view image in full size

![]()

Nuclei templates are made for testing certain vulnerabilities. Either it’s known misconfigurations, CVEs, default credentials, general fuzzing techniques, and even more! It’s a pretty powerful way to describe how you can detect the issues, and it’s also a very powerful technique to test at a mass scale. This tool comes with a lot of [templates](https://github.com/projectdiscovery/nuclei-templates/) already premade, but using them out of the box, will most likely result in duplicate findings. Using your custom templates will increase the chance of finding vulnerabilities by a lot! What if I told you that you don’t need to put a lot of effort into making your own? There is no need to read a lot of documentation when you are starting out. It’s pretty simple, once you understand the basics.

## Default Directory Structure

To make building your own templates easier, it’s just mandatory to understand the base structure. When you install nuclei, templates by default will be in your home directory. If I list them out, you will see there are multiple categories and multiple directories:

Press enter or click to view image in full size

![]()

Those directories separate templates by their use case, and the way how you run them:

* **headless** — meant for the templates for headless mode.
* **dns** — for checking DNS records mostly.
* **file** — will have various checks specified files. Because you can also pass not URLs, but files to the tool.
* **http** — just regular HTTP requests. We will spend our focus here this time since it’s just the most common way of using Nuclei.
* **javascript** — in case you want to run some JavaScript functions on the client side.
* **network** — if you have, for instance, IPs with different ports, you can do some network-based scanning.
* **ssl** — for SSL checks.

Others like **code**, **config**, **helpers**, and **workflows** are basically a bit advanced stuff!

## Structure of Templates

Templates are written in YAML, it’s a pretty simple way to describe data, mostly using key-value pairs. If we check **dns -> azure-takeover-detection.yaml** template, we will see the 3 main parts:

![]()

It’s meant for in case you only want to use that template only. You can use it with nuclei using this command:

```
nuclei -u target.com -id azure-takeover-detection
```

![]()

It will have some metadata. Some of those values are mandatory, like the **name** of the template, the **author** who made the template, the **severity** (usually by CVSS score), and the **description** but other parts are optional like **reference**, **classification,** and **metadata**.

The last part usually will be **tags**. The tags are also mandatory since this one could be used when you want to run multiple templates of certain group. For this example, the **dns** tag could be used to run the DNS templates in this directory. To run templates of specific group, you could use the following command:

```
nuclei -u target.com -tags dns
```

Press enter or click to view image in full size

![]()

Here, the **dns** will tell the nuclei how you want to send the DNS request, and the **matchers** will specify the condition when to display output to the terminal. In this case, if the DNS record contains string **69.164.223.206**.

There are other types of **part 3** structure, for example — **file**, which could be used for scanning files using nuclei like in **python-scanner.yaml** template:

Press enter or click to view image in full size

![]()

As you notice first 2 parts are the same — **id** and **info**, but the third part will be the **file**.

Even though nuclei has many options for templates, most people use it mainly for sending HTTP requests, so let’s explore HTTP-based templates. There are multiple main ways to write HTTP-based templates. Let’s explore the **phpmyadmin-misconfiguration.yaml** file:

Press enter or click to view image in full size

![]()

It’s a phpmyadmin misconfiguration template with an **id** and **info** parts which we already know, but this time you can see there is an **http** section. There are multiple ways to send HTTP requests using nuclei:

Press enter or click to view image in full size

![]()

As you can notice, you can use the **raw** keyword and specify the request as you see in Burp. This way you can also send HTTP requests using other verbs like POST, PUT, etc.

## Method #1

As we just learned the core structure of templates, now it’s time for the first method on how you can build your own. I recommend starting by just reading already premade ones and trying to do something similar. What I like to do, is split my terminal in two parts, and on the left side, I will have already made a nuclei template, and on the right side, the template that I will be building. For this case, I have selected **aem-xss-childrenlist-xss.yaml** file as an example:

Press enter or click to view image in full size

![]()

On the right side, I have opened a new file using the nano editor called the same name as the template on the right. I have created it on **~/nuclei-templates-cust/** directory.

The first step using this approach is j...