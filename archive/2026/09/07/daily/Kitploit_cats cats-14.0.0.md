---
title: cats cats-14.0.0
url: https://kitploit.com/en/posts/github-endava-cats-cats-1400
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:41:02.904141
---

# cats cats-14.0.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/5565/7be11ec6fcbb7faea54573f1fe3deacc5a3fced12759b807114952279314bc56.png)

New releaseSep 7, 2026

# cats cats-14.0.0

Automated REST API fuzzer and negative testing tool for OpenAPI endpoints. Generates, runs, and reports thousands of self-healing tests with no coding effort, covering boundary and security scenarios.

Share

![CATS logo](https://raw.githubusercontent.com/Endava/cats/master/images/cats_logo_light.svg)

![CI](https://img.shields.io/github/actions/workflow/status/Endava/cats/main.yml?style=for-the-badge&logo=git&logoColor=white)
[![Commits](https://img.shields.io/github/commit-activity/m/Endava/cats?style=for-the-badge&logo=git&logoColor=white)](https://github.com/Endava/cats/pulse)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Java Version](https://img.shields.io/badge/Java-25+-blue.svg)](https://openjdk.org)
[![GraalVM](https://img.shields.io/badge/GraalVM-Native-orange.svg)](https://www.graalvm.org)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cats&metric=alert_status)](https://sonarcloud.io/dashboard?id=cats)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=cats&metric=coverage)](https://sonarcloud.io/dashboard?id=cats)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=cats&metric=bugs)](https://sonarcloud.io/dashboard?id=cats)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=cats&metric=code_smells)](https://sonarcloud.io/dashboard?id=cats)

> CATS documentation is available at <https://endava.github.io/cats/>

**REST API fuzzer and negative testing tool. Run thousands of self-healing API tests within minutes with no coding effort!**

* **Comprehensive**: tests are generated automatically based on a large number scenarios and cover **every** field and header
* **Intelligent**: tests are generated based on data types and constraints; each Fuzzer has specific expectations depending on the scenario under test
* **Highly Configurable**: high amount of customization: you can filter specific Fuzzers, HTTP response codes, HTTP methods, request paths, provide business context and a lot more
* **Self-Healing**: as tests are generated, any OpenAPI spec change is picked up automatically
* **Simple to Learn**: flat learning curve, with intuitive configuration and syntax
* **Fast**: automatic process for write, run and report tests which covers thousands of scenarios within minutes

> Short on time? Check out the [1-minute Quick Start Guide](https://endava.github.io/cats/docs/intro)!

# Overview

By using a simple and minimal syntax, with a flat learning curve, CATS (**C**ontract **A**PI **T**esting and **S**ecurity) enables you to generate thousands of API tests within minutes with **no coding effort**.
All tests are **generated, run and reported automatically** based on a pre-defined set of **100+ Fuzzers**.
The Fuzzers cover a wide range of boundary testing and negative scenarios from fully random large Unicode values to well crafted, context dependant values based on the request data types and constraints.
Even more, you can leverage the fact that CATS generates request payloads dynamically and write simple end-to-end functional tests.

## HTML Report

![CATS](https://assets.kitploit.com/production/public/readmes/5565/2776a3de53fc07694230600957c775be2c9e3ffae99e010e5d8260cdc7392056.png)

## Command Line

![CATS](https://assets.kitploit.com/production/public/readmes/5565/7be11ec6fcbb7faea54573f1fe3deacc5a3fced12759b807114952279314bc56.png)

# Tutorials on how to use CATS

This is a list of articles with step-by-step guides on how to use CATS:

* [Testing the GitHub API with CATS](https://ludovicianul.github.io/posts/github-api-testing/)
* [How to write self-healing functional tests with no coding effort](https://ludovicianul.github.io/posts/self-healing-api-tests/)

# Some bugs found by CATS

* <https://github.com/hashicorp/vault/issues/13274> | <https://github.com/hashicorp/vault/issues/13273>
* <https://github.com/hashicorp/vault/issues/13225> | <https://github.com/hashicorp/vault/issues/13232>
* <https://github.com/go-gitea/gitea/issues/19397> | <https://github.com/go-gitea/gitea/issues/19398>
* <https://github.com/go-gitea/gitea/issues/19399>

# Installation

## Homebrew

root@kitploit:~

```
> brew tap endava/tap
> brew install cats
```

## Manual

CATS is bundled both as an executable JAR or a native binary. The native binaries do not need Java installed.

After downloading your OS native binary, you can add it to PATH so that you can execute it as any other command line tool:

root@kitploit:~

```
sudo cp cats /usr/local/bin/cats
```

You can also get autocomplete by downloading the [cats\_autocomplete](https://github.com/endava/cats/blob/master/cats_autocomplete) script and do:

root@kitploit:~

```
source cats_autocomplete
```

To get persistent autocomplete, add the above line in `.zshrc` or `.bashrc`, but make sure you put the fully qualified path for the `cats_autocomplete` script.

You can also check the `cats_autocomplete` source for alternative setup.

There is no native binary for Windows, but you can use the uberjar version. This requires Java 25+ to be installed.

You can run it as `java -jar cats.jar`.

Head to the releases page to download the latest version: <https://github.com/Endava/cats/releases>.

## Build from sources

You can build CATS from sources on you local box. You need [Java 25](https://sdkman.io/jdks). Maven is already bundled.

> Before running the first build, please make sure you do a `./mvnw clean`. CATS uses a fork of [OKHttp](https://square.github.io/okhttp/) which will install locally
> under the `5.X.X-CATS` version, so don't worry about overriding the official versions.

You can use the following Maven command to build the project as an uberjar:

`./mvnw package -Dquarkus.package.type=uber-jar`

You will end up with a `cats-runner.jar` in the `target` folder. You can run it with `java -jar cats-runner.jar ...`.

You can also build native images using a [GraalVM Java version](https://www.graalvm.org/).

`./mvnw package -Pnative`

### Notes on Unit Tests

You may see some `error` log messages while running the Unit Tests. Those are expected behaviour for testing the negative scenarios of the Fuzzers.

# Contributing

Please refer to [CONTRIBUTING.md](https://github.com/endava/cats/blob/master/CONTRIBUTING.md).

[Read more](/en/tools/github/endava/cats?expand=1)

## Categories

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[API Security Testing](/en/categories/api-security-testing)[Web Security](/en/categories/web-security)[Fuzzing](/en/categories/fuzzing)

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