---
title: aws-security-assessment-solution v3.0.0
url: https://kitploit.com/en/posts/github-awslabs-aws-security-assessment-solution-v300
source: Kitploit
date: 2026-09-10
fetch_date: 2026-09-11T06:51:43.003626
---

# aws-security-assessment-solution v3.0.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/5740/f5c82cf8f1f6e4d30df0350af5b131fbeb01ccfcf3945ff93ffec3ab44ddb75a.png)

New releaseSep 10, 2026

# aws-security-assessment-solution v3.0.0

An AWS tool to help you create a point in time assessment of your AWS account using Prowler.

Share

## Self-Service Security Assessment Solutions (v2.0)

Cybersecurity remains a very important topic and point of concern for many CIOs, CISOs, and their customers. To meet these important concerns, AWS has developed a primary set of services customers should use to aid in protecting their accounts. [Amazon GuardDuty](https://aws.amazon.com/guardduty/), [AWS Security Hub](https://aws.amazon.com/security-hub/), [AWS Config](https://aws.amazon.com/config/), and [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc) reviews help customers maintain a strong security posture over their AWS accounts. As more organizations deploy to the cloud, especially if they are doing so quickly, and they have not yet implemented the recommended AWS Services, there may be a need to conduct a rapid security assessment of the cloud environment.

We have developed an inexpensive, easy to deploy, secure, and fast solution to provide our customers with a security assessment report. These reports are generated using the open source project [Prowler](https://github.com/prowler-cloud/prowler). Prowler performs point in time security assessment based on AWS best practices and can help quickly identify any potential risk areas in a customer’s deployed environment. If you are interested in conducting these assessments on a continuous basis, AWS recommends enabling Security Hub’s [Foundational Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp.html). If you are interested in integrating your Prowler assessment results with Security Hub, you can follow the instructions in the [Prowler Documentation](https://docs.prowler.cloud/en/latest/tutorials/aws/securityhub/).

> Note: Prowler is not an AWS owned solution. Customers should independently review Prowler before running this solution. Any dependencies associated with Prowler should be kept up to date. This solution installs a pinned version of Prowler (currently 5.41.0) from the pip package installer, so that a change to Prowler's output format cannot break a scan without warning. To move to a newer release, edit the `pip3 install prowler==` line in `2-sat2-codebuild-prowler.yaml`.

📕 For more in depth step-by-step instructions, visit module 2 in the [SHIP Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/3bd6e4da-265a-4c79-ab47-639b7ef23c9d/en-US/20-satv2).

## Table of Contents

* [Overview](#overview)
* [Parameters](#parameters)
* [Deployment](#deployment)
* [Single account scan](#single-account-scan)
  + [AWS CloudShell](#aws-cloudshell)
    - [Deploy the solution](#deploy-the-solution)
  + [AWS Console](#aws-console)
    - [Deploy the solution](#deploy-the-solution-1)
* [Multi-account scan](#multi-account-scan)
  + [AWS CloudShell](#aws-cloudshell-1)
    - [Step 1: Deploy prerequisite role](#step-1-deploy-prerequisite-role)
    - [Step 2: Deploy the SATv2 solution](#step-2-deploy-the-satv2-solution)
  + [AWS Console](#aws-console-1)
    - [Step 1: Deploy prerequisite role](#step-1-deploy-prerequisite-role-1)
    - [Step 2: Enable delegated administrator for AWS Organizations](#step-2-enable-delegated-administrator-for-aws-organizations)
    - [Step 3: Deploy the SATv2 solution](#step-3-deploy-the-satv2-solution)
* [Review the results](#review-the-results)
  + [SATv2 Dashboard (recommended)](#satv2-dashboard-recommended)
  + [Prowler Dashboard](#prowler-dashboard)
* [Scan types](#scan-types)
  + [Basic Scan](#basic-scan)
  + [Intermediate scan](#intermediate-scan)
  + [Full scan](#full-scan)
* [Notifications](#notifications)
* [Reporting Summary](#reporting-summary)
  + [How the Athena table is built](#how-the-athena-table-is-built)
  + [Scan history and duplicates](#scan-history-and-duplicates)
* [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
* [Clean Up](#clean-up)
* [Security](#security)
* [License](#license)

## Overview

The solution is deployed with [AWS CloudFormation](https://aws.amazon.com/cloudformation/). When deployed, an [AWS CodeBuild](https://aws.amazon.com/codebuild/) project and an [Amazon S3](https://aws.amazon.com/s3/) bucket to store the Prowler generated reports are created. An [AWS Lambda](https://aws.amazon.com/lambda/) function is then used to start the AWS CodeBuild project.

The parameter (user input) defaults will run a basic scan in a single account. However, you can choose different parameters to run more extensive scans or to scan multiple accounts. The deployment process takes less than 5 minutes to complete. The solution’s AWS CloudFormation templates are provided for review in this Github repository.

Once the template is deployed, the CodeBuild project will run. The default assessment takes around 5 minutes to complete. The time to complete a security assessment will vary depending on the number of resources and the scan options selected. At the end of the assessments the reports are delivered to the created S3 Bucket.

![architecture diagram](https://assets.kitploit.com/production/public/readmes/5740/f5c82cf8f1f6e4d30df0350af5b131fbeb01ccfcf3945ff93ffec3ab44ddb75a.png)

## Parameters

SATv2 can be customized by updating the CloudFormation parameters. This section summarizes the available options and provides a link to the section with more information.

| Parameter | Description | More information |
| --- | --- | --- |
| ProwlerScanType | Specify which type of scan to perform. Selecting full without specifying different ProwlerOptions will do a full scan. To perform a specific check, choose Full and append -c  to ProwlerOptions. | [Scan types](#scan-types) |
| MultiAccountScan | Set this to true if you want to scan all accounts in your organization. You must have deployed the prerequisite template to provision a role, or specify a different ProwlerRole with the appropriate permissions. | [Multi-account scan](#multi-account-scan) |
| Reporting | Set this to true if you want to summarize the Prowler reports into a single csv. This is helpful when scanning multiple accounts. | [Reporting Summary](#reporting-summary) |
| EmailAddress | Specify an address if you want to receive an email when the assessment completes. | [Notifications](#notifications) |
| **Advanced Parameters** |  |  |
| ConcurrentAccountScans | For multi-account scans, specify the number of accounts to scan concurrently. This is useful for large organizations with many accounts. Selecting more than three changes the size of the CodeBuild instance and may incur additional costs. |  |
| CodeBuildTimeout | Set the timeout for the CodeBuild job. The default is 300 minutes (5 hours). |  |
| MultiAccountListOverride | Specify a space delimited list of accounts to scan. Leaving this blank will scan all accounts in your organization. Ensure that you have set `MultiAccountScan` parameter above to true if you want to scan specific accounts. If you can't provide delegated ListAccount access, you can provide the MultiAccountListOverride parameter. | [Multi-account scan](#multi-account-scan) |
| ProwlerOptions | Specify the parameters for Prowler. The --role and ARN will automatically be adde...