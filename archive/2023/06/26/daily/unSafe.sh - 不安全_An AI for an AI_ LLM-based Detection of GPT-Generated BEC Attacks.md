---
title: An AI for an AI: LLM-based Detection of GPT-Generated BEC Attacks
url: https://buaq.net/go-170234.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:44:48.249257
---

# An AI for an AI: LLM-based Detection of GPT-Generated BEC Attacks

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/eec9a8eb83af89061b1ffcfbb61edade.jpg)

An AI for an AI: LLM-based Detection of GPT-Generated BEC Attacks

Step into the new frontier of cyber threats, where GenAI has created a seismic shift, allowing
*2023-6-25 19:11:19
Author: [perception-point.io(查看原文)](/jump-170234.htm)
阅读量:28
收藏*

---

Step into the new frontier of cyber threats, where GenAI has created a seismic shift, allowing adversaries to easily craft new social engineering attacks and outsmart traditional detection tools.

## GenAI: The New Frontier of Cyber Security

In the increasingly volatile threat landscape, the challenges cyber defenders are up against is perpetually evolving. Today, we stand at the brink of a new frontier – one defined by harnessing revolutionary AI technologies to create new malware and malicious social engineering ploys that are highly convincing and strategically crafted. This frontier is defined by [Generative AI](https://www.techtarget.com/searchenterpriseai/definition/generative-AI) (GenAI), which is [being exploited by threat actors](https://www.forbes.com/sites/forbestechcouncil/2023/02/13/how-to-protect-against-ai-based-email-security-threat-vectors/?sh=47ca4fee1225) to design and launch sophisticated, highly targeted attacks against organizations worldwide.

## Understanding Generative AI and Its Capabilities

Before we delve into the risks, let’s first understand what Generative AI is. GenAI represents a collection of machine learning technologies capable of creating high-quality output that has traditionally required a human touch. Whether it’s writing captivating articles, crafting compelling stories, or even creating sophisticated [deepfake videos](https://www.aicpa-cima.com/news/article/deepfakes-emerge-as-real-cybersecurity-threat), democratized GenAI has it all covered.

[Large Language Models](https://www.techtarget.com/whatis/definition/large-language-model-LLM) (LLMs) like [OpenAI](https://openai.com/)‘s ChatGPT, Google’s [Bard](https://bard.google.com/), and others are now capable of generating content that’s almost indistinguishable from human-written texts. And while this is a fascinating achievement in the realm of artificial intelligence, it poses a significant threat in the wrong hands.

## The Abuse of GenAI in BEC Attacks

Imagine receiving an email that looks like it’s from your boss, or from a trusted vendor you’ve worked with for years, or even your bank. It’s personalized to you, contextually relevant, and grammatically perfect. It’s convincing. Except it’s not exactly real. It’s a product of GenAI, carefully crafted by adversaries to manipulate emotions, build false trust, and ultimately, to “social engineer” the recipient of the email into falling for a scam, clicking a link, downloading a file, or even transferring money.

The Verizon’s [Data Breach Investigations Report (DBIR) 2023](https://www.verizon.com/business/resources/reports/dbir/?CMP=OOH_SMB_OTH_22222_MC_20200501_NA_NM20200079_00001) shows that social engineering attacks have become increasingly prevalent in 2023, in which [Business Email Compromise (BEC)](https://perception-point.io/guides/bec/business-email-compromise/) attacks **have nearly doubled, accounting for over 50%** of incidents involving social engineering techniques ([phishing](https://perception-point.io/spearphishing/) is a close second).

[Impersonation](https://perception-point.io/guides/bec/business-email-compromise/), phishing, and especially BEC attacks are now being “supercharged” with the [power of GenAI](https://perception-point.io/blog/ai-the-double-edged-sword-of-cybersecurity/) (particularly LLMs), allowing cyber criminals to work faster, and on a much larger scale than ever before. Previously time-consuming preparation work, such as target research and reconnaissance, “copywriting”, and design, can now be done within minutes by using well-crafted prompts. This means more potential victims and an increased likelihood of successful attacks. Perception Point’s [2023 Annual Report](https://perception-point.io/resources/report/2023-annual-report/) highlights an alarming 83% growth in BEC attack attempts in 2022.

![](https://lh5.googleusercontent.com/AyRvBB-tYzi6yblC6juDqADh2OXNcdRr447pXFogWrGxD4r7u-6zV3Wtx88yYAdlc002I69pbG3nTRIn51it3YJNALe1-JLlHXDPAqSnzvVIzJTf0gaKfajwDCXD6J7jX8QpzJPB9_P-7O0e0EnqCtw)

*Sample GenAI-generated BEC attack caught by Perception Point*

## A Critical Need for GenAI Detection Technology

As [GenAI continues to become more accessible](https://hbr.org/2018/01/what-changes-when-ai-is-so-accessible-that-everyone-can-use-it), the risks it poses become increasingly significant. Traditional email security solutions, designed to detect typical indicators of phishing or other malicious emails, are struggling to keep up. They are not designed to handle the sophistication and subtleties of GenAI-generated content. This in itself highlights the need for a new breed of detection capabilities specifically designed to counter GenAI attacks.

Contextual and behavioral detection methods, like those utilized by Abnormal Security, IronScales, Tessian, Avanan and other security vendors, have shown effectiveness against traditional BEC and phishing attacks. However, they somewhat struggle against GenAI-powered attacks. GenAI can help craft personalized, contextually apt, and grammatically sound emails that mimic legitimate communication, bypassing the usual patterns these detection methods rely on. Moreover, if fed enough data, for example by leveraging “[thread hijacking](https://perception-point.io/blog/beware-4-advanced-attack-examples-you-should-know-about/)”, tools like ChatGPT can easily simulate the impersonated user behavior and writing style, further complicating detection.

Recognizing this growing threat, [Perception Point](https://perception-point.io/) has developed a state-of-the-art LLM-based detection model, specifically designed to identify the use of GenAI in malicious emails. This is a game-changing approach, augmenting the ability to protect organizations not just from the human-written email threats (sophisticated as they may be), but also from the up and coming new wave of machine-generated cyber attacks.

## GenAI Decoded: Perception Point’s Answer to LLM-Generated Social Engineering

Perception Point’s innovative detection solution combats GenAI-generated social engineering and BEC threats by leveraging the power of [Transformers](https://en.wikipedia.org/wiki/Transformer_%28machine_learning_model%29), AI models capable of understanding the semantic context of text, very similar to the technology behind GenAI and LLMs (GPT-4, LLaMA, PaLM2, etc.). The strength of this approach lies in recognizing the repetition of identifiable patterns in LLM-generated text.

The innovative model uses these patterns to identify potential threats. It groups, or “clusters”, emails with similar semantic content, allowing it to distinguish between emails within the same group, and thus pinpoint patterns characteristic of LLM-generated content. The model was initially trained on hundreds of thousands malicious emails and is continuously trained on novel attacks.

## How It Works

When an email is processed by Perception Point, the model evaluates its content and provides a probability score within milliseconds, ranging from 0 to 1. This score indicates the likelihood that the email was generated by an LLM and also its potential for malicious intent. In addition, the model delivers a descriptive textual analysis explaining the potential threat, if the content is determined as malicious in nature.

To illustrate t...