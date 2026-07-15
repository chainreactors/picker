---
title: Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads
url: https://thehackernews.com/2026/07/claude-for-chrome-flaw-lets-other.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:49:59.228801
---

# Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads](https://thehackernews.com/2026/07/claude-for-chrome-flaw-lets-other.html)

**Swati Khandelwal**Jul 14, 2026Browser Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6dKqmptCkoLw0bB5PV9wa9zqqfMmsIU0yrc4vQ2FdIFYClQBeZyUifVSr4wny1umoGovVKP57bzeh3-8RjmK8VktgN_y8TGTnkkw6Ua49L3xfWT_n8Ks6ob2NpIy78NSAV4-XU7HxfdmYqAZcKYz7DIjihqBI8OsQIgW3a4vca7taNTohCTDrqEamAk4/s1700-e365/claude-chrome-flaw.jpg)

Any other browser extension that can run a script on claude.ai can still trigger Claude for Chrome tasks aimed at your Gmail, your latest Google Doc and its comments, and your Calendar.

Both this and ClaudeBleed need a rogue extension that can already run a script on claude.ai; the difference is scope. Anthropic restricted the arbitrary-prompt path in May as part of its response to the [ClaudeBleed](https://web.archive.org/web/20260508132614/https%3A//layerxsecurity.com/blog/a-flaw-in-claudes-browser-extension-allows-any-extension-to-hijack-it/) flaw, boxing external callers into a fixed set of tasks, but [Manifold Security](https://www.manifold.security/blog/claude-for-chrome-extension-bypass) says the gap is still open in v1.0.80, the current release, eight versions later.

If you run Claude for Chrome and any other extension that can touch claude.ai, you are in scope. In the default "ask before acting" mode, the forged task still hits an approval box you have to click.

If you switched on "Act without asking," the hands-off automation mode, it runs with no prompt at all. The quickest guard is to turn "Act without asking" off and review any extension with permission to read or change data on claude.ai. That restores the approval step but does not remove the forged-click path, and there is no patch as of July 14.

The Hacker News unpacked the current build and confirmed both mechanisms remain in v1.0.80.

## The trigger accepts a forged click

After **ClaudeBleed**, Anthropic stopped letting the page hand Claude any text it wanted and boxed external callers into nine fixed task IDs baked into the extension bundle.

Three are onboarding practice prompts, three drive DoorDash, Salesforce, and Zillow, and the last three, `usecase-gmail`, `usecase-gdocs`, and `usecase-calendar`, are the ones that read your mail, your latest doc and its comments, and your calendar. The allowlist is a real improvement. The page can no longer put words in Claude's mouth.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The weak point is what pulls the trigger. A content script in the extension listens on claude.ai for a click on a specific element (`#claude-onboarding-button`), reads its `data-task-id`, and if the ID is one of the nine allowlisted tasks, sends the extension an `open_side_panel` message carrying it. The panel opens with the matching prompt loaded. What the handler never checks is `event.isTrusted`, the browser flag that tells a real user click from one a script dispatched.

So any extension whose content script can reach the DOM on claude.ai can build the element, set the task ID, and dispatch a synthetic click. The extension treats it as a genuine tap. Manifold demonstrated the trigger with six lines pasted into the claude.ai console, with `isTrusted: false` in the logs confirming the fake click was honored.

With browser control on, the default once onboarding finishes, that forged click loads the `usecase-gmail` task into the panel. In default mode, an approval box still stands between that and any actual read, and the user has to click it. Manifold rates the flaw CVSS 7.7 High in that mode, and 9.6 Critical once a user has enabled "Act without asking," where the same task runs silently.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn9WgNIZf1jJyX-D_OfPMOOFeVMfvTcBe7k4gz4dA5D4ExKKC51_uMJ_5Gf4AHaWWEib5BVozAU-98s0KR5oimWy6Qi8DW60xHhT2MWibBdANAIE9CAAyvqOA_bZSsW5sx1gCNtPkeeo0oPtqU1SystZzH-i_wcGD3HNlbirjG9c4ZfdqHsUkIa6o-IWg/s1700-e365/claude-ch.jpg)

The one-line fix, the researchers say, rejects synthetic clicks at the top of the handler. It has not shipped.

## A quieter flaw sits underneath

The second issue is not remotely reachable today, but it is what removes the approval step if another flaw ever exposes it. When Claude's side panel loads with `?skipPermissions=true` in its URL, it boots straight into `skip_all_permission_checks` and starts acting without asking.

No gesture, no consent screen. A red banner warning that Claude can now take most actions online does appear, but only after the privileged session is already running. The banner tells you what happened. It does not stop it from happening.

For now, that URL can only be built by the extension itself, so there is no direct remote path. A future bug that lets a lower-privileged context set that parameter could turn the forged-click trick into a fully silent account read. That path could be exposed by a URL-accepting message handler, a panel-building regression, or an XSS flaw in the options page. Manifold's fix is to stop reading permission mode from the URL and boot the panel in ask mode every time.

Manifold maps the working attack to the OWASP Top 10 for LLM apps as indirect prompt injection, since the attacker triggers one of the extension's nine allowlisted prompts with a forged click, and the silent-execution risk to excessive agency. Both reproduce whether the side panel is set to Opus, Sonnet, or Fable. The bug is in the extension, not the model.

## Reported in May, still in the shipping code

Manifold reported both issues on May 21 against v1.0.72. Anthropic acknowledged them the next day, then closed both. It shut the forged-click report on the grounds that the underlying trust-boundary problem was already tracked under the earlier ClaudeBleed report, which [Anthropic said](https://www.manifold.security/bl...