---
title: AI-Native SARIF
url: https://parsiya.net/blog/ai-native-sarif/
source: Hackerman's Hacking Tutorials
date: 2025-12-12
fetch_date: 2025-12-13T03:14:33.652960
---

# AI-Native SARIF

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Dec 11, 2025
- 9 minute read - [AI](https://parsiya.net/categories/ai/) [Static Analysis](https://parsiya.net/categories/static-analysis/)

# AI-Native SARIF

* [Abstract](#abstract)
  + [What is SARIF?](#what-is-sarif)
* [What Should I Add to the SARIF File?](#what-should-i-add-to-the-sarif-file)
  + [Rule Context](#rule-context)
  + [Code Context](#code-context)
  + [The Feedback Loop](#the-feedback-loop)
* [Where Does the ~~Soda~~ Data Go?](#where-does-the-soda-data-go)
  + [Rule Context](#rule-context-1)
  + [Code Context](#code-context-1)
* [When Do I Modify the SARIF File?](#when-do-i-modify-the-sarif-file)
* [Where Does the Data Come From?](#where-does-the-data-come-from)
* [What Did We Learn Here Today?](#what-did-we-learn-here-today)

The "radical" idea to add prompts and code context directly into SARIF files for
AI triage.

Write the clickbait title and then immediately give away the whole thing in the
preview. Pick a struggle, gurrl!

Special thanks to [Krishna](https://www.linkedin.com/in/krishnachaitanyatelikicherla/) from Microsoft and [Lewis](https://www.linkedin.com/in/theoriginalenglishbreakfast/)
from Semgrep for reviewing the post and giving me feedback.

# Abstract

In
[WTF is ... - AI-Native SAST](/blog/wtf-is-ai-native-sast/ "WTF is ... - AI-Native SAST")
I proposed four phases of AI-Native SAST in increasing complexity:

1. Prompt + Code
2. Prompt + Agent
3. Tailored Prompt + SAST Result
4. Agent + Code Graph + SAST MCP

The last two methods work on the results of SAST tooling. AI needs code, static
analysis results, tailored prompt, and context to be effective. Keeping track of
these and mashing them all together is an added layer of unnecessary headache.
In this blog I will explore how a SARIF file can act as the single source of
truth for AI triage.

## What is SARIF?

SARIF is [Static Analysis Results Interchange Format](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html). It's a format
for storing static analysis results, oh wait, the name actually tells us what it
does. It's a JSON file with a specific schema. Your static analysis tool should
be able to output the results in this format, if not, call your vendor!

I am not going to propose modifying the SARIF format. Run-on blogs are more my
thing than corporate whitepapers. So I will try to find opportunities without
breaking the current specification.

# What Should I Add to the SARIF File?

While I want this blog to concentrate on the *how* rather than the *what*, I
will still expand a little on the
[Tailored Prompt + SAST Result section](/blog/wtf-is-ai-native-sast/#tailored-prompt--sast-result "Tailored Prompt + SAST Result section")
section of the previous blog. I propose AI triage needs this info in the SARIF
file:

1. Rule context. Generated for each static analysis rule.
   1. Tailored prompt.
   2. Good and bad usage/code.
2. Code context. Generated for each individual finding.
   1. Code snippet.
   2. Code metadata.

Let's use a hypothetical static analysis rule for SSRF in C#. Usually, I start
by looking for `HttpClient.GetAsync` and then figure out if the input can be
influenced by users. Here's a [Semgrep rule for it](https://github.com/semgrep/semgrep-rules/blob/develop/csharp/lang/security/ssrf/http-client.yaml).

And I know many of you will just fixate on the contents so I will preemptively
state this is just an example and your bike-shedding will fall on deaf ears.
Save it for the promotion committee.

## Rule Context

This is the context that explains the rule and helps AI triage the result
correctly.

For our SSRF example, *the tailored prompt* explains what SSRF is, how
`HttpClient.GetAsync` works, and why it might be vulnerable to SSRF if user
input can influence the URI.

*Good and bad code patterns* can be liberated from your SAST tests. Show AI
examples of true and false positives.

![You do know you're using this meme format incorrectly, right?](02.webp "You do know you're using this meme format incorrectly, right?")
You do know you're using this meme format incorrectly, right?

## Code Context

*Code context* is based on the matched code and generated independently of the
rules.

Should the actual code be in the file? "Don't put the code in the file, Parsia!"
said my manager. But the results of static analysis ARE also sensitive info.
More importantly, they are a direct result of static analysis so access to the
files likely includes access to code anyway.

But OK, be careful putting sensitive info in the magic file. Alas, yet another
piece of red tape holding civilization back!

![Contrary to popular belief I actually value feedback (don't tell them).](01.webp "Contrary to popular belief I actually value feedback (don't tell them).")
Contrary to popular belief I actually value feedback (don't tell them).

*Code metadata* is the extra information about the matched code and its
surrounding context. You should use a combination of static analysis and AI
here. For example, static analysis identifies all API routes based on
decorators/keywords and AI summarizes them.

At a minimum, I need the AI generated description of the surrounding function
block[1](#fn:1). I could also include more context about the code's functionality
(for example, this is an API route that retrieves user's info from another
microservice).

## The Feedback Loop

You should refine the aforementioned data as time goes by. While it is tempting
to add the false positives to per-rule context, your first line of defense is
tweaking your SAST rule to filter these out. That is not always possible so
some false positives will eventually end up in the context.

A function that was misidentified as an API route should refine the system
(prompt + SAST as we discussed above) that generates the *code metadata*. It
will most likely work result in a modified prompt.

But enough about the data, I want to focus on the actual format here.

# Where Does the ~~Soda~~ Data Go?[2](#fn:2)

I needed to analyze the SARIF structure to find suitable locations for this
info. I've written a good chunk of code for processing SARIF output in
[Go](https://github.com/parsiya/semgrep_go) and [Rust](https://github.com/parsiya/semgrep-rs) and even did some
[fun Semgrep experiments](/blog/semgrep-fun/ "fun Semgrep experiments").
This was a chance to look at other parts of the format.

## Rule Context

The `runs > tool > rules` section is perfect for the rule context. It has a list
of all rules executed by the tool. According to section
[3.19.23 rules property](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html#_Toc141790806) of the specification, it can have one or
more [reportingDescriptors](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html#_Toc141791086).

I will be using an example from running
[Marco Ivaldi's (0xdea) Semgrep rules](https://github.com/0xdea/semgrep-rules) against OWASP Juice Shop.
I've removed some parts to make things easier to read. I will look at the
[c.command-injection rule](https://github.com/0xdea/semgrep-rules/blob/main/rules/c/command-injection.yaml).

```
{
  "runs": [
    {
      "tool": {
        "driver": {
          "rules...