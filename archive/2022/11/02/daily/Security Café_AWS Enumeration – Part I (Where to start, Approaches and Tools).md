---
title: AWS Enumeration – Part I (Where to start, Approaches and Tools)
url: https://securitycafe.ro/2022/11/01/aws-enumeration-part-1/
source: Security Café
date: 2022-11-02
fetch_date: 2025-10-03T21:32:47.514431
---

# AWS Enumeration – Part I (Where to start, Approaches and Tools)

[Skip to content](#content)

[Security Café](https://securitycafe.ro/)

Security Research and Services

* [Things we do on a daily basis](https://securitycafe.ro/security-services-for-business/)
  + [Red Team (DORA/TIBER) exercises](https://securitycafe.ro/security-services-for-business/dora-tiber-exercises/)
  + [Web Application Penetration Testing](https://securitycafe.ro/security-services-for-business/web-application-penetration-testing/)
  + [Mobile Application Penetration Testing](https://securitycafe.ro/security-services-for-business/mobile-application-penetration-testing/)
  + [Infrastructure Penetration Testing](https://securitycafe.ro/security-services-for-business/infrastructure-penetration-testing/)
  + [Vulnerability Assessment](https://securitycafe.ro/security-services-for-business/vulnerability-assessment/)
* [CVEs, Talks and Tools](https://securitycafe.ro/cves-talks-and-tools/)
* [Contact](https://securitycafe.ro/contact/)
* [About](https://securitycafe.ro/about/)

[![](https://securitycafe.ro/wp-content/uploads/2015/01/cropped-cropped-coffee-banner-2-4.jpg)](https://securitycafe.ro/)

![](https://securitycafe.ro/wp-content/uploads/2022/10/aws-enumeration-feature-image.png?w=840)

# AWS Enumeration – Part I (Where to start, Approaches and Tools)

[November 1, 2022](https://securitycafe.ro/2022/11/01/aws-enumeration-part-1/ "10:30 am") [Eduard Agavriloae](https://securitycafe.ro/author/eagavriloae/ "View all posts by Eduard Agavriloae") [aws](https://securitycafe.ro/category/cloud-security/aws/), [Cloud Security](https://securitycafe.ro/category/cloud-security/) [Leave a comment](https://securitycafe.ro/2022/11/01/aws-enumeration-part-1/#respond)

This article is covering multiple ways to enumerate the resources within an AWS environment. We’ll explain how to perform enumeration, what you should look for, and multiple ways of doing it, both automated and manual.

## 1. What you should look for

First, the easiest way to identify attack vectors or misconfigurations is to perform a complete enumeration. This includes all the resources, permissions, and configurations.

However, not everything deserves the same attention. A higher focus should be put on services from which you can exfiltrate access credentials or on IAM resources that can lead to privilege escalation.

Additionally, you must know your goal. If you’re performing a cloud security configuration review, then you should focus on anything that can be improved, like encryption at rest or in transit, proper logging practices, and so on. Whereas, if you’re on a penetration testing/red team engagement, the previously mentioned aspects would not be of interest and the focus should be on practical exploitation.

## 2. Prerequisites

The ideal way to perform discovery and enumeration is by having read-only access over all the resources within the target account.

For this, there are two options:

* The client provides a role with global read-only permissions that we will assume from our account
* The client provides access to a user within the target account that has global read-only permissions

From these options, the simpler one for both parties is the role-based approach. For the second option, we would need to receive a set of access keys in order to perform checks from AWS CLI and automated tools.

There’s also the scenario where the client wants to simulate an insider threat and gives us the same level of access as another account, a case in which we might have both read and write permissions.

## 3 Manual discovery and enumeration

### 3.1Enumerate everything

A good approach, especially when you also want to improve your AWS knowledge, is to enumerate literally everything by using AWS CLI.

How can you do this? Well, an AWS CLI command has the next structure:

```
aws [options] <command> <subcommand> [parameters]

# For example:
aws --region eu-central-1 ec2 describe-instances --instance-ids $instance_id
```

Every command and subcommand has good documentation that can be accessed appending `help` at the end of the command.

```
# get general help, list global parameters and list services
aws help

# get subcommands available to a certain service
aws ec2 help

# get details about parameters available,
# examples and more for a certain subcommand
aws ec2 describe-instance help
```

So, if you’re new to AWS and don’t know where to start, just type `aws help` and see the list of available services.

![](https://securitycafe.ro/wp-content/uploads/2022/10/aws-cli-available-services.png?w=327)

List of services from AWS CLI

Next, choose a service or just take each one at a time and start the enumeration. There are 3 keywords available for every service that are pointing to an enumeration subcommand: describe, list, and get. The exception is the s3 service which uses ls as a subcommand for enumeration.

Nonetheless, just choose a service and hit `aws service help`. Now, look for subcommands that contain “describe”, “list” and “get”. Let’s do an example with Lambda Functions.

![](https://securitycafe.ro/wp-content/uploads/2022/10/aws-cli-lambda-enumeration-commands.jpg?w=618)

Lambda enumeration commands

In the above screenshot, we got a list of the commands that we can use to enumerate the Lambda service. Note that some subcommands will require information already gathered in order to enumerate. For example, by running `list-functions` we’ll get the list of lambda functions. Based on this information we can enumerate further with other commands like `get-policy`.

One trick to simplify the process is to directly run the subcommand. If you’re missing arguments, the AWS CLI will return an error and specify what mandatory parameters you should feed.

![](https://securitycafe.ro/wp-content/uploads/2022/10/aws-cli-mandatory-parameters.png?w=712)

Mandatory parameters for subcommand

This process is very time-consuming but is helping you to better understand what AWS has to offer, what you should enumerate, and what are the common services that you can prioritize in the next engagement.

The last thing to keep in mind is that some AWS resources are region dependent, meaning that if you configured your AWS CLI on eu-central-1 and that resource is created in us-east-1, then you would not be able to identify it without mentioning the right region.

In part II of this article, we’ll provide a list of the most useful enumeration commands based on the service’s importance and the risk that a misconfiguration can bring there.

### 3.2 CIS Benchmarks

You can use the CIS benchmarks to go through some of the most common and of interest services in order to see what the target is using.

Although these resources are better for performing a cloud configuration review if you have limited experience with AWS this would help you to get started. The benchmark is especially useful for learning because it details the risk, but also provides remediation solutions.

References:

* CIS Amazon Web Services Foundations Benchmark v1.4.0
* CIS AWS End User Compute Services Benchmark v1.0.0
* CIS Amazon Web Services Three-tier Web Architecture Benchmark v1.0.0

The CIS benchmarks can be downloaded from <https://downloads.cisecurity.org/> once you made a free account.

### 3.3 AWS Resource Groups & Tag Editor

At the moment, AWS doesn’t have a central dashboard for viewing all the resources and services used. However, if you have access to the web console, you can use the service AWS Resource Groups & Tag Editor for enumerating all the resources within the account. The next screenshot exemplifies this:

![](https://securitycafe.ro/wp-content/uploads/2022/10/aws-web-console-resource-groups-and-tag-editor.png?w=1024)

Enumeration using Tag Editor

The advantages are:

* You can search across all regions at once
* You can search for all the services at once
* You get an exportable list with all the identified resources

The disadvantages, however:

* The search result will identify maximum 500 items in a single s...