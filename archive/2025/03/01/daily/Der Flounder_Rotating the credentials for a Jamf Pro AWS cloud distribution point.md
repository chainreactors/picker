---
title: Rotating the credentials for a Jamf Pro AWS cloud distribution point
url: https://derflounder.wordpress.com/2025/02/28/rotating-the-credentials-for-a-jamf-pro-aws-cloud-distribution-point/
source: Der Flounder
date: 2025-03-01
fetch_date: 2025-10-06T21:57:31.073958
---

# Rotating the credentials for a Jamf Pro AWS cloud distribution point

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Amazon Web Services](https://derflounder.wordpress.com/category/amazon-web-services/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/) > Rotating the credentials for a Jamf Pro AWS cloud distribution point

## Rotating the credentials for a Jamf Pro AWS cloud distribution point

February 28, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of setting up an AWS-hosted cloud distribution point for Jamf Pro, you will need to set up a user in AWS and get an access key and secret access key. I describe that process as part of an earlier post on [how to set up an AWS-hosted cloud distribution point](https://derflounder.wordpress.com/2017/03/07/creating-a-jamf-pro-cloud-distribution-point-using-amazon-web-services/). However, many shop’s security policies mandate rotating AWS credentials on a regular basis. For those with requirements like this, please see below the jump for how to rotate these credentials for an AWS-hosted cloud distribution point.

The following procedure will walk you through the process of setting up a new AWS access key and secret access key which can be used to update the credentials used for an AWS-hosted cloud distribution point. This process assumes the following:

* A. You have an existing AWS-hosted cloud distribution point set up in Jamf Pro.
* B. You have an existing AWS IAM programmatic user account set up with the correct permissions to access and manage the AWS-hosted cloud distribution point set up in Jamf Pro.
* C. You can log into the AWS console using an account with console access with sufficient permissions to perform the following actions:
  + i. Access AWS’s IAM service for the account which has the existing AWS IAM programmatic user account referenced in pre-requisite B above.
  + ii. Change the security credentials for the existing AWS IAM programmatic user account referenced in pre-requisite B above.
* D. You can log into your Jamf Pro admin console using an account with sufficient permissions to perform the following actions:
  + i. Access the cloud distribution point settings.
  + ii. Edit the cloud distribution point settings.

1. Log into the AWS console.

2. Select the **IAM** service.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.29.png?w=598&h=325 "Screenshot 2025-02-23 at 2.29.png")

3. Identify and select the existing AWS IAM programmatic user account referenced in pre-requisite B above.

4. For that user account, select **Security Credentials**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.31.png?w=600&h=329 "Screenshot 2025-02-23 at 2.31.png")

5. See how many access keys (active and inactive) are currently associated with the account.

An AWS IAM user account can have up to two total access keys set up in it. This procedure assumes you have one active access key which is being used as credentials for the AWS-hosted cloud distribution point. You will need to set up a second active access key as part of rotating the credentials for the cloud distribution point and both sets of access keys must be active for the rotation process to successfully complete.

If you already have two active access keys showing for the existing AWS IAM programmatic user account, stop here. Before proceeding, you will need to identify if a) if second access key is being used by something else, b) what the second access key is being used for and c) get its functionality moved to another IAM programmatic user account.

The rest of the procedure assumes that you have one active access key associated with the account.

6. Click the **Create Access Key** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.34.png?w=598&h=328 "Screenshot 2025-02-23 at 2.34.png")

7. For use case, select **Other.** Once the **Other** case has been selected, click the **Next** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.37.png?w=599&h=473 "Screenshot 2025-02-23 at 2.37.png")

8. Set a description tag (if desired), then click the **Create Access Key** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.39.png?w=598&h=205 "Screenshot 2025-02-23 at 2.39.png")

9. The access key will be created, with an access key ID and secret access key.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.40.png?w=599&h=335 "Screenshot 2025-02-23 at 2.40.png")

This is the only time you will have access to both the access key ID and secret access key information. You can click the **Show** button to reveal the secret access key information.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.40-1.png?w=599&h=335 "Screenshot 2025-02-23 at 2.40.png")

You also have the option of downloading both the access key ID and secret access key information in a .csv file.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.40-2.png?w=599&h=335 "Screenshot 2025-02-23 at 2.40.png")

The information in the .csv file will look similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Access key ID | Secret access key |
| --- | --- | --- |
|  | AKIATFL3V52CQ4EI54FA | UtK4219dBAE0211497183b20aa2a6296/Dk7de |

[view raw](https://gist.github.com/rtrouton/e8abd818c5ca73d6ae3712e38a937673/raw/c80dc5c79ebbbfb7e29dcdcd78fc43c66a77867c/mdm_aws_cloud_dp_user_account_accessKeys.csv)
 [mdm\_aws\_cloud\_dp\_user\_account\_accessKeys.csv](https://gist.github.com/rtrouton/e8abd818c5ca73d6ae3712e38a937673#file-mdm_aws_cloud_dp_user_account_accesskeys-csv)
hosted with ❤ by [GitHub](https://github.com)

10. Once you have both the access key ID and secret access key information stored for later reference, click the **Done** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.40-3.png?w=599&h=335 "Screenshot 2025-02-23 at 2.40.png")

You should now see a second active access key appear in the AWS console. The access key ID is displayed, but the secret access key is never shown again following the access key’s creation (described in step 9.)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.45.png?w=599&h=328 "Screenshot 2025-02-23 at 2.45.png")

11. Log into the Jamf Pro admin console for the Jamf Pro instance which has the relevant AWS-hosted cloud distribution point.

12. Go to **Settings**: **Server**: **Cloud Distribution Point**.

13. In the **Cloud distribution point** window, verify that **Content Delivery Network** is set to the following:

**Amazon Web Services**

14. Click the **Edit** button to update the credentials for the AWS-hosted cloud distribution point.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/02/screenshot-2025-02-23-at-2.47.png?w=600&h=383 "Screenshot 2025-02-23 at 2.47.png")

15. In the **Access Key ID** entry field, put in the following information:

Access key ID

16. In the **Secret Access Key** and **Verify Secret Access Key** entry fields, put in the following information:

Secret access key

17. Once you’ve verified that the correct informat...