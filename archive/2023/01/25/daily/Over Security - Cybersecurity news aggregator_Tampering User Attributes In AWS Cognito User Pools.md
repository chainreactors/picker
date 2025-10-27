---
title: Tampering User Attributes In AWS Cognito User Pools
url: https://blog.doyensec.com//2023/01/24/tampering-unrestricted-user-attributes-aws-cognito.html
source: Over Security - Cybersecurity news aggregator
date: 2023-01-25
fetch_date: 2025-10-04T04:45:01.955271
---

# Tampering User Attributes In AWS Cognito User Pools

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

# Tampering User Attributes In AWS Cognito User Pools

24 Jan 2023 - Posted by Francesco Lacerenza, Mohamed Ouad

![CloudsecTidbit](../../../public/images/cloudsectidbit-logo200.jpg)

### From The Previous Episodeâ¦ Did you solve the CloudSecTidbit Ep. 1 IaC lab?

#### Solution

The challenge for the [data-import](https://blog.doyensec.com/2022/10/18/cloudsectidbit-dataimport.html) CloudSecTidbit is basically reading the content of an internal bucket. The frontend web application is using the targeted bucket to store the logo of the app.

The name of the bucket is returned to the client by calling the `/variable` endpoint:

```
$.ajax({
    type: 'GET',
    url: '/variable',
    dataType: 'json',
    success: function (data) {
        let source_internal = `https://${data}.s3.amazonaws.com/public-stuff/logo.png?${Math.random()}`;
        $(".logo_image").attr("src", source_internal);
    },
    error: function (jqXHR, status, err) {
        alert("Error getting variable name");
    }
});
```

The server will return something like:

```
"data-internal-private-20220705153355922300000001"
```

So the schema should be clear now. Letâs use the data import functionality and try to leak the content of the `data-internal-private` S3 bucket:

![](/public/images/cloudsectidbit-dataimported.png)
*Extracting data from the internal S3 bucket*

Then, by visiting the Data Gallery section, you will see the `keys.txt` and `dummy.txt` objects, which are stored within the internal bucket.

## Tidbit No. 2 - Tampering User Attributes In AWS Cognito User Pools

Amazon Web Services offer a complete solution to add user sign-up, sign-in, and access control to web and mobile applications: Cognito. Letâs first talk about the service in general terms.

From AWS Cognitoâs welcome page:

> âUsing the Amazon Cognito user pools API, you can create a user pool to
> manage directories and users. You can authenticate a user to obtain tokens
> related to user identity and access policies.â

Amazon Cognito collects a userâs profile attributes into directories called **pools** that an application uses to handle all authentication related tasks.

### Pool Types

The two main components of Amazon Cognito are:

* **User pools**: Provide sign-up and sign-in options for app users along with
  attributes association for each user.
* **Identity pools**: Provide the possibility to grant users access to other
  AWS services (e.g., DynamoDB or Amazon S3).

With a user pool, users can sign in to an app through Amazon Cognito, OAuth2, and SAML identity providers.

Each user has a profile that applications can access through the software development kit (SDK).

### User Attributes

User attributes are pieces of information stored to characterize individual users, such as name, email address, and phone number. A new user pool has a set of default *standard attributes*. It is also possible to add custom attributes to satisfy custom needs.

### App Clients & Authentication

An app is an entity within a user pool that has permission to call management operation APIs, such as those used for user registration, sign-in, and forgotten passwords.

In order to call the operation APIs, an app client ID and an optional client secret are needed. Multiple app integrations can be created for a single user pool, but typically, an app client corresponds to the platform of an app.

A user can be authenticated in different ways using Cognito, but the main options are:

* **Client-side authentication flow** - Used in client-side apps to obtain
  a valid session token (JWT) directly from the pool;
* **Server-side authentication flow** - Used in server-side app with the authenticated server-side API for Amazon Cognito user pools. The server-side app calls the `AdminInitiateAuth` API operation. This operation requires AWS credentials with permissions that include `cognito-idp:AdminInitiateAuth` and `cognito-idp:AdminRespondToAuthChallenge`. The operation returns the required authentication parameters.

In both the cases, the end-user should receive the resulting JSON Web Token.

After that first look at AWS SDK credentials, we can jump straight to the tidbit case.

### Unrestricted User Attributes Write in AWS Cognito User Pool - The Third-party Users Mapping Case

For this case, we will focus on a vulnerability identified in a Web
Platform that was using AWS Cognito.

The platform used Cognito to manage users and map them to their account in a third-party platform *X\_platform* strictly interconnected with the provided service.

In particular, users were able to connect their *X\_platform* account and allow the platform to fetch their data in *X\_platform* for later use.

```
{
  "sub": "cf9..[REDACTED]",
  "device_key": "us-east-1_ab..[REDACTED]",
  "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_..[REDACTED]",
  "client_id": "9..[REDACTED]",
  "origin_jti": "ab..[REDACTED]",
  "event_id": "d..[REDACTED]",
  "token_use": "access",
  "scope": "aws.cognito.signin.user.admin",
  "auth_time": [REDACTED],
  "exp": [REDACTED],
  "iat": [REDACTED],
  "jti": "3b..[REDACTED]",
  "username": "[REDACTED]"
}
```

In AWS Cognito, user tokens permit calls to all the User Pool APIs that can be hit using access tokens alone.

The permitted API definitions can be found [here](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_Operations.html).

If the request syntax for the API call includes the parameter `"AccessToken": "string"`, then it allows users to modify something on their own UserPool entry with the previously inspected JWT.

The above described design does not represent a vulnerability on its own, but having users able to edit their own User Attributes in the pool could lead to severe impacts if the backend is using them to apply internal platform logic.

The user associated data within the pool was fetched by using the AWS CLI:

```
$ aws cognito-idp get-user --region us-east-1--access-token eyJra..[REDACTED SESSION JWT]
```

```
{
    "Username": "[REDACTED]",
    "UserAttributes": [
        {
            "Name": "sub",
            "Value": "cf915â¦[REDACTED]"
        },
        {
            "Name": "email_verified",
            "Value": "true"
        },
        {
            "Name": "name",
            "Value": "[REDACTED]"
        },
        {
            "Name": "custom:X_platform_user_id",
            "Value": "[REDACTED ID]"
        },
        {
            "Name": "email",
            "Value": "[REDACTED]"
        }
    ]
}
```

## The Simple Deduction

After finding the `X_platform_user_id` user pool attribute, it was clear
that it was there for a specific purpose. In fact, the platform was
fetching the attribute to use it as the primary key to query the
associated `refresh_token` in an internal database.

Attempting to spoof the attribute was as simple as executing:

```
$ aws --region us-east-1 cognito-idp update-user-attributes --user-attributes "Name=custom:X_platform_user_id,Value=[ANOTHER REDACTED ID]" --access-token eyJra..[REDACTED SESSION JWT]
```

![](/public/images/cloudsectidbit-otherjokes.png)

The attribute edit succeeded and the data from the other user started to flow into the attackerâs account. The platform trusted the attribute as immutable and used it to retrieve a `refresh_token` needed to fetch and show data from *X\_platform* in the UI.

## Point Of The Story - Default READ/WRITE Perms On U...