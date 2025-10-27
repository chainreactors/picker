---
title: IMDShift - Automates Migration Process Of Workloads To IMDSv2 To Avoid SSRF Attacks
url: https://buaq.net/go-173711.html
source: unSafe.sh - 不安全
date: 2023-08-05
fetch_date: 2025-10-04T12:00:14.702033
---

# IMDShift - Automates Migration Process Of Workloads To IMDSv2 To Avoid SSRF Attacks

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/7f6c744796780b2f84bd2557ec603d1a.jpg)

IMDShift - Automates Migration Process Of Workloads To IMDSv2 To Avoid SSRF Attacks

AWS workloads that rely on the metadata endpoint are vulnerable to Server-Side Request Forge
*2023-8-4 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-173711.htm)
阅读量:19
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjkdAXXT1Vs-6Oy4K6P0TnBAdIDvenbdnYsBQpmuRZ9F-R9-D5OU4EhWJEHj3kcXwTk7DUt4KUVRePq963C0qwZcAg9If_4934Rfs26CgqRakWhYaRnPs19Zqb5ziD3Vam3tbOb1u9Le0pd75ABslChRzjDCbp05oD4m9odoQ_06EYlElCz--T-zHhz93i8=w640-h270)](https://blogger.googleusercontent.com/img/a/AVvXsEjkdAXXT1Vs-6Oy4K6P0TnBAdIDvenbdnYsBQpmuRZ9F-R9-D5OU4EhWJEHj3kcXwTk7DUt4KUVRePq963C0qwZcAg9If_4934Rfs26CgqRakWhYaRnPs19Zqb5ziD3Vam3tbOb1u9Le0pd75ABslChRzjDCbp05oD4m9odoQ_06EYlElCz--T-zHhz93i8)

AWS workloads that rely on the [metadata](https://www.kitploit.com/search/label/Metadata "metadata") endpoint are [vulnerable](https://www.kitploit.com/search/label/Vulnerable "vulnerable") to Server-Side Request Forgery (SSRF) attacks. IMDShift automates the migration process of all workloads to IMDSv2 with extensive capabilities, which implements enhanced security measures to protect against these attacks.

## Features

* Detection of AWS workloads that rely on the metadata endpoint amongst various services which includes - EC2, ECS, EKS, Lightsail, AutoScaling Groups, [Sagemaker](https://www.kitploit.com/search/label/Sagemaker "Sagemaker") Notebooks, Beanstalk (in progress)
* Simple and intuitive command-line interface for easy usage
* Automated migration of all workloads to IMDSv2
* Standalone hop limit update for compatible resources
* Standalone metadata endpoint enable operation for compatible resources
* Detailed logging of migration process
* Identify resources that are using IMDSv1, using the `MetadataNoToken` CloudWatch metric across specified regions
* Built-in Service Control Policy (SCP) recommendations

## IMDShift vs. Metabadger

[Metabadger](https://github.com/salesforce/metabadger "Metabadger") is an older tool that was used to facilitate migration of [AWS EC2](https://www.kitploit.com/search/label/AWS%20EC2 "AWS EC2") workloads to IMDSv2.

IMDShift makes several improvements on Metabadger's capabilities:

* IMDShift allows migration of standalone services and not all EC2 instances, blindly. For example, the user can choose to only migrate EKS workloads, also some services such as Lightsail, do not fall under EC2 umbrella, IMDShift has the capability to migrate such resources as well.
* IMDShift allows standalone enabling of metadata endpoint for resources it is currently disabled, without having to perform migration on the remaining resources
* IMDShift allows standalone update response hop limit for resources where metadata endpoint is enabled, without having to perform migration on the remaining resources
* IMDShift allows, not only the option to include specific regions, but also skip specified regions
* IMDShift not only allows usage of AWS profiles, but also can assume roles, to work
* IMDShift helps with post-migration activities, by suggesting various Service Control Policies (SCPs) to implement.

## Installation

### Production Installation

```
git clone https://github.com/ayushpriya10/imdshift.git
```

### Development Installation

```
git clone https://github.com/ayushpriya10/imdshift.git
cd imdshift/
python3 -m pip install -e .
```

## Usage

```
Options:
  --services TEXT             This flag specifies services scan for IMDSv1
                              usage from [EC2, Sagemaker, ASG (Auto Scaling
                              Groups), Lightsail, ECS, EKS, Beanstalk].
                              Format: "--services EC2,Sagemaker,ASG"
  --include-regions TEXT      This flag specifies regions explicitly to
                              include scan for IMDSv1 usage. Format: "--
                              include-regions ap-south-1,ap-southeast-1"
  --exclude-regions TEXT      This flag specifies regions to exclude from the
                              scan explicitly. Format: "--exclude-regions ap-
                              south-1,ap-southeast-1"
  --migrate                   This boolean flag enables IMDShift to perform
                              the migration, defaults to "False". Format: "--
                              migrate"
  --   update-hop-limit INTEGER  This flag specifies if the hop limit should be
                              updated and with what value. It is recommended
                              to set the hop limit to "2" to enable containers
                              to be able to work with the IMDS endpoint. If
                              this flag is not passed, hop limit is not
                              updated during migration. Format: "--update-hop-
                              limit 3"
  --enable-imds               This boolean flag enables IMDShift to enable the
                              metadata endpoint for resources that have it
                              disabled and then perform the migration,
                              defaults to "False". Format: "--enable-imds"
  --profile TEXT              This allows you to use any profile from your
                              ~/.aws/credentials file. Format: "--profile
                                 prod-env"
  --role-arn TEXT             This flag let's you assume a role via aws sts.
                              Format: "--role-arn
                              arn:aws:sts::111111111:role/John"
  --print-scps                This boolean flag prints Service Control
                              Policies (SCPs) that can be used to control IMDS
                              usage, like deny access for credentials fetched
                              from IMDSv2 or deny creation of resources with
                              IMDSv1, defaults to "False". Format: "--print-
                              scps"
  --check-imds-usage          This boolean flag launches a scan to identify
                              how many instances are using IMDSv1 in specified
                              regions, during    the last 30 days, by using the
                              "MetadataNoToken" CloudWatch metric, defaults to
                              "False". Format: "--check-imds-usage"
  --help                      Show this message and exit.
```

IMDShift - Automates Migration Process Of Workloads To IMDSv2 To Avoid SSRF Attacks
![IMDShift - Automates Migration Process Of Workloads To IMDSv2 To Avoid SSRF Attacks](https://blogger.googleusercontent.com/img/a/AVvXsEjkdAXXT1Vs-6Oy4K6P0TnBAdIDvenbdnYsBQpmuRZ9F-R9-D5OU4EhWJEHj3kcXwTk7DUt4KUVRePq963C0qwZcAg9If_4934Rfs26CgqRakWhYaRnPs19Zqb5ziD3Vam3tbOb1u9Le0pd75ABslChRzjDCbp05oD4m9odoQ_06EYlElCz--T-zHhz93i8=s72-w640-c-h270)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/08/imdshift-automates-migration-process-of.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)