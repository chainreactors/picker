---
title: Sandfly 1.6.1 – Host ID Updates and Other Fixes
url: https://sandflysecurity.com/blog/sandfly-1-6-1-host-id-updates-and-other-fixes
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:27:46.841723
---

# Sandfly 1.6.1 – Host ID Updates and Other Fixes

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 1.6.1 – Host ID Updates and Other Fixes

07 February 2019

Product Update

Sandfly 1.6.1 is released and has some

## Install Simplified

The [install procedure for Sandfly has been greatly simplified](https://docs.sandflysecurity.com/docs/server-install). You now need to run one script on the server and enter some basic information and it will complete the cryptographic key generation and write out configuration files. Server install is now an under 5 minute process (with most of that time waiting to generate the cryptographic keys).

## Host ID Changes to Work with Load Balancers

When Sandfly adds a host, it was using a SHA256 fingerprint of the system’s SSH key. This is the same procedure all SSH clients use to detect if the remote host is identical to what you used to previously connect to it.

Sandfly however uses it also to know a host it is connecting to is known even if it changes its IP address between scans. In this way, you can be in a very dynamic environment but Sandfly will always be able to know what hosts are there and update the results correctly. Basically, we track hosts by SSH fingerprint, not by IP address or even hostname.

This works great except if a host happens to be using the same key as other hosts on the network. Re-using SSH keys for hosts is never advised, but it can happen under a couple cases:

1. A user makes an image of a system that has already generated a SSH host key and that image simply has the same key re-used over and over again each time they spin up a new host off that image (not advised).
2. The systems are located behind a load balancer and that load balancer is presenting identical SSH keys when you connect to it before it farms out the connection to systems behind it.

In the above cases, Sandfly would see the same SSH key and update that system as if it were the same host. This meant that systems with duplicated host keys for whatever reason would stomp on each other’s results when Sandfly ran each time.

Now we have changed this behavior. We still use the SSH key fingerprint, but also combine it with other host attributes when we login to create a unique ID that will be different even if you are behind load balancers, or re-imaging systems.

## Host ID Auto-Update

With the above explanation out of the way, this update takes your old Host IDs and updates them to the new method automatically. When you do this update we will do this behind the scenes, but with some caveats:

1. The Host ID will be updated, but not any results we have for the old Host ID. In other words, if you have pass and fail results from your hosts in the system they will still be there. However they will be tied to the legacy Host ID. This means you may see duplicate results as new sandfly results come in with the new Host ID. These duplicates will remain until you delete them manually (for alarm events), or they expire out naturally for the pass or error events.
2. If you see double alarms, this is again due to the above. **We do not delete or modify your old alerts to ensure they are not damaged.** You will need to simply delete them and they will be generated again with the new Host ID if they are still present.

This should all be transparent to you when you re-start after the update. If you have any problems, please contact us for support.

## Process Caching

We have added caching for process checks that gives them almost a 50% speed boost. They were already fast, but now have become even faster and use less CPU on the remote hosts when running.

## Syslog Hostname Fixed

Customers reported that the syslog entries being generated were returning the Docker container name (a hex value) instead of the Sandfly server name into their SIEM and syslog management systems. We have fixed this so you will see the Sandfly server hostname now as part of the syslog entry.

## Syslog UTC Time Format

All time values internally for Sandfly have always been in UTC time to avoid timezone issues and give consistent time logging. We have now updated the syslog generation code to also UTC timestamp all syslog entries we generate. SIEM/Syslog aggregators will now see this UTC timestamp as part of each syslog entry they receive.

## Enhanced OS Attributes Permissions Fixed

In Sandfly 1.6.0 we introduced enhanced attributes for Operating Systems that gives a lot more details about the host, hardware, and CPU. On some systems there were permission problems causing this to fail. We have fixed this so that if permission problems happen, we simply don’t collect this data and you get the standard attributes only. This is not common, but can happen on some hosts depending on how they are configured.

## Documentation Updated

We have updated the documentation to include a list of threats detected by Sandfly, and all they keywords that can be returned in the results. This can be useful to customers building out parsing for their SIEM products and want to know what values are available:

[Linux Threats Detected](https://docs.sandflysecurity.com/docs/sandfly-threats-detected)

[Linux Forensic Keywords](https://docs.sandflysecurity.com/docs/sandfly-forensic-keyword-list)

## Important: Updating Sandfly

Due to the changes to the install scripts, you must pull the latest changes from GitHub or things will break. The newest scripts update your keys and config data to a new format for future use.

Please read the upgrade information, paying attention to running this command from inside the sandfly-setup directory.

`git pull origin`

[Sandfly Update Instructions](https://docs.sandflysecurity.com/docs/upgrading-sandfly)

## Thanks

This update is preparing for some more features in the future. Thanks for using Sandfly.

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