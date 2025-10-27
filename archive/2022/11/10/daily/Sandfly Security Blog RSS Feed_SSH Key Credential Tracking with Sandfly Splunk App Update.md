---
title: SSH Key Credential Tracking with Sandfly Splunk App Update
url: https://www.sandflysecurity.com/blog/ssh-key-credential-tracking-with-sandfly-splunk-app-update
source: Sandfly Security Blog RSS Feed
date: 2022-11-10
fetch_date: 2025-10-03T22:13:47.301445
---

# SSH Key Credential Tracking with Sandfly Splunk App Update

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# SSH Key Credential Tracking with Sandfly Splunk App Update

09 November 2022

[Sandfly's Splunk App](https://splunkbase.com/apps/#/product/all/author/sandfly) has been updated and now has separate inputs to accept our new [SSH Key Hunter](https://www.sandflysecurity.com/platform/ssh-credential-security/) data feed. SSH Hunter agentlessly collects SSH public key data to track how they can be used for logins across your Linux systems. We are now making that data available to all Splunk users.

Collecting SSH public key data allows Sandfly to build an in-depth view of your SSH credential posture without jeopardizing security by giving access to secret key data during the process.

The SSH key data Sandfly collects can be used in a large number of ways such as the following:

* Finding and tracking compromised SSH credentials and users.
* Seeing what SSH keys are used on what systems.
* Tracking and identifying keys by date first and last seen.
* Detecting changes to *authorized\_keys* files including creation and modification times to help with incident response.
* Finding key types, duplicate keys, obsolete keys, and more.

The SSH Hunter collects this data agentlessly across all Linux systems watched by Sandfly. This includes not only typical server installations, but also IoT and embedded Linux appliances where traditional agent-based Linux EDR coverage has no visibility.

## Tracking SSH Credentials for Compromise

During a breach, the ability to track compromised SSH credentials eliminates a lot of wasted time. Specifically, it allows incident response teams to rapidly contain and remediate breaches where a stolen key is used to initiate lateral movement by attackers.

Below we show a sample Splunk dashboard included with the App. The built-in dashboards and sample reports can be quickly taken by SOC teams to incorporate into their own visuals and workflow inside Splunk.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Tracking SSH Keys with Sandfly's Splunk Dashboard](https://www.datocms-assets.com/56687/1667956487-splunk-ssh-key-summary.png?auto=format&dpr=2&q=60&w=920 "Tracking SSH Keys with Sandfly's Splunk Dashboard")

Below we see an example where we isolate all keys seen. Clicking on any key will break out individual results about the key and what hosts it's appeared on over time.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH Key Tracking Last Seen Date](https://www.datocms-assets.com/56687/1667956989-splunk-ssh-key-last-seen-report.png?auto=format&dpr=2&q=60&w=920 "SSH Key Tracking Last Seen Date")

## SSH Key Forensics for Incident Response on Linux

The SSH public key data we collect contains extensive information to allow Splunk to query on values such as dates, key types, users, hosts, key cryptographic hashes, and much more.

Splunk users can use this data to build custom reports and alerts such as:

* Alerts on new keys seen anywhere.
* Alerts on keys showing up for certain hosts or users (e.g. root).
* Alerts on banned or old keys returning from the grave on any host.
* Queries for known compromised keys and where they've been seen over time.
* Reports on key usage statistics, age of keys, and what they are being used for and where.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH Key Forensics on Linux](https://www.datocms-assets.com/56687/1667956697-splunk-ssh-key-details.png?auto=format&dpr=2&q=60&w=920 "SSH Key Forensics on Linux")

We also have detailed views to build queries for SSH keys inside Splunk. For example, all key fields below in the detailed forensic view can be used to build searches.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH Key Detailed Forensic Data for Linux](https://www.datocms-assets.com/56687/1667956803-splunk-ssh-key-forensic-data.png?auto=format&dpr=2&q=60&w=920 "SSH Key Detailed Forensic Data for Linux")

## Monitoring SSH Authorized Key Files

Finally, we make available file creation and modification times to detect if an SSH *authorized\_keys* file has been created or altered. The data shows specific users and full paths to the file for rapid identification and response.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![SSH authorized_keys Modified Detailed View](https://www.datocms-assets.com/56687/1667956927-splunk-ssh-authorized_keys-created-past-7-days-detail-listing.png?auto=format&dpr=2&q=60&w=920 "SSH authorized_keys Modified Detailed View")

## SSH Key Tracking Agentlessly and Fast

Tracking SSH keys on Linux is an important task and is not found in traditional Linux EDR tools. Sandfly's agentless security platform not only collects this data instantly, but processes it to make it immediately useful for Splunk users hunting for compromised SSH credentials.

Licensed customers of Sandfly can use our [Splunk App for free](https://splunkbase.com/apps/#/product/all/author/sandfly). Please [contact us](https://www.sandflysecurity.com/contact-us/) if you have any further questions or would like a demo of how Sandfly's SSH Hunter can help.

---

Post Tags:

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

© 2025 Sandfly Security, Ltd. [End User License Agreement](/end-user-license-agreement) & [Privacy Policy](/privacy-policy). This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply. Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

[![Veracode Verified Standard](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fveracode-verified-standard-white.d24ef83e.png&w=384&q=75 "Veracode Verified Standard")](https://www.veracode.com/verified/directory/sandfly-security)