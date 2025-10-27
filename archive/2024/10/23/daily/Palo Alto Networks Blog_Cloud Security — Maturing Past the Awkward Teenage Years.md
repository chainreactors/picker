---
title: Cloud Security — Maturing Past the Awkward Teenage Years
url: https://www.paloaltonetworks.com/blog/2024/10/cloud-security-maturing-past-the-awkward-teenage-years/
source: Palo Alto Networks Blog
date: 2024-10-23
fetch_date: 2025-10-06T18:59:44.747681
---

# Cloud Security — Maturing Past the Awkward Teenage Years

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Cloud Security](https://www.paloaltonetworks.com/blog/category/cloud-security/)
* Cloud Security — Maturing...

# Cloud Security — Maturing Past the Awkward Teenage Years

Link copied

By [Dena De Angelo](/blog/author/ddeangelo/ "Posts by Dena De Angelo")

Oct 22, 2024

8 minutes

[Cloud Security](/blog/category/cloud-security/)

[Points of View](/blog/category/points-of-view/)

[Product Features](/blog/security-operations/category/product-features/)

[Interview](/blog/tag/interview/)

![](/blog/wp-content/themes/panwblog2023/dist/images/audio-icon.svg)

Nathaniel Quist – Cloud Security

*00:00*
*00:00*

Volume Slider

10s

10s

10s

10s

Seek Slider

The genesis of cloud computing can be traced back to the 1960s concept of utility computing, but it came into its own with the launch of Amazon Web Services (AWS) in 2006. This marked the beginning of cloud computing's adolescence (with some early “terrible twos” no doubt) revolutionizing how businesses access and utilize computing resources. As such, cloud security is emerging from its tumultuous teenage years into a more mature phase.

The initial growing pains of rapid adoption and security challenges are giving way to more sophisticated, purpose-built security solutions. This maturation reflects a deeper understanding of cloud-specific threats and the shared responsibility model, paving the way for more resilient and secure cloud ecosystems.

However, with the rapid adoption of cloud technologies comes an equally swift evolution of cybersecurity threats. As organizations transition from traditional, legacy infrastructure to virtual cloud environments, they face new, dare we say bold, challenges in securing their digital assets. According to the [Unit 42 Cloud Threat Report](/prisma/unit42-cloud-threat-research):

> The rate of cloud migration shows no sign of slowing down—from $370 billion in 2021, with predictions to reach $830 billion in 2025—with many cloud-native applications and architectures already having had time to mature. The dynamic nature of cloud technology—with feature updates in public cloud services, new attack methods and the widespread use of open-source code—is now driving awareness of the risks inherent to modern, cloud-native development.

To that end, this blog post explores the current state of cloud security, common misconceptions and best practices for strengthening your cloud defenses. David Moulton, director of thought leadership, sat down with Nathaniel Quist (“Q”), manager of Cloud Threat Intelligence at Palo Alto Networks and Unit 42, to discuss the intricate and hidden world of cloud threats in a recent [Threat Vector Podcast](https://thecyberwire.com/podcasts/threat-vector) interview.

## Buckle Up, Buttercup

According to Unit 42 research, it can be inferred that by 2025, cloud threats will increase by 188% based on data they have observed over the past three years. This alarming upward trend highlights the urgent need for robust cloud security measures. Q explains:

> Cloud breaches have exploded as threat actors shift their focus from on-premises environments to the cloud. Attackers are literally minting money with cryptojacking or malicious and unauthorized mining for cryptocurrency.

The impact of these attacks is significant and visible as 45% of organizations say they are seeing APT threats targeting their ever-expanding infrastructures, including their cloud environment. These statistics underscore the critical importance of implementing security in cloud environments.

## Common Misconceptions about Cloud Security

Many organizations transitioning to the cloud harbor misconceptions that can leave them vulnerable and exposed. Q highlights one of the most prevalent fallacies:

> Some misconceptions are that I can just ‘lift and shift’ everything from my data center up into the cloud and everything will be great. I'll have cost savings in that the cloud is supposed to be cheaper and more secure. Therefore, it'll be easier. It's definitely a misconception.

This "lift and shift" approach often leads to unexpected costs and security gaps. Organizations must understand that cloud security requires a different mindset and approach compared to traditional, on-premises security because cloud environments are fundamentally different in their architecture, scalability and shared responsibility model.

Cloud platforms offer dynamic and distributed resources that can rapidly scale, introducing new attack surfaces and security challenges. Additionally, the shared responsibility model in cloud computing means that while providers secure the infrastructure, customers are responsible for securing their data, applications and access management.

This division of responsibilities requires a reimagining of security strategies, emphasizing aspects like identity and access management (IAM), data encryption and continuous monitoring of cloud-native threats that may not have been as important in traditional on-premises environments.

As a result, another crucial misconception revolves around the shared responsibility model. Q explains:

> That's the user of the cloud…that's *your* responsibility. AWS, GCP, Azure, they will not patch your systems for you, and they will not design your user access.

Understanding this shared responsibility is paramount for maintaining a secure cloud environment. Organizations must clearly delineate which security aspects fall under their purview, and which are managed by the cloud service provider (CSP). This clarity ensures that no security gaps are left unaddressed. It prevents duplication of efforts and allows for the implementation of a comprehensive security strategy that aligns with the unique characteristics of cloud infrastructure.

Failure to fully grasp and act on this shared responsibility model can lead to vulnerabilities, data breaches and compliance issues, potentially resulting in significant financial and reputational damage as evidenced by the [2023 MOVEit Transfer data breach](https://unit42.paloaltonetworks.com/threat-brief-moveit-cve-2023-34362/). This incident, which affected thousands of organizations worldwide, exploited a zero-day vulnerability in a widely used file transfer tool hosted on cloud infrastructure. The breach resulted in the theft of sensitive data from numerous high-profile companies and government agencies, highlighting the cascading effects of security lapses in cloud-based services and the value of understanding and implementing proper security measures in shared responsibility models.

## The Challenge of Cloud-Based Threats

Detecting and mitigating cloud-based threats presents unique challenges. Q points out, "We're kind of limited in the amount of visibility we have in the cloud when it comes to a granular runtime operation."

This limited visibility, combined with the sheer volume of data generated in cloud environments, makes it difficult for security teams to identify and respond to threats effectively. It's a paradoxical situation where security teams face "both too much data and not enough data."

## Emerging Cloud-Native Threats

Cloud-native environments, such as those using Docker and Kubernetes, are particularly attractive to attackers due to their complexity and potential for automation. Q shares a startling example:

> We released an identity access management credential inside of a GitHub repo. And then within 4 minutes of that identity and access management credential being placed inside of that GitHub repo, we had active cryptomining happen in our environment.

This level of automation in attacks necessitates equally sophisticated and automated defense mechanisms:

* Continuous integration/continuous deployment (CI/CD) pipeline security tools that automatically scan code and IaC (infrastructure-as-code) templates for vulnerabilities and misconfigurations before deploymen...