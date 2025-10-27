---
title: Improving IaC with Spacelift
url: https://www.adainese.it/blog/2022/10/31/improving-iac-with-spacelift/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-30
fetch_date: 2025-10-03T21:19:38.366813
---

# Improving IaC with Spacelift

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Improving IaC with Spacelift

#### Table of contents

* [Stacks: run instances from GitHub](#stacks-run-instances-from-github)
* [Environment and context](#environment-and-context)
* [Policies: binding Terraform and Ansible together](#policies-binding-terraform-and-ansible-together)
* [Manual actions](#manual-actions)
* [Everything good?](#everything-good)
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

## Improving IaC with Spacelift

Andrea Dainese

October 31, 2022

[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/spacelift.webp)](/images/vendors/spacelift.webp)

This is the third part of my IaC overview based on a personal experiment: building Cyber range using the IaC paradigm. Here is the
[first](https://www.adainese.it/blog/2022/10/29/infrastructure-as-code-for-cyber-ranges/ "Infrastructure as code for Cyber Ranges")
and
[second](https://www.adainese.it/blog/2022/10/30/ansible-with-bastion-host/ "Ansible with bastion host")
parts.

A few weeks ago I met Spacelift and I had the chance to test their product. Spacelift is described as:

> Collaborative Infrastructure for modern software teams

In practice, Spacelift offers a web UI and a framework to maintain, test, and organize infrastructures using the IaC (Infrastructure as Code) paradigm.

I decided to adapt my playbooks so they could be managed within Spacelift. Even if I like Spacelift very much, I always plan an exit strategy. In practice, I can run my playbooks outside Spacelift, and this is useful to me for developing, testing, and debugging. I consider this a “soft” lock-in, and this is very important to me.

This post summarizes how I used Spacelift for my simple scenario. Mind that Spacelift is more powerful and can actually cover a lot of complex scenarios.

## Stacks: run instances from GitHub

From the official doc page:

> Stack is one of the core concepts in Spacelift. […] You can think about a stack as a combination of source code, the current state of the managed infrastructure (eg. Terraform state file), and configuration in the form of environment variables and mounted files.

In my scenario, I need two stacks: one for Terraform and another one for Ansible. I have seen three approaches to build and maintaining stacks:

* fully manual: all stacks are created by humans;
* fully automated: all stacks are created by Terraform;
* hybrid: the main stack create secondary tasks.

In the fully automated approach, all stacks and relationships between them are created by Terraform. Everything around Spacelift can be managed with the IaC paradigm, so this could be the best way for many DevOps engineers. Sometimes the “builder” stacks are managed within Spacelift too: in this case, the stack which can manipulate Spacelift projects must be `administrative`.

In my scenario, I used a hybrid approach: the main stack builds dependent stacks and the relationship between them, but it also creates the AWS infrastructure. In short, my Terraform stack:

* is created manually from a GitHub repository;
* is triggered on every GitHub commit;
* after the plan phase a manual confirmation is required;
* is responsible to build the Ansible stack and related policies and environments;
* is responsible to build the AWS infrastructure;
* is responsible to trigger the Ansible stack.

Let’s see how to build the Terraform stack:

* Provider: GitHub
* Repository: dainok/iac
* Branch: master
* Project root: lab-all-in-one-vulnerable-website
* Backend: Terraform
* Administrative: true
* Name: lab-all-in-one-vulnerable-website

Once it has been created, the stack can be triggered:

[![Spacelift run view](/blog/2022/10/31/improving-iac-with-spacelift/spacelift-stack-run.png)](/blog/2022/10/31/improving-iac-with-spacelift/spacelift-stack-run.png)

## Environment and context

Spacelift stacks can be configured with environment variables (within the stack itself) or context (a sort of shared environment). My approach is to define context containing data that can be shared between stacks:

[![Spacelift context](/blog/2022/10/31/improving-iac-with-spacelift/spacelift-context.png)](/blog/2022/10/31/improving-iac-with-spacelift/spacelift-context.png)

Context can contain both environment variables and files. In my scenario I use:

* a context defining Spacelift API token;
* a context defining AWS API token;
* a context built by the Terraform stack sharing some data between the Terraform and the Ansible stack.

To be more specific the last context is used to share the SSH private key with the Ansible stack and to set some Ansible environment variables.

## Policies: binding Terraform and Ansible together

> Spacelift uses an open-source project called Open Policy Agent and its rule language, Rego, to execute user-defined pieces of code we call Policies at various decision points.

Policies can be used to modify the stack behavior. For example, additional security checks can be implemented, or a specific user is required to approve the plan. In my case I used:

* a push policy to avoid automatic triggering of the Ansible stack after a commit;
* a tri...