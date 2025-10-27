---
title: The Danger of Falling to System Role in AWS SDK Client
url: https://blog.doyensec.com//2022/10/18/cloudsectidbit-dataimport.html
source: Over Security - Cybersecurity news aggregator
date: 2022-10-20
fetch_date: 2025-10-03T20:25:07.226805
---

# The Danger of Falling to System Role in AWS SDK Client

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# The Danger of Falling to System Role in AWS SDK Client

18 Oct 2022 - Posted by Francesco Lacerenza, Mohamed Ouad

![CloudsecTidbit](../../../public/images/cloudsectidbit-logo200.png)

## Introduction to the series

When it comes to Cloud Security, the first questions usually asked are:

* How is the infrastructure configured?
* Are there any public buckets?
* Are the VPC networks isolated?
* Does it use proper IAM settings?

As application security engineers, we think that there are more interesting and context-related questions such as:

* Which services provided by the cloud vendor are used?
* Among the used services, which ones are directly integrated within the web platform logic?
* How is the web application using such services?
* How are they combined to support the internal logic?
* Is the usage of services ever exposed or reachable by the end-user?
* Are there any unintended behaviors caused by cloud services within the web platform?

By answering these questions, **we usually find bugs**.

Today we introduce the â**CloudSecTidbits**â series to share ideas and knowledge about such questions.

CloudSec Tidbits is a blogpost series showcasing interesting bugs found by Doyensec during cloud security testing activities. Weâll focus on times when the cloud infrastructure is properly configured, but the web application fails to use the services correctly.

Each blogpost will discuss a specific vulnerability resulting from an insecure combination of web and cloud related technologies. Every article will include an [Infrastructure as Code (IaC) laboratory](https://github.com/doyensec/cloudsec-tidbits/) that can be easily deployed to experiment with the described vulnerability.

## Tidbit # 1 - The Danger of Falling to System Role in AWS SDK Client

Amazon Web Services offers a comprehensive SDK to interact with their cloud services.

Letâs first examine how credentials are configured. The AWS SDKs require users to pass access / secret keys in order to authenticate requests to AWS. Credentials can be specified in different ways, depending on the different use cases.

When the AWS client is initialized without directly providing the credentialâs source, the AWS SDK acts using a clearly defined logic. The AWS SDK uses a different credential provider chain depending on the base language. The credential provider chain is an ordered list of sources where the AWS SDK will attempt to fetch credentials from. The first provider in the chain that returns credentials without an error will be used.

For example, the SDK for the Go language will use the following chain:

1. 1) Environment variables
2. 2) Shared credentials file
3. 3) If the application uses ECS task definition or RunTask API operation, IAM role for tasks
4. 4) If the application is running on an Amazon EC2 instance, IAM role for Amazon EC2

The code snippet below shows how the SDK retrieves the first valid credential provider:

Source: [aws-sdk-go/aws/credentials/chain\_provider.go](https://github.com/aws/aws-sdk-go/blob/bef02444773a49eaf30cdd615920b56896827c06/aws/credentials/chain_provider.go#L67)

```
// Retrieve returns the credentials value or error if no provider returned
// without error.
//
// If a provider is found it will be cached and any calls to IsExpired()
// will return the expired state of the cached provider.
func (c *ChainProvider) Retrieve() (Value, error) {
	var errs []error
	for _, p := range c.Providers {
		creds, err := p.Retrieve()
		if err == nil {
			c.curr = p
			return creds, nil
		}
		errs = append(errs, err)
	}
	c.curr = nil

	var err error
	err = ErrNoValidProvidersFoundInChain
	if c.VerboseErrors {
		err = awserr.NewBatchError("NoCredentialProviders", "no valid providers in chain", errs)
	}
	return Value{}, err
}
```

After that first look at AWS SDK credentials, we can jump straight to the tidbit case.

### Insecure AWS SDK Client Initialization In User Facing Functionalities - The Import From S3 Case

By testing several web platforms, we noticed that data import from external cloud services is an often recurring functionality. For example, some web platforms allow data import from third-party cloud storage services (e.g., AWS S3).

In this specific case, we will focus on a vulnerability identified in a web application that was using the AWS SDK for Go (v1) to implement an âImport Data From S3â functionality.

The user was able to make the platform fetch data from S3 by providing the following inputs:

* S3 bucket name - Import from public source case;

  **OR**
* S3 bucket name + AWS Credentials - Import from private source case;

The code paths were handled by a function similar to the following structure:

```
func getObjectsList(session *Session, config *aws.Config, bucket_name string){

	//initilize or re-initilize the S3 client
	S3svc := s3.New(session, config)

	objectsList, err := S3svc.ListObjectsV2(&s3.ListObjectsV2Input{
			Bucket:  bucket_name
	})

	return objectsList, err
}

func importData(req *http.Request) (success bool) {

	srcConfig := &aws.Config{
		Region: &config.Config.AWS.Region,
	}

	req.ParseForm()
	bucket_name := req.Form.Get("bucket_name")
	accessKey := req.Form.Get("access_key")
	secretKey := req.Form.Get("secret_key")
	region := req.Form.Get("region")

	session_init, err := session.NewSession()
	if err != nil {
		return err, nil
	}

	aws_config = &aws.Config{
		Region: region,
	}

	if len(accessKey) > 0 {
		aws_config.Credentials = credentials.NewStaticCredentials(accessKey, secretKey, "")
	} else {
		aws_config.Credentials = credentials.AnonymousCredentials
	}

	objectList, err := getObjectsList(session_init, aws_config, bucket_name)

...
```

Despite using `credentials.AnonymousCredentials` when the user was not providing keys, the function had an interesting code path when `ListObjectsV2` returned errors:

```
...
if err != nil {
		if err, awsError := err.(awserr.Error); awsError {
			aws_config.credentials = nil
			getObjectsList(session_init, aws_config, bucket_name)
		}
}
```

The error handling was setting `aws_config.credentials = nil` and trying again to list the objects in the bucket.

![](/public/images/cloudsectidbit-fry.png)
*Looking at `aws_config.credentials = nil`*

Under those circumstances, the credentials provider chain will be used and eventually the instanceâs IAM role will be assumed. In our case, the automatically retrieved credentials had full access to internal S3 buckets.

### The Simple Deduction

If internal S3 bucket names are exposed to the end-user by the platform (e.g., via network traffic), the user can use them as input for the âimport from S3â functionality and inspect their content directly in the UI.

![](/public/images/cloudsectidbit-spongebob.jpeg)
*Reading internal bucket names list extracted from Burp Suite history*

In fact, it is not uncommon to see internal bucket names in an applicationâs traffic as they are often used for internal data processing. In conclusion, providing internal bucket names resulted in them being fetched from the import functionality and added to the platform userâs data.

### Different Client Credentials Initialization, Different Outcomes

AWS SDK clients require a `Session` object containing a `Credential` object for the initialization.

Described below are the three main ways to set the credentials needed by the client:

#### NewStaticCredentials

Within the credentials package, the `NewStaticCrede...