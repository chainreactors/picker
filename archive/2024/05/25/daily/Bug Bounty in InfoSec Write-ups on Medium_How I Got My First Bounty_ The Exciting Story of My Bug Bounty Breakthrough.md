---
title: How I Got My First Bounty: The Exciting Story of My Bug Bounty Breakthrough
url: https://infosecwriteups.com/how-i-got-my-first-bounty-the-exciting-story-of-my-bug-bounty-breakthrough-d8391973ed41?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-25
fetch_date: 2025-10-06T17:17:31.773437
---

# How I Got My First Bounty: The Exciting Story of My Bug Bounty Breakthrough

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd8391973ed41&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-my-first-bounty-the-exciting-story-of-my-bug-bounty-breakthrough-d8391973ed41&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-my-first-bounty-the-exciting-story-of-my-bug-bounty-breakthrough-d8391973ed41&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d8391973ed41---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d8391973ed41---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Got My First Bounty: The Exciting Story of My Bug Bounty Breakthrough

[![whit3ros3](https://miro.medium.com/v2/resize:fill:64:64/1*2J9Dr5hsmPXG3IuVU4C3VA.jpeg)](https://medium.com/%40jay_rana?source=post_page---byline--d8391973ed41---------------------------------------)

[whit3ros3](https://medium.com/%40jay_rana?source=post_page---byline--d8391973ed41---------------------------------------)

6 min read

·

May 15, 2024

--

6

Listen

Share

Press enter or click to view image in full size

![]()

Long time no see! I’ve been a bit preoccupied with other tasks besides bug bounty hunting, so I haven’t had the chance to post any blogs. But setting all that aside, today I want to share how I achieved every beginner bug hunter’s dream: scoring that first bounty. Still gives me chills just thinking about it!

So, without further ado, let’s dive into the details of this exhilarating experience.

**Let’s get Started**

The most important takeaway from this blog is simple:

*Keep learning about different vulnerabilities and, more importantly, put that newly gained knowledge into practice. There are hundreds and thousands of websites out there waiting to be hunted, with millions of vulnerabilities just waiting to be discovered by someone.*

**Further Details**

Here’s how it all went down. The bug that landed me my first bounty was actually a combination of two bugs:

> *GraphQL API key leak & cache poisoning.*

The target? A private one I stumbled upon using some good ol’ Google dorking. (Psst, here’s a handy [repo](https://github.com/sushiwushi/bug-bounty-dorks) for some similar Google Dorks.)

**Exploration**

The scope of my program was massive, which was great because it meant more things to poke at. I started by hunting down the main domain and, as some of you might know from my previous blogs, I have a thing for starting with finding JavaScript files — they’re like treasure chests sometimes, just sitting there with API keys waiting to be exploited.
So, I ran my trusty one-liner commands to extract those JS files and extract the API keys in them, one after the other.

```
cat domains.txt | waybackurls | grep '.js' | httpx -mc 200 >> js.txt
```

```
nuclei -l js.txt -t /home/kali/.local/nuclei-templates/http/exposures -o potential_secrets.txt
```

(Hey you!! Confused about where these commands came from? Check out my [last blog](https://medium.com/bugbountywriteup/critical-bug-alert-how-i-hacked-into-a-companys-database-287fa27c8339).)

While these were running in the background, I used the ‘[dirb](https://www.kali.org/tools/dirb/)’ tool to discover all directories related to the target.

**A ray of light**

After letting both processes run overnight, I woke up to some promising results. [Nuclei](https://www.kali.org/tools/nuclei/) didn’t disappoint, flagging a JS file containing a GraphQL API key. To verify, I opened the JS file and found this:

Press enter or click to view image in full size

![]()

And dirb did its job too, giving out a bunch of URLs but one which quickly grabbed my eye after finding that API key

> https://www.redacted.com/graphql

Lesgooooooo!!!

But then came the moment of truth: “You don’t know squat about GraphQL, bro.” Just this line kept running through my mind.

**Collecting the arsenal**

So, Determined to overcome this hurdle, I immersed myself in learning about it. Shoutout to [PortSwigger Academy](https://portswigger.net/web-security) — that place is gold for learning about vulnerabilities, my go-to resource for mastering vulnerabilities.
So, my next couple of days went solely into researching, learning, and collecting all my arsenal against this new enemy of mine.

So, I stumbled upon something called an introspection query, which basically lets you peek into the GraphQL schema. It’s like a special query that clients can use to ask a GraphQL service about its structure. With this query, you can get info about types, fields, directives, and more.
(Psst, wanna know more about it?? [Here you go](https://payatu.com/blog/graphql-exploitation-part-1/).)

Press enter or click to view image in full size

![]()

Result of introspection query

But let me tell you, when I first got this response from using the query, it was a bit overwhelming. It just kept going and going, and as a newbie to GraphQL, it was like trying to make sense of a maze.

Then came the lifesaver: the “[InQL Burp extension](https://portswigger.net/bappstore/296e9a0730384be4b2fffef7b4e19b1f).” It helped me visualize the schema in a way that even a total beginner like me could understand. All I had to do was copy-paste that chaotic response into a text file and feed it to the extension, and bam! Everything suddenly became much clearer. Easy peasy, right?

![]()

**Exploring the Schema**

After using the InQL Burp extension, I got a beautifully visualized version of the GraphQL schema, all nicely structured and organized. It was a relief to see everything laid out so clearly.

Then, it hit me: I remembered finding two API keys in the JavaScript file.😈

So, here I had the schemas for both of these keys. But wait a sec… the schema from the private key had two extra queries: “tags” and “users”.

![]()

First, I checked out the “tags” info, but nothing interesting popped up there. Then, it was time to dig into the “users” field. Fingers crossed, I used some queries to see what this “users” field was all about.

And guess what? Voilà!

Press enter or click to view image in full size

![]()

Got the data of different users, and let me tell you, it was like hitting the jackpot!

**The Unexpected Twist**

I was all set with all the data in hand, ready to start writing up my report. Description, check. Steps to reproduce, check. And then, it was time for the POC (Proof of Concept).
So, I started sending different Burp requests to take screenshots, something caught my attention! After a few requests, I realized that I...