---
title: Your DFIR Tool Can’t Tell You Who Did It. FACT Tells You When You’re Allowed To.
url: https://brettshavers.com/brett-s-blog/entry/your-df-ir-tool-cant-tell-you-who-did-it-fact-tells-you-when-youre-allowed-to
source: Instapaper: Unread
date: 2025-12-20
fetch_date: 2025-12-21T03:27:04.434295
---

# Your DFIR Tool Can’t Tell You Who Did It. FACT Tells You When You’re Allowed To.

![Brett Shavers](https://brettshavers.com/images/brettsramblings.png)

* [Home](/?view=entry&layout=latest)
* [Brett's Blog](/brett-s-blog)
* [My Books](/my-books)
* [Courses](/my-courses)
* [Hire me?](/meet-brett)
* [About Me](/about-brett)
* [Contact](/contact-brett)

## Brett's Ramblings

Font size:
+
–

[Print](/brett-s-blog/entry/your-df-ir-tool-cant-tell-you-who-did-it-fact-tells-you-when-youre-allowed-to?tmpl=component&print=1&format=print "Print")

4 minutes reading time
(802 words)

# Your DF/IR Tool Can’t Tell You Who Did It. FACT Tells You When You’re Allowed To.

[Digital Forensics](/brett-s-blog/categories/digital-forensics)

[Brett Shavers](/brett-s-blog/blogger/brett)

Sunday, 14 December 2025

4462 Hits

DF/IR doesn’t usually fail on the technical work. It fails at the exact moment someone gets impatient and confuses **activity with identity**, and then confuses **identity with attribution**.

“This account did it” becomes “this person did it,” with zero bridge, zero falsification, and a pile of untested assumptions. That’s how you build an attribution that looks confident right up until it gets proven wrong.

![](/images/easyblog_articles/764/b2ap3_large_Tie-the-Act-to-the-Actor.png)

Not “which laptop.” Not “which account.” Not “which session.” A real human.

That’s where conclusions get proven wrong. Not because the artifacts were fake or the analysis was inaccurate. Because the bridge from **act → actor** was never built, never tested, and never written down. Shared access, credential misuse, remote admin actions, automation, service accounts, AI agents… ordinary alternatives survive, and the “attribution” collapses.

*FACT isn’t academic homework. It’s practical application.*

## **What FACT fixes (the thing we all pretend isn’t a problem)**

We’ve gotten very good at moving through **identity** layers but conflate, comingle, and misinterpret **attribution** levels.

|  |  |
| --- | --- |
| **Identity Layers** | **Attribution Layers** |
| * Artifact-level * Device-level * Account-level * User/session-level * Person-level | * Technical attribution * Investigative attribution * Legal attribution |

That’s where we get proven wrong. FACT draws a hard line between **identification** and **attribution**, and it forces you to work the layers instead of skipping them. If you’ve seen it before, you already know why this matters.

## **“Stay in your lane” (this section in FACT alone is worth the download)**

**![](/images/easyblog_articles/764/b2ap3_large_roles.png)**

If you’re operating as an **examiner/analyst**, FACT puts you in the lane you should live in:

*“This device, this account, this action, at this time, with these uncertainties.”*

It also makes a second, usually unspoken point: The moment you go beyond scope and start relying on interviews, CCTV, HR files, access-control records, witness statements, financial records, or other evidence, you are no longer operating *only* as an examiner. Functionally, and legally, you stepped into the **practitioner–investigator** role.

That’s not a moral judgment. It’s a responsibility boundary. And it completely changes how you can approach attribution and what you’re allowed to testify about it.

FACT helps you keep those roles clean, your reasoning explicit, and your conclusions defensible. Aka: It keeps you out of the hot seat.

## **What you get when you download FACT**

This is what’s inside the PDF, in plain terms: Usable structure with a clear F-A-C-T lifecycle for attribution and separation of roles (some can only identify, others can attribute).

[![](/images/easyblog_articles/764/b2ap3_large_downloadFACT.png)](https://doi.org/10.5281/zenodo.17745959)

FACT Attribution Framework™ v1.0 (December 2025)
DOI: <https://doi.org/10.5281/zenodo.17745959>

## **Why FACT wasn’t peer reviewed before release (briefly, without bs from BS)**

Academic peer review has value. It can improve clarity, spot weaknesses, and force you to defend structure, definitions, and theory.

Academic publishing rewards the act of publishing: novelty, citations, and getting through the review gate. But practitioners live in a different economy: they don’t get rewarded for a clever theory; they get punished when the theory doesn’t survive contact with real cases, real constraints, and real adversarial challenge.

In real casework, you don’t get to be “interesting.” You work to be right or you get proven wrong. Those incentives are not the same. Don’t pretend that they are.

I released FACT v1.0 as a usable tool first (versioned, public, and meant to be applied) because a framework that isn’t used or seen is just fancy literature on a shelf.

And no, this framework didn’t go out for a blind review. FACT v1.0 received pre-release review from 36 of 45 invited, experienced practitioners and stakeholders spanning law enforcement, corporate DFIR, consulting, academia, and attorneys. The feedback was consistent: existing frameworks don’t provide a structured, defensible approach to person-level attribution, and FACT fills that gap without replacing anything you already use.

FACT doesn’t compete with your DF/IR lifecycles. It wraps them in legal bookends: authority and compliance up front, and reporting/testimony-ready reasoning at the end.

And yes, FACT will be subject to peer review and comparison next year.

## **Why you should believe a practitioner-first release can last**

I’ve already watched this play out. In 2006 and 2008 I published two virtualization forensics papers as practitioner essays. No journal pipeline, no paywall; they kept getting cited and quoted for years afterward across textbooks, dissertations, conference papers, and peer-reviewed work, including citations that show up nearly two decades later (one is a book titled virtualization forensics!). That’s not because a gatekeeper approved them; it’s because the ideas survived contact with reality and stayed useful.

**Peer review is a gate. What you got is a gauntlet.**

## **Read FACT and tell me you haven’t wanted it for years**

I get it. Most in DF/IR don’t “adopt frameworks.” We skim them, nod, and go back to work.

FACT is different on purpose. It’s designed to be grabbed and used today.

You’re going to read FACT and say: **“It is about time someone wrote this down.”**

[![](/images/easyblog_articles/764/b2ap3_large_downloadFACT.png)](https://doi.org/10.5281/zenodo.17745959)

FACT Attribution Framework™ v1.0 (December 2025)
DOI: <https://doi.org/10.5281/zenodo.17745959>

---

**PS**

[**Check out the DFIR Soundtrack**](https://www.youtube.com/playlist?list=PL7t7cXJsdNmbLSR3Z2gyOfRcODxaFuT_i)

[**![](/images/easyblog_articles/764/b2ap3_large_Vinyl.png)**](https://www.youtube.com/playlist?list=PL7t7cXJsdNmbLSR3Z2gyOfRcODxaFuT_i)

[Tweet](https://twitter.com/intent/tweet?url=https%3A%2F%2Fbrettshavers.com%2Fbrett-s-blog%2Fentry%2Fyour-df-ir-tool-cant-tell-you-who-did-it-fact-tells-you-when-youre-allowed-to&text=Your+DF%2FIR+Tool+Can%E2%80%99t+Tell+You+Who+Did+It.+FACT+Tells+You+When+You%E2%80%99re+Allowed+To.&via=Brett_Shavers)

[pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbrettshavers.com%2Fbrett-s-blog%2Fentry%2Fyour-df-ir-tool-cant-tell-you-who-did-it-fact-tells-you-when-youre-allowed-to&media=https%3A%2F%2Fbrettshavers.com%2Fimages%2Feasyblog_articles%2F764%2Fb2ap3_thumbnail_Tie-the-Act-to-the-Actor.png&description=Your+DF%2FIR+Tool+Can%E2%80%99t+Tell+You+Who+Did+It.+FACT+Tells+You+When+You%E2%80%99re+Allowed+To.)

×

Stay Informed

When you subscribe to the blog, we will send you an e-mail when there are new updates on the site so you wouldn't miss them.

Your Name

E-mail Address

Subscribe to the blog

[Fight City Hall: If You Missed the Webinar, You’re...](/brett-s-blog/entry/fight-city-hall-if-you-missed-the-webinar-youre-making-mistakes-you-dont-know-about)

#### About the author

[![Brett Shavers](https://brettshavers.com/images/easyblog_avatar/42_brett.JPG)](/brett-s-blog/blogger/brett)

### [Brett Shavers...