---
title: opencti v7.260824.0
url: https://kitploit.com/en/posts/github-opencti-platform-opencti-72608240
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:58:56.245919
---

# opencti v7.260824.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/352/cbb54d84d8ab10ea2ff1f19f4f9470d0be3ec6f5ee1ad3afce5a4b501de52f32.png)

New releaseAug 24, 2026

# opencti v7.260824.0

Open Cyber Threat Intelligence Platform

Share

# [![OpenCTI](https://assets.kitploit.com/production/public/readmes/352/3d342aee354db84cb4ec2e9cfe79ba57f9b84f0e7f0ddd4b7bc1ecf0f694eb7c.png)](https://opencti.io)

[![](https://img.shields.io/badge/website-opencti.io-blue.svg)](https://opencti.io)
[![](https://img.shields.io/badge/documentation-latest-orange.svg)](https://docs.opencti.io)
[![](https://img.shields.io/badge/slack-3K+%20members-4A154B)](https://community.filigran.io)
[![](https://drone.filigran.io/api/badges/OpenCTI-Platform/opencti/status.svg)](https://drone.filigran.io/OpenCTI-Platform/opencti)
[![](https://codecov.io/gh/OpenCTI-Platform/opencti/graph/badge.svg)](https://codecov.io/gh/OpenCTI-Platform/opencti)
[![DeepScan grade](https://deepscan.io/api/teams/4926/projects/6716/branches/57311/badge/grade.svg)](https://deepscan.io/dashboard#view=project&tid=4926&pid=6716&bid=57311)
[![DeepScan grade](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com)
[![](https://img.shields.io/docker/pulls/opencti/platform)](https://hub.docker.com/u/opencti)

## Introduction

OpenCTI is an open source platform allowing organizations to manage their cyber threat intelligence knowledge and observables. It has been created in order to structure, store, organize and visualize technical and non-technical information about cyber threats.

The structuration of the data is performed using a knowledge schema based on the [STIX2 standards](https://oasis-open.github.io/cti-documentation/). It has been designed as a modern web application including a [GraphQL API](https://graphql.org) and a UX-oriented frontend. Also, OpenCTI can be integrated with other tools and applications such as [MISP](https://github.com/MISP/MISP), [TheHive](https://github.com/TheHive-Project/TheHive), [MITRE ATT&CK](https://github.com/mitre/cti), etc.

![Screenshot](https://assets.kitploit.com/production/public/readmes/352/cbb54d84d8ab10ea2ff1f19f4f9470d0be3ec6f5ee1ad3afce5a4b501de52f32.png "Screenshot")

## Objective

The goal is to create a comprehensive tool allowing users to capitalize technical (such as TTPs and observables) and non-technical information (such as suggested attribution, victimology etc.) while linking each piece of information to its primary source (a report, a MISP event, etc.), with features such as links between each information, first and last seen dates, levels of confidence, etc. The tool is able to use the [MITRE ATT&CK framework](https://attack.mitre.org) (through a [dedicated connector](https://github.com/OpenCTI-Platform/connectors)) to help structure the data. The user can also choose to implement their own datasets.

Once data has been capitalized and processed by the analysts within OpenCTI, new relations may be inferred from existing ones to facilitate the understanding and the representation of this information. This allows the user to extract and leverage meaningful knowledge from the raw data.

OpenCTI not only allows [imports](https://docs.opencti.io/latest/usage/import-automated/) but also [exports of data](https://docs.opencti.io/latest/usage/feeds/) under different formats (CSV, STIX2 bundles, etc.). [Connectors](https://hub.filigran.io/cybersecurity-solutions/open-cti-integrations) are currently developed to accelerate interactions between the tool and other platforms.

## Editions of the platform

OpenCTI platform has 2 different editions: Community (CE) and Enterprise (EE). The purpose of the Enterprise Edition is to provide [additional and powerful features](https://filigran.io/offering/subscribe) which require specific investments in research and development. You can enable the Enterprise Edition directly in the settings of the platform.

* OpenCTI Community Edition, licensed under the [Apache 2, Version 2.0 license](https://github.com/opencti-platform/opencti/blob/HEAD/LICENSE).
* OpenCTI Enterprise Edition, licensed under the [Enterprise Edition license](https://github.com/opencti-platform/opencti/blob/HEAD/LICENSE).

To understand what OpenCTI Enterprise Edition brings in terms of features, just check the [Enterprise Editions page](https://filigran.io/offering/subscribe) on the Filigran website. You can also try this edition by enabling it in the settings of the platform.

## Documentation and demonstration

If you want to know more on OpenCTI, you can read the [documentation on the tool](https://docs.opencti.io). If you wish to discover how the OpenCTI platform is working, a [demonstration instance](https://demo.opencti.io) is available and open to everyone. This instance is reset every night and is based on reference data maintained by the OpenCTI developers.

## Releases download

The releases are available on the [Github releases page](https://github.com/OpenCTI-Platform/opencti/releases). You can also access the [rolling release package](https://releases.opencti.io) generated from the master branch of the repository.

## Installation

All you need to install the OpenCTI platform can be found in the [official documentation](https://docs.opencti.io). For installation, you can:

* [Use Docker](https://docs.opencti.io/latest/deployment/installation/#using-docker)
* [Install manually](https://docs.opencti.io/latest/deployment/installation/#install-manually)
* [Use Terraform (community)](https://docs.opencti.io/latest/deployment/installation/#terraform)
* [Use Helm charts (community)](https://docs.opencti.io/latest/deployment/installation/#helm-charts)

## Contributing

### Code of Conduct

OpenCTI has adopted a [Code of Conduct](https://github.com/opencti-platform/opencti/blob/HEAD/CODE_OF_CONDUCT.md) that we expect project participants to adhere to. Please read the [full text](https://github.com/opencti-platform/opencti/blob/HEAD/CODE_OF_CONDUCT.md) so that you can understand what actions will and will not be tolerated.

### Contributing Guide

Read our [contributing guide](https://github.com/opencti-platform/opencti/blob/HEAD/CONTRIBUTING.md) to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes to OpenCTI.

### Beginner friendly issues

To help you get familiar with our contribution process, we have a list of [beginner friendly issues](https://github.com/OpenCTI-Platform/opencti/labels/beginner%20friendly%20issue) which are fairly easy to implement. This is a great place to get started.

### Development

If you want to actively help OpenCTI, we created a [dedicated documentation](https://docs.opencti.io/latest/development/environment_ubuntu/) about the deployment of a development environment and how to start the source code modification.

## Community

### Status & bugs

Currently OpenCTI is under heavy development, if you wish to report bugs or ask for new features, you can directly use the [Github issues module](https://github.com/OpenCTI-Platform/opencti/issues).

### Discussion

If you need support or you wish to engage a discussion about the OpenCTI platform, feel free to join us on our [Slack channel](https://community.filigran.io). You can also send us an email to [[email protected]](/cdn-cgi/l/email-protection#a3c0cccdd7c2c0d7e3c5cacfcac4d1c2cd8dcacc).

## About

### Authors

OpenCTI is a product designed and developed by the company [Filigran](https://filigran.io).

[![](https://assets.kitploit.com/production/public/readmes/352/b03c59c13d0ea58d8aa8ed406b47bbacf1d4e2953fe64d2e94f58b93850a07db.png)](https://filigr...