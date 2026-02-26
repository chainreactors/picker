---
title: The CLAIR Model: A Synthesized Conceptual Framework for Mapping Critical Infrastructure Interdependencies &#x5b;Guest Diary&#x5d;, (Wed, Feb 25th)
url: https://isc.sans.edu/diary/rss/32748
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-25
fetch_date: 2026-02-26T04:12:05.361432
---

# The CLAIR Model: A Synthesized Conceptual Framework for Mapping Critical Infrastructure Interdependencies &#x5b;Guest Diary&#x5d;, (Wed, Feb 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32744)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [The CLAIR Model: A Synthesized Conceptual Framework for Mapping Critical Infrastructure Interdependencies [Guest Diary]](/forums/diary/The%2BCLAIR%2BModel%2BA%2BSynthesized%2BConceptual%2BFramework%2Bfor%2BMapping%2BCritical%2BInfrastructure%2BInterdependencies%2BGuest%2BDiary/32748/)

**Published**: 2026-02-25. **Last Updated**: 2026-02-25 21:09:28 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/The%2BCLAIR%2BModel%2BA%2BSynthesized%2BConceptual%2BFramework%2Bfor%2BMapping%2BCritical%2BInfrastructure%2BInterdependencies%2BGuest%2BDiary/32748/#comments)

[This is a guest diary contributed by Claire Perry ([LinkedIn](http://https://www.linkedin.com/in/ctwperry/))]

The structural integrity of modern society is predicated upon a dense and often opaque network of interconnected systems. For decades, the modeling of these systems remained siloed within specific domains: industrial processes were governed by the hierarchical constraints of the Purdue Model, while corporate and data-centric ecosystems were organized using various Enterprise Architecture (EA) frameworks (Fortinet, n.d.; The Open Group, n.d.). However, the accelerating convergence of Information Technology (IT) and Operational Technology (OT) has exposed a critical analytical gap. Disruptions in the external utility grid, once considered an unlikely factor, now propagate through the physical and logical layers of the enterprise with devastating speed, as evidenced by recent power-related disconnections of large-scale data center operations (Mural et al., 2026; Islam et al., 2023).

To bridge this gap, this report introduces the Comprehensive Linkage and Architectural Infrastructure Resiliency (CLAIR) Model. The CLAIR Model is a new conceptual framework that synthesizes the vertical depth of the Purdue Enterprise Reference Architecture (PERA) with the multi-dimensional, interrogative breadth of the Zachman Framework for Enterprise Architecture (Fortinet, n.d.; The Open Group, n.d.). By establishing a unified taxonomy that accounts for everything from the sub-physical utility grid to the hyper-distributed cloud, the CLAIR Model provides a structured scope for identifying and visualizing critical infrastructure interdependencies. This framework prioritizes the identification of these linkages over specific mitigations, offering a diagnostic tool for understanding how failures in one sector, such as the power grid, generate cascading effects across the data center and manufacturing landscapes (Fortinet, n.d.; Islam et al., 2023; Virginia Department of Emergency Management, n.d.).

### Historical Context and the Necessity of Synthesis

The conceptual origin of industrial modeling lies in the 1990s at Purdue University, where researchers developed the Purdue Enterprise Reference Architecture (PERA) to standardize computer-integrated manufacturing (Fortinet, n.d.). The Purdue Model established a functional hierarchy ranging from Level 0 (physical processes) to Level 4 (business logistics), effectively creating an "automation pyramid." Isolation of sensitive controllers from internet-facing business networks is typically achieved via a "demilitarized zone" (DMZ) at Level 3.5 (Fortinet, n.d.).

While the Purdue Model excels at describing the internal dependencies of a single plant, it is inherently insular. It treats the external world as a series of inputs (Level 0) or external services (Level 5) without mapping the complex, bidirectional relationships between the plant and the broader infrastructure (Cybersecurity and Infrastructure Security Agency, 2025a; Williams, 1994). In parallel, Enterprise Architecture (EA) frameworks like Zachman were developed to organize the design artifacts of complex organizations from multiple stakeholder perspectives (The Open Group, n.d.). The CLAIR Model recognizes that neither framework, in isolation, can characterize the risks of a "system-of-systems" environment (Department of Defense, 2008). In modern critical infrastructure, a data center is not merely a facility at Level 4 of the Purdue Model; it is a massive electric load at the intersection of global telecommunications, regional power grids, and local water supply systems (UK Parliament, 2025; Chen et al., 2025). Failure to understand these dynamics results in ineffective response and poor coordination between decision-makers (Dudenhoeffer et al., 2006).

The CLAIR Model: Structural Hierarchy and Extended Levels

The CLAIR Model expands the traditional five-level Purdue hierarchy into a ten-level architectural stack. This expansion is designed to capture the "Level -1" dependencies on primary utility infrastructure and the "Level 6" and "Level 7" dependencies on cloud and safety systems (CISA, 2025a; Russo, 2022).

| CLAIR MODEL: 10-Level Architectural Stack | | | |
| --- | --- | --- | --- |
| Level | Layer | Description | Typical assets |
| >7 | High-Trust / Safety Systems | Ultimate integrity & safe-state maintenance | SIS, DNSSEC, Digital root of trust |
| 6 | The Connected World | External cloud & distributed services | AWS/Azure, IIoT platforms,external VPNs |
| 5 | Corporate Enterprise | Business planning & enterprise services | ERP, HR portals, BI/analytics |
| 4 | Business Operations | Resource Management & Workflow Execution | Workflow tools, Data Repositories, Reporting |
| 3.5 | Operational Boundary / Industrial DMZ | IT-OT convergence, traffic filtration, System Integration &Traffic Management | Firewalls, proxies, IPS/IDS, jump hosts, Security Gateways |
| 3 | Site Operations, Local Management | Facility-wide control, monitoring, Real-time System Oversight | Management Servers, Local Configuration Tools, SCADA servers, |
| 2 | Supervisory Control/Direct Control | Local, Immediate System Monitoring & Adjustment | HMI/SCADA clients, User Interfaces, Supervisory Applications |
| 1 | Core Function | Automated regulation & Execution of Primary Tasks | PLCs, RTUs, IEDs, Embedded Logic, Specialized Processors |
| 0 | Environment Interface | Real-time interaction with the physical world | Input/Output Devices, Sensors, Scanners |
| -1 | Primary Infrastructure | External utility generation &distribution | Power grid, Water, Pipelines, Network Backbones, Core Communication |

### Level -1: The Primary Infrastructure Foundation

The inclusion of Level -1 acknowledges that the "physics" of Level 0 is entirely dependent on a primary technology layer that exists outside the control of the plant operator (Islam et al., 2023). In the CLAIR Model, Level -1 encompasses the electricity generation and transmission systems, which exhibit complex dynamic behaviors such as low inertia and harmonic distortion when interfacing with data center power electronics (Chen et al., 2025). This layer is the source of cascading failure triggers, where a line fault in the high-voltage grid necessitates immediate load redistribution, often leading to voltage fluctuations that destabilize Level 0 sensors and Level 1 controllers (Islam et al., 2023).

### Levels 0-5: What Can Be Controlled

Levels 0–5 are generally within the organization’s direct control because the systems, assets, and processes at these layers are typically owned and/or administered by the business, company, or government entity. However, even within this “control zone,” organizations still inherit external dependencies, especially for software, firmware, and operating systems that rely on vendor-provided patche...