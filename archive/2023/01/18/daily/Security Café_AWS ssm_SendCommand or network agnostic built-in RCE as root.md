---
title: AWS ssm:SendCommand or network agnostic built-in RCE as root
url: https://securitycafe.ro/2023/01/17/aws-post-explitation-with-ssm-sendcommand/
source: Security Café
date: 2023-01-18
fetch_date: 2025-10-04T04:09:33.911107
---

# AWS ssm:SendCommand or network agnostic built-in RCE as root

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

![](https://securitycafe.ro/wp-content/uploads/2023/02/feature-post-exploitation.jpeg?w=840)

# AWS ssm:SendCommand or network agnostic built-in RCE as root

[January 17, 2023](https://securitycafe.ro/2023/01/17/aws-post-explitation-with-ssm-sendcommand/ "8:53 pm") [Eduard Agavriloae](https://securitycafe.ro/author/eagavriloae/ "View all posts by Eduard Agavriloae") [aws](https://securitycafe.ro/category/cloud-security/aws/), [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Penetration Testing](https://securitycafe.ro/category/penetration-testing/) [2 comments](https://securitycafe.ro/2023/01/17/aws-post-explitation-with-ssm-sendcommand/#comments)

Post-exploitation in cloud can be fun and easy if you have the right permissions. There is no other permission that I would rather have than ssm:SendCommand. In this article I’ll present you multiple attack vectors that would help you in further compromising the cloud environment and escalating your privileges. Let’s get hacking!

## 1. What is SSM

SSM stands for Simple Systems Manager, but that is its old name. Now is called just Amazon Systems Manager.

The service exposes multiple features that allow you to manage your EC2 instances among other things. For SSM to work you need to install the SSM Agent on the target EC2 instance, ensure that communication with the SSM API can be established and grant set of basic permissions to the instance.

Once the prerequisites are met, you can control the instance(s) from SSM either individually or multiple at once. The fact that you can manage tens of instances at once is exactly why most organizations are using SSM.

The most common features are:

* Patch Manager – Used to apply patches simultaneously on multiple instances
* Session Manager – SSH connection to instance even if you don’t have the SSH private key or if the SSH port is not reachable from your IP
* Run command – Perform operations through documents (kind of local binaries/script), including running system commands
* Compliance – Checks compliance of various conditions across multiple instances
* Automation – Simplifies common maintenance and deployment tasks, but cannot be scheduled
* Inventory – Provides visibility into your EC2 instances and on-premises computing environment

So, how does it work? Well, like most of AWS services, it has a dashboard from where you can use the mentioned features giving that you have the right permissions to do so. The next screenshot illustrates the SSM dashboard from Inventory.

![](https://securitycafe.ro/wp-content/uploads/2023/01/aws-ssm-example-dashboard.png?w=1024)

Amazon Systems Manager can also be used from AWS CLI which we’ll leverage later as part of the exploitation process.

## 2. ssm:SendCommand

As you can see, SSM is a powerful service and access to it should be granted only to authorized entities and as granular as possible. We’ll see in the next chapter what can cause a violation of least privilege principle.

Now, “ssm:SendCommand” is the permission required for using the Run Command feature. We briefly presented it in the previous chapter, but let’s detail it.

Run Command works by specifying a document along with the required parameters and the target instance(s). AWS says that “An AWS Systems Manager document (SSM document) defines the actions that Systems Manager performs on your managed instances”. Consider a document a binary/script that is executed on the target instance. In reality, a SSM document is just a JSON with various fields that is interpreted by the SSM Agent on the instance.

There are over 100 documents predefined in SSM, but among these, two are most of interest: AWS-RunShellScript (works on Linux and MacOS) and AWS-RunPowerShellScript (works on Windows and Linux). Both are executing system commands, which is basically a built-in RCE.

You can use any of them in the next manner:

```
# this will return the command ID which you'll need in order to retrieve the execution's result
aws ssm send-command --instance-ids $ec2_instance_id --document-name "AWS-RunShellScript" --parameters commands=$command

# get command output
aws ssm list-command-invocations --command-id $command_id --details
```

![](https://securitycafe.ro/wp-content/uploads/2023/01/image.png?w=1024)

In the screenshot above we executed the “id” command and retrieved the execution’s output. Notice something weird? The command executed as **root**. I can tell you that the same thing is available for Windows, where the commands are executed under **NT** **Authority\SYSTEM**. We’ll get into why that happens in chapter 4. But until then, notice that “send-command” works with the parameter “–instance-id**s**“, meaning that you can launch the same command at once against multiple EC2 instances.

To familiarize yourself with this feature and its documents I recommend using the web portal where you can easily navigate through documents and execute them against instances from your account.

![](https://securitycafe.ro/wp-content/uploads/2023/01/image-1.png?w=1024)

Before we move further, as you noticed, you need to know the instance’s ID in order to send commands to it. For getting it, you will need additional permissions. There are high chances that the EC2 instance will have other policies (e.g for sending logs). Below are some commands that you can blindly try. If you have permissions for at least one of them, instance ids will be returned in most of the cases. Just make sure you are in the right region or try multiple regions. You can change the region from AWS CLI with “aws configure set region <region>”.

* aws ec2 describe-instances
* aws ec2 describe-addresses
* aws ec2 describe-volumes
* aws ec2 describe-bundle-tasks
* aws ec2 describe-classic-link-instances
* aws ec2 describe-conversion-tasks
* aws ec2 describe-elastic-gpus
* aws ec2 describe-export-tasks
* aws ec2 describe-fleets
  + aws ec2 describe-fleet-instances –fleet-id $fleet\_id
* aws ec2 describe-iam-instance-profile-associations
* aws ec2 describe-instance-credit-specifications
* aws ec2 describe-instance-event-windows
* aws ec2 describe-instance-status
* aws ec2 describe-network-insights-analyses
* aws ec2 describe-replace-root-volume-tasks
* aws ec2 describe-network-interfaces
* aws ec2 describe-route-tables
* aws ec2 describe-spot-instance-requests
* aws ec2 describe-volume-status

Depending on what resources are in the target AWS account, some commands like describe-bundle-tasks might return an empty array. The best chances are with describe-instances, describe-volumes and describe-instance-status. These should be the first ones to try.

## 3. Misconfigurations and causes

### 3.1 General aspects

As you can see, the feature is very powerful and can lead to the complete compromise to any EC2 instance from the AWS account. This is exactly why, by granting this permission to multiple u...