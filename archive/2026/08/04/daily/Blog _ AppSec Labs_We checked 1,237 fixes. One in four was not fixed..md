---
title: We checked 1,237 fixes. One in four was not fixed.
url: https://appsec-labs.com/we-checked-1237-fixes/
source: Blog | AppSec Labs
date: 2026-08-04
fetch_date: 2026-08-05T04:58:12.333208
---

# We checked 1,237 fixes. One in four was not fixed.

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

# We checked 1,237 fixes. One in four was not fixed.

August 4, 2026

[No comments yet](https://appsec-labs.com/we-checked-1237-fixes/#respond)

**Between October 2021 and August 2026 our clients sent 1,237 fixes back to us and asked us to confirm they worked. 307 of them did not.**

That is more than one in four. Not one in four findings — one in four *fixes*, each one submitted by a team that believed the work was done.

## Where this number comes from

Retesting is included in how we work and costs nothing extra. When a client has fixed something they tell us, and we re-run the original attack. The finding is then closed as fixed, or it is not. The one thing we cannot do is start it — the client has to ask, and most of the time nobody does.

Across the window we reported 4,956 findings to clients. **1,237 were sent back for verification**, and 1,159 of those reached a definite verdict. This article is about those 1,159, because they are the only fixes in the industry anyone can actually score.

| Final verdict | Fixes | Share |
| --- | --- | --- |
| Fixed | 846 | 73.0% |
| Not fixed | 176 | 15.2% |
| Partially fixed | 131 | 11.3% |
| Mitigated, not fixed | 6 | 0.5% |

**26.5% failed verification** — and that is the figure *after* however many rounds it took, not on the first attempt.

## The first attempt is much worse

Look at the first verdict rather than the last, and the picture is harder:

| First verdict | Fixes |
| --- | --- |
| Fixed | 524 |
| Mitigated but not verified | 337 |
| Not fixed | 190 |
| Partially fixed | 119 |

**Only 42% of fixes are right the first time we look.** The gap between that and the 73% that eventually pass is entirely made of second and third attempts — work that only happened because somebody checked.

Most of that recovery happens in one extra round: 1,081 fixes closed after a single retest, 119 needed two, 20 needed three. A stubborn tail needed up to ten.

## Why a fix fails

The failures are not carelessness. They cluster in a way that anyone who has fixed a security bug will recognise.

**The fix addresses the proof, not the flaw.** We report an authorization bypass and demonstrate it on object 1,041. The check gets added for that endpoint. The same missing check on the neighbouring endpoint, which our report described but did not screenshot, stays open. This is the single most common shape of a partial fix.

**The fix is correct and incomplete.** Input is validated on the path we showed, and the second path into the same handler is untouched.

**The control was mitigated rather than fixed.** A WAF rule now blocks the payload we sent. The vulnerability is still there; what changed is one signature. That is why we score *mitigated* separately from *fixed* — on first inspection 337 fixes were exactly this, and treating them as done would have flattered everyone.

Every one of these is invisible without a retest. The developer has no way to know: the attack in the report does not work any more, which from their side looks exactly like success.

## The delay is not where you would guess

The obvious explanation for a slow remediation loop is that the security firm is a bottleneck. It is worth checking, so here is ours, and it is checkable against any engagement we have run.

| Step | Median |
| --- | --- |
| Report delivered → fix submitted to us | 33 days |
| Fix submitted → our verdict | 0.2 days |
| Report delivered → finding closed | 35 days |

We turn a retest around in about five hours. The other 33 days are the fix itself, which is entirely reasonable — engineering takes time. The point is only that **the verification step costs almost nothing**, so whatever is stopping organisations from closing the loop, it is not the cost of the check.

## What actually stops it

Of the customers who have had ten or more findings reported to them, **28 have never submitted a single one for retest.** Six verify everything. The median organisation verifies **19%** of what it is told about.

That spread is not about budget or sector. It tracks one thing: whether the retest was written into the engagement at the start, or left as something to arrange later. Loops that were part of the plan get closed. Loops that were optional do not, because the moment a report is delivered the people who would drive it are already on the next thing.

## What to do about it

**Treat “fixed” as a claim, not a status.** Until someone has re-run the attack, a closed ticket records an intention. On our numbers, that intention is wrong about a quarter of the time.

**Put the retest in the statement of work.** Not as an option, not as a follow-on quote. The single strongest predictor of whether findings get verified is whether somebody agreed to verify them before the test started.

**Ask for the failure detail, not just the pass.** A retest that says “fixed” teaches you nothing. One that says “fixed on the endpoint we demonstrated, still open on the other three” tells you something about how your team reads a report — which is worth more than the individual bug.

**Retest by class, not by ticket.** If we found an IDOR on one object, the question at retest is not whether that object is fixed. It is whether the pattern was fixed. The 11% of fixes that come back partial are almost entirely this.

---

*Figures are from our own engagement records, October 2021 to August 2026: 4,956 findings reported to clients, 1,237 submitted for retest, 1,159 reaching a definite verdict. Counts and distributions only — no client is identifiable from any number here. A companion piece, [what 890 security engagements actually find](/what-890-security-engagements-actually-find/), covers which findings we report and which are genuinely dangerous.*

![](https://secure.gravatar.com/avatar/?s=120&d=mm&r=g)

#####

## Post navigation

[Previous](https://appsec-labs.com/he-what-890-security-engagements-actually-find/)

[Next](https://appsec-labs.com/he-we-checked-1237-fixes/)

#### Search

Search for:

#### Categories

* [AI and LLM Security](https://appsec-labs.com/category/ai-llm-security/) (28)
* [API Security](https://appsec-labs.com/category/api-security/) (9)
* [Application Security](https://appsec-labs.com/category/application-security/) (22)
* [Authorization and Access Control](https://appsec-labs.com/category/authorization/) (11)
* [Black Box Testing](https://appsec-labs.com/category/black-box-testing/) (3)
* [Brute Force](https://appsec-labs.com/category/brute-force/) (1)
* [Cloud Security](https://appsec-labs.com/category/cloud-security/) (17)
* [Engagements and Process]...