---
title: Recon on Steroids — Discover EVEN MORE Subdomains
url: https://infosecwriteups.com/recon-on-steroids-discover-even-more-subdomains-b6967c3fc33b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-11
fetch_date: 2025-10-06T17:16:24.612733
---

# Recon on Steroids — Discover EVEN MORE Subdomains

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb6967c3fc33b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-on-steroids-discover-even-more-subdomains-b6967c3fc33b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-on-steroids-discover-even-more-subdomains-b6967c3fc33b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b6967c3fc33b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b6967c3fc33b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Recon on Steroids — Discover EVEN MORE Subdomains

[![Ott3rly](https://miro.medium.com/v2/resize:fill:64:64/1*3wMPJmhJUNOpqobsPBkS8g.jpeg)](https://ott3rly.medium.com/?source=post_page---byline--b6967c3fc33b---------------------------------------)

[Ott3rly](https://ott3rly.medium.com/?source=post_page---byline--b6967c3fc33b---------------------------------------)

5 min read

·

Apr 29, 2024

--

Listen

Share

Won’t you love to find the website or asset that nobody else has found, test it, and find some serious vulnerability that will result in a big fat paycheck? Yes, it is possible! If you’re thinking outside the box! The big programs, which have “all our assets in scope”, “everything that they own in scope” or something similar mentioned in their policy, could unlock the path to finding untested areas. I will show my own unique methods to discover more core subdomains. This will probably even surprise the program managers when they realize that you have found an asset they have no idea that they own.

Watch this video in case you are too lazy to read :)

## Main Website Recon

If you saw some of my videos from the [recon playlist](https://www.youtube.com/watch?v=gG-WzTD_Mg8&list=PLYR5SjLcHUs7cD5go5QJ6teVCZy6qx_5N), you know that I show most of my examples of the [Coca-Cola company](https://app.intigriti.com/researcher/programs/tccc/coca-cola/detail). I usually prepare a list of root domains in the **wildcards.txt** file. Let’s try populating this file.

The first thing that I gonna show you, is just doing simply stupid recon — just going to the main website called **coca-cola.com**. In their vulnerability disclosure policy, they mentioned that all the brands of this company are basically in the scope. In this case, the first thing you should always do before even doing something intensive — is to go to the main website and try to write down as many brands as possible that they own. For example, **sprite.com**, **fanta.com**, and many others might be included since these brands do belong to them:

Press enter or click to view image in full size

![]()

Of course, you have to verify those domains by just simply googling them. Just place terms like “Sprite” or “Fanta” in the search bar, and even more core domains with different TLDs will start appearing.

## Certificate Recon

The next way to get core subdomains is by checking the certificate websites. I like to use [crt.sh](https://crt.sh/), passing the company organization name there. To get the company name, you can use Wikipedia, Crunchbase, or the simplest way — just by going to the footer and copying the company name:

Press enter or click to view image in full size

![]()

Let’s use “The Coca-Cola Company” to paste it to the **crt.sh**:

![]()

You always want to validate those domains because sometimes there will be cases when the domain was working 10 years ago and it was part of the company, but after a while, it stopped working, it could have been purchased by another company or just the domain was not used, stopped working or other person created the similar website or similar brand and used that domain name. So always validate the collected subdomains!

Additionally, what you can do is add **&output=json** to the end of the URL query and copy it to the terminal for further filtering. Use the curl command with [jq](https://jqlang.github.io/jq/) to do some magic:

```
curl -s 'https://crt.sh/?q=%22The+Coca-Cola+Company%22&output=json' | jq '.[] | .common_name' -r | sort -u
```

The **jq** tool will filter out common names of certificates in the **crt.sh** website. The **-r** flag will show only the raw output and **sort -u** will leave unique results. There will be a lot of results but you will only need the core top-level domains. I suggest filtering them out using manual inspection and of course, validating them by going to the site directly or quickly running [subfinder](https://github.com/projectdiscovery/subfinder) to check their subdomains.

## Google Recon

Another way is just searching on Google by the footer. This time I suggest using an almost full footer string like “© The Coca-Cola Company. All rights reserved.” and paste it on the search bar:

![]()

If you noticed, I have removed the year. It is a good idea to do this since it will also include some results of older websites that were updated a long time ago.

## Shodan Search Engine

One more way is just using [Shodan](https://www.shodan.io/). Try to specify the company name using this dork:

```
org:"The Coca-Cola Company"
```

You might want to replace it with your target company name and look for the hostnames. The Shodan usually includes them along with IP information. It’s another good area to collect root domains but as always, you have to double-check them first.

## Fofa Search Engine

So the last one is one of my favorites — using [fofa](https://en.fofa.info/) search engine, using favicons. Firstly, let’s try to search by the company name here in the quotes:

Press enter or click to view image in full size

![]()

Next, you want to click on more and select the favicons that resemble the main logo of the company. In this case, it will be either a bottle or it could be Coca-Cola’s name.

Press enter or click to view image in full size

![]()

Once again, like on Shodan, you will get a bunch of results that might have many hostnames to add to your list. Another tip is to use those favicon hashes that appear in the Fofa search bar for Shodan search. I have already mentioned this in my previous [article](https://medium.com/bugbountywriteup/mastering-shodan-search-engine-8c80b80dae09) about Shodan Dorking, so make sure to check that out!

## Last Things

There might be even more ways to get some wildcard domains but those there are my favorites that I personally use. You have to use your imagination, think outside the box, and research current recon tools to get ahead in this Bug Bounty Game.

If you find this information u...