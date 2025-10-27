---
title: IoT Devices in Password-Spraying Botnet
url: https://www.schneier.com/blog/archives/2024/11/iot-devices-in-password-spraying-botnet.html
source: Schneier on Security
date: 2024-11-07
fetch_date: 2025-10-06T19:20:33.732226
---

# IoT Devices in Password-Spraying Botnet

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

## IoT Devices in Password-Spraying Botnet

Microsoft is [warning](https://arstechnica.com/information-technology/2024/11/microsoft-warns-of-8000-strong-botnet-used-in-password-spraying-attacks/) Azure cloud users that a Chinese controlled botnet is engaging in “highly evasive” password spraying. Not sure about the “highly evasive” part; the techniques seem basically what you get in a distributed password-guessing attack:

> “Any threat actor using the CovertNetwork-1658 infrastructure could conduct password spraying campaigns at a larger scale and greatly increase the likelihood of successful credential compromise and initial access to multiple organizations in a short amount of time,” Microsoft officials wrote. “This scale, combined with quick operational turnover of compromised credentials between CovertNetwork-1658 and Chinese threat actors, allows for the potential of account compromises across multiple sectors and geographic regions.”
>
> Some of the characteristics that make detection difficult are:
>
> * The use of compromised SOHO IP addresses* The use of a rotating set of IP addresses at any given time. The threat actors had thousands of available IP addresses at their disposal. The average uptime for a CovertNetwork-1658 node is approximately 90 days.* The low-volume password spray process; for example, monitoring for multiple failed sign-in attempts from one IP address or to one account will not detect this activity.

Tags: [botnets](https://www.schneier.com/tag/botnets/), [China](https://www.schneier.com/tag/china/), [Internet of Things](https://www.schneier.com/tag/internet-of-things/), [passwords](https://www.schneier.com/tag/passwords/)

[Posted on November 6, 2024 at 7:02 AM](https://www.schneier.com/blog/archives/2024/11/iot-devices-in-password-spraying-botnet.html) •
[7 Comments](https://www.schneier.com/blog/archives/2024/11/iot-devices-in-password-spraying-botnet.html#comments)

### Comments

Clive Robinson •
[November 6, 2024 8:56 AM](https://www.schneier.com/blog/archives/2024/11/iot-devices-in-password-spraying-botnet.html/#comment-441520)

@ Folks,

Welcome to the “New word order” form of “clickbait” to get attention.

With regards the implicit question in,

> ‘Not sure about the “highly evasive” part’

That “highly evasive” is what advertising people once used to call a “hook”. It’s purpose is to activate your emotions not your reasoning.

Think of it like the “Camel Cowboy” of those deadly cigarette adverts,

“Yer all, wana look like him”

Right… Such was the typical sales and marketing reasoning (not sure if that said more about them or what they thought of prospective customers of time).

So “highly evasive” will become the new “think of the children” type dog whistle at some point, and in turn it will get replaced… Each in some way more desperately reaching than it’s predecessors.

Why, well it’s a side effect of what we outside the US call “The American way”. If you think back it was sufficiently well known or believed that you could get compensation money for “sipping hot coffee” and complaining that the person who had sold it had not given sufficient warning…

Thus there is a form of reasoning process that sort of says,

“If we don’t grab attention we will get sued.”

So we get “marketing speak” hooks as a legal protection… And as always underneath driving it will be the ever moving target of “best practice” for lawyers et al to drive things forward.

Which is why I’m reminded of the old,

“Build a better mouse trap…”

Saying of old, in that the person who comes up with a near perfect “marketing speak” removal tool will certainly have many people beat a path to their door…

Only these days it will be lawyers or worse[1] from sales and marketing execs wanting to eliminate the “rice bowl breaker” with maximum prejudice.

[1] For those who think I’m being a little over melodramatic, just consider what has so far happened to people that have developed “ad blockers” and similar for web browsers.

Clive Robinson •
[November 6, 2024 9:39 AM](https://www.schneier.com/blog/archives/2024/11/iot-devices-in-password-spraying-botnet.html/#comment-441521)

On a more technical note…

There is very little new here.

It is in effect an extension on a “bot net” doing a “Distributed Denial of Service”(DDoS) attack using “Internet of Things”(IoT) or consumer grade “Network Appliances” that have not had security “patches” applied if they even exist, which mostly they do not.

The difference for what it is worth is the “denial of service” part of the “pay load” is not just a “load magnifier” (though it is). It actually returns something of use to the attacker (login credentials etc).

For the defender there is actually no real solution to the problem. That is what ever you do just makes it worse for legitimate users and your service, without stopping the attacker or even inconveniencing them much.

Thus it’s a process that has fallen into the same issues that Electronic Warefare did with “Electromagnetic Counter Measures” where ECM begat ECCM that, in turn begat ECCCM and so on. Each additional C represented an exponential step increase in cost for basically at best a fractional increase in utility.

As was once noted,

“There can only be so much noise, before the headache drives you mad.”

As with ECM the looser is almost always the “static defender” who is daft enough to “stay in the game”. Thus the solution is “get out of the game” and where that is not possible to stop being “static” or a “defender” or both.

One effective way is “segregation” that is either not go beyond your own perimeter (stop using external comms) or set up your systems such that anything an external attacker might reach has no value to them because it’s entirely segregated from your internal systems.

Another of less utility is to make a significant “Step change in method” that the attacker is trying to utilize. Whilst doing this for authentication on systems inside your perimeter is under your control… With Cloud and other external Services it’s not.

There is an increasing trend for people to “bring back in house” services they had previously put into Cloud Services on the mistaken belief it would “make savings” of some form.

The reality is a short term effectively “one off” saving in exchange for getting hooked by “rent seeking” ever increasing costs. Worse Cloud is rarely low risk not just security wise but technically as well. It also reduces flexibility and responsiveness in all but trivial usages.

ResearcherZero •
[November 11, 2024 1:42 AM](https://www.schneier.com/blog/archives/2024/11/iot-devices-in-password-spraying-botnet.html/#comment-441581)

TP-Link decided to release some firmware updates today for EoL routers.

ResearcherZero •
[November 11, 2024 2:54 AM](https://www.schneier.com/blog/archives/2024/11/iot-devices-in-password-spraying-botnet.html/#comment-441584)

@Clive Robinson

There ...