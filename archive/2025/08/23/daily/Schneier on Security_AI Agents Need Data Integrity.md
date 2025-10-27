---
title: AI Agents Need Data Integrity
url: https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html
source: Schneier on Security
date: 2025-08-23
fetch_date: 2025-10-07T00:50:27.655872
---

# AI Agents Need Data Integrity

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

## AI Agents Need Data Integrity

Think of the Web as a digital territory with its own social contract. In 2014, [Tim Berners-Lee](https://spectrum.ieee.org/the-fathers-of-the-internet-revolution-urge-todays-pioneers-to-reinvent-the-web) called for a [“Magna Carta for the Web”](https://www.theguardian.com/technology/2014/mar/12/online-magna-carta-berners-lee-web) to restore the balance of power between individuals and institutions. This mirrors the original charter’s purpose: ensuring that those who occupy a territory have a meaningful stake in its governance.

[Web 3.0](https://en.wikipedia.org/wiki/Web3)—the distributed, [decentralized Web](https://spectrum.ieee.org/tag/decentralized-web) of tomorrow—is finally poised to change the Internet’s dynamic by returning ownership to data creators. This will change many things about what’s often described as the “CIA triad” of [digital security](https://spectrum.ieee.org/tag/digital-security): confidentiality, integrity, and availability. Of those three features, data integrity will become of paramount importance.

When we have agency in digital spaces, we naturally maintain their integrity—protecting them from deterioration and shaping them with intention. But in territories controlled by distant platforms, where we’re merely temporary visitors, that connection frays. A disconnect emerges between those who benefit from data and those who bear the consequences of compromised integrity. Like homeowners who care deeply about maintaining the property they own, users in the Web 3.0 paradigm will become stewards of their personal digital spaces.

This will be critical in a world where [AI agents](https://spectrum.ieee.org/tag/ai-agents) don’t just answer our questions but act on our behalf. These agents may execute financial transactions, coordinate complex workflows, and autonomously operate critical infrastructure, making decisions that ripple through entire industries. As digital agents become more autonomous and interconnected, the question is no longer whether we will trust AI but what that trust is built upon. In the new age we’re entering, the foundation isn’t intelligence or efficiency—it’s integrity.

### What Is Data Integrity?

In information systems, integrity is the guarantee that data will not be modified without authorization, and that all transformations are verifiable throughout the data’s life cycle. While availability ensures that systems are running and confidentiality prevents unauthorized access, integrity focuses on whether information is accurate, unaltered, and consistent across systems and over time.

It’s a new idea. The undo button, which prevents accidental data loss, is an integrity feature. So is the reboot process, which returns a computer to a known good state. Checksums are an integrity feature; so are verifications of network transmission. Without integrity, security measures can backfire. Encrypting corrupted data just locks in errors. Systems that score high marks for availability but spread [misinformation](https://spectrum.ieee.org/tag/misinformation) just become [amplifiers](https://spectrum.ieee.org/tag/amplifiers) of risk.

All [IT systems](https://spectrum.ieee.org/tag/it-systems) require some form of data integrity, but the need for it is especially pronounced in two areas today. First: [Internet of Things](https://spectrum.ieee.org/tag/internet-of-things) devices interact directly with the physical world, so corrupted input or output can result in real-world harm. Second: AI systems are only as good as the integrity of the data they’re trained on, and the integrity of their decision-making processes. If that foundation is shaky, the results will be too.

Integrity manifests in four key areas. The first, *input integrity,* concerns the quality and authenticity of data entering a system. When this fails, consequences can be severe. In 2021, [Facebook’s global outage](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) was triggered by a single mistaken command—an input error missed by automated systems. Protecting input integrity requires robust [authentication](https://spectrum.ieee.org/tag/authentication) of data sources, cryptographic signing of sensor data, and diversity in input channels for cross-validation.

The second issue is *processing integrity,* which ensures that systems transform inputs into outputs correctly. In 2003, the [U.S.-Canada blackout](https://www.nerc.com/pa/rrm/ea/Documents/August_2003_Blackout_Final_Report.pdf) affected 55 million people when a control-room process failed to refresh properly, resulting in damages exceeding US $6 billion. Safeguarding processing integrity means formally verifying algorithms, cryptographically protecting models, and monitoring systems for anomalous behavior.

*Storage integrity* covers the correctness of information as it’s stored and communicated. In 2023, the Federal Aviation Administration was [forced to halt](https://www.thestack.technology/faa-outage-cause-notam-database-file-not-cyber/) all U.S. departing flights because of a corrupted database file. Addressing this risk requires cryptographic approaches that make any modification computationally infeasible without detection, distributed storage systems to prevent single points of failure, and rigorous backup procedures.

Finally, *contextual integrity* addresses the appropriate flow of information according to the norms of its larger context. It’s not enough for data to be accurate; it must also be used in ways that respect expectations and boundaries. For example, if a smart speaker listens in on casual family conversations and uses the data to build advertising profiles, that action would violate the expected boundaries of [data collection](https://spectrum.ieee.org/tag/data-collection). Preserving contextual integrity requires clear data-governance policies, principles that limit the use of data to its intended purposes, and mechanisms for enforcing information-flow constraints.

As AI systems increasingly make critical decisions with reduced human oversight, all these dimensions of integrity become critical.

### The Need for Integrity in Web 3.0

As the digital landscape has shifted from Web 1.0 to [Web 2.0](https://spectrum.ieee.org/tag/web-2-0) and now evolves toward Web 3.0, we’ve seen each era bring a different emphasis in the [CIA triad](https://www.fortinet.com/resources/cyberglossary/cia-triad) of confidentiality, integrity, and availability.

Returning to our home metaphor: When simply having shelter is what matters most, availability takes priority—the house must exist and be functional. Once that foundation is secure, confidentiality becomes important—you need locks on your doors to keep others out. Only after these basics are established do you begin to consider integrity, to ensure that what’s inside the house remains trustworthy, unaltered, and consistent...