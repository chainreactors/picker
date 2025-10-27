---
title: Unauthorized Access To Admin Panel via Swagger
url: https://infosecwriteups.com/unauthorized-access-to-admin-panel-via-swagger-c242e8341045?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-24
fetch_date: 2025-10-04T10:28:52.351731
---

# Unauthorized Access To Admin Panel via Swagger

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc242e8341045&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthorized-access-to-admin-panel-via-swagger-c242e8341045&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funauthorized-access-to-admin-panel-via-swagger-c242e8341045&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c242e8341045---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c242e8341045---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unauthorized Access To Admin Panel via Swagger

[![M7arm4n](https://miro.medium.com/v2/resize:fill:64:64/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---byline--c242e8341045---------------------------------------)

[M7arm4n](https://m7arm4n.medium.com/?source=post_page---byline--c242e8341045---------------------------------------)

3 min read

·

Mar 4, 2023

--

Listen

Share

Hi guys, My name is Arman and you know me as [M7arm4n](https://twitter.com/M7arm4n). Today I want to talk about how I was able to access the admin panel in Coca-Cola for the 2022 World Cup 🏆

![https://bugcrowd.com/coca-cola]()

<https://bugcrowd.com/coca-cola>

The essential part of discovering this vulnerability is continuous RECON, about 1 month before Hunting on this program, I decided to test my private recon tool. So I fired my recon tool on Coca-Cola domains, My tools do subdomain enumeration daily and push results into the database.

After around one month continues recon, Now time to check the results. Around 20/30 subdomains were added during the last month. Before starting deep hunting, I decided to try a mass scan on all new results.

Fuzzing directories of subdomains for sensitive information is one of the most popular methods, but the PowerPoint of this method is your wordlist.

I recommend you build your own wordlist from GitHub and write-ups, even CVEs. Onetime for a hack-the-box machine, faced to a WordPress website whiteout any features. I immediately fuzzed the website with a special wordlist for the WordPress website. As soon as possible I found this endpoint that leads to Local File Inclusion :D

```
wp-admin/admin-ajax.php?action=duplicator_download&file=..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd
```

So, Back to our story. I usually do my fuzz with [FFUF](https://github.com/ffuf/ffuf), I recommend you most of the time fuzzing websites one by one, Anyway in this case I did it all in one :) with the following [command](https://twitter.com/remonsec/status/1441617313250172930):

```
ffuf -w wordlist.txt:FUZZ -w subdomain.txt:URL -u URLFUZZ -ac -of csv -o result.txt
```

And for check the result:

```
cat result.txt | awk -F ',' '{print $3}'
```

Sometimes the rush of programmers in developing websites to present to the employer makes them forget to consider and implement basic security protocols during development. In this scenario, the programmer was developing a website for the 2022 World Cup, which was a blog model website so that normal users did not have the ability to log in or create an account, and there was only one admin role.

The admin directory was available at **/admin**, after some tests like directory/file brute force, to try to find the registering endpoint, SQL and LDAP bypass, etc method. I didn’t find anything. Actually, I was sad but I don’t know why I had a kind of feeling that said to me you were able to access the admin panel:)

During the testing admin panel, the fuzzing process was finished as well. I back to the results and figure out I have another important endpoint to check for this website and that was an API Swagger. I immediately open the endpoint and checked functions, all the functions and features were available without authentication and all these are for admin 😍

Press enter or click to view image in full size

![]()

The main login admin panel was safe but I think the programmer was updating the API admin panel and was using Swagger for his tests, but he forgot to define authentication for Swagger. Now we have bypassed the admin panel :))

Thank you for following me here, Don’t forget to follow for more write-ups.

<https://twitter.com/M7arm4n>

[Infosec](https://medium.com/tag/infosec?source=post_page-----c242e8341045---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----c242e8341045---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----c242e8341045---------------------------------------)

[Admin Panel](https://medium.com/tag/admin-panel?source=post_page-----c242e8341045---------------------------------------)

[Bugs](https://medium.com/tag/bugs?source=post_page-----c242e8341045---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c242e8341045---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c242e8341045---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c242e8341045---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c242e8341045---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--c242e8341045---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![M7arm4n](https://miro.medium.com/v2/resize:fill:96:96/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---post_author_info--c242e8341045---------------------------------------)

[![M7arm4n](https://miro.medium.com/v2/resize:fill:128:128/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---post_author_info--c242e8341045---------------------------------------)

[## Written by M7arm4n](https://m7arm4n.medium.com/?source=po...