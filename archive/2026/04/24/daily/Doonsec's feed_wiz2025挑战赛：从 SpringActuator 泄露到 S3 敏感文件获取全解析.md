---
title: wiz2025挑战赛：从 SpringActuator 泄露到 S3 敏感文件获取全解析
url: https://mp.weixin.qq.com/s/rJo_PbmfsHps59apo5cVWw
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:34:34.453896
---

# wiz2025挑战赛：从 SpringActuator 泄露到 S3 敏感文件获取全解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lFfjZayicKlFFsQY59M3O216Q8qJx0VKVTQ6kGlIKdznoFE7y2MuiaAzVPwLjzZw00RMKhkZxhlx0d7Dhyd2qP2rvJiaVHLJfHsHwZrNu4HZ1U/0?wx_fmt=jpeg)

# wiz2025挑战赛：从 SpringActuator 泄露到 S3 敏感文件获取全解析

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于蚁景网络安全
，作者l0-0l

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yk0SeU4ibQcLl1mDLlqhbAOdK1Ik3EO85soOvkh9e8wQ/0)

**蚁景网络安全**
.

致力于为你带来更实用的网络安全技术内容！

### 背景

经过几周的利用和权限提升，你获得了访问你希望是最终服务器的权限，然后可以使用它从 S3 存储桶中提取秘密旗帜。

但这不会容易。目标使用 AWS 数据边界来限制对存储桶内容的访问。

`You've discovered a Spring Boot Actuator application running on AWS: curl https://ctf:88sPVWyC2P3p@challenge01.cloud-champions.com

{"status":"UP"}

### 解决过程

#### Spring Boot Actuator 泄露

首先我们分析一下，flag 肯定是在存储桶中，因为这里说了已经对我们的桶进行了限制，所以匿名访问的方法可能没有作用，不过这里还是尝试一下，首先匿名访问需要获取存储桶的名称，因为题目已经告诉了 Spring Boot Actuator 明显我们可以查看 env

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldz3nUia1mdibC8oicerHj94xbeic4x0pBZ1WtIX2pFiavcMlMZiaz1zRQT3faKx0sFSbx0nLBP56ZjicP9Tg/640?wx_fmt=png&from=appmsg)

尝试列出

```
ounter(lineounter(lineounter(lineuser@monthly-challenge:~$ aws s3 ls s3://challenge01-470f711/ --no-sign-request
An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied
```

不行，没有权限，所以我们必须去寻找凭证

我第一想法就是元数据

但是没有反应

```
ounter(linecurl http://169.254.169.254/latest/meta-data
```

估计这个 shell 不是一个 EC2 的

然后就是寻找凭据了，可以使用一些工具，比如 truffleHog

然后简单找了一下

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineuser@monthly-challenge:/$ grep -ri --exclude-dir={/proc,/sys,/dev,/run,/snap,/var/lib/docker} 'Secret Access Key' //usr/local/aws-cli/v2/2.27.37/dist/awscli/botocore/data/datazone/2018-05-10/service-2.json:          "documentation":"<p>The secret access key of a connection.</p>"/usr/local/aws-cli/v2/2.27.37/dist/awscli/botocore/data/datazone/2018-05-10/service-2.json:          "documentation":"<p>The secret access key of the environment credentials.</p>"/usr/local/aws-cli/v2/2.27.37/dist/awscli/botocore/data/s3control/2018-08-20/service-2.json:          "documentation":"<p>The secret access key of the Amazon Web Services STS temporary credential that S3 Access Grants vends to grantees and client applications. </p>"/usr/local/aws-cli/v2/2.27.37/dist/awscli/botocore/data/appflow/2020-08-23/service-2.json:          "documentation":"<p> The Secret Access Key portion of the credentials. </p>"/usr/local/aws-cli/v2/2.27.37/dist/awscli/botocore/data/appflow/2020-08-23/service-2.json:          "documentation":"<p> The Secret Access Key portion of the credentials. </p>"/usr/local/aws-cli/v2/2.27.37/dist/awscli/botocore/data/opsworks/2013-02-18/service-2.json:          "documentation":"<p>When included in a request, the parameter depends on the repository type.</p> <ul> <li> <p>For Amazon S3 bundles, set <code>Password</code> to the appropriate IAM secret access key.</p> </li> <li> <p>For HTTP bundles and Subversion repositories, set <code>Password</code> to the password.</p> </li> </ul> <p>For more information on how to safely handle IAM credentials, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html\">https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html</a>.</p> <p>In responses, OpsWorks Stacks returns <code>*****FILTERED*****</code> instead of the actual value.</p>"/usr/local/aws-cli/v2/2.27.37/dist/awscli/botocore/data/s3/2006-03-01/service-2.json:      "documentation":"<p>Creates a copy of an object that is already stored in Amazon S3.</p> <note> <p>You can store individual objects of up to 5 TB in Amazon S3. You create a copy of your object up to 5 GB in size in a single atomic action using this API. However, to copy an object greater than 5 GB, you must use the multipart upload Upload Part - Copy (UploadPartCopy) API. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/CopyingObjctsUsingRESTMPUapi.html\">Copy Object Using the REST Multipart Upload API</a>.</p> </note> <p>You can copy individual objects between general purpose buckets, between directory buckets, and between general purpose buckets and directory buckets.</p> <note> <ul> <li> <p>Amazon S3 supports copy operations using Multi-Region Access Points only as a destination when using the Multi-Region Access Point ARN. </p> </li> <li> <p> <b>Directory buckets </b> - For directory buckets, you must make requests for this API operation to the Zonal endpoint. These endpoints support virtual-hosted-style requests in the format <code>https://<i>amzn-s3-demo-bucket</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com/<i>key-name</i> </code>. Path-style requests are not supported. For more information about endpoints in Availability Zones, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html\">Regional and Zonal endpoints for directory buckets in Availability Zones</a> in the <i>Amazon S3 User Guide</i>. For more information about endpoints in Local Zones, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html\">Concepts for directory buckets in Local Zones</a> in the <i>Amazon S3 User Guide</i>.</p> </li> <li> <p>VPC endpoints don't support cross-Region requests (including copies). If you're using VPC endpoints, your source and destination buckets should be in the same Amazon Web Services Region as your VPC endpoint.</p> </li> </ul> </note> <p>Both the Region that you want to copy the object from and the Region that you want to copy the object to must be enabled for your account. For more information about how to enable a Region for your account, see <a href=\"https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-standalone\">Enable or disable a Region for standalone accounts</a> in the <i>Amazon Web Services Account Management Guide</i>.</p> <important> <p>Amazon S3 transfer acceleration does not support cross-Region copies. If you request a cross-Region copy using a transfer acceleration endpoint, you get a <code>400 Bad Request</code> error. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html\">Transfer Acceleration</a>.</p> </important> <dl> <dt>Authentication and authorization</dt> <dd> <p>All <code>CopyObject</code> requests must be authenticated and signed by using IAM credentials (access key ID and secret access key for the IAM identities). All headers with the <code>x-amz-</code> prefix, including <code>x-amz-copy-source</code>, must be signed. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html\">REST Authentication</a>.</p> <p> <b>Directory buckets</b> - You must use the IAM credentials to authenticate and authorize your access to the <code>CopyObject</code> API operation, instead of using the temporary security credentials through the <code>CreateSession</code> API operation.</p> <p>Amazon Web Services CLI or SDKs handles authentication and authorization on your behalf.</p> </dd> <dt>Permissions</dt> <dd> <p>You must have <i>read</i> access to the source object and <i>write</i> access to the destination bucket.</p> <ul> <li> <p> <b>General purpose bucket permissions</b> - You must have permissions in an IAM policy based on the source and destination bucket types in a <code>CopyObject</code> operation.</p> <ul> <li> <p>If the source object is in a general purpose bucket, you must have <b> <code>s3:GetObject</code> </b> permission to read the source object that is being copied. </p> </li> <li> <p>If the destination bucket is a general purpose bucket, you must have <b> <code>s3:PutObject</code> </b> permission to write the object copy to the destination bucket. </p> </li> </ul> </li> <li> <p> <b>Directory bucket permissions</b> - You must have permissions in a bucket policy or an IAM identity-based policy based on the source and destination bucket types i...