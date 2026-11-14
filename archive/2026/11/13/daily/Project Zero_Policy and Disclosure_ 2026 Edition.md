---
title: Policy and Disclosure: 2026 Edition
url: https://projectzero.google/2026/11/disclosure-policy.html
source: Project Zero
date: 2026-11-13
fetch_date: 2026-11-14T08:20:18.757117
---

# Policy and Disclosure: 2026 Edition

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# Policy and Disclosure: 2026 Edition

[2026-Nov-13](/2026/11/disclosure-policy.html "Permalink to this post")
Natalie Silvanovich

Since 2021, Project Zero has followed a â90 + 30â vulnerability disclosure policy, allowing vendors up to 90 days to remediate a vulnerability plus an extra 30 days âsoak timeâ for patch rollout. Our goal was to encourage faster patching and give vendors time to deliver patches to users. The advent of AI-assisted vulnerability discovery and exploitation has changed the threat landscape such that the vulnerability remediation timeline encouraged by our disclosure policy is clearly insufficient.

LLMs have increased the speed at which attackers can find and exploit vulnerabilities, alongside the risk that multiple parties, including malicious ones, discover the same bug. A vulnerability reported today presents a much higher immediate risk to users than one reported last year. In this new environment, it is crucial that vendors move towards remediating vulnerabilities faster.

LLMs have also decreased the time it takes for attackers to reverse engineer and exploit a vulnerability based on a patch, to the extent that zero patch-to-exploitation time is a reasonable, though imperfect, model of attacker behavior. Patch soak time is no longer meaningful in a world where attackers can almost immediately determine bug details from a patch, and can put users at risk by creating a false sense of secrecy. âPatch gapâ is the time between a fix being released for a security vulnerability and the user installing the relevant update. It is equally crucial that vendors reduce patch gap, either by reducing patch rollout time or using other strategies to protect users while remediation is in progress.

LLMs have also increased the volume of vulnerabilities that Project Zero reports. We are finding several vulnerabilities a week in targets where we once found a few vulnerabilities a year. Aspects of our policy that require vendor negotiation or agreement, including determining whether a bug is fixed and whether grace period applies, are quickly becoming unmanageable.

Today, we are announcing a new vulnerability disclosure policy, created with the following goals in mind:

* Encourage faster vulnerability remediation
* Encourage vendors to reduce âpatch gapâ
* Allow for the policy to be automated by both Project Zero and vendors

## Our new policy: âFull Xâ

*Vulnerabilities will be disclosed X days after they are reported to the vendor.*

Starting today, our policy is âFull 90â, i.e. vulnerabilities will be disclosed 90 days after they are reported to the vendor.

**On February 2, 2027, we will move to a âFull 60â policy where vulnerabilities are disclosed after 60 days.**

**On January 3, 2028, we will move to a âFull 30â policy where vulnerabilities are disclosed after 30 days.**

We are also removing most âspecial casesâ from our disclosure policy, including grace period and variant policy. The only exceptions to our new policy are:

* **Vulnerabilities actively exploited in the wild** -- ITW vulnerabilities will be handled according to Googleâs [application security vulnerability disclosure policy](https://about.google/company-info/appsecurity/)
* **Public vulnerabilities** -- Project Zero may make details of a vulnerability public, at our discretion, if the details have already been made public by others
* **Vendor request** -- We will make vulnerability details public if the vendor we reported it to requests it

### Why reduce remediation time gradually?

Project Zero solicited feedback from the vendors we report the most vulnerabilities to as a part of developing this new policy. An overarching concern was that immediately changing the policy could harm users by making unfixed vulnerabilities available to attackers while vendors are in the process of improving their remediation processes and technology. While the benefits of delaying disclosure are declining due to the increased probability that attackers will discover a vulnerability during the embargo period, we still feel there are benefits in the short term.

In addition, vendors mentioned two more subtle concerns. One was that an overly-aggressive disclosure policy would encourage fixing bugs reported under the new policy with more priority, even if they are less severe than other reported vulnerabilities. The other was that immediately enforcing a policy that some vendors arenât equipped to meet might lead to a state where vendors accept that they cannot fix bugs within the deadline and donât attempt to.

We decided on a policy that encourages vendors to improve remediation time on a schedule that is challenging but realistic, with the hope that this will lead to vendors broadly improving their remediation processes and infrastructure in a way that eventually enables them to fix all reported vulnerabilities quickly.

### What about severity?

While our analysis isnât always perfect, Project Zero only reports vulnerabilities with substantial severity and demonstrated security impact in our tracker. That said, we donât feel severity is an effective metric for making disclosure decisions, especially in the current environment. A vulnerabilityâs severity does not affect the likelihood that it will be discovered by attackers, only its impact on users.

When vendors determine severity and use it to prioritize bug fixes, they are making decisions about what risks they are willing to expose their users to, and it is reasonable to accept the risk of low-severity bugs, like unexploitable null pointer crashes or minor info leaks in a lot of circumstances. But this doesnât change the availability of these vulnerabilities to attackers, and we want our policy to reflect this reality.

Itâs also important to acknowledge that Project Zero holds itself to high standards with regards to the reproducibility, readability, reachability and reported security impact of the vulnerabilities we report. This policy assumes bugs reports are of this quality, and it is reasonable for vendors to treat low quality-bug reports differently.

### What about hardware?

We encourage all vendors to consider how they would respond to imminent disclosure of a serious vulnerability, including non-patch [strategies](/2026/10/emergency-patching.html), as there is no guarantee that defenders will be the first to find a bug. That said, Project Zero has occasionally granted [exceptions](/vulnerability-disclosure-faq.html#exceptions) to our policy on rare occasions, including Spectre and Meltdown, and will continue to do so in the future.

### Are you really not going to check whether bugs are fixed?

The question of whether a bug is fixed for the purposes of our policy has always been challenging and somewhat unresolved, particularly with regards to code that is not shipped directly to users and not publicly available. It is not unusual for Project Zero to communicate with vendors multiple times for each bug report to come to an agreement on whether a vulnerability is fixed. As more vendors experiment with vulnerability remediation strategies that are not patching like temporarily disabling code paths, we expect this to become even more complex.

We still plan to track whether bugs are fixed and communicate if they are not, however, this will not be a decision point in our policy. This will enable us to share technical details of how users are protected without needing to make a binary judgeme...