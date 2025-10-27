---
title: Sidekick 3.0
url: https://binary.ninja/2025/02/26/sidekick-3.0.html
source: Binary Ninja
date: 2025-02-27
fetch_date: 2025-10-06T20:35:36.062107
---

# Sidekick 3.0

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

## Sidekick 3.0

* [Brian Knudson](https://github.com/kristopax)
* [Tim Bryant](https://github.com/iamausertoo)
* 2025-02-26
* [sidekick](/tag/sidekick)

Today, we are excited to announce Sidekick 3.0! In addition to a number of bug fixes, UX improvements, and updated models, this release extends Sidekickâs analysis capabilities and with tighter Binary Ninja integration. In particular, our new query language, expanded editing capabilities, custom tool system, and the re-designed Assistant (now called the Analysis Console) stand out. These features and more continue to make Sidekick the best AI-powered tool for binary analysis on the market.

## Exploring Relationships, Finding Answers

As a reverse engineer, building relationships between code and data is foundational for understanding a binary. An AI assistant also needs to be able to navigate those same relationships and gather relevant information before it can properly analyze and understand whatâs going on.

With Sidekick 3.0, we are introducing a new query language called the [Binary Ninja Query Language (BNQL)](https://docs.sidekick.binary.ninja/latest/guide/analysis/bnql/), which has been designed specifically for use by AI models to navigate code and data relationships with ease. As an example, this means that Sidekick will now search with cross-references to find and substantiate answers to your questions.

![Analysis Console](/blog/images/sidekick-3.0/analysis-console-multi-step.png)
*Figure 1: Sidekickâs Analysis Console uses BNQL to collect more information from the binary for deeper analysis.*

## Editing Binaries Like a Ninja

As reverse engineers, we donât just stare at a bunch of bytes and magically come up with the answer to a specific question. To reach our goals, we shape an analysis database to reflect our findings along the way: naming functions, defining and applying types, adding comments and tags, and building custom views for the things we care about most. We wanted Sidekick 3.0 to have the same power.

To that end, weâve designed an AI-friendly format for editing binaries, letting Sidekick manipulate the database with ninja-like precision. It can add, remove, or tweak *anything*: functions, data variables, symbols, sections, and even raw bytes! This mirrors the full control over analysis that youâd expect from a seasoned pro.

![Analysis Console](/blog/images/sidekick-3.0/analysis-console-decompilation-cleanup.png)
*Figure 2: Sidekickâs Analysis Console directly applies edits to the binary to create structure definitions, rename functions, and rename variables.*

But, it doesnât stop there! Sidekick can also create and curate custom analysis indexes using BNQL queries, quickly gathering points of interest so you can focus on what matters most to you.

![Analysis Console](/blog/images/sidekick-3.0/analysis-console-create-index.png)
*Figure 3: Sidekickâs Analysis Console creates Analysis Indexes and adds entries using BNQL.*

## Extending Deep Analysis with a Custom Toolkit

Reverse engineering relies on tools that search binaries, compute precise results, or automate repetitive tasks. When these tools are reusable and tailored to specific needs, they improve efficiency across projects. Sidekick 3.0 extends its deep analysis capabilities by creating a growing set of custom tools designed for reuse.

![Analysis Console](/blog/images/sidekick-3.0/analysis-console-register-tool.png)
*Figure 4: Sidekickâs Analysis Console manages and uses set of active tools that can be extended to add new or existing tools to accomplish a given task.*

In this release, Sidekick thoughtfully generates parameterized scripts, drawing on Binary Ninjaâs API and our AI-driven program analysis (`LLMOperator`) from the prior release. These scripts form a toolkit that can be applied to recurring tasksâlike finding specific function patterns or tagging cross-referencesâwithout needing constant rework. As the toolkit expands with each project, both you and Sidekick become more efficient, leveraging past analysis to streamline future efforts.

![Automation Workbench](/blog/images/sidekick-3.0/automation-workbench-script-parameters-dialog.png)
*Figure 5: Scripts are tools that can define parameters in order to accept inputs at runtime.*

## Analysis Console

The new Sidekick Analysis Console is your home base for deep analysis. This feature, formerly known as the Sidekick Assistant, has been completely revamped so you and Sidekick can collaborate more effectively. In the Analysis Console, the assistant can:

* Interpret and analyze both the code and the content of your conversation (*Figure 1*)
* Search for items in the binary using BNQL (*Figures 1 & 3*)
* Store and retrieve analysis results using Analysis Indexes (*Figure 3*)
* Search, create, register, and run tools that perform tasks to assist in completing your request (*Figure 4*)
* Edit the binary (e.g. rename functions and variables, add comments, etc.) (*Figure 2*)

The Analysis Console maintains a collection of sessions (formerly called pages) that capture the history of your interactions with the assistant. New in this release is the ability to search for content across all sessions and yield results that allow you to navigate to their location within a session.

![Analysis Console](/blog/images/sidekick-3.0/analysis-console-search-sessions.png)
*Figure 6: Analysis Console yields search results from across all sessions.*

To get more familiar with the new Analysis Console, check out our [documentation](https://docs.sidekick.binary.ninja/latest/guide/analysis/analysis_console/).

## Other Changes

### Automation Workbench

Formerly known as the Analysis Workbench, the Automation Workbench provides two key features that let you write smarter, more capable scripts:

* LLMs can be leveraged for program analysis tasks directly from within your script. This is done using the `LLMOperator` construct. For each `LLMOperator`, you can select the model it uses from among a catalog of available models or even one that you provide.
* The Scripting Assistant (formerly called the Coding Assistant) works with you to write both your script and also the prompts for the LLMs used by the `LLMOperator`s of your script.

New in this release for the Automation Workbench are the following:

* Scripts now support parameters, allowing you to create reusable scripts that can be run with different inputs. (*Figure 5*)
* Scripts are now tools that can be executed by the Analysis Console, providing input parameters when needed.
* A script and the `LLMOperator`s that it uses are now combined into a single unit, generated together by the Scripting Assistant.
* You can now manually add `LLMOperator`s to a script and reference them by name.

#### Migrating Existing Scripts

Starting in Sidekick 3.0, `LLMOperator`s accept a single input argument during construction. This argument is the name of the `LLMOperator` specification that the `LLMOperator` should use. If you have existing scripts that use `LLMOperator`s, you will need to update them to use the new format. The easiest way to do this is to use the Scripting Assistant to generate the new code for you. However...