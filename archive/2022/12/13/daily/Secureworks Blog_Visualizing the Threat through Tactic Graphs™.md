---
title: Visualizing the Threat through Tactic Graphs™
url: https://www.secureworks.com/blog/visualizing-the-threat-through-tactic-graphs
source: Secureworks Blog
date: 2022-12-13
fetch_date: 2025-10-04T01:20:16.675929
---

# Visualizing the Threat through Tactic Graphs™

[Skip to Main Content](#main-content)[Skip to Footer](#cmp-footer-a1fbb96a)

[Sophos completes Secureworks acquisition](https://www.sophos.com/en-us/press/press-releases/2025/02/sophos-completes-secureworks-acquisition)

* [Experiencing a Breach?](https://www.sophos.com/en-us/products/incident-response-services/emergency-response)
* Contact Us
* Support
* [Blog](/blog)
* English

[![logo](/-/media/images/logos/logo_new.svg?iar=0&hash=61254867B6545667A8E17DD1352849AF)](/ "Secureworks")

* Platform
* Services
* Solutions
* About
* Partners
* Resources

[Request Demo](/contact/request-demo-xdr)

Blog

# Visualizing the Threat through Tactic Graphs™

A new way to simplify how you use and analyze telemetry and alerts in Secureworks® Taegis™.

![Visualizing the Threat through Tactic Graphs](/-/media/images/insights/blog/2022/tactic-graphics/visualizing-the-threat-through-tactic-graphs-360x190.png?h=190&iar=0&w=360&hash=EB82763D0652B54BE54DA6F1DFB7BB04?io=transform:fit,width:4568,height:2568)

[Secureworks](/author/Secureworks)

December 12, 2022

Security analysts desperately need more streamlined ways of understanding potentially malicious activity in their enterprise environments across all telemetry sources. In fact, simplified correlation of diverse telemetry and alerts — most notably in the form of Tactic Graphs, part of [Secureworks® Taegis™ XDR’s](/sitecore/service/notfound.aspx?item=web%3a%7bDC8A7C4A-2DFE-42D9-BE11-15C94F3050B0%7d%40en) detection portfolio — can help you keep your organization safer and reduce staff burnout.

Allow me to explain.

## Tracking a Stealth Opponent

Once upon a time, cyberattacks were relatively simple smash-and-grabs. Threat actors didn’t worry much about how much “noise” they made — that is, how noticeable their presence might be to your security team — because they didn’t plan on sticking around long. Their objective was to get in, quickly propagate their attack as far as possible, and get out.

Today’s threat actors are far more sophisticated. Once they get past your perimeter, they want to covertly survey your environment to zero in on a target, such as a domain controller. That way, they can steal credentials that enable them time to continue probing and perusing your environment for vulnerabilities in your high-value assets without detection.

They can also utilize stolen credentials to execute an effective ransomware attack by mass-deploying a malicious payload across multiple systems.

To maintain this high level of stealth, an attack must be fairly complex. After all, it takes more careful work to get past a warehouse’s security system than it does to just break a window and steal whatever you can get your hands on before law enforcement arrives.

Complexity-enabled stealth, in other words, is what buys today’s attackers the time they need to compromise your organization’s vital systems before you can find them and neutralize them.

To keep your organization safe, you need to give your analysts tools that help them quickly detect complex attacks that have lots of disparate, subtle moving parts. This is exactly what Taegis XDR Tactic Graphs do.

## Alleviating Burnout

Threat detection isn’t the only reason to give your SOC team a better way to cope with stealth and complexity. Given how difficult it is to recruit and retain skilled cybersecurity professionals, you’ll also benefit from the way Tactic Graphs helps alleviate staff burnout.

Our [most recent survey results](https://view.secureworks.com/minimize-the-noise-of-cybersecurity-alerts/p/1) indicate that there’s been a remarkable 60% increase in SOC workloads over just the past year. Organizations also report a startling 71% burnout rate.

There are three underlying causes for both of these troubling statistics. One cause is obviously sheer volume. As our enterprise environments grow and threat activity intensifies, we’re generating a massive volume of telemetry — which, in turn, inundates analysts with a massive volume of alerts.

Next is the complexity of the attacks that analysts must discover buried like needles in this haystack of alert volume. Again, today’s attacker operates stealthily in your environment. So, your analysts must somehow piece together clues from a bit of telemetry here and an exceeded threshold there.

Finally, there is the ambiguity inherent in every piece of data the SOC receives. Analysts must constantly assess this data to answer all kinds of critical — and mentally challenging — questions, including:

* Is this alert meaningful? Or is it a false positive?
* If it’s a false positive, do we need to suppress it moving forward?
* If it’s a true positive, what should the next research and/or escalation step be?
* How does this alert relate to other alerts we’ve received?
* Does this combination of alerts suggest a specific type of active threat?
* If some specific type of active threat is suggested, is there a way to confirm our analysis?
* If our analysis is sufficiently confirmed, what is our next most important step to decisively neutralize the threat?

The relentless stress on analysts to answer these questions for a growing volume of telemetry and alerts in order to discover complex threats isn’t going to let up any time soon. That’s why it’s so important that we make life easier for analysts sooner, rather than later.

## Tactic Graphs: Reducing Risk and Stress

Tactic Graphs work by mapping a threat actor tactic to a collective set of conditions across IT assets — thereby converting all the telemetry and alerts associated with that set of conditions into a single, readily interpreted alert.

Consider, for example, a series of failed authentication attempts. Those attempts could create a real headache for an analyst. They could simply be a result of a user forgetting their credentials. Or perhaps some users’ credentials have been updated, but they’re using devices that still have the old credentials saved. The problem could even be a misconfigured bit of software.

To determine whether this is an Active Directory enumeration attack, what we really need to know is whether a *single host* is executing multiple failed attempts for *several different usernames*.

This is obviously something an analyst could investigate. But that investigation would require nontrivial time and effort. And if the analyst’s investigation reveals that the cause of the multiple failed authentication attempts is actually innocuous, we’ve sent them on a wild goose chase — when their time would have been much better spent hunting down a genuine threat.

Tactic Graphs preempt the need for such investigation by proactively correlating authentication failures with a tactic (in this case a set of failed authentication attempts detected by Taegis XDR) with two conditions: 1) five or more failed attempts from the same host and 2) those attempts being for more than one username.

If that correlation exists, then that Tactic Graph generates a single alert that has already identified a very specific type of malicious activity for the analyst. Which is certainly better than forcing an analyst to investigate 60 different pieces of security-related telemetry. And potentially come up empty. Or, worse yet, wake someone up at 2 a.m. for nothing.

## Discover for Yourself

That’s just one basic example of the powerful correlation rules you can create with Tactic Graphs in order to reduce alert volume, better detect complex multifaceted attacks, and relieve analysts of time-consuming detective work.

And with Taegis XDR, your Tactic Graph correlations can perform rules-based correlations across all of your telemetry — including endpoints, public clouds, networks and third-party monitoring tools.

As you leverage Tactic Graphs more broadly across more types of threats, you’ll dramatically decrease the time it takes for you to discover stealth activity in your environment and alleviate your SOC burnout problem.

That’s why I encourage you to learn more about Tactic Grap...