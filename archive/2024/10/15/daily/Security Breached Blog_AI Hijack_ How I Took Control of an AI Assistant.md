---
title: AI Hijack: How I Took Control of an AI Assistant
url: https://blog.securitybreached.org/2024/10/14/ai-hijack-how-i-took-control-of-an-ai-assistant/
source: Security Breached Blog
date: 2024-10-15
fetch_date: 2025-10-06T18:56:51.056567
---

# AI Hijack: How I Took Control of an AI Assistant

[Skip to content](#page)

[Security Breached Blog](https://blog.securitybreached.org/)

Hack Smart, Stay Safe: Comprehensive Guides to Cybersecurity and Bug Bounty

October 14, 2024

Share

* [BugBounty POC](https://blog.securitybreached.org/category/bugbounty-poc/)
* [0](https://blog.securitybreached.org/2024/10/14/ai-hijack-how-i-took-control-of-an-ai-assistant/#respond)

# AI Hijack: How I Took Control of an AI Assistant

[![](https://secure.gravatar.com/avatar/ef54bde2238ac374f791981be3203fa54846df4f19d8690ea5d4b924daca55b4?s=64&r=g)](https://blog.securitybreached.org/author/babayaga47/)

by [MuhammadKhizerJaved](https://blog.securitybreached.org/author/babayaga47/ "Posts by MuhammadKhizerJaved")

Hi Everyone! Welcome back! It’s been a while since I’ve written a blog, so I decided to share this recent discovery with you all today. This finding highlights the importance of API key security in AI-powered applications.

In this blog post, we’ll explore how I uncovered and exploited an **OpenAI API** key that allowed me to take control of an AI assistant in a production environment. This discovery not only demonstrates the potential risks associated with AI integration but also emphasizes the need for robust security practices in the rapidly evolving field of AI-powered solutions.

## What is an AI Assistants?

Before we delve into the details of the vulnerability, let’s briefly discuss what AI assistants are.

AI assistants are sophisticated software applications powered by large language models, such as OpenAI’s GPT-4. According to [OpenAI](https://platform.openai.com/docs/assistants/overview) “The Assistants API allows you to build AI assistants within your own applications. An Assistant has instructions and can leverage models, tools, and files to respond to user queries.” These assistants can understand and generate human-like text, making them valuable tools for various tasks, including customer support, content creation, and data analysis.

Protecting these assistants is important, as their misconfiguration can lead to unauthorized access, data breaches, and potential misuse of AI capabilities.

## The Discovery Process

The journey of this bug began with a routine overview of a website that leverage AI for it’s main business features. On the homepage the site featured a prompt area where users could interact with an AI assistant. As always, I started with some basic reconnaissance.

[![](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/Web_Target_homepage.png?resize=620%2C141&ssl=1)](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/Web_Target_homepage.png?ssl=1)

### Initial Interaction

I asked the AI assistant a simple question: “**Are you based on OpenAI? If yes, then which AI model are you based on?**” The response was quite revealing:

`"Yes, I am based on OpenAI's language models. I'm specifically powered by the GPT-4 model, which is designed to assist with a wide variety of tasks, including user research and assessments. To help match you with the right expert, may I know your first name?"`

This confirmation that the assistant was powered by **OpenAI’s GPT-4** model gave me a clear direction for my investigation.

[![](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/initial_prompt_question.png?resize=620%2C139&ssl=1)](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/initial_prompt_question.png?ssl=1)

### Burp Suite BCheck

After some unsuccessful attempts at prompt injection, I decided to look for any information related to the AI assistant in the website’s JavaScript files, particularly focusing on API key exposure. To automate this process, I created a simple Burp Suite BCheck:

```
metadata:
    language: v2-beta
    name: "OpenAI API Key Exposure (passive)"
    description: "Looks for leaked OpenAI API keys (sk- or sess-) in response bodies."
    author: "@KHIZER_JAVED47"
    tags: "passive", "token", "exposure", "openai"
given response then
    if {latest.response} matches "(sk-[A-Za-z0-9_-]{32,})|(sess-[A-Za-z0-9]{40})" then
        report issue:
            severity: high
            confidence: firm
            detail: "Leaked OpenAI API key found in the response. OpenAI API keys beginning with 'sk-' or 'sess-' were detected, which could lead to unauthorized access."
            remediation: "Immediately revoke the exposed key, generate a new key, and ensure sensitive keys are never exposed in client-side responses."

    end if
```

[![](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/burp_bcheck.png?resize=620%2C202&ssl=1)](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/burp_bcheck.png?ssl=1)

This BCheck passively scans responses for patterns matching OpenAI API keys. To my surprise, it quickly identified a hardcoded API key in the website’s `main.js` file.

[![](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/bcheck_alert.png?resize=620%2C330&ssl=1)](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/bcheck_alert.png?ssl=1)

[![](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/openai_api_key_laked_in_js_file.png?resize=620%2C259&ssl=1)](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/openai_api_key_laked_in_js_file.png?ssl=1)

## Exploiting the Vulnerability

With the API key in hand, I turned to the [OpenAI API documentation](https://platform.openai.com/docs/api-reference/introduction) to understand how I could leverage this access. I crafted a series of requests to explore the extent of the vulnerability.

### Accessing OpenAI API Endpoints

First, I listed all the AI models accessible with the leaked API key:

```
GET /v1/models HTTP/2
Host: api.openai.com
User-Agent: ct/JS 4.53.2
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Authorization: Bearer sk-vjK....-Leaked-API-KEY
Openai-Beta: assistants=v2
```

[![](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/openai_models_list.png?resize=620%2C327&ssl=1)](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/openai_models_list.png?ssl=1)

This request successfully returned a list of all available models, confirming that the API key was indeed valid and had broad access.

Next, I queried the assistants associated with this API key:

```
GET /v1/assistants HTTP/2
Host: api.openai.com
User-Agent: ct/JS 4.53.2
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Authorization: Bearer sk-vjK....-Leaked-API-KEY
Openai-Beta: assistants=v2
```

[![](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/openai_assistants_list.png?resize=620%2C232&ssl=1)](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2024/10/openai_assistants_list.png?ssl=1)

This request revealed all the AI assistants created by the company, including their unique instructions and configurations.

The Initial AI Assistant had the following Set of Instructions

```
   {
      "id": "asst_Assistant_id",
      "object": "assistant",
      "created_at": 1728850042,
      "name": "Angelina",
      "description": null,
      "model": "gpt-4o",
      "instructions": "\nYou are an expert user researcher that knows how to ask the right questions to clearly understand a user's redacted needs. Your goal is to collect information to then match the user with a redacted expert. Feel free to respond to the user in a natural tone, and offer encouragement and support throughout the conversation. Ask the user for their first name first and use their name at-will in follow up responses.\n\nJSON Response Format: Format each response as follows:\n  {\n    \"assistant_response\": {\n      content: \"\", // contains the response content, concluding with a question mark.\n      question_type: \"\"...