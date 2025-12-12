---
title: Using AI Gemma 3 Locally with a Single CPU , (Wed, Dec 10th)
url: https://isc.sans.edu/diary/rss/32556
source: SANS Internet Storm Center, InfoCON: green
date: 2025-12-11
fetch_date: 2025-12-12T03:23:10.761419
---

# Using AI Gemma 3 Locally with a Single CPU , (Wed, Dec 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32554)

# [Using AI Gemma 3 Locally with a Single CPU](/forums/diary/Using%2BAI%2BGemma%2B3%2BLocally%2Bwith%2Ba%2BSingle%2BCPU/32556/)

**Published**: 2025-12-10. **Last Updated**: 2025-12-11 02:37:47 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Using%2BAI%2BGemma%2B3%2BLocally%2Bwith%2Ba%2BSingle%2BCPU/32556/#comments)

Several months ago, I got a Nucbox K8 Plus minicomputer to use as a [Proxmox 9](https://pve.proxmox.com/wiki/Main_Page) server. At the time of this acquisition, I didn't realize this minicomputer had an artificial intelligence (AI) engine [[1](https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-7-8845hs.html)] build in the CPU that could be used to run AI applications locally. A coworker recommended that I try [Google Gemma 3](https://deepmind.google/models/gemma/gemma-3/) as a local AI open model to work with my use cases.

"Gemma is a family of generative artificial intelligence (AI) models and you can use them in a wide variety of generation tasks, including question answering, summarization, and reasoning." [[2](https://ai.google.dev/gemma/docs/core)], a review of the Gemma 3 key features is also posted on this page. This page [[3](https://ai.google.dev/gemma/docs/core#sizes)] lists the minimum requirements for the 5 Gemma 3 models 270M, 1B, 4B, 12B, and 27B.

**Default Open WebUI**

![](https://isc.sans.edu/diaryimages/images/gemma3_intro_page.png)

**My Setup with Open WebUI**

* OS is a Linux Container (LXC) Ubuntu 24.04
* Ollama with gemma3:12b [[4](https://deepmind.google/models/gemma/gemma-3/)]
* Open WebUI [[5](https://github.com/open-webui/open-webui)]

**Installing Ollama with Gemma 3**

I used these steps to get Gemma setup. First review the requirements for RAM [[3](https://ai.google.dev/gemma/docs/core#sizes)] before deciding with Gemma 3 model to install. You can start small (i.e. 4B or smaller) for testing before using a larger model. I'm using  4B and 12B with 16 GB of RAM with my installation.

![](https://isc.sans.edu/diaryimages/images/gemma3_installation.png)

If you want to test some queries before installing the WebUI, this last command will open the interpreter:

ollama run gemma3:4b

Since I have a Ryzen 7 CPU, my next step was to install the admgpu [7] software to use the AI features of the CPU. The last step is to install the graphical interface to work from a browser using the Open WebUI [5] and there are several models listed here to get the WebUI running. I had to try a few combinations; in the end this is what I used:

sudo docker run -d -p 80:8080 -v ollama:/root/.ollama --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

**Bugs in Proxmox 9 for LXC and AppArmor**

For the Linux Container to run correctly, I had to edit the edit the LXC config file (114 is the container number) and add those two lines:

vi /etc/pve/lxc/114.conf

* lxc.apparmor.profile: unconfined
* lxc.mount.entry: /dev/null sys/module/apparmor/parameters/enabled none bind 0 0

And it may also be necessary to add this as well in the sudo command before installing the docker: --security-opt apparmor:unconfined

**Login WebUI Interface**

After the installation of the WebUI, you need to create the first admin account before being able to login.My first query asked my AI to describe the IPv4 header:
![](https://isc.sans.edu/diaryimages/images/gemma3_ip_question.png)

Gemma 3 offers the ability to work with large files with its 128K context, work with images and has multilingual support which is practical if you know multiple languages. Finally, it can run locally in PC, laptop and smartphone on a single GPU or TPU and smaller devices. If you have experience using Gemma 3, what are the use cases you are using it? You can add your comments in our [contact form](https://isc.sans.edu/contact.html).

[1] https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-7-8845hs.html
[2] https://ai.google.dev/gemma/docs/core
[3] https://ai.google.dev/gemma/docs/core#sizes
[4] https://deepmind.google/models/gemma/gemma-3/
[5] https://github.com/open-webui/open-webui
[6] https://ai.google.dev/gemma/docs/integrations/ollama?utm\_source=deepmind.google&utm\_medium=referral&utm\_campaign=gdm&utm\_content
[7] https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installryz/native\_linux/install-ryzen.html
[8] https://forum.proxmox.com/threads/priviledge-container-disabling-apparmor-does-not-work.122168/
[9] https://blog.ktz.me/apparmors-awkward-aftermath-atop-proxmox-9/
[10] https://docs.openwebui.com/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [AI](/tag.html?tag=AI) [Gemma3](/tag.html?tag=Gemma3) [gemma312b](/tag.html?tag=gemma312b) [images](/tag.html?tag=images) [multilingual support](/tag.html?tag=multilingual support) [Open WebUI](/tag.html?tag=Open WebUI) [test support](/tag.html?tag=test support)

[0 comment(s)](/diary/Using%2BAI%2BGemma%2B3%2BLocally%2Bwith%2Ba%2BSingle%2BCPU/32556/#comments)

* [previous](/diary/32554)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)