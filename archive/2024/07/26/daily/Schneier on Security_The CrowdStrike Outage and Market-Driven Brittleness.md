---
title: The CrowdStrike Outage and Market-Driven Brittleness
url: https://www.schneier.com/blog/archives/2024/07/the-crowdstrike-outage-and-market-driven-brittleness.html
source: Schneier on Security
date: 2024-07-26
fetch_date: 2025-10-06T17:45:03.714727
---

# The CrowdStrike Outage and Market-Driven Brittleness

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

## The CrowdStrike Outage and Market-Driven Brittleness

Friday’s massive internet outage, caused by a mid-sized tech company called CrowdStrike, disrupted major airlines, hospitals, and banks. Nearly [7,000 flights were canceled](https://www.independent.co.uk/tech/microsoft-outage-crowdstrike-global-it-flights-banks-windows-b2582964.html). It took down 911 systems and factories, courthouses, and television stations. Tallying the total cost will take time. The outage affected more than 8.5 million Windows computers, and the cost will surely be in the [billions of dollars](https://www.theguardian.com/technology/article/2024/jul/24/crowdstrike-outage-companies-cost)­—easily matching the most costly previous cyberattacks, such as [NotPetya](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/).

The catastrophe is yet another reminder of how brittle global internet infrastructure is. It’s complex, deeply interconnected, and filled with single points of failure. As we experienced last week, a single problem in a small piece of software can take large swaths of the internet and global economy offline.

The brittleness of modern society isn’t confined to tech. We can see it in many parts of our infrastructure, from [food](https://www.fda.gov/food/sampling-protect-food-supply/microbiological-surveillance-sampling-fy22-23-farm-inspections-and-sampling-leafy-greens-grown#_ftn2) to [electricity](https://energy.utexas.edu/research/ercot-blackout-2021), from [finance](https://insight.kellogg.northwestern.edu/article/what-went-wrong-at-aig) to [transportation](https://www.nytimes.com/2024/03/27/us/baltimore-bridge-collapse.html). This is often a result of globalization and consolidation, but not always. In information technology, brittleness also results from the fact that hundreds of companies, none of which you’ve heard of, each perform a small but essential role in keeping the internet running. CrowdStrike is one of those companies.

This brittleness is a result of market incentives. In enterprise computing—as opposed to personal computing—a company that provides computing infrastructure to enterprise networks is incentivized to be as integral as possible, to have as deep access into their customers’ networks as possible, and to run as leanly as possible.

Redundancies are unprofitable. Being slow and careful is unprofitable. Being less embedded in and less essential and having less access to the customers’ networks and machines is unprofitable—at least in the short term, by which these companies are measured. This is true for companies like CrowdStrike. It’s also true for CrowdStrike’s customers, who also didn’t have resilience, redundancy, or backup systems in place for failures such as this because they are also an expense that affects short-term profitability.

But brittleness is profitable only when everything is working. When a brittle system fails, it fails badly. The cost of failure to a company like CrowdStrike is a fraction of the cost to the global economy. And there will be a next CrowdStrike, and one after that. The market rewards short-term profit-maximizing systems, and doesn’t sufficiently penalize such companies for the impact their mistakes can have. ([Stock prices depress](https://www.marketwatch.com/story/crowdstrikes-stock-extends-declines-as-it-draws-a-downgrade-in-wake-of-incident-06b13093) only temporarily. Regulatory penalties are minor. Class-action lawsuits settle. Insurance blunts financial losses.) It’s not even clear that the information technology industry could exist in its current form if it had to take into account all the risks such brittleness causes.

The asymmetry of costs is largely due to our complex interdependency on so many systems and technologies, any one of which can cause major failures. Each piece of software depends on dozens of others, typically written by other engineering teams sometimes years earlier on the other side of the planet. Some software systems have not been properly designed to contain the damage caused by a bug or a hack of some key software dependency.

These failures can take many forms. The CrowdStrike failure was the result of a [buggy software update](https://www.youtube.com/watch?v=wAzEJxOo1ts). The bug [didn’t get caught](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/) in testing and was rolled out to CrowdStrike’s customers worldwide. Sometimes, failures are deliberate results of a cyberattack. Other failures are just random, the result of some [unforeseen dependency](https://aws.amazon.com/message/12721/) between [different pieces of critical software systems](https://www.zdnet.com/article/aws-suffers-third-outage-of-the-month/).

Imagine a house where the drywall, flooring, fireplace, and light fixtures are all made by companies that need continuous access and whose failures would cause the house to collapse. You’d never set foot in such a structure, yet that’s how software systems are built. It’s not that 100 percent of the system relies on each company all the time, but 100 percent of the system can fail if any one of them fails. But doing better is expensive and doesn’t immediately contribute to a company’s bottom line.

Economist Ronald Coase [famously described](https://www.economist.com/schools-brief/2017/07/28/coases-theory-of-the-firm) the nature of the firm­—any business­—as a collection of contracts. Each contract has a cost. Performing the same function in-house also has a cost. When the costs of maintaining the contract are lower than the cost of doing the thing in-house, then it makes sense to outsource: to another firm down the street or, in an era of cheap communication and coordination, to another firm on the other side of the planet. The problem is that both the financial and risk costs of outsourcing can be hidden—delayed in time and masked by complexity—and can lead to a false sense of security when companies are actually entangled by these invisible dependencies. The ability to outsource software services became easy a little over a decade ago, due to ubiquitous global network connectivity, cloud and software-as-a-service business models, and an increase in industry- and government-led certifications and box-checking exercises.

This market force has led to the current global interdependence of systems, far and wide beyond their industry and original scope. It’s why flying planes depends on software that has nothing to do with the avionics. It’s why, in our connected internet-of-things world, we can imagine a similar bad software update resulting in our cars not starting one morning or our refrigerators failing.

This is not something we can dismantle overnight. We have built a society based on complex technology that we’re utterly dependent on, with no reliable way to manage that technology. Compare the internet with ecological systems. Bot...