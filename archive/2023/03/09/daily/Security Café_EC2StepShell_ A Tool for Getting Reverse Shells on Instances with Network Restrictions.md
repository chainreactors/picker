---
title: EC2StepShell: A Tool for Getting Reverse Shells on Instances with Network Restrictions
url: https://securitycafe.ro/2023/03/08/ec2stepshell-reverse-shells-private-ec2-instances/
source: Security Café
date: 2023-03-09
fetch_date: 2025-10-04T09:01:48.493170
---

# EC2StepShell: A Tool for Getting Reverse Shells on Instances with Network Restrictions

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

![](https://securitycafe.ro/wp-content/uploads/2023/02/feature-image-ec2stepshell-4.png?w=588)

# EC2StepShell: A Tool for Getting Reverse Shells on Instances with Network Restrictions

[March 8, 2023](https://securitycafe.ro/2023/03/08/ec2stepshell-reverse-shells-private-ec2-instances/ "9:30 am") [Eduard Agavriloae](https://securitycafe.ro/author/eagavriloae/ "View all posts by Eduard Agavriloae") [Announcements](https://securitycafe.ro/category/announcements/), [aws](https://securitycafe.ro/category/cloud-security/aws/), [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Penetration Testing](https://securitycafe.ro/category/penetration-testing/) [Leave a comment](https://securitycafe.ro/2023/03/08/ec2stepshell-reverse-shells-private-ec2-instances/#respond)

A tool for getting reverse shells in EC2 instances where network communication to your host is restricted.

In my last article, [AWS ssm:SendCommand or network agnostic built-in RCE as root](https://securitycafe.ro/2023/01/17/aws-post-explitation-with-ssm-sendcommand/), I talked about how ssm:SendCommand can be used to execute code under high privileges on EC2 instances along with the prerequisites needed to complete the attack chain.

One topic of interest was getting reverse shells, which was easy for public EC2 instances, but didn’t work with private and network restricted instances.

Well, I made a tool that fixes this and in this article I’ll show you how to use it.

## About the tool

EC2StepShell is an open-source AWS post-exploitation tool for getting high privileges reverse shells in public or private EC2 instances. It works by sending commands to EC2 instances with ssm:SendCommand and then retrieves the output using ssm:ListCommandInvocations.

The tools shines for EC2 instances that can’t establish network communication with your host (private EC2 instances or with restrictive security groups).

You can find the tool on:

* GitHub: <https://github.com/saw-your-packet/EC2StepShell>
* PyPi: <https://pypi.org/project/EC2StepShell/>

## Usage

Let’s go straight into it so that you can get hacking. We’ll see in the next chapters more technical details.

```
# Installation
python3 -m pip install EC2StepShell

# Help menu
python3 -m ec2stepshell -h

# Most basic usage
python3 -m ec2stepshell $instance_id --region $region
```

![](https://securitycafe.ro/wp-content/uploads/2023/02/zoomed-short-demo-ec2stepshell.gif?w=800)

Now, if you run the tool like this, the default profile configured in AWS CLI will be used to start the reverse shell. The tool also supports custom profiles, temporary access credentials and persistent access credentials.

```
# running using the default profile configured in AWS CLI
python -m ec2stepshell $instance_id --region $region

# running using a specific profile configured in AWS CLI
python -m ec2stepshell $instance_id --region $region --profile $profile

# running using persistent access credentials
python -m ec2stepshell $instance_id --region $region --access-key $access_key --secret-key $secret_key

# running using temporary access credentials
python -m ec2stepshell $instance_id --region $region --access-key $access_key --secret-key $secret_key --session-token $session_token
```

## How it works

The tool doesn’t directly interact with the EC2 instance. Instead, it communicates with the service AWS Systems Manager (SSM).

To act like reverse shell, the tools does two things:

1. Sends the user’s command by calling ssm:SendCommand
2. Retrieves the command’s output

The 2 steps are inside a “while True” loop.

![](https://securitycafe.ro/wp-content/uploads/2023/02/ec2stepshell-architecture.jpg?w=599)

Before starting the shell, there is an initialization process. In this phase, the running OS on the instance, the host’s name and the current working directory are determined. With this information the command input line is constructed so that it would like like a SSH connection.

![](https://securitycafe.ro/wp-content/uploads/2023/02/ec2stepshell-initialization.png?w=331)

Even if the OS is mentioned using input arguments, the tool still verifies if the mentioned OS is right and tries to self determine it otherwise.

This is how the process looks like for both UNIX and Windows. In the first image we manually specified that the OS is Windows, but the instance is running on Linux.

![](https://securitycafe.ro/wp-content/uploads/2023/02/ec2stepshell-initialization-demo.png?w=770)

In the next image we didn’t specify the OS, but the tool automatically determined that it is Windows.

![](https://securitycafe.ro/wp-content/uploads/2023/02/ec2stepshell-initialization-windows-demo.jpg?w=891)

## Requirements

The tool is meant to be used in a post-exploitation scenario, so you need to have access within the AWS environment. The type of access required by the tool is programmatic access, meaning access credentials. Both temporary and persistent access credentials are fine.

Only two permissions are needed for the tool to work:

* ssm:SendCommand
* ssm:ListCommandInvocations

The action ssm:SendCommand must be granted over the target EC2 instance and the documents:

* AWS-RunShellScript
* AWS-RunPowerShellScript

I tested the tool with the next policy and it worked just fine:

![](https://securitycafe.ro/wp-content/uploads/2023/02/ec2s2-minimum-permissions.png?w=431)

Usually organizations are not restricting the access to only certain documents, but this is what permissions you need in a more granular approach:

![](https://securitycafe.ro/wp-content/uploads/2023/02/ec2s2-minimum-permissions-granular.png?w=631)

What if you don’t know if you meet the requirements? Well, if you have the instance’s ID and you know the region, just run the tool and see if you get a shell. Worst case scenario, you’ll get an Access Denied error, but best case scenario you get a high privileges reverse shell.

## Advanced usage

When sending a command, there is an initial wait time of 0.7 seconds before attempting to retrieve the output. If the output is not retrieved, then a retry process starts.

The tool will retry 3 times to get the output and between each retry there is a wait time of 0.3 seconds.

![](https://securitycafe.ro/wp-content/uploads/2023/02/ec2s2-retry-flow.png?w=612)

This works fine for Linux instances, even if they are t2.micro. I wanted to make the shell as responsive as possible by default, without affecting the availability. However, this will not work as well for Windows instances. This is the reason why you can and should modify the initial delay, the number of retries and the retry delay.

![](https://securitycafe.ro/wp-content/uploads/2023/02/ec2s2-help-menu.png?w=1024)

For a t2.micro Windows Server instance I had to adjust the initial delay to 2.5 seconds and the retry delay to 0.7 in order to make it work alright. Depending on the instance’s performan...