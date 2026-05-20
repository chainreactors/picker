---
title: The Sleeper Agent Bug: How One HTML Payload Lay Hidden for Months to Attack My Inbox ⏳
url: https://infosecwriteups.com/the-sleeper-agent-bug-how-one-html-payload-lay-hidden-for-months-to-attack-my-inbox-9d3f1e9df60e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-19
fetch_date: 2026-05-20T06:03:25.914661
---

# The Sleeper Agent Bug: How One HTML Payload Lay Hidden for Months to Attack My Inbox ⏳

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-sleeper-agent-bug-how-one-html-payload-lay-hidden-for-months-to-attack-my-inbox-9d3f1e9df60e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-sleeper-agent-bug-how-one-html-payload-lay-hidden-for-months-to-attack-my-inbox-9d3f1e9df60e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9d3f1e9df60e---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9d3f1e9df60e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# The Sleeper Agent Bug: How One HTML Payload Lay Hidden for Months to Attack My Inbox ⏳

[![LordofHeaven](https://miro.medium.com/v2/resize:fill:64:64/1*KZRV0GWTj8BUGxiz_w7oPg.png)](https://lordofheaven1234.medium.com/?source=post_page---byline--9d3f1e9df60e---------------------------------------)

[LordofHeaven](https://lordofheaven1234.medium.com/?source=post_page---byline--9d3f1e9df60e---------------------------------------)

3 min read

·

Oct 22, 2025

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9d3f1e9df60e&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-sleeper-agent-bug-how-one-html-payload-lay-hidden-for-months-to-attack-my-inbox-9d3f1e9df60e&source=---header_actions--9d3f1e9df60e---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

**A short recon story about a delayed HTML injection, a surprising phishing vector, and why every output channel deserves the same hardening as your web UI.**

When I first started poking around a site I’d signed up for long ago — let’s call it **xyz.com** — I was in bug-hunting mode. I threw common payloads into every visible input field, especially the **Name** field, because that’s one of the easiest places developers forget to sanitize properly.

My test payload was intentionally multi-purpose: a tiny template expression, an HTML anchor, and an input element — designed to probe different rendering contexts at once.

```
{{8*8}}/”><A HREF=evil.com>HELLO</A”>
{{8*8}}"><A HREF="http://evil.com">HELLO</A>
```

I hit **Save**, checked my profile page, and… nothing useful. The UI showed the name as raw/encoded text — no math evaluated, no clickable link, no input element. I logged it as negative and moved on. The payload became a ghost, quietly stored in xyz.com’s database.

## The Return of the Phantom 👻

Months later, while skimming my inbox, I saw an email from xyz.com: **“Checking your security settings.”** At first glance it seemed legit — corporate copy, brand styling, the whole nine yards. Then I froze.

Right above the sign-off, where my name should have been dynamically inserted, the exact payload I’d submitted months earlier had been rendered — HTML and all. The template expressions had been evaluated to numbers. The `<a>` tag had become a clickable link to `http://evil.com`. Even an actual HTML input field appeared inside the email.

## Get LordofHeaven’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

Seeing your own test payload show up, fully alive, in an official email from a trusted service is a mix of validation and dread. Validation because your test worked; dread because an attacker could weaponize the same oversight against many users.

Press enter or click to view image in full size

![]()

## What happened (simple breakdown)

1. I submitted a value containing HTML into the **Name** field.
2. xyz.com stored that value in its database.
3. The web UI escaped or encoded the value (so it looked safe in-browser).
4. Later, an email template interpolated the stored value into an HTML email **without proper escaping**.
5. The mail client rendered the injected HTML, producing a live link and form control — exactly what I injected.

Short version: **stored unescaped input → inserted into HTML email → rendered by mail client = stored HTML injection in email.**

## Why this is dangerous

* **Users trust official emails.** People are far likelier to click a link from a service they use than from a random site.
* **Email clients don’t enforce browser CSPs.** Many protections that exist in browsers are absent or weaker in mail clients.
* **Wide blast radius.** If that template is used for security emails or mass notifications, many users could be exposed.
* **Social engineering potential.** Attackers can craft plausible phishing content with vendor branding and context.

## Quick developer checklist — fixes that actually help

* **Escape user input when rendering HTML emails.** Encode `<`, `>`, `&`, `"`, `'` (`&lt;`, `&gt;`, `&amp;`, `&quot;`, `&#x27;`).
* **Use auto-escaping** provided by your template engine; avoid marking user data `safe`/`raw`.
* **Whitelist characters** for name-like fields (letters, digits, spaces, common punctuation).
* **Prefer plain-text** for critical security emails (password resets, MFA changes).
* **Normalize input at ingestion** as a second line of defense.
* **Test templates with malicious payloads** in CI to catch regressions.
* **Audit all output sinks**: web UI, emails, admin panels, logs, PDFs, mobile push — anything that can render user data.

## Final thoughts

A tiny, forgotten field can become a powerful attack vector when stored and later reused in a different context. Don’t assume “no visible reflection in the UI = safe.” Treat every output channel as hostile, and apply the same rigorous escaping and testing you use for front-end XSS across email templates and other async outputs.

[Web Security](https://medium.com/tag/web-security?source=post_page-----9d3f1e9df60e---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----9d3f1e9df60e---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----9d3f1e9df60e---------------------------------------)

[Html Injection](https://medium.com/tag/html-injection?source=post_page-----9d3f1e9df60e---------------------------------------)

[Coffinxp](https://medium.com/tag/coffinxp?source=post_page-----9d3f1e9df60e---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9d3f1e9df60e---------------------------------------)

[![InfoSec Write-ups](http...