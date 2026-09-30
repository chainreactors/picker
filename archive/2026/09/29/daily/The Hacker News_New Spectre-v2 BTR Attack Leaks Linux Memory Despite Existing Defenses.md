---
title: New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses
url: https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html
source: The Hacker News
date: 2026-09-29
fetch_date: 2026-09-30T07:42:59.104335
---

# New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses](https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html)

**Ravie Lakshmanan**Sep 29, 2026Vulnerability / Hardware Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCNHT9zDz8oOamcA5EH8a3KGAtk9R9bE_UxGY_uPThgxZJu9vX-YG1olbgiX5WBVdwDd52LpDfSyryC6GZ45tUi2bKLe_aWnbj0Ir3WQZeGYF8Vr7U7icoPn4tcuwfpOZagVfry-KG5_jzLPb-fbPiFBlv142UOgqAPpC193t6BslvCE1l1XWo2z5_mFYV/s1700-nu-rw-lo-l85-e365/linux-intel.jpg)

A group of academics from VUSec and Scuola Superiore Sant'Anna have disclosed details of a new [Spectre](https://spectreattack.com/) CPU vulnerability variant that affects Just-In-Time ([JIT](https://en.wikipedia.org/wiki/Just-in-time_compilation)) engines present in web browsers, language runtimes, and the operating system kernel, across multiple CPU vendors.

The new Spectre v2 variant has been codenamed **[Branch Target Reuse (BTR)](https://www.vusec.net/projects/btr)**.

"The key insight is that, while modern CPUs restore architectural code coherence after self-modification, they do not necessarily invalidate stale indirect branch prediction entries (i.e., branch targets)," researchers Sander Wiebing, Yuhui Zhu, Alessandro Biondi, and Cristiano Giuffrida said in an accompanying paper.

"In JIT engines, these stale targets can outlive the original code and later be reused when the code cache is repopulated, yielding a transient execute-after-free primitive. This allows attackers to hijack transient control flow to newly generated code at obsolete offsets, bypassing software hardening or reaching misaligned gadgets."

BTR was evaluated against SpiderMonkey (the JIT engine of Mozilla Firefox), GraalVM, and the Linux kernel's cBPF JIT, all of which have been found to be affected, although with "markedly different exploitability characteristics and leakage rates."

As a proof-of-concept, two end-to-end exploits have been devised against the Linux kernel that can be used to leak and recover the root password hash within minutes from a fully patched Intel system with default protections enabled.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Spectre [refers](https://thehackernews.com/2024/03/ghostrace-new-data-leak-vulnerability.html) to a class of CPU security vulnerabilities first discovered in 2017 that exploit speculative execution, a performance optimization technique that modern processors use to predict and execute instructions beforehand.

An attacker can exploit this loophole to trick a CPU into performing speculative operations that access sensitive data, and then infer that data through a cache timing side channel.

Spectre v2 is one [specific type of the Spectre attack](https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html) that abuses indirect branch prediction in modern processors to achieve the same goals. Specifically, it poisons the CPU's branch prediction mechanism to cause a victim program to execute an indirect branch, which, in turn, causes the CPU to mispredict the branch and speculatively execute attacker-controlled code or a gadget.

Although the [results of the misprediction](https://thehackernews.com/2025/01/new-slap-flop-attacks-expose-apple-m.html) are discarded, an attacker can infer what the victim's speculative execution accessed by taking advantage of the cache state changes and measuring the cache changes.

"BTR targets JIT engines and arises from the interplay between Self-Modifying Code (SMC) and indirect branch prediction," the researchers said, adding, "JIT engines do expose exploitable transient-execution opportunities induced by SMC for the first time."

The attack presumes an attacker who is able to run unprivileged code in a JIT engine and is seeking to disclose sensitive data from the host environment. The entire sequence of actions is as follows -

* The attacker lures the JIT engine into allocating a training chunk and forces the victim branch to jump to it, thereby inserting a BTB entry referencing the current entry point.
* The attacker forces a deallocation of the training chunk and an allocation of the target chunk that partially reuses the same address.
* The attacker triggers the indirect branch again, the CPU uses the now-stale branch target buffer (BTB) entry and speculatively jumps to the old training-chunk entry point.
* The end result is control-flow hijacking and secret data disclosure.

"By redirecting control flow to an architecturally invalid entry point, the attacker can bypass Spectre hardening mitigations or execute misaligned instructions, ultimately disclosing secret data," the researchers explained.

However, a key aspect BTR hinges on is that the stale BTB entry must not be invalidated or replaced after the JIT engine frees the training chunk, and the branch predictor must select the stale BTB entry for prediction.

"This is the first example of a practical in-place Spectre-v2 attack – using the very same indirect branch for both training and testing," Giuffrida told The Hacker News via email.

"Common wisdom has always been this would be hard to pull off, because traditional Spectre-v2 attacks exploit "spatial" target violations (i.e., hijack an indirect branch target into another) and doing so for a single branch seems intuitively hard (given that you can only 'spatially' go from a valid indirect branch target to another of the same branch)."

"BTR shows this assumption is incorrect once one can mount "temporal" Spectre-v2 attacks like BTR, where the indirect branch and even the target stay the same, but the "meaning" of the target (i.e., the underlying code) changes."

The new Spectre v2 variant also undermines existing mitigations for this line of attack, including those of [Training Solo](https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html) (CVE-2024-28956 and CVE-...