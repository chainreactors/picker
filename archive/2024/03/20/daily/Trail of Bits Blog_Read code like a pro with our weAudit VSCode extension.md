---
title: Read code like a pro with our weAudit VSCode extension
url: https://blog.trailofbits.com/2024/03/19/read-code-like-a-pro-with-our-weaudit-vscode-extension/
source: Trail of Bits Blog
date: 2024-03-20
fetch_date: 2025-10-04T12:11:57.415232
---

# Read code like a pro with our weAudit VSCode extension

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Read code like a pro with our weAudit VSCode extension

Filipe Casal

March 19, 2024

[tool-release](/categories/tool-release/)

Today, we’re releasing [weAudit](https://marketplace.visualstudio.com/items?itemName=trailofbits.weaudit), the collaborative code-reviewing tool that we use during our security audits. With weAudit, we review code more efficiently by taking notes and tracking bugs in a codebase directly inside VSCode, reducing our reliance on external tools, ensuring we never lose track of bugs we find, and enabling us to share that information with teammates.

We designed weAudit with features that are crucial to our auditing process:

* **Bookmarks for findings and notes:** Bookmark code regions to identify findings or add audit notes.
* **Tracking of audited files:** Mark entire files as reviewed.
* **Collaboration:** View and share findings with multiple users.
* **Creation of GitHub issues:** Fill in detailed information about a finding and create a preformatted GitHub issue right from weAudit.

You can install it through the [VSCode marketplace](https://marketplace.visualstudio.com/items?itemName=trailofbits.weaudit) and find its code in our [`vscode-weaudit`](https://github.com/trailofbits/vscode-weaudit) repo.

![](/img/wpdump/adf7a6e76cd6e5ee2ea8305cd2c3db9a.png)

## Why we built weAudit

When we review complex codebases, we often compile detailed notes about both the high-level structure and specific low-level implementation details to share with our project team. For high-level notes, standard document sharing tools more than suffice. But those tools are not ideal for sharing low-level, code-specific notes. For those, we need a tool that allows us to share notes that are more tightly coupled with the codebase itself, almost like using post-it notes to navigate through a complex book. Specifically, we need a tool that allows us to do the following:

* Quickly navigate through areas of interest in the codebase
* Visually highlight significant areas of the code
* Add audit notes to certain parts of the codebase

![](/img/wpdump/968abf762165a18ce0b4566438e3a9ea.png)

For some time, I used a very simple extension for VSCode called “Bookmarks”, which allowed me to add basic notes to lines of code. However, I was never satisfied with this extension, as it was missing crucial features:

* The highlighted code did not display the notes I had written next to the code.
* I had no way of sharing code coverage information with my client or fellow engineers auditing the codebase.
* I had no way of sharing my notes and bookmarks. During an audit with a team of engineers, I need to be able to share these things with my team so that my knowledge is their knowledge, and vice versa.

All of us engineers at Trail of Bits agreed that we needed a better tool for this purpose. We realized that if we wanted an extension tailored to our needs, we would need to create it. That is why we built weAudit.

## weAudit’s main features

The features we built into weAudit streamline our process of bookmarking, annotating, and tracking code files under audit, sharing our notes, and creating GitHub issues for findings we discover.

### Bookmarks

The extension supports two types of bookmarks: **findings**, which represent buggy or suspicious regions of code, and **notes**, which represent personal annotations about the code.

You can add findings and notes to the current code snippet selection by running the corresponding VSCode commands or using the keyboard shortcuts:

* “weAudit: New Finding from Selection” (shortcut: Cmd + J)
* “weAudit: New Note from Selection” (shortcut: Cmd + K)

These commands will highlight the code in the editor and create a new bookmark in the “List of Findings” view in the sidebar.

By clicking on an item in the “List of Findings” view, you can navigate to the corresponding region of code.

Files with a finding will have a “!” annotation next to the file name in both the file tree of VSCode’s default “Explorer” view and in the tab above the editor, making it immediately clear which files have findings.
![](/img/wpdump/4f90ac99ba91d78877ccbdbd216e6183.png)

The highlight colors can be customized in the extension settings.

### Tracking audited files

After reviewing a file, you can mark it as audited by running the “weAudit: Mark File as Reviewed” command or its keyboard shortcut, Cmd + 7. The whole file will be highlighted, and the file name in both the file tree and the tab above the editor will be annotated with a ✓.

The highlight color can be customized in the extension settings.

### Daily log

Have you ever had trouble remembering which files you reviewed the previous week? Or do you just really like meaningless statistics such as the number of lines of code you read in a single day? You can see these stats by showing the daily log, accessible from the “List of Findings” panel.

![](/img/wpdump/4ef2ff3480ef6f382c6394f13e2e9824.png)

You can also view the daily log by running the “weAudit: Show Daily Log” command in the command palette.

### Collaboration with multiple users

You can share weAudit files (located in the `.vscode` folder) with your co-auditors to share findings and notes about the code. In the “weAudit Files” panel, you can toggle to show or hide the findings from each user by clicking on each entry. The colors for other users’ findings and notes and for your own findings and notes are customizable in the extension settings.

![](/img/wpdump/6ff9e39b96eade29dffdcb35947d3e93.png)

### Detailed findings

You can fill in detailed information about a finding by clicking on it in the “List of Findings” view in the sidebar, where you can add all the information we include in our audit reports: title, severity, difficulty, description, exploit scenario, and recommendations for resolving the issue.

![](/img/wpdump/7578da44a5854ffdd7e0a7dc31f279f4.png)

This information is then used to prefill a template, allowing you to quickly open a GitHub issue with all of the relevant details for the finding.

You can find more details and information about other features in our [README](https://github.com/trailofbits/vscode-weaudit).

### Try it out for yourself!

If you use VSCode to navigate through large codebases, we invite you to try weAudit—even if you are not looking for bugs—and let us know what you think!

We welcome any bug reports, feature requests, and contributions in our [`vscode-weaudit`](https://github.com/trailofbits/vscode-weaudit) repo.

If you’re interested in VSCode extension security, check out our “[Escaping misconfigured VSCode extensions](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/)” and “[Escaping well-configured VSCode extensions (for profit)](https://blog.trailofbits.com/2023/02/23/escaping-well-configured-vscode-extensions-for-profit/)” blog posts.

[Contact us](https://www.trailofbits.com/contact/) if you need help securing your VSCode extensions or any other application.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-fi...