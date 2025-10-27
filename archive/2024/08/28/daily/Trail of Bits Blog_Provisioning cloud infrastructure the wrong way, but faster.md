---
title: Provisioning cloud infrastructure the wrong way, but faster
url: https://blog.trailofbits.com/2024/08/27/provisioning-cloud-infrastructure-the-wrong-way-but-faster/
source: Trail of Bits Blog
date: 2024-08-28
fetch_date: 2025-10-06T18:04:04.941621
---

# Provisioning cloud infrastructure the wrong way, but faster

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Provisioning cloud infrastructure the wrong way, but faster

Artem Dinaburg

August 27, 2024

[machine-learning](/categories/machine-learning/), [research-practice](/categories/research-practice/)

Today we’re going to provision some cloud infrastructure the Max Power way: by combining automation with unchecked AI output. Unfortunately, this method produces cloud infrastructure code that 1) works and 2) has terrible security properties.

In a nutshell, AI-based tools like Claude and ChatGPT readily provide extremely bad cloud infrastructure provisioning code, like code that uses common hard-coded passwords. These tools also happily suggest “random” passwords for you to use, which by the nature of LLM-generated output are not random at all. Even if you try to be clever and ask these tools to provide password generation code, that code is fraught with serious security flaws.

To state the obvious, do not blindly trust AI tool output. Cloud providers should work to identify the bad patterns (and hard-coded credentials) suggested in this blog post, and work to block them at the infrastructure layer (like they do when committing an API key to GitHub). LLM vendors should consider making it a bit more difficult to generate cloud infrastructure code with glaring security problems.

![](/img/wpdump/e9562628d483a3571dead992d1b754fa.png)

<https://www.youtube.com/watch?v=7P0JM3h7IQk>
**Homer:** There’s three ways to do things: the right way, the wrong way, and the Max Power way.
**Bart:** Isn’t that the wrong way?
**Homer:** Yes, but faster!

### Let’s create a Windows VM

Pretend you are new to cloud development. You want to make a Windows VM with Terraform on Microsoft Azure, and RDP into the machine. (We will use Azure as a motivating example only because it’s the provider I’ve needed to work with, but the fundamental issues generalize to all cloud providers).

Let’s ask ChatGPT 4o and Claude what we should do.

Here’s what ChatGPT said:

![](/img/wpdump/e8fb5532e149bcefcc389eed9efa682a.png)
…
![](/img/wpdump/277d2093ac25ca8da430a79a9a43cbf9.png)
…
![](/img/wpdump/e62155c88f9d3580a41eb94828d735b3.png)

Let’s also ask Claude Sonnet:

![](/img/wpdump/d09286bc7987ebce30041fcefd45e4dc.png)
![](/img/wpdump/bac422385fc2cc3fa690cf8d32c1d3b5.png)

At least Claude reminds you to change `admin_password`.

These are hard-coded credentials, and using them is bad. Yes, Claude asks you to change them, but how many people will actually do it? It should be fairly simple to craft the right prompts and extract out all (technically, nearly all) credentials that ChatGPT or Claude would output.

### Ask for better credentials

We all know hard-coded credentials are bad. What if we ask for some better ones?

We’ll start with ChatGPT:
![](/img/wpdump/e741c60356f965e7c81fa385afdd6e9c.png)

What’s wrong with this output? These are absolutely **not random**! Notice that ChatGPT is *not* using its code execution functionality; it’s just emitting some next-most-likely tokens. You should never use these “passwords” for anything; odds are someone else will get the exact same list when they ask.

Next, let’s try Claude.

![](/img/wpdump/ea3c5651e4edb9d79eaa598f044f58b7.png)

At first, it gives the proper answer. But Claude quickly gives up when asked slightly differently.

![](/img/wpdump/e506e01347412c7819e28693c6683632.png)

I don’t mean to prompt-engineer a desired answer. I had actually asked Claude first and received the bad answer prior to realizing it will sometimes do the right thing.

### How about password generation?

Maybe we can ask these tools to write code that generates passwords. Indeed, a part of the task I needed to accomplish called for creating multiple Azure AD accounts, and this seemed like a logical method. Let’s see how our AI-based tools do at auto-generation of account credentials.

Here’s ChatGPT’s solution:

![](/img/wpdump/c4516f59d80f1acf111735eea832f734.png)

![](/img/wpdump/d1044ec044f45ae136d4b7768e777fe1.png)

And here’s Claude’s solution:

![](/img/wpdump/4a85c4aa65e6aac412f186b0f176d44a.png)

![](/img/wpdump/fe73aa65bc9bb3ad7b5da433033eb301.png)

Both of these solutions are **extremely deceptive since they look correct but are horribly wrong**. They will generate “random” looking passwords, but there is a flaw: Python’s `random` module is **not a secure source of random data**. It is a pseudorandom generator seeded with the current system time. It is trivial to generate *all of the possible passwords this script could have made for the past year or more*. The passwords it provides should not be used for anything, except maybe throwaway testing. The correct thing you want is the [Python secrets module](https://docs.python.org/3/library/secrets.html).

### What can be done?

Undoubtedly, this rabbit hole goes deep. The responses here were just what I encountered in a few days of trying to automate Terraform workflows. The sad state of affairs is that people who are the least likely to understand the impact of hard-coded credentials and weak random values are also the most likely to copy-paste raw AI tool output.

Cloud providers should assume that people are already copy-pasting output from ChatGPT and Claude, and should work to block common hard-coded credentials and other poor infrastructure patterns.

LLM vendors should make it a bit more difficult for users to accidentally shoot themselves in the foot. It shouldn’t be impossible to experience this behavior, but it should definitely not be the default.

And as always, cloud infrastructure is complex; if you’re serious about enhancing the security of yours, consider having us perform an [infrastructure threat model assessment](https://www.trailofbits.com/contact/), which will identify weaknesses and potential attack paths and suggest ways to address them. There’s a lot more than hard-coded credentials and weak randomness lurking out in your large automated infrastructure deployment.

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
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.