---
title: IAMActionHunter in action
url: https://securitycafe.ro/2023/07/27/iamactionhunter-in-action/
source: Security Café
date: 2023-07-28
fetch_date: 2025-10-04T11:54:46.714189
---

# IAMActionHunter in action

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

![](https://securitycafe.ro/wp-content/uploads/2023/07/pexels-photo-6702764.jpeg?w=840)

# IAMActionHunter in action

[July 27, 2023](https://securitycafe.ro/2023/07/27/iamactionhunter-in-action/ "4:44 pm") [Eduard Agavriloae](https://securitycafe.ro/author/eagavriloae/ "View all posts by Eduard Agavriloae") [aws](https://securitycafe.ro/category/cloud-security/aws/), [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Pentest techniques](https://securitycafe.ro/category/pentest-techniques/) [Leave a comment](https://securitycafe.ro/2023/07/27/iamactionhunter-in-action/#respond)

Let’s take a look at the latest cloud tool published by Rhino Security Labs: IAMActionHunter.

Here I will detail the practical approach I took during an engagement and how the tool helped me. The latest version was used, which at the moment is v1.0.5.

GitHub: <https://github.com/RhinoSecurityLabs/IAMActionHunter>

Blog from Rhino Security Labs: <https://rhinosecuritylabs.com/aws/iamactionhunter-aws-iam-permissions/>

## Contents

1. Introduction
2. Why this tool
3. Practical usage
4. Features that would have helped me
5. Conclusions

## 1. Introduction

You see, privilege escalation and IAM misconfigurations are topics I enjoy exploiting, but it takes time to develop attack vectors. That’s because most organizations have hundreds of roles and custom policies. From some time now I felt the need of a tool that would help me in finding missing pieces for completing various attack vectors and I think with IAMActionHunter that tool is here.

## 2. Why this tool

IAMActionHunter downloads data about users, roles and their policies. Then you can offline query the data to find who exactly can do a certain action. This may sound simple and programmatically it may be, but doing it manually is just not feasible. In this engagement, the AWS account had over 200 roles. I had access to a few partially privileged roles and I had some attacks in mind, but for that, I had to check which role can perform a certain action. Well, it’s just not possible to do a reverse search natively from AWS. You have to check every role. This is where IAMActionHunter comes into place.

What about other tools? I often use Cloudsplaining along with ScoutSuite, which are great tools, but they don’t have a way to make this reverse query and find out what IAM identity can perform a certain action.

ScoutSuite is close to provide this, but is not really as good as IAMActionHunter.

Let’s search for IAM identities that can perform ssm:SendCommand. Using ScoutSuite we can go to Security->IAM->Permissions and we will have a list similar as the one below.

![](https://securitycafe.ro/wp-content/uploads/2023/07/scout-suite.png?w=1024)

Search for “ssm:SendCommand” in ScoutSuite

I have to say that is a little hard to read this and the condition is displayed as “[object Object]” which requires us to manually verify it. It’s better than doing it manually, but let’s check how IAMActionHunter works.

![](https://securitycafe.ro/wp-content/uploads/2023/07/iam-action-send-command-1.png?w=1013)

Search for “ssm:SendCommand” in IAMActionHunter

Terminal output is cool, but I find it easier to use the CSV output (–csv file-name.csv). Here you can also see how the conditions are displayed.

![](https://securitycafe.ro/wp-content/uploads/2023/07/iam-action-send-command-csv.png?w=1024)

Search for “ssm:SendCommand” in IAMActionHunter with CSV output

Not only that is better than ScoutSuite, but is exactly what I need when developing IAM based attack vectors and it works fine even for hundreds of roles with all kinds of conditions.

## 3. Practical usage

As I said, I had access to some partially privileged roles. Now, from one of the roles I already could execute ssm:SendCommand, which, in the context of my engagement, I needed to report as finding. The thing is that this role also had the permissions sts:AssumeRole, iam:PassRole, lambda:CreateFunction, lambda:InvokeFunction, ec2:RunInstance and some more. Because of this, I wanted to identity the full extend on how ssm:SendCommand can be used by this role indirectly (by assuming another role, creating a Lambda Function with that permissions and so on).

Well, here is where IAMActionHunter was really helpful. After getting a list of all the IAM principals with the permissions ssm:SendCommand, I was able to fully understand the extent on which my role could have used this permission even if it wasn’t directly attached to its identity.

![](https://securitycafe.ro/wp-content/uploads/2023/07/meme.jpg?w=650)

The reality of AWS IAM attack vectors

I also used IAMActionHunter in another way, which I think you will find more useful. I used Cloudsplaning to identify what policies contain privilege escalation vectors. Then I checked in ScoutSuite the trust relationship policy attached to that role and I finally used IAMActionHunter to find who has the permissions required to enable the privilege escalation vector (“iamactionhunter –account 123456789012 –query lambda:CreateFunction,lambda:InvokeFunction,iam:PassRole –all-or-none” for example)

You can directly search for privilege escalation vectors from IAMActionHunter with “–config privescs”, but I found out this only after the engagement so I couldn’t test it’s validity.

## 4. Features that would have helped me

There are 2 things that would have helped me during the engagement. The first one: to be able to filter the results based on a pattern. What I mean by that is something like:

```
iamactionhunter --account 123456789012 --role *logging* --query iam:CreateUser
```

There are scenarios where you can do certain operations only over pattern based named resources. Like only passing roles with the name “\*logging\*” to Lambda Functions. Now, if I have the pass role permissions, it would help me to search for permissions only on those roles. Of course it’s easy to do it manually, especially in the CSV format, but I am just saying. It can be a nice feature.

The second one, to be able to filter roles based on their trust relationship. I was actually looking for roles with a certain permission that can be assumed by EC2 instances. The option now is to make a list of roles that can be assumed by EC2 and run IAMActionHunter for each one. Again, is a workaround easy to do, but it would also be a nice feature to have.

As a last note, it’s not clear at the moment how to use the “–config” flag or how to make your own list of configs. Looking at the source code (<https://github.com/RhinoSecurityLabs/IAMActionHunter/blob/main/IAMActionHunter/configs/all.py>) becomes easy to understand it, but it would be easier to have it as documentation.

## 5. Conclusions

I want to thank Dave Yesland (name taken from GitHub repo) from Rhino Security Labs for developing this tool. It’s really helpful and I already integrated it in my hacking ...