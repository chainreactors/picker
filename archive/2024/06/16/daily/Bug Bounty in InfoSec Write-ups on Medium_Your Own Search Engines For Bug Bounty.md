---
title: Your Own Search Engines For Bug Bounty
url: https://infosecwriteups.com/your-own-search-engines-for-bug-bounty-773845aa4e6a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-06-16
fetch_date: 2025-10-06T16:54:44.970326
---

# Your Own Search Engines For Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F773845aa4e6a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyour-own-search-engines-for-bug-bounty-773845aa4e6a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyour-own-search-engines-for-bug-bounty-773845aa4e6a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-773845aa4e6a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-773845aa4e6a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Your Own Search Engines For Bug Bounty

[![Ott3rly](https://miro.medium.com/v2/resize:fill:64:64/1*3wMPJmhJUNOpqobsPBkS8g.jpeg)](https://ott3rly.medium.com/?source=post_page---byline--773845aa4e6a---------------------------------------)

[Ott3rly](https://ott3rly.medium.com/?source=post_page---byline--773845aa4e6a---------------------------------------)

4 min read

·

Jun 3, 2024

--

6

Listen

Share

Press enter or click to view image in full size

![]()

Using Google and Bing Dorking could get leads for pretty big bounties! Do you know you can customize those search engines only to show you the bug bounty targets? Let’s explore the way how you can set up custom search engines.

## Programmable Search Engine by Google

The first custom search that you could use is a [programmable search engine](https://programmablesearchengine.google.com/) by Google. You could create a search field that would only show your specified websites. It’s pretty useful for bug bounties. If you never used this tool and tried to access it directly — you will see a view like this:

Press enter or click to view image in full size

![]()

Let’s click on “add” to start and name the search engine. I will mine the **Bug Bounty Targets**:

Press enter or click to view image in full size

![]()

When you are creating it the first time, I only recommend adding one wildcard domain:

![]()

For search settings, I do not select anything, since you don’t need the image search and safe search — would only limit your results. Lastly, what’s left to do is just fill in CAPTCHA and press “Create”:

![]()

I only fill one target since it’s more convenient to use a custom search engine in edit mode. Next, let’s click on “Customize”:

![]()

Now we are in the edit mode… If you click on “Add” near the sites to search, it will be more convenient right now:

![]()

What I recommend you to do, is just add as many targets as possible. I suggest you use the [BBSCOPE](https://github.com/sw33tLie/bbscope) tool as it could help you to gather a lot of wildcard domains even from private programs. I also recommend adding in chunks of like 50, because if you try to add a lot of targets at once — this search engine could crash:

![]()

After adding your targets, you could use a public URL of your search engine:

![]()

![]()

This search bar will be only applicable to your specified websites. It’s pretty much convenient just to do like simple search on that website. For example, if you are looking for API endpoints, you could just write down “api” or maybe you are looking for admin endpoints… Keep in mind that you cannot do the same as regular or Google Dorking.

## Bing Custom Search

My second favorite custom search engine is [Bing Custom Search](https://www.customsearch.ai/). It is useful if you are going after two to three large programs since it does have some limitations, unlike Google. It has a limit of 100 targets, so I suggest only using this on high bounty-paying programs. Let’s click on “get started”:

![]()

You will be prompted to log in with your Microsoft account. After that, you will see this page, if you are accessing it first time:

![]()

Click on “create new instance”. Give it a name like “S-Tier targets” and click “okay”:

Press enter or click to view image in full size

![]()

Wait until it loads and then you can start adding your URLs. I will use **fisglobal** as the example and make sure your check “includes sub pages” and click on the plus symbol:

![]()

After adding the first website, you can really add more targets by *Type in a URL* (up to 100):

![]()

You can use the right side of the screen to search “API” endpoints:

Press enter or click to view image in full size

![]()

## Last Thoughts

We have looked into two custom search engines. Even though it’s not the same as regular Dorking, you can still apply this to filter out some assets.

If you find this information useful, please share this article on your social media, I will greatly appreciate it! I am active on [Twitter](https://ott3rly.com/twitter), check out some content I post there daily! If you are interested in video content, check my [YouTube](https://ott3rly.com/youtube). Also, if you want to reach me personally, you can visit my [Discord](https://ott3rly.com/discord) server. Cheers!

*Originally published at* [*https://ott3rly.com*](https://ott3rly.com/your-own-search-engines-for-bug-bounty/) *on June 3, 2024.*

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----773845aa4e6a---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----773845aa4e6a---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----773845aa4e6a---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----773845aa4e6a---------------------------------------)

[Information Technology](https://medium.com/tag/information-technology?source=post_page-----773845aa4e6a---------------------------------------)

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--773845aa4e6a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--773845aa4e6a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--773845aa4e6a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--773845aa4e6a---------------------------------------)

·[Last published 1 hour ago](/baby-dfc2547dc387?source=post_page---post_publication_info--773845aa4e6a---------------------------------------)

A c...