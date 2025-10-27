---
title: Sandfly 4.5.0 - Powerful New Expression Syntax
url: https://sandflysecurity.com/blog/sandfly-4-5-0-powerful-new-expression-syntax
source: Sandfly Security Blog RSS Feed
date: 2023-06-12
fetch_date: 2025-10-04T11:45:19.325425
---

# Sandfly 4.5.0 - Powerful New Expression Syntax

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 4.5.0 - Powerful New Expression Syntax

11 June 2023

Product Update

Sandfly 4.5.0 has received a massive capability upgrade with a new expression language syntax. This new upgrade greatly expands how our agentless threat hunting and incident response modules can be used to protect Linux.

Sandfly 4.5.0 upgrade includes:

* New expression language syntax allows rapid and wider creation of custom threat hunting sandflies for customers.
* All built-in modules have been reviewed and depth of coverage for Linux threats broadened.
* We have expanded our CPU support to cover IBM POWER8, 9 and 10 processors.

This update has important changes for customers using **existing custom sandflies**. Please see the section on upgrading custom sandfliesfor more details.

## Sandfly Expression Language Syntax

Today, we introduce a new expression language syntax based on the [expr package in Go](https://expr.medv.io/docs/Language-Definition). The expression language syntax allows customers to more rapidly create new modules using any of the Linux forensic parameters collected by Sandfly.

For instance, if you wanted to do a simple search for a process SHA512 hash in the past you would do the following:

`...
"process": {
 "hash": {
 "sha512": [
 "sha512_hash_here",
 "another_hash_here"
 ]
 },
...`

Under the new expression language syntax the form changes to:

`...
"rules": [
 "process.hash.sha512 matches '^(sha512_hash_here|another_hash_here)$'"
 ]
...`

The new syntax allows combining of multiple data fields with conventional logic operators (*and*, *or*, *not*), plus comparisons of integer and floating point fields (<, >, ==, !=). Additionally, it includes full regex support and the ability to use logic operators for negation, conditional checks, and much more.

Further, you can search inside forensic array data such as SSH keys found by Sandfly, user details, file and process attributes, and other critical Linux forensic data. For example, below we are searching for any SSH key using older *ssh-rsa* values as part of a security policy sweep:

`...
"rules": [
 "any(user.ssh.authorized_keys.data, {.type matches '^ssh-rsa$'})"
 ]
...`

## Expression Language Syntax

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Custom Sandfly Expression Language Syntax](https://www.datocms-assets.com/56687/1686518885-customer-sandfly-expr-syntax.png?auto=format&dpr=2&q=60&w=920 "Custom Sandfly Expression Language Syntax")

The expression language syntax is covered in our online documentation:

[Custom Sandfly Creation](https://support.sandflysecurity.com/support/solutions/articles/72000604474)

[Custom Sandfly Options and Keywords](https://support.sandflysecurity.com/support/solutions/articles/72000604319)

Sandfly forensic keyword names and types are defined here:

[Sandfly Forensic Keywords](https://support.sandflysecurity.com/support/solutions/folders/72000044384)

## Expanded Coverage for Linux Threats

During the expression syntax upgrade we took the time to expand many Linux threat hunting modules internally. We are now able to spot more kinds of attacks against Linux and modules have been upgraded to find wider threat variants.

## IMPORTANT: Old Custom Sandflies Disabled

While the new syntax is very powerful, it is **not backwards compatible** with the old format sandflies you may have created. There is no direct path to upgrade these older modules so during the upgrade they will be disabled. If you have created custom sandflies, you will need to upgrade them individually.

**Licensed customers can contact customer support and we will do the conversion for you free of charge.** Please contact us and we will instruct you on exporting your existing custom modules and how to send them to us so we can port them for you quickly.

## IBM POWER Processor Support

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![IBM Summit Supercomputer Runs Power9 CPUs - Photo Credit IBM](https://www.datocms-assets.com/56687/1686520520-the_summit_supercomputer.jpg?auto=format&dpr=2&q=60&w=920 "IBM Summit Supercomputer Runs Power9 CPUs - Photo Credit IBM")

For this upgrade we also added in support for POWER8, 9 and 10 processors. Customers running on IBM hardware using Linux now have full Sandfly support. Sandfly is committed to having the broadest and deepest security coverage of Linux on the market. We support more modern, legacy, and embedded systems than any other company. Sandfly works on the following CPUs today with no modifications:

* Intel
* AMD
* Arm
* MIPS
* POWER

Customers running Sandfly across multiple architectures and distributions receive identical Linux security coverage:

* Process, file, directory, user, and log file attack detection.
* Security policy sweeps.
* Advanced attacker and stealth rootkit detection.
* SSH key tracking and threat detection.
* User password auditing.
* Rapid agentless threat hunting.

Sandfly supports modern and legacy systems up to a decade+ old both on-prem and in the cloud. We also run on many embedded devices, including difficult to monitor network edge gear often targeted by advanced adversaries. Sandfly gives extensive coverage without the risk of deploying endpoint agents on Linux.

## New Read Only and Scan Only User Roles

We have added in new roles for users to restrict access to read only and scan only modes. This allows a SIEM user that can only read results without ability to initiate any other actions. Likewise, a SOAR tool can be given access to initiate threat scans without the ability to modify or see unrelated data from the API.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Read-only user.](https://www.datocms-assets.com/56687/1686527854-user-read-api-role.png?auto=format&dpr=2&q=60&w=920 "Read-only user.")

## Get a Free License Today

All Sandfly users get the upgraded and expanded expression language syntax modules. Licensed customers get the ability to create custom modules on the fly for rapid and immediate threat hunting.

[Get Sandfly](https://sandflysecurity.com/get-sandfly/)

## Upgrading Sandfly

Sandfly 4.5.0 represents a significant upgrade with powerful new expression syntax that we will be leveraging for exciting new features we will be announcing shortly. All customers are encouraged to upgrade. We are here to help with any questions.

Customers wishing to upgrade can follow the instructions here:

[Upgrading Sandfly](https://support.sandflysecurity.com/support/solutions/articles/72000078711-upgrading-sandfly)

If you have any questions, please [reach out to us](https://www.sandflysecurity.com/contact-us/).

Thank you for using Sandfly.

---

Post Tags:

[Product Update](/blog/tag/product-update)[News](/blog/tag/news)

Share this post:

[← Return to Blog](/blog)

---

#### Contact Us

---

+64 3 3792313[4 Ash Street Christchurch, New Zealand 8011](https://goo.gl/maps/9cFto1o6GNa9RK6S9)

#### Connect With Us

---

#### Product Navigation

---

* [Threat Detection](/platform/threat-detection)
* [SSH Key Monitoring](/platform/ssh-key-monitoring)
* [Password Auditing](/platform/password-auditing)
* [Drift Detection](/platform/drift-detection)
* [Incident Response](/platform/incident-response)
* [Requirements & Installation](/resources/requirements-installation)

#### General Navigation

---

* [Our Company](/about-us/our-company)
* [Partners](/about-us/partner)
* [Under Attack?](/under-attack)
* [Contact Us](/contact-us)
* [Let’s Connect](/request-a-meeting)
* [Manage My Subscription](https://billing.sandflysecurity.com/p/login/28o7tJe2vbLNfEA9AA)

#### Sign-up For Updates

---

First Name

First Name

Last Name

Last Name

Email

Email

Subscribe

© 2025 Sandfly Security, Ltd. ...