---
title: Escalating a Blind Upload to RCE via Path Traversal into Cron and DNS-Restricted Callback Bypass
url: https://infosecwriteups.com/escalating-a-blind-upload-to-rce-via-path-traversal-into-cron-and-dns-restricted-callback-bypass-0f63db01be92?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-14
fetch_date: 2026-08-15T02:47:42.283086
---

# Escalating a Blind Upload to RCE via Path Traversal into Cron and DNS-Restricted Callback Bypass

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fescalating-a-blind-upload-to-rce-via-path-traversal-into-cron-and-dns-restricted-callback-bypass-0f63db01be92&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fescalating-a-blind-upload-to-rce-via-path-traversal-into-cron-and-dns-restricted-callback-bypass-0f63db01be92&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0f63db01be92---------------------------------------)

·

1. [1. Introduction](/?source=post_page-----0f63db01be92---------------------------------------#88d8 "1. Introduction")
2. [2. The Upload](/?source=post_page-----0f63db01be92---------------------------------------#52d6 "2. The Upload")
3. [2.1 The directory field enters the path unchanged](/?source=post_page-----0f63db01be92---------------------------------------#11ef "2.1 The directory field enters the path unchanged")
4. [2.2 Proving that the write is real](/?source=post_page-----0f63db01be92---------------------------------------#6e7a "2.2 Proving that the write is real")
5. [3. Reading the Filesystem Through an Endpoint That Only Writes](/?source=post_page-----0f63db01be92---------------------------------------#5c9b "3. Reading the Filesystem Through an Endpoint That Only Writes")
6. [3.1 Fingerprinting the host](/?source=post_page-----0f63db01be92---------------------------------------#f06b "3.1 Fingerprinting the host")
7. [4. Cron Reads a Directory, Not a Filename](/?source=post_page-----0f63db01be92---------------------------------------#0ffd "4. Cron Reads a Directory, Not a Filename")
8. [4.1 Planting a benign, self-removing crontab](/?source=post_page-----0f63db01be92---------------------------------------#8cb6 "4.1 Planting a benign, self-removing crontab")
9. [4.2 Reading command output through a filename](/?source=post_page-----0f63db01be92---------------------------------------#e261 "4.2 Reading command output through a filename")
10. [4.3 Confirming it over the network](/?source=post_page-----0f63db01be92---------------------------------------#5a0f "4.3 Confirming it over the network")
11. [5. Detail of The Chain in One Script](/?source=post_page-----0f63db01be92---------------------------------------#778e "5. Detail of The Chain in One Script")
12. [6. Defense](/?source=post_page-----0f63db01be92---------------------------------------#3a8a "6. Defense")
    1. [Never construct a filesystem path from raw request input](/?source=post_page-----0f63db01be92---------------------------------------#d266 "Never construct a filesystem path from raw request input")
    2. [Require authentication and authorization](/?source=post_page-----0f63db01be92---------------------------------------#adea "Require authentication and authorization")
    3. [Run the service as an unprivileged account](/?source=post_page-----0f63db01be92---------------------------------------#4aa7 "Run the service as an unprivileged account")
    4. [Isolate uploaded files](/?source=post_page-----0f63db01be92---------------------------------------#af02 "Isolate uploaded files")
    5. [Avoid exposing a filesystem-state oracle](/?source=post_page-----0f63db01be92---------------------------------------#305d "Avoid exposing a filesystem-state oracle")
13. [7. Closing Notes](/?source=post_page-----0f63db01be92---------------------------------------#b86f "7. Closing Notes")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0f63db01be92---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Rce

Bug Bounty

Bug Bounty Tips

Bug Bounty Writeup

Bugs

# Escalating a Blind Upload to RCE via Path Traversal into Cron and DNS-Restricted Callback Bypass

[![Alvin Ferdiansyah](https://miro.medium.com/v2/resize:fill:64:64/1*jCQW4Dcioim59s1E0JwOqQ@2x.jpeg)](https://alvinferd.medium.com/?source=post_page---byline--0f63db01be92---------------------------------------)

[Alvin Ferdiansyah](https://alvinferd.medium.com/?source=post_page---byline--0f63db01be92---------------------------------------)

13 min read

·

Aug 2, 2026

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D0f63db01be92&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fescalating-a-blind-upload-to-rce-via-path-traversal-into-cron-and-dns-restricted-callback-bypass-0f63db01be92&source=---header_actions--0f63db01be92---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

RCE Proof

## 1. Introduction

I found an unauthenticated file upload on one of bug bounty target website. The endpoint accepted a file and a caller-controlled destination directory, allowing the write to escape the intended upload folder and reach sensitive locations on the underlying server.

At first, the finding looked close to remote code execution. I controlled the file contents and i could influence where the file was stored, But the usual file-upload exploitation path **was unavailable.**

The server replaced every uploaded filename with **a generated UUID and forced a** `.png` **extension**. I could not preserve `.php`, `.jsp`, or any other executable suffix. **The returned upload URL was also inaccessible without authentication**, and the frontend web server appeared to serve files from a different filesystem location than the backend used for storage.

There was no download function, no local file inclusion, and no error message that exposed the uploaded contents. I could write bytes to the server, but I could neither choose their final name nor retrieve them afterward.

That created three problems:

1. Was the traversal reaching the host’s real filesystem, or only an application-controlled storage layer?
2. What privileges did the backend have when it performed the write?
3. Could a file become executable without controlling its filename or requesting it through the web server?

Instead of asking how to make the application execute the file, I began looking for another component on the host that might discover and process it automatically.

This article follows that progression: proving that the write reached the real filesystem, turning directory-creation failures into a blind filesystem oracle, and determining whether an upload with no controllable filename or read-back path could still be escalated into code execution.

## 2. The Upload

## 2.1 The directory field enters the path unchanged

The endpoint accepted a multipart file and a form field naming the destination directory. It required no account, session cookie, bearer toke...