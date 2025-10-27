---
title: Sidekick 2.0
url: https://binary.ninja/2024/08/12/sidekick-2.0.html
source: Binary Ninja
date: 2024-08-13
fetch_date: 2025-10-06T18:04:00.769242
---

# Sidekick 2.0

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

## Sidekick 2.0

* [Brian Knudson](https://github.com/kristopax)
* [Tim Bryant](https://github.com/iamausertoo)
* 2024-08-12
* [sidekick](/tag/sidekick)

Itâs been just under 4 months since we officially launched Sidekick 1.0. During that time, we have been busy making improvements and creating new ways to make reversing even easier. All of that hard work has culminated into the release of Sidekick 2.0, which we are pleased to introduce to you today.

We donât increment major version numbers lightly, and Sidekick has earned this bump with a major new feature that will change the way you reverse engineer in addition to other improvements and fixes.

Not long ago, we gave a [sneak preview](https://www.youtube.com/watch?v=IdNFMIQ9roQ&t=4681s) of the Analysis Workbench (formerly called the Analysis Console) and wrote a [blog](https://binary.ninja/2024/06/28/sidekick-beyond-chatgpt.html) introducing its concepts in advance of this release. With the Sidekick 2.0 release today, itâs here and ready to save you time and effort.

## Analysis Workbench: Your AI-Enhanced Command Center

The Analysis Workbench is a bridge between your analytical skills and advanced AI capabilities. Itâs designed to complement Binary Ninjaâs existing UI and API, providing a clean and intuitive interface for translating your high-level analysis goals into actionable scripts and real results.

Behind this simple interface (Figure 1), it orchestrates an array of AI models along with the Binary Ninja API to understand and perform your intended analysis.

![Analysis Workbench](/blog/images/sidekick-2.0/analysis-workbench.png)

*Figure 1. The Analysis Workbench combines the best of both online and offline models to solve problems that used to take far more manual labor.*

### Effortless AI-Powered Reverse Engineering with Sidekick

When you describe a task to the Analysis Workbench, several processes take place that take a high level task and decompose it into steps, which are mediated by AI and which leverage AI for binary analysis. AI can be very helpful, but not if it creates extra work. While the AI capabilities of Sidekick are powerful, theyâre designed to enhance your expertise, not replace it:

* The Analysis Workbench lets you engage in a dialogue with the system, refining your analysis goals and tweaking the generated scripts through natural language interaction (Figure 2).

  ![Analysis Workbench Coding Assistant](/blog/images/sidekick-2.0/analysis-workbench-coding-assistant.png)

  *Figure 2. The Coding Assistant helps you write scripts that leverage AI models and the Binary Ninja API.*
* For those who prefer a hands-on approach, you can directly edit the generated scripts and customize the prompt templates generated for the AI models (Figure 3). You can also see how Sidekick translated your high-level goals into concrete analysis steps. This transparent approach ensures that whether youâre a seasoned reverse engineer or just starting out, you can leverage AI and the Binary Ninja API at a level that suits your expertise and preferences, while also learning from the systemâs approach to problem-solving.

  ![Analysis Workbench Operator Template](/blog/images/sidekick-2.0/analysis-workbench-operator-template.png)

  *Figure 3. The Operator tab shows you how Sidekick translates your requests into LLM prompts.*

The beauty of the Analysis Workbench lies in its ability to abstract away the complexities of AI integration while still allowing you to go under the hood when you want to.

* For veterans, itâs a force multiplier. Quickly prototype complex analysis workflows, automate repetitive tasks, and explore new approaches to challenging binaries.
* For newcomers, itâs a learning accelerator. Access advanced analysis techniques without needing to master every detail of the Binary Ninja API or the nuances of prompt engineering for large language models.

### Sidekick in Action

Enough talk. Check out these blog posts to see Sidekick solving analysis tasks with ease!

* [Sidekick in Action: Deobfuscating Strings in Amadey Malware](https://binary.ninja/2024/08/12/sidekick-in-action-deobfuscating-strings-in-amadey-malware.html)
* [Sidekick in Action: Analyzing Firmware](https://binary.ninja/2024/08/12/sidekick-in-action-analyzing-firmware.html)

### Whatâs Next

To get more familiar with the Analysis Workbench, check out our [documentation](https://docs.sidekick.binary.ninja/guide/analysis_workbench/).

In the future, we will be publishing more blogs about this new feature, so stay tuned!

For now, go ahead and [sign up](https://sidekick.binary.ninja/account/purchase_plan) for Sidekick! If youâre already a subscriber, [update](https://docs.sidekick.binary.ninja/getting-started/#updating-the-plugin) your plugin now.

## Updated Indexes Sidebar

Indexes have been simplified to focus on their main purpose - storing and displaying items and metadata in the binary for easy reference. The ability to create indexes has been moved to the Analysis Workbench. We believe this change allows you to create indexes in a more streamlined and intuitive way.

### Index Pinning

Are you one of those people that like to look at multiple things at once? Well, we created Index Pinning just for you. Now, if you want to open an index in a separate pane within the main view frame, you can (Figure 4). In fact, you can do it multiple times to your heartâs contentâ¦ or until you run out of display real estate.

![Index Pinning](/blog/images/sidekick-2.0/index-pinning.png)

*Figure 4. Metadata can be easily viewed in the Preview area. Indexes can be pinned as new panes for easy reference.*

### Migrating Existing Indexes and Indexers

To migrate your existing indexes to the new version of Sidekick, you will need to regenerate them using the Analysis Workbench. We provide two straightforward options to help you migrate your indexer scripts:

1. To import indexer scripts from an existing BNDB, load the BNDB and select `Import Indexer Scripts from Binary View` from the top-level `Sidekick` Plugin menu. Select which indexers you want to convert to Analysis Workbench scripts. Once imported, go to the Analysis Workbench and search for the script by name. Then, run it to regenerate the index and its entries.

   ![Sidekick Plugin Main Menu - Import Indexer Scripts Actions](/blog/images/sidekick-2.0/import-scripts.png)
2. To import indexer scripts from your local indexer catalog, select `Import Indexer Scripts from Indexer Catalog` from the top-level `Sidekick` Plugin menu. Select which indexers you want to convert to Analysis Workbench scripts. Once imported, go to the Analysis Workbench and search for the script by name. Then, run it to regenerate the index and its entries.

We have made a best-effort to convert your legacy indexer scripts to Analysis Workbench scripts. However, we may have not captured all scenarios and you may need to revise the converted script for it to run successfully. Thankfully, the Sidekick Coding Assistant within the Analysis Workbench script editor is right there to help you.

## Other Updates and Minimum Requirements

These arenât the only improvements weâve made, of co...