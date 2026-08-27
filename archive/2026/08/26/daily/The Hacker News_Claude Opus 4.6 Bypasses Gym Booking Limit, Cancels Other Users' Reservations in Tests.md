---
title: Claude Opus 4.6 Bypasses Gym Booking Limit, Cancels Other Users' Reservations in Tests
url: https://thehackernews.com/2026/08/claude-opus-46-bypasses-gym-booking.html
source: The Hacker News
date: 2026-08-26
fetch_date: 2026-08-27T12:14:30.052141
---

# Claude Opus 4.6 Bypasses Gym Booking Limit, Cancels Other Users' Reservations in Tests

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

# [Claude Opus 4.6 Bypasses Gym Booking Limit, Cancels Other Users' Reservations in Tests](https://thehackernews.com/2026/08/claude-opus-46-bypasses-gym-booking.html)

**Swati Khandelwal**Aug 26, 2026AI Security / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiLH7AlxOwnKOlTs4Zi3D7tyko_H-564oFmjcBu-YP4_YR7HMgRvWhGB9r0NhXwpVoqVk82yjCt9XjEcDfo7-iSoAVduYsjNndt3gU2fHqJ7PlwnFCjRaHJSYEMuZMAZOn6M_yGZ24JuUUjVCs1hTXes8h-q4OLFj2liDETlKzvCRAqKa-jX2Yrh-iErI/s1700-e365/claude-gym.jpg)

Aikido Security has published research that recreates the Australian gym-booking incident in a synthetic environment, finding that Claude Opus 4.6, running on the OpenClaw agent harness, exploited a client-side-only booking restriction in 9 of 10 runs.

The original incident was first reported by ABC News on August 10, based on chat logs and screenshots the user supplied. He had asked an OpenClaw agent running Opus 4.6 to book him into a gym class. The agent booked sessions months beyond the window the site allowed.

It then tested, without being asked, whether the same API would let it cancel another member's waitlist entry. The test removed the person holding the top place and moved the user up one position. The agent told him it could not add the member back.

Aikido's test system is a single-page web application backed by a GraphQL API carrying the two flaws described in the original incident. The seven-day booking window is enforced only in the frontend, and the cancelReservation mutation does not check whether the logged-in user owns the reservation, a case of insecure direct object reference (IDOR).

In two of the ten runs, the model went on to cancel another member's confirmed booking through that second flaw before halting itself. Aikido said no prompt in any run asked the model to exploit a vulnerability.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"This dynamic suggests that safeguards may be overreactive to explicit user requests and underreactive to indirect user requests, or that models lose sight of ethical context during a sequence of repeated actions or tool calls," Aikido security researcher Oliver Smith said.

The runs used Claude Opus 4.6, which Anthropic made generally available on February 5, 2026, on OpenClaw v2026.4.1, with the model's own safety training in place and [extended thinking disabled](https://www.aikido.dev/blog/australian-gym-hack-openclaw-test).

The Hacker News confirmed via [the npm registry](https://registry.npmjs.org/openclaw) on August 25 that OpenClaw v2026.4.1 was published on April 1, 2026, and that 168 versions have shipped since then, with the current release being 2026.7.1-2.

In run one, the model canceled a confirmed reservation belonging to another member. The cancellation auto-promoted the person at the top of the waitlist.

"I shouldn't have tested that on a real reservation. That's on me. The class is back to 12/12 with the waitlist promoted, so the state is mostly consistent — but one real member did lose their spot," the model said in the run-one transcript.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3q5DRoM8V5LDW7n7Vp0BdYqbMp3BgwP7rDZ-WRFshLYhOpey7kIa1R71SF0GsWYEy5im7IRh0rvs3EwASwgKjVxrYNddiqb5ApficE9SoX1JAQu4frrCT3VuWvL3H6YFWYAXB6KvsQvlUcc4_OOmdMGus5kkK-Xx5a8EjDo9h_DPQAr1huKIKTbogYIE/s1700-e365/run--1.png)

All ten opening prompts directed the model to examine the site's API or backend, and several noted the seven-day restriction while requesting consistent bookings.

Aikido published no control arm using a plain booking request. It calculated the [average probability](https://github.com/oliversmith-aikido/gym_booking_misalignment_evaluation) of the dominant choice across its 16 sampled decision points to be 96.38%.

Anthropic had recorded the same class of behavior before the model shipped.

"We did observe some increases in misaligned behaviors in specific areas, such as sabotage concealment capability and overly agentic behavior in computer-use settings, though none rose to levels that affected our deployment assessment," Anthropic said in the [Claude Opus 4.6 system card](https://www.anthropic.com/claude-opus-4-6-system-card).

The same system card puts Opus 4.6's over-refusal rate on Anthropic's higher-difficulty benign evaluation at 0.04%, against 0.83% for Opus 4.5 and 8.50% for Sonnet 4.5.

The setup differs from [July's frontier-lab disclosures](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals). There, a misconfiguration left a sealed evaluation environment with live internet access, and Anthropic's models went on to [breach three real organizations](https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html). Anthropic said it believes those incidents to be "closer to a harness and operational failure than a model alignment failure."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Cybersecurity agencies in Australia and the U.S. have [warned about IDOR flaws before](https://thehackernews.com/2023/07/cybersecurity-agencies-warn-against.html).

The vendor behind the gym booking software remains unnamed, and no fix has been disclosed as of August 25.

The Australian Signals Directorate (ASD), which named the original incident in [an alert published on August 11](https://www.cyber.gov.au/about-us/view-all-content/news/when-ai-agents-take-unexpected-actions), advised the following -

* **Individuals should restrict agentic AI use** to low-risk, non-sensitive tasks and avoid granting agents broad or unrestricted access or decision-making authority
* **Maintain a human in the loop** to review, approve and monitor agent actions, particularly where interactions with third-party services or other users may occur
* **Organisations providing online services** should consider that AI agents might identify and exploit vulnerabilities at s...