---
title: An Evening with Claude (Code)
url: https://blog.xpnsec.com/An-Evening-with-Claude-Code/
source: XPN InfoSec Blog
date: 2025-11-29
fetch_date: 2025-11-30T03:26:20.259478
---

# An Evening with Claude (Code)

[![XPN Logo](/images/profile-image.jpg)](https://blog.xpnsec.com)
[XPN / Adam Chester](https://blog.xpnsec.com)

[Posts](https://blog.xpnsec.com)
[Tags](https://blog.xpnsec.com/tags)
[About](https://blog.xpnsec.com/about)

[Twitter](https://twitter.com/_xpn_ "Twitter")
[GitHub](https://github.com/xpn "GitHub")
[LinkedIn](https://linkedin.com/in/xpn "LinkedIn")
[RSS](https://blog.xpnsec.com/rss/ "RSS Feed")
[Instagram](https://www.instagram.com/xpnsecpub "Instagram")

[« Back to home](https://blog.xpnsec.com "Back to homepage")

# An Evening with Claude (Code)

![An Evening with Claude (Code)](https://assets.xpnsec.com/an-evening-with-claude-code/cover.webp)

Posted on 29th November 2025

---

[claude](/tags#claude) [llm](/tags#llm) [mcp](/tags#mcp) [vulnerability](/tags#vulnerability) [cve](/tags#cve)

16 min read

I’d love to start this blog post with something really click-baity (“How I pwn3d Claude Code using ChatGPT Codex” or something similar to bring some interest) but, alas, it was not meant to be.

This blog post explores a bug I found one evening while trying to find a command execution primitive within Claude Code to demonstrate the risks of this new technology to a client.

At SpecterOps, we work with clients in various sectors and often with many non-standard assessment types. This particular engagement was very open scoped and the task was simple: explore the risks of allowing MCP servers to be used in our organisation.

Of course, installing a local MCP server comes with a lot of risk, even when you put aside the fact that part of the MCP spec requires local code execution by design (AI go fast!). But when working with technology being rapidly adopted by users and businesses, simply advising a client to “block all MCP servers” is a sure fire way to see how creative employees can get with working around your controls. This is why I love it when customers want to do their research up front and use metrics and evidence to back their decisions.

So, let’s go back to the beginning. The task was simple: show us the risks of MCP.

# Streaming HTTP MCP Can’t Hurt?

Hopefully, I’ve drilled the point home by now. We know that allowing employees to install MCP servers locally is no fun. To be honest, even for us as researchers, it’s pretty boring to explore. Instead, I wanted to explore something else: can an MCP server exposed remotely using HTTP as its transport lead to code execution?

We know that Claude Code is one of the most popular agentic dev tools which supports MCP as a method of including functionality; however, a remotely hosted MCP server means that as attackers, we’re limited to a few techniques of coercing Sonnet to do our evil bidding. We needed a code execution primitive we could exploit.

# An Evening With Claude Code

With the target set, I went to take a look at Claude Code’s source. I originally expected this to be open, but that wasn’t the case.

While searching, I uncovered a [blog post](https://daveschumaker.net/digging-into-the-claude-code-source-saved-by-sublime-text/) by [Dave Schumaker](https://x.com/davely) about his discovery of a source map during an early release of Claude Code which provided a nice starting point. It became obvious, however, that the current version (2.0.25 at the time) had come a long way.

Instead, I started to search for any known write-ups of vulnerabilities in Claude Code, which led to a nice [blog post](https://cymulate.com/blog/cve-2025-547954-54795-claude-inverseprompt/) from [Elad Beber](http://twitter.com/EladBeber) on the identification of [CVE-2025-54795](https://nvd.nist.gov/vuln/detail/CVE-2025-54795). Again, this is a fantastic writeup of a code exec vulnerability and an example of the protections used to avoid people running around prompt injecting Claude with commands [willy-nilly](https://www.merriam-webster.com/dictionary/willy-nilly). But after throwing a few commands at Claude and comparing the responses to Elad’s analysis, it was clear that a lot had changed.

So I bit the bullet, threw on [Lofi Girl](https://www.youtube.com/channel/UCSJ4gkVC6NrvII8umztf0Ow), and started again. Installing the latest version (2.0.25), there was a single file of cli.js which was heavily obfuscated. Using [WebCrack](https://github.com/j4k0xb/webcrack) slimmed it down, but it was still heavily mangled.

Usually, when dealing with any kind of obfuscated code, I prefer a hybrid approach of static and dynamic analysis. I attempted to launch cli.js with the debugger attached:

```
node --inspect cli.js
```

This kicked off Node, but then the process quickly exited. This time, I flipped over to adding an initial breakpoint on execution:

```
node --inspect-brk cli.js
```

Attaching DevTools, I took a look to see what was happening. Immediately, I saw this:

![](https://assets.xpnsec.com/an-evening-with-claude-code/image1.png)

This check was obviously trying to identify debug flags and, tracing a bit further, I found the reason for the process exiting:

![](https://assets.xpnsec.com/an-evening-with-claude-code/image2.png)

If you ever needed a sign that something good lies beyond, this was it! An attempt to avoid debugging Claude Code was a flag that Anthropic thought there was something worth protecting.

To evade this, you can simply put the following into the DevTools console before resuming execution:

```
process.execArgs = []
```

# Searching for Regex

Dealing with an obfuscated codebase prevents methodically stepping through each area of code, so instead I often look for general indicators of functionality that I want to target.

Looking through the JavaScript, something immediately stood out:

![](https://assets.xpnsec.com/an-evening-with-claude-code/image3.png)

This regex matches the observation from Elad in his blog post. Could it be this easy: just analyze this regex for fixes and find another hole?

Immediately, I tested a few commands in Claude Code which matched the regex:

![](https://assets.xpnsec.com/an-evening-with-claude-code/image4.png)

This felt like a good start, so my tactic became:

1. Find a command permitted within the identified regex
2. Find an argument to the command which fits within the regex but permits code execution

For the purpose of review, let’s tidy things up a bit so you can see what I was dealing with:

```
/^echo(?:\s+(?:'[^']*'|"[^"$<>\n\r]*"|[^|;&`$(){}><#\\!"'\s]+))*(?:\s+2>&1)?\s*$/
/^claude -h$/
/^claude --help$/
/^git status(?:\s|$)[^<>()$`|{}&;\n\r]*$/
/^git blame(?:\s|$)[^<>()$`|{}&;\n\r]*$/
/^git ls-files(?:\s|$)[^<>()$`|{}&;\n\r]*$/
/^git config --get[^<>()$`|{}&;\n\r]*$/
/^git remote -v$/
/^git remote show\s+[a-zA-Z0-9_-]+$/
/^git tag$/
/^git tag -l[^<>()$`|{}&;\n\r]*$/
/^git branch$/
/^git branch (?:-v|-vv|--verbose)$/
/^git branch (?:-a|--all)$/
/^git branch (?:-r|--remotes)$/
/^git branch (?:-l|--list)(?:\s+".*"|'[^']*')?$/
/^git branch (?:--color|--no-color|--column|--no-column)$/
/^git branch --sort=\S+$/ /^git branch --show-current$/
/^git branch (?:--contains|--no-contains)\s+\S+$/
/^git branch (?:--merged|--no-merged)(?:\s+\S+)?$/
/^uniq(?:\s+(?:-[a-zA-Z]+|--[a-zA-Z-]+(?:=\S+)?|-[fsw]\s+\d+))*(?:\s|$)\s*$/
/^pwd$/
/^whoami$/
/^ps(?:\s|$)(?!.*-o)(?!.*-O)[^<>()$`|{}&;\n\r]*$/
/^node -v$/ /^npm -v$/
/^python --version$/
/^python3 --version$/
/^tree$/
/^history(?:\s+\d+)?\s*$/
/^alias$/
/^arch(?:\s+(?:--help|-h))?\s*$/
/^ip addr$/
/^ifconfig(?:\s+[a-zA-Z][a-zA-Z0-9_-]*)?\s*$/ /^jq(?!\s+.*(?:-f\b|--from-file|--rawfile|--slurpfile|--run-tests|-L\b|--library-path))(?:\s+(?:-[a-zA-Z]+|--[a-zA-Z-]+(?:=\S+)?))*(?: +(?:'[^'`]*'|"[^"`]*"|[^-\s][^\s]*))?\s*$/ /^cd(?:\s+(?:'[^']*'|"[^"]*"|[^\s;|&`$(){}><#\\]+))?$/ /^ls(?:\s+[^<>()$`|{}&;\n\r]*)?$/ /^find(?:\s+(?:(?!-delete\b|-exec\b|-execdir\b|-ok\b|-okdir\b|-fprint0?\b|-fls\b|-fprintf\b)[^<>()$`|{}&;\n\r\s]|\\[()]|\s)+)?$/]);
```

Thankfully, looking at the list, there were plenty of options that would lead to code execution. If we take `git branch`, we could just go with something trivial like:

``...