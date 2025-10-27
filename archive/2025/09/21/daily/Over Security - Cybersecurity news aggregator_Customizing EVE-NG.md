---
title: Customizing EVE-NG
url: https://www.adainese.it/blog/2024/07/27/customizing-eve-ng/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-21
fetch_date: 2025-10-02T20:29:03.107566
---

# Customizing EVE-NG

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Customizing EVE-NG

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

## Customizing EVE-NG

Andrea Dainese

July 27, 2024

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/eve-ng.webp)](/images/vendors/eve-ng.webp)

Let’s delve into the most important part: customizing EVE-NG for DevNetOps. In particular, we will proceed to:

* Configure an internal network dedicated to device management.
* Import the labs from the
  [GitHub repository](https://github.com/dainok/courses)
   dedicated to DevNetOps courses.
* Compile and install
  [Python](https://www.python.org/)
   3.10 (not required in EVE-NG 6)
* Create a user dedicated to development, with a dedicated Pythonenvironment.
* Utilize
  [Visual Studio Code](https://code.visualstudio.com/)
   for remote development on the EVE-NG server.

## Configure an Internal Management Network

In automation, each lab we create requires a seemingly trivial yet essential characteristic: the IP addresses of the devices must be accessible from the automation system. If the
[EVE-NG PRO](https://www.eve-ng.net/index.php/features-compare/)
 version has a native feature (NAT Cloud) that simplifies this, in EVE-NG CE, we need to find a strategy to achieve the same result.

The goal is to configure an additional network on EVE-NG that allows us to connect the management interfaces of the devices we will use for our labs, whether they are virtual (internal to EVE-NG) or physical (PLC and other external physical devices). The diagram below summarizes our intention:

[![Patreon Image](/blog/2024/07/27/customizing-eve-ng/9415f3cf67808299903b7efd695cc12d.webp)](/blog/2024/07/27/customizing-eve-ng/9415f3cf67808299903b7efd695cc12d.webp)

Firstly, let’s clarify the networking of EVE-NG and introduce some concepts in Linux in general.

A Linux system represents its network interfaces with various names, typically prefixed (**eth**, **ens**…) associated with an identifier number. Network interfaces can represent either a physical network card or a virtual network card. In our environment, we find that the physical network card is represented by **eth0**, but there are other network cards named **pnet**.

We can view the network interfaces of the system with one of the following commands:

```
ifconfig -a
ip link
```

The configured **pnet** interfaces are actually virtual switches (bridges) configured by default during installation:

[![Patreon Image](/blog/2024/07/27/customizing-eve-ng/a2cef7f1044efc96d7bcbbd6d9a4d230.webp)](/blog/2024/07/27/customizing-eve-ng/a2cef7f1044efc96d7bcbbd6d9a4d230.webp)

In particular, we see that the bridge **pnet0** is associated with the physical interface **eth0**. Or, in other words, anything associated with the bridge **pnet0** will also be transmitted on the **eth0** network. As we’ll see in the web interface, we can add Cloud networks. Cloud networks are simply the **pnet** bridges. In particular, the **pnet0** network is also used for web access. In fact, the management IP address is associated with the bridge **pnet0**, as we can see using one of the following commands:

```
ifconfig pnet0
ip address show pnet0
```

We can then configure an IP address on the **pnet9** network and connect the management interfaces of the devices to the **Cloud9** network.

EVE-NG, based on Ubuntu Linux Server 20.04 LTS, configures networks via the **/etc/network/interfaces** file. In particular, we need to configure the part related to the **pnet9** bridge as follows:

[![Patreon Image](/blog/2024/07/27/customizing-eve-ng/15625cd4f79dad09bfeeea609e5ae346.webp)](/blog/2024/07/27/customizing-eve-ng/15625cd4f79dad09bfeeea609e5ae346.webp)

We use the
[APIPA](https://en.wikipedia.org/wiki/Link-local_address)
 network, defined to be local. In this sense, in an Enterprise context, we have reasonable certainty of not overlapping with other networks. The remaining **pnet2-9** interfaces can be deleted.

We can now reload the modified network configuration:

```
/etc/init.d/networking restart
```

If we ever want to associate a physical interface with this bridge, we need to add the line:

```
bridge_ports eth1
```

Continue reading
[the post on Patreon](https://www.patreon.com/posts/customizing-eve-108921627)
.

## Andrea Dainese

For information, collaborations, proposals, requests for help, donations, use one of the following channels; email is preferred.

#### Past events

* - [SDN: Software Defined Now](/files/slides/20240305-cisco-aci-automation.pdf "View slides")
* - [Cybercrime](/files/slides/20231122-cybercrime.pdf "View slides")
* - [BGP attack scenarios](/files/slides/20220901-bgp-attack-scenarios.pdf "View slides")
* - [Approaching OT/ICS Security](/files/slides/20220317-approaching-ot-ics-security.pdf "View slides") (with [Festo Academy](https://www.festocte.it/eventi/industry_4_0/17-03-2022/webinar_la_cybersecurity_nelle_reti_di_fabbrica_P/))
* - [Cyber Range: Analyzing a Cyber Attack](/files/slides/20200922-cyberrange.pdf "View slides")
* - [Securing OT/ICS plants](/files/slides/20200623...