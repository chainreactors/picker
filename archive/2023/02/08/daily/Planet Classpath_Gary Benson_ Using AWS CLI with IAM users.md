---
title: Gary Benson: Using AWS CLI with IAM users
url: https://gbenson.net/aws-cli-with-iam-users/
source: Planet Classpath
date: 2023-02-08
fetch_date: 2025-10-04T05:55:47.136294
---

# Gary Benson: Using AWS CLI with IAM users

[Skip to content](#content)

[gbenson.net](https://gbenson.net/)

# Using AWS CLI with IAM users

[gbenson](https://gbenson.net/author/admin/ "Posts by gbenson")

[AWS](https://gbenson.net/category/aws/), [Gotchas](https://gbenson.net/category/gotchas/)

Monday 6th February 2023Tuesday 7th February 2023
1 Minute

When you [configure AWS CLI to use an IAM user](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html "Configuring the AWS CLI to use AWS IAM Identity Center"), the first thing it asks for is an SSO session name. *Don’t put whitespace or punctuation in it.* The command doesn’t tell you this, but it’s going to use what you enter as an identifier, and fail with a cryptic error:

```
$ aws configure sso
SSO session name (Recommended): AWS CLI on Gary's Chromebook
SSO start URL [None]: https://whatever.awsapps.com/start
SSO region [None]: us-east-1
SSO registration scopes [sso:account:access]:

An error occurred (InvalidClientMetadataException) when calling the RegisterClient operation:
```

You need to put something like “gbenson” in there.

* Tagged
* [AWS](https://gbenson.net/tag/aws/)

![](https://secure.gravatar.com/avatar/7f5ceed659dcc3dfbbaabaa442f88548841b5c261110017a8d507eb468d1a875?s=80&d=mm&r=g)

## Published by gbenson

I make things // he/him [View all posts by gbenson](https://gbenson.net/author/admin/)

**Published**
Monday 6th February 2023Tuesday 7th February 2023

## Post navigation

[Previous Post sed trick](https://gbenson.net/sed-trick/)

[Next Post The other AWS IAM SSO problem](https://gbenson.net/sessionless-aws-iam-sso/)

[Proudly powered by WordPress](http://wordpress.org/)
 |
Theme: Independent Publisher 2 by [Raam Dev](http://raamdev.com/).