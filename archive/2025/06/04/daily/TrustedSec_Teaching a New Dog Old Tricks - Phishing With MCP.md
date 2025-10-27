---
title: Teaching a New Dog Old Tricks - Phishing With MCP
url: https://trustedsec.com/blog/teaching-a-new-dog-old-tricks-phishing-with-mcp
source: TrustedSec
date: 2025-06-04
fetch_date: 2025-10-06T22:53:38.551790
---

# Teaching a New Dog Old Tricks - Phishing With MCP

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Teaching a New Dog Old Tricks - Phishing With MCP](https://trustedsec.com/blog/teaching-a-new-dog-old-tricks-phishing-with-mcp)

June 03, 2025

# Teaching a New Dog Old Tricks - Phishing With MCP

Written by
James Williams

Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/TeachingNewDogOldTricks_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1748452657&s=2ed46f30279ed6f9049e0b259986be00)

Table of contents

* [1.1 Building Our MCP Server](#MCPserver)
* [1.2 Going Phishing](#Phishing)
* [1.3 Conclusion](#Conclusions)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#8bb4f8fee9e1eee8ffb6c8e3eee8e0aeb9bbe4feffaeb9bbffe3e2f8aeb9bbeaf9ffe2e8e7eeaeb9bbedf9e4e6aeb9bbdff9fef8ffeeefd8eee8aeb9baadeae6fbb0e9e4eff2b6dfeeeae8e3e2e5ecaeb9bbeaaeb9bbc5eefcaeb9bbcfe4ecaeb9bbc4e7efaeb9bbdff9e2e8e0f8aeb9bba6aeb9bbdbe3e2f8e3e2e5ecaeb9bbdce2ffe3aeb9bbc6c8dbaeb8caaeb9bbe3fffffbf8aeb8caaeb9cdaeb9cdfff9fef8ffeeeff8eee8a5e8e4e6aeb9cde9e7e4ecaeb9cdffeeeae8e3e2e5eca6eaa6e5eefca6efe4eca6e4e7efa6fff9e2e8e0f8a6fbe3e2f8e3e2e5eca6fce2ffe3a6e6e8fb "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fteaching-a-new-dog-old-tricks-phishing-with-mcp "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Teaching%20a%20New%20Dog%20Old%20Tricks%20-%20Phishing%20With%20MCP%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fteaching-a-new-dog-old-tricks-phishing-with-mcp "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fteaching-a-new-dog-old-tricks-phishing-with-mcp&mini=true "Share on LinkedIn")

Recently, there has been a lot of focus on enhancing AI with MCP. This has included giving AI access to [reverse engineering tools](https://github.com/LaurieWired/GhidraMCP), using it to [identify network resources](https://trustedsec.com/blog/mcp-an-introduction-to-agentic-op-support), and allowing it to [control an implant](https://x.com/_xpn_/status/1902848551463399504), mimicking the actions of a known threat actor. I wanted to see if we could use AI to build some convincing phishing pretexts and how much work would be needed to make it happen.

## 1.1 Building Our MCP Server

We’re going to use Claude for this experiment, as its desktop app will integrate easily with our MCP servers. We want to be able to give it a company name or URL and let it do most of the heavy lifting for us. There’s just one problem—Claude doesn’t have access to the Internet.

The [modelcontextprotocol](https://github.com/modelcontextprotocol/servers/blob/main/src/brave-search/README.md) project on GitHub has a Brave Search MCP Server, which integrates the Brave Search API. A free tier of this is available, which is limited to 2,000 requests. However, this API doesn’t allow direct website access—only access to search results. We’re going to add this to Claude anyway, but we’re also going to need to build something to let Claude access sites directly. While we’re at it, we will also add the ability to read and write files so we don’t need to manually save Claude work.

[Modelcontextprotocol.io](http://Modelcontextprotocol.io) has a good “[getting started](https://modelcontextprotocol.io/quickstart/server#claude-for-desktop-integration-issues)” guide, which we’re going to adapt to our needs. Using uv, a Python package manager [written in Rust](https://github.com/astral-sh/uv), we create a new project with a venv, install our dependencies, and generate our FS.py file. To actually create our MCP, we’re going to use cursor ([cursor.com](http://cursor.com)) to edit the code. After adding our imports (utilizing the ‘getting started guide’ as a reference), we can start adding our @server.tool declarations. Using the power of AI, we can essentially tab complete the entire file in a few minutes. We are then left with the following code:

```
from mcp.server.fastmcp import FastMCP
import os
import requests

server = FastMCP("FS Interaction")
@server.prompt()
def setup_prompt() -> str:
    return """
You are a file system interaction agent.
You can use the following tools to interact with the file system:
    - ls(directory: str) -> list[str]: List the contents of a directory
    - cat(file: str) -> str: Read the contents of a file
    - write(file: str, content: str) -> str: Write to a file
When asked to read a file, you should carefully consider the users request, analyze the file and respond to
question after reviewing the file contents.
    If you cannot answer the question based on the file contents, s...