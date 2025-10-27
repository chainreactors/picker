---
title: Phish Out of Water
url: https://posts.specterops.io/phish-out-of-water-aaeb677a5af3?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-07-17
fetch_date: 2025-10-06T17:43:17.420680
---

# Phish Out of Water

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Faaeb677a5af3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fphish-out-of-water-aaeb677a5af3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fphish-out-of-water-aaeb677a5af3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-aaeb677a5af3---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-aaeb677a5af3---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

## PHISHING SCHOOL

# Phish Out of Water

## Bypassing Web Proxies so Your Phish Don’t Suffocate

[![Forrest Kasler](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*twL-x8eyh-Q1_GWn)](https://medium.com/%40fakasler?source=post_page---byline--aaeb677a5af3---------------------------------------)

[Forrest Kasler](https://medium.com/%40fakasler?source=post_page---byline--aaeb677a5af3---------------------------------------)

11 min read

·

Jul 16, 2024

--

Listen

Share

You just fought long and hard to convince a user to click on your link. They are dying to know about the contents of your macro enabled excel file. So, don’t let web proxies ruin your fun by blocking your payload! We are in the home stretch, but that doesn’t mean we get to take a victory lap just yet.

Press enter or click to view image in full size

![]()

Me, trying not to scare the phish

## The Good Ol’ Days

I remember it well. The year was 2014, and I was embarking on my first phishing expedition as a fledgling penetration tester. I fired up my Metasploit listener, minted an EXE payload with Veil, and called it ‘dresscode\_policy.doc.exe’. I sent out my emails and, in return, was blessed with a bounty of shells raining in from the deep blue internet. In those days, it seemed like there would always be phish on the table. Looking back now, I can hardly believe it was ever so easy.

## Sparse Waters

We’ve continued to overphish the same waters year after year with reckless abandon and now the phish don’t bite like they used to. The same bait doesn’t work. The same nets come up empty. We have only ourselves to blame for being so selfish (selphish?). We used EXEs like harpoons and now they are completely blocked unless they are signed. We wove nets of PowerShell until AMSI and constrained language mode cut them to ribbons. We dredged scores of users with Excel macros until Microsoft almost did away with [macros](https://techcrunch.com/2022/07/11/microsoft-office-macros-block/) entirely. We even used mark of the web bypasses to the brink of [extinction](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-zero-day-bug-exploited-to-push-malware/).

How will we ever catch a phish again?

## What’s Really Happening

I was being a bit dramatic, but I did want to make one point:

**Defenses adapt to threats and we are the threats.**

As new phishing techniques emerge, one of the most obvious defenses has always been to try to block initial access payloads based on their file type. Someone starts slinging malware in Microsoft Excel add-in ([XLL](https://blogs.blackberry.com/en/2021/12/threat-thursday-warzone-rat-breeds-a-litter-of-scriptkiddies)) files, and suddenly it makes sense for most organizations to just block these files outright. Payload types that were ‘working’ across the board just months ago tend to make too much noise and now get blocked.

We may mourn the fall of our favorite initial access payloads (R.I.P. OLE), but not all hope is lost. Let’s talk about the challenge of initial access from a high level so we can see our options more clearly. First, we’ll talk about objectives, then discuss defenses, and finally bypasses!

## Can It Run Code?

If a file type can run code, or open another application that can run code, then it can likely be used for initial access. To get a full list of potentially dangerous files, we can look at the ones blocked by default on Outlook:

<https://support.microsoft.com/en-us/office/blocked-attachments-in-outlook-434752e1-02d3-4e90-9124-8b81e49a8519>

The list is 120 entries long! And even that is not the full list, considering that Outlook still allows dangerous file types like macro enabled Office documents. Thanks to [@mrd0x](https://twitter.com/mrd0x), another good source is filesec.io:

[https://filesec.io/#](https://filesec.io/)

Use the “Double Click” filter to find file types that are particularly useful for phishing. These “Double Click” files initiate some action when clicked by a user. Often running a script or executable of some kind. That list is 77 entries long!

![]()

Dangerous Extensions

Our goal for initial access is to successfully deliver at least one of these files to the target and convince them to open/run it. Which file types are allowed will vary depending on controls in your target environment, but it is extremely unlikely that all of these file types are blocked. Often, several of these “dangerous” files are used in business processes and have exceptions applied to them. We just need to find one exception!

## The Wall

There is a wall between us and our target. It is lined with turrets that want to destroy our payload. This wall consists of the corporate proxy, the corporate firewall, and the target’s browser. Each has some visibility into what users are downloading and each will try to prevent users from inviting us into the network, but there’s a problem with their eyesight. They really only have three ways of knowing what file type is being downloaded, and we can control each one.

1. ***Extensions*** — The last characters of the file name (e.g., doc, txt, exe)
2. ***MIME Types*** — The content type we specify in our server response headers (e.g., application/msword, text/plain, application/x-msdownload)
3. ***Magic Numbers*** — The first bytes in a file (e.g., “50 4B 03 04” for .zip files or “4D 5A” for Windows executables)

Under normal circumstances, these indicators should all tell a consistent story like:

A windows executable with an extension of “exe”, AND a MIME type of “application/x-msdownload”, AND “4D 5A” (the “MZ” header) as the first two bytes.

Therefore, you could write a program to detect these dangerous files based on any single characteristic. Writing detections based on all three would be extremely redundant. I suspect many software engineers have made this very mistake. Choosing a single indicator, writing the detection logic, and thinking that would be enough. However, it’s the *contents* of the file and not its name, MIME type, or magic number that make it dangerous. Now that we have a clear view of our adversary, let’s talk about how we might slip past their watch.

## Bypasses

As I menti...