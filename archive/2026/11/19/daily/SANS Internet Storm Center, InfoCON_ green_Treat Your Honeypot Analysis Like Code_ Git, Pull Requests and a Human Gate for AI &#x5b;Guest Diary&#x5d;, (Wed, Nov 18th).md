---
title: Treat Your Honeypot Analysis Like Code: Git, Pull Requests and a Human Gate for AI &#x5b;Guest Diary&#x5d;, (Wed, Nov 18th)
url: https://isc.sans.edu/diary/rss/33534
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-19
fetch_date: 2026-11-20T09:23:09.566528
---

# Treat Your Honeypot Analysis Like Code: Git, Pull Requests and a Human Gate for AI &#x5b;Guest Diary&#x5d;, (Wed, Nov 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33532)

Click HERE to learn more about classes Guy is teaching for SANS

# [Treat Your Honeypot Analysis Like Code: Git, Pull Requests and a Human Gate for AI [Guest Diary]](/forums/diary/Treat%2BYour%2BHoneypot%2BAnalysis%2BLike%2BCode%2BGit%2BPull%2BRequests%2Band%2Ba%2BHuman%2BGate%2Bfor%2BAI%2BGuest%2BDiary/33534/)

**Published**: 2026-11-18. **Last Updated**: 2026-11-19 01:53:48 UTC
**by** [Kevin Truong, SANS.edu BACS Student](/handler_list.html#kevin-truong,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Treat%2BYour%2BHoneypot%2BAnalysis%2BLike%2BCode%2BGit%2BPull%2BRequests%2Band%2Ba%2BHuman%2BGate%2Bfor%2BAI%2BGuest%2BDiary/33534/#comments)

[This is a Guest Diary by Kevin Truong, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Introduction**
When conducting analysis of honeypot activity, it's easy for it to start as a pile of terminal output. The process is manual; screenshots of the terminal, plus a text file that gets edited in a common word processing application until it is "done". There is no say whether a certain number came from a certain query, what changed between drafts, or who decided to drop a caveat.

While hosting my own honeypot sensor, I wrote up three attacks:

* An SSH brute force that logged in as mysql/mysql [[1](https://github.com/kevtruo/security/tree/main/analysis/2026-10-18-ssh-brute-force-mysql-default-creds)]
* A bot looking for Telegram Desktop sessions and SMS modems [[2](https://github.com/kevtruo/security/tree/main/analysis/2026-10-19-telegram-sms-recon-bot)]
* A month of RedTail exploits against PHP plus one oversized multipart POST that matches the shape of PHP2Shell (CVE-2026-109618) [[3](https://github.com/kevtruo/security/tree/main/analysis/2026-10-03-php-vulnerability-hunt)].

Instead of a document folder though, I kept every report in a public git repository [[4](https://github.com/kevtruo/security)] and changed it only through pull requests. Supporting me in my analysis was an AI coding agent (Claude Code), which also drafted reports as a separate GitHub machine account. I wanted to give my Claude Code sessions a tangible identity in the code submission and review process, where a dedicated GitHub account could propose changes but never approve or merge them.

Even though I drove every part of the analysis process, the code review of each pull request marked a deliberate step in my workflow which acted as both a gate and a spot-check of the content I was producing.

This diary describes that setup, what the git history shows about how well it worked, and what I would change.

**Why Do It**

The question this post answers are: can version control and a mandatory human review make AI-drafted security analysis trustworthy enough to publish?

It matters for three reasons:

* **Reproducibility**. An indicator list or a timeline is only as good as the query behind it. If the query and its output are stored next to the claim, anyone can check it.
* **Public safety**. Honeypot reports contain things that must not be published: the sensor's own address, its hostname, its cloud account, and sometimes attacker material such as private keys. Once something reaches a public git history, deleting the file does not remove it [[4](https://github.com/kevtruo/security), SECURITY.md].
* **AI accountability**. Language models are fluent and are confident; but fluency and confidence don't mean accuracy. If an AI is part of the workflow, there needs to be a record of what it wrote, what a human changed, and who approved it.

**The Setup**

The repository has one folder per attack. Each folder holds the summary, every piece of evidence it cites, and a hash list:

![](https://isc.sans.edu/diaryimages/images/Kevin_Truong_pic1.png)

Every exhibit in a report's appendix shows the exact jq query that produced it, for example:

![](https://isc.sans.edu/diaryimages/images/Kevin_Truong_pic2.png)

Before anything leaves the sensor, output is passed through a filter that replaces the sensor's address with <sensor-ip>, and then hashed. Anyone who clones the repository can confirm the evidence has not changed since it was committed:

![](https://isc.sans.edu/diaryimages/images/Kevin_Truong_pic3.png)

The workflow around those files is shown in Figure 1.

![](https://isc.sans.edu/diaryimages/images/Kevin_Truong_pic4.png)

The important pieces are:

* A separate identity for the AI. Pull requests from the machine account are written by Claude Code sessions. It is a machine account I operate, and the README says so publicly [[4](https://github.com/kevtruo/security)].
* The AI can write but not merge. A GitHub ruleset on main requires a pull request with one approval, blocks force-pushes and branch deletion and has no bypass actors. The AI account has written access, but GitHub does not let an author approve their own pull request, so it can never get a change into main alone.
* A public-safety checklist on every PR. The pull request template asks the author to confirm that they read the full diff, that the secret scan is clean, that every IP and account is a placeholder (attacker indicators excepted), that there are no hostnames or local paths, and that attachments were checked by hand. The AI fills this in and I check it.
* A secret scanner before every commit. A pre-commit hook runs gitleaks locally.

**Options to Close Gaps**

Comparing the ruleset with my own design notes [4, homelab/change-control.md] showed where the live settings fall short:

![](https://isc.sans.edu/diaryimages/images/Kevin_Truong_pic5.png)

Fortunately, none of these needs’ new tools. These are repository settings and habits, which is the point. The controls that are deployed are the ones enforced by the server (GitHub), not ones written into a file the AI could edit on its own branch.

**Who Benefits**

* Students and new analysts get a structure that forces each claim to point at evidence, and a history that shows a reviewer how their analysis improved. This works as a solo project, but the benefits grow exponentially with multiple analysts and reviewers.
* Honeypot operators and DShield contributors can publish findings with less risk of leaking their sensor's identity, because the scrubbing and checklist happen before a merge, not after.
* Teams adopting AI assistants get a pattern they can copy: a separate identity for the AI, server-side merge controls, and a checklist that the AI must fill in honestly. The record shows exactly where the AI's work ended and a human's began.
* Readers of the reports can verify them. Every indicator traces to a query, and every query's output has a hash.

**Conclusion**

Version control is not new to security teams, where it's commonly seen in areas like detection rules and infrastructure code. That said though, treating something like honeypot/log analysis like code gave me reproducible evidence, a reviewable history, and a safe way to use an AI drafter: it proposed, I reviewed, and only I could merge. The history also kept me honest about the parts that did not work. Those gaps are visible because the work was in git, and each has a simple fix in the repository settings.

**References**

[1] Honeypot Attack Summary: SSH Brute Force from 77.239.124.204. https://github.com/kevtruo/security/tree/main/analysis/2026-10-18-ssh-brute-force-mysql-default-creds
[2] Honeypot Attack Summary: Telegram Session and SMS Modem Reconnaissance Bot. https://github.com/kevtruo/security/tree/main/analysis/2026-10-19-telegram-sms-recon-bot
[3] Honeypot Attack Summary: PHP Vulnerability Hunt, RedTail and a PHP2Shell-Pattern Request. https://github.com/kevtruo/security/tree/main/analysis/2026-10-03-php-vulnerability-hunt
[4] kevtruo/security repository...