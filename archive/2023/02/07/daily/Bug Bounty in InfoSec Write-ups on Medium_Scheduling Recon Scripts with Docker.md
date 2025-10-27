---
title: Scheduling Recon Scripts with Docker
url: https://infosecwriteups.com/scheduling-recon-scripts-with-docker-794c46794c28?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-07
fetch_date: 2025-10-04T05:50:42.920695
---

# Scheduling Recon Scripts with Docker

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F794c46794c28&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fscheduling-recon-scripts-with-docker-794c46794c28&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fscheduling-recon-scripts-with-docker-794c46794c28&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-794c46794c28---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-794c46794c28---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Scheduling Recon Scripts with Docker

## Cronjobs are useful for scheduling tasks to run automatically at a specified time or interval. In this tutorial, we’ll go over how to set up a cronjob with Docker for recon purposes.

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:64:64/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---byline--794c46794c28---------------------------------------)

[Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---byline--794c46794c28---------------------------------------)

4 min read

·

Jan 6, 2023

--

Share

Press enter or click to view image in full size

![]()

Photo by [Ran Berkovich](https://unsplash.com/%40berko?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

### Introduction

First, add the following line to your `crontab` file to run the `cron.sh` script every minute: <https://crontab.guru/> This is a useful site for cron timings

```
* * * * * export $(xargs < /app/.env); /app/cron.sh >> /app/log/cron.log 2>&1
```

This line exports the environment variables specified in the `.env` file and runs the `cron.sh` script, redirecting the output to the `cron.log` file in the `/app/log` directory.

Next, in your `docker-compose.yml` file, add the following lines to specify the location of your environment file and create the necessary directories and files:

```
version: "3.9"
services:
  recon:
    build: .
    env_file:
      - .env
    volumes:
      - ./recon:/app/recon
      - ./log:/app/log
```

Now we need the `Dockerfile`

```
FROM ubuntu:22.04
# Install prerequisites
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    dnsutils \
    cron
RUN mkdir /app/
WORKDIR /app/
COPY ./…
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--794c46794c28---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--794c46794c28---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--794c46794c28---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--794c46794c28---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--794c46794c28---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:96:96/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--794c46794c28---------------------------------------)

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:128:128/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--794c46794c28---------------------------------------)

[## Written by Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---post_author_info--794c46794c28---------------------------------------)

[369 followers](https://adamjsturge.medium.com/followers?source=post_page---post_author_info--794c46794c28---------------------------------------)

·[21 following](https://medium.com/%40adamjsturge/following?source=post_page---post_author_info--794c46794c28---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----794c46794c28---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----794c46794c28---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----794c46794c28---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----794c46794c28---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----794c46794c28---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----794c46794c28---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----794c46794c28---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----794c46794c28---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----794c46794c28---------------------------------------)