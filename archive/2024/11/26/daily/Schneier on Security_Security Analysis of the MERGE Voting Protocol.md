---
title: Security Analysis of the MERGE Voting Protocol
url: https://www.schneier.com/blog/archives/2024/11/security-analysis-of-the-merge-voting-protocol.html
source: Schneier on Security
date: 2024-11-26
fetch_date: 2025-10-06T19:22:28.170115
---

# Security Analysis of the MERGE Voting Protocol

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

## Security Analysis of the MERGE Voting Protocol

Interesting analysis: [An Internet Voting System Fatally Flawed in Creative New Ways](https://arxiv.org/pdf/2411.11796).

> **Abstract:** The recently published “MERGE” protocol is designed to be used in the prototype CAC-vote system. The voting kiosk and protocol transmit votes over the internet and then transmit voter-verifiable paper ballots through the mail. In the MERGE protocol, the votes transmitted over the internet are used to tabulate the results and determine the winners, but audits and recounts use the paper ballots that arrive in time. The enunciated motivation for the protocol is to allow (electronic) votes from overseas military voters to be included in preliminary results before a (paper) ballot is received from the voter. MERGE contains interesting ideas that are not inherently unsound; but to make the system trustworthy—to apply the MERGE protocol—would require major changes to the laws, practices, and technical and logistical abilities of U.S. election jurisdictions. The gap between theory and practice is large and unbridgeable for the foreseeable future. Promoters of this research project at DARPA, the agency that sponsored the research, should acknowledge that MERGE is internet voting (election results rely on votes transmitted over the internet except in the event of a full hand count) and refrain from claiming that it could be a component of trustworthy elections without sweeping changes to election law and election administration throughout the U.S.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [DARPA](https://www.schneier.com/tag/darpa/), [protocols](https://www.schneier.com/tag/protocols/), [voting](https://www.schneier.com/tag/voting/)

[Posted on November 25, 2024 at 7:09 AM](https://www.schneier.com/blog/archives/2024/11/security-analysis-of-the-merge-voting-protocol.html) •
[7 Comments](https://www.schneier.com/blog/archives/2024/11/security-analysis-of-the-merge-voting-protocol.html#comments)

### Comments

wiredog •
[November 25, 2024 11:55 AM](https://www.schneier.com/blog/archives/2024/11/security-analysis-of-the-merge-voting-protocol.html/#comment-441829)

FYI, the “CAC” is the [DoD Common Access Card](https://www.cac.mil/Common-Access-Card/) which replaced the old military id and is used to access US DoD systems. IIRC it also has crypto certs on the card.

[Cybershow](https://cybershow.uk) •
[November 25, 2024 1:07 PM](https://www.schneier.com/blog/archives/2024/11/security-analysis-of-the-merge-voting-protocol.html/#comment-441830)

Neil Postman’s “Seven Questions To Ask About Technology”

Seven questions that we need to ask about any technology;

Q1: What is the problem for which this new technology is a solution?

Q2: Whose problem, is it? Who will benefit from the technology, and

Q3: What new problems might be created because we have solved the
problem?

Q4: Which people and what institutions might be most seriously harmed
by these technological solutions?

Q5: What changes in language are being enforced by new technologies?
What is being gained and what is being lost by such changes?

Q6: What sort of people and institutions acquire special economic and
political power because of the technological change?

Q7: What alternate uses might be made of a technology?

To my mind, “electronic voting” is a solution to a problem that
doesn’t exist. Arguments for it are based on edge-cases and baloney
about “saving money” (there’s plenty of money and it doesn’t need
“saving”). It’s a sci-fi type technology that feels like something
“cool from the future”, but with a moment of grown-up thought we
realise it offers no advantages but introduces many new security
risks. It is  [chindogu](https://cybershow.uk/blog/posts/chindogu)

Clive Robinson •
[November 25, 2024 8:03 PM](https://www.schneier.com/blog/archives/2024/11/security-analysis-of-the-merge-voting-protocol.html/#comment-441838)

@ Bruce, ALL,

With regards,

> “The gap between theory and practice is large and unbridgeable for the foreseeable future.”

It’s not foreseeable it’s indefinite or untill representative democracy in the way it is implemented currently is dead and buried.

Voting has three basic issues that have to be ensured if it is to be trusted,

1, Identifying a voter as valid.
2, Ensuring the voters vote is anonymous.
3, Ensuring the vote tally is accurate.

The first issue we’ve still not resolved and likely never will is the first one. Because it confuses to entirely separate things

1, The “physical” body.
2, The “information” identity.

In short you can not reliably prove you are who you claim to be.

All attempts so far either fail for the obvious reason, or are “turtles all the way down”.

If you want to think about the obvious reason in a more abstract way think about Cash or Cards in your pocket when you get stopped and searched. You can claim they are yours but the Cop can claim their not and confiscate them. Quite a few US States have laws enshrining this. The other side of this is drugs in a shared house as far as the law is concerned they are yours and you will do time.

Thus the very real, very problematic and very harmful,

“Disconnect between physical objects and information.”

It’s one of the fundamental reasons why not just voting, but the entire judicial system will be forever broken.

Oh and before people say “bio-metrics” that does not prove anything at all. Firstly because they are “physical” not “informational” and the “official record” can be changed at any time, thus Fred Smith, becomes Paul Jones at the swap of a piece of paper or the press of an enter key.

I’ll let others go through the other two, but you will find they all have several “disconnects” within them, or are “turtle s all the way down”.

The advantage of voting booth paper ballots is that the physical system has two properties that electronic systems do not,

1, They have a very high work factor for an attacker to falsify.

2, As physical objects they have an inordinate quantity of forensically verifiable chains of evidence.

Samuel Johnson •
[November 25, 2024 8:24 PM](https://www.schneier.com/blog/archives/2024/11/security-analysis-of-the-merge-voting-protocol.html/#comment-441839)

> Digital voting can be a pivotal component in evolving our democratic processes to reflect today’s technological advancements and voter needs.

Compared to having an educated and informed electorate it’s not of the slightest consequence.

Gert-Jan •
[November 26, 2024 6:52 AM](https://www.schneier.com/blog/archives/2024/11/security-analysis-of-the-merge-voting-protocol.html/#comment-441846)

@ Rontea

Where did you copy this promotion text? It’s one of the most unbalanced view on any issue.

{blockquote}
Embracing digital voting technologies could greatly enhance voter participation
{blockquote}

Yes, it could. It could also grealy reduce voter ...