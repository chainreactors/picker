---
title: Sandfly 1.4.4 – Mind your PIDness
url: https://sandflysecurity.com/blog/sandfly-1-4-4-mind-your-pidness
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:27:56.840076
---

# Sandfly 1.4.4 – Mind your PIDness

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 1.4.4 – Mind your PIDness

19 September 2018

Product Update

## Sandfly 1.4.4 Update

Sandfly 1.4.4 is now released. We have added some new sandflies and broken out an older one to be more granular.

Feature list:

* Sandflies to flag running processes under hidden subdirectories.
* Sandflies to detect malicious PID files broken out into separate components.
* Fixed a bug in the UI that was not allowing confirmation dialogs to show up without refreshing the screen.

## Mind your PIDness

Yeah, it’s a bad pun but we couldn’t resist. Sandfly has features to detect malicious entries under the Linux */var/run* directory targeting Process ID (PID) files. We have taken these checks and broken them out into separate components. This allows users to whitelist particular ones if they are causing a rare false alarm instead of needing to disable the entire set.

The */var/run* (or */run*) directory is targeted by malware on Linux. This directory is usually found across all Linux installs so it’s a handy place to do a variety of malicious things such as:

* Hide executable binaries disguised as a .pid file.
* Hold stolen data for later exfiltration off the host disguised as a .pid file.
* Hold configuration data for malware to help with persistence inside a .pid file.

PID files under */var/run* should usually contain the process number that is running (e.g. 1427, 3342, etc.). Sometimes we’ve seen PID files contain an extra line for a command that is running, but this is unusual. Mostly though if these files are holding data that isn’t a simple number value, is too large, or contains evidence it’s encrypted or a binary, then we want to alert you.

We now have the previous Sandfly PID check broken broken out into the following sandflies:

**sandfly\_file\_suspicious\_run\_pid\_binary** – Checks for PID files that are actually Linux executable binaries. You should never see this.

**sandfly\_file\_suspicious\_run\_pid\_encrypted** – Checks for PID files that appear to contain high entropy data indicating it may be encrypted. Malware can store stolen data in an encrypted form in PID files before data exfiltration.

**sandfly\_file\_suspicious\_run\_pid\_not\_integer** – Checks for PID files that are not simply an integer value. It is possible that a PID file may contain more than an integer, but it’s not common.

**sandfly\_file\_suspicious\_run\_pid\_too\_big** – Checks for PID files that are simply too large. Large PID files can be used to hold configuration or stolen data waiting for data exfiltration.

## Processes Running from a Hidden Sub-Directory

Next we added a new class of sandfly to flag processes that are running from a hidden sub-directory anywhere in their path. For instance:

*/var/tmp/.ICE-unix/*

This directory appears to be normal and is found on many Linux hosts by default. But any kind of process running from this or other hidden directories is extremely suspicious in general. *Why are you hiding the directory that is running a supposedly legitimate system process anyway?* This is a favorite tactic of malware, especially cryptominers that we’ve been seeing a lot lately. Also it’s used by various Linux worms and rootkits.

What it looks like:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux Hidden Subdirectory Malicious Process](https://www.datocms-assets.com/56687/1635216293-hidden-subdir-process.png?auto=format&dpr=2&q=60&w=920 "Linux Hidden Subdirectory Malicious Process")

We also added in a sandfly to help incident responders that will flag processes running from a hidden directory anywhere on the system. This sandfly has extremely low chance of false alarms in general, but we’ve see a couple isolated cases so we’ve made it an incident response sandfly to be run manually as a result. This is a good check to run as an incident responder to quickly catch any malware using this tactic.

The new sandfly names are the following:

**sandfly\_process\_running\_from\_hidden\_bin\_dir** – Flags processes running from a hidden directory under common system binary directories.

**sandfly\_process\_running\_from\_hidden\_lib\_dir** – Flags processes running from a hidden directory under common system library directories.

**sandfly\_process\_running\_from\_hidden\_usr\_dir** – Flags processes running from a hidden directory under /usr directories.

**sandfly\_process\_running\_from\_hidden\_dev\_dir** – Flags processes running from a hidden directory under /dev directories.

**sandfly\_process\_running\_from\_hidden\_system\_dir** – Flags processes running from a hidden directory under system directories like /boot, /lost+found.

**sandfly\_process\_running\_from\_hidden\_tmp\_dir** – Flags processes running from a hidden directory under tmp directories.

**sandfly\_process\_running\_from\_hidden\_etc\_dir** – Flags processes running from a hidden directory under /etc directories.

**sandfly\_process\_running\_from\_hidden\_var\_dir** – Flags processes running from a hidden directory under /var directories.

**sandfly\_process\_running\_from\_hidden\_root\_dir** – Flags processes running from a hidden directory under the top level / directory.

**sandfly\_process\_running\_from\_hidden\_dir\_anywhere** – Flags processes running from a hidden directory anywhere on the system.

## Upgrading Is Easy

We recommend you upgrade to the latest version to take advantage of these new features.

**Upgrading Sandfly is very easy with our included scripts.** Please read the instructions here:

[How to Upgrade Sandfly](https://docs.sandflysecurity.com/docs/upgrading-sandfly)

Thank you for using Sandfly.

---

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

© 2025 Sandfly Security, Ltd. [End User License Agreement](/end-user-license-agreement) & [Privacy Policy](/privacy-policy). This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply. Linux® is the registered trademark of Linus Torvalds in the U.S. and other countries.

[![Veracode Verified Standard](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fveracode-verified-standard-white.d24ef83e.png&w=384&q=75 "Veracode Verified Standard")](https://www.veracode.com/verified/directory/sandfly-security)