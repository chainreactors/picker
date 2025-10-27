---
title: What to Do With Products Without SSO?
url: https://zeltser.com/products-without-sso/
source: Lenny Zeltser
date: 2024-09-17
fetch_date: 2025-10-06T18:25:07.681528
---

# What to Do With Products Without SSO?

☰

# [Lenny Zeltser](https://zeltser.com/)

Close

* [Information Security](https://zeltser.com/information-security/)
* [Technology](https://zeltser.com/technology/)
* [Malicious Software](https://zeltser.com/malicious-software/)

* [Cloud Services Research](https://zeltser.com/cloud-services-research/)
* [Consulting Research](https://zeltser.com/consulting-research/)
* [Toy Chest](https://zeltser.com/toy-chest/)

* [Blog](https://zeltser.com/blog/)

* [About](https://zeltser.com/about/)
* [Contact](https://zeltser.com/contact/)

* [Search](http://)

Close

# What to Do With Products Without SSO?

![](https://cdn.zeltser.com/wp-content/uploads/2024/09/funnel.jpg)

What should you do with the SaaS products that your organization had to purchase without Single Sign-On (SSO)? And to get this out of the way: Vendors that lock SSO behind enterprise-only plans [do a disservice to their customers](/witholding-sso/). No wonder the US government’s [Secure by Design Pledge](https://www.cisa.gov/securebydesign/pledge) expects vendors to offer SSO in baseline product versions.

But this article isn’t complaining about SSO-taxing vendors–it’s more pragmatic than that. Let’s start with the role that SSO plays in modern defense architecture, and then cover how to implement similar security measures without such a centralized mechanism.

## **Controlled Entry Points as Defense Tactics**

First, why is SSO so important to security and IT professionals? It acts as a chokepoint. Defenders have historically used choke points to control attackers. Numerous examples include:

* [Battle of Thermopylae](https://en.wikipedia.org/wiki/Battle_of_Thermopylae) (480 BCE): A small Greek force defended the narrow Thermopylae pass against the much larger Persian army. The location allowed the Greeks to inflict significant losses.
* [Battle of Stirling Bridge](https://en.wikipedia.org/wiki/Battle_of_Stirling_Bridge) (1297): The Scots positioned themselves near the narrow Stirling Bridge, which allowed them to overwhelm the English forces as they crossed the bridge in small groups.
* [Battle of Morgarten](https://en.wikipedia.org/wiki/Battle_of_Morgarten) (1315): The Swiss Confederates ambushed the Austrian forces in a narrow pass between a lake and the mountains. The advantageous terrain allowed the Swiss to achieve a decisive victory.

Just as historical defenders leveraged choke points to concentrate their resources and control the flow of attackers, SSO centralizes authentication, creating a single, controlled entry point for accessing multiple systems.

## **SSO as a Control Funnel**

Centralizing authentication through an SSO provider allows efficient enforcement of security measures, account management, access monitoring, and attack surface reduction:

* **Enforce security measures:** Enable multi-factor authentication (MFA) to help prevent attacks such as [those that affected Snowflake customers in May 2024](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion). Control which authentication factors are available, enforce password complexity, configure session duration, and manage credential resets.
* **Manage user accounts:** Automate user provisioning and deprovisioning via SSO-provided [SCIM](https://scim.cloud/) capabilities. Automatically assign roles according to personnel needs. Gain visibility into product utilization for licensing requirements.
* **Monitor access:** Use the SSO provider’s anomaly detection to flag suspicious login attempts, such as those that occur from unexpected locations or malicious infrastructure. Direct logs to a centralized location ([SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management)) for analysis, correlation, and forensics.
* **Reduce the attack surface:** Expose a single, fortified login mechanism provided by the SSO vendor, reducing reliance on individual SaaS vendors' security practices.

These benefits don’t apply to the SaaS products onboarded without standards-based SSO, [putting defenders at a significant disadvantage](/defenders-advantage/).

## **Compensating for the Lack of SSO**

To define baseline SSO expectations organizations should:

1. Formally require SSO (and SCIM) for all SaaS purchases.
2. Communicate that policy to internal purchasers and vendors.
3. Educate purchasers to negotiate SSO capabilities when buying and renewing products.
4. Create a process for approving exceptions when SSO is unavailable.

When granting an exception to buy an SaaS product without SSO support, organizations must compensate for the loss of security measures by [assigning responsibilities may be assigned](/distribute-cybersecurity-tasks/) to IT, cybersecurity teams, or business units. Define expectations for:

* **User account settings:** Acceptable 2FA factors, password requirements, session duration expectations, etc.
* **Provisioning and Deprovisioning**: Steps for creating user accounts with the right privileges and disabling the accounts when employees leave or no longer need the product.
* **Security Monitoring:** Detecting attacks and configuration weaknesses, reviewing in-app security logs, or directing events to the organization’s SIEM.
* **Centralized Oversight:** Determining whether the appropriate security responsibilities for securing the product are being followed.

Organizations should recognize that they take on these burdens when purchasing SaaS products without SSO. If they cannot commit to these security measures, they accept the increased risk that the SaaS product will be compromised or look for an alternative product that offers SSO.

The absence of SSO in SaaS products poses significant security challenges. Organizations can tackle them by enforcing SSO policies, negotiating for SSO capabilities, and implementing compensating security measures. By taking these steps, you can maintain robust security even without centralized access control, ensuring your SaaS environment remains secure and manageable.

Updated September 16, 2024

 Lenny Zeltser

### Did you like this?

Follow me for more of the good stuff.

* [Twitter

  Twitter](https://twitter.com/lennyzeltser)
* [RSS

  RSS Feed](https://zeltser.com/feed/)
* [LinkedIn

  LinkedIn](https://www.linkedin.com/in/lennyzeltser)

### About the Author

I transform ideas into outcomes, building on my 25 years of experience in cybersecurity. As the CISO at Axonius, I lead the security program to earn customers' trust. I'm also a Faculty Fellow at SANS Institute, where I author and deliver training for incident responders. The variety of cybersecurity roles I've held, and the expertise I’ve accumulated allow me to create practical solutions that drive business growth.

[Learn more](https://zeltser.com/about)

### More on

* [Information Security](https://zeltser.com/information-security)
* [Technology](https://zeltser.com/technology)

Share

* [Twitter](https://twitter.com/share?url=https://zeltser.com/products-without-sso/)
* [Facebook](https://www.facebook.com/sharer.php?u=https://zeltser.com/products-without-sso/)
* [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://zeltser.com/products-without-sso/)
* Email

Copyright © 1995-2025 Lenny Zeltser. All rights reserved.