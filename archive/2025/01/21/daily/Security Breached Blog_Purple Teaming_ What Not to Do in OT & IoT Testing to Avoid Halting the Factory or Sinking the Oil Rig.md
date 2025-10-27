---
title: Purple Teaming: What Not to Do in OT & IoT Testing to Avoid Halting the Factory or Sinking the Oil Rig
url: https://blog.securitybreached.org/2025/01/20/purple-teaming-what-not-to-do-in-ot-iot-testing-to-avoid-halting-the-factory-or-sinking-the-oil-rig/
source: Security Breached Blog
date: 2025-01-21
fetch_date: 2025-10-06T20:13:51.808914
---

# Purple Teaming: What Not to Do in OT & IoT Testing to Avoid Halting the Factory or Sinking the Oil Rig

[Skip to content](#page)

[Security Breached Blog](https://blog.securitybreached.org/)

Hack Smart, Stay Safe: Comprehensive Guides to Cybersecurity and Bug Bounty

January 20, 2025

Share

* [Purple Teaming](https://blog.securitybreached.org/category/purple-teaming/)
* [0](https://blog.securitybreached.org/2025/01/20/purple-teaming-what-not-to-do-in-ot-iot-testing-to-avoid-halting-the-factory-or-sinking-the-oil-rig/#respond)

# Purple Teaming: What Not to Do in OT & IoT Testing to Avoid Halting the Factory or Sinking the Oil Rig

[![](https://secure.gravatar.com/avatar/5ab39afe7f0c8e2c9e7a17044092edc8e890061374025f227e6655e5a4856c43?s=64&r=g)](https://blog.securitybreached.org/author/umairahmed/)

by [Umair Ahmed](https://blog.securitybreached.org/author/umairahmed/ "Posts by Umair Ahmed")

Hi Everyone, I am **Umair Ahmed** currently working as Senior Security Engineer @ [HelloFresh](https://hellofresh.com), lately have been doing quite a bit of purple teaming around industrial systems, thought of sharing my experience here.
Testing operational and IoT systems is no easy feat, especially when the stakes involve halting a factory or sinking an oil rig. Every one of us who has embarked on the journey to test OT/IoT systems has felt nervous and cautious about things going south. Here’s to all the comrades out there who want to excel in these situations:

[![](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2025/01/iot2-1.png?resize=620%2C166&ssl=1)](https://i0.wp.com/blog.securitybreached.org/wp-content/uploads/2025/01/iot2-1.png?ssl=1)

*click to expand*

## 1. Preparation, Planning, and Scoping

Before you start, focus on these critical aspects: Network Services, Web/API, CMS/Apps, Wireless Security, Social Engineering, IaaS/PaaS/SaaS, Physical Security, and Operations Technology. Breaking them into manageable categories will help avoid oversight and improve planning.

### Key Steps:

* **Understand the Landscape:** Get a holistic view of the technology, processes, and people in place.
* **Ask Questions:** Inquire about third-party companies involved in deployment and maintenance, their roles, backup information, disaster recovery plans, redundancies, and other relevant factors. For example, ask questions like:

  ***‘What are the response times for third-party support?’, ‘What specific systems have redundancy in place?’*,** or ***‘What are the protocols for disaster recovery in case of a major outage?’***
* **Research and Prepare:** Set up infrastructure for social engineering, Command & Control (C2) tools ([C2 Matrix](https://howto.thec2matrix.com/)), collaboration tools (e.g., [Vectr](https://docs.vectr.io/user/important-concepts/)), VPNs (if required), and access systems for different user behaviors.

## 2. Analysis of Business-Critical Operations

Identify and analyze key factors from the CIA (Confidentiality, Integrity, Availability) triad.

### Considerations:

* **System Impact:** Understand the financial and operational implications of a system going offline e.g. If you are testing a Factory/Oil Rig.
* **Redundancy:** Assess the cost (business, human, financial) of systems being affected.
* **Wireless Security:** Evaluate its impact on IoT, OT, and PLC communications.
* **SOPs:** Review standard procedures for physical security and site safety.
* **Environment-Specific Do’s and Don’ts:** Ensure compliance.
* **Test Devices:** Verify the availability and cost of hardware testing.

## 3. Threat Modeling

With knowledge of the business, facilities, hardware, and SOPs, model threats based on the known information. Gather this knowledge effectively by conducting interviews with key personnel, reviewing relevant documentation such as operational manuals and incident reports, and performing on-site observations to understand processes and configurations.

### Key Steps:

* **APT Research:** Investigate industry-relevant APTs and their TTPs ([MITRE ATT&CK](https://attack.mitre.org/groups/)).
* **Risk Register:** Use the risk register to validate feasibility.
* **Threat Register:** Include business threats from past incidents, threat hunting, or projections.
* **Detection Team Input:** Validate threats with insights from detection and response teams.
* **Business Insights:** Incorporate input from business and supply chain teams.
* **Kill Chain Scenarios:** Create detailed scenarios using frameworks like [Lockheed Martin’s Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) and tools like Vectr.

Lastly, Be as thorough as possible about droppers, shells, commands, tactics, processes, tools. This will give visibility to relevant stakeholders and if something is deemed to be dangerous it will be rooted out in the next step.

## 4. Stakeholder Alignment

Align stakeholders to mitigate risks effectively.

### Key Actions:

* **Define Objectives:** Ensure a clear understanding of goals, processes, timelines, and actions.
* **Discuss Risks:** Identify and mitigate worst-case scenarios.
* **Timing:** Schedule testing outside peak business hours.
* **Approval:** Obtain agreement from all stakeholders.

## 5. Execution

During execution, perform scans, enumeration, and exploitation carefully. For example, when conducting a vulnerability scan, use low-intensity modes to avoid overwhelming the network. Similarly, during exploitation, simulate a breach scenario in a controlled environment to assess the impact without disrupting operations. These precautions ensure testing is effective yet minimally intrusive.

### Best Practices:

* **Throttle Scans:** Avoid availability issues.
* **Assume Breach:** In case exploitation might disrupt systems, plan redundancies.
* **API Testing:** Start with documentation rather than direct scans.
* **Access Control Checks:** Test at network and application layers.
* **Wireless Testing:** Test from extended ranges to simulate intruder scenarios.
* **Social Engineering:** Focus on evidence collection without deploying malicious payloads.
* **Security Gap Analysis:** Review people, processes, and compile results in the checklists for future reference.
* **Physical Security:** Check locks, document sensitive information, and demonstrate identity cloning techniques (e.g., Flipper Zero).
* **OSINT and CTI:** Leverage tools like Shodan and Censys for device footprints.
* **Monitoring Evidence:** Record detection and monitoring outcomes.

## 6. Cleaning

Ensure a clean slate post-engagement.

### Steps:

* **Hardware and Software:** Remove any tools used.
* **Revert Changes:** Restore configurations to their original state.

## 7. Reporting

Create a comprehensive report for technical and non-technical audiences. Include key sections such as an executive summary, methodology, detailed findings with evidence, impact analysis, and actionable recommendations. Use visuals like charts or diagrams to make complex data more accessible.

### Essentials:

* **Document Findings:** Provide evidence and reproduction steps.
* **Summarize Outcomes:** Summary for technical and non technical audiences including business leadership with clear outcomes and action items (next steps).
* **Debrief:** Prepare a debrief presentation and run it through all the stakeholders to establish the acceptance of responsibilities and next steps to be taken by relevant teams
* **Simplify Processes:** Make all the processes easy to follow for teams, and agree on the clear SLAs and exceptions (if any).

Always remember this is the most important step because the engagement will be useless unless results are properly delivered, understood and mitigations are taken.

## 8. Vulnerability Management (Follow-ups)

This phase tests your ability to ensure follow-through.

### Tips:

* **Dashboards:** Use dashboards created in the last steps to track and monitor the progress of action items.
* **Reminders:** Regularly follow up with teams.

At the end of this process, take a moment to breathe, Enjoy your life because you will...