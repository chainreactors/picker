---
title: Harvesting GitLab Pipeline Secrets
url: https://blog.compass-security.com/2024/12/harvesting-gitlab-pipeline-secrets/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-04
fetch_date: 2025-10-06T19:41:28.909056
---

# Harvesting GitLab Pipeline Secrets

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Harvesting GitLab Pipeline Secrets](https://blog.compass-security.com/2024/12/harvesting-gitlab-pipeline-secrets/ "Harvesting GitLab Pipeline Secrets")

[December 3, 2024](https://blog.compass-security.com/2024/12/harvesting-gitlab-pipeline-secrets/ "Harvesting GitLab Pipeline Secrets")
 /
[Jan Friedli](https://blog.compass-security.com/author/jfriedli/ "Posts by Jan Friedli")
 /
[0 Comments](https://blog.compass-security.com/2024/12/harvesting-gitlab-pipeline-secrets/#respond)

> TLDR: Scan GitLab job logs for credentials using <https://github.com/CompassSecurity/pipeleak>

Many organizations use (self-hosted) GitLab instances to manage their source code and a lot of infrastructure is managed in code (IaC), thus these configurations must be source-controlled as well, putting a lot of responsibility on the source code platform in use. Often deployments are automated using CI/CD pipeline jobs. Each of these jobs has a log that users can access, and it is usually public. As these projects must handle secrets securely there is a lot of room for configuration errors.

## CI/CD Variable Handling

Usually, developers configure their secret variables in the [GitLab CI/CD Variables Settings](https://docs.gitlab.com/ee/ci/variables/). For each variable, there are multiple security-related configuration options.

**Visibility**

* Visible: The variable is visible in the job output log.
* Masked: Masked in job logs but value can be revealed in CI/CD settings. Requires values to meet regular expression requirements
* Masked and hidden: Masked in job logs, and can never be revealed in the CI/CD settings after the variable is saved.

**Flags**

* Protect variable: Export variable to pipelines running on protected branches and tags only.

Setting these as restrictive as possible is crucial as the job logs are [usually public](https://docs.gitlab.com/ee/ci/pipelines/settings.html#change-which-users-can-view-your-pipelines).

Many reasons exist why credentials might be leaked in the job output. Moreover, it is important to review generated artifacts as well. It is possible that credentials are not logged in the output but later saved in job artifacts, that can be downloaded.

## Typical Job Misconfigurations

The most obvious misconfiguration is logging sensitive values in the job output e.g. for debugging purposes and not protecting the values as described above. The following examples are real-world scenarios of job outputs.

```
# Example 0 - Echoing Google Cloud Credentials, variations of this include commands e.g. `printenv`, `env` etc.

$ mkdir -p ./creds
$ echo $GCLOUD_SERVICE_KEY | base64 -d > ./creds/serviceaccount.json
$ echo $GCLOUD_SERVICE_KEY
[cut by compass]
$ cat ./creds/serviceaccount.json
{
 "type": "service_account",
 "project_id": "[redacted by compass]",
 "private_key_id": "[redacted by compass]",
 "private_key": "-----BEGIN PRIVATE KEY-----[redacted by compass]-----END PRIVATE KEY-----\n",
 "client_email": "[redacted by compass].iam.gserviceaccount.com",
 "client_id": "[redacted by compass]",
 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
 "token_uri": "https://oauth2.googleapis.com/token",
 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
 "client_x509_cert_url": "[redacted by compass]",
 "universe_domain": "googleapis.com"
}
$ terraform init
Initializing the backend...
Successfully configured the backend "[redacted by compass]"! Terraform will automatically
use this backend unless the backend configuration changes.

# Example 1 - Echoing the SSH private key
$ git remote set-url origin "${CI_REPOSITORY_URL}"
Executing "step_script" stage of the job script
$ eval $(ssh-agent -s)
Agent pid 13
$ echo "$PRIVATE_KEY"
-----BEGIN OPENSSH PRIVATE KEY-----
[redacted by compass]
```

Another common issue is setting e.g. a tool’s verbosity to a debug level and not realizing that it does start to log sensitive values.

```
# Example 3 - SSH session used to deploy a setup using Docker and leaking the command line environment variables

debug1: Sending command: docker run -d --name my-api -e DATABASE_URL=postgresql://postgres:[redacted by compass]@postgres.[redacted by compass]rds.amazonaws.com/postgres -p 80:80 registry.gitlab.com/[redacted by compass]/api
debug1: channel 0: free: client-session, nchannels 1

# Example 4 - Node error log leaking the MongoDB connection string due to an error

$ npm install --silent
$ npm test --silent
(node:38) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
Server is running on  8000  Backend API
(node:38) [DEP0170] DeprecationWarning: The URL mongodb://admin:admin@[redacted by compass]:27017,[redacted by compass]:27017[redacted by compass]:27017/test?authSource=admin&replicaSet=[redacted by compass]&retryWrites=true&w=majority&ssl=true is invalid. Future versions of Node.js will throw an error.
==============Mongodb Database Connected Successfully==============
Database connection successful
 ✔ should establish a successful database connection (1041ms)
 1 passing (1s)
```

In reality, there are tons of variations of these issues.

## Harvesting Secrets

Now finding these secrets is quite cumbersome as groups and projects can contain a lot of jobs, that’s why we introduce you to [Pipeleak](https://github.com/CompassSecurity/pipeleak).

[![Pipeleak Logo](https://blog.compass-security.com/wp-content/uploads/2024/11/logo.png)](https://blog.compass-security.com/wp-content/uploads/2024/11/logo.png)

Pipeleak – Leaky Leek

Pipeleak automatically scans job logs for secrets. Its ruleset can be easily extended and it offers a [Trufflehog](https://github.com/trufflesecurity/trufflehog) integration, which allows finding verified credentials.

The Pipeleak scanner generates a log output printing any findings. In this example Pipeleak scans only jobs of projects that the current user is a member of and which match the search query `secret-pipelines`, filtering the results to `high` and `high-verified` only.

```
$ pipeleak --gitlab https://gitlab.com --token glpat-[cut by compass] --member --artifacts --cookie [cut by compass] --search secret-pipelines --confidence high,high-verified
2024-11-18T10:34:02Z INF Gitlab Version Check revision=40decc847c8 version=17.6.0-pre
2024-11-18T10:34:02Z INF Fetching projects
2024-11-18T10:34:02Z INF Provided GitLab session cookie is valid
2024-11-18T10:34:02Z INF Filtering scanned projects by query=secret-pipelines
2024-11-18T10:34:05Z INF Fetched all projects
2024-11-18T10:34:07Z WRN HIT Artifact (in archive) archive=artifact_archive_file.tar confidence=high file=secrets_in_archive.txt jobName=archives-job ruleName="Generic - 1719" url=gitlab.com/frj1comp/secret-pipelines/-/jobs/8398606421 value="datadog_api_key=secrets.txt file hit "
[cut by compass]
2024-11-18T10:34:07Z WRN HIT confidence=high jobName=build-job ruleName="AWS API Key" url=gitlab.com/frj1comp/secret-pipelines/-/jobs/8398625852 value="ruffle Hog AKIAYVP4CIPPERUVIFXG\" Truffle Hog AKIAYVP4CIPPERUVIFXG $ echo \"https://gitlab-ci-token:$MASK_ME@g"
[cut by compass]
2024-11-18T10:34:07Z WRN HIT DOTENV: Check artifacts page which is the only place to download the dotenv file artifactUrl=gitlab.com/frj1comp/secret-pipelines/-/jobs/8398606415/-/artifacts confidence=high jobId=8398606...