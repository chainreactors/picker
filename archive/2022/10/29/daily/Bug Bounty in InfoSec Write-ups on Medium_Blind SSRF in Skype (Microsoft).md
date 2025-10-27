---
title: Blind SSRF in Skype (Microsoft)
url: https://infosecwriteups.com/blind-ssrf-in-skype-microsoft-6639f4961052?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-10-29
fetch_date: 2025-10-03T21:13:35.953930
---

# Blind SSRF in Skype (Microsoft)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6639f4961052&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblind-ssrf-in-skype-microsoft-6639f4961052&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6639f4961052---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6639f4961052---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Blind SSRF in Skype (Microsoft)

[![Jayateertha Guruprasad](https://miro.medium.com/v2/resize:fill:64:64/1*bmKMCGbQfIUNeymH5M7Pow.jpeg)](https://jayateerthag.medium.com/?source=post_page---byline--6639f4961052---------------------------------------)

[Jayateertha Guruprasad](https://jayateerthag.medium.com/?source=post_page---byline--6639f4961052---------------------------------------)

2 min read

·

Oct 28, 2022

--

1

Listen

Share

Server Side Request Forgery is a vulnerability that allows attacker to make server request to attacker controlled network location/path.

While analyzing requests in Burp for Skype for Web, found a endpoint at \*.\*.skype.com/path?url=https://example.com , As the url param appeared interesting tried to change the url with my ngrok instance & got a hit !

Confirmed that it’s Skype which hit the url by looking at the ngrok inspect web console by verifying received User-Agent header(Skype)and IP address in who.is.

Although I was able to make the server hit arbitrary webpage, I couldn’t get full response. I could only get status code, content-type, content-length(size) of response and text content from few selected HTML tags. That’s, it’s not full SSRF as expected, but is a blind/partial SSRF.

Tried to access below paths —

1. localhost/internal ip address -> Failed
2. Tried to bypass localhost/internal ip address using url redirect/url shortner methods -> Failed
3. External ip address/webpage -> Success
4. Common Azure/AWS/DigitalOcean Meta data IP addresses -> Failed
5. Not so commonly used, Azure related IP address (168.63.129.16) -> Success -> This IP can be used to determine VM’s health by using <http://168.63.129.16/metadata/v1/maintenance> endpoint, which should return OK (200 Status Code) if VM is functioning. (Refer [this](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16?WT.mc_id=docs-azuredevtips-azureappsdev) for more information)

Tried changing url param value to <http://168.63.129.16/metadata/v1/maintenance> , got 200 Ok response, with size of response as 2 bytes which confirms that response text probably contains OK in response.

Made a nice report mentioning all the details and sat back waiting for Microsoft to reproduce and fix the report.

Fortunately this was in scope for bounty under the M365 Bounty Program and got a nice $$$$ bounty !

Press enter or click to view image in full size

![]()

Party Hard!

Report Timeline:

1. Reported — Sep 23, 2022
2. Additional Details Updated — Oct 3, 2022
3. Bounty Rewarded — Oct 8, 2022
4. Fixed — Oct 12, 2022

## Liked my article ? **Follow me on twitter (**[**@jayateerthaG**](https://twitter.com/jayateerthaG)**) and medium for more content about bugbounty, Infosec, cybersecurity and hacking.**

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Hacking](https://medium.com/tag/hacking?source=post_page-----6639f4961052---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----6639f4961052---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----6639f4961052---------------------------------------)

[Microsoft](https://medium.com/tag/microsoft?source=post_page-----6639f4961052---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----6639f4961052---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6639f4961052---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6639f4961052---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6639f4961052---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6639f4961052---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--6639f4961052---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Jayateertha Guruprasad](https://miro.medium.com/v2/resize:fill:96:96/1*bmKMCGbQfIUNeymH5M7Pow.jpeg)](https://jayateerthag.medium.com/?source=post_page---post_author_info--6639f4961052---------------------------------------)

[![Jayateertha Guruprasad](https://miro.medium.com/v2/resize:fill:128:128/1*bmKMCGbQfIUNeymH5M7Pow.jpeg)](https://jayateerthag.medium.com/?source=post_page---post_author_info--6639f4961052---------------------------------------)

[## Written by Jayateertha Guruprasad](https://jayateerthag.medium.com/?source=post_page---post_author_info--6639f4961052---------------------------------------)

[386 followers](https://jayateerthag.medium.com/followers?source=post_page---post_author_info--6639f4961052---------------------------------------)

·[39 following](https://medium.com/%40jayateerthag/following?source=post_page---post_author_info--6639f4961052---------------------------------------)

I get paid for breaking things !

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6639f4961052---------------------...