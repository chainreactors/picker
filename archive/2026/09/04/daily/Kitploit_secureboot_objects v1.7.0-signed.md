---
title: secureboot_objects v1.7.0-signed
url: https://kitploit.com/en/posts/github-microsoft-secureboot_objects-v170-signed
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:09.520284
---

# secureboot_objects v1.7.0-signed

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/8812/eea98606e6cebea58534b1a1a2a724214ee2e6df27d764647cd1fb2243773ab0.png)

New releaseSep 4, 2026

# secureboot\_objects v1.7.0-signed

Microsoft's curated repository of secure boot objects (KeK, Db, Dbx) for firmware and runtime, enabling transparent revocation updates and platform-level boot security.

Share

# Secure Boot Objects

This repository is used to hold the secure boot objects recommended by Microsoft.

For documentation visit our [Wiki](https://github.com/microsoft/secureboot_objects/wiki)!

## Versioning

This repository follows [semantic versioning](https://semver.org/) `<major>.<minor>.<revision>`,
which is a versioning scheme that conveys meaning about the underlying changes.

### Version Components

* **Major**: Indicates an incompatible change between firmware secure boot versions.
  This is a significant change that may require updates to the firmware or other
  components. (Today there is only version 1)
* **Minor**: Represents additional revocations, usually the result of a security incident.
  These changes should be documented in the release notes to inform users about the security updates.
* **Revision**: Generally a non-breaking change, such as script updates or minor improvements.
  These changes do not affect the compatibility of the firmware secure boot.

### Release Forms

There are two forms of release that should generally stay in lock step:

* **Unsigned firmware-based secure boot payloads**: Denoted as (`<major>.<minor>.<revision>`). These payloads
  are intended for use in firmware and are not signed.
* **Signed runtime-based secure boot payloads**: Denoted as (`<major>.<minor>.<revision>-signed`). These
  payloads are signed and intended for use at runtime, providing an additional layer of security.

In a situation where a minor release is needed to be made for one release and not the other. Both will be
moved forward and the release notes will indicate no change was made.

By following this versioning scheme, we ensure that users can easily understand the nature of the changes in
each release and maintain compatibility with their systems.

## Transparency

By Keeping the contents of the KeK, Db, and Dbx in a human readable form in
this repository, it enables developers to easily review the contents and make
changes as needed. This also enables an easy way for the KeK, Db, and (mainly)
the Dbx to be updated transparently and then consumed by any platform!

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact `[[email protected]](/cdn-cgi/l/email-protection) <mailto:[[email protected]](/cdn-cgi/l/email-protection)>`\_. with any additional questions or comments.

## License

The files in this repository are licensed under the [BSD-2-Clause-Patent](https://github.com/microsoft/secureboot_objects/blob/main/License.txt) license.

[Read more](/en/tools/github/microsoft/secureboot_objects?expand=1)

## Categories

[Embedded Systems Security](/en/categories/embedded-systems-security)[Configuration Auditing](/en/categories/configuration-auditing)[Security Virtualization](/en/categories/security-virtualization)[Hardware Security](/en/categories/hardware-security)[Supply Chain Security](/en/categories/supply-chain-security)[Firmware Analysis](/en/categories/firmware-analysis)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories