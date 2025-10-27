---
title: BSides Athens 2023 Wrap-Up
url: https://blog.rootshell.be/2023/06/25/bsides-athens-2023-wrap-up/
source: /dev/random
date: 2023-06-26
fetch_date: 2025-10-04T11:48:02.961683
---

# BSides Athens 2023 Wrap-Up

[Skip to content](#content)

[![/dev/random](https://blog.rootshell.be/wp-content/uploads/2016/05/art-of-war-e1464648394825.jpg)](https://blog.rootshell.be/)

[/dev/random](https://blog.rootshell.be/)

"If the enemy leaves a door open, you must rush in." – Sun Tzu

Search for:

* [About Me](https://blog.rootshell.be/about/)
  + [About Me](https://blog.rootshell.be/about/)
  + [Online Presentations](http://www.slideshare.net/xme)
  + [PGP Public Key](https://blog.rootshell.be/pgp-public-key/)
* [Disclaimer](https://blog.rootshell.be/disclaimer/)
* [Tools](https://blog.rootshell.be/?page_id=3051)
  + [alerts2afterglow](https://github.com/xme/alerts2afterglow)
  + [hoover](https://github.com/xme/hoover)
  + [inotes.py](https://github.com/xme/inotes.py)
  + [known\_hosts\_bruteforcer](https://github.com/xme/known_hosts_bruteforcer)
  + [pastemon](https://github.com/xme/pastemon)
  + [oplb](https://github.com/xme/oplb)
  + [ossec\_dashboard](https://github.com/xme/ossec_dashboard)
  + [ossec2dshield](https://github.com/xme/ossec2dshield)
  + [twittermon](https://github.com/xme/twittermon)
  + [rrhunter](https://github.com/xme/rrhunter)
  + [syslog2loggly](https://github.com/xme/syslog2loggly)

![](https://blog.rootshell.be/wp-content/uploads/2023/06/IMG_1999-scaled-e1687701834644-900x400.jpeg)

# BSides Athens 2023 Wrap-Up

[June 25, 2023](https://blog.rootshell.be/2023/06/25/bsides-athens-2023-wrap-up/ "16:06") [Security](https://blog.rootshell.be/category/security/), [Wrap-Up](https://blog.rootshell.be/category/wrap-up-2/) [Leave a comment](https://blog.rootshell.be/2023/06/25/bsides-athens-2023-wrap-up/#respond)

A quick wrap-up of the last edition of BSides Athens that occurred yesterday, Saturday 24th. I really like this event for multiple reasons. First, the atmosphere, I’ve plenty of Greek friends and I like this country… and food! This was already the 8th edition and full in person! They reached an audience of 350 people coming from many countries! This was a two-tracks event with regular talks in track 1 and workshop/demos in the track 2. I stayed in track 1 the whole day.

The keynote speaker was Eric Eifert who talked about «*The evolution of Cyber Security and what to expect next*». Based on his bread experience, he reviewed some major security incidents from the past. For all of them, Eric briefly presented the incident, the challenges and lessons learned. It started in 1996 with «The Cuckoo’s Egg» (also a known book). Espionage activity performed by a German citizen. Very simple attack (password brute-force). In 1996, «Moonlight Maze», massive data breach across NASA, Pentagon, military contractors, etc. In 1998, «Solar Sunrise» targeted the US Air Force. In 1999, «Operation Allied Force» targeting NATO by Chinese attackers. Robert Hansen was spying for Russian between 1979 and 2001. I really like the following Eric’s quote:

« In God we trust, everyone else should be monitored! »

Want more? «Mandiant APT1 Report» in 2006-2013. Hundreds of TBytes stolen from at least 141 organisations. «Careem Cyber Extorsion» in 2018. with 14M customers PII stolen. The present? «Dubai Expo 2020» social media accounts impersonated Dubai Expo and used by scammers. Fake job postings, fake news about COVID-19 etc. In 2023, «Anonymous Sudan» performed multiple attacks in Sweden, Denmark (critical infrastructure), banks in Sudan, Israeli targets, … «Modern spy craft» a long-term employee identified as bypassing access control systems and accessing sensitive locations. Today, they are plenty of funny devices like the Flipper Zero, BadUSD or Bash bunny.

And the future? Let’s ask to ChatGPT. Eric did the exercise and received a very generic reply:

* Increased sophistication with machine learning
* Critical infrastructure
* IoT
* From ransomware to cyber extorsion, cyber hostages
* Supply chain attacks
* Emerging technologies (wearable medical devices)
* Nation-state sponsored attacks

![](https://blog.rootshell.be/wp-content/uploads/2023/06/IMG_1989.jpeg)

Then, we started with a bunch of talks related to offensive as well as defensive security. The first one was «*Hacking your favorite kiosk*» by A. Koureleas, G. Tyritidis. What is a kiosk? «*A Windows operating system feature that only allows one application to run*» ([Microsoft](https://learn.microsoft.com/en-us/windows/configuration/kiosk-methods) offers indeed a «kiosk mode» in Windows) They are everywhere and could contain interesting information. The demonstrated how easy it is to bypass this mode of operation and regain a regular access to the operating system. They also covered kiosk mode provided by Android devices (you can find a lot of tablet in shops, train stations, etc. They are everywhere. I was surprised to see that the [iKat](https://www.ikat.kronicd.net/) project is still alive!

After a welcomed coffee break, the next presentation was «*Harvesting low hanging fruits in Red Teaming exercises*» by [Nick Kapellos](https://twitter.com/kapellos). The topic was about easy ways to move forward during RT exercises mainly with passwords. Why passwords remain a key info? They can be (re)used for multiple attacks:

* Domain admin
* Latéral movements
* RDP/ Winrm WMI / PSexec /…
* NTLM hashes

Nick showed how easy we can find passwords in a corporate environment. A good location to search for passwords: SMB shares (IT folders, users files, configuration files, …) but beware of honeypots! He also covered Kerberoasting, MSSQL, NTLM and our best friends: printers! Note that Chrome is also interesting because passwords and cookies are easy to extract.

Vangelis Stykas presented «*Electryone: in the land of no sun*». After targeting EV chargers, Vangelis had a look at the photovoltaic ecosystem. Did you know the [horus scenario](https://horusscenario.com/)? Inverters are nice targets and, guess what, have plenty of vulnerabilities. They are connected to cloud platforms that have major vulnerabilities too. Vangelis found multiple vendors with vulnerabilities. He contacted them and give us a feedback about their reactions. What scares me is not the fact that they have vulnerabilities. It is « normal » but the way they reply (when they do!) is crazy!

![](https://blog.rootshell.be/wp-content/uploads/2023/06/IMG_1990.jpeg)

After the lunch break, a panel was organised with an interesting topic in the cybersecurity field: What about inclusivity? It’s a fact that we need more women to help with cybersecurity. But it’s not only a man/woman problem. They are many others. I found the Ana Batronivic’s testimony very interesting. She’s disabled and discovered a passion for security. She explained the difficulties she’s facing on a day to day basic. She published a very nice blog [article](https://blog.aquilosec.com/blog/accessible-cybersecurity/) on this topic.

The next talk was the one from [Sam Stepanyan](https://twitter.com/securestep9) from OWASP. He presented a tool supported by the OWASP foundation: [Nettacker](https://owasp.org/www-project-nettacker/). Honestly, I did not know this tool and the presentation motivated me to install/test it. It’s a vulnerability scanner written in Python but, compared to tools like BurpSuite, the scope can be extended to multiple sites, subnets, etc. It’s completely modular and «modules» can be easily developed to test for more vulnerabilities (not only web oriented). I had an interesting chat with Sam and he told me that the idea is to replace classic scanner like Nessus! No more no less…

Then, [Paris Zoumpouloglou](https://twitter.com/pzubu) presented «*From chasing clouds to governing them – A cloud security journey*». Working for Riot Games, he explained how the company improved the management of their huge cloud platform. What issues they faced, how they solved it, etc. Indeed, starting to deploy services in the cloud is easy but, as Paris, explained, you can quickly reach the limitations of standard tools proposed by cloud providers in terms of performance, storage, etc.

...