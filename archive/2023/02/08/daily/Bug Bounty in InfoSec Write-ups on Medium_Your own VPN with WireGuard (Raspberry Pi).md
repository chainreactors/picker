---
title: Your own VPN with WireGuard (Raspberry Pi)
url: https://infosecwriteups.com/your-own-vpn-with-wireguard-raspberry-pi-286d9902f6d2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-08
fetch_date: 2025-10-04T05:57:54.223636
---

# Your own VPN with WireGuard (Raspberry Pi)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F286d9902f6d2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyour-own-vpn-with-wireguard-raspberry-pi-286d9902f6d2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyour-own-vpn-with-wireguard-raspberry-pi-286d9902f6d2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-286d9902f6d2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-286d9902f6d2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Your own VPN with WireGuard (Raspberry Pi)

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:64:64/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---byline--286d9902f6d2---------------------------------------)

[Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---byline--286d9902f6d2---------------------------------------)

3 min read

·

Jan 11, 2023

--

Share

This guide will walk you through the process of setting up a VPN with WireGuard. WireGuard is a modern and secure VPN that is very easy to setup. Throughout the article I will be referencing <https://github.com/WeeJeWel/wg-easy>

## Why host our own VPN?

VPNs are a great resource that can allow you to accomplish multiple goals. You’ll be able navigate more securely when on public wifi. You’ll also be able to mask your IP (if you set it up in a VPS). If you set it up on your own home network you can access devices like a NAS or an VMs you have on the network.

## Prerequisites:

* Anything that can run docker (We will be using a Raspberry Pi)
* Docker

## Step 1: Docker

To install Docker on your device, we can go to https://docs.docker.com/desktop/install/linux-install/ to find how to install for your operating system and distro.

## Step 2: Setup WireGuard

Setting up WireGuard using wg-easy, execute the following command:

```
docker run -d \
  --name=wg-easy \
  -e WG_HOST=🚨YOUR_SERVER_IP \
  -e PASSWORD=🚨YOUR_ADMIN_PASSWORD \
  -v ~/.wg-easy:/etc/wireguard \
  -p 51820:51820/udp \
  -p 51821:51821/tcp \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_MODULE \
  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
  --sysctl="net.ipv4.ip_forward=1" \
  --restart unless-stopped \
  weejewel/wg-easy
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--286d9902f6d2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--286d9902f6d2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--286d9902f6d2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--286d9902f6d2---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--286d9902f6d2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:96:96/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--286d9902f6d2---------------------------------------)

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:128:128/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--286d9902f6d2---------------------------------------)

[## Written by Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---post_author_info--286d9902f6d2---------------------------------------)

[369 followers](https://adamjsturge.medium.com/followers?source=post_page---post_author_info--286d9902f6d2---------------------------------------)

·[21 following](https://medium.com/%40adamjsturge/following?source=post_page---post_author_info--286d9902f6d2---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----286d9902f6d2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----286d9902f6d2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----286d9902f6d2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----286d9902f6d2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----286d9902f6d2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----286d9902f6d2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----286d9902f6d2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----286d9902f6d2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----286d9902f6d2---------------------------------------)