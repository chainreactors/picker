---
title: What 890 security engagements actually find
url: https://appsec-labs.com/what-890-security-engagements-actually-find/
source: Blog | AppSec Labs
date: 2026-08-04
fetch_date: 2026-08-05T04:58:14.302865
---

# What 890 security engagements actually find

[Skip to content](#content)

[![AppSec Labs logo](https://appsec-labs.com/wp-content/uploads/2023/09/logo_appsec_labs-transformed1-1.png)](https://appsec-labs.com)

* [Penetration Testing Services](https://appsec-labs.com/our-services/)
  + [Web Applications](https://appsec-labs.com/web-application-penetration-testing/)+ [SaaS & Multi-Tenant](https://appsec-labs.com/saas-penetration-testing/)+ [APIs](https://appsec-labs.com/api-penetration-testing/)+ [Mobile Apps](https://appsec-labs.com/mobile-application-penetration-testing/)+ [AI & LLM](https://appsec-labs.com/ai-llm-penetration-testing/)
* [About](https://appsec-labs.com/about/)
  + [Alumni](https://appsec-labs.com/alumni/)+ [The Book](https://appsec-labs.com/managed-code-rootkits/)+ [Testimonials](https://appsec-labs.com/testimonials/)
* [Careers](https://appsec-labs.com/careers/)
* Knowledge
  + [Blog](https://appsec-labs.com/blog/)+ [Research](https://appsec-labs.com/research/)+ [Attacks & Tests](https://appsec-labs.com/attack-and-tests/)+ [Testing modes](https://appsec-labs.com/testing-modes/)
* [Contact](https://appsec-labs.com/contact_us/)
* EN
  + [עברית](https://appsec-labs.com/he/)

X

Contact us

#### Contact us

Have a question or comment? Submit your message through our contact form and a member of our team will get back to you within 24 hours.

Δ

[Application Security](https://appsec-labs.com/category/application-security/)

# What 890 security engagements actually find

August 4, 2026

[No comments yet](https://appsec-labs.com/what-890-security-engagements-actually-find/#respond)

**We have recorded 6,643 findings across 890 engagements since our platform went live.** This is what is actually in them.

Not a vendor threat report, not a survey of what people say they worry about. Our own findings, from our own engagements, counted.

## What is being counted, before any of the numbers

The window is **October 2021 to August 2026** — the engagements recorded in our own platform. Work from before that lived in a different system and is not counted here, so treat every number as a floor rather than a lifetime total.

**890 engagements, 167 client organisations, 6,643 findings.** Most of that work is penetration testing; a small remainder is design, code and architecture review. Findings run from 0 to 73 per project, with a median of 5 — and 234 projects produced none at all, which is a result too.

**83% of findings map to a named finding type**, and the rankings below describe that subset. Severities are the severity we assigned when we wrote the finding, so one a client has since fixed still counts as what it was.

## Most of what we find is not critical, and anyone who tells you otherwise is selling

| Severity | Findings | Share |
| --- | --- | --- |
| Informational | 569 | 8.6% |
| Low | 3,299 | 49.7% |
| Medium | 1,724 | 26.0% |
| High | 751 | 11.3% |
| Critical | 295 | 4.4% |

**15.7% of everything we report is high or critical. 4.4% is critical.**

I want to be blunt about what that means, because it cuts against how our industry sells. If a supplier promises a critical finding in every engagement, one of two things is true: they are testing systems that are genuinely broken, or they are inflating severity so the report looks like value for money. We would rather tell you the system held up.

But do not read that small slice as the unimportant part. **It is the entire point.** A median engagement of ours produces five findings. On these proportions, fewer than one of them is the finding that could actually hurt you — and the other four are housekeeping: real, worth fixing, and not what you hire a person for.

**The whole craft is making sure that one finding is in the report.** Everything below is about the difference between the four and the one.

## How a finding gets to you

Before any of this reaches a client, it goes through a step most reports never mention, so here is ours with the numbers attached.

**Every finding is written by one consultant and reviewed by a second.** The reviewer’s job is to be the first person who did *not* find the bug — somebody who has to be convinced by the evidence written down, rather than by having been in the room when it worked. They can approve it, or send it back.

**3,802 findings have been through that review. One in four was sent back.**

| Review outcome | Findings | Share |
| --- | --- | --- |
| Approved first pass | 2,846 | 74.9% |
| Sent back once | 761 | 20.0% |
| Sent back twice | 136 | 3.6% |
| Sent back three or more times | 57 | 1.5% |

**956 findings were returned to their author before a client ever saw them.** That is the number I would want from a supplier and the one nobody publishes, because on the surface it looks like an admission. It is the opposite: it is the only evidence that the second pair of eyes is doing anything. A firm with a 100% first-pass rate does not have a better process than us. It has a rubber stamp.

It is not a slow step — the median finding spends **one day** in review, and about **2.8 days** from written to approved. Across the window that work has been spread over 22 consultants writing and 11 reviewing.

And the severity you read is not something that gets negotiated on the way out: **98% of severities are exactly what the consultant who found the issue first assigned.**

## The findings that actually endanger a business

Now the part that matters. Take the findings we rate high or critical, and ask a second question of each: *when this appears, how often is it serious?*

| Finding | Times found | High or critical | Rate |
| --- | --- | --- | --- |
| Persistent cross-site scripting | 88 | 72 | 82% |
| Authorization bypass via IDOR | 106 | 56 | 53% |
| Reflected cross-site scripting | 60 | 50 | 83% |
| Bypassing authorization schema (vertical) | 82 | 49 | 60% |
| Bypassing authorization schema (horizontal) | 59 | 42 | 71% |
| Brute force on login panel | 50 | 34 | 68% |
| Denial of service via user lockout | 61 | 29 | 48% |
| SQL injection | 28 | 23 | 82% |
| Kiosk mode breakout | 26 | 19 | 73% |
| Business logic bypass — data validation | 38 | 17 | 45% |
| Broken access control | 15 | 12 | 80% |

These are not the findings we report most often. Our highest-volume findings — Content Security Policy misconfiguration, missing HSTS, subresource integrity — do not appear on this list at all, and a scanner will hand you every one of them. **The findings that fill a report and the findings that endanger a business are almost entirely different sets.**

## And one class dominates

Group that list by class. **Authorization — IDOR, vertical and horizontal bypass, broken access control, anonymous bypass, forceful browsing — comes to 173. Every variety of cross-site scripting combined comes to 128.**

**Authorization is the single largest class of serious finding we report.** When we find something that genuinely endangers a business, it is more often a broken authorization boundary than anything else.

## Why authorization is the one a tool will not hand you

This is the part worth internalising, and it is not a marketing line — it follows directly from what these bugs are.

A cross-site scripting payload *looks wrong*. There is a string with angle brackets in a field that should hold a name. An SQL injection looks wrong. A traversal looks wrong. A tool can pattern-match all of them, because the request itself is malformed. That is why scanners find XSS, and why XSS is the one class that comes close to authorization above.

An authorization bypass is a *perfectly well-formed request*. A valid, authenticated session asks for object 1,041 instead of object 1,040. Every field is the right type. Every value is in range. The signature verifies. Nothing about it is anomalous in any way a scanner can express — and the server answers, because nobody wrote the check that says this user does not own that object.

To find it, you have to know what object 1,041 is, who is supposed to see it, and what the roles in th...