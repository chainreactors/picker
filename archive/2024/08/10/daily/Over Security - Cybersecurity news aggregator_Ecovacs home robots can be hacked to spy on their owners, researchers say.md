---
title: Ecovacs home robots can be hacked to spy on their owners, researchers say
url: https://techcrunch.com/2024/08/09/ecovacs-home-robots-can-be-hacked-to-spy-on-their-owners-researchers-say/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-10
fetch_date: 2025-10-06T18:06:25.303495
---

# Ecovacs home robots can be hacked to spy on their owners, researchers say

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-lockup.svg) TechCrunch Desktop Logo](https://techcrunch.com)

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-logo-mobile.svg) TechCrunch Mobile Logo](https://techcrunch.com)

* [Latest](/latest/)
* [Startups](/category/startups/)
* [Venture](/category/venture/)
* [Apple](/tag/apple/)
* [Security](/category/security/)
* [AI](/category/artificial-intelligence/)
* [Apps](/category/apps/)
* [Disrupt 2025](https://techcrunch.com/events/tc-disrupt-2025/)

* [Events](/events/)
* [Podcasts](/podcasts/)
* [Newsletters](/newsletters/)

Search

Submit

Site Search Toggle

Mega Menu Toggle

### Topics

[Latest](/latest/)

[AI](/category/artificial-intelligence/)

[Amazon](/tag/amazon/)

[Apps](/category/apps/)

[Biotech & Health](/category/biotech-health/)

[Climate](/category/climate/)

[Cloud Computing](/tag/cloud-computing/)

[Commerce](/category/commerce/)

[Crypto](/category/cryptocurrency/)

[Enterprise](/category/enterprise/)

[EVs](/tag/evs/)

[Fintech](/category/fintech/)

[Fundraising](/category/fundraising/)

[Gadgets](/category/gadgets/)

[Gaming](/category/gaming/)

[Google](/tag/google/)

[Government & Policy](/category/government-policy/)

[Hardware](/category/hardware/)

[Instagram](/tag/instagram/)

[Layoffs](/tag/layoffs/)

[Media & Entertainment](/category/media-entertainment/)

[Meta](/tag/meta/)

[Microsoft](/tag/microsoft/)

[Privacy](/category/privacy/)

[Robotics](/category/robotics/)

[Security](/category/security/)

[Social](/category/social/)

[Space](/category/space/)

[Startups](/category/startups/)

[TikTok](/tag/tiktok/)

[Transportation](/category/transportation/)

[Venture](/category/venture/)

### More from TechCrunch

[Staff](/about-techcrunch/)

[Events](/events/)

[Startup Battlefield](/startup-battlefield/)

[StrictlyVC](https://strictlyvc.com/)

[Newsletters](/newsletters/)

[Podcasts](/podcasts/)

[Videos](/video/)

[Partner Content](/sponsored/)

[TechCrunch Brand Studio](/brand-studio/)

[Crunchboard](https://www.crunchboard.com/)

[Contact Us](/contact-us/)

![An Ecovacs Deebot T20 Omni.](https://techcrunch.com/wp-content/uploads/2024/08/ecovacs-vacuum-robot.png?w=1024)

**Image Credits:**[Ecovacs / YouTube (opens in a new window)](https://www.youtube.com/watch?v=jUMujy8sw2k)

[Security](https://techcrunch.com/category/security/)

# Ecovacs home robots can be hacked to spy on their owners, researchers say

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

1:00 PM PDT · August 9, 2024

Malicious hackers can take over control of vacuum and lawn mower robots made by Ecovacs to spy on their owners using the devices’ cameras and microphones, new research has found.

Security researchers Dennis Giese and Braelynn Luedtke are due to speak at the Def Con hacking conference on Saturday detailing their research into [Ecovacs](https://www.ecovacs.com/us) robots. When they analyzed several Ecovacs products, the two researchers found a number of issues that can be abused to hack the robots via Bluetooth and surreptitiously switch on microphones and cameras remotely.

“Their security was really, really, really, really bad,” Giese told TechCrunch in an interview ahead of the talk.

The researchers said they reached out to Ecovacs to report the vulnerabilities but never heard back from the company, and believe the vulnerabilities are still not fixed and could be exploited by hackers.

An Ecovacs spokesperson told TechCrunch that the company would not fix the flaws found by the researchers, saying that “users can rest assured that they do not need to worry excessively about this.”

The main issue, according to the researchers, is that there is a vulnerability that allows anyone using a phone to connect to and take over an Ecovacs robot via Bluetooth from as far away as 450 feet (around 130 meters). And once the hackers take control of the device, they can connect to it remotely because the robots themselves are connected via Wi-Fi to the internet.

“You send a payload that takes a second, and then it connects back to our machine. So this can, for example, connect back to a server on the internet. And from there, we can control the robot remotely,” said Giese. “We can read out to Wi-Fi credentials, we can read out all the [saved room] maps. We can, because we’re sitting on the operation of the robot’s Linux operating system. We can access cameras, microphones, whatever.”

![A dog on a couch in someone's house seen through the camera of a hacked Ecovacs device.](https://techcrunch.com/wp-content/uploads/2024/08/ecovacs-vulnerabilities-dog.png?w=680)

A dog seen through a hacked Ecovacs device. **Image Credits:**Dennis Giese and Braelynn Luedtke

Giese said that the lawn mower robots have Bluetooth active at all times, while the vacuum robots have Bluetooth enabled for 20 minutes when they switch on, and once a day when they do their automatic reboot, which makes them a bit harder to hack.

Because most of the newer Ecovacs robots are equipped with at least one camera and a microphone, once the hackers have control of a compromised robot, the robots can be turned into spies. The robots have no hardware light or any other indicator that warns people nearby that their cameras and microphones are on, according to the researchers.

On some models there is, in theory, an audio file that gets played every five minutes saying the camera is on but hackers could easily delete the file and stay stealthy, Giese said.

“You can basically just delete or overwrite the file with the empty one. So the warnings are not playing anymore if you access the camera remotely,” said Giese.

Apart from the risk of hacking, Giese and Luedtke said they found other problems with Ecovacs devices.

Among the issues, they said: The data stored on the robots remains on Ecovacs’ cloud servers even after deleting the user’s account; the authentication token also remains on the cloud, allowing someone to access a robot vacuum after deleting their account and potentially allowing them to spy on the person who may have purchased the robot secondhand. Also, the lawn mower robots have an anti-theft mechanism that forces someone to enter a PIN if they pick up the robot, but the PIN is stored in plaintext inside the lawn mower so a hacker could easily find it and use it.

The researchers said that once an Ecovacs robot is compromised, if the device is in range of other Ecovacs robots, those devices can be hacked, too.

Giese and Luedtke said they analyzed the following devices: Ecovacs Deebot 900 Series, Ecovacs Deebot N8/T8, Ecovacs Deebot N9/T9, Ecovacs Deebot N10/T10, Ecovacs Deebot X1, Ecovacs Deebot T20, Ecovacs Deebot X2, Ecovacs Goat G1, Ecovacs Spybot Airbot Z1, Ecovacs Airbot AVA, and the Ecovacs Airbot ANDY.

***UPDATE, Aug. 14, 1:22 p.m. ET**: This story has been updated to include Ecovacs’ statement.*

Topics

[cybersecurity](https://techcrunch.com/tag/cybersecurity/), [DEF CON](https://techcrunch.com/tag/def-con/), [ecovacs](https://techcrunch.com/tag/ecovacs/), [hackers](https://techcrunch.com/tag/hackers/), [hacking](https://techcrunch.com/tag/hacking/), [infosec](https://techcrunch.com/tag/infosec/), [Internet of Things](https://techcrunch.com/tag/internet-of-things/), [Robot Vacuums](https://techcrunch.com/tag/robot-vacuums/), [Robotics](https://techcrunch.com/category/robotics/), [Security](https://techcrunch.com/category/security/)

![Lorenzo Franceschi-Bicchierai](https://techcrunch.com/wp-content/uploads/2025/07/Lorenzo-headshot-2023-cropped.jpeg?w=150)

Lorenzo Franceschi-Bicchierai

Senior Reporter, Cybersecurity

Lorenzo Franceschi-Bicchierai is a Senior Writer at TechCrunch, where he covers hacking, cybersecurity, surveillance, and privacy.

You can contact or verify outreach from Lorenzo by emailing lorenzo@techcrunch.com, via encrypted message at +1 917 257 1382 on Signal, and @lorenzofb on Keybase/Telegram.

[View Bio](https://techcrunch.c...