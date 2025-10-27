---
title: A few thoughts on CVE
url: https://shostack.org/blog/thoughts-on-cve/
source: Shostack & Friends Blog
date: 2025-04-16
fetch_date: 2025-10-06T22:07:13.906503
---

# A few thoughts on CVE

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. A few thoughts on CVE

Shostack + Friends Blog

# A few thoughts on CVE

Thoughts on the CVE funding crisis
![The CVE logo](/images/blog/img/2025/cve-416w.jpeg)

CVE funding is apparently ~~not~~ being renewed. (See third
April 16 update). I haven’t been operationally involved for a long
time and I’m sorry for what the team is going through. I’m not
alone in having strong feelings, and I want to talk about some of
the original use cases that informed us as we set up the
system. (You might also enjoy my thoughts on [25 Years of CVE](https://shostack.org/blog/25-years-of-cve/) for some context.) Those included comparing between vulnerability
posts. It’s a lot of work to decide if two vulns are the same.
Tagging both with a name was an important use case in 1997,
and one that I got to revisit around 2010 when I was doing work to
understand how malware got into PCs. Most of the attacks in
exploit kits were not CVE-labeled. So deciding what they were was
hours per vuln, with a high failure rate, versus minutes when they
had a CVE assigned.

CVE achieved public good status exceptionally quickly, in part
because of support from thoughtful leaders like Tony
Sager while he was at NSA. Finding support from outside the
government was, as I recall, harder because MITRE is
Congressionally chartered and has difficulty taking money from
anyone but the US Government.

There are other used cases, and I want to mention them because I
was talking in private to friends, and they weren’t aware of
these. All vendor names are used as examples.

* Did redhat fix this python bug or do we need to find a patch is
  way easier with cves.* Did Apple fix this OpenSSL bug after getting version locked to
    OpenSSL .9.8?
  * Having a name lets you discuss “did Microsoft fix this yet?” and
    if there’s a tool that tests it, you can cross-check the bug, the
    proof of concept, and the patch.
  * Having an authoritative public timetable, including issuance, helped
    everyone understand when a vendor was slow-rolling a fix.

I’m hopeful that the CNAs will pick up the load, and that they either have reserved blocks or can coordinate among themselves to assign blocks for use in a way that helps with the core mission of vuln identifiers as this gets sorted.

## Additional commentary

I expect that this post will be updated, and so I’ll include some date headers.

### April 16

There are now three alternatives, and CISA funding. Apparently, I
chose a bad time to go to sleep. The ENISA one is
issuing EUVD identifiers which won’t pass validators (The lead in
is 4 letters, the id strings are 5).

I feel a need to emphasize that CVEs are names, not risk
scores. “The NVD performs enrichment on CVEs that have been
published to the CVE List.” That includes CVSS, which neither NVD
nor CVSS describe as a risk system. You can assess someone’s
technical nuance by how much they claim that CVE includes risk
assessment, but be kind, it’s a fast moving story.

#### April 16 (afternoon)

The most important part of CVE is not the unique number, but the
funding and expertise to run a credible program. The unique
number was the center of what Dave Mann called a “concordance,”
and I believe this is subtle but crucial: The value of CVE is not
as a database, but as a stable way to cross-reference between
databases and other tools. Dave and I have had many conversations
about books having an ISBN, a UPC code, a Dewey number and a
Library of Congress number. They serve
different goals, and are managed by different groups. The number
needs to be accompanied by enough information to durably
differentiate it, and each bit of information carries a cost, as
does handling objections or controversy.

#### April 16 (third update)

A lot of people are asking what they should do. The short term answer is
remain calm, and possibly consider where your organization is
dependant on this or other unfunded resources, such as small open
source projects, and fund them. Funding CVE was complicated by MITRE
only being able to accept American Government money. (At least when I
was involved.) But that doesn’t apply to most of the open source
projects you depend on. In the short term, setting up funding for
those resources is a wise choice.

Reuters is reporting that [funding is extended for 11
months](https://www.reuters.com/world/us/us-agency-extends-support-last-minute-cyber-vulnerability-database-2025-04-16/), which is great, and I am thankful to the folks at
CISA who made it happen. But we can’t count on it. The administration has
been both mercurial and apparently careless in breaking contracts, impounding
funds that had been authorized and appropriated, sometimes even
clawing them back or threatening to do so after they’ve been
paid. It’s bad enough that I described it as a [constitutional crisis](https://shostack.org/blog/the-first-constitutional-crisis-of-2025/) a
month ago. The current reprive doesn’t mean things are back to
normal, or will remain normal for the next 11 months.

### April 17

I’m hearing from people in a position to know that there’s good
support from leadership at DHS and CISA, but there were some
contractual renewal complexities. The problem was compounded
because the USG doesn’t like talking about contracts until they’re
signed. Todd Beardsley [reports
similarly](https://www.runzero.com/blog/cve-marches-on/) from yesterday’s board meeting.

### Some other useful data points include:

* CVE records will continue to be available at [github](https://github.com/CVEProject). Brian Krebs [says](https://infosec.exchange/%40briankrebs/114344203019345999) the API that CNAs use to get CVEs will remain available.
* Josh Bressers has set up a discord, [Extended Vulnerability Community](https://discord.gg/gSCrXxMuPx).
* Jen Easterly has a good [post](https://www.linkedin.com/posts/jen-easterly_quick-note-a-potential-shutdown-activity-7318021583191617538-xfa_?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAABXB8Bi8nzcKtYJy26uPQJtELAN8sgDB4) on Linkedin about the
  problems CVE solves and what’ll happen without it.
* [VulnCheck commits to providing
  CVEs for researchers](https://vulncheck.com/press/vulncheck-to-support-cve-program). Anthony Bettini was there at the start, and is a stalwart.
* April 16: Bleeping Computer reports CISA has [announced emergency funding](https://www.bleepingcomputer.com/news/security/cisa-extends-funding-to-ensure-no-lapse-in-critical-cve-services/).
* April 17: I’m now tracking four alternative systems:
  + [CVE Foundation](https://www.thecvefoundation.org/) where Kent Landfield is an officer. Kent has been part of CVE from the very early days.
  + ENISA has launched an [EUVD](https://euvd.enisa.europa.eu/) which is issuing EUVDs.
  + [GCVE.EU](https://gcve.eu/) might be run by [circl](https://circl.lu/), but it’s unclear.
  + Steve Springett has called for [an OWASP community effort](https://owasp.org/blog/2025/04/17/owasp-global-vulnerability-intelligence.html).
  + I won’t be adding any more anonymous efforts here.
* April 16: Bob Rudis has released a tone-perfect [Crawl](https://mastodon.social/%40hrbrmstr/114347122882714891).

[Critical update: fixed the Josh Bressers discord link...