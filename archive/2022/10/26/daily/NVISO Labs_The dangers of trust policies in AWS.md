---
title: The dangers of trust policies in AWS
url: https://blog.nviso.eu/2022/10/25/the-dangers-of-trust-policies-in-aws/
source: NVISO Labs
date: 2022-10-26
fetch_date: 2025-10-03T20:53:18.452386
---

# The dangers of trust policies in AWS

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

# The dangers of trust policies in AWS

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[AWS](https://blog.nviso.eu/category/cloud-security/aws/), [Cloud Security](https://blog.nviso.eu/category/cloud-security/)

October 25, 2022May 26, 2023
4 Minutes

# Introduction

Everyone that has used Amazon Web Services (AWS) knows that the cloud environment has a unique way of granting access to users and resources. This is done by allowing users and/or resources to temporarily assume roles. These kinds of actions are possible because of trust policies that are assigned to those roles. A trust policy is a document that is attached to every role in an AWS environment. This document describes what users, groups, roles and/or resources are allowed to temporarily assume the role in order to perform actions.

Trust policies are very useful to temporarily grant specific access to a user or a resource. They add a layer of protection on the roles to avoid misuse by an adversary. Trust policies are most commonly used in either of following four cases:

* Allowing an AWS service to access another AWS service
* Allowing cross-account access between two AWS accounts
* Allowing a third-party web identity access to the AWS account
* As a means of single sign-on authentication

# Benefits and dangers of trust policies

There are many possible implementations of a trust policy. Below are two examples of trust policies and their use cases.

***Example 1:** a role is created that has access to a lambda function. The trust policy for this role is made so that everyone has access to this role (using the “\*” wildcard). This could be used when a website has a lambda function that calculates something unique, which everyone should be able to use.*

***Example 2:** there are two AWS accounts, one of which is used to run an application that is publicly available and the other is used for security monitoring on other AWS accounts. In this setup, there is a lambda function in the public AWS account that pushes all logs from the public account to the logging AWS account. For this, a role is created inside the security monitoring AWS account that can be assumed by the lambda function on the public account.*

![Visualized setup of Example 2](https://blog.nviso.eu/wp-content/uploads/2022/10/Setup-example-2.png)

Figure 1: Visual of the setup of Example 2

Both examples described above have some fundamental problems with their trust policies. In Example 1, we allow anyone and everything access to our lambda function. Any mistake in the code can therefore be exploited and can lead to an initial foothold on the AWS account. Even more drastically, if the permissions of the role do not limit access to just the single lambda, anyone can have access to any lambda function in the AWS account!

Even more problematic, there is an attack technique that uses trust policies to allow external enumeration of users and roles on a target environment. An adversary wouldn’t even need access to this environment in order to enumerate the names of users and roles. The core of the attack relies on the following: The attacker has a role on their environment with an initial trust policy attached to it. By changing the trust policy, they can attempt to allow or deny target users or roles access to their own role. If the change causes an error, the user or role does not exist. Similarly, if the change is successful, the user or role exists. Adversaries use this commonly in the wild to enumerate roles and attempt to assume the discovered roles. In Example 1, because the trust policy allows anyone to access the role, this will create an initial foothold in the AWS account.

In Example 2, we are going to assume that the adversary already has an initial foothold in the AWS account. A real-life scenario of this could be a compromised or dissatisfied programmer that has the option to modify lambda functions. Any permission that the lambda function has can therefore be abused to get more information on the security monitoring AWS account. A single permission problem can therefore be abused and have disastrous consequences on this sensitive environment.

![Visualized attack on Example 2](https://blog.nviso.eu/wp-content/uploads/2022/10/Attack-1-example-2.png)

Figure 2: Example of an attack executed on Example 2

# Best practices for trust policies

A trust policy allows a user or resource to access a specific set of permissions inside an AWS account. Because of this, it is important that clear boundaries are defined to avoid adversaries abusing the role. The best practice for trust policies is to limit the resources, users, groups and roles that have access to them. Avoid the “\*” wildcard at all cost and limit access to the role to a single service or a single group in the AWS account. If we look back at Example 1, a better implementation would be to only allow the website access to the lambda function. This way, all traffic can first be filtered out by the website before being sent to the lambda function.

Overall, it is best to avoid using cross-account trust policies since they allow lateral movement between AWS accounts. However, since this is not always possible, following best practice can help you better protect your AWS accounts: Before setting up the cross-account trust policy, first identify the most sensitive of two accounts. This account is the one that will perform the action, since this is the most trusted account. If we want to reengineer Example 2, we could set up a function inside the security monitoring AWS account instead of the public AWS account. This function would then have access to a role on the public AWS account and would pull the data from that account into its own.

![Visualized potential solution for Example 2](https://blog.nviso.eu/wp-content/uploads/2022/10/Solution-example-2.png)

Figure 3: An example of a “better” solution for Example 2

# Conclusion

Using trust policies allows for many opportunities and complex setups. However, with a lot of possibilities also comes a lot of responsibility. Therefore, it is important to properly plan trust relations before implementing them.

When setting up trust policies, always ensure that the policy applies to the least possible number of users or resources. Also make sure that the more sensitive resources or accounts perform the actions on the le...