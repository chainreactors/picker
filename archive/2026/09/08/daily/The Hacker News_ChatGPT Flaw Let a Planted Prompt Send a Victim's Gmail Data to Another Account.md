---
title: ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account
url: https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html
source: The Hacker News
date: 2026-09-08
fetch_date: 2026-09-09T06:56:58.339247
---

# ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account](https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html)

**Ravie Lakshmanan**Sep 08, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0jB-6O69dYNeqBTcSFXPcSQCqwabmHwmdGzC_ne5LyuUH-9v0MpLbJ1cgApFSqTuGG0Z_fKAD4A7gLcBcTdw6oUIv0nh_Pmyb5Obv7XhRY0jVGwPQ50S7rUnYZR8FUvYntVxL03GYJ010-iagkPkeZJ8oV6gvbEaVJPGw-L2rabD5pqOOu2HYW9g_nFcT/s1700-nu-rw-lo-l85-e365/chatgpt-gmail.jpg)

Check Point Research said in a report published today that a single instruction planted in a ChatGPT conversation could cause ChatGPT to quietly work for an attacker while answering the user's question as usual.

In the company's proof of concept, that hidden work read data from the user's connected Gmail account and passed it to a second ChatGPT account through a hidden channel between the two. The reply the user saw said nothing about it.

[Check Point](https://research.checkpoint.com/2026/the-shared-clipboard-inside-the-sandbox-cross-account-data-leakage-in-chatgpt/) said the same channel could also copy out the chat history and the files in that conversation.

How much an attacker could take depended on what the session could already access, including its data, tools, other connected apps, and permissions.

The instruction had to be in the conversation before any of this worked. Check Point named three ways to get it there: a prompt the user pastes in, a shared ChatGPT conversation the user opens, or a custom GPT that holds it in its builder instructions, which are not shown to the user.

After that, one ordinary message was enough to start it. Check Point wrote the instruction so that ChatGPT, in Thinking mode, ran two streams of work in the same turn.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

ChatGPT answered the user. At the same time, it checked a hidden mailbox for a task from the attacker, carried out that task using the tools in the user's session, and sent the result back. The instruction told the model to keep the two streams separate, so the hidden task never appeared in the visible answer.

The only sign that an app had been used was a small "Talked to Gmail" label above the answer. It recorded a read that had already happened and gave the user no chance to allow or refuse it.

Nothing asked the user first because of how connected apps work by default. OpenAI's documentation lists [Important actions](https://help.openai.com/en/articles/11487775-apps-in-chatgpt) as the default permission, which allows ChatGPT to read from an app without prompting. ChatGPT asks only before actions that could have a real effect outside ChatGPT, expose sensitive information, or be hard to undo.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKQcL7Wh3VP52_K0egOntbfTkF6xlJKpmTFaB8M184oLZbPLna-iXMjk5qbWQV9SFKG8a9EOXXLr0Q7X1Tt7iREpwPB14bDRWpNls0wlEoFlb17qDrLL7YQSg5S6vfwFxgZSaamUh7eNyJE0NtIn4kSk3IOG8aKcdigmQTWyYbVFgB5ZyK4bpYZqItxvsE/s1700-nu-rw-lo-l85-e365/gmail.png)

A user who wants to be asked every time can switch to Always ask. In Business, Enterprise, and Edu workspaces, admins choose which actions each app may take and who may use it. Apps are on by default on Business plans and off by default on Enterprise and Edu.

Check Point said it disclosed the finding to OpenAI and that OpenAI confirmed the internal service behind the channel had been taken offline. There is no update for users to install.

The channel ran between the containers where ChatGPT runs code. ChatGPT builds one for each conversation when a task calls for it.

OpenAI's [documentation](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt) says the Python environment ChatGPT uses for data analysis cannot make requests to the web or to outside APIs. Check Point said containers built for separate conversations, including ones under different accounts, had no direct path to each other either.

All of them could reach one internal service. ChatGPT sometimes needs to install extra Python or npm packages. Rather than allowing the containers to reach public package repositories, each was allowed to talk to an internal JFrog Artifactory instance that fetched packages for it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_93FvHQPCJB30TthzwinZMPby3k-uLilFvrmCzWF31LIqOnSRJ7_N1qrIK9B62-84qidFpRtMrrJSLYjcyGfE5zWSldw8f6cmqIxkHVN01qbDNOTnsGJ-piQl7enpL6ihku4CtlcNUcAiyS8wfJB71HC_QDQzCEPkT8NYuQz3zvPEB0b5WMHyYuj_D5MF/s1700-nu-rw-lo-l85-e365/jj.png)

That instance let a container attach named values, called properties, to a stored file and read them back. The credentials the container held for read access were also enough to write those properties. They sat in environment variables, where code that ChatGPT ran could pick them up. The code did not need to steal a separate secret or escalate privileges.

The properties were not kept separate by account. From a container under one account, Check Point attached a property named chatgpt\_test\_ts, containing the current time, to a cached file. In a conversation under a different account, it requested that file's properties and received the same name and value.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

A property can carry plain text or Base64, and anything too large for one can be split across several and reassembled at the other end. That turned the package service's metadata into a shared clipboard between containers that were not supposed to reach each other.

This is the second channel out of the same part of ChatGPT that Check Point has reported. In [March](https://thehackernews.com/2026/03/openai-patches-chatgpt-data.html), it described one that used DNS lookups to send conversation data to an external server, and said OpenAI ...