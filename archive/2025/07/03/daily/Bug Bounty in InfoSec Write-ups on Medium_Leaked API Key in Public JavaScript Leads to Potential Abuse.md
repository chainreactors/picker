---
title: Leaked API Key in Public JavaScript Leads to Potential Abuse
url: https://infosecwriteups.com/leaked-api-key-in-public-javascript-leads-to-potential-abuse-e2f255ee0ee5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-03
fetch_date: 2025-10-06T23:50:27.996233
---

# Leaked API Key in Public JavaScript Leads to Potential Abuse

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe2f255ee0ee5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fleaked-api-key-in-public-javascript-leads-to-potential-abuse-e2f255ee0ee5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fleaked-api-key-in-public-javascript-leads-to-potential-abuse-e2f255ee0ee5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e2f255ee0ee5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e2f255ee0ee5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Leaked API Key in Public JavaScript Leads to Potential Abuse

[![127.0.0.1](https://miro.medium.com/v2/resize:fill:64:64/1*OpnEGtDWv2MkGt3n7HAPkA.jpeg)](https://medium.com/%40aashifm?source=post_page---byline--e2f255ee0ee5---------------------------------------)

[127.0.0.1](https://medium.com/%40aashifm?source=post_page---byline--e2f255ee0ee5---------------------------------------)

3 min read

·

Jun 29, 2025

--

3

Listen

Share

On a typical late-night recon session—just me, my terminal, and a cup of coffee—I was passively scanning a few assets on **domain.com**, a target participating in a public bug bounty program.

Press enter or click to view image in full size

![]()

I wasn’t expecting much at first, just running through my usual checklist: **subdomain enumeration, JS file discovery, parameter harvesting, and content scraping.**

**Here’s how it started**:

### # Defining Target domain

```
echo domain.com > targets.txt
```

### **# Subdomain enumeration**

```
subfinder -dL targets.txt -silent >> subs.txt
```

*It’s a passive enumeration where it takes the subdomain from publicly available online sources such as search engines, certificate logs, DNS databases, APIs, without directly interacting with the target domain.*

### **# Probing for live hosts**

```
cat subs.txt | httpx -silent >> live.txt
```

*This identify which subdomains are actually alive (i.e., responding to HTTP/HTTPS requests) from all subdomains.*

### **# Crawling for JS files**

```
cat live.txt | waybackurls | grep ".js" >> jsurls.txt
```

*Extracting js urls gives you advantage of exposing any sensitive informations like APIs, Secret Keys, AWS Credentials etc…*

### # Crawling for Parameters

```
cat live.txt | waybackurls | grep '=' tee params.txt
```

After gathering a list of live JavaScript files, I filtered out the third-party ones and focused on those hosted directly on domain.com.

Press enter or click to view image in full size

![]()

## 📜 Manual JS Review

Sometimes, tools aren’t enough—you have to read the code. So I fetched a few large JS files and manually inspected them:

```
curl -s https://www.domain.com/static/main.js | less
```

While scrolling, a particular block caught my attention:

```
const config = {
  apiKey: "AKIAXXXXXXXEXAMPLEKEY123",
  data=91173hsbakexampledata
}
```

💥 Boom. An API key, sitting exposed in client-side code. Immediately, a few red flags popped up in my head.

## 🔍 What Could Go Wrong?

Even without knowing exactly what service the key belonged to, I knew this was risky:

* *If the key had write permissions, it could lead to data tampering or account abuse.*
* *If it was for a billing-based service, someone could drain quotas or rack up costs.*
* *If tied to a misconfigured backend, this could help escalate to sensitive data access.*

## 🚨 Reporting

I submitted the issue through Hackerone, providing:

* *JS file URL*
* *Code snippet showing the exposed key*
* *Potential impact (resource abuse, data exposure, chaining risk)*

After a week, the hackerone team responded:

Press enter or click to view image in full size

![]()

Hackerone’s response

Although it wasn’t eligible for a bounty, the report was valid, and that felt like a win in itself.

### Lesson that should be taken

> To all frontend developers out there: Never include secrets or API keys in client-side code. Anyone can access and extract them with a browser or terminal.

### To Avoid

* Use environment variables and backend proxies to protect keys.
* Set strict scopes and rate limits on all tokens.

## 🧠 Final Thoughts

Even though it’s a duplicate bug. But it was a real issue, and it reminded me that **simple recon and manual inspection** still matter. Not every win comes with a reward—but every valid report sharpens your instincts.

### 🔁Found this useful?

### Clap👏, Share & Comment.

> Thank you guys…

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----e2f255ee0ee5---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----e2f255ee0ee5---------------------------------------)

[API](https://medium.com/tag/api?source=post_page-----e2f255ee0ee5---------------------------------------)

[JavaScript](https://medium.com/tag/javascript?source=post_page-----e2f255ee0ee5---------------------------------------)

[Low Hanging Fruit](https://medium.com/tag/low-hanging-fruit?source=post_page-----e2f255ee0ee5---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e2f255ee0ee5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e2f255ee0ee5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e2f255ee0ee5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e2f255ee0ee5---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e2f255ee0ee5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![127.0.0.1](https://miro.medium.com/v2/resize:fill:96:96/1*OpnEGtDWv2MkGt3n7HAPkA.jpeg)](https://medium.com/%40aashifm?source=post_page---post_author_info--e2f255ee0ee5------------------------...