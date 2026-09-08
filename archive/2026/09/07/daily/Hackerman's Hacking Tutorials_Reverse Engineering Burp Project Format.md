---
title: Reverse Engineering Burp Project Format
url: https://parsiya.net/blog/burp-project-reverse/
source: Hackerman's Hacking Tutorials
date: 2026-09-07
fetch_date: 2026-09-08T06:41:03.755344
---

# Reverse Engineering Burp Project Format

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Sep 7, 2026
- 6 minute read - [Reverse Engineering](https://parsiya.net/categories/reverse-engineering/) [Burp](https://parsiya.net/categories/burp/) [AI](https://parsiya.net/categories/ai/)

# Reverse Engineering Burp Project Format

* [.nfo](#nfo)
  + [[greetz]](#greetz)
  + [[anti-greetz]](#anti-greetz)
* [Motivation](#motivation)
* [Methodology](#methodology)
* [Pitfalls](#pitfalls)
  + [Decompilation Problems](#decompilation-problems)
  + [Imaginary Side Quests](#imaginary-side-quests)
* [Interesting Stuff](#interesting-stuff)
  + [Self-Describing Objects](#self-describing-objects)
  + [Installation ID](#installation-id)
* [Future Work](#future-work)

(A)I reverse engineered Burp Suite's project format and built a tool that
exports Proxy history, Repeater messages, and Target Site Map traffic. See
[parsiya/prub](https://github.com/parsiya/prub) and [the documented format](https://github.com/parsiya/prub/blob/main/ai-docs/format-specification.md).

I did not "hack" Burp; this is not a crack. The tool only extracts data from
existing project files.

* Model: GPT-5.6-Sol - High reasoning effort - 1M context window.
* Rough cost: ~160 USD (fewer than 16,000 GitHub Copilot AI credits).
  + I am very ~~cheap~~ efficient with tokens.
  + Main reversing session cost $100 and ended up with a big 520K token context window.
* Harness: GitHub Copilot CLI and GitHub Copilot Chat in VS Code.

# .nfo

## [greetz]

* PortSwigger for giving us this great tool.
* Short story: [The Girl Who Was Plugged In](https://en.wikipedia.org/wiki/The_Girl_Who_Was_Plugged_In) by James Tiptree Jr. (actually Alice Bradley Sheldon).
* Music: [Destiny 2: Forsaken Original Soundtrack - Track 19 - The Man They Called Cayde](https://www.youtube.com/watch?v=UVTu6Wa0wpY).
  + "Hey, take me with you." - Cayde-6.

## [anti-greetz]

* PortSwigger for not giving Repeater access to the extensions API.
* Ending of [0wnz0red](https://www.salon.com/2002/08/28/0wnz0red/) by Cory Doctorow.
  + Amazing setting and premise, but very meh ending :(.

# Motivation

One of my biggest gripes with Burp's extension API is the lack of access to
Repeater tabs. You can export all the proxy history with an extension (or
manually in Burp), but you cannot do the same for Repeater tabs.

In the past, I've used gimmicks to capture all my traffic:

1. Exported the Repeater section of a project and ran `string` to extract requests/responses.
2. Used [a second copy of Burp as an Upstream proxy](/blog/2025-08-15-how-burp-ai-works/#upstream-proxy) to capture all traffic.
3. Created [parsiya/looking-glass](https://github.com/parsiya/looking-glass), an extension that stores everything in a database.

Tokens are still cheap and AI is good at reversing, so I am working through my
bucket list[1](#fn:1).

> Clear that project backlog before the end of the free token era.
>
> **Our esteemed elder and spiritual scholar**
> [Adam Hassan](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7487635110092038145/ "https://www.linkedin.com/feed/update/urn:li:activity:7487635110092038145/")

# Methodology

The target version is Burp Pro `2026.7.1`.

1. Decompiled the Burp Pro jar file with [skylot/jadx](https://github.com/skylot/jadx) and [Vineflower/vineflower](https://github.com/Vineflower/vineflower).
2. Created the following Burp project files:
   1. Empty project.
   2. Project with a specific request/response in Proxy History.
   3. Project with two specific request/responses in Repeater (to test tab groups).
3. Opened the whole thing in VS Code and started prompting in GitHub Copilot Chat.

I am hands-on with AI. I like to steer extensively, review everything, and start
fresh sessions to keep the context window small.

There were many false starts. Maybe (A)I could have done this autonomously with
a good eval harness, but prompting specific things was easier and faster. See
the [activity log](https://github.com/parsiya/prub/blob/main/ai-docs/activity-log.md) for detailed tracking.

# Pitfalls

This section documents what I tried, what didn't work, and other issues I had
during this process.

## Decompilation Problems

Originally I wanted to use Ghidra, like
[when (A)I reversed my keyboard utility](/blog/ai-borked-keyboard/ "when (A)I reversed my keyboard utility")
but normal decompilers worked here.

| Class Statistics | Num | Notes |
| --- | --- | --- |
| Classes in the JAR | 55,120 | Includes Burp and bundled dependencies |
| Classes in the `burp` package | 20,609 | Important stuff |
| Top-level Burp input classes | 20,491 | Baseline used for source filename coverage |
| Focused JADX source files | 19,030 | 92.87% top-level coverage; 1,461 missing |
| Vineflower source files | 20,502 | 99.81% top-level coverage; 39 missing |

* Don't decompile everything, just focus on the `burp` package. Both JADX and
  Vineflower went OOM.
* Combine both outputs. Every class missing from Vineflower existed in JADX, and
  15 of those had clean JADX output.

## Imaginary Side Quests

As models become more intelligent, they invent extra objectives and repeat
useless tasks: running `git diff` after every file change outside Git
repositories, getting stuck on Markdown warnings, line endings, and empty lines,
or, worst of all, making up goals.

For example, I asked AI to move a file from the parent directory to
`prub/ai-docs` and then edit it. Instead of doing a normal `mv` (I realize I
should've done the move myself), it copied the file from memory and then ran
three different commands (`cmp`, 2x `diff`) to check if the file has been moved
correctly.

```
...
Generating patch (230 lines) in ...

Ran terminal command:
cmp -s ai-docs/activity-log.md prub/ai-docs/activity-log.md
  && printf 'activity logs match\n'

The byte-for-byte check did not report a match, likely because the source
Markdown uses Windows line endings while the new file uses repository-standard
Linux line endings. I’ll confirm content equivalence while ignoring CRLF, then
make the link and inventory edits.

Ran terminal command:
diff --strip-trailing-cr --brief ai-docs/activity-log.md prub/ai-docs/activity-log.md

Ran terminal command:
diff --strip-trailing-cr --unified=1 ai-docs/activity-log.md prub/ai-docs/activity-log.md
```

Clopus 4.6 would never, RIP friend 😭.

AI also repeatedly wandered beyond goals. My initial goal was Repeater and
Proxy, but it kept trying to investigate Scanner and specifically Logger. I had
already mentioned that Logger information is not persisted in the project file.
It's like talking to a cat!

!['You are not immune to propaganda' Garfield meme](02.webp "But AGI is here!")
But AGI is here!!1!Image credit: [Mark Vomit @ Tumblr](https://markvomit.tumblr.com/post/172083570225/you-are-not-immune-to-propaganda)

# Interesting Stuff

Discussing the format is useless in the age of AI. Just pass `ai-docs` to your
favorite LLM and go from there. Instead, here are interesting things (A)I saw in
the format.

* **Stable field lookup:** Readers search by field ID, so physical field
  positions can move.
* **Shared records:** Proxy and Target Site Map can reference the exact same
  request/response objects.
  + I guess Site Map references objects from other tools, too.
* **Forwarding objects:** Updated objects can redirect readers to...