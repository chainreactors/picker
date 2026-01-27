---
title: Binary Ninja Enterprise 2.0 Released
url: https://binary.ninja/2026/01/26/enterprise-2.0.html
source: Binary Ninja
date: 2026-01-26
fetch_date: 2026-01-27T03:37:27.098644
---

# Binary Ninja Enterprise 2.0 Released

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Binary Ninja [5.2, codename Io, is out](/2025/11/13/binary-ninja-5.2-io.html) and includes bitfield support, containers, hexagon, and much more.

# Binary Ninja Blog

## Binary Ninja Enterprise 2.0 Released

* [Alexander Taylor](https://github.com/fuzyll)
* 2026-01-26
* [announcements](/tag/announcements), [enterprise](/tag/enterprise)

![Ultimate >](/blog/images/enterprise-2.0/ultimate.jpg)

Binary Ninja Enterprise 2.0 is here, and itâs a **free upgrade for all active customers**! While we plan on supporting the current Enterprise 1.2.x branch for our next few Binary Ninja releases to give customers time to migrate, Enterprise 2.0 already comes with a significant upside: An on-premises version of our new [WARP service](https://warp.binary.ninja/). To get started, customers with active support can find the server installers in the [customer portal](https://portal.binary.ninja), or have them sent via email using the [license recovery](https://binary.ninja/renew) system. (Note: A v1.x `manage_server` *will not* update itself directly to v2.0. We wanted to make sure your current servers wouldnât update unexpectedly.)

* [Highlights](#highlights)
* [WARP: On-Prem](#warp-on-prem)
* [Server Deployment](#server-deployment)
  + [Client Installers](#client-installers)
* [Upgrade Path](#upgrade-path)
* [Get Started Today!](#get-started-today)

## Highlights

If you just want the highlights, here they are:

* An on-prem WARP service is now included at no extra charge for current and future Enterprise customers.
* API updates in v2.0 allow new client features like searching for files across projects, with more features on the way.
* Rootless Podman deployments on RHEL now have first-class support.
* Major infrastructure refresh should make deployment and maintenance easier.
* All dependencies and containers have been updated to their latest versions.

## WARP: On-Prem

Since Binary Ninja 4.2, weâve been talking a lot about WARP, our new function identification solution. See [the WARP deep dive](/2025/08/22/warp.html) for more details on what WARP does, and the [Binary Ninja 5.2 release notes](/2025/11/13/binary-ninja-5.2-io.html#warp-server) where we mentioned the release of the [public service](https://warp.binary.ninja/). Enterprise 2.0 brings that service fully on-prem.

The Enterprise server now acts as an OAuth2 provider, so downstream services (like WARP) can trust it directly. The Enterprise service stack now, by default, deploys a copy of the WARP server and configures OAuth2 between Enterprise and WARP. This means your Enterprise server account is also your WARP server account. After generating an API key and configuring WARP inside Binary Ninja, youâll have the same signature matching functionality, but in your own network.

![WARP UI](/blog/images/warp/ui.png)

## Server Deployment

This release also completely changes the way the Enterprise server is deployed. Previously, if you made modifications to the base installation, you had to pass those options as CLI flags to every command that needed them. Now, `manage_server install` writes a `config.env` file alongside the generated `docker-compose.yml` file that captures any non-default options you set. If you ever need to see all options, the new `manage_server env` command will print them all out for you (and can be piped to a file if youâd like).

This change also means that the `update` command is no longer aliased to the `install` command. You will `install` once, then `update` afterward. Some customers have wanted a better way to check for updates as well, so weâve added an `--only-update-self` option that will only update `manage_server` as a stop-gap on our way to providing a better experience through our customer portal.

### Client Installers

One final change to be aware of is that we no longer include the client installers inside the server image. This has the added benefits of:

1. Updated images are now *significantly* smaller, making updates faster to perform (the client installers were larger than the entire server image).
2. Server admins can now choose which installers they want to provide and can have multiple different versions of installers available for download (even dev builds!).

Server admins will need to upload client installers themselves. To support this, we have updated the [customer portal](https://portal.binary.ninja) so that anyone with an Enterprise server can also download Binary Ninja Ultimate stable and dev installers.

![Client Installers](/blog/images/enterprise-2.0/installer-downloads.png)

## Upgrade Path

Due to the abundance of changes in this release, upgrading from Enterprise 1.x to 2.0 **requires a full backup and restore of server data**. We understand this might be painful for some customers, so weâre committed to supporting Enterprise 1.x for the next couple of releases of Binary Ninja to give time for upgrades to happen. You can also run Enterprise 1.x and 2.0 side-by-side, as long as some of their deployment details (like the port number) are different.

Please see our [updated documentation](https://docs.enterprise.binary.ninja/upgrade.html#version-specific-considerations) for more details on how to upgrade your server.

To prevent accidental, undesired upgrades, you must manually download the new `manage_server` binary for Enterprise 2.0 from the [customer portal](https://portal.binary.ninja) to perform the upgrade. An existing 1.x `manage_server` binary is not capable of performing the upgrade by itself.

## Get Started Today!

If you are an existing Binary Ninja Enteprise customer, grab the Enterprise 2.0 package and installers from the [customer portal](https://portal.binary.ninja) or via [license recovery](https://binary.ninja/recover). This update is available at **no extra charge** to all active Enterprise customers.

If you arenât a current Binary Ninja Enterprise customer, now is a fantastic time to become one! Please see the [features page](https://binary.ninja/enterprise) for more information and contact us to schedule a demo or obtain a quote. Weâd love to have you on board!

And, finally, regardless of whether youâre a customer or not, please donât hesitate to contact us:

* Enterprise-specific questions and issues should be directed to `[[email protected]](/cdn-cgi/l/email-protection)`.
* Technical support questions can be directed to `[[email protected]](/cdn-cgi/l/email-protection)`.
* And, if youâre truly not sure, `[[email protected]](/cdn-cgi/l/email-protection)` will get you going to the right place.

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2026 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#81e3e8efe0f3f8efe8efebe0c1f7e4e2f5eef3b2b4afe2eeec)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)