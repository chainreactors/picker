---
title: 2024 Reverse Engineering Survey: The State of the Industry
url: https://binary.ninja/2024/11/08/user-survey-results.html
source: Binary Ninja
date: 2024-11-09
fetch_date: 2025-10-06T19:16:41.351099
---

# 2024 Reverse Engineering Survey: The State of the Industry

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

## 2024 Reverse Engineering Survey: The State of the Industry

* Brent Fosdick
* Å Ã¡rka Fletcher
* 2024-11-08
* [reversing](/tag/reversing), [meta](/tag/meta), [announcements](/tag/announcements)

We are excited to share results from our 2024 Reverse Engineering survey! This annual survey helps unpack the current state of the reverse engineering industry and gives insight into how Binary Ninja can better serve the reverse engineering community. Letâs dive into the insights.

![2024 Reverse Engineering Survey: The State of the Industry](/blog/images/2024-user-survey/2024-reverse-engineering-survey.png)

## User Experience Breakdown

### How experienced do you consider yourself in reverse engineering?

Our survey tapped into a broad range of skill levels. A solid 34% of respondents consider themselves at the intermediate level, while 25% feel theyâve reached advanced territory. Another 15% rated themselves as experts, and plenty of folks mentioned theyâre just getting started on their reverse engineering journey.

![How experienced do you consider yourself in reverse engineering?](/blog/images/2024-user-survey/01-how-experienced-are-you-2.svg)

### I reverse engineerâ¦

From our findings, 56% of respondents reverse engineer on the job, and 11% do it as part of their studies. Even more telling, 63% dig into reverse engineering outside of work, showing just how passionate and dedicated the hobbyist community really is.

![I reverse engineerâ¦](/blog/images/2024-user-survey/02-i-reverse-engineer-2.svg)

### Why do you reverse engineer?

The reverse engineers surveyed partake heavily in hobbyist challenges like modding, CTFs, and crackmes, pulling in 79% of the communityâs focus. Vulnerability research is another close contender at 64%, while malware analysis captures the interest of 48%. Emulation and internal software auditing each stand out, both at ~22%. Code recovery sits at 18% of respondents, while 15% of participants reverse engineer for interoperability reasons.

![For what purposes do you reverse engineer?](/blog/images/2024-user-survey/03-for-what-purposes-do-you-reverse-engineer-2.svg)

### How many hours per week would you estimate you spend reverse engineering?

The survey shows that a sizable group is putting in some serious reverse engineering time â 35% are logging over 10 hours weekly. Meanwhile, 35% spend between 5-10 hours and 23% dedicate a solid 1-5 hours each week.

![How many hours per week would you estimate you spend reverse engineering?](/blog/images/2024-user-survey/04-how-many-hours-per-week-on-reverse-engineering-2.png)

Our analysis shows that the most dedicated reverse engineers often come from organizations where reverse engineering isnât just a side task â itâs a central focus shared by several team members. This suggests that companies with robust reverse engineering teams are truly diving deep, making these tools a key part of their daily workflow.

## Tooling for Reverse Engineering

### Whatâs your go-to solution for debugging & dynamic analysis?

When it comes to debugging and dynamic analysis, gdb is the top choice, used by 61% of respondents. Additionally, tools like x64dbg, Binary Ninjaâs debugger, and LLDB are commonly employed, highlighting the diverse and versatile toolkit our users depend on.

![What's your go-to solution for debugging & dynamic analysis?](/blog/images/2024-user-survey/10-whats-your-goto-solution-for-debugging-2.png)

### How often do you use reversible/time-travel debugging?

Reversible or time-travel debugging is still an emerging feature, with 52% of respondents yet to explore it. However, 24% use it rarely and 11% occasionally, indicating growing interest and potential for increased adoption as they become more familiar with its capabilities.

![How often do you use reversible/time-travel debugging?](/blog/images/2024-user-survey/11-reversible-debugging.png)

## Binary Ninja vs. Ghidra vs. IDA

We cross-referenced variables from the survey results to build up profiles of Binary Ninja, Ghidra, and IDA users. From this, we were able to determine the most common activities, time spent on reverse engineering activities per week, preferred debugging tools, and favorite plugins for each user profile.

| Â | Binary Ninja | IDA | Ghidra |
| --- | --- | --- | --- |
| Most common activities | Vulnerability Research, Hobby - Modding, CTF | Malware Analysis, Hobby - Modding, CTF, Crackme | Malware Analysis, Hobby - Modding, CTF, Crackme |
| Time spent on reverse engineering activities per week | 10+ hours | 10+ hours | 1-5 hours |
| Preferred debugging tool | gdb | x64dbg | gdb |
| Favorite plugins | bindiff, lighthouse | bindiff | gef |

## Binary Ninja Breakdown

Thatâs it for our overall population summary, but what about the questions we asked specifically of Binary Ninja users?

### Do you use automatic updates?

A significant 82% of users choose automatic updates, ensuring they always have the latest features and security improvements. While most individuals surveyed opted for automatic updates, a significant portion of teams in larger organizations avoid them in favor of manually managing updates.

![Do you use automatic updates?](/blog/images/2024-user-survey/05-automatic-updates.png)

### Which branch do you use?

In general, users show a preference for the dev branch, with 52% opting for it over the stable branch. Although users generally prefer dev over stable, the more experienced users tended to prefer stable branches. This indicates a balance within the community between those eager to test and utilize the latest features and those prioritizing reliability.

![Which branch do you use?](/blog/images/2024-user-survey/06-which-branch-do-you-use-3.png)

### Have you heard about Sidekick?

Awareness of [Binary Ninja Sidekick](https://sidekick.binary.ninja/), our AI-powered extension, is high, with 82% of users familiar with it. This widespread awareness highlights the growing interest in leveraging AI to enhance reverse engineering workflows.

![Have you heard about Sidekick?](/blog/images/2024-user-survey/07-binary-ninja-sidekick-2.png)

## Why Do This Survey?

Our annual survey not only helps us better understand the overall market and produce general summaries like this for the benefit of the community as a whole, but it also gives us concrete data we can use to make Binary Ninja better. Hereâs a list of specific changes weâve made in the last year, many of which were directly inspired by results from the previous survey. Your feedback matters to us!

Based on last yearâs survey results, we implemented several key updates:

* [Our 4.0 (Dorsai) Release](https://binary.ninja/2024/02/28/4.0-dorsai.html)
* [Restructuring the Binary Ninja Decompiler](https://binary.ninja/2024/06/19/restructuring-the-decompiler.html)
* [Sidekick 1.0 Release](https://binary.ninja/2024/04/18/sidekick-release.html)
* [Binary Ninja Free](https://binary.ninja/free)
* [Types View](https://docs.binary.ninja/guide/types/basictypes.html#types-view)
* [Type Archives](https://docs.binary.ninja/guide/types/typearchives.html)
* [Windows Kernel Debugging](https://docs.binary.ninja/guide/debugger/windows-k...