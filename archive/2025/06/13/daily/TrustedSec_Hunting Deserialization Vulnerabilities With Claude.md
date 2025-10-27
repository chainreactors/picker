---
title: Hunting Deserialization Vulnerabilities With Claude
url: https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude
source: TrustedSec
date: 2025-06-13
fetch_date: 2025-10-06T22:54:21.149251
---

# Hunting Deserialization Vulnerabilities With Claude

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
* [Hunting Deserialization Vulnerabilities With Claude](https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude)

June 12, 2025

# Hunting Deserialization Vulnerabilities With Claude

Written by
James Williams

Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/HuntingDeserializationVulnsClaude_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1749496812&s=3a91953a1f0c944dd6788fe2226c512b)

Table of contents

* [Setup](#Setup)
* [Finding Existing Vulnerabilities](#vulnerabilities)
* [Finding New Vulnerabilities](#newvulnerabilities)
* [Final Thoughts](#Final)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#1f206c6a7d757a7c6b225c777a7c743a2d2f706a6b3a2d2f6b77766c3a2d2f7e6d6b767c737a3a2d2f796d70723a2d2f4b6d6a6c6b7a7b4c7a7c3a2d2e397e726f247d707b6622576a716b7671783a2d2f5b7a6c7a6d767e7376657e6b7670713a2d2f496a73717a6d7e7d7673766b767a6c3a2d2f48766b773a2d2f5c737e6a7b7a3a2c5e3a2d2f776b6b6f6c3a2c5e3a2d593a2d596b6d6a6c6b7a7b6c7a7c317c70723a2d597d7370783a2d59776a716b767178327b7a6c7a6d767e7376657e6b76707132696a73717a6d7e7d7673766b767a6c3268766b77327c737e6a7b7a "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhunting-deserialization-vulnerabilities-with-claude "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Hunting%20Deserialization%20Vulnerabilities%20With%20Claude%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhunting-deserialization-vulnerabilities-with-claude "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhunting-deserialization-vulnerabilities-with-claude&mini=true "Share on LinkedIn")

In this post, we are going to look at how we can find zero-days in .NET assemblies using Model Context Protocol (MCP).

## Setup

Before we can start vibe hacking, we need an MCP that will allow Claude to disassemble .NET assemblies. Reversing a .NET binary is normally something I would do with [**dotPEAK**](https://www.jetbrains.com/decompiler/); however, this is a Windows-only tool. Luckily for us, [ilspycmd](https://github.com/icsharpcode/ILSpy) exists and can be run on Mac/Linux. The [ilspycmd-docker](https://github.com/berdav/ilspycmd-docker/tree/main) repository provides a Dockerfile for ilspycmd, but the current version on GitHub is a few years out of date and won’t build.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig01_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527487&s=8ab9469644ed9fa0573c6767f6c004f1)

Figure 1 - Build Error for ilspycmd-docker

Luckily, the error message is quite explicit about the problem, and a small change to the Dockerfile will fix the problem.

```
FROM mcr.microsoft.com/dotnet/sdk:8.0

RUN useradd -m -s /bin/bash ilspy
USER ilspy

WORKDIR /home/ilspy

RUN dotnet tool install -g ilspycmd

RUN echo 'export PATH="$PATH:/home/ilspy/.dotnet/tools/"' >> /home/ilspy/.bashrc

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
```

We can build this new image with the following command:

```
docker build -t ilspycmd .
```

With our Dockerfile updated and our container built, we can build a simple MCP server using Python. We’ll use the same framework as shown in our [previous blog that discusses building an MCP server](https://trustedsec.com/blog/teaching-a-new-dog-old-tricks-phishing-with-mcp).

```
from mcp.server.fastmcp import FastMCP
import subprocess
import os

server = FastMCP("ilspy docker")

@server.prompt()
def setup_prompt() -> str:
    return """
    You can use the following commands to decompile .NET assemblies, using ilspy:
    - decompile(file: str, output_folder: str) -> int: Decompile the file at the provided path.
    The returned value is the success code, with 0 indicating a successful run
    """

@server.tool()
def run_ilspycmd_docker(exe_path, output_folder) -> int:
    """
    Run ilspycmd in a Docker container to decompile a DLL

    Args:
        dll_path (str): Path to the DLL file to decompile
        output_folder (str): Folder where decompiled code will be placed

    Returns:
        tuple: (return_code, stdout, stderr)
    """
    # Get absolute paths
    input_dir = os.path.abspath(os.path.dirname(exe_path))
    output_dir = os.path.abspath(output_folder)
    exe_filename = os.path.basename(exe_path)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create input directory inside container
    container_input_dir = "/decompile_in"
    container...