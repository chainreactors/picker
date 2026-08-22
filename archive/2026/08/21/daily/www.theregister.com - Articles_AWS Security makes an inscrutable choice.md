---
title: AWS Security makes an inscrutable choice
url: https://www.theregister.com/security/2026/08/22/aws-security-makes-an-inscrutable-choice-corey-quinn/5291446
source: www.theregister.com - Articles
date: 2026-08-21
fetch_date: 2026-08-22T02:52:47.598247
---

# AWS Security makes an inscrutable choice

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

security

# AWS Security makes an inscrutable choice

Quarantining leaked credentials is not good enough

Corey Quinn
[Corey
Quinn](https://www.theregister.com/author/corey-quinn)
Special to El Reg

Published
sat 22 Aug 2026 // 00:42 UTC

One of the best ways to lower your AWS bill by 99 percent or more is by not checking your keys into public GitHub repositories. Many of us have done this inadvertently over the years, and the defenses against it have improved dramatically (my personal favorite being "using non-ephemeral credentials derived from OIDC or SSO is an anti-pattern"), but it still happens.

On Friday, BleepingComputer [reported on a Truffle Security finding](https://www.bleepingcomputer.com/news/security/hundreds-of-leaked-aws-keys-give-full-control-over-corporate-accounts/) that hundreds of leaked AWS keys are root keys and are somehow still active and valid.

AWS Security is full of very smart people who care deeply about a number of things, including "not abetting crime." If they detect (usually via automated means) that a credential has been leaked, they're quick to apply a [Quarantine Policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCompromisedKeyQuarantineV3.html) to it. Trouble is, that policy enumerates a bunch of bad behaviors in an ever-expanding graph of principals and associated behaviors.

REG AD

AWS' considered position on this is that they don't want to break customer environments: "The policy aims to limit the potential damage that may be caused by fraud-related activity leading to unauthorized charges, while not impacting the existing resources."

REG AD

AWS' considered position on this is wrong.

If I get access to your credentials (much less a root credential, good god), deactivating them may very well break your workload because anything that relies on those credentials will start failing. Until you rotate them, those workloads will continue to fail. That's not good!

But I promise you, as a bad actor, I can do far worse to you.

### Hold my tea

Go ahead and apply a quarantine policy to a credential set and toss it my way. I won't be able to buy savings plans, read your S3 data, modify Lambda functions, and do a host of other things.

But here's what I can do.

* Anything I damn well feel like on RDS. You don't have anything important in databases, right?
* ssm:SendCommand / ssm:StartSession are permitted, which means I can run commands as root on EC2 instances, which will in turn invoke with that instance role’s permissions.
* sts:AssumeRole means that I can assume any other role in the account and get its permissions, rendering the entire restriction list potentially moot.
* I can use autoscaling:CreateAutoScalingGroup / UpdateAutoScalingGroup to launch instances via the Auto Scaling service-linked role, so the ec2:RunInstances deny never applies.
* cloudtrail:LookupEvents gets denied (that'll stop you from... reading the audit log), but I can call both cloudtrail:StopLogging and DeleteTrail which do exactly what you expect; you don't have an audit log anymore.
* SES denies ses:GetSendQuota / ListIdentities actions, but y'know what's missing? SendEmail, so I can blast my spam out to your entire list.
* sns:GetSMSAttributes means I can't get your SMS configuration, but I can absolutely sns:Publish to send fraudulent text messages wherever I'd like.
* s3:DeleteObject gets denied, but s3:PutObject is allowed. I can't delete your data, but I can fill a bucket to petabytes.
* Next, they fail to block s3:PutBucketVersioning, s3:PutObjectLockConfiguration, s3:PutObjectRetention, and s3:PutObjectLegalHold. So on any existing bucket, like that one I just stuffed petabytes into, I can enable versioning, turn on Object Lock, and set a bucket-default COMPLIANCE-mode retention out to 2126, or alternatively slap it on per object. COMPLIANCE retention can't be shortened or removed by anyone, including the account root and AWS Support. The only way to remove it is to delete the entire AWS account.
* secretsmanager:GetSecretValue, ssm:GetParameter\* (WithDecryption), and kms:Decrypt are all unencumbered, so your secrets are now my secrets. Sharing is good!
* Backups are important, so it's a shame you don't have any. Well, not after I kick off backup:DeleteRecoveryPoint / Delet...