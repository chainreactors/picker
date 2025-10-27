---
title: Quickpost: The Electric Energy Consumption Of LLMs
url: https://blog.didierstevens.com/2024/10/06/quickpost-the-electric-energy-consumption-of-llms/
source: Didier Stevens
date: 2024-10-07
fetch_date: 2025-10-06T18:49:19.473879
---

# Quickpost: The Electric Energy Consumption Of LLMs

# [Didier Stevens](https://blog.didierstevens.com/)

## Sunday 6 October 2024

### Quickpost: The Electric Energy Consumption Of LLMs

Filed under: [Quickpost](https://blog.didierstevens.com/category/quickpost/) — Didier Stevens @ 19:17

I’ve read claims that AI queries require a lot of energy. Today I heard another claim on the Nerdland Podcast (a popular science podcast here in Belgium): “letting ChatGPT write an email of 100 words requires 70 Wh” (if you’re interested, that’s said at 00:28:05 in [this episode](https://podcast.nerdland.be/nerdland-maandoverzicht-oktober-2024/)).

I though to myself: that’s a lot of energy. 70 Wh is 252,000 Ws (70 W \* 3600 s). Assume that it takes 10 seconds to write that email, then it requires 25,200 W of power, or 25 kW. That’s way more than the theoretical maximum I can get here at home from the power grid (9 kW).

So I decided to do some quick & dirty tests with my desktop computer and my powermeter.

First test: measure everything.

Step 1: starting up my desktop computer (connected to my powermeter) and waiting for the different services to startup, required 2.67 Wh of electrical energy:

![](https://blog.didierstevens.com/wp-content/uploads/2024/10/screen07.bmp)

Step 2: I opened a command prompt, started Ollama, typed a query to generate an email, and waited for the result. By then, the required electrical energy op my desktop computer (since starting up) was 3.84 Wh:

![](https://blog.didierstevens.com/wp-content/uploads/2024/10/screen08.bmp)

So step 2 took 57 seconds (00:02:36 minus 00:01:39) and required 1.17 Wh (3.84 – 2.67). That’s way less than 70 Wh.

![](https://blog.didierstevens.com/wp-content/uploads/2024/10/2024-10-06_19-02-28.png)

Second test: just measure the query.

I restarted my computer and started Ollama. Then I started my powermeter and pasted my query and waited for the answer:

![](https://blog.didierstevens.com/wp-content/uploads/2024/10/2024-10-06_19-34-08.png)

That took 3 seconds and required 0.236 Wh:

![](https://blog.didierstevens.com/wp-content/uploads/2024/10/screen09.bmp)

Notice that I have not just measured the electrical energy consumption of Ollama processing my query, but I measured the total electrical energy consumption of my desktop computer while Ollama was processing my query.

0.236 Wh for a computer running Ollama and processing a query is very different than 70 Wh for ChatGPT processing a query. That’s almost 300 times more, so even though my test here is just anecdotal and I’m using another LLM than ChatGPT, I will assume that 70 Wh is a gross overestimation.

FYI: asking Google “what is the electrical energy consumption of chatgpt processing a query”, I find results mentioning between 1 and 10 Wh. That’s closer to my tests than the 70 Wh claim.

---

[Quickpost info](https://blog.didierstevens.com/2007/11/01/announcing-quickposts/)

---

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2024/10/06/quickpost-the-electric-energy-consumption-of-llms/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2024/10/06/quickpost-the-electric-energy-consumption-of-llms/?share=x)

### *Related*

[Comments (4)](https://blog.didierstevens.com/2024/10/06/quickpost-the-electric-energy-consumption-of-llms/#comments)

## 4 Comments [»](#postcomment "Leave a comment")

1. Thank you for the insightful post on the electric energy consumption of LLMs. One question that comes to mind is regarding the energy used during the training phase of these models? Of course this would have to be later devided by the times a model is used.

   Comment by Anonymous — Monday 14 October 2024 @ [9:43](#comment-629361)
2. That’s something interesting to think about, thanks for the suggestion.

   Comment by [Didier Stevens](https://didierstevens.wordpress.com/) — Tuesday 15 October 2024 @ [16:33](#comment-629367)
3. The most energy is consumed when training the model. Not when the model queried.

   What people tend to forget is that the training of new LLM iterations never end, because the holy grail of AI is not found yet (or just market share). While using LLM version x.y is in use, its creator is already training the next version of the LLM. And training the next version always needs a considerate amount of extra energy in comparison to the previous version.

   Comment by Anonymous — Sunday 10 November 2024 @ [9:54](#comment-629502)
4. That is true. Nevertheless, there are many claims that LLM queries require more energy than classic web search queries. Not clear to me if that is true too.

   Do you have numbers for training?

   Comment by [Didier Stevens](https://didierstevens.wordpress.com/) — Monday 11 November 2024 @ [8:32](#comment-629503)

[RSS feed for comments on this post.](https://blog.didierstevens.com/2024/10/06/quickpost-the-electric-energy-consumption-of-llms/feed/) [TrackBack URI](https://blog.didierstevens.com/2024/10/06/quickpost-the-electric-energy-consumption-of-llms/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools](https://blog.didierstevens.com/programs/virustotal-tools/)
    - [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
    - [YARA Rules](https://blog.didierstevens.com/programs/yara-rules/)
    - [ZIPEncryptFTP](https://blog.didierstevens.com/programs/zipencryptftp/)
  + [Public Drafts](https://blog.didierstevens.com/public-drafts/)
    - [Cisco Tricks](https://blog.didierstevens.com/public-drafts/cisco-tricks/)
  + [Screencasts & Videos](https://blog.didierstevens.com/screencasts-videos/)
* Search for:
* ## Top Posts

  + [PDF Tools](https://blog.didiersteven...