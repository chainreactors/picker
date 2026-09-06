---
title: changedetection.io v0.60.3
url: https://kitploit.com/en/posts/github-dgtlmoon-changedetectionio-0603
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:24.567148
---

# changedetection.io v0.60.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/43320/8dc68615b084e4e3a2abaefa5fc1c4744c84ed82fa5d627cb8893959190d825f.png)

New releaseSep 5, 2026

# changedetection.io v0.60.3

Best and simplest tool for website change detection, web page monitoring, and website change alerts. Perfect for tracking content changes, price drops, restock alerts, and website defacement monitoring—all for free or enjoy our SaaS plan!

Share

# Detect Website Changes Automatically — Monitor Web Page Changes in Real Time

Monitor websites for updates — get notified via Discord, Email, Slack, Telegram, Webhook and many more.

**Detect web page content changes and get instant alerts.**

Ideal for monitoring price changes, content edits, conditional changes and more.

[![Web site page change monitoring](https://assets.kitploit.com/production/public/readmes/43320/d5c169758f07364766d5f3966244ba0de3c1d25105865c98e91b0c8f8002a19e.png "Web site page change monitoring")](https://changedetection.io?src=github)

[![Release Version](https://assets.kitploit.com/production/public/readmes/placeholders/f0fc86cfe65f76d40e15aaec61704ec8220a56dc89d4be03c46f67cb31b9fa8c.svg)](https://github.com/dgtlmoon/changedetection.io/releases) [![Docker Pulls](https://img.shields.io/docker/pulls/dgtlmoon/changedetection.io?style=for-the-badge)](https://hub.docker.com/r/dgtlmoon/changedetection.io) [![License](https://img.shields.io/github/license/dgtlmoon/changedetection.io.svg?style=for-the-badge)](LICENSE.md)

![changedetection.io](https://github.com/dgtlmoon/changedetection.io/actions/workflows/test-only.yml/badge.svg?branch=master)

[**Get started with website page change monitoring straight away. Don't have time? Try our $8.99/month subscription, use our proxies and support!**](https://changedetection.io) , *half the price of other website change monitoring services!*

* Chrome browser included.
* Nothing to install, access via browser login after signup.
* Super fast, no registration needed setup.
* Get started watching and receiving website change notifications straight away.
* See our [tutorials and how-to page for more inspiration](https://changedetection.io/tutorials)

## AI-powered website change detection — smart alerts and plain-language summaries

Stop drowning in noise. Connect any LLM (OpenAI, Gemini, Anthropic, Ollama and more) and go from *"something changed"* to *"only the thing you care about changed"*.

**AI change detection rules** — write a plain-English intent once: *"notify me only when the price drops below $50"*, *"alert me when the item comes back in stock"*, *"ignore navigation and footer changes"*. The AI evaluates every detected diff against your intent and silently suppresses everything irrelevant. Fewer false positives, zero noise.

**AI change summaries** — instead of staring at a raw diff, your notification reads *"Price dropped from $89.99 to $67.00"* or *"3 new products added to the listing"*. Works globally or per-watch, with full control over the prompt.

Works with any model you already pay for — GPT-4o-mini and Gemini Flash handle this well at fractions of a cent per check. Or run it entirely locally with **Ollama**, **vLLM**, **LM Studio**, or any **OpenAI-compatible self-hosted endpoint** — pick the *OpenAI-compatible (vLLM, LM Studio, llama.cpp)* option in the provider dropdown and point it at your server's `/v1` URL. Powered by [LiteLLM](https://github.com/BerriAI/litellm), giving you seamless access to [100+ supported providers and models](https://docs.litellm.ai/docs/providers).

[![AI-powered website change detection — plain language change summaries and smart alert rules](https://assets.kitploit.com/production/public/readmes/43320/589bf75fc5ef6f71db67cdbab9ae6b06d6b1589ee07e4c90192ba0227a6df98c.jpg "AI website change detection with LLM change summaries and intelligent alert filtering")](https://changedetection.io?src=github)

*Note: Available in our subscription/hosted service from June 2026*

### Target specific parts of the webpage using the Visual Selector tool.

Available when connected to a [playwright content fetcher](https://github.com/dgtlmoon/changedetection.io/wiki/Playwright-content-fetcher) (included as part of our subscription service)

[![Select parts and elements of a web page to monitor for changes](https://assets.kitploit.com/production/public/readmes/43320/4fef30ed77d4e782c0e29985213751710e869230524b1accb49408f4bd9caaa0.gif "Select parts and elements of a web page to monitor for changes")](https://changedetection.io?src=github)

### Easily see what changed, examine by word, line, or individual character.

[![Self-hosted web page change monitoring context difference ](https://assets.kitploit.com/production/public/readmes/43320/0a3dac1c0a40541cbb64040c24a85165c397770de901a9d7f9b90815df6842f8.png "Self-hosted web page change monitoring context difference ")](https://changedetection.io?src=github)

### Perform interactive browser steps

Fill in text boxes, click buttons and more, setup your changedetection scenario.

Using the **Browser Steps** configuration, add basic steps before performing change detection, such as logging into websites, adding a product to a cart, accept cookie logins, entering dates and refining searches.

[![Website change detection with interactive browser steps, detect changes behind login and password, search queries and more](https://assets.kitploit.com/production/public/readmes/43320/a27674b491b27facbc558d572cbb4d9f0ce734bcb9e3ded7272d4f4265a72bc0.gif "Website change detection with interactive browser steps, detect changes behind login and password, search queries and more")](https://changedetection.io?src=github)

After **Browser Steps** have been run, then visit the **Visual Selector** tab to refine the content you're interested in.
Requires Playwright to be enabled.

### Awesome restock and price change notifications

Enable the *"Re-stock & Price detection for single product pages"* option to activate the best way to monitor product pricing, this will extract any meta-data in the HTML page and give you many options to follow the pricing of the product.

Easily organise and monitor prices for products from the dashboard, get alerts and notifications when the price of a product changes or comes back in stock again!

[![Easily keep an eye on product price changes directly from the UI](https://assets.kitploit.com/production/public/readmes/43320/10745bf4b727597112a6d47da95d44e7e1e52d214a675045aeae560201155e9a.png "Easily keep an eye on product price changes directly from the UI")](https://changedetection.io?src=github)

Set price change notification parameters, upper and lower price, price change percentage and more.
Always know when a product for sale drops in price.

[![Set upper lower and percentage price change notification values](https://assets.kitploit.com/production/public/readmes/43320/ca9e40b5dd7dbc8d7dd0510d8d0ce46ccad3fc576136c2f6430a66a759441b75.png "Set upper lower and percentage price change notification values")](https://changedetection.io?src=github)

### Example use cases

* Products and services have a change in pricing
* *Out of stock notification* and *Back In stock notification*
* Monitor and track PDF file changes, know when a PDF file has text changes.
* Governmental department updates (changes are often only on their websites)
* New software releases, security advisories when you're not on their mailing list.
* Festivals with changes
* Discogs restock alerts and monitoring
* Realestate listing changes
* Know when your favourite whiskey is on sale, or other special deals are announced before anyone else
* COVID related news from government we...