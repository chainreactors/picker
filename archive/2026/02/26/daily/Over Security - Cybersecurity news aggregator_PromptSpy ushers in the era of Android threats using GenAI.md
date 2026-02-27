---
title: PromptSpy ushers in the era of Android threats using GenAI
url: https://www.welivesecurity.com/en/eset-research/promptspy-ushers-in-era-android-threats-using-genai/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-26
fetch_date: 2026-02-27T04:08:34.631466
---

# PromptSpy ushers in the era of Android threats using GenAI

[xml version="1.0" encoding="UTF-8"?](/en/ "WeLiveSecurity")

Award-winning news, views, and insight from the ESET security community

English

[Español](/es/ "Español")[Deutsch](/de/ "Deutsch")[Português](/pt/ "Português")[Français](/fr/ "Français")

[xml version="1.0" encoding="UTF-8"?](/en/ "WeLiveSecurity")

* [TIPS & ADVICE](/en/tips-advice/ "TIPS & ADVICE")

---

* [BUSINESS SECURITY](/en/business-security/ "BUSINESS SECURITY")

---

* ESET RESEARCH

  [About ESET Research](/en/about-eset-research/ "About ESET Research")[Blogposts](/en/eset-research/ "Blogposts")[Podcasts](/en/podcasts/ "Podcasts")[White papers](/en/white-papers/ "White papers")[Threat reports](/en/threat-reports/ "Threat reports")

---

* [WeLiveScience](/en/we-live-science/ "WeLiveScience")

---

* FEATURED

  [Ukraine crisis – Digital security resource center](/en/ukraine-crisis-digital-security-resource-center/ "Ukraine crisis – Digital security resource center")[WeLiveProgress](/en/we-live-progress/ "WeLiveProgress")[COVID-19](/en/covid-19/ "COVID-19")[Resources](/en/resources/ "Resources")[Videos](/en/videos/ "Videos")

---

* TOPICS

  [Digital Security](/en/cybersecurity/ "Digital Security")[Scams](/en/scams/ "Scams")[How to](/en/how-to/ "How to")[Privacy](/en/privacy/ "Privacy")[Cybercrime](/en/cybercrime/ "Cybercrime")[Kids online](/en/kids-online/ "Kids online")[Social media](/en/social-media/ "Social media")[Internet of Things](/en/internet-of-things/ "Internet of Things")[Malware](/en/malware/ "Malware")[Ransomware](/en/ransomware/ "Ransomware")[Secure coding](/en/secure-coding/ "Secure coding")[Mobile security](/en/mobile-security/ "Mobile security")[Critical infrastructure](/en/critical-infrastructure/ "Critical infrastructure")[Threat research](/en/about-eset-research/ "Threat research")

---

* ABOUT US

  [About WeLiveSecurity](/en/company/about-us/ "About WeLiveSecurity")[Our Experts](/en/our-experts/ "Our Experts")[Contact Us](/en/company/contact-us/ "Contact Us")

---

* [English](/en/ "English")

  [Español](/es/ "Español")[Deutsch](/de/ "Deutsch")[Português](/pt/ "Português")[Français](/fr/ "Français")

Award-winning news, views, and insight from the ESET security community

ESET Research

# PromptSpy ushers in the era of Android threats using GenAI

ESET researchers discover PromptSpy, the first known Android malware to abuse generative AI in its execution flow

[![Lukas Stefanko](https://web-assets.esetstatic.com/tn/-x45/wls/2023/07/lukas-stefanko.jpeg)](/en/our-experts/lukas-stefanko/ "Lukas Stefanko")

[**Lukas Stefanko**](/en/our-experts/lukas-stefanko/ "Lukas Stefanko")

19 Feb 2026
 •
,
14 min. read

![PromptSpy ushers in the era of Android threats using GenAI](https://web-assets.esetstatic.com/tn/-x700/wls/2026/02-26/promptspy/promptspy-gemini-genai-malware.jpg)

ESET researchers uncovered the first known case of Android malware abusing generative AI for context-aware user interface manipulation. While machine learning has been used to similar ends already – just recently, researchers at Dr.WEB found [Android.Phantom](https://news.drweb.com/show/?i=15110), which uses TensorFlow machine learning models to analyze advertisement screenshots and automatically click on detected elements for large scale ad fraud – this is the first time we have seen generative AI deployed in this manner. Because the attackers rely on prompting an AI model (in this instance, Google’s Gemini) to guide malicious UI manipulation, we have named this family PromptSpy. This is the second AI powered malware we have discovered – following [PromptLock](https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/) in August 2025, the first known case of AI-driven ransomware.

While generative AI is deployed only in a relatively minor part of PromptSpy's code – that responsible for achieving persistence – it still has a significant impact on the malware's adaptability. Specifically, Gemini is used to analyze the current screen and provide PromptSpy with step-by-step instructions on how to ensure the malicious app remains pinned in the recent apps list, thus preventing it from being easily swiped away or killed by the system. The AI model and prompt are predefined in the code and cannot be changed. Since Android malware often relies on UI navigation, leveraging generative AI enables the threat actors to adapt to more or less any device, layout, or OS version, which can greatly expand the pool of potential victims.

The main purpose of PromptSpy is to deploy a built-in VNC module, giving operators remote access to the victim’s device. This Android malware also abuses the Accessibility Service to block uninstallation with invisible overlays, captures lockscreen data, records video. It communicates with its C&C server via the VNC protocol, using AES encryption.

Based on language localization clues and the distribution vectors observed during analysis, this campaign appears to be financially motivated and seems to primarily target users in Argentina. Interestingly, analyzed PromptSpy samples suggest that it was developed in a Chinese‑speaking environment.

PromptSpy is distributed by a dedicated website and has never been available on Google Play. As an App Defense Alliance partner, we nevertheless shared our findings with Google. Android users are automatically protected against known versions of this malware by [Google Play Protect](https://support.google.com/googleplay/answer/2812853?hl=en), which is enabled by default on Android devices with Google Play Services.

> **Key points of this blogpost:**
>
> * PromptSpy is the first known Android malware to use generative AI in its execution flow, even though it’s only to achieve persistence.
> * Google's Gemini is used to interpret on-screen elements on the compromised device and provide PromptSpy with dynamic instructions on how to execute a specific gesture to remain in the recent app list.
> * The main (non-generative-AI-assisted) purpose of PromptSpy is to deploy a VNC module on the victim's device, allowing attackers to see the screen and perform actions remotely.
> * PromptSpy has not been observed in our telemetry yet, making it a possible proof of concept; however, the discovery of a likely distribution domain suggests the existence of a variant targeting users in Argentina.
> * PromptSpy can capture lockscreen data, block uninstallation, gather device info, take screenshots, record screen activity as video, and more.

## PromptSpy’s AI-powered functionality

Even though PromptSpy uses Gemini in just one of its features, it still demonstrates how incorporating these AI tools can make malware more dynamic, giving threat actors ways to automate actions that would normally be more difficult with traditional scripting.

As was briefly mentioned already, Android malware usually depends on hardcoded screen features such as taps, coordinates, or UI selectors – methods that can break with UI changes across devices, OS versions, or manufacturer skins. PromptSpy aims to achieve persistence by staying embedded in the list of recent apps by executing the “lock app in recent apps” gesture (the full process is described in the *[Analysis](#Analysis)* section), which varies between devices and manufacturers. This makes it difficult to automate with fixed scripts traditionally used by Android malware.

PromptSpy therefore takes a completely different approach: it sends Gemini a natural‑language prompt along with an XML dump of the current screen, giving the AI a detailed view of every UI element: its text, type, and exact position on the display.

Gemini processes this information and responds with JSON instructions that tell the malware what action to perform (for example, a tap) and where to perform it. The malware saves both its previous prompts and Gemini’s responses, allowing Gemini to understand context and to coordinate multistep interactions.

Figure 1 shows a code snippet of PromptSpy’s init...