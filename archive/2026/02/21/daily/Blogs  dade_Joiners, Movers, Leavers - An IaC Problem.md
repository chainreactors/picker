---
title: Joiners, Movers, Leavers - An IaC Problem
url: https://0xda.de/blog/2026/02/joiners-movers-leavers-an-iac-problem/
source: Blogs  dade
date: 2026-02-21
fetch_date: 2026-02-22T04:10:07.794044
---

# Joiners, Movers, Leavers - An IaC Problem

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2026/02/joiners-movers-leavers-an-iac-problem/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

5 minutes

# [Joiners, Movers, Leavers - An IaC Problem](https://0xda.de/blog/2026/02/joiners-movers-leavers-an-iac-problem/)

I’m a huge proponent of infrastructure as code. What I mean when I say this is mostly Terraform – and for an important reason (and when I say Terraform, I mostly mean OpenTofu, for another important reason). One of the things that I most value about infrastructure as code is its declarative nature. You define what you want, maybe you define the order that resources depend on each other to help Terraform apply things in the correct order, and then you get what you asked for. No defining a series of bash commands wrapped in yaml to execute to achieve the outcome you want. Just say what you want, and get it (unless it’s the AWS WAF Terraform provider, in which case just give up).

While I obviously appreciate terraform to manage things like cloud infrastructure, I think its value also goes far beyond that. I think an organization can get a great deal of value adopting IaC practices for things like managing GitHub [organizations](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/enterprise_organization), [repos](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/repository), [teams](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team), [branch protection rules](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/branch_protection), etc. Or for managing Okta [groups](https://registry.terraform.io/providers/okta/okta/latest/docs/resources/group), [apps](https://registry.terraform.io/providers/okta/okta/latest/docs/resources/app_saml), [group rules](https://registry.terraform.io/providers/okta/okta/latest/docs/resources/group_rule), [authenticators](https://registry.terraform.io/providers/okta/okta/latest/docs/resources/authenticator), [network zones](https://registry.terraform.io/providers/okta/okta/latest/docs/resources/network_zone), etc. Or for managing Cloudflare zero trust [lists](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_list), [device posture integrations](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_device_posture_integration), [device posture rules](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_device_posture_rule), etc.

But I left out many notable resources in these examples. I didn’t mention assigning people to GitHub teams. I didn’t mention assigning people to Okta apps or groups. In fact, I mostly avoid assigning people to anything in my terraform. This is due to the fundamental nature of a person’s relationship with an organization, and how I find that to be at odds with Infra-as-Code paradigms.

Would it be awesome to be able to just point to the spot in the repo where all the users who have access to any given application or repository are? Absolutely. Would it be awesome to get automatic drift detection and correction so that if someone is inappropriately assigned to an application without going through the proper channels, the problem automatically gets corrected? You betcha. Would it be great if a user is offboarded and we leave a bunch of code lying around referencing their user? Wait…

Therein lies my biggest problem with managing users in Terraform. A user’s lifecycle is fundamentally unlike any of the other resources that I mentioned. A user’s lifecycle is broken up into 3 major events: joining, moving, and leaving. A user joins the company and needs to be given access to things relevant to their role. A user gets promoted or maybe changes teams, and they need to have access revoked to old things, and new access given for their new role. A user wins the lottery and leaves the organization, their access needs to be revoked. These are core lifecycle events that enterprise identity tools have started to understand and work into their capabilities.

While we could absolutely manage all of this in Terraform, it creates manual operations whenever these lifecycle events happen. I’m sure with extremely careful construction of your terraform, you could minimize the amount of work needed, but it would still be manual work. I can already envision the schemes we could concoct with groups that are assigned to apps (which I do use Terraform for) and a bunch of group rules that create all sorts of automated group assignment behaviors for users (oh but those assignments aren’t in Terraform, so your source of truth is still wrong, lol).

We want automation to handle core user lifecycle events. Ideally this automation is rooted in the HRIS system, such that IT doesn’t have to lift a finger when a user is offboarded. The user is offboarded in the HRIS system and the IDP automatically disables their account. When the IDP disables their account, SCIM integrations reach out to core services and disable their accounts there. For cases where SCIM is not available, we shame our vendors who have the audacity to charge us $100k a year for “enterprise” software but who have not yet figured out that important little detail that users sometimes leave companies.

Another area that is gaining traction, and which terraform gets in the way of, is just-in-time access provisioning / escalation. I find it weird to say this, because I’m pretty sure Intel had a 10-year-old version of this when I started working there over a decade ago, but many players in the market are now building out solutions to allow users to request time-bound access (or escalated access) to resources, and allow those resource owners to approve the requests without the need for intervention by IT. This JIT access is fantastic because it allows users to maintain the least amount of necessary privilege as their default experience, and then escalate only when needed, and with peer review.

Again, we could absolutely achieve this with Terraform. First we teach John from accounts payable how to create an SSH key, install git, clone a repo, make a change, don’t forget the pre-commit hooks, John, commit the change, push the change, deal with the merge conflict, quit his job, buy a farm, breathe a deep sigh of relief as he realizes he can finally live the rest of his life in peace. All so he could access the billing information for our AWS account. Oh hey, John, when you’re done with your access, don’t forget to make the revert commit, that way you don’t retain the high level of access. A revert commit is like hitting the undo button except for nerds. Well, you see, Git is like a tree that contains a series of patches. No not like a nicotine patch, like a… you know what, John, I’ll take care of it.

“But dade, we could automate that with CI and a custom pull request syntax that specifies how long to keep the change for” – you, an absolute fool, a mad lad, an emperor among nerds, probably.

I’m not saying that these things *can’t* be solved with Terraform, just that they probably shouldn’t be. I think that user access to resources is probably the one place where we should just leave Terraform out of it.

---

Share this page

`https://0xda.de/blog/2026/02/joiners-movers-leavers-an-iac-problem/`

[security](https://0xda.de/tags/security)[infrastructure](https://0xda.de/tags/infrastructure)

1011 Words
...