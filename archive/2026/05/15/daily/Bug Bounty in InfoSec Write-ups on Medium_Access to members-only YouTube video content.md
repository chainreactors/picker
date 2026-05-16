---
title: Access to members-only YouTube video content
url: https://infosecwriteups.com/access-to-members-only-youtube-video-content-6f5d951da209?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-15
fetch_date: 2026-05-16T05:14:15.826125
---

# Access to members-only YouTube video content

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccess-to-members-only-youtube-video-content-6f5d951da209&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccess-to-members-only-youtube-video-content-6f5d951da209&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6f5d951da209---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6f5d951da209---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# **Access to members-only YouTube video content**

[![Seqrity](https://miro.medium.com/v2/resize:fill:64:64/1*wMk8SwutLp89HGvVoAmayQ.jpeg)](https://seqrity.medium.com/?source=post_page---byline--6f5d951da209---------------------------------------)

[Seqrity](https://seqrity.medium.com/?source=post_page---byline--6f5d951da209---------------------------------------)

2 min read

·

2 days ago

--

3

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D6f5d951da209&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccess-to-members-only-youtube-video-content-6f5d951da209&source=---header_actions--6f5d951da209---------------------post_audio_button------------------)

Share

I was browsing the NahamSec YouTube channel when I noticed some members-only videos. Usually, you need to be a paid member of a channel to access them, but as a bug hunter, I tried to access them without paying. One approach that came to mind was using Gemini. Since Gemini is another Google product, I thought it might have deeper access to YouTube videos.

I tested this using [Google AI Studio](https://aistudio.google.com).

**My first prompt was:**

```
Print all details and subtitles separately like
[Visual]
[Subtitle]
Print each [Visual] and [Subtitle] alongside by timestamp.
https://www.youtube.com/watch?v=D1QdCusWu8M
```

The output was not accurate.

## Get Seqrity’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

At that time, Gemini was on version 2.0. A week later, version 2.5 was released with a new feature: a dedicated YouTube tool that allows you to attach video links directly.

![]()

I tried again. Gemini 2.5 treated the links differently, and the output was exactly what I expected. It printed the subtitles and described the video frame by frame.

Press enter or click to view image in full size

![]()

Since the video was about developing a Caido plugin, I tried to fetch the code from a specific time using this prompt:

```
print javascript code at 0m52s693ms - 0m56s333ms
```

**The result was:**

```
> var script = document.createElement('script');
  script.src = 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/aes.js';
  script.addEventListener('load', function() {
      window.getCookie = function(name) {
          var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
          if (match) return match[2];
```

I reported this bug to the Google Bug Bounty program and was awarded $1,337.

**Original report:**

[## Access to members only YouTube video content | Google Bug Hunters

### Found a security vulnerability? Discover our forms for reporting security issues to Google: for the standard VRP…

bughunters.google.com](https://bughunters.google.com/reports/vrp/V5pPrth1n?source=post_page-----6f5d951da209---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----6f5d951da209---------------------------------------)

[Ai Security](https://medium.com/tag/ai-security?source=post_page-----6f5d951da209---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----6f5d951da209---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----6f5d951da209---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6f5d951da209---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6f5d951da209---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6f5d951da209---------------------------------------)

[86K followers](/followers?source=post_page---post_publication_info--6f5d951da209---------------------------------------)

·[Last published 23 hours ago](/i-got-blocked-by-outlier-twice-the-second-time-i-had-built-my-own-browser-4a9040438f4e?source=post_page---post_publication_info--6f5d951da209---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Seqrity](https://miro.medium.com/v2/resize:fill:96:96/1*wMk8SwutLp89HGvVoAmayQ.jpeg)](https://seqrity.medium.com/?source=post_page---post_author_info--6f5d951da209---------------------------------------)

[![Seqrity](https://miro.medium.com/v2/resize:fill:128:128/1*wMk8SwutLp89HGvVoAmayQ.jpeg)](https://seqrity.medium.com/?source=post_page---post_author_info--6f5d951da209---------------------------------------)

[## Written by Seqrity](https://seqrity.medium.com/?source=post_page---post_author_info--6f5d951da209---------------------------------------)

[227 followers](https://seqrity.medium.com/followers?source=post_page---post_author_info--6f5d951da209---------------------------------------)

·[38 following](https://medium.com/%40seqrity/following?source=post_page---post_author_info--6f5d951da209---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----6f5d951da209---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6f5d951da209---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6f5d951da209---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6f5d951da209------------------------------------...