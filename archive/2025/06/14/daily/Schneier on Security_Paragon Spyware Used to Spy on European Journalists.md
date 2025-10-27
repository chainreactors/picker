---
title: Paragon Spyware Used to Spy on European Journalists
url: https://www.schneier.com/blog/archives/2025/06/paragon-spyware-used-to-spy-on-european-journalists.html
source: Schneier on Security
date: 2025-06-14
fetch_date: 2025-10-06T22:55:08.922106
---

# Paragon Spyware Used to Spy on European Journalists

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Paragon Spyware Used to Spy on European Journalists

Paragon is an Israeli spyware company, increasingly in the news (now that NSO Group seems to be waning). “Graphite” is the name of its product. Citizen Lab [caught it](https://citizenlab.ca/2025/06/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/) spying on multiple European journalists with a zero-click iOS exploit:

> On April 29, 2025, a select group of iOS users were notified by Apple that they were targeted with advanced spyware. Among the group were two journalists that consented for the technical analysis of their cases. The key findings from our forensic analysis of their devices are summarized below:
>
> * Our analysis finds forensic evidence confirming with high confidence that both a prominent European journalist (who requests anonymity), and Italian journalist Ciro Pellegrino, were targeted with Paragon’s Graphite mercenary spyware.* We identify an indicator linking both cases to the same Paragon operator.* Apple confirms to us that the zero-click attack deployed in these cases was mitigated as of iOS 18.3.1 and has assigned the vulnerability [CVE-2025-43200](https://support.apple.com/en-us/122174).
>
> Our analysis is ongoing.

The list of confirmed Italian cases is in the report’s appendix. Italy has [recently admitted](https://www.accessnow.org/press-release/no-normalising-spyware-italy/) to using the spyware.

TechCrunch [article](https://techcrunch.com/2025/06/12/researchers-confirm-two-journalists-were-hacked-with-paragon-spyware/). Slashdot [thread](https://yro.slashdot.org/story/25/06/12/2235231/researchers-confirm-two-journalists-were-hacked-with-paragon-spyware).

Tags: [hacking](https://www.schneier.com/tag/hacking/), [Israel](https://www.schneier.com/tag/israel/), [privacy](https://www.schneier.com/tag/privacy/), [spyware](https://www.schneier.com/tag/spyware/), [surveillance](https://www.schneier.com/tag/surveillance/)

[Posted on June 13, 2025 at 6:17 AM](https://www.schneier.com/blog/archives/2025/06/paragon-spyware-used-to-spy-on-european-journalists.html) •
[4 Comments](https://www.schneier.com/blog/archives/2025/06/paragon-spyware-used-to-spy-on-european-journalists.html#comments)

### Comments

Andy •
[June 13, 2025 2:15 PM](https://www.schneier.com/blog/archives/2025/06/paragon-spyware-used-to-spy-on-european-journalists.html/#comment-445914)

At some point the problem is with Apple and Google and not the attacker. Why can’t they deliver secure software?! It’s the equivalent of a car manufacturer producing cars with breakable locks

[Soatok](https://soatok.blog) •
[June 13, 2025 2:26 PM](https://www.schneier.com/blog/archives/2025/06/paragon-spyware-used-to-spy-on-european-journalists.html/#comment-445915)

@andy

> Why can’t they deliver secure software?!

Because general purpose computers don’t have a reliable separation between data and code. So if you can send a specially crafted bit of data (in the case of CVE-2025-43200, a photo), you can get code to run on the target device.

This is endemic to the software industry. Moving to memory-safe languages will help, but ultimately, we ultimately need to move to formally verified parsers for every data format that an application accepts.

Clive Robinson •
[June 14, 2025 12:19 AM](https://www.schneier.com/blog/archives/2025/06/paragon-spyware-used-to-spy-on-european-journalists.html/#comment-445921)

@ Andy,

With regards,

> “At some point the problem is with Apple and Google and not the attacker. Why can’t they deliver secure software?!”

Because “software” is not the problem “the user is”.

Users want,

1.1, Convenience

And a few more things along those lines.

The first three on the list are what drives the design of the products.

The next two are people going to the wrong end of the,

“Personal Rights v. Social Responsibility”

Spectrum.

If you want security you have to accept two basic concepts,

2.1, Segregation
2.2, Least connectivity

And they have to apply from the bottom most layers of the computing stack all the way to the top.

Traditionally we do not present the stack in anything like a complete way, just some “bits in the middle” as seen in the 7layer ISO-OSI and 4layer DOD-IP stacks.

As an apparantly “unbreakable blinkered view” people do not venture into the “Physical layers” at the bottom, nor do they venture into the “Social layers” at the top.

But also few understand that Data/Code are actually indistinguishable from each other, they are just a “bag of bits”(BoB), that has no meaning without mata-data. Meta-data is what code is all about, and in turn meta-data has no meaning without meta-meta-data that is where humans tend to actually act/exist (yes there are other “meta” layers just as there are many if not endless semantic layers in language).

It is at the human layers that Data/Code becomes useful thus “information”.

More than a human lifetime of experience with computing tells mankind you can not separate code/data they have to exist not side by side but together. One without the other is not just useless but “meaningless”.

There are three basic things you can do with information,

3.1, Store it
3.2, Communicate it
3.3, Process it.

Less well realised is that “information in isolation” not just has no utility, it is actually meaningless… Because it can not be used to do “work”.

So to “be secure” means the “information” can not be used usefully to do “work”…

You might have heard the old,

“Information wants to be free.”

The reality is information has to be free to do work and so be of any use hence the expression “closed book” in it’s many forms.

But also remember the sage advice of Benjamin Franklin –restating advice given in “Romeo and Juliet”– of,

> *“Three may keep a secret, if two of them are dead”*

Applies to “information” and it’s security…

If you only “store information” i.e. “Data at rest”, then you can keep it secret, but communicating and processing information by their very nature are insecure.

Like “work” in the more general sense communications and processing are “inefficient” and thus there is “waste” that escapes into the environment. The waste is “always modulated” by the “work” and the “work” is always correlated by it’s use.

In information security we call the waste “side channels” and just as with the use of energy if it does not get dispersed into the larger environment then work can not be done.

It’s what Claude Shannon was stumbling around back in or before WWII and why his thoughts gave rise to the same basic truths about information as entropy relates to energy (because the processes are effectively the same).

He realised that communications was not possible without “waste” in the form of “redundancy”.

Some years later Gus Simmons showed that “where there is redundancy, side channels must exist”… And through those information leaks.

So all you can r...