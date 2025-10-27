---
title: The Data Breach Disclosure Conundrum
url: https://www.troyhunt.com/the-data-breach-disclosure-conundrum/
source: Troy Hunt's Blog
date: 2024-09-28
fetch_date: 2025-10-06T18:30:43.573365
---

# The Data Breach Disclosure Conundrum

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# The Data Breach Disclosure Conundrum

28 September 2024

The conundrum I refer to in the title of this post is the one faced by a breached organisation: disclose or suppress? And let me be even more specific: should they disclose to *impacted individuals,* or simply never let them know? I'm writing this after many recent such discussions with breached organisations where I've found myself wishing I had this blog post to point them to, so, here it is.

Let's start with tackling what is often a fundamental misunderstanding about disclosure obligations, and that is *the legal necessity to disclose*. Now, as soon as we start talking about legal things, we run into the problem of it being different all over the world, so I'll pick a few examples to illustrate the point. As it relates to the UK GDPR, there are two essential concepts to understand, and they're the first two bulleted items in [their personal data breaches guide](https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/?ref=troyhunt.com):

> The UK GDPR introduces a duty on all organisations to report certain personal data breaches to the relevant supervisory authority. You must do this within 72 hours of becoming aware of the breach, where feasible.

> If the breach is likely to result in a high risk of adversely affecting individuals’ rights and freedoms, you must also inform those individuals without undue delay.

On the first point, "certain" data breaches must be reported to "the relevant supervisory authority" within 72 hours of learning about it. When we talk about disclosure, often (not just under GDPR), that term refers to the responsibility to report it to the *regulator*, not the *individuals*. And even then, read down a bit, and you'll see the carveout of the incident needing to expose personal data that is *likely* to present a "risk to people’s rights and freedoms".

This brings me to the second point that has this massive carveout as it relates to disclosing to the individuals, namely that the breach has to present "a high risk of adversely affecting individuals’ rights and freedoms". [We have a similar carveout in Australia](https://www.oaic.gov.au/privacy/your-privacy-rights/data-breaches/what-is-a-notifiable-data-breach?ref=troyhunt.com) where the obligation to report to individuals is predicated on the likelihood of causing "serious harm".

This leaves us with the fact that in many data breach cases, organisations may decide they don't need to notify individuals whose personal information they've inadvertently disclosed. Let me give you an example from smack bang in the middle of GDPR territory: Deezer, the French streaming media service that went into HIBP early January last year:

> New breach: Deezer had 229M unique email addresses breached from a 2019 backup and shared online in late 2022. Data included names, IPs, DoBs, genders and customer location. 49% were already in [@haveibeenpwned](https://twitter.com/haveibeenpwned?ref_src=twsrc%5Etfw&ref=troyhunt.com). Read more: [https://t.co/1ngqDNYf6k](https://t.co/1ngqDNYf6k?ref=troyhunt.com)
>
> — Have I Been Pwned (@haveibeenpwned) [January 2, 2023](https://twitter.com/haveibeenpwned/status/1609754235557777408?ref_src=twsrc%5Etfw&ref=troyhunt.com)

229M records is a *substantial* incident, and there's no argument about the personally identifiable nature of attributes such as email address, name, IP address, and date of birth. However, at least initially (more on that soon), Deezer chose not to disclose to impacted individuals:

> Chatting to [@Scott\_Helme](https://twitter.com/Scott_Helme?ref_src=twsrc%5Etfw&ref=troyhunt.com), he never received a breach notification from them. They disclosed publicly via an announcement in November, did they never actually email impacted individuals? Did \*anyone\* who got an HIBP email get a notification from Deezer? [https://t.co/dnRw8tkgLl](https://t.co/dnRw8tkgLl?ref=troyhunt.com) [https://t.co/jKvmhVCwlM](https://t.co/jKvmhVCwlM?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [January 2, 2023](https://twitter.com/troyhunt/status/1610010254649221120?ref_src=twsrc%5Etfw&ref=troyhunt.com)

> No, nothing … but then I’ve not used Deezer for years .. I did get this👇from FireFox Monitor (provided by your good selves) [pic.twitter.com/JSCxB1XBil](https://t.co/JSCxB1XBil?ref=troyhunt.com)
>
> — Andy H (@WH\_Y) [January 2, 2023](https://twitter.com/WH_Y/status/1610014498852577280?ref_src=twsrc%5Etfw&ref=troyhunt.com)

> Yes, same situation. I got the breach notification from HaveIBeenPwned, I emailed customer service to get an export of my data, got this message in response: [pic.twitter.com/w4maPwX0Qe](https://t.co/w4maPwX0Qe?ref=troyhunt.com)
>
> — Giulio Montagner (@Giu1io) [January 2, 2023](https://twitter.com/Giu1io/status/1610010540717346818?ref_src=twsrc%5Etfw&ref=troyhunt.com)

This situation understandably upset many people, with many cries of "but GDPR!" quickly following. [And they did know *way* before I loaded it into HIBP too](https://web.archive.org/web/20221129113711/https%3A//support.deezer.com/hc/en-gb/articles/7726141292317-Third-Party-Data-Breach), almost two months earlier, in fact (courtesy of archive.org):

> This information came to light November 8 2022 as a result of our ongoing efforts to ensure the security and integrity of our users’ personal information

They knew, yet they chose not to contact impacted people. [And they're also confident that position didn't violate any data protection regulations](https://support.deezer.com/hc/en-gb/articles/7726141292317-Third-Party-Data-Breach?ref=troyhunt.com) (current version of the same page):

> Deezer has not violated any data protection regulations

And based on the carveouts discussed earlier, I can see how they drew that conclusion. Was the disclosed data likely to lead to "a high risk of adversely affecting individuals’ rights and freedoms"? You can imagine lawyers arguing that it wouldn't. Regardless, people were *pissed,* and if you read through those respective Twitter threads, you'll get a good sense of the public reaction to their handling of the incident. HIBP sent 445k notifications to our own individual subscribers and another 39k to those monitoring domains with email addresses in the breach, and if I were to hazard a guess, that may have been what led to this:

> Is this \*finally\* the [@Deezer](https://twitter.com/Deezer?ref_src=twsrc%5Etfw&ref=troyhunt.com) disclosure notice to individuals, a month and a half later? It doesn’t look like a new incident to me, anyone else get this? [https://t.co/RrWlczItLm](https://t.co/RrWlczItLm?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [February 20, 2023](https://twitter.com/troyhunt/status/1627757160221519872?ref_src=twsrc%5Etfw&ref=troyhunt.com)

So, they know about the breach in Nov, and they told people in Feb. It took them a quarter of a year to tell their customers they'd been breached, and if my understanding of their position and the regulations they were adhering to is correct, they never needed to send the notice at all.

I appreciate that's a very long-winded introduction to this post, but it sets the scene and illustrates the conundrum perfectly: an organisation may not need to disclose to individuals, but if they don't, they risk a backlash that may eventually force their hand.

In my past dealing with organisations that were reticent to disclose to their customers, their positions were often that the data was relatively benign. Email addresses, names, and some other identifiers of minimal consequence. It's often clear that the organisation is leaning towards the "uh, may...