---
title: The cost of complexity: Ansible AWX
url: https://www.adainese.it/blog/2024/05/05/the-cost-of-complexity-ansible-awx/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-06
fetch_date: 2025-10-06T17:15:52.198469
---

# The cost of complexity: Ansible AWX

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# The cost of complexity: Ansible AWX

#### Table of contents

* [AWX Operator](#awx-operator)
* [Reboot](#reboot)
* [Ansible Galaxy](#ansible-galaxy)
* [paramiko vs pylibssh](#paramiko-vs-pylibssh)
* [Bastion host](#bastion-host)
* [Authentication](#authentication)
* [Conclusions](#conclusions)

#### Latest posts

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/10/05/creating-an-interface-in-strata-cloud-manager/)

[Creating an interface in Strata Cloud Manager](/blog/2025/10/05/creating-an-interface-in-strata-cloud-manager/)
October 05, 2025

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

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 160 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 124 posts

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

## The cost of complexity: Ansible AWX

Andrea Dainese

May 05, 2024

[Automation](/categories/automation/ "All posts under Automation"),
[Infrastructure](/categories/infrastructure/ "All posts under Infrastructure")

[![Post cover](/images/vendors/ansible.webp)](/images/vendors/ansible.webp)

For several years now, [Ansible AWX](https://github.com/ansible/awx "Ansible AWX") has been on my ToDo list. I have always postponed dealing with it due to its complexity, but today I find myself having to tackle it. I knew it would be challenging, but I didn’t imagine just how much.

This post aims to summarize the steps to install a development instance of AWX and discuss the enormous, unnecessary, and harmful complexity that our infrastructures have reached.

## AWX Operator

First and foremost, it’s essential to note that AWX is available via containers on the [Kubernetes](https://kubernetes.io/ "Kubernetes") platform. My attempts to run the application in standalone mode or as a simple container on [Docker](https://www.docker.com/ "Docker") were futile.

I chose to prepare an Ubuntu Linux 22.04 VM on which I installed [Minikube](https://minikube.sigs.k8s.io/docs/ "Minikube"). Minikube, in turn, installs a reduced version of [Kubernetes](https://kubernetes.io/ "Kubernetes").

To summarize:

* My lab contains a VMware vSphere cluster;
* Within the cluster, there is a virtualized instance of [Ubuntu Linux 22.04](https://ubuntu.com/ "Ubuntu Linux");
* On the Linux system, a [Kubernetes](https://kubernetes.io/ "Kubernetes") environment is virtualized (created through [Minikube](https://minikube.sigs.k8s.io/docs/ "Minikube"));
* On [Kubernetes](https://kubernetes.io/ "Kubernetes"), we install [Ansible AWX](https://github.com/ansible/awx "Ansible AWX") using the [AWX Operator](https://github.com/ansible/awx-operator "AWX Operator") application.

For the details of the individual steps, I refer you to the two links by Christopher Hart at the end of the post.

The reflection I want to make concerns the complexity of the environment necessary to run what is an orchestrator of playbooks. The probability that something will go wrong in the setup is very high, and debugging any problems requires expertise in many, too many, different environments. Not to mention how to update, backup, restore, or design the disaster recovery process for such a solution.

## Reboot

After a few hours of use, I realize that my instance of AWX is no longer working correctly. The reason becomes almost immediately apparent: the disk space of the Ubuntu Linux system was exhausted. I extend the disk space and restart the system… but AWX doesn’t seem to start.

In order, I verify:

* Docker on Ubuntu Linux;
* Minikube;
* Docker within Kubernetes;
* The AWX containers within Kubernetes.

```
minikube status
minikube restart
minikube kubectl -- get pods -A
minikube service list
kubectl logs --namespace=awx -p svc/awx-service
kubectl get services --namespace awx
```

After a few minutes, the AWX service responds, but it is not exposed. A few more minutes, and I manage to reach the login page again.

## Ansible Galaxy

The playbooks I wrote use the `cisco.ios` collection, which is installed by default with [Ansible](https://www.ansible.com/ "Ansible"), but it seems not to exist in AWX. I discover that there is a specific format for defining the dependencies of an AWX project. You need to create the `collections/requirements.yml` file indicating the necessary dependencies:

```
collections:
- name: cisco.ios
  version: 8.0.0
  source: https://galaxy.ansible.com
```

I rerun the playbook and move on to the next error.

## paramiko vs pylibssh

The next error indicates the use of `paramiko` instead of `ansible-pylibssh`:

```
ASK [cisco_ios_system : SETTING FACTS] ****************************************
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
ok: [sw1.example.com]
ok: [sw2.example.com]
TASK [cisco_ios_system : CONFIGURING HOSTNAME AND DOMAIN NAME] *****************
fatal: [sw2.example.com]: FAILED! => {"changed": false, "msg": "No existing session"}
fatal: [sw1.example.com]: FAILED! => {"changed": false, "msg": "No existing session"}
```

However, the `cisco.ios` collection requires the use of `ansible-pylibssh`, not present by default on Ansible and AWX, which instead use `paramiko`. With little hope, I force the use of `pylibssh`, configuring in the inventory:

```
ansible_network_cli_ssh_type: libssh
```

I rerun the playbook, and indeed the error reports the absence of the library:

```
TASK [cisco_ios_system : CONFIGURING HOSTNAME AND DOMAIN NAME] *****************
fatal: [sw1.example.com]: FAILED! => {"changed": false, "msg": "Failed to i...