---
title: When Backups Open Backdoors: Accessing Sensitive Cloud Data via "Synology Active Backup for Microsoft 365"
url: https://modzero.com/en/blog/when-backups-open-backdoors-synology-active-backup-m365/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-29
fetch_date: 2025-10-06T22:53:53.902571
---

# When Backups Open Backdoors: Accessing Sensitive Cloud Data via "Synology Active Backup for Microsoft 365"

[![](/img/logo.svg)](https://modzero.com/en/)

[ ]

* [ ]
  Services
  [Services](/en/services/)
  + [Application Pentesting](/en/services/#application-pentesting)
  + [Cloud Pentesting](/en/services/#cloud-pentesting)
  + [Red Teaming](/en/services/#red-teaming)
  + [Hardware/Software Review](/en/services/#hardware-review)
  + [Design & Concept Advisory](/en/services/#design-concept-advisory)
* [ ]
  Company
  [Company](/en/company/)
  + [About](/en/company/#about)
  + [Jobs](/en/company/#jobs)
* [Blog](/en/blog/)
* [Advisories](/en/advisories/)

[DE](/de/)[Contact](https://modzero.com/en/contact/)

[⟵ Blog](https://modzero.com/en/blog/)

disclosure

# When Backups Open Backdoors: Accessing Sensitive Cloud Data via "Synology Active Backup for Microsoft 365"

June 27, 2025 — by Leonid Hartmann

## TL;DR

We discovered a leaked credential that allowed anyone unauthorized access to all Microsoft tenants of organizations that use Synology’s [“Active Backup for Microsoft 365”](https://www.synology.com/en-global/dsm/feature/active_backup_office365) (ABM). This flaw could be leveraged by malicious actors to obtain potentially sensitive information â such as all messages in Microsoft Teams channels. It was reported to Synology and tracked as [CVE-2025-4679](https://www.cve.org/CVERecord?id=CVE-2025-4679).

This blog post contains the full technical walk-through and discovery of the vulnerability, its impact, and our experience during the responsible disclosure process with Synology.

The standalone disclosure report is available on our [advisory page](https://modzero.com/en/advisories/mz-25-02-synology-active-backup-m365/) and potential Indicators of Compromise (IoC) are provided [in a dedicated section](/en/blog/when-backups-open-backdoors-synology-active-backup-m365/#indicators-of-compromise) further below.

---

## Background

During a red-team engagement against a customer’s Microsoft Entra tenant and Azure infrastructure we came across an application named [“Synology Active Backup for M365”](https://www.synology.com/en-global/dsm/feature/active_backup_office365).

The application had broad permissions â such as read access to all groups and Microsoft Teams channel messages â making it an ideal target to obtain information that may be useful for further attacks (i.e. credential abuse or [social engineering](https://www.microsoft.com/en-us/microsoft-365-life-hacks/privacy-and-safety/what-is-social-engineering)).

To analyze it, we created our own lab environment consisting of a [Microsoft sandbox tenant](https://developer.microsoft.com/en-us/microsoft-365/dev-program) and the ABM add-on installed within Synology’s [DiskStation Manager](https://www.synology.com/en-us/dsm) (DSM) operating system. For research purposes it is not necessary to have a Synology NAS appliance, as the entire OS can be [virtualized via Docker](https://github.com/vdsm/virtual-dsm).
We also built some tools along the way, which can be helpful to reverse engineer [DSM add-on packages](https://archive.synology.com/download/Package/). We will share them for other security researchers on [our GitHub](https://github.com/modzero/) soon.

### About ABM

Synology is best known for its network-attached storage (NAS) solutions, marketed as backup servers for private or business use. “Active Backup for Microsoft 365” (ABM) is their free software add-on developed for the DSM. It offers integration with Microsoft services, such as OneDrive, SharePoint, Exchange Online and Microsoft Teams, to perform automated backups. With over 1.2 million installations, the add-on sees broad adoption among organizations that are transitioning to cloud-based workloads.

![](/static/synology-abm365/abm365-package-center-addon.png)

#### Synology DSM Package Center â ABM add-on page

#### Setup

After installing ABM, the user is guided through a setup wizard, which is designed to link the NAS instance to their respective Microsoft tenant. This is the most interesting aspect of the [setup process](https://kb.synology.com/en-uk/DSM/tutorial/Quick_Start_Active_Backup_for_Microsoft_365), as it facilitates the access to an organization’s data in the cloud.

High-level setup procedure:

1. **Login & Consent** â The wizard sends the user to the Microsoft login portal where they sign in, and are prompted to grant admin consent for ABM’s requested permissions within the tenant.

![](/static/synology-abm365/abm365-entra-app-admin-consent.png)

#### ABM permissions admin consent prompt for the organization

2. **Handoff** â After confirmation, an OAuth login through the ABM application is performed. Microsoft hands off the user and their resulting authorization details (the auth code) to a Synology middleware service, which then forwards everything back to the user’s NAS instance.

![](/static/synology-abm365/synooauth-middleware-nas-redirect.png)

#### Synology middleware ("SynoOauth") â NAS instance redirect prompt [redacted for display]

3. **Finalization** â The ABM add-on on the NAS exchanges the user’s authorization details for a Microsoft Graph API scoped access token at the organization’s Microsoft OAuth endpoint to finalize the setup.

![](/static/synology-abm365/abm365-setup-overview.png)

#### General ABM setup overview

*Sidenote: The user is also required to activate the add-on with their Synology account after installation as part of the setup procedure, for which further details are skipped in this post.*

## Technical Concepts & Context

Before diving into the details of the vulnerability, let’s take a step back and cover a few basics related to the [authentication concepts of Microsoft Entra](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).

### Identities, Applications, and Permissions

The ABM add-on leverages the [Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview), allowing companies like Synology to publish Software-as-a-Service (SaaS) applications that users access through their Microsoft account. These accounts are managed by the dedicated Microsoft tenant of an organization, which is a trusted cloud instance of [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id). Each tenant stores and manages all organizational data across Microsoft 365 services, like Microsoft Teams.

ABM is published as a *multi-tenant application* by the Synology tenant, enabling other organizations to “install” it within their own. The application properties, such as authentication settings, are globally defined by the “app registration” of the publishing tenant. Whereas each consuming tenant maintains a local representation known as a “service principal” â determining the application’s effective permissions within that tenant.

![](/static/synology-abm365/entra-abm-multitenant-app-concept.png)

#### Simplified Microsoft Entra multi-tenant application concept (ABM)

Permissions granted through consent â either by individual users or the organization’s administrators â determine the actions an application can perform against APIs such as [Microsoft Graph](https://learn.microsoft.com/en-us/graph/traverse-the-graph). These permissions can be of type *delegated* (signed-in user required) or *application* (may act independently). Therefore, authenticating as either a user or the service principal of an application grants access to the tenant’s protected data.
ABM is configured to request both types of permissions, including privileged access such as reading [**details of every group**](https://graphpermissions.merill.net/permission/Group.Read.All?tabs=apiv1%2CadministrativeUnit1) (`Group.Read.All`) as well as [**all Microsoft Teams channel messages**](https://graphpermissions.merill.net/permission/ChannelMessage.Read.All?tabs=apiv1%2CaiInteraction1) (`ChannelMessage.Read.All`) via application permissions. As such, when ABM is setup for the first time, an organization’s administrator must grant tho...