---
title: Dependency Scanning v2.1.1
url: https://kitploit.com/en/posts/gitlab-components-dependency-scanning-211
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:37.649207
---

# Dependency Scanning v2.1.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/649/3d944b47d3005b0ddf7ba7a201dc51b99e2680f991821b13823643ae589c40b5.png)

New releaseSep 3, 2026

# Dependency Scanning v2.1.1

Generates CycloneDX SBOMs and dependency scanning reports to identify project dependencies, licenses, and vulnerabilities within GitLab CI/CD pipelines.

Share

# Component for Dependency and License Scanning

This component generates a CycloneDX Software Bill of Materials, which is
used by GitLab to identify a project's dependencies, and their licenses. This
[CycloneDX Software Bill of Materials](https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscyclonedx) is compatible with the [GitLab taxonomy](https://docs.gitlab.com/ee/development/sec/cyclonedx_property_taxonomy.html).
Additionally, this component is capable of generating a [Dependency Scanning report](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportsdependency_scanning)
from the vulnerabilities detected in the project's dependencies.

## Requirements

This CI/CD component requires GitLab [dependency scanning](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/) capabilities, a
[GitLab Ultimate](https://about.gitlab.com/pricing/feature-comparison/) feature.

## Usage

Add the following snippet to your `.gitlab-ci.yml` to run the `dependency-scanning`
job with the default configuration.

root@kitploit:~

```
include:
  - component: $CI_SERVER_FQDN/components/dependency-scanning/main@<VERSION>
```

You can also customize the job uisng the CI/CD component's inputs. For example,
you can configure the log level and the job stage with the following configuration.

root@kitploit:~

```
include:
  - component: $CI_SERVER_FQDN/components/dependency-scanning/main@<VERSION>
    inputs:
      log_level: "debug"
      stage: "security-scanning"
```

> [!note]
> Make sure to set the component's version. Released versions may be found in the
> [tags section](https://gitlab.com/components/dependency-scanning/-/tags) of the
> project. More information on component versioning and available options may be
> found in [component versions documentation](https://docs.gitlab.com/ee/ci/components/#component-versions).

### Inputs

Please see the [catalog page](https://gitlab.com/explore/catalog/components/dependency-scanning)
for the complete list of allowed inputs.

## Contribute

1. Read how to [contribute to GitLab development](https://docs.gitlab.com/ee/development/contributing/)
   and the [Development guide for GitLab official CI/CD components](https://docs.gitlab.com/ee/development/cicd/components.html).
2. Submit a merge request, and follow the bot instructions.

## Release process

1. Promote unreleased changelogs with `changie batch auto`.
2. Update `CHANGELOG.md` with `changie merge`.
3. Create a new release using the latest version in the changelog with `git tag "$(changie latest -r)" && git push origin "$(changie latest -r)"`.

[Read more](/en/tools/gitlab/components/dependency-scanning?expand=1)

## Categories

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[DevSecOps](/en/categories/devsecops)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories