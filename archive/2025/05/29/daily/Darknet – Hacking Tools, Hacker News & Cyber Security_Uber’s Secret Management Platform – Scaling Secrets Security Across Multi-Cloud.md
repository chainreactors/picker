---
title: Uber’s Secret Management Platform – Scaling Secrets Security Across Multi-Cloud
url: https://www.darknet.org.uk/2025/05/ubers-secret-management-platform-scaling-secrets-security-across-multi-cloud/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2025-05-29
fetch_date: 2025-10-06T22:26:37.365732
---

# Uber’s Secret Management Platform – Scaling Secrets Security Across Multi-Cloud

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# Uber’s Secret Management Platform – Scaling Secrets Security Across Multi-Cloud

May 28, 2025

Views: 629

## Introduction

Managing secrets—such as API keys, credentials, and tokens—across a vast, multi-cloud infrastructure is a complex challenge. Uber addressed this by developing a centralised Secret Management Platform to handle over 150,000 secrets across over 5,000 microservices. This article explores the architecture, strategies, and outcomes of Uber’s approach to secrets management.

![Uber's Secret Management Platform - Scaling Secrets Security Across Multi-Cloud](data:image/svg+xml...)![Uber's Secret Management Platform - Scaling Secrets Security Across Multi-Cloud](https://www.darknet.org.uk/wp-content/uploads/2025/05/Ubers-Secret-Management-Platform-Scaling-Secrets-Security-Across-Multi-Cloud-640x427.jpg)

---

## Addressing Secrets Sprawl

Uber identified the risks associated with secrets scattered across codebases, configurations, and various systems. To mitigate this, they implemented both preventive and remediation strategies:

* **Preventive Measures:** A CLI tool integrated as a pre-commit hook in Git blocks commits containing secrets, preventing them from entering code repositories.
* **Remediation Strategies:** Real-time and scheduled scanning methods detect exposed secrets in code changes, Slack conversations, and build logs. Upon detection, the system notifies the responsible parties to revoke and remove the secrets, ensuring prompt remediation.

These measures significantly reduced the risk of secret leaks and minimised the need for incident responses.

---

## Consolidating Secret Vaults

Before the platform’s development, Uber operated 25 secret vaults across various teams and cloud providers. This decentralised approach led to inconsistencies and management challenges. The Secrets team undertook a consolidation process:

* **Standardisation:** Defined a Secret Management Standard to govern storage, rotation, and leak responses.
* **Migration:** Moved secrets from custom vaults and databases into six centrally managed vaults, reducing complexity and improving oversight.

This consolidation enabled uniform security baselines and streamlined secret management across the organisation.

---

## Building the Secret Management Platform

With centralised vaults in place, Uber developed a comprehensive Secret Management Platform featuring:

* **Metadata Model:** Describes properties of each secret, aiding in governance and automation.
* **Unified Interfaces:** Provides API, CLI, and web UI for seamless interaction with the platform.
* **Lifecycle Management:** Automates secret rotation, deletion, and revocation processes.
* **Access Management:** Implements consistent access controls across all secrets.
* **Integration Support:** Facilitates secret exchange with third-party vendors and SaaS applications.

This platform enhanced security and improved developer productivity by simplifying secret management tasks.

---

## Impact and Outcomes

The implementation of the Secret Management Platform led to significant improvements:

* **Reduced Secret Distribution:** Monitoring and scoping of secret access within containers resulted in up to a 90% reduction in secrets distributed to workloads.
* **Enhanced Security Posture:** Centralised management and standardised practices minimised the risk of secret leaks and unauthorised access.
* **Operational Efficiency:** Consolidating vaults and automating secret lifecycle processes streamlined operations and reduced overhead.

These outcomes underscore the effectiveness of Uber’s approach to secrets management in a complex, multi-cloud environment.

---

## Conclusion

Uber’s development of a centralised Secret Management Platform exemplifies a robust solution to the challenges of secrets management at scale. By consolidating vaults, standardising practices, and automating processes, they enhanced security, operational efficiency, and reduced risk. Organisations facing similar challenges can draw valuable insights from Uber’s strategy to strengthen their secrets management practices.

Source: <https://www.uber.com/blog/building-ubers-multi-cloud-secrets-management-platform>

## Related Posts:

* [Doppler CLI - Streamlined Secrets Management for DevOps](https://www.darknet.org.uk/2025/05/doppler-cli-streamlined-secrets-management-for-devops/)
* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [Force Push Scanner - Hunt GitHub Dangling Commits…](https://www.darknet.org.uk/2025/07/force-push-scanner-hunt-github-dangling-commits-for-leaked-secrets/)
* [Uber Paid Hackers To Hide 57 Million User Data Breach](https://www.darknet.org.uk/2017/11/uber-paid-hackers-hide-57-million-user-data-breach/)
* [Leveraging OSINT from the Dark Web - A Practical How-To](https://www.darknet.org.uk/2025/07/leveraging-osint-from-the-dark-web-a-practical-how-to/)
* [Envilder - Secure AWS SSM CLI for Environment…](https://www.darknet.org.uk/2025/06/envilder-secure-aws-ssm-cli-for-environment-variable-management/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fubers-secret-management-platform-scaling-secrets-security-across-multi-cloud%2F)

[Tweet](https://twitter.com/intent/tweet?text=Uber%27s+Secret+Management+Platform+-+Scaling+Secrets+Security+Across+Multi-Cloud&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fubers-secret-management-platform-scaling-secrets-security-across-multi-cloud%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fubers-secret-management-platform-scaling-secrets-security-across-multi-cloud%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fubers-secret-management-platform-scaling-secrets-security-across-multi-cloud%2F&text=Uber%27s+Secret+Management+Platform+-+Scaling+Secrets+Security+Across+Multi-Cloud)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F05%2Fubers-secret-management-platform-scaling-secrets-security-across-multi-cloud%2F)

[Email](/cdn-cgi/l/email-protection#a59ad6d0c7cfc0c6d198f0c7c0d7809792d6809795f6c0c6d7c0d1809795e8c4cbc4c2c0c8c0cbd1809795f5c9c4d1c3cad7c880979588809795f6c6c4c9cccbc2809795f6c0c6d7c0d1d6809795f6c0c6d0d7ccd1dc809795e4c6d7cad6d6809795e8d0c9d1cc88e6c9cad0c183c7cac1dc98e1ccd6c6cad3c0d7809795cdcad2809795f0c7c0d7809795c7d0ccc9d1809795c4809795c6c0cbd1d7c4c9ccdfc0c1809795d5c9c4d1c3cad7c8809795d1ca809795c8c4cbc4c2c0809795cad3c0d78097959490958097e6959595809795d6c0c6d7c0d1d6809795c4c6d7cad6d6809795908097e69595958097e7809795c8ccc6d7cad6c0d7d3ccc6c0d68097e6809795c0cbcdc4cbc6cccbc2809795d6c0c6d0d7ccd1dc809795c4cbc1809795d7c0c1d0c6cccbc2809795c0ddd5cad6d0d7c08b8095e18095e48095e18095e4f7c0c4c185e8cad7c085edc0d7c09f85809795cdd1d1d5d68096e48097e38...