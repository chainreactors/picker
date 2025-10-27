---
title: The CMMC Countdown, Part 3
url: https://www.secjuice.com/cmmc-part-3/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-26
fetch_date: 2025-10-06T19:22:23.869553
---

# The CMMC Countdown, Part 3

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[INFOSEC](/tag/infosec/)

# The CMMC Countdown: The Action Plan, Part 3

Continue your CMMC action plan with this high-level review of the five-point controls required to get a conditional certificate.

* [![Miguel A. Calles](/content/images/size/w100/2024/02/Miguel-portrait-2019-cropped.jpg)](/author/serverlessciso/)

#### [Miguel A. Calles](/author/serverlessciso/)

Nov 24, 2024
• 6 min read

![The CMMC Countdown: The Action Plan, Part 3](/content/images/size/w2000/2024/11/turkeys-doing-Cirque-du-Soleil-with-locks-and-rings-of-fire.png)

Turkeys performing at a modern circus show. Microsoft Copilot created this image.

As stressed in the previous [CMMC Countdown post](https://www.secjuice.com/cmmc-part-2/), the five points are make or break to get a conditional CMMC certification. We will continue briefly reviewing how to address the remaining five pointers.

## CMMC Action Plan, continued

### AC.L2-3.1.18

> Control connection of mobile devices.
> Determine if:
> [a] mobile devices that process, store, or transmit CUI are identified;
> [b] mobile device connections are authorized; and
> [c] mobile device connections are monitored and logged.

Consider showing that all mobile devices are managed using mobile device management (MDM) software the provides built-in authorization, monitoring and logging.

You could simplify your compliance posture by preventing mobile device access.

### AT.L2-3.2.1

> Ensure that managers, systems administrators, and users of organizational systems are made aware of the security risks associated with their activities and of the applicable policies, standards, and procedures related to the security of those systems.
> Determine if:
> [a] security risks associated with organizational activities involving CUI are identified;
> [b] policies, standards, and procedures related to the security of the system are identified;
> [c] managers, systems administrators, and users of the system are made aware of the security risks associated with their activities; and
> [d] managers, systems administrators, and users of the system are made aware of the applicable policies, standards, and procedures related to the security of the system.

Consider showing a security awareness and training plan document that identifies your organization's cybersecurity and CUI risks and the training courses that will educate employees on those risks. Consider using the [SANS Security Awareness Planning Toolkit.](https://www.sans.org/tools/security-awareness-planning-toolkit/?ref=secjuice.com)

### AT.L2-3.2.2

> Ensure that personnel are trained to carry out their assigned information security-related duties and responsibilities.
> Determine if:
> [a] information security-related duties, roles, and responsibilities are defined;
> [b] information security-related duties, roles, and responsibilities are assigned to designated personnel; and
> [c] personnel are adequately trained to carry out their assigned information securityrelated duties, roles, and responsibilities.

Consider showing the training assigned to the information technology and cybersecurity team members. Also, the training should be focused on the specific IT and cybersecurity systems used at your organization. Consider identifying these training assignments in your security awareness and training plan.

### AU.L2-3.3.1

> Create and retain system audit logs and records to the extent needed to enable the monitoring, analysis, investigation, and reporting of unlawful or unauthorized system activity.
> Determine if:
> [a] audit logs needed (i.e., event types to be logged) to enable the monitoring, analysis, investigation, and reporting of unlawful or unauthorized system activity are specified;
> [b] the content of audit records needed to support monitoring, analysis, investigation, and reporting of unlawful or unauthorized system activity is defined;
> [c] audit records are created (generated);
> [d] audit records, once created, contain the defined content;
> [e] retention requirements for audit records are defined; and
> [f] audit records are retained as defined.

Consider reviewing which logs your systems are already capturing and how long they are being retained. Document those existing logs and the retention period. Review them and see whether they can help identify unlawful or unauthorized activity. Your security information and event manager (SIEM) might be able to create reports that identify unauthorized logins and anomalous behavior. Document this internal review as additional evidence. Make adjustments to the logs and retention periods as needed.

### CM.L2-3.4.1

> Establish and maintain baseline configurations and inventories of organizational systems (including hardware, software, firmware, and documentation) throughout the respective system development life cycles.
> Determine if:
> [a] a baseline configuration is established;
> [b] the baseline configuration includes hardware, software, firmware, and documentation;
> [c] the baseline configuration is maintained (reviewed and updated) throughout the system development life cycle;
> [d] a system inventory is established;
> [e] the system inventory includes hardware, software, firmware, and documentation; and
> [f] the inventory is maintained (reviewed and updated) throughout the system development life cycle.

Consider creating a document that captures the hardware, software, and firmware when setting up new workstations, laptops, and servers. Revise this document at least annually. Create a document or use an inventory tracking system that identifies all the devices and their hardware, software, and firmware. Review the document at least annually, but ideally, as changes occur if you track it manually.

### CM.L2-3.4.2

> Establish and enforce security configuration settings for information technology products employed in organizational systems.
> Determine if:
> [a] security configuration settings for information technology products employed in the system are established and included in the baseline configuration; and
> [b] security configuration settings for information technology products employed in the system are enforced.

Consider showing how you harden each new machine and maintain its hardening. Show the scripts, Windows group policy objects, and security profiles (in MDM and security management tools). Collect any reports that show how these security configurations are applied and maintained.

### IA.L2-3.5.1

> Identify system users, processes acting on behalf of users, and devices.
> Determine if:
> [a] system users are identified;
> [b] processes acting on behalf of users are identified; and
> [c] devices accessing the system are identified.

Consider leveraging the implementation and evidence used for [AC.L2-3.1.1](https://www.secjuice.com/cmmc-part-2/). Furthermore, consider defining how each user's unique identifier (e.g., username) and device's unique identifiers (e.g., hostname) are assigned.

### IA.L2-3.5.2

> Authenticate (or verify) the identities of users, processes, or devices, as a prerequisite to allowing access to organizational systems.
> Determine if:
> [a] the identity of each user is authenticated or verified as a prerequisite to system access;
> [b] the identity of each process acting on behalf of a user is authenticated or ...