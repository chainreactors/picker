---
title: Sidekick in Action: Finding Vulnerabilities in dnsmasq
url: https://binary.ninja/2025/02/26/sidekick-in-action-finding-vulnerabilities-in-dnsmasq.html
source: Binary Ninja
date: 2025-02-27
fetch_date: 2025-10-06T20:35:38.141486
---

# Sidekick in Action: Finding Vulnerabilities in dnsmasq

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Sidekick in Action: Finding Vulnerabilities in dnsmasq

* [Brian Knudson](https://github.com/kristopax)
* 2025-02-26
* [sidekick](/tag/sidekick)

Hello, and welcome to another exciting episode of âSidekick in Actionâ! Today, we will be applying Sidekick to a variety of common vulnerability discovery tasks while looking at the popular network utility `dnsmasq`.

## The Challenge

We have selected `dnsmasq` version 2.80 (stripped) as our target to analyze using Sidekick for several reasons:

* **Historical Vulnerabilities**: `dnsmasq` 2.80 has known CVEs, providing a clear, documented set of vulnerabilities for analysis.
* **Realistic Deployment Scenario**: The stripped binary, devoid of function symbols, mirrors real-world deployed software. The absence of symbols forces analysts to rely on code patterns, heuristics, and context, which illustrates how Sidekick can accelerate vulnerability discovery even in less-than-ideal conditions.
* **Compact yet Complex Codebase**: Despite its relatively small size, `dnsmasq` integrates diverse functionalities (DNS, DHCP, TFTP), presenting a rich collection of code paths and program logic.
* **Open Source**: Source code is available to enhance analysis if needed and to verify results.

Reverse engineering and vulnerability research involve non-trivial tasks like function identification, decompilation, pattern recognition, and vulnerability identification that all require considerable time, effort, and expertise. Sidekick can help with these by automatically reasoning about code and detecting well-known patterns and structures to identify behaviors, generate names, and recognize complex properties of software such as security.

## Stage 1: What is this thing?

When looking at a binary for the first time, it helps to begin with an understanding of what youâre dealing with at a high level in order to ground the context of further investigations. Sometimes you may already have prior knowledge about the binary, and other times not. As mentioned above, we are starting with a version of `dnsmasq` that has been stripped of function symbol names and also given a generic file name to prevent Sidekick from placing too much attention on metadata instead of the code itself.

Using the Analysis Console interface, letâs start with something simple and ask the Analysis Assistant what the binary is.

![Analysis Console](/blog/images/sidekick-in-action-dnsmasq/analysis-console.what-binary-is-this-v2.png)

After Sidekick completes, youâll notice a few things:

* The Analysis Assistant issued several queries for information in the binary in the form of âSearch binaryâ tool requests based on its determination of the information it needed to complete your request.
* The âSearch binaryâ tool requests use the Binary Ninja Query Language (BNQL) to retrieve objects from the binary. The Analysis Assistant automatically generated the appropriate query using the correct syntax.
* After analyzing the results of its search, Sidekick provides an answer to our request along with a summary of its supporting findings.

The output from each tool request can be viewed by expanding the message using the chevron button that appears when you hover over the message. This allows us to see the information the Analysis Assistant uses as context to complete our request.

![Analysis Console](/blog/images/sidekick-in-action-dnsmasq/analysis-console.tool-output-expanded.png)

Before moving on to the next step, itâs important to keep in mind that the Analysis Console is powered by large language models that inherently perform with some amount of indeterminism. This means that for a given request, you may not always get the same answer. Since the Analysis Assistant makes potentially multiple decisions on the overall strategy and specific steps taken to complete your task, there will be variation in its results. Knowing this, we have provided a mechanism for you to easily request the Analysis Assistant to retry any request by simply hovering over its message and clicking the âRetryâ button that appears.

![Analysis Console](/blog/images/sidekick-in-action-dnsmasq/analysis-console.retry.png)

Letâs see how that works in practice.

![Analysis Console](/blog/images/sidekick-in-action-dnsmasq/analysis-console.what-binary-is-this-v2.png)

After Sidekick completes this time, youâll notice a few things:

* The Analysis Assistant used a different approach and employed different steps to complete our request. This time it used just the strings used in the main function to determine what the binary is.
* The Analysis Assistant came to the same conclusion.

With that said, letâs continue on our `dnsmasq` bug hunt. Now that we âofficiallyâ know what binary weâre looking at, letâs see if we can determine the specific version since that information will determine what (if any) known vulnerabilities exist.

Since the Analysis Assistant was so helpful with our first request, letâs try it out on this task.

![Analysis Console](/blog/images/sidekick-in-action-dnsmasq/analysis-console.what-version-is-this.png)

Before continuing on to find the version number, letâs first take note of the highlighted link to address `0x4fc56`. Yes, the Analysis Console supports highlighted links to functions, symbols, addresses, and even Analysis Indexes. Simply click on the link, and the main view will navigate the cursor to that location for a nice quality of life improvement.

Now back to the version number. Well, it appears that Sidekick found a string containing a version number. Letâs confirm that the string is actually used in the code and, if so, look at the code to potentially verify its use as a version number of the program. While we could pull up Binary Ninjaâs Cross-References sidebar for the string to see where itâs used in the binary, letâs see what Sidekick can do with this task.

![Analysis Console](/blog/images/sidekick-in-action-dnsmasq/analysis-console.confirm-version-string.png)

In this case, Sidekick used a BNQL query to find the one function that uses the version string and captured that functionâs code (`sub_1cfa0` passes the version string as an argument to the function `sub_14d30`). Sidekick also captured the code of another instance of the version number being used as additional context to aid in its analysis before coming to the final determination that the version string is in fact used as a version number during DNS bindings on initialization.

Now that we know what our binary is and its specific version, letâs see if we can find any known vulnerabilities.

## Stage 2: Are there any known vulnerabilities?

Sidekick leverages the vast knowledge of large language models (LLMs) to help answer your questions about the binary, so for this step, we are going to see what vulnerabilities it knows of that are associated with this version of `dnsmasq`.

![Analysis Console](/blog/images/sidekick-in-action-dnsmasq/analysis-console.known-vulnerabilities.png)

The first thing you will notice is that Sidekick immediately tried to search the binary for evidence of vulnerabilities despite our request for information from its existing knowl...