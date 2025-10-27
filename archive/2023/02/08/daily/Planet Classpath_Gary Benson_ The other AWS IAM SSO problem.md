---
title: Gary Benson: The other AWS IAM SSO problem
url: https://gbenson.net/sessionless-aws-iam-sso/
source: Planet Classpath
date: 2023-02-08
fetch_date: 2025-10-04T05:55:45.980134
---

# Gary Benson: The other AWS IAM SSO problem

[Skip to content](#content)

[gbenson.net](https://gbenson.net/)

# The other AWS IAM SSO problem

[gbenson](https://gbenson.net/author/admin/ "Posts by gbenson")

[AWS](https://gbenson.net/category/aws/), [Gotchas](https://gbenson.net/category/gotchas/)

Tuesday 7th February 2023Tuesday 7th February 2023
1 Minute

The other thing you’ll run into using IAM users in AWS CLI is that a lot of things don’t support SSO sessions anyway. If you [configure an IAM user with an SSO session name](https://gbenson.net/aws-cli-with-iam-users/ "Using AWS CLI with IAM users") as recommended you’ll get errors like this:

```
$ eb init -p python-3.8 eb-flask-app
ERROR: InvalidConfigError - The profile "default" is configured to use SSO but is missing required configuration: sso_start_url, sso_region
```

and this:

```
$ terraform apply
| Error: configuring Terraform AWS Provider: loading configuration: profile "default" is configured to use SSO but is missing required configuration: sso_region, sso_start_url
```

You can fix these by configuring without an SSO session:

```
$ aws configure sso
SSO session name (Recommended):
WARNING: Configuring using legacy format (e.g. without an SSO session).
Consider re-running "configure sso" command and providing a session name.
SSO start URL [None]: https://whatever.awsapps.com/start
SSO region [None]: us-east-1
 ...
```

You can also fix them by just editing your `~/.aws/config`, and copying the `sso_start_url` and `sso_region` keys from the `[sso-session ...]` section into the relevant user’s section, but that might be a hack too far!

* Tagged
* [AWS](https://gbenson.net/tag/aws/)

![](https://secure.gravatar.com/avatar/7f5ceed659dcc3dfbbaabaa442f88548841b5c261110017a8d507eb468d1a875?s=80&d=mm&r=g)

## Published by gbenson

I make things // he/him [View all posts by gbenson](https://gbenson.net/author/admin/)

**Published**
Tuesday 7th February 2023Tuesday 7th February 2023

## Post navigation

[Previous Post Using AWS CLI with IAM users](https://gbenson.net/aws-cli-with-iam-users/)

[Next Post Flask on Elastic Beanstalk](https://gbenson.net/elastic-beanstalk-flask/)

[Proudly powered by WordPress](http://wordpress.org/)
 |
Theme: Independent Publisher 2 by [Raam Dev](http://raamdev.com/).