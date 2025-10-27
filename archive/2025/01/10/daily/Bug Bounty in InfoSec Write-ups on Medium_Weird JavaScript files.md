---
title: Weird JavaScript files
url: https://infosecwriteups.com/weird-javascript-files-7e6e7296e914?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-10
fetch_date: 2025-10-06T20:07:35.215739
---

# Weird JavaScript files

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7e6e7296e914&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweird-javascript-files-7e6e7296e914&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweird-javascript-files-7e6e7296e914&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7e6e7296e914---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7e6e7296e914---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Weird JavaScript files 🥴

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:64:64/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---byline--7e6e7296e914---------------------------------------)

[cryptoshant🇮🇳](https://medium.com/%40dsmodi484?source=post_page---byline--7e6e7296e914---------------------------------------)

4 min read

·

Jan 8, 2025

--

Listen

Share

Hello Hacker, In this writeup I am going to explain the importance of looking JS files on the website, some tools that I preferred and also I am going to discuss one of my finding in this writeup. So let’s get started.

Press enter or click to view image in full size

![]()

**Why to look at JS files?**

Javascript is a something like the engine in the car so it is holding so much details then you can find anywhere. In js, you can understand how the logic of the website works, sometimes finds a hardcoded gems like apikeys, database credentials, admin panel passwords and many more things. I know when we look or open js files it looks so weird and we generally starts running **ffuf**, **dirsearch** or **wfuzz** and increase traffic on the website I generally prefer **google dorking** or analyzing the js file if available in the source code and if I don’t find anything then I go with directory fuzzing tools.

**Which tools I prefer to look js files?**

1. [**Trufflehog**](https://chromewebstore.google.com/detail/trufflehog/bafhdnhjnlcdbjcdcnafhdcphhnfnhjc)**:** This extension is comes in both **google** and **firefox** and this is used to find some sensitive api keys, .git files, config files, secret keys and all that stuffs. Truly says by using this tool and reporting many bugs like api keys, .git files all are closed as NA or informative or Duplicate so I don’t know is it best to use this tool everytime or not but still I am using this tool and now I am not reporting any bugs like api key or something similar which are found by this tool unless I can prove the real impact.
2. **Linkfinder:** I personally like this tool because this tool gives you all the paths or directories stored in js files in a very organized way in your browser and I like this tool because this tool also helped me to find a vulnerability. I will discuss vulnerability later. To download and use this tool is very easy you can use this tool here is the link 👇

[## GitHub - GerbenJavado/LinkFinder: A python script that finds endpoints in JavaScript files

### A python script that finds endpoints in JavaScript files - GerbenJavado/LinkFinder

github.com](https://github.com/GerbenJavado/LinkFinder?source=post_page-----7e6e7296e914---------------------------------------)

**3. JSA:** Actually I never used this tool but I heard or read somewhere that this tool is also used for analyzing Js files so that I am adding this tool and I will use this tools in my upcoming testing also. Link here 👇

[## GitHub - w9w/JSA: Javascript security analysis (JSA) is a program for javascript analysis during…

### Javascript security analysis (JSA) is a program for javascript analysis during web application security assessment. …

github.com](https://github.com/w9w/JSA?source=post_page-----7e6e7296e914---------------------------------------)

**Bug Discovery?**

During testing one of the big company I found a subdomain like **discuss.xyz.com** and when I visit the page I can see the welcome page only nothing special or no features, only **welcome** message in the middle. So I thought to run **ffuf** and **dirsearch** but sadly I don’t find any interesting things all the paths are 404 or 403 and at the end I got nothing 🥺. So I didn’t leave this as it is and I research more things and I find-out the tool **Linkfinder** to extract the hidden paths or directories from the js files. So I use this tool and guess what? where the **ffuf** and **dirsearch** fails where this tools give me some directories like **/movies , /sip and /notifications.** After analyzing all this endpoint **/movies** and **/notifications** endpoint give nothing only blank page and **/sip** page disclose users information like users real name, their profile pictures, their discussion about sip’s like to change the plan, or to close the sip, or to know more about their current sip and there are 3 mentors who are giving reply back to all the questions and so on lots of live data I found. Now I search for this app firstly like is this things is meant to be publicly accessible or not? And after research I got to know the person who are **verified** or **done kyc** and have **started** their **daily sip** then only the particular person is only authorized to join this community and I feel like I found a valid bug 🤗. There are still more feature at this endpoint like, likes someone comment, or we can comment to any question and also we can edit or delete our comment but sadly all things needs the proper authorization token and I am unable to get that 😶. But still this is a valid P4 bug because it only affects confidentiality I guess.

**Impact:**

An attacker can have an unauthorized access to read the message of legitimate users with their real name, profile photos and according to users query an attacker can even guess what type of sips does user hold.

**Mitigation:**

Owner should make proper authorization checks so that the confidentiality of users can be secured in proper way.

**Report Status:**

Sadly, I submitted this report on Nov, 2024 but still waiting for their response till now no response from company and bug is still not fixed. Hope they will respond me 🤞

**Lesson Learned?**

Don’t just relay on directory fuzzing tools only, also used js file enumerations to find more paths or hidden paths to directly access it.

Anyways hope for the best and just move on and I wanted to tell you to also use **Linkfinder or JSA** because no wordlist contains /sip, /movie endpoint and if any wordlist contains this words then fear of **429 (Too many request)** andit will take more time as compared ...