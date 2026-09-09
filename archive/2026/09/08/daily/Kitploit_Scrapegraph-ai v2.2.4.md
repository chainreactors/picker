---
title: Scrapegraph-ai v2.2.4
url: https://kitploit.com/en/posts/github-scrapegraphai-scrapegraph-ai-v224
source: Kitploit
date: 2026-09-08
fetch_date: 2026-09-09T06:55:03.909313
---

# Scrapegraph-ai v2.2.4

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/41478/e11a555115b80e07241afdb0aec04ee9fae66f983d969d27fbd8a64a21f090de.png)

New releaseSep 8, 2026

# Scrapegraph-ai v2.2.4

AI-powered web scraping library using LLMs to extract structured data from websites and documents with minimal configuration.

Share

## 🚀 **Looking for an even faster and simpler way to scrape at scale (only 5 lines of code)?** Check out our enhanced version at [**ScrapeGraphAI.com**](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=oss_cta&ut#m_content=top_banner)! 🚀

---

# 🕷️ ScrapeGraphAI: You Only Scrape Once

[![ScrapeGraphAI](https://assets.kitploit.com/production/public/readmes/41478/e11a555115b80e07241afdb0aec04ee9fae66f983d969d27fbd8a64a21f090de.png)](https://scrapegraphai.com)

[English](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/README.md) | [中文](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/chinese.md) | [日本語](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/japanese.md)
| [한국어](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/korean.md)
| [Русский](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/russian.md) | [Türkçe](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/turkish.md)
| [Deutsch](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/german.md)
| [Español](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/spanish.md)
| [français](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/french.md)
| [Português](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/portuguese.md)
| [Italiano](https://github.com/scrapegraphai/scrapegraph-ai/blob/main/docs/italian.md)

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/scrapegraphai?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/scrapegraphai)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[![ScrapeGraphAI%2FScrapegraph-ai | Trendshift](https://trendshift.io/api/badge/repositories/15078)](https://trendshift.io/repositories/15078)

[ScrapeGraphAI](https://scrapegraphai.com) is a *web scraping* python library that uses LLM and direct graph logic to create scraping pipelines for websites and local documents (XML, HTML, JSON, Markdown, etc.).

Just say which information you want to extract and the library will do it for you!

## 🚀 Integrations

ScrapeGraphAI offers seamless integration with popular frameworks and tools to enhance your scraping capabilities. Whether you're building with Python or Node.js, using LLM frameworks, or working with no-code platforms, we've got you covered with our comprehensive integration options..

[![Web data extraction at scale? Try ScrapeGraphAI cloud](https://assets.kitploit.com/production/public/readmes/41478/0e788431fde2dc01cf2aa4b53d87b9befe3c728b719a5a45dec11ffb4d7c77a5.png)](https://scrapegraphai.com)

You can find more informations at the following [link](https://scrapegraphai.com)

**Integrations**:

* **API**: [Documentation](https://docs.scrapegraphai.com/introduction)
* **SDKs**: [Python](https://docs.scrapegraphai.com/sdks/python), [Node](https://docs.scrapegraphai.com/sdks/javascript)
* **LLM Frameworks**: [Langchain](https://docs.scrapegraphai.com/integrations/langchain), [Llama Index](https://docs.scrapegraphai.com/integrations/llamaindex), [Crew.ai](https://docs.scrapegraphai.com/integrations/crewai), [Agno](https://docs.scrapegraphai.com/integrations/agno), [CamelAI](https://github.com/camel-ai/camel)
* **Low-code Frameworks**: [Pipedream](https://pipedream.com/apps/scrapegraphai), [Bubble](https://bubble.io/plugin/scrapegraphai-1745408893195x213542371433906180), [Zapier](https://zapier.com/apps/scrapegraphai/integrations), [n8n](http://localhost:5001/dashboard), [Dify](https://dify.ai), [Toolhouse](https://app.toolhouse.ai/mcp-servers/scrapegraph_smartscraper)
* **MCP server**: [Link](https://smithery.ai/server/%40ScrapeGraphAI/scrapegraph-mcp)

## 🚀 Quick install

The reference page for Scrapegraph-ai is available on the official page of PyPI: [pypi](https://pypi.org/project/scrapegraphai/).

root@kitploit:~

```
pip install scrapegraphai

# IMPORTANT (for fetching websites content)
playwright install
```

**Note**: it is recommended to install the library in a virtual environment to avoid conflicts with other libraries 🐱

## 💻 Usage

There are multiple standard scraping pipelines that can be used to extract information from a website (or local file).

The most common one is the `SmartScraperGraph`, which extracts information from a single page given a user prompt and a source URL.

root@kitploit:~

```
from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract useful information from the webpage, including a description of what the company does, founders and social media links",
    source="https://scrapegraphai.com/",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> For OpenAI and other models you just need to change the llm config!
>
> root@kitploit:~
>
> ```
> graph_config = {
>    "llm": {
>        "api_key": "YOUR_OPENAI_API_KEY",
>        "model": "openai/gpt-4o-mini",
>    },
>    "verbose": True,
>    "headless": False,
> }
> ```

The output will be a dictionary like the following:

root@kitploit:~

```
{
    "description": "ScrapeGraphAI transforms websites into clean, organized data for AI agents and data analytics. It offers an AI-powered API for effortless and cost-effective data extraction.",
    "founders": [
        {
            "name": "",
            "role": "Founder & Technical Lead",
            "linkedin": "https://www.linkedin.com/in/perinim/"
        },
        {
            "name": "Marco Vinciguerra",
            "role": "Founder & Software Engineer",
            "linkedin": "https://www.linkedin.com/in/marco-vinciguerra-7ba365242/"
        },
        {
            "name": "Lorenzo Padoan",
            "role": "Founder & Product Engineer",
            "linkedin": "https://www.linkedin.com/in/lorenzo-padoan-4521a2154/"
        }
    ],
    "social_media_links": {
        "linkedin": "https://www.linkedin.com/company/101881123",
        "twitter": "https://x.com/scrapegraphai",
        "github": "https://github.com/ScrapeGraphAI/Scrapegraph-ai"
    }
}
```

There are other pipelines that can be used to extract information from multiple pages, generate Python scripts, or even generate audio files.

| Pipeline Name | Description |
| --- | --- |
| SmartScraperGraph | Single-page scraper that only needs a user prompt and an input source. |
| SearchGraph | Multi-page scraper that extracts information from the top n search results of a search engine. |
| SpeechGraph | Single-page scraper that extracts information from a website and generates an audio file. |
| ScriptCreatorGraph | Single-page scraper that extracts information from a website and generates a Python script. |
| SmartScraperMultiGraph | Multi-page scraper that extracts information from multiple pages given a single prompt and a list of sources. |
| ScriptCreatorMultiGraph | Multi-page scraper that gener...