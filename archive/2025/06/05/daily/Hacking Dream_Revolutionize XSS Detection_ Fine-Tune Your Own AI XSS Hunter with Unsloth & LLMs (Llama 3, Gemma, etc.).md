---
title: Revolutionize XSS Detection: Fine-Tune Your Own AI XSS Hunter with Unsloth & LLMs (Llama 3, Gemma, etc.)
url: https://www.hackingdream.net/2025/06/xss-detection-fine-tune-your-own-ai-xss-hunter.html
source: Hacking Dream
date: 2025-06-05
fetch_date: 2025-10-06T22:53:05.395415
---

# Revolutionize XSS Detection: Fine-Tune Your Own AI XSS Hunter with Unsloth & LLMs (Llama 3, Gemma, etc.)

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Revolutionize XSS Detection: Fine-Tune Your Own AI XSS Hunter with Unsloth & LLMs (Llama 3, Gemma, etc.)

[June 05, 2025](https://www.hackingdream.net/2025/06/xss-detection-fine-tune-your-own-ai-xss-hunter.html "permanent link")

Cross-Site Scripting (XSS) remains a persistent and dangerous threat in web applications. Traditional detection methods have their limits, but what if you could train your own specialized AI to sniff out these vulnerabilities with greater nuance? Welcome to the world of fine-tuning Large Language Models (LLMs) for cybersecurity! In this comprehensive guide, we'll walk you through the process of supervised fine-tuning an LLM using the incredibly efficient [Unsloth](https://github.com/unslothai/unsloth) library to create a potent XSS detector. Whether you're a cybersecurity enthusiast, a developer, or an AI practitioner, get ready to level up your security toolkit.

[![XSS Detection Fine-Tune Your Own AI Hunter](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNNmh6zisQ4fKRSnlR_ZbLs_FlPO-yFENwDhSxPOl-kG2vbSXKsjgg2uivQ56wyzyfl5Fwg2iblddNPCZ7Z00ggEwqQj9N_XFDKCdIweWhyphenhyphenpOO9KwJ5BJNnbclvfvEyw12llZLt2PfkuckAi5SwocJHOvVJdJbVzKe2aWdE5uLCls5N-rV8fJE22Jr-vYD/w640-h426/XSS%20Detection%20Fine-Tune%20Your%20Own%20AI%20Hunter.jpg "XSS Detection Fine-Tune Your Own AI Hunter")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNNmh6zisQ4fKRSnlR_ZbLs_FlPO-yFENwDhSxPOl-kG2vbSXKsjgg2uivQ56wyzyfl5Fwg2iblddNPCZ7Z00ggEwqQj9N_XFDKCdIweWhyphenhyphenpOO9KwJ5BJNnbclvfvEyw12llZLt2PfkuckAi5SwocJHOvVJdJbVzKe2aWdE5uLCls5N-rV8fJE22Jr-vYD/s1024/XSS%20Detection%20Fine-Tune%20Your%20Own%20AI%20Hunter.jpg)

### Why Fine-Tune an LLM for XSS Detection?

Generic, pre-trained LLMs are powerful, but they might not possess the specialized knowledge to accurately identify complex XSS vulnerabilities within the context of specific HTTP request patterns or generate precise, actionable insights. Fine-tuning allows us to:

* **Specialize:** Teach the model the specific patterns and nuances of XSS vulnerabilities.
* **Improve Accuracy:** Achieve higher precision and recall for XSS detection compared to general models.
* **Custom Output:** Train the model to provide output in a structured format (like JSON) that includes not just a vulnerability flag, but also suggested payloads and reasoning.
* **Understand Your Data:** Tailor the model to the types of applications and codebases you typically encounter.

By using a custom "instruction-following" dataset, we can guide the LLM to become an expert XSS analyst.

### Meet Unsloth: Supercharging Your Fine-Tuning Journey

Unsloth is a game-changing open-source library that makes fine-tuning LLMs significantly faster (up to 2-5x) and more memory-efficient (reducing GPU RAM usage by up to 60%) without sacrificing performance. This makes sophisticated fine-tuning accessible even on platforms like Google Colab with free-tier GPUs.

### Prerequisites: What You'll Need

* **Google Colab Account:** We'll be using Colab for its free GPU access. Get one at [colab.research.google.com](https://colab.research.google.com/).
* **Hugging Face Account:** To download pre-trained models and (optionally) save your fine-tuned model. Sign up at [huggingface.co](https://huggingface.co/).
* **Hugging Face Token:** Create an API token with 'write' access from your Hugging Face account settings (under "Access Tokens"). This will be needed to save your model to the Hub.
* **Your Custom XSS Dataset:** This is crucial! You'll need a dataset in JSONL (JSON Lines) format. Each line should be a JSON object containing:
  + `instruction`: A clear task description for the LLM.
  + `input`: An object containing `http_request_details` (like method, path, headers, body, injection points) for an HTTP request.
  + `output`: The desired JSON response from the LLM, indicating if it's vulnerable, providing analysis, a payload, and reasoning.*(Note: Creating a high-quality dataset is a significant task itself, involving generating diverse vulnerable and non-vulnerable HTTP request examples and their corresponding analyses. we will not be covering the dataset creation part in this blogpost)*
* **Basic Python Knowledge:** Familiarity with Python will be helpful.

### Sample Custom XSS Data Set

This is just my sample dataset, you can get creative on developing a better dataset

```
{"id": "d4e9552f44d94826913fccbb28a92e49", "instruction": "Analyze the provided HTTP endpoint details where '%QUERY%' marks a user-controlled injection point. Determine if an XSS vulnerability exists. If so, identify the vulnerable parameter or location, suggest a representative payload that would confirm the vulnerability, and provide a justification for both the vulnerability and why the payload works. If not vulnerable, state so with a detailed reason.", "input": {"description": "Analysis of potential XSS vulnerability in POST request to path '/api/v2/users/batch_update'. Injection point marked by '%QUERY%' in location type: Unknown.", "http_request_details": {"raw_endpoint_info": "POST /api/v2/users/batch_update HTTP/1.1\\nContent-Type: application/json\\n\\n{\"updates\": [{\"userId\": \"user1\", \"new_status\": \"active\"}, {\"userId\": \"user2\", \"custom_field\": \"%QUERY%\"}]}", "method": "POST", "path": "/api/v2/users/batch_update", "headers": [], "query_parameters_template": [], "body_template": null, "injection_point_marker": "%QUERY%", "injection_location_type": "Unknown"}, "payload_applied_in_source_log": "![](\)"}, "output": {"is_vulnerable": true, "analysis": "The application fails to properly sanitize or encode user-controlled input in JSON fields, allowing injection of crafted HTML/JS that leads to XSS.", "vulnerable_parameter_suggestion": "custom_field", "recommended_payload_for_confirmation": "![](\)", "reasoning_for_payload": "Payload uses a tab-encoded \"javascript:\" URI to bypass naive filters and trigger an XSS alert in browsers parsing injected HTML."}}

{"id": "e242243ef1434f7da43d778b42825dc4", "instruction": "Analyze the provided HTTP endpoint details where '%QUERY%' marks a user-controlled injection point. Determine if an XSS vulnerability exists. If so, identify the vulnerable parameter or location, suggest a representative payload that would confirm the vulnerability, and provide a justification for both the vulnerability and why the payload works. If not vulnerable, state so with a detailed re...