---
title: Friday Squid Blogging: NGC 1068 Is the “Squid Galaxy”
url: https://www.schneier.com/blog/archives/2025/05/friday-squid-blogging-ngc-1068-is-the-squid-galaxy.html
source: Schneier on Security
date: 2025-05-30
fetch_date: 2025-10-06T22:38:47.848249
---

# Friday Squid Blogging: NGC 1068 Is the “Squid Galaxy”

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

## Friday Squid Blogging: NGC 1068 Is the “Squid Galaxy”

I hadn’t known that the NGC 1068 galaxy is nicknamed the “Squid Galaxy.” It is, and it’s [spewing neutrinos](https://scitechdaily.com/the-squid-galaxys-black-hole-just-unleashed-a-neutrino-storm-without-the-light/) without the usual accompanying gamma rays.

As usual, you can also use this squid post to talk about the security stories in the news that I haven’t covered.

Tags: [squid](https://www.schneier.com/tag/squid/)

[Posted on May 29, 2025 at 5:04 PM](https://www.schneier.com/blog/archives/2025/05/friday-squid-blogging-ngc-1068-is-the-squid-galaxy.html) •
[32 Comments](https://www.schneier.com/blog/archives/2025/05/friday-squid-blogging-ngc-1068-is-the-squid-galaxy.html#comments)

### Comments

ResearcherZero •
[May 29, 2025 10:36 PM](https://www.schneier.com/blog/archives/2025/05/friday-squid-blogging-ngc-1068-is-the-squid-galaxy.html/#comment-445614)

SSH backdoor can only be removed by factory reset and manual reconfiguration.

‘https://www.greynoise.io/blog/stealthy-backdoor-campaign-affecting-asus-routers

Vicious Trap

The SSH backdoor persists across firmware updates and uses no malware.
<http://www.labs.greynoise.io/grimoire/2025-03-28-ayysshush/>

ResearcherZero •
[May 29, 2025 10:58 PM](https://www.schneier.com/blog/archives/2025/05/friday-squid-blogging-ngc-1068-is-the-squid-galaxy.html/#comment-445615)

ConnectWise says a small number of customers were targeted by a nation state attack.

ConnectWise had stated ASP.NET machine keys were used in ViewState code injection attacks.

‘https://www.connectwise.com/company/trust/advisories

ViewState allows state values to be preserved across page postbacks.

Microsoft identified that more than 3,000 machine keys had been publicly disclosed online.
After achieving remote code execution, attackers had set up Godzilla to control servers.
<https://www.microsoft.com/en-us/security/blog/2025/02/06/code-injection-attacks-using-publicly-disclosed-asp-net-machine-keys/>

Clive Robinson •
[May 30, 2025 5:44 AM](https://www.schneier.com/blog/archives/2025/05/friday-squid-blogging-ngc-1068-is-the-squid-galaxy.html/#comment-445623)

@ ResearcherZero, Bruce, ALL,

With regards the link to Greynoise labs you give…

The opening paragraph is, –independent of the vulnerability the article is about,– of interest,

> *“Using an AI powered network traffic analysis tool we built called SIFT, GreyNoise has caught multiple anomalous network payloads with zero-effort that are attempting to disable…”*

Using a variant of a ‘current AI LLM and ML system’ to “scan logs” looking for “low level anomalous signals” is something I’ve been thinking about.

As anyone who has tried it knows reading in-depth logs is important, but it’s “drudge work”. Something most humans can not do if even for quite short periods of time.

Yes you can learn to read them like a book, but you can also go mad trying, or both… So it falls to the “chicken or the egg” question.

Conventional automated scanning looks for “Known, Knowns” or sometimes “Unknown, Knowns” but generally not “Unknown, Unknowns”. But whilst they filter a lot of junk thus making the task less arduous, they do throw up a lot of “grass” of “false detects”. Due to this they are in some respects easy to get past due to the back-end human not seeing the “valid signature in the noise”.

As we know LLM&ML systems are just “adaptive filters” working on “tokenised strings of text” and finding correlations to “train the weights”. In effect a statistical tool that can very effectively parse the lines of text from log files.

The trick is getting it to recognise “Low Probability of Intercept”(LPI) signals. This is something certain “Electronic Warfare”(EW) tools currently do via thresholding techniques (and more complex tricks).

Put overly simply you remove the deterministic “know signals”, and events that have very low or no repeated entries of the “random signals” as “out of band” then to use the Martian quote,

“You science the shit out of it”

On what remains “in band” in the middle between what you assume is “deterministic” and “random” that is effectively “the chaos zone”.

You can do this by slowly moving the thresholds you can tune the filter not just to the “regular events” but also the “determanisticaly irregular events” made by adding pseudo random or actual random noise to hide the
probe signal. Basically to search for “hiding patterns”.

Having “pre-filtered” you can then use the AI to do the equivalent of “semantic searches” on higher level meanings to drill down to essential elements that can be investigated in other ways.

There are other tricks and you can find them in books etc on EW and LPI communications systems likewise radar processing in the presence of jamming signals[1]. The idea being to either “select or reject” a signal from other signals, so broadly “select LPI” and “reject jamming”

Knowing how some of such systems work from published works you can then do the classical “Renaissance-Man” trick of taking know solutions or methods from one knowledge domain and apply it to a new knowledge domain.

Like “statistical mechanics” it does not require any real intelligence to perform the drudge work, you just “go through the motions repeatedly” in a way not to dissimilar to “Weather forecasting”. Something the current AI and ML systems can do, but most humans can not.

[1] A classic “amateur” example goes back to the days of the Russian “Woodpecker” Broadband HF Over The Horizon Radar –based just next to Chernobyl– that jammed “Ham bands” from the mid 1970’s through to the end of the 80’s,

<https://en.wikipedia.org/wiki/Duga_radar>

Basically the signal processing was based on fast “noise gates” that cut the signal path for the high energy radar pulses leaving most of the desired signal “that the operators brain” the filled in the gaps made by the gates.

Clive Robinson •
[May 30, 2025 6:55 AM](https://www.schneier.com/blog/archives/2025/05/friday-squid-blogging-ngc-1068-is-the-squid-galaxy.html/#comment-445624)

@ Bruce,

You mention,

> “[T]he “Squid Galaxy.” It is, and it’s spewing neutrinos without the usual accompanying gamma rays.”

The article you link to notes it’s at quite a varience to the current “standard model” which has a lot of “Dark Matter” “Dark Energy” fiddles to try to keep the model alive in the face of new “conflicting observations”.

As the article notes,

> “Now, researchers from institutions including UCLA, Osaka University, and Japan’s Kavli Institute for the Physics and Mathematics of the Universe believe the Squid Galaxy may be producing neutrinos in a previously unknown way—one that doesn’t match the standard models.”

So expect more “Dark XXX” fiddling…

The simple fact is “Dark XXX” fiddles have three things in common

1, They predict nothing.
2, They can be twiddled to match anything.
3, They are therefore “unfalsifia...