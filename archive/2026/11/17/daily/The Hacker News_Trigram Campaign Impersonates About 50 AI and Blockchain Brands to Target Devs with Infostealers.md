---
title: Trigram Campaign Impersonates About 50 AI and Blockchain Brands to Target Devs with Infostealers
url: https://thehackernews.com/2026/11/trigram-campaign-impersonates-about-50.html
source: The Hacker News
date: 2026-11-17
fetch_date: 2026-11-18T09:22:48.477681
---

# Trigram Campaign Impersonates About 50 AI and Blockchain Brands to Target Devs with Infostealers

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Trigram Campaign Impersonates About 50 AI and Blockchain Brands to Target Devs with Infostealers](https://thehackernews.com/2026/11/trigram-campaign-impersonates-about-50.html)

**Ravie Lakshmanan**Nov 17, 2026Malware / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXvywoP0qreCtUhDgAD1y24HevVHwAH9bGo904BuaQ7-amvdkk6Oi8gz8WjF-Hwiu3SinN266QM0KwUX6lDnayGOtMaSEff_b5vybBsdwvDhiai2uGsAlYfMgCdquPmKqaqM6eY54pG9HsMR7X5Sf7M4nkbIaHmWJMBG1uL3ggpJMMvfQR6FbMagqug2QG/s1700-nu-rw-lo-l85-e365/target.jpg)

Artificial intelligence (AI), blockchain, and logistics sectors across Europe and the U.S. have emerged as the target of a large-scale, industrialized campaign dubbed **Trigram**.

"Trigram is a large-scale campaign that impersonates about 50 brands in the blockchain and AI sectors, to trick developers into executing an infostealer themselves," Stormshield [said](https://www.stormshield.com/news/cti-trigram-campaign/) in a deep-dive technical report published Monday.

"Three social engineering scenarios (recruitment, conference, and package tracking), a software supply-chain compromise, and trojanized code repositories all converge on the same infrastructure and the same payload."

The activity is assessed to share similarities with intrusion sets linked to North Korea, particularly **Kimsuky** and **UNK\_DeadDrop**. Some aspects of this campaign have been previously documented by [Proofpoint](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html), SafeDep, [Jamf](https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html), and [Genians Security Center](https://thehackernews.com/2026/09/weekly-recap-387m-crypto-hack-citrix.html#:~:text=Kimsuky%20Conducts%20Git%2DBased%20C2%20Attacks).

It's worth noting that the cluster tracked as UNK\_DeadDrop exhibits similarities with a long-running North Korea-aligned campaign referred to as [Contagious Interview](https://thehackernews.com/2026/11/fbi-says-north-korean-hackers-stole.html#from-facestealer-to-contagious-interview). First observed between April and May 2026, it employs phishing emails using developer role recruitment or code review themes to target developers across finance, cryptocurrency, education, and technology sectors to deploy an information stealer.

On Linux and macOS systems, the attack chains lead to the deployment of Overlord, an open-source remote access trojan (RAT) framework to facilitate data theft.

Then, in August 2026, Jamf Threat Labs [disclosed](https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html) details of a macOS campaign using a fake Zoom installer to deploy Overlord RAT, although the Apple device management company said at the time that it found no "direct overlap" between the activity and UNK\_DeadDrop.

"The Overlord variant observed here shares a LaunchAgent label (com.zoom) and plist name (com.zoom.plist) with [FlexibleFerret](https://thehackernews.com/2025/02/north-korean-hackers-deploy-ferret.html), a DPRK-attributed macOS malware family associated with the Contagious Interview campaign," it added.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Overlord has also been distributed as recently as late October 2026 via another channel: a forged commit in the antd-img-crop GitHub repository that installs the malware by means of a prebuild hook ("prebuild.js") as soon as a developer runs the "npm run build" command. The npm package in itself was not impacted.

The JavaScript payload is designed to download and run a fake installer that sets up Node.js and fetches an encrypted JavaScript next-stage that runs entirely in memory and locates its command-and-control (C2) server via a GitLab dead-drop. The third-stage malware is responsible for harvesting credentials and installing the OverLord framework.

"The malware steals browser passwords, cookies, keychains, cryptocurrency wallets, SSH keys and .env files on macOS, Linux and Windows, then installs a remote-access agent disguised as Google software," SafeDep [said](https://safedep.io/blog/antd-img-crop-forged-commit-overlord-stealer) in an analysis of the malware.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3Gpkk7pRRk6xMNKk7RxEIQFLeQwfG1VhugvdCgvUgqcYqLDtzaUAlTkYao3dz5yrx66JVde5OTHFG7CSViY5bNObTHAgdvkQI_4Qk94MzrV4-cYaa17zLOx5uzv9fA2fCZAa4M87eJaG1MVGIKA1_qbu-i2oZf9njF7NbFFZh2HmDx9UxjTXOrHNK-_3N/s1700-nu-rw-lo-l85-e365/1.jpg) |
| The forged commit pushed to "antd-img-crop⁠" on October 31, 2026 |

On macOS and Linux systems, it also displays a fake dialog asking users to enter their system password so as to "apply system updates and verify drivers and security settings." Interestingly, the same payload is delivered via two other initial access vectors -

* A fake careers portal impersonating Amber Group, a legitimate cryptocurrency firm
* A sideloaded Microsoft Visual Studio Code (VS Code) or Cursor extension named "google-dev-tools.google-update-support" that's likely launched via a coding assessment and deleted after it's run

"The fake recruiter, the paste-a-command 'verification' step and the focus on developers and cryptocurrency holders match the publicly documented Contagious Interview campaign," SafeDep said. "The match rests on technique and does not prove who the operators are."

The third branch of the campaign revolves around another cluster tracked by Genians as [Operation GitPower](https://www.genians.co.kr/en/blog/threat_intelligence/kimsuky_ai_llm). Attributed to the Kimsuky group, the activity [involves](https://www.octoprobe.ai/blog/kimsuky-operation-gitpower-github-c2/) operating local large language model (LLM) environments using Ollama and GPT4All to generate decoy documents and use them to target professionals and organizations in the fields of policy, academia, international cooperation, diplomacy, and security research.

Present w...