---
title: AI Decision Models and Their Impact on AI SOC Platforms
url: https://thehackernews.com/2026/10/ai-decision-models-and-their-impact-on.html
source: The Hacker News
date: 2026-10-16
fetch_date: 2026-10-17T06:39:14.017014
---

# AI Decision Models and Their Impact on AI SOC Platforms

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [AI Decision Models and Their Impact on AI SOC Platforms](https://thehackernews.com/2026/10/ai-decision-models-and-their-impact-on.html)

**The Hacker News**Oct 16, 2026Artificial Intelligence / Security Operations

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVccQyMWKH3TTGpMGwsFUkVETAsZFTWBlOZyCPr3ZlMJfVPTN09xHFKk94-6OWpwhpE68JRImlVGgma5xaM66ohDwD5XvlOu1FjQPllSMNRvuDUMPB0PNUJEK3u2MaELBNvDP0GNThHj3IGreaWQe6UpzfZ55Ei6HeOpmbcWzo6Mach5g3-9OJPBuA1wY/s1700-nu-rw-lo-l85-e365/modal.jpg)

In the space of a month, a new category of AI model went from nonexistent to everywhere. TypeSafe AI released [Jev](https://dealroom.co/news/157162-what-is-jev-typesafe-ais-decision-model-for-software/) on September 15 and called it a System One model, a nod to [Kahneman's fast, intuitive thinking](https://thehackernews.com/2026/07/thinking-fast-and-slow-in-soc-case-for.html). OpenAI announced its own [Decisions API](https://serpapi.com/blog/introduction-to-openais-decisions-api-building-a-remote-job-finder-with-serpapi/) at DevDay and opened a public beta on October 6. Cribl published [cribl-decision](https://huggingface.co/cribl-ai/cribl-decision-1.0), an open LoRA adapter you can run locally. Others, like Laya, are already showing up in open source tooling.

These models skip text generation entirely. You hand them some state and a set of typed questions. They hand back a choice, a score, or a yes/no with a probability attached.

For security operations, I think this is some of the best news of the year. I also think most of the conversation is pointed at the wrong layer.

## **Why a SOC should be excited**

Three properties make decision models a natural fit for alert triage.

**You get a number you can automate against.** A typed answer with a calibrated probability is something you can put a threshold on. Ask the model whether an alert is benign and you get back a probability. Close it automatically above 0.97. Below 0.6, treat it as a likely incident and escalate it. Anything in between goes to an analyst for a closer look. TypeSafe even suggests stricter thresholds for irreversible actions, which maps neatly onto “disable an account” versus “add a comment to the ticket.”

**They're cheap enough for every alert.** Jev is priced at $42 per billion input tokens, with responses in 70 to 500 milliseconds. Say an enterprise sees 450,000 alerts a year and you feed a few thousand tokens per alert. The model bill lands somewhere around a hundred dollars a year. The economic argument for cherry-picking and only looking at high-severity alerts just disappeared!

**Every verdict becomes a record.** The answer space is fixed in advance and the output carries its own probability. You can log every decision, replay it, and compare it with what actually happened. That's far easier to audit than a paragraph of generated reasoning.

One caveat worth keeping in mind. When vendors say these models "can't hallucinate," they mean the output always matches the schema you defined. A well-formed answer can still be wrong.

## **But a calibrated guess is still just a guess**

The old rule still applies. Garbage in, garbage out.

Calibration is a promise about a distribution. When a well-calibrated model says 90%, it means that across inputs that look like this one, it's right about 90% of the time. So the question that matters is what "this one" looks like. If the input is an alert title and a severity field, the model is calibrated about alerts with that title and that severity. It knows nothing about the host.

Here's why that matters in practice. Our [AI SOC Report 2026](https://intezer.com/2026-ai-soc-report-for-cisos) covers 25 million alerts triaged across our customer base in 2025. In that data, 82,000 alerts went through a live memory scan of the endpoint. About 2,600 of those machines had an active infection. And 51% of the infected machines had already been reported as mitigated by the EDR.

Think about what a decision model sees for one of those alerts. Malware detected, threat quarantined, low severity. A perfectly calibrated model should close it with high confidence, because most alerts that look like that really are fine. The model did its job. The input was wrong.

Severity has the same problem at a larger scale. Nearly 1% of real incidents in our data traced back to alerts at the lowest severity levels. At an average of 450,000 alerts a year, that's roughly 54 real threats, about one a week.

Cribl's own model card says it plainly. The model can be overconfident, and it's sensitive to how the prompt and candidates are worded. That's honest, and it applies to every model in this category.

## **What evidence actually looks like**

Think about a crime scene. You can describe it to a chatbot in general terms and get a plausible theory. Or you can bring in the DNA lab, the fingerprints, the forensic evidence and the witness statements. Nobody needs to ask which approach finds the right suspect.

Security investigations work the same way. Filip Stojkovski recently called this Security Context Engineering, and I think the name fits. The job is to turn an alert into a set of facts before anyone, human or model, makes a call.

|  |  |  |
| --- | --- | --- |
| The question | What the alert usually gives you | What forensic evidence gives you |
| What ran? | "Suspicious PowerShell" | The process tree, the parent, the full command line, the script on disk |
| What did it do? | A hash and a reputation score | What the file did when detonated, the network calls, the files it dropped |
| Is it still there? | "Mitigated" from the EDR | A live memory scan showing injected code or a fileless payload |
| Who was it? | A username | Where they logged in, from which device, and whether that's normal for them |

The third row deserves extra attention. The most common families we found in memory last year were tools like Mimikatz, Meterpreter and Cobalt Strike...