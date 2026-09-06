---
title: peirates v1.1.31
url: https://kitploit.com/en/posts/github-inguardians-peirates-v1131
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:32.328216
---

# peirates v1.1.31

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/4705/e025f91f4703189c1e93234ef16f699b9a65ccd2aa7cb56c95c5caceaf962b9d.png)

New releaseSep 5, 2026

# peirates v1.1.31

Peirates - Kubernetes Penetration Testing tool

Share

# Peirates

[![Release](https://img.shields.io/github/release/inguardians/peirates.svg?style=flat-square)](https://github.com/inguardians/peirates/releases/latest) [![gosec](https://github.com/inguardians/peirates/actions/workflows/gosec.yml/badge.svg)](https://github.com/inguardians/peirates/actions/workflows/gosec.yml)

![Logo](https://assets.kitploit.com/production/public/readmes/4705/e025f91f4703189c1e93234ef16f699b9a65ccd2aa7cb56c95c5caceaf962b9d.png)

## What is Peirates?

Peirates, a Kubernetes penetration tool, enables an attacker to escalate privilege and pivot
through a Kubernetes cluster. It automates known techniques to steal and collect service account tokens,
secrets, obtain further code execution, and gain control of the cluster.

## Where do I run Peirates?

You run Peirates from a container running on Kubernetes or from a Kubernetes node, outside the container.

## Does Peirates attack a Kubernetes cluster?

Yes, it absolutely does. Talk to your lawyer and the cluster owners before using this tool in a Kubernetes cluster.

## Who creates Peirates?

InGuardians' CTO Jay Beale first conceived of Peirates and put together a group of InGuardians developers
to create it with him, including Faith Alderson, Adam Crompton and Dave Mayer. Faith convinced us to all
learn Golang, so she could implement the tool's use of the kubectl library from the Kubernetes project.
Adam persuaded the group to use a highly-interactive user interface. Dave brought contagious enthusiasm.
Together, these four developers implemented attacks and began releasing this tool that we use on our
penetration tests.

Other contributors have helped as well - see GitHub to see more, but please also review [credits.md](https://github.com/inguardians/peirates/blob/main/credits.md).

## Do you welcome contributions?

Yes, we absolutely do. Submit a pull request and/or reach out to [[email protected]](/cdn-cgi/l/email-protection#afdfcac6ddcedbcadc82cbcad9efc6c1c8daceddcbc6cec1dc81ccc0c2).

## What license is this released under?

Peirates is released under the GPLv2 license.

## Running Peirates

If you just want the peirates binary to start attacking things, grab the latest
release from the [releases page](https://github.com/inguardians/peirates/releases/latest).

For command behavior, prerequisites, side effects, cleanup, and troubleshooting,
see the [main menu command reference](https://github.com/inguardians/peirates/blob/main/docs/commands/README.md).

## Peirates as a Container Image

You can find a useful [alpine-peirates container image on Docker Hub](https://hub.docker.com/r/bustakube/alpine-peirates), with a version number tag that tracks the Peirates version.

For example, for `alpine-peirates:v1.1.27d`, which contains peirates version `v1.1.27d`, run:

root@kitploit:~

```
docker pull bustakube/alpine-peirates:v1.1.27d
```

## Building Peirates

However, if you want to build from source, read on!

Get peirates

root@kitploit:~

```
go get -v "github.com/inguardians/peirates"
```

Get libary sources if you haven't already (Warning: this will take almost a
gig of space because it needs the whole kubernetes repository)

root@kitploit:~

```
go get -v "k8s.io/kubectl/pkg/cmd" "github.com/aws/aws-sdk-go"
```

Build the executable

root@kitploit:~

```
cd $GOPATH/github.com/inguardians/peirates
make
```

The default `build` target generates a statically linked Linux AMD64 executable
named `peirates` in the repository root. You can also invoke it explicitly with
`make build`.

Build compressed Linux distributions for AMD64, ARM, ARM64, and 386:

root@kitploit:~

```
make dist
```

Distribution archives contain statically linked binaries and are written to
`scripts/`. Set `DIST_COMPRESS=no` to keep unpacked binaries or
`DIST_ARCHES=amd64` to build a subset of architectures. Individual targets such
as `make dist-arm64` are also available.

[Read more](/en/tools/github/inguardians/peirates?expand=1)

## Categories

[Privilege Escalation](/en/categories/privilege-escalation)[Container Security](/en/categories/container-security)[Exploitation](/en/categories/exploitation)[Information Gathering](/en/categories/information-gathering)[Post-Exploitation](/en/categories/post-exploitation)[Penetration Testing](/en/categories/penetration-testing)[Cloud Security](/en/categories/cloud-security)[Container Escape](/en/categories/container-escape)

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