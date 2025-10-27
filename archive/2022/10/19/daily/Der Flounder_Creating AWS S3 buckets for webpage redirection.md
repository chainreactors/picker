---
title: Creating AWS S3 buckets for webpage redirection
url: https://derflounder.wordpress.com/2022/10/18/creating-aws-s3-buckets-for-webpage-redirection/
source: Der Flounder
date: 2022-10-19
fetch_date: 2025-10-03T20:13:05.558108
---

# Creating AWS S3 buckets for webpage redirection

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Amazon Web Services](https://derflounder.wordpress.com/category/amazon-web-services/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Creating AWS S3 buckets for webpage redirection

## Creating AWS S3 buckets for webpage redirection

October 18, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

I recently had an issue where I needed to solve a particular problem:

1. I had a DNS domain name

**dns.name.here**

2. I needed to point it to a HTTPS URL hosted on another domain:

<https://other.dns.name.here/path/to/site/goes/here>

3. The DNS server for **dns.name.here** does not support [HTTP Redirect records](https://web.media.mit.edu/~holbrow/post/dns-cname-a-record-and-http-redirect-explained/).

To address this, I decided to use S3 buckets hosted on Amazon Web Services to handle the redirection to the HTTPS URL. In this scenario, what I’m doing is pointing the relevant **dns.name.here** domain name at the S3 bucket’s AWS domain name. The S3 bucket is [performing a HTTP 301 redirect](https://blog.hubspot.com/blog/tabid/6307/bid/7430/what-is-a-301-redirect-and-why-should-you-care.aspx), which sends the requesting web browser the URL of the site I want to connect to. For those interested, Amazon’s documentation of how to use an S3 bucket for URL redirection is linked below:

<https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html>

After doing it the first time manually, I decided to see if anyone had scripted this task. It turns out the answer is “no”, at least for what I wanted to do, so I’ve written a script which handles this task. For more details, please see below the jump.

The script I’ve developed sets up S3 buckets in Amazon Web Services for use with redirecting DNS or URL requests to an alternative HTTP or HTTPS URL.

**Pre-requisites:**

The [AWS CLI tool](https://aws.amazon.com/cli/) must be installed.
The AWS CLI tool [must be configured to use AWS programmatic user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) with the permissions to do the following:

* Create an S3 bucket
* Set permissions on the newly-created S3 bucket
* Apply an S3 bucket policy to the newly-created S3 bucket
* Apply a website configuration to the newly-created S3 bucket

**Usage:**

**./s3\_website\_redirection\_creator.sh**

Once the pre-requisites are met, this script performs the following actions:

1. Requests a name for an S3 bucket, which should be the DNS name that you want to set up a redirection for.
2. Requests the AWS region that the S3 bucket should be created in.
3. Requests the HTTP or HTTPS URL of the website that the redirection is being set up for.

Once the user-requested information is provided, this script performs the following actions:

1. Creates an S3 bucket using the name supplied by user input
2. Set permissions on the newly-created S3 bucket so that no public access is permitted.
3. Set the default encryption behavior for the newly-created S3 bucket to be enabled and to use Amazon S3-managed encryption keys.
4. Sets an S3 bucket policy which blocks non-SSL connections to the contents of the newly-created S3 bucket.
5. Set the website configuration for the desired URL redirection for the newly-created bucket.

![Screen Shot 2022 10 18 at 4 41 10 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/10/screen-shot-2022-10-18-at-4.41.10-pm.png?w=595 "Screen Shot 2022-10-18 at 4.41.10 PM.png")

Once the S3 bucket is created, you should be able to verify that accessing the HTTP address of the S3 bucket results in your browser being automatically forwarded to the desired website address.

![Screen Shot 2022 10 18 at 4 39 25 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/10/screen-shot-2022-10-18-at-4.39.25-pm.png?w=595 "Screen Shot 2022-10-18 at 4.39.25 PM.png")

![Screen Shot 2022 10 18 at 4 39 38 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/10/screen-shot-2022-10-18-at-4.39.38-pm.png?w=595 "Screen Shot 2022-10-18 at 4.39.38 PM.png")

This script is available below and also from GitHub at the following location:

<https://github.com/rtrouton/aws_scripts/tree/main/s3_website_redirection_creator>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # This script sets up S3 buckets in Amazon Web Services for use with redirecting |
|  | # DNS or URL requests to an alterative HTTP or HTTPS URL. |
|  | # |
|  | # The following pre-requisites are needed: |
|  | # |
|  | # \* The AWS CLI tool must be installed |
|  | # \* The AWS CLI tool must have access to AWS programmatic user credentials with the |
|  | # permissions to do the following: |
|  | # |
|  | # \* Create an S3 bucket |
|  | # \* Set permissions on the newly-created S3 bucket |
|  | # \* Apply an S3 bucket policy to the newly-created S3 bucket |
|  | # \* Apply a website configuration to the newly-created S3 bucket |
|  | # |
|  | # |
|  | # Once the pre-requisites are met, this script performs the following actions: |
|  | # |
|  | # A. Requests a name for an S3 bucket, which should be the DNS name that you want to set up a redirection for. |
|  | # B. Requests the AWS region that the S3 bucket should be created in. |
|  | # C. Requests the HTTP or HTTPS URL of the website that the redirection is being set up for. |
|  | # |
|  | # Once the user-requested information is provided, this script performs the following actions: |
|  | # |
|  | # 1. Creates an S3 bucket using the name supplied by user input |
|  | # 2. Set permissions on the newly-created S3 bucket so that no public access is permitted. |
|  | # 3. Set the default encryption behavior for the newly-created S3 bucket to be enabled and to use Amazon S3-managed encryption keys. |
|  | # 4. Sets an S3 bucket policy which blocks non-SSL connections to the contents of the newly-created S3 bucket. |
|  | # 5. Set the website configuration for the desired URL redirection for the newly-created bucket. |
|  |  |
|  | # Set exit code |
|  | exitCode=0 |
|  |  |
|  | clear |
|  | echo "This script sets up S3 buckets in Amazon Web Services for website redirection." |
|  | echo "You will need to enter the following information:" |
|  | echo "" |
|  | echo "A. The name of the new S3 bucket, which should be the DNS name that you want to set up a redirection for." |
|  | echo "B. The Amazon Web Services region that you want to create the S3 bucket in." |
|  | echo "C. The address of the website address you want to redirect to." |
|  | echo "" |
|  | read -p "Please enter the name of the new S3 bucket: " s3\_bucket\_name |
|  | read -p "Please enter the AWS region that the new S3 bucket should be created in: " s3\_bucket\_region |
|  | read -p "Please enter the website address you want to redirect to : " website\_url |
|  |  |
|  | # Figure out if an HTTP or HTTPS URL is being used. |
|  |  |
|  | http\_protocol=${website\_url%://\*} |
|  |  |
|  | # Get the website URL and split it as necessary for use with the redirection rules. |
|  |  |
|  | site=${website\_url#\*//} |
|  |  |
|  | if [[ "$site" == \*\/\* ]]; then |
|  | site=${site%%/\*} |
|  | site\_path=${website\_url#\*//} |
|  | site\_path=${site\_path#\*/} |
|  | else |
|  | site=${site%%/\*} |...