---
title: Ehxb | Path Traversal Vulnerabilities
url: https://infosecwriteups.com/ehxb-path-traversal-vulnerabilities-from-discovery-to-automation-569b64ce46ac?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-03
fetch_date: 2025-11-04T03:09:42.553937
---

# Ehxb | Path Traversal Vulnerabilities

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F569b64ce46ac&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fehxb-path-traversal-vulnerabilities-from-discovery-to-automation-569b64ce46ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fehxb-path-traversal-vulnerabilities-from-discovery-to-automation-569b64ce46ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40Ehxb)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-569b64ce46ac---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-569b64ce46ac---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Ehxb | Path Traversal Vulnerabilities

[![Ehxb](https://miro.medium.com/v2/resize:fill:64:64/1*9wV9KGuFnX3qaHOsqutwUg.png)](https://ehxb.medium.com/?source=post_page---byline--569b64ce46ac---------------------------------------)

[Ehxb](https://ehxb.medium.com/?source=post_page---byline--569b64ce46ac---------------------------------------)

8 min read

·

Oct 9, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

When I first started learning about web security, **path traversal** was one of those vulnerabilities that seemed almost too simple to be real. How could something as basic as manipulating a filename cause such serious damage? But after spending hours in the lab and testing real applications, I realized that simplicity is often what makes it so dangerous. Developers overlook it, filters fail to catch it, and before you know it, an attacker is reading your server’s most sensitive files.

In this post, I’ll walk you through what path traversal is, where to find it, how to test it with five different bypass techniques, and finally, how to automate your testing using Python. Let’s dive in.

### What is Path Traversal?

Path traversal, also known as directory traversal, is a vulnerability that allows attackers to access files and directories stored outside the web root folder. By manipulating file path references, an attacker can navigate through the server’s directory structure and read arbitrary files.

The most common target? The **/etc/passwd** file on **Linux** systems. It’s a standard file that contains user account information, and it’s the perfect proof of concept because it’s readable by any user and confirms you’ve successfully traversed the directory structure.

The impact can range from information disclosure (**source code**, **configuration files**, **credentials**) to complete server compromise if the attacker can write files or access sensitive application logic.

### Where Do We Find Path Traversal?

**Path traversal** vulnerabilities typically appear in features that handle file operations. Here are the most common places to look:

> **Image loaders**: Applications that display images based on a filename parameter (like product images, avatars, or gallery viewers).
>
> **File download features**: Any endpoint that lets users download files by specifying a filename or path.
>
> **Document viewers**: PDF viewers, report generators, or any feature that loads documents dynamically.
>
> **Template engines**: Systems that load templates based on user input.
>
> **File upload handlers**: Sometimes the filename itself can be manipulated during upload.
>
> **Include/require statements**: Especially in older PHP applications where user input is passed to include() or require().

The key is to look for any parameter that seems to reference a file: filename, file, path, template, page, document, or even custom parameter names like img, doc, or resource.

## Testing Path Traversal: 5 Real-World Scenarios

Now let’s get practical. I’m going to show you five different scenarios I encountered while practicing in **PortSwigger’s** Web Security Academy labs. Each one represents a different defense mechanism and how to bypass it.

### Scenario 1: The Simple Case

The first scenario is the most straightforward. The application takes a filename parameter and directly uses it to load an image. No filters, no validation, just pure trust in user input.

The vulnerable request looks like this:

```
GET /image?filename=product.jpg
```

Press enter or click to view image in full size

![]()

To exploit it, I simply replaced the filename with a path traversal sequence:

```
GET /image?filename=../../../etc/passwd
```

Press enter or click to view image in full size

![]()

The ../ tells the server to go up one directory. By chaining three of them together, I navigated from the images directory, through the web root, and into the system’s /etc directory.

How I found it: I intercepted the image request in Burp Suite, noticed the filename parameter, and immediately tested it with the classic traversal payload. The response came back with the full contents of /etc/passwd. No resistance at all.

### Scenario 2: Absolute Path Bypass

The second scenario was trickier. The application blocked traversal sequences like ../ entirely. Any attempt to use them resulted in an error or the request being rejected.

But here’s the thing: if the application blocks relative paths, what about absolute paths?

Instead of trying to navigate up directories, I just told the server exactly where to go:

```
GET /image?filename=/etc/passwd
```

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

And it worked. The application was so focused on blocking ../ that it forgot to validate absolute paths.

How I found it: After my initial ../ payload was blocked, I tried different variations. When I used the absolute path /etc/passwd, the application happily served the file. This taught me that filters are often incomplete they block one thing but forget about another.

### Scenario 3: Non-Recursive Stripping

The third scenario had a filter that stripped out ../ sequences from the input. At first glance, this seems like a solid defense. But the filter had a fatal flaw: it only ran once.

Here’s what I mean. If I sent ../../../etc/passwd, the filter would remove the ../ sequences, leaving me with etc/passwd, which wouldn’t work.

But what if I nested the sequences? What if I sent ….// instead of ../?

When the filter removes ../ from …./, it leaves behind ../ again. So my payload became:

```
GET /image?filename=….//….//….//etc/passwd
```

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

Press enter or click to view imag...