---
title: AWS Enumeration – Part II (Practical enumeration)
url: https://securitycafe.ro/2022/12/14/aws-enumeration-part-ii-practical-enumeration/
source: Security Café
date: 2022-12-15
fetch_date: 2025-10-04T01:32:38.199067
---

# AWS Enumeration – Part II (Practical enumeration)

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

![](https://securitycafe.ro/wp-content/uploads/2022/12/aws-enumeration-part-ii-feature-image-3.png?w=840)

# AWS Enumeration – Part II (Practical enumeration)

[December 14, 2022](https://securitycafe.ro/2022/12/14/aws-enumeration-part-ii-practical-enumeration/ "9:30 am") [Eduard Agavriloae](https://securitycafe.ro/author/eagavriloae/ "View all posts by Eduard Agavriloae") [aws](https://securitycafe.ro/category/cloud-security/aws/), [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Pentest techniques](https://securitycafe.ro/category/pentest-techniques/) [Leave a comment](https://securitycafe.ro/2022/12/14/aws-enumeration-part-ii-practical-enumeration/#respond)

We hackers love cheat sheets so here are mine for AWS IAM, EC2, S3 Buckets and Lambda Functions. In Part I we showed what approaches you can take for enumerating an AWS environment. This time, we’ll present you a cheat sheet of commands that will help you in lateral movement, privilege escalation and data exfiltration.

## 1. IAM (Identity and Access Management)

This is the place that usually gives you the most powerful attack vectors. Giving the wrong permission, setting a lax role trust relationship or having groups with admin privileges are some examples of insecure configurations that I encounter all the time. The only thing left is creating an attack vector.

A cheat sheet for IAM resources:

```
# USERS
# list users
aws iam list-users
# list groups of an user
aws iam list-groups-for-user --user-name $username
# list policies attached to a user
aws iam list-user-policies --user-name $username
aws iam list-attached-user-policies --user-name $username
# list signing certificates of a user
aws iam list-signing-certificates --user-name $username
# list ssh public keys
aws iam list-ssh-public-keys --user-name $username
# get SSH key details
aws iam get-ssh-public-key --user-name $username --encoding PEM --ssh-public-key-id $ssh_id
# check mfa devices of users
aws iam list-virtual-mfa-devices
# check if user can login in web console
aws iam get-login-profile --user-name $username
# GROUPS
# list groups for the AWS account
aws iam list-groups
# list group policies
aws iam list-group-policies --group-name $group_name
aws iam list-attached-group-policies --group-name $group_name
# POLICIES
# list policies for AWS account
aws iam list-policies
# filter for customer managed policies
aws iam list-policies --scope Local | grep -A2 PolicyName
# check policy details
aws iam get-policy --policy-arn $policy_arn
# check policy version which will also details the given permission. version-id from previous command
aws iam get-policy-version --policy-arn $policy_arn --version-id $version_id
# check policy for user
aws iam get-user-policy --user-name $username --policy-name $policy_name
# ROLES
# list roles for AWS account
aws iam list-roles
# check details for role
aws iam get-role --role-name $role_name
# check for policies attached to role
aws iam list-attached-role-policies --role-name $role_name
aws iam list-role-policies --role-name $role_name
# get details for those policies
aws iam get-role-policy --role-name $role --policy-name $policy
```

Now, what can you do with this information? By enumerating this you can determine what you need to do to complete the attack vector. Some examples:

* A role has admin privileges and can be assumed by all the users within the account. Two users do not use MFA. The missing piece of the attack vector would be the compromise of one user account from those two.
* A group has admin privileges. We need to find a way to add an user that’s in our control there
* A role for EC2 instances has admin privileges. We need to compromise an EC2 instance that’s using this role and exfiltrate the access credentials

We keep things simple for the moment, but we don’t actually need IAM resources with admin privileges. Is enough to compromise resources with permissions that can lead to a privilege escalation attack.

All privilege escalation vectors include IAM actions. Here is a list of actions that can directly lead to privesc and should be further analyzed:

* iam:PutGroupPolicy
* iam:PutRolePolicy
* iam:PutUserPolicy
* iam:AttachGroupPolicy
* iam:AttachRolePolicy
* iam:AttachUserPolicy
* iam:CreatePolicyVersion
* iam:AddUserToGroup
* iam:CreateLoginProfile
* iam:UpdateLoginProfile
* iam:CreateAccessKey

## 2. S3 Buckets

S3 buckets are interesting and more than often misconfigured. The worst thing is having a public bucket with private data, but there are other things that matter as well. For example, missing encryption at rest or in transit, missing access logging, missing versioning where needed and so on.

The cheat sheet for S3 Bucket enumeration:

```
# if the endpoint is private, then it must be used the --endpoint switch
# aws --endpoint http://$ip:$port s3api list-buckets
# list buckets
aws s3api list-buckets --query "Buckets[].Name"
aws s3 ls
# check bucket location
aws s3api get-bucket-location --bucket $bucket_name
# enumerate bucket objects
aws s3api list-objects-v2 --bucket $bucket_name
aws s3api list-objects --bucket $bucket_name
aws s3 ls $bucket_name
# check object versions
aws s3api list-object-versions --bucket $bucket_name
# check bucket ACLs and object ACLs
aws s3api get-bucket-acl --bucket $bucket_name
aws s3api get-object-acl --bucket $bucket_name --key $file_name
# download objects from the S3 bucket
aws s3 cp s3://$bucket_name/$file_name $local_path
# check bucket policy status
aws s3api get-bucket-policy-status --bucket $bucket_name --output text | python -m json.tool
# check public access for a bucket
aws s3api get-public-access-block --bucket $bucket_name
# check if object listing is allowed for anonymous users
# should get something like directory listing if allowed
curl http://$domain/$bucket_name | xmllint --format -f
# check if ListBucket is explicitly allowed
aws s3api get-bucket-policy --bucket $bucket_name
```

I’ve seen organizations storing access keys and other credentials in S3 buckets, so having access inside the bucket can be very useful.

A bucket can be made public in multiple ways. One way is to explicitly make it public by not blocking public access from the web console.

Another way, more subtle to errors, is through the use of bucket policy. The bucket can be made public by allowing all principles to perform actions on the bucket.

My favorite way however is when people grant access to “Authenticated” principles, believing that they grant access to the users within the account. In fact, this grants access to any AWS user from the internet, which is almost as making the bucket public.

If you don’t have listing permissions over the bucket you can enumerate it as an web application with tools like dirb or gobuster.

You can find bucket names by following the next URL structure: <https://bucket-name.s3.amazonaws.com>.

N...