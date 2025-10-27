---
title: Swagger XSS Mass Hunting
url: https://infosecwriteups.com/swagger-xss-mass-hunting-b7a19e23cfd9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-01
fetch_date: 2025-10-06T17:00:12.414595
---

# Swagger XSS Mass Hunting

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb7a19e23cfd9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fswagger-xss-mass-hunting-b7a19e23cfd9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fswagger-xss-mass-hunting-b7a19e23cfd9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b7a19e23cfd9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b7a19e23cfd9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Swagger XSS Mass Hunting

[![YoungVanda](https://miro.medium.com/v2/resize:fill:64:64/1*xJCKzxgEb-2Ao40zUAJY9Q.jpeg)](https://youngvanda.medium.com/?source=post_page---byline--b7a19e23cfd9---------------------------------------)

[YoungVanda](https://youngvanda.medium.com/?source=post_page---byline--b7a19e23cfd9---------------------------------------)

2 min read

·

Jul 29, 2023

--

5

Listen

Share

***In the name of Allah***

Hi guys, I’m YoungVanda and in this write-up, I’m gonna explain my own approach towards Swagger XSS and why I don’t use the Nuclei template ( swagger-api.yaml) ;d

Press enter or click to view image in full size

![]()

### The Entire Flow

```
1. Find as many subdomains as possible
2. cat all_subs.txt | dnsx | tee -a resolved_ones.txt
3. cat resolved_ones.txt | httpx | tee -a alive_ones.txt
4. ffuf -w /root/wordlist/api/swagger_xss.txt:FUZZ -w alive_ones.txt:URL -u URLFUZZ -mc 200 -o ffuf-result.txt
5. cat ffuf-result.txt | jq -r .results[].url | tee -a feed_me_to_httpx.txt
6. cat feed_me_to_httpx.txt | httpx -silent -title | tee -a title.txt
7. cat title.txt | grep "Swagger UI"
```

### First Step

Find as many subdomains as possible you can get help from Chaos.

### Second Step

Now it’s time to resolve subdomains. If you get false positive, use ShuffleDNS with -d and -l options.

### Third Step

After resolving them, we need to find alive subdomains. You can add
User-Agent, Time Delay and etc

### Fourth Step

Now we are ready to fuzz for Swagger UI endpoints.

```
ffuf -w /root/wordlist/api/swagger_xss.txt:FUZZ -w alive_ones.txt:URL -u URLFUZZ -mc 200 -o ffuf-result.txt
```

### Fifth Step

Extracting found URLs from ffuf result.

```
cat ffuf-result.txt | jq -r .results[].url | tee -a feed_me_to_httpx.txt
```

### Sixth Step

Now, we use httpx with -title to get the title of fuzzed and possible endpoints for Swagger UI.

```
cat feed_me_to_httpx.txt | httpx -silent -title | tee -a title.txt
```

### Seventh Step

```
cat title.txt | grep "Swagger UI"
```

### Why Not Nuclei (swagger-api.yaml) ?

1. In this methodology wordlist is so important and what I realised is that the wordlists inside this template is not enogh.
2. We’re looking for Swagger UI not API paths. We should be aware of our wordlist so this way you can reduce the extra traffics. I mean you should remove endpoints like this:
   \* /swagger-ui.js
   \* /swagger-ui.yaml
   \* /swagger-ui.json
   Because you looking for Swagger UI, which under a certain version is vulnerable to XSS, not API path. But if you’re looking for API path that’s a different thing.

### Best Approach

I think the best approach would be fixing above-mentioned problems and code your own private nuclei template. Even though, my methodology worked fine so far, I was able to find multiple VDP bugs, and you can use it if you’re not into coding templates, but it takes lots of time and energy, also you have to send lots of requests. Therefore, I tried to explain my previous methodology and the reason why I don’t use default Nuclei template in this regard so you guys can think and get the idea or maybe you can come up with a better methodology.

### Update

Check out this post. I talked about my recent RDP finding and some more useful tips:
<https://twitter.com/young_vanda_/status/1700590035282587861>

My Twitter Account: [@young\_vanda\_](https://twitter.com/young_vanda_)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b7a19e23cfd9---------------------------------------)

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b7a19e23cfd9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b7a19e23cfd9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b7a19e23cfd9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b7a19e23cfd9---------------------------------------)

·[Last published 1 hour ago](/baby-dfc2547dc387?source=post_page---post_publication_info--b7a19e23cfd9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![YoungVanda](https://miro.medium.com/v2/resize:fill:96:96/1*xJCKzxgEb-2Ao40zUAJY9Q.jpeg)](https://youngvanda.medium.com/?source=post_page---post_author_info--b7a19e23cfd9---------------------------------------)

[![YoungVanda](https://miro.medium.com/v2/resize:fill:128:128/1*xJCKzxgEb-2Ao40zUAJY9Q.jpeg)](https://youngvanda.medium.com/?source=post_page---post_author_info--b7a19e23cfd9---------------------------------------)

[## Written by YoungVanda](https://youngvanda.medium.com/?source=post_page---post_author_info--b7a19e23cfd9---------------------------------------)

[300 followers](https://youngvanda.medium.com/followers?source=post_page---post_author_info--b7a19e23cfd9---------------------------------------)

·[1 following](https://medium.com/%40youngvanda/following?source=post_page---post_author_info--b7a19e23cfd9---------------------------------------)

bug hunter, used to be a professional chess player, now an amateur boxer

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b7a19e23cfd9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b7a19e23cfd9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b7a19e23cfd9-----------------------...