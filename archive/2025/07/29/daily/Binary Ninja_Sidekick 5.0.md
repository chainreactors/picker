---
title: Sidekick 5.0
url: https://binary.ninja/2025/07/28/sidekick-5.0.html
source: Binary Ninja
date: 2025-07-29
fetch_date: 2025-10-06T23:52:31.957060
---

# Sidekick 5.0

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

## Sidekick 5.0

* [Brian Knudson](https://github.com/kristopax)
* [Tim Bryant](https://github.com/iamausertoo)
* 2025-07-28
* [sidekick](/tag/sidekick)

Weâre excited to announce Sidekick 5.0 - our latest vision for AI-assisted reverse engineering with Binary Ninja. In this release, Sidekick comes with a new capability to proactively work on tasks that complement your efforts without requiring your supervision. Sidekick also captures and maintains insights from this analysis in a new, fully editable knowledge store called the Notebook. Additionally, weâve made many important changes and improvements to ensure that Sidekick continues to make reverse engineering faster and easier than ever.

## Collaborative AI: Works With You, Not Instead of You

Sidekick 5.0 introduces active collaboration - a smarter way to work alongside AI thatâs always in sync with your analysis, never in your way. Sidekick pays attention to what youâre working on and automatically queues up helpful analyses that complement and support your current goals. The new [Tasks](https://docs.sidekick.binary.ninja/v5.0/guide/tasks/) sidebar is the central location where you can review and manage all of Sidekickâs ongoing and completed tasks. Every part of the process is fully transparent: from your original task description, to the plan and instructions Sidekick generates, to the steps it takes and the final results - so you always know exactly whatâs happening and why.

* Tasks Sidebar
* Tasks Results
* Tasks Log

![Tasks Sidebar](/blog/images/sidekick-5.0/features-tasks-sidebar.png)

![Tasks Results](/blog/images/sidekick-5.0/features-tasks-results.png)

![Tasks Log](/blog/images/sidekick-5.0/features-tasks-log.png)

Want even more control? You can [delegate specific tasks](https://docs.sidekick.binary.ninja/v5.0/guide/tasks/#delegating-tasks) by describing what you want Sidekick to tackle. While you move on to other parts of your project, Sidekick handles the analysis in the background and has results ready when you return.

* Delegate Tasks
* Review Delegated Tasks

![Delegate Tasks](/blog/images/sidekick-5.0/features-tasks-new-task.png)

![Review Delegated Tasks](/blog/images/sidekick-5.0/features-delegate-tasks-review.png)

Every reverse engineering workflow is unique, which is why Sidekick lets you [set your preferred mode](https://docs.sidekick.binary.ninja/v5.0/guide/tasks/#setting-the-collaboration-level) of automation and level of oversight. Whether you want to keep a close eye on every step or let Sidekick take the initiative, youâre always in control. This combination of proactive support and configurable supervision means you get exactly the assistance you want - helping you work faster, stay focused, and solve tough problems with less friction.

![Collaboration Mode](/blog/images/sidekick-5.0/features-tasks-collaboration-mode.png)

## Binary-Wide Context: Captures and Integrates Insights Across an Entire Binary

The new [Notebook](https://docs.sidekick.binary.ninja/v5.0/guide/records/#notebook) sidebar brings together everything you and Sidekick discover during your reverse engineering efforts, storing it in one place as organized, easily accessible documents. Insights from Sidekickâs analysis tasks are automatically captured as categorized documents, each with clear provenance, so you always know where information came from. You can also [create your own documents](https://docs.sidekick.binary.ninja/v5.0/guide/records/#adding-documents) to capture personal findings, theories, or workflow notes - everything is editable and under your control.
The Notebook is not just a passive record. Sidekick actively references the information stored in your Notebook as context for ongoing and future analyses, ensuring that discoveries in one part of the binary inform your work everywhere else. Even features like the Chat assistant draw on this collective knowledge, making every insight you or Sidekick uncover available exactly when you need it.

* Notebook Sidebar
* Add Documents

![Notebook Sidebar](/blog/images/sidekick-5.0/features-notebook-sidebar.png)

![Add Documents](/blog/images/sidekick-5.0/features-notebook-add.png)

## Other Notable Changes

### Better Models

Sidekick 5.0 leverages upgraded language models for all of its core features. These new models improve the quality, accuracy, and context-awareness of Sidekickâs analysis and explanations, giving you smarter insights and more reliable results across every workflow.

### Chat: Concise Answers and Better Performance

[Chatting](https://docs.sidekick.binary.ninja/v5.0/guide/chat/) with Sidekick is faster and more efficient than ever. Youâll notice faster response times, more concise and relevant answers, and a smoother overall experience - whether youâre digging into technical details or asking for high-level guidance.

### Binary Ninja Query Language Improvements

Weâve enhanced the [Binary Ninja Query Language](https://docs.sidekick.binary.ninja/v5.0/guide/bnql/) to make it even more powerful and intuitive. Expect easier filtering, richer query capabilities, and improved results - making it simpler for Sidekick to surface exactly the information you need during your analysis.

### Changes to Names and Icons

Minor changes to note if you are upgrading from Sidekick 3.

|  |  |  |
| --- | --- | --- |
| ![Chat Sidebar Name and Icon](/blog/images/sidekick-5.0/icons-chat.png) | **[Chat](https://docs.sidekick.binary.ninja/v5.0/guide/chat/)** | The Analysis Console sidebar is now simply called **Chat**, matching its primary mode of interaction. Along with this, what were previously called âSessionsâ are now referred to as **Chats** for consistency and clarity. |
| ![Decompilation Suggestions Sidebar Icon](/blog/images/sidekick-5.0/icons-suggestions.png) | **[Decompilation Suggestions](https://docs.sidekick.binary.ninja/v5.0/guide/suggestions/)** | The **Decompilation Suggestions** sidebar icon is now a pencil with magic sparkles. Is it because it magically edits the binary to improve code clarity, or because it makes your code so clean it sparkles? You decide. |
| ![Automation Workbench Sidebar Icon](/blog/images/sidekick-5.0/icons-automation-workbench.png) | **[Automation Workbench](https://docs.sidekick.binary.ninja/v5.0/guide/automation_workbench/)** | The **Automation Workbench** sidebar icon is now a hammer. |
| ![Indexes Name and Icon](/blog/images/sidekick-5.0/icons-indexes.png) | **[Indexes](https://docs.sidekick.binary.ninja/v5.0/guide/records/#indexes)** | The Analysis Indexes sidebar is now called just **Indexes**, and its icon is a table to better suit the way its contents are displayed. |
| ![Notebook Sidebar Icon](/blog/images/sidekick-5.0/icons-notebook.png) | **[Notebook](https://docs.sidekick.binary.ninja/v5.0/guide/records/#notebook)** | The new **Notebook** sidebar uses the icon from the previous Analysis Indexes sidebar, which is an open book. |
| ![Tasks Sidebar Icon](/blog/images/sidekick-5.0/icons-tasks.png) | **[Tasks](https://docs.sidekick.binary.ninja/v5.0/guide/tasks/)** | The new **Tasks** sidebar uses the icon from the previous Automation Workbench sidebar, which is a stack of car...