---
title: WRAITH – Browser Hooking and Blind XSS Page Mirroring
url: https://www.darknet.org.uk/2026/09/wraith-browser-hooking-and-blind-xss-page-mirroring/
source: Over Security
date: 2026-09-07
fetch_date: 2026-09-08T06:42:22.932664
---

# WRAITH – Browser Hooking and Blind XSS Page Mirroring

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / WRAITH – Browser Hooking and Blind XSS Page Mirroring

# WRAITH – Browser Hooking and Blind XSS Page Mirroring

Published September 7, 2026 |

Views: 121

WRAITH is a browser-hooking framework that combines a BeEF-style command channel with the evidence collection normally associated with tools such as [xsshunter-express](https://www.darknet.org.uk/2025/08/xsshunter-express-self-hosted-blind-xss-payload-capture-and-analysis/). A JavaScript hook calls home over WebSocket, appears in an operator console and can receive capture, social-engineering and local-reconnaissance modules.

![WRAITH browser hook and Page Mirror concept](https://www.darknet.org.uk/wp-content/uploads/2026/09/wraith-browser-hooking-blind-xss-page-mirror-640x360.webp)

The public repository appeared on 1 August 2026. Its three commits all landed that day: the initial code release, a metadata correction and a documentation update. The package declares version 1.0.0, but there is no GitHub release and the project describes itself as work in progress.

Advertisement

Darknet first covered [BeEF in October 2006](https://www.darknet.org.uk/2006/10/beef-browser-exploitation-framework/), when its modular console and list of controlled browsers were the story. BeEF still uses a hooked browser as a beachhead for command modules. WRAITH keeps that model, adds the one-shot evidence expected from blind-XSS tooling, then tries to make the captured page navigable.

The hook itself is small enough to follow. It derives its callback address from the script URL, connects to the public `/ws/hook` endpoint and sends a browser fingerprint. The operator can deploy JavaScript modules to that live browser; completed results return over the same channel and are persisted by the server.

Page Capture fires automatically by default. It records the origin, URL and referrer, reads JavaScript-visible cookies, serialises the DOM and attempts a screenshot. The implementation labels the two important failures instead of hiding them: HttpOnly cookies are unavailable to JavaScript, while Content Security Policy or cross-origin images can prevent a useful screenshot.

Page Mirror takes a different route. When the operator follows a link, the command is relayed to the hooked browser. That browser calls `fetch()` with credentials included, reads the response and sends the returned HTML back to WRAITH. The request therefore carries cookies that JavaScript cannot read directly, including an HttpOnly session cookie, because the browser attaches them to an eligible same-origin request.

HttpOnly still does its job: the cookie value is not exposed to the hook. It does not prevent code already executing in the origin from asking the browser to make an authenticated request. WRAITH makes that distinction visible in its practice lab, where the captured cookie list is empty but a mirrored request can still reach a session-gated page.

The operator is not remotely driving the victim’s original tab. WRAITH removes scripts from the returned HTML, inserts a base URL, intercepts link clicks and blocks form submissions inside a sandboxed frame. Each selected link becomes another credentialed GET request through the hooked browser.

Advertisement

A server-rendered application with useful links can become a navigable evidence set. A client-heavy application whose interface depends on JavaScript will not replay faithfully, and a workflow that requires a form submission is deliberately stopped. Calling it a mirror is fair; treating it as a complete remote-browser session is not.

For a red-team engagement, the useful sequence starts after authorised JavaScript execution has already been achieved. Page Capture establishes where a blind payload fired. Page Mirror can then inspect same-origin pages available to that browser session without first extracting the session token. Cross-origin reads remain subject to the browser’s Same-Origin Policy.

## What was tested

I cloned the current `main` branch, installed the locked Node dependencies and started WRAITH on loopback. The operator console, demo page, practice lab and hook script each returned HTTP 200. All twelve JavaScript files passed Node’s syntax checker.

The public-bind safeguard also behaved as documented. Starting the server on `0.0.0.0` without an operator password exited with status 1 and refused to expose the console. I did not connect a second browser, deploy an overlay or exercise Page Mirror against anything outside the bundled local lab.

Maturity note

WRAITH has one contributor and no test command in `package.json`. The repository had 137 stars and 12 forks when reviewed on 1 September 2026, but those counts do not establish operational use. Its code has not changed since the initial public commit.

## Installation

The documented Docker route requires Node.js 18 or later, Docker and Docker Compose. The repository’s setup sequence is:

git clone https://github.com/Arcanum-Sec/wraith
cd wraith
./setup.sh

|  |  |
| --- | --- |
| 1  2  3 | git clone https://github.com/Arcanum-Sec/wraith  cd wraith  ./setup.sh |

`setup.sh` asks for the public address and operator credentials, generates a session-signing secret, writes a protected `.env` file and starts the container. A local development route is also documented with `npm install` followed by `npm start`.

The service refuses a public bind without an operator password, but the hook endpoint must remain reachable by design. A real deployment therefore needs more than a password: the project’s deployment guide recommends TLS, a per-cohort credential and removing the service between exercises.

## The server becomes part of the evidence boundary

WRAITH persists captured credentials, DOM content, scan results and mirrored page HTML under `data/sessions.json`. It keeps as many as sixty mirrored pages per session and caps stored HTML at two megabytes per page. Hiding a session in the console does not delete it; the operator has a separate permanent-forget action.

That makes the WRAITH host sensitive even in an authorised exercise. The data directory can contain the same application content and credentials the engagement was intended to demonstrate. Retention, access control and teardown belong in the test plan before the first payload is delivered, not after the console has collected evidence.

## WRAITH is not a BeEF replacement yet

BeEF has accumulated thousands of commits, an extension system and a large catalogue of command modules. WRAITH currently ships a much smaller set: three login overlays, page capture and a browser-based port scanner alongside the mirror. The comparison is useful because it shows the design lineage; it does not establish feature parity.

Blind-XSS tooling usually proves that a payload executed and returns a snapshot. A classic browser hook supplies an interactive command channel. WRAITH joins those stage...