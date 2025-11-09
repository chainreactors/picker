---
title: Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic
url: https://thehackernews.com/2025/11/microsoft-uncovers-whisper-leak-attack.html
source: The Hacker News
date: 2025-11-08
fetch_date: 2025-11-09T03:14:47.620917
---

# Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Microsoft Uncovers 'Whisper Leak' Attack That Identifies AI Chat Topics in Encrypted Traffic](https://thehackernews.com/2025/11/microsoft-uncovers-whisper-leak-attack.html)

**Nov 08, 2025**Ravie LakshmananNetwork Security / Data Protection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpBHsV_c7cesyV98XY3_PW3Ag8I1NBsboj592iw07Rlmy2xCs3QTpBUcZf59rmLBCo4JppU4HFF9GU8H7i_ADzqyvO_IxWj3GZWoVkzsh4GRWHyD1LSPWZgUEii8SnZE_BJxTmJMdG8RfstqNmGNIRcUdshTfQcPTJRVzVUJopn6FrCk5KvI0xc18Vy7bk/s2600/ai-leak.jpg)

Microsoft has disclosed details of a novel side-channel attack targeting remote language models that could enable a passive adversary with capabilities to observe network traffic to glean details about model conversation topics despite encryption protections under certain circumstances.

This leakage of data exchanged between humans and streaming-mode language models could pose serious risks to the privacy of user and enterprise communications, the company noted. The [attack](https://arxiv.org/abs/2511.03675) has been codenamed **Whisper Leak**.

"Cyber attackers in a position to observe the encrypted traffic (for example, a nation-state actor at the internet service provider layer, someone on the local network, or someone connected to the same Wi-Fi router) could use this cyber attack to infer if the user's prompt is on a specific topic," security researchers Jonathan Bar Or and Geoff McDonald, along with the Microsoft Defender Security Research Team, [said](https://www.microsoft.com/en-us/security/blog/2025/11/07/whisper-leak-a-novel-side-channel-cyberattack-on-remote-language-models/).

Put differently, the attack allows an attacker to observe encrypted TLS traffic between a user and LLM service, extract packet size and timing sequences, and use trained classifiers to infer whether the conversation topic matches a sensitive target category.

Model streaming in large language models ([LLMs](https://en.wikipedia.org/wiki/Large_language_model)) is a technique that allows for incremental data reception as the model generates responses, instead of having to wait for the entire output to be computed. It's a critical feedback mechanism as certain responses can take time, depending on the complexity of the prompt or task.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The latest technique demonstrated by Microsoft is significant, not least because it works despite the fact that the communications with artificial intelligence (AI) chatbots are encrypted with HTTPS, which ensures that the contents of the exchange stay secure and cannot be tampered with.

Many a side-channel attack has been devised against LLMs in recent years, including the ability to [infer the length of individual plaintext tokens](https://arxiv.org/abs/2403.09751) from the size of encrypted packets in streaming model responses or by exploiting timing differences caused by caching LLM inferences to execute input theft (aka [InputSnatch](https://arxiv.org/abs/2411.18191)).

Whisper Leak builds upon these findings to explore the possibility that "the sequence of encrypted packet sizes and inter-arrival times during a streaming language model response contains enough information to classify the topic of the initial prompt, even in the cases where responses are streamed in groupings of tokens," per Microsoft.

To test this hypothesis, the Windows maker said it trained a binary classifier as a proof-of-concept that's capable of differentiating between a specific topic prompt and the rest (i.e., noise) using three different machine learning models: [LightGBM](https://github.com/microsoft/LightGBM), [Bi-LSTM](https://www.sciencedirect.com/science/article/pii/S1319157823004196), and [BERT](https://en.wikipedia.org/wiki/BERT_%28language_model%29).

The result is that many models from Mistral, xAI, DeepSeek, and OpenAI have been found to achieve scores above 98%, thereby making it possible for an attacker monitoring random conversations with the chatbots to reliably flag that specific topic.

"If a government agency or internet service provider were monitoring traffic to a popular AI chatbot, they could reliably identify users asking questions about specific sensitive topics – whether that's money laundering, political dissent, or other monitored subjects – even though all the traffic is encrypted," Microsoft said.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgplFdSOeej6uU261lrCy1TA65VnGEjhawsFcilFTTEiAvfyBlhjEF8o5fy-o7KikHXoiDZWb9WM-_k6m3fV59-eSIOOUEmjT8mFDAAWrA2GQuYj408_VMd3-kodQjWkNPRGqF5EGkUb3kNAGDCcZM8dIVtPOSkNQraiqIRRwA-IImcRKzWmhXdWoYVNQ6v/s2600/remotellm.jpg) |
| Whisper Leak attack pipeline |

To make matters worse, the researchers found that the effectiveness of Whisper Leak can improve as the attacker collects more training samples over time, turning it into a practical threat. Following responsible disclosure, OpenAI, Mistral, Microsoft, and xAI have all deployed mitigations to counter the risk.

"Combined with more sophisticated attack models and the richer patterns available in multi-turn conversations or multiple conversations from the same user, this means a cyberattacker with patience and resources could achieve higher success rates than our initial results suggest," it added.

One effective countermeasure devised by OpenAI, Microsoft, and Mistral involves adding a "random sequence of text of variable length" to each response, which, in turn, masks the length of each token to render the side-channel moot.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Microsoft is also recommending that users concerned about their privacy when talking to AI providers can avoid discussing highly sensitive topics when using untrusted networks, utilize a VPN for an extra layer of protection, use non-streaming models of LLMs, and switch to providers that have implemented mitigations.

The disclosure com...