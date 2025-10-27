---
title: Ansible with bastion host
url: https://www.adainese.it/blog/2022/10/30/ansible-with-bastion-host/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-30
fetch_date: 2025-10-03T21:19:37.613456
---

# Ansible with bastion host

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Ansible with bastion host

#### Table of contents

* [Scenario](#scenario)
* [Bastion host and AWS EC2 dynamic inventory](#bastion-host-and-aws-ec2-dynamic-inventory)
* [Configuring internal hosts via bastion](#configuring-internal-hosts-via-bastion)
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

## Ansible with bastion host

Andrea Dainese

October 30, 2022

[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/blog/2022/10/30/ansible-with-bastion-host/cyber-range-diagram-w-bastion.webp)](/blog/2022/10/30/ansible-with-bastion-host/cyber-range-diagram-w-bastion.webp)

This is the second part of my IaC overview based on a personal experiment: building Cyber range using the IaC paradigm. Here are the
[first](https://www.adainese.it/blog/2022/10/29/infrastructure-as-code-for-cyber-ranges/ "Infrastructure as code for Cyber Ranges")
and
[third](https://www.adainese.it/blog/2022/10/31/improving-iac-with-spacelift/ "Improving IaC with Spacelift")
parts.

In a pure design perspective, the client-to-site VPN approach is still the best. But from an automation perspective, I had to redesign it including a bastion host. I don’t like the idea so much, but the pros are more than the cons.

## Scenario

Compared to the scenario with the client-to-site VPN concentrator, this one seems simpler: internal VMs are reachable via the Linux bastion host. In practice, the bastion host proxies SSH connections. The bastion host does not require any configuration at all.

Because my scenario requires that attendees can reach internal VMs, I copy into the bastion host the SSH private key needed to log in to the internal VMs. In the future, I think it’s better if the bastion host serves also as an OpenVPN concentrator.

[![Cyber range diagram with bastion host](/blog/2022/10/30/ansible-with-bastion-host/cyber-range-diagram-w-bastion.png)](/blog/2022/10/30/ansible-with-bastion-host/cyber-range-diagram-w-bastion.png)

## Bastion host and AWS EC2 dynamic inventory

At this point Ansible should:

* configure the bastion host using the public IP address;
* configure the internal hosts using the private IP address via the bastion host’s public IP address.

Because of the Spacelift design, I had to configure everything using a single Ansible playbook. It means that the AWS EC2 Ansible inventory must:

* return the public IP address for the bastion host;
* return the private IP addresses for the internal VMs.

Moreover, Ansible should configure the SSH proxy just before logging in to each internal host.

After several attempts, I find a working recipe. Let’s start with the Ansible inventory:

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
  ansible_host: public_ip_address if tags.Name == "bastion" else private_ip_address
```

Remember I wrote that IaC is 80% plan and standardization? I assume that in every scenario I will use “bastion” as the hostname for the bastion host, and I tag the hostname in the AWS EC2 configuration. This is one of my “standards” (assumptions).

In the above AWS EC2 Ansible inventory configuration, I return the public IP address only if the `Name` tag is equal to `bastion`. The inventory returns the private IP address for any other VMs.

My Ansible playbook starts configuring the Ansible host:

```
- hosts: tag_Name_bastion
  gather_facts: no
  remote_user: ubuntu
  roles:
    - role: linux-bastion
      tags: always
```

In the role, I find the available SSH key and upload it to the bastion host for attendees. Remember I wrote that I want a “soft” lock-in? That’s where I make the playbook compatible with Spacelift environments and mine. I also used the tag “always” because I configure `ansible_ssh_private_key_file` (see after).

## Configuring internal hosts via bastion

At this point I can configure internal hosts. Another assumption I made is that tags contains any interesting attributes I use in Ansible to group, query and configure hosts. In practice I’m using the following tags:

* `Os:ubuntu`: for Ubuntu VMs;
* `Database:mariadb`: for MariaDB VMs;
* `Webapp:wordpress`: for VMs with Wordpress.

My Ansible playbook runs multiple plays:

```
- hosts: tag_Name_bastion
  gather_facts: no
  remote_user: ubuntu
  roles:
    - role: linux-bastion
      tags: always

- hosts: tag_Os_ubuntu:!tag_Name_bastion
  gather_facts: yes
  become: yes
  vars_files:
    - default.yaml
  roles:
    - role: set-environment
      tags: always

# [...]

- hosts: tag_Os_ubuntu:&tag_Database_mariadb
  gather_facts: yes
  become: yes
  vars_files:
    - default.yaml
  roles:
    - role: set-environment
      tags: always
    - role: linux-mariadb
      tags: mariadb

# [...]

- hosts: tag_Os_ubuntu:&tag_Webapp_wordpress

# [...]
```

Ansible facts are host specific: it means that if I set `ansible_ssh_private_key_file` on the bastion host, it is undefined for other hosts.

How could I configure SSH proxy for any internal hosts excluding the bastion host?

The magic happens in the `default.yaml` file using [Ansible...