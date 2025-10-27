---
title: Beware the Hidden Risk in Your Entra Environment
url: https://thehackernews.com/2025/06/beware-hidden-risk-in-your-entra.html
source: The Hacker News
date: 2025-06-26
fetch_date: 2025-10-06T22:55:59.343558
---

# Beware the Hidden Risk in Your Entra Environment

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Beware the Hidden Risk in Your Entra Environment](https://thehackernews.com/2025/06/beware-hidden-risk-in-your-entra.html)

**Jun 25, 2025**The Hacker NewsIdentity Management / Enterprise Security

[![Guest Account Risk in Entra Environment](data:image/png;base64... "Guest Account Risk in Entra Environment")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisPtqswn7Gf_uPltaHNuUt2ZnBgBf6kQy5NtkJQjEJnVvHlPlgrgTSp3qfr0Gct9qwbPiqVLQziWHC3UEriyT-gIpeKCclfacYrJlUAg9gr9TVPPiY6lLFu9uZWqkAsMVIVZjHWQYly5F-4oMQQUt7yn0gmyxdtxz2JDQ8lgC2kvlE7QcWiOMzRrPyBCLp/s790-rw-e365/guest.jpg)

*If you invite guest users into your Entra ID tenant, you may be opening yourself up to a surprising risk.*

A gap in access control in Microsoft Entra's subscription handling is allowing guest users to create and transfer subscriptions into the tenant they are invited into, while maintaining full ownership of them.

All the guest user needs are the permissions to create subscriptions in their home tenant, and an invitation as a guest user into an external tenant. Once inside, the guest user can create subscriptions in their home tenant, transfer them into the external tenant, and retain full ownership rights. This stealthy privilege escalation tactic allows a guest user to gain a privileged foothold in an environment where they should only have limited access.

Many organizations treat guest accounts as low-risk based on their temporary, limited access, but this behavior, which works as designed, opens the door to known attack paths and lateral movement within the resource tenant. It can allow a threat actor to achieve unauthorized reconnaissance and persistence in the defender's Entra ID, and advance privilege escalation in certain scenarios.

Typical threat models and best practices don't account for an unprivileged guest creating their own subscription within your tenant, so this risk may not only exist outside your organization's controls; it may be off your security team's radar as well.

## **How to Compromise Your Entra ID Tenant with a Guest User Account**

Guest-made subscription footholds exploit the fact that Microsoft's billing permissions (Enterprise Agreement or Microsoft Customer Agreement) are scoped at the billing account, not the Entra directory. Most security teams think about Azure permissions as either Entra Directory Roles (such as Global Administrator) or Azure RBAC Roles (such as Owner). But there is another set of permissions that get overlooked: Billing Roles.

While Entra Directory and Azure RBAC Roles focus on managing permissions around identities and access to resources, Billing roles operate at the billing account level, which exists outside the well-understood Azure tenant authentication and authorization boundaries. A user with the right billing role can spin up or transfer subscriptions from their home tenant to gain control inside a target tenant, and a security team that is strictly auditing Entra Directory roles won't gain visibility of these subscriptions in a standard Entra permission review.

When a B2B guest user is invited to a resource tenant, they access the tenant via federation from their home tenant. This is a cost-saving measure, the trade-off being that your tenant cannot enforce auth controls like MFA. As such, defenders usually try to limit the privileges and access of guests as they are inherently less securable. However, if the guest has a valid billing role in their home tenant, they can use it to become a subscription owner inside Azure.

This is also true for guest users who exist in pay-as-you-go Azure tenants that an attacker could spin up in just a few minutes. And, by default, any user, including guests, can invite external users into the directory. This means an attacker could leverage a compromised account to invite in a user with the correct billing permissions into your environment.

## **How an Attacker can Gain Elevated Access Using an Unprivileged Entra Guest Account:**

1. Attacker gets control of a user with a billing role that can create subscriptions / owner of a subscription in a tenant, either by:
   1. Creating their own Entra tenant using an Azure free trial (the user they signed up with will be a Billing Account owner)
   2. Or, by compromising an existing user in a tenant who already has a privileged billing role / subscription ownership
2. Attacker gets an invite to become a guest user in their target Entra tenant. By default, any user or guest can invite a guest into the tenant.
3. Attacker logs into the Azure Portal, goes into their own home directory – which they completely control.
4. Attacker navigates to Subscriptions > Add +.
5. Attacker switches to the "Advanced" tab and sets the defender's directory as the target directory.
6. Attacker creates subscription. No subscription will appear in the attacker tenant. Instead, the subscription appears in the defender tenant, under the root management group.
7. Attacker will automatically be assigned the RBAC Role of "Owner" for this subscription.

## **Real-World Risk: What a Restless Guest Can Do with a New Subscription**

Once an attacker has a subscription with Owner permissions within another organization's tenant, they can use that access to perform actions that would normally be blocked by their limited role. These include:

* **Listing Root Management Group Administrators -** In many tenant configurations, guest users have zero permissions to list other users within a tenant; however, following a guest subscription attack, that visibility becomes possible. The guest Owner can view the "Access Control" role assignments on the subscription they've created. Any administrators assigned at the root management group level of the tenant will be inherited and will appear in the role assignments view of the subscription, exposing a list of high-value privileged accounts that are ideal targets for follow-on attacks and social engineering.
* **Weakening the Default Azure Policy Tied to the Subscription -** By default, all subs...