---
title: NASA AIT-GUI Flaws Could Let Unauthenticated Attackers Issue Spacecraft Commands
url: https://thehackernews.com/2026/08/nasa-ait-gui-flaws-could-let.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:09.949119
---

# NASA AIT-GUI Flaws Could Let Unauthenticated Attackers Issue Spacecraft Commands

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [NASA AIT-GUI Flaws Could Let Unauthenticated Attackers Issue Spacecraft Commands](https://thehackernews.com/2026/08/nasa-ait-gui-flaws-could-let.html)

**Swati Khandelwal**Aug 20, 2026Vulnerability / Critical Infrastructure

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0aHi13XpphD98KUUKTJJB0T5eJW8TLe8qecYWanC8lqujxWOn4dtJUXThwqpfnrd9daSkiLMxXb7r6EFFbYY2fy3qSZteMtPB5Sl5t4K01MKoHywiyohPzUQX17h3oj126zywGtTEP8twGQnbs0wjaecaY8nLhAWXLw0anuJuL2iSJmKBVnzlZhy842E/s1700-e365/nasa.jpg)

Security researchers at Cycode have disclosed a chain of flaws in AIT-GUI, the browser-based operator console for NASA/JPL's open-source AMMOS Instrument Toolkit, that allow an unauthenticated attacker to issue arbitrary commands to the software's spacecraft and instrument command bus.

The chain, tracked as **GHSA-p9r8-2q67-fp86** and rated 9.4 on the CVSS v3.1 scoring system, impacts AIT-GUI versions 2.5.1 and earlier, with the advisory listing version 2.5.2 as the fixed release. The advisory, published August 13, 2026, states that no CVE has been assigned to it.

The AMMOS Instrument Toolkit is a framework for building ground data systems, the software that sends commands to instruments and spacecraft and processes the telemetry coming back down. AIT-GUI is its operator console, and the endpoints in question relay operator commands to a command bus.

"The blast radius of an unauthenticated POST is measured in issued instrument commands, not defaced pages," Cycode said in the [writeup](https://cycode.com/blog/ait-gui-unauthenticated-command-execution/).

According to the advisory, the AIT-GUI web server reads its configured host value and then discards it, binding the listener to the hardcoded address 0.0.0.0 on port 8080 by default, and exposes the command, script, and sequence routes without credential-based authentication or authorization and without cross-site request forgery (CSRF) protection. Cycode clarified that the routes are gated by a session cookie, but a session can be obtained without credentials by requesting the root page.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Two of those routes also build filesystem paths from unvalidated input. The issues are classified as CWE-306, CWE-352, and CWE-22.

The advisory said an unauthenticated party who can reach the port can do the following -

* Issue arbitrary instrument and spacecraft commands via POST /cmd
* Execute server-side scripts via POST /script/run, including files outside the intended directory via path traversal
* Run command sequences via POST /seq, including out-of-directory files passed to a subprocess

Cycode clarified that a command cannot be sent with a single anonymous request. A request to `POST /cmd` without a valid session cookie returns HTTP 401, but `GET /` calls `Sessions.create()` and returns a `sid` cookie without requiring credentials. Repeating the command request with that cookie passes the session check and sends the command.

"A web GUI used to drive spacecraft and instrument commanding shipped a server that listens on every network interface, asks nobody for a password, and can be steered by any web page an operator happens to open," Yuval Elbar, a security researcher at Cycode, said.

Cycode said its proof-of-concept for the cross-origin portion of the chain was run on localhost. Because the routes accept application/x-www-form-urlencoded bodies, which browsers treat as CORS "simple" requests, the test showed that a cross-origin POST can be delivered without a preflight and processed by the server. Cycode said the same conditions can hold against a network-reachable instance, but the remote path was not independently exploited as part of its work.

"Captured network traffic from a real browser confirms the cross-origin POST is delivered with zero OPTIONS preflight requests, and the server processes it," the advisory said.

AIT-GUI 2.5.2 was [released](https://github.com/NASA-AMMOS/AIT-GUI/releases/tag/2.5.2) on August 12, 2026. It binds the configured host, defaulting to localhost, adds a before\_request hook that compares a request's Origin or Referer against the server's own Host for POST, PUT, DELETE, and PATCH, and confines /script/run and /seq to their configured roots.

"State-changing endpoints (POST/PUT/DELETE/PATCH) now reject cross-origin browser requests via a same-origin (Origin/Referer vs Host) check, mitigating CSRF. Non-browser clients that send neither header are unaffected," the project said in the [changelog](https://github.com/NASA-AMMOS/AIT-GUI/blob/2.5.2/CHANGELOG.md) for version 2.5.2.

After reviewing the advisory, The Hacker News examined the tagged source for versions 2.4.1, 2.5.1, and 2.5.2 in the project's repository. In 2.5.2, the root route still calls Sessions.create() and issues a session cookie to any request without a credential check, and the command route accepts any request carrying that cookie.

THN confirmed against the tagged 2.5.2 source on August 20, 2026, that the release restricts where the console listens and blocks browser-driven cross-origin requests, and does not add authentication to the command, script, or sequence endpoints. Cycode told The Hacker News that it therefore does not consider the chain fully remediated in 2.5.2, saying the release addresses the remote exposure and cross-site delivery paths but leaves the missing-authentication weakness intact.

We also confirmed via [PyPI](https://pypi.org/project/ait-gui/) on August 20, 2026, that the latest published release of the ait-gui package is 2.4.1, uploaded on July 27, 2023, and that versions 2.5.0, 2.5.1, and 2.5.2 do not appear in the release history. The 2.4.1 source carries the same hardcoded 0.0.0.0 bind and the same unconfined path construction on both routes, and PyPI lists no vulnerabilities for it. The advisory identifies the affected package ecosystem as pip.

Separately, a second record covers the same missing-authenticatio...