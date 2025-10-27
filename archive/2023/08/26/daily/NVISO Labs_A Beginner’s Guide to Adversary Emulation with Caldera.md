---
title: A Beginner’s Guide to Adversary Emulation with Caldera
url: https://blog.nviso.eu/2023/08/25/a-beginners-guide-to-adversary-emulation-with-caldera/
source: NVISO Labs
date: 2023-08-26
fetch_date: 2025-10-04T11:59:35.345492
---

# A Beginner’s Guide to Adversary Emulation with Caldera

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# A Beginner’s Guide to Adversary Emulation with Caldera

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[Adversary Emulation](https://blog.nviso.eu/category/red-team/adversary-emulation/), [Purple Team](https://blog.nviso.eu/category/purple-team/)

August 25, 2023August 24, 2023
11 Minutes

![caldera logo](https://wazuh.com/uploads/2022/04/caldera-post-icon.png)

## **Target Audience**

The target audience for this blog post is individuals who have a basic understanding of cybersecurity concepts and terminology and looking to expand their knowledge on adversary emulation. This post delves into the details of adversary emulation with the Caldera framework exploring the benefits it offers. By catering to a beginner to intermediate audience, the blog post aims to strike a balance between providing fundamental information for newcomers and offering valuable insights and techniques that can benefit individuals who are already familiar with the basics of cybersecurity.

## **What is Adversary Emulation**

Adversary emulation is a methodology used to simulate the Tactics, Techniques, and Procedures (TTPs) used by known Advanced Persistent Threats (APTs), with the goal of identifying vulnerabilities in an organization’s security defenses. By emulating real-world attacks and incident response techniques, such as exploitation of vulnerabilities and lateral movement within a network, cybersecurity teams can gain a better understanding of their security posture and identify areas for improvement.

## **The Need for Adversary Emulation**

Adversary emulation can help organizations test their security defenses against real-world threats. Some of the benefits the emulation offers are:

* **Identifying vulnerabilities:** Adversary emulation assists organizations in identifying vulnerabilities, weaknesses or misconfigurations in their security defenses that might not have been detected through conventional security testing. This information can enhance the existing detection mechanisms by creating new alerts and rules that are triggered when similar activities are detected. The emulation results can also work as a guide in prioritizing mitigation and patching activities.
* **Improving security controls:** By identifying weaknesses in their security defenses, organizations can make informed decisions about how to improve their security controls. This can include implementing new security technologies, updating security policies, or providing additional security awareness training to employees.
* **Measuring security effectiveness:** Adversary emulation enables organizations to assess the effectiveness of their security defenses within a controlled environment. Through analyzing the emulation results, organizations can have a clearer understanding of how well their incidence response plan operates in real-world scenarios.If any gaps or inefficiencies are identified, the plan can be refined based on the new data.
* **Staying ahead of emerging threats:** Adversary emulation exercises can help organizations stay ahead of emerging threats by testing their security defenses against new and evolving attack techniques. This can help organizations prepare for future threats and ensure that their security defenses are effective in protecting against them.

## **Emulation VS Simulation**

Emulation involves creating a replica of a specific system or environment, such as an operating system, network, or application. It provides a more realistic testing environment, which can help identify vulnerabilities and test the effectiveness of security controls in a more accurate and reliable way. However, creating an emulation environment can be time-consuming and resource-intensive, and it may not always be feasible to replicate every aspect of a real-world environment.

Simulation, on the other hand, involves creating a hypothetical scenario that models a real-world attack. It is often quicker and easier to set up, and can be used to test response plans and procedures without the need for a complex emulation environment. However, simulations may not always provide a completely accurate representation of a real-world attack scenario, and the results may be less reliable than those obtained through emulation.

## **The Caldera Framework**

MITRE’s Caldera project is an open-source platform that allows organizations to automatically emulate the tactics, techniques, and procedures (TTPs) used by real-world APTs. The platform is designed to be modular, which means that it can be customized to fit the specific needs of an organization. More information can be found in the official [documentation](https://caldera.readthedocs.io/en/latest/) and on [GitHub](https://github.com/mitre/caldera). Red team operators can benefit from this by manually executing TTPs and blue team operators can run automated incident response actions. Caldera is also highly extensible, meaning that it can be integrated with other security tools to provide a comprehensive view of an organization’s security defenses. Moreover, it is built on the **MITRE ATT&CK** framework which is where the platform draws all the Tactics, Techniques and Procedures (TTPs) from.

Most common use cases of this framework include but not limited to:

* **Autonomous Red Team Engagements:** This case is used to emulate the TTPs of known adversary profiles to discover gaps across an infrastructure, test the defenses currently in place and train operators on detection different threats.
* **Manual Red Team Engagements:** This case allows red team operators to replace or extend the attack capabilities of a scenario, giving them more freedom and control over the current emulation.
* **Autonomous Incident Response:** This case is used by blue team operators to perform automated incident response actions to aid them in identifying TTPs and threats that other security solutions may not detect and/or prevent.

Caldera consists of two main components:

* **The core system**, which is the framework’s code, including an asynchronous command-and-control (C2) server with a REST API and a web interface.
* **Plugins** which are separate repositories that expand the core framework capabilities and provide additional functionality. Examples include agents, GUI interfaces, collections of TTPs and more.

In Figure 1 below, we are greeted with when we login eithe...