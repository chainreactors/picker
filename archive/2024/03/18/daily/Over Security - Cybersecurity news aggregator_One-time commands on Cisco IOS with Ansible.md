---
title: One-time commands on Cisco IOS with Ansible
url: https://www.adainese.it/blog/2023/09/25/one-time-commands-on-cisco-ios-with-ansible/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-18
fetch_date: 2025-10-04T12:08:22.527485
---

# One-time commands on Cisco IOS with Ansible

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# One-time commands on Cisco IOS with Ansible

#### Table of contents

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

## One-time commands on Cisco IOS with Ansible

Andrea Dainese

September 25, 2023

[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/ansible.webp)](/images/vendors/ansible.webp)

In this article, we present an initial example of executing mass commands using Ansible on Cisco IOS devices. We will utilize the pre-configured “Cisco Legacy Core-Access topology” lab available in the repository [DevNetOps course material](https://github.com/dainok/courses "DevNetOps course material"):

[![Lab topology](/blog/2023/09/25/one-time-commands-on-cisco-ios-with-ansible/topology.png)](/blog/2023/09/25/one-time-commands-on-cisco-ios-with-ansible/topology.png)

Firstly, we need to create an [inventario](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html "Ansible inventory"). At this stage, we won’t delve deeply into the topic, but simply create a file containing all the devices present in the lab and the necessary variables, such as:

* `ansible_host`: the IP address of the device, as we don’t have a DNS system for automatic resolution;
* `ansible_user`: the user (admin) to access the device;
* `ansible_ssh_pass`: the password (cisco) to access the device;
* `ansible_connection`: the connection mode Ansible should use to connect;
* `ansible_network_os`: the type of device.

The `inventory.yml` file will look like this:

```
all:
  hosts:
    sw1.example.com:
    ansible_host: 169.254.1.101
    ansible_user: admin
    ansible_ssh_pass: cisco
    ansible_connection: ansible.netcommon.network_cli
    ansible_network_os: cisco.ios.ios
```

Since we are working with devices that only support outdated algorithms, we need to specifically enable them. We will do this by working on an SSH client config file named `ansible_libssh.conf`:

```
KexAlgorithms diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1
HostKeyAlgorithms ssh-rsa,ssh-dss

Host *
    ServerAliveInterval 5
    ServerAliveCountMax 3
```

In theory, it would be sufficient to specify only the algorithms to add, prepending the symbol `+`. However, in my tests, this syntax might cause issues. Therefore, I suggest defining all the algorithms we will need in our tests.

The `ansible_libssh.conf` file will be referenced by the `ansible.cfg` file, which defines the settings of the libssh library:

```
[persistent_connection]
ssh_type = libssh

[libssh_connection]
host_key_checking = false
look_for_keys = false
config_file = ../ansible_libssh_conf
```

Next, we start the nodes and verify that they are reachable:

```
ansible all -i inventory.yml -m ping
```

The above command executes a so-called ad-hoc command. In other words, we ran the ping command on all devices configured in the inventory.

Similarly, we can decide to execute a command on all devices:

```
ansible all -i inventory.yml -m cisco.ios.ios_command -a "commands='show version'"
```

We can adjust the number of parallel processes running the playbook. This number depends on available resources, particularly the number of CPUs, but not limited to that. Running a playbook involves “idle times,” i.e., time when the Ansible machine is waiting for output from the device. For Cisco devices, consider the time elapsed from entering the `show running-config` command to actually seeing the output on the screen. Therefore, we can safely increase the number of forks to double the available processors without risking overloading the Ansible controller:

```
[defaults]
forks = 8
```

## Andrea Dainese

For information, collaborations, proposals, requests for help, donations, use one of the following channels; email is preferred.

#### Past events

* - [SDN: Software Defined Now](/files/slides/20240305-cisco-aci-automation.pdf "View slides")
* - [Cybercrime](/files/slides/20231122-cybercrime.pdf "View slides")
* - [BGP attack scenarios](/files/slides/20220901-bgp-attack-scenarios.pdf "View slides")
* - [Approaching OT/ICS Security](/files/slides/20220317-approaching-ot-ics-security.pdf "View slides") (with [Festo Academy](https://www.festocte.it/eventi/industry_4_0/17-03-2022/webinar_la_cybersecurity_nelle_reti_di_fabbrica_P/))
* - [Cyber Range: Analyzing a Cyber Attack](/files/slides/20200922-cyberrange.pdf "View slides")
* - [Securing OT/ICS plants](/files/slides/20200623-clubitfvg-securing-ot-ics-plants.pdf "View slides")
* - [Automation for Cisco NetOps](/files/slides/20190226-automation-for-cisco-netops.pdf "View slides")
* - [SDN, Complexity and TCO](/files/slides/20181107-ciscon-sdn-complexity-and-tco-looking-for-an-easy-way.pdf "View slides")
* - [Protection and visibility for enterprise networks](/files/slides/20181003-nts-protection-and-visibility-for-enterprise-networks.pdf "View slides")
* - [Why WAN AccelerAtors (still) matter?](/files/slides/20141106-festival-ict-why-wan-accelerators-still-matter.pdf "View slides")
* - [Designing an Hybrid Data Center Infrastructure](/files/slides/20130918-festival-ict-designing-an-hybrid-data-center-i...