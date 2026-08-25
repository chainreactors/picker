---
title: AliExpress accused of fingerprinting shoppers with silent audio trick that also muted a dev's headphones
url: https://www.theregister.com/security/2026/08/24/aliexpress-accused-of-fingerprinting-shoppers-with-silent-audio-trick-that-also-muted-a-devs-headphones/5291662
source: www.theregister.com - Articles
date: 2026-08-24
fetch_date: 2026-08-25T03:00:58.134650
---

# AliExpress accused of fingerprinting shoppers with silent audio trick that also muted a dev's headphones

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

Security

# AliExpress accused of fingerprinting shoppers with silent audio trick that also muted a dev's headphones

Sawtooth waves you can't hear still mess with your Bluetooth. Firefox and Brave say they've got you covered

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
mon 24 Aug 2026 // 13:32 UTC

Developer Matt Callaghan claims he caught Alibaba trying to track web users by playing sounds through browsers vulnerable to audio fingerprinting.

The software engineer drew attention to the issue late last week after investigating why his Bluetooth headphones stopped playing music whenever he visited Alibaba's website.

“Recently I ran into a strange problem with my Bluetooth headphones,” Callaghan [wrote](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html). “They support multipoint Bluetooth audio, so they can be connected to my PC and phone at the same time. Normally, the PC takes priority playing audio, with my phone being able to play audio when nothing is playing on the PC.

REG AD

“Usually I listen to music on my phone but with notifications or YouTube playing through the PC, this works reliably until I open an AliExpress page in Firefox or Chrome.

REG AD

“Shortly after loading the AliExpress homepage, audio from my phone would stop playing. Closing the AliExpress tab fixes it immediately. Muting the tab/Firefox/Windows does not help, and there is no visible video, music, or other media playing on the page.”

Callaghan tried to find any hidden conventional media elements but found nothing. Further digging revealed two audio scripts that he said were “extremely obfuscated” within Alibaba’s browser security and anti-abuse tooling.

He said the scripts built a WebAudio graph that introduced a sawtooth oscillator to generate a waveform, an analyzer to measure the result after the waveform passes through a browser’s audio implementation, and a script to read the associated frequency data.

The scripts set the audio’s gain to zero, meaning the end user won’t hear anything, but the WebAudio graph will still be processed by the browser.

“This is very different from an autoplaying video,” said Callaghan. “There is no media element for the browser's normal tab mute control to stop. As far as the page is concerned, it is performing live audio processing.

“In my case, that appears to have been enough for Firefox or Windows to keep the Bluetooth audio path active, preventing my multipoint headphones from switching cleanly back to the phone.”

Callaghan found further evidence in the code of Alibaba looking for data related to screen dimensions, device memory, browser plugins, WebGL rendering, mouse events, and more.

As well as signs that Alibaba is encrypting data and sending it to its telemetry services, the developer said all of it amounts to “a fairly comprehensive browser and device fingerprint.”

REG AD

The Register has asked Alibaba to comment.

Despite Callaghan saying he could reliably reproduce this issue on both Firefox and Chrome, [Firefox](https://www.theregister.com/security/2026/08/11/mozilla-revokes-firefox-signing-key-after-unencrypted-copy-lands-in-github/5285908) issued a [Xtatement](https://x.com/firefox/status/2090589371049087177) saying its anti-fingerprinting technology thwarts Alibaba’s tracking tricks.

## MORE CONTEXT

* [### Google Chrome lacks protection against one of the most basic and common ways to track users online](/security/2026/04/16/google-chrome-lacks-browser-fingerprinting-defenses/5229136)
* [### Your browser has ad tech's fingerprints all over it, but there's a clean-up squad in town](/security/2025/06/30/your-browser-has-ad-techs-fingerprints-all-over-it/777950)
* [### UK ICO not happy with Google's plans to allow device fingerprinting](/security/2024/12/23/ico-puts-foot-down-on-googles-planned-fingerprinting-change/1345008)
* [### Meta, Spotify break Apple's device fingerprinting rules – new claim](/security/2024/05/07/meta-spotify-break-apples-device-fingerprinting-rules/1159350)

It pointed to a [blog post](https://ritter.vg/blog-webaudio_alibaba.html) from Tom Ritter, a security engineer on the Firefox team, who explained that as of version 118 (September 2023), the protections it intro...