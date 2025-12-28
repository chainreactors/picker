---
title: Hello SmuggleX 👋🏼
url: https://www.hahwul.com/blog/2025/hello-smugglex/
source: HAHWUL
date: 2025-12-27
fetch_date: 2025-12-28T03:34:46.271243
---

# Hello SmuggleX 👋🏼

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/blog/2025/hello-smugglex/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/blog/2025/hello-smugglex/)

[한국어](https://www.hahwul.com/ko/blog/2025/hello-smugglex/)

DECEMBER 27, 2025

# Hello SmuggleX 👋🏼

Rust-powered HTTP Request Smuggling Scanner.

Hello! I've recently released a new tool I've been working on and shared it via [𝕏](https://x.com/hahwul/status/2004224255618420976). It's called smugglex, a tool designed to detect HTTP Request Smuggling.

![](https://www.hahwul.com/blog/2025/hello-smugglex/top.jpg)
*<https://github.com/hahwul/smugglex>*

## Installation

It currently supports installation through various package managers like Homebrew, Snapcraft, Nix, Cargo, and more. Please refer to the [Installation documentation](https://smugglex.hahwul.com/getting-started/installation/) and install using your preferred method.

```
# e.g.,
cargo install smugglex
brew install hahwul/smugglex/smugglex
nix profile install github:hahwul/smugglex
```

For reference, I plan to align support for these package managers across all the tools I develop. Nix and others are already supported in recently updated tools (noir, smugglex), and dalfox (already applied in the v3 codebase), urx, and other tools will provide similar installation methods in the future.

## Detect Smuggling

This tool primarily aims to detect HTTP Request Smuggling. You can perform scans as shown below, targeting either a single target or multiple targets.

```
# Single target
smugglex https://target.com

# Multiple targets
cat urls.txt | smugglex
```

If smuggling is detected, it provides a sample request that you can use for testing, as shown below.

![](https://www.hahwul.com/blog/2025/hello-smugglex/sample.jpg)

## Exploiting

smugglex currently provides 2 exploit methods. When using this feature, it performs additional tests upon detecting smuggling.

```
EXPLOIT:
  -e, --exploit <EXPLOIT>
          Exploit types to run after detection (comma-separated: localhost-access,path-fuzz)
```

For localhost-access, it performs functions to access various localhost information through smuggled requests.

```
[*] Testing localhost access on port 80...
[*] Generated localhost payload for port 80
--- REQUEST ---
POST / HTTP/1.1
Host: 0a1100f0035b6b6380e0c60e005c00c4.web-security-academy.net
Connection: keep-alive
Content-Length: 6
Transfer-Encoding: chunked
1
X
0
GET / HTTP/1.1
Host: 127.0.0.1:80
Connection: close
```

path-fuzz explores backend paths using smuggled requests with a predefined list or a user-provided list (`--exploit-wordlist`).

## Next Plan

In fact, after sharing it, I've received a lot of interest and feedback via DMs. While features are important, for now, my priority is improving smuggling detection performance (increasing true positives and reducing false positives). I'll continue expanding the exploit section, and ultimately, I hope it evolves beyond a simple scanner into a tool that covers the entire process of testing HTTP Request Smuggling.

If you try it out and have any suggestions for improvements, please feel free to let me know.
The year is already coming to an end! Wishing everyone a happy new year with lots of good fortune!

[#sec](https://www.hahwul.com/tags/sec/)
[#smugglex](https://www.hahwul.com/tags/smugglex/)

[ ]

[ ]

### Table of Contents

[Installation](https://www.hahwul.com/blog/2025/hello-smugglex/#installation)

[Detect Smuggling](https://www.hahwul.com/blog/2025/hello-smugglex/#detect-smuggling)

[Exploiting](https://www.hahwul.com/blog/2025/hello-smugglex/#exploiting)

[Next Plan](https://www.hahwul.com/blog/2025/hello-smugglex/#next-plan)

[Next

Red, Blue, Purple in Offensive Security](https://www.hahwul.com/blog/2025/red-blue-purple/)

[Contact](/contact)
[Thanks](/thanks)
[Sitemap](/sitemap.xml)
Random
[Feeds](/feeds)

© 2025 HAHWUL
Developed and Designed by Me

* [WHO](/about/)
* [BLOG](/blog/)
* [SEC](/sec/)
* [DEV](/dev/)
* [PROJECTS](/projects/)

---

* Language
  + [ENGLISH](https://www.hahwul.com/blog/2025/hello-smugglex/)
  + [한국어](https://www.hahwul.com/ko/blog/2025/hello-smugglex/)