---
title: From image Upload to Workspace Takeover: Deconstructing a Critical Stored XSS Attack
url: https://infosecwriteups.com/from-image-upload-to-workspace-takeover-deconstructing-a-critical-stored-xss-attack-55d821c73b72?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-06
fetch_date: 2025-10-02T19:44:20.016602
---

# From image Upload to Workspace Takeover: Deconstructing a Critical Stored XSS Attack

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F55d821c73b72&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-image-upload-to-workspace-takeover-deconstructing-a-critical-stored-xss-attack-55d821c73b72&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-image-upload-to-workspace-takeover-deconstructing-a-critical-stored-xss-attack-55d821c73b72&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-55d821c73b72---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-55d821c73b72---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From image Upload to Workspace Takeover: Deconstructing a Critical Stored XSS Attack

[![Abhishek meena](https://miro.medium.com/v2/resize:fill:64:64/1*g4tYjgpvB52xwZPNMcvefg.png)](https://medium.com/%40Aacle?source=post_page---byline--55d821c73b72---------------------------------------)

[Abhishek meena](https://medium.com/%40Aacle?source=post_page---byline--55d821c73b72---------------------------------------)

4 min read

·

Sep 1, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

This “Image” Hacked a Company Workspace

A seemingly harmless feature — file uploading — became the entry point for a complete workspace takeover in a recent vulnerability found in the Dust platform. This case serves as a critical reminder of how a classic Stored Cross-Site Scripting (XSS) flaw, when combined with architectural oversights, can lead to devastating consequences, including privilege escalation and full administrative control.

## The Attack Chain Unraveled ⛓️

The attack’s brilliance lay in its simplicity and ability to chain together several seemingly minor flaws into a high-impact exploit. It didn’t require complex code or password theft; it only needed one user to click one link.

Press enter or click to view image in full size

![]()

The Attack Chain: From One Click to Total Compromise

Here’s a step-by-step breakdown of how it worked:

1. **Disguised Malicious File Upload**: The attacker, logged in as a low-privilege member, uploaded a file named something innocuous like `xss_poc.png`. However, they manipulated the request to set the file's
2. `Content-Type` to `text/html`. The system's validation checks failed to catch this mismatch, prioritizing the declared content type over the file extension.
3. **Same-Origin Hosting**: The uploaded HTML file was hosted on the main application domain (`dust.tt`). This was the pivotal mistake. By serving user-generated content from the same origin as the core application, the platform allowed any script within that file to operate within the application's trusted security context.
4. **The Bait**: The attacker shared the direct URL to the uploaded file with a workspace administrator. To the admin, it appeared to be just another link to an image file shared by a colleague.
5. **Silent Execution**: When the administrator visited the link, their browser didn’t render an image. Instead, it correctly interpreted the
6. `text/html` content type and executed the JavaScript embedded in the file. Because this script ran on the
7. `dust.tt` domain, it automatically inherited the administrator's authenticated session.
8. **API-driven Takeover**: The JavaScript payload was designed to silently make API calls on the administrator’s behalf. It first fetched the workspace ID and then sent a
9. `POST` request to the API endpoint responsible for managing members. This request promoted the attacker's own account to an "admin" role. The action was performed seamlessly in the background, using the victim's active session, with no indication that a compromise had occurred.

## The Widespread Impact 💥

Once the attacker gained admin privileges, it was game over for the workspace’s security. They could:

![]()

Your Browser, Their Commands

* **Escalate Privileges**: Promote their own account to the highest level.
* **Revoke Access**: Downgrade or remove the legitimate administrators, locking them out of their own workspace.
* **Access Sensitive Data**: View and delete private secrets and internal data accessible only to administrators.
* **Achieve Full Compromise**: Take complete control over the workspace, its members, and all its data.

The attack didn’t require stealing the victim’s session cookie; it leveraged the active session directly, making it highly efficient and difficult to detect through traditional means.

## Key Security Lessons and Mitigation Strategies

This incident underscores several fundamental principles for securing modern web applications, especially those handling user-generated content.

### 1. Sandbox User Content on a Separate Domain

The most effective countermeasure is to **serve all user-uploaded files from a separate, cookie-less domain**. For example, if your application runs on `app.com`, user content should be served from a sandboxed domain like `app-usercontent.com`. This isolates the content, ensuring that even if a malicious script executes, it cannot access the main application's cookies or make authenticated API calls.

### 2. Enforce `Content-Disposition: attachment`

To prevent browsers from rendering files inline, always send the `Content-Disposition: attachment; filename="..."` header. This forces the browser to trigger a download prompt instead of trying to display the content, neutralizing XSS vectors embedded in files like HTML or SVG.

### 3. Validate Files by Content, Not Metadata

Never trust user-provided metadata like filenames or `Content-Type` headers. Implement **server-side validation** that inspects a file's actual contents (e.g., using magic bytes) to determine its true type. A file ending in `.png` should contain a valid PNG data structure, not HTML tags.

### 4. Implement a Strict Content-Security-Policy (CSP)

A well-configured CSP acts as a vital layer of defense. It can be used to block inline scripts (`script-src 'self'`) and restrict where resources can be loaded from, significantly reducing the attack surface for XSS even if a malicious file is uploaded and rendered.

This case is a powerful illustration of why security must be approached in layers. A single point of failure — in this case, trusting and rendering a user-uploaded file in the same security context as the application — can unravel an entire system’s defenses.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----55d821c73b72---------------------------------------)

[Infosec](https://medium.com/ta...