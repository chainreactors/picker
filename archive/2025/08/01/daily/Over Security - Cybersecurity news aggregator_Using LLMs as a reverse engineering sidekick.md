---
title: Using LLMs as a reverse engineering sidekick
url: https://blog.talosintelligence.com/using-llm-as-a-reverse-engineering-sidekick/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-01
fetch_date: 2025-10-07T00:49:18.317398
---

# Using LLMs as a reverse engineering sidekick

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Using LLMs as a reverse engineering sidekick

By
[Guilherme Venere](https://blog.talosintelligence.com/author/guilherme/)

Thursday, July 31, 2025 06:00

[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)

* This research explores how large language models (LLMs) can complement, rather than replace, the efforts of malware analysts in the complex field of reverse engineering.
* LLMs may serve as powerful assistants to streamline workflows, enhance efficiency, and provide actionable insights during malware analysis.
* We will showcase practical applications of LLMs in conjunction with essential tools like Model Context Protocol (MCP) frameworks and industry-standard disassemblers and decompilers, such as IDA Pro and Ghidra.
* Readers will gain insights into which models and tools are best suited for common challenges in malware analysis and how these tools can accelerate the identification and understanding of unknown malicious files.
* We also show how some common hurdles faced when using LLMs may influence the results, like cost increases due to tool usage and limitations of input context size in local models.

---

## Talos' suggested approach

As the adoption of LLMs accelerates across industries, concerns about their potential to replace human expertise have become widespread. However, rather than viewing it as a threat to human expertise, we can consider LLMs as powerful tools to help malware researchers in our work.

We seek to show with this research that even by using low-cost tools and hardware, a malware researcher can take advantage of this technology to improve their work.

This blog covers the different choices of client applications available to interact with LLMs and disassemblers, the features to consider when choosing the best language model and the available plugins to integrate these applications into a solid framework to help during a malware analysis session.

For our tests, we decided to use a setup composed of a MCP server which implements integration with IDA-PRO and a MCP client based on VSCode. With this stack, we show how MCP servers can be used to help the language model execute tasks based on user input or in reaction to information found in the malicious code.

This blog also provides a step-by-step guide on how to set up your environment to achieve a basic setup to use an LLM with a local model running on your GPU.

## Introduction to MCP

The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is an open protocol that standardizes how applications provide context to LLM clients and models. Tools and data sources made available by MCP servers provide the context, and the LLM model can choose which tool or data source to access based on user request or autonomously select it during runtime.

MCP servers implement tools using code and a description instructing the LLM on how to use each tool. The code can implement any kind of task, be it accessing API integration, file or network access, or any other automation necessary.

![](https://blog.talosintelligence.com/content/images/2025/07/llm-flow.jpg)

Figure 1. Diagram showing how an MCP server connects to other components in a typical setup.

These components can all be installed on the same or separate machines as needed. For example, the local LLM model may run on a separate server with better GPUs while IDA Pro and MCP server may be on a different machine with more restricted access, due to it being used to handle malware.

## Choosing the right tools for the trade

A user interacts with an MCP server through an MCP client, which serves as the main interface to query the LLM model, exchange data with MCP servers and display this data back to the user. These clients can be any application which supports the MCP protocol, such as the [Claude.AI Desktop](https://claude.ai/download) or [Visual Studio Code](https://code.visualstudio.com/) (VSCode), using any of the MCP client extensions available in their marketplace.

For this blog, we use VSCode with the Cline MCP client extensions, but any of the many extensions currently available can be used. The most popular ones are:

* Cline: <https://cline.bot/>
* Roo Code: <https://roocode.com/>
* Copilot MCP: <https://marketplace.visualstudio.com/items?itemName=AutomataLabs.copilot-mcp>

For local implementations, the inference engine imposes another choice to make. There are several open-source engines with different levels of performance and usage complexity. Some of them are Python frameworks like [vLLM,](https://docs.vllm.ai/en/v0.7.3/index.html) others are C++ with Python-bindings and can be deployed on full servers that can be contacted via a REST API like [LLama.CPP](https://github.com/ggml-org/llama.cpp?tab=readme-ov-file) or Ollama. They all have advantages and disadvantages and an analysis between them is beyond the scope of this article. For our experiments we decided to use Ollama, mainly for its simplicity of use.

### Model selection criteria

The next component needed is an LLM. These can be either a cloud-based model or a locally running model. Most of the MCP clients support a wide range of cloud-based services and have pre-configured settings for them. For locally running models, using the [Ollama](https://ollama.com/) inference engine with one of their supported models is one of the most compatible solutions.

When choosing which model to use with MCP servers, some features need to be taken into consideration. This is due to the way MCP client interacts with the model and the MCP servers.

First, the model must support prompts with structured instructions. This is how the client will inform the model about what MCP tools are available, what they are used for and the template syntax on how to use them.

The model must also support large input [contex...