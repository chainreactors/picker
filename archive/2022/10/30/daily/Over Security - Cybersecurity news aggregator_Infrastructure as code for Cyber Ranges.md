---
title: Infrastructure as code for Cyber Ranges
url: https://www.adainese.it/blog/2022/10/29/infrastructure-as-code-for-cyber-ranges/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-30
fetch_date: 2025-10-03T21:19:36.441400
---

# Infrastructure as code for Cyber Ranges

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Infrastructure as code for Cyber Ranges

#### Table of contents

* [Scenario](#scenario)
* [Plan and standardization](#plan-and-standardization)
* [Creating infrastructure](#creating-infrastructure)
* [Configuring the infrastrucutre](#configuring-the-infrastrucutre)
* [Other stuff (certificates)](#other-stuff-certificates)
* [Conclusions](#conclusions)

#### Latest posts

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)

[Modifying an object in Strata Cloud Manager](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)
September 28, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)

[From Single-Site to Multi-Site with NDO](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)
September 24, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)

[Retrieving firewall interfaces with Strata Cloud Manager](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)
September 21, 2025

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)

[EVE-NG Linux VM SSH troubleshooting](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)
September 20, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 159 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 123 posts

[![Category cover](/images/categories/ciso.webp)](/categories/ciso)

[CISO](/categories/ciso)
 23 posts

[![Category cover](/images/categories/personal-security.webp)](/categories/personal-security)

[Personal Security](/categories/personal-security)
 22 posts

[![Category cover](/images/categories/security.webp)](/categories/security)

[Security](/categories/security)
 20 posts

[![Category cover](/images/categories/notes.webp)](/categories/notes)

[Notes](/categories/notes)
 19 posts

[![Category cover](/images/categories/infrastructure.webp)](/categories/infrastructure)

[Infrastructure](/categories/infrastructure)
 12 posts

[![Category cover](/images/categories/ot-ics.webp)](/categories/ot-ics)

[OT/ICS](/categories/ot-ics)
 5 posts

[![Category cover](/images/categories/books.webp)](/categories/books)

[Books](/categories/books)
 3 posts

[![Category cover](/images/categories/unetlab.webp)](/categories/unetlab)

[UNetLab](/categories/unetlab)
 3 posts

[![Category cover](/images/categories/writeup.webp)](/categories/writeup)

[Write-up](/categories/writeup)
 3 posts

[![Category cover](/images/categories/osint.webp)](/categories/osint)

[OSInt](/categories/osint)
 2 posts

[![Category cover](/images/categories/life.webp)](/categories/life)

[My life](/categories/life)
 1 posts

## Infrastructure as code for Cyber Ranges

Andrea Dainese

October 29, 2022

[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/blog/2022/10/29/infrastructure-as-code-for-cyber-ranges/cyber-range-diagram.webp)](/blog/2022/10/29/infrastructure-as-code-for-cyber-ranges/cyber-range-diagram.webp)

This is the first part of my IaC overview based on a personal experiment: building Cyber range using the IaC paradigm. Here are the
[second](https://www.adainese.it/blog/2022/10/30/ansible-with-bastion-host/ "Ansible with bastion host")
and
[third](https://www.adainese.it/blog/2022/10/31/improving-iac-with-spacelift/ "Improving IaC with Spacelift")
parts.

During my Twitch session, I’m used to offering a practical lab to attendees. My labs are automatically created on AWS, using Terraform and Ansible.

## Scenario

My scenario is pretty simple: I need to create a set of VM inside AWS and configure them with some additional software and services. Those VMs expose some vulnerable services which can be exploited and defended by attendees.

Before starting the Twitch session, I manually started Terraform and Ansible to create and configure VMs. To be specific I use:

* Terraform, to create VMs in AWS;
* Terraform, to create client-to-site VPN gateway;
* OpenVPN to connect to the internal side of the lab;
* Ansible, via OpenVPN, to configure VMs.

The building process takes less than 10 minutes.

[![Cyber range diagram](/blog/2022/10/29/infrastructure-as-code-for-cyber-ranges/cyber-range-diagram.png)](/blog/2022/10/29/infrastructure-as-code-for-cyber-ranges/cyber-range-diagram.png)

## Plan and standardization

IaC is 80% plan and standardization. It means that we need to identify requirements, scenarios, and corner cases. Then we need to identify how we define our infrastructure (I refer to this phase as “modeling”), and finally, we should write prototypes to verify our idea and approach.

In my case I need to create Cyber range scenarios that can include multiple VMs:

* with various operating systems and applications;
* attached to different networks;
* possibly protected by additional appliances (firewalls).

All VMs must be accessible by a specific host to configure them.

Last requirement: all scenarios should be completely created from scratch and destroyed after the session. No permanent data is expected.

In my case I decided to:

* write a custom Terraform module to create the basic infrastructure (Internet access, basic networks, client-to-site VPN gateway, or bastion hosts);
* define manually the additional components (additional VMs, networks, and how they are connected);
* configure each VMs using roles (multiple roles can be configured within the same VM).

## Creating infrastructure

The very basic scenario requires creating a bastion host and at least one Ubuntu Linux VM. The Terraform documentation is pretty explanatory, and there are no issues with that.

My only suggestion is: plan carefully what you need now and shortly, and be ready to adapt.

In my cases, I decided to use tags to track down OS, installed applications, purpose, and administrative users… Those tags will be useful in Ansible.

## Configuring the infrastrucutre

Here come the problems: Terraform and Ansible are two different universes, and I need to make them communicate. Using AWS, and planning carefully my infrastructure, I found the AWS EC2 Ansible inventory pretty good, even if it has some limitations.

In short:

* Terraform creates the infrastructure by applying tags;
* AWS EC2 Ansible inventory fetches the AWS EC2 instances and prepares an Ansible-compatible inventory, maintaining the tags;
* After establishing the OpenVPN connection, Ansible can configure internal VMs.

The Ansible AWS EC2 inventory resolves all internal VMs with the private IP address:

```
plugin: aws_ec2
regions:
  - eu-central-1
filters:
  instance-state-name: running
keyed_groups:
  - key: tags
    prefix: tag
hostnames:
  - tag:Name
compose:
  ansible_host: private_ip_address
```

At this point, we have an excellent way to build and configure the infrastructure, no matter if VMs are reachable from the Internet or not. The only side effect is that client-to-site VPN connections impact a lot on my AWS account.

## Other stuff (certificates)

The above approach requires building and maintaining a CA (Certification Authority):

* AWS client-to-site concentrator requires a server certificate;
* VPN clients need the CA public certificate to validate the concentrator certificate;
* VPN clients need a valid certificate to be accepted by the VPN concentrator;
* AWS client-to-site concentrator needs the CA public certificate to validate the client certificates;
* additional servers (e.g...