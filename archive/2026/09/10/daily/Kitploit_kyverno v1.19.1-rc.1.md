---
title: kyverno v1.19.1-rc.1
url: https://kitploit.com/en/posts/github-kyverno-kyverno-v1191-rc1
source: Kitploit
date: 2026-09-10
fetch_date: 2026-09-11T06:51:42.641546
---

# kyverno v1.19.1-rc.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50828/4fb8aae1ab2eac22760efc734b40230d8e0286a3129d7faf0523332fcb75cfb9-display-v1.webp)

New releaseSep 10, 2026

# kyverno v1.19.1-rc.1

Enforce security and compliance on Kubernetes clusters via admission controls, resource mutation, background scans, and container image signature verification.

Share

# Kyverno [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Cloud%20Native%20Policy%20Management.%20No%20new%20language%20required%251&url=https://github.com/kyverno/kyverno/&hashtags=kubernetes,devops)

**Cloud Native Policy Management 🎉**

[![Build Status](https://github.com/kyverno/kyverno/actions/workflows/check-tests.yaml/badge.svg)](https://github.com/kyverno/kyverno/actions/workflows/check-tests.yaml)
[![Go Report Card](https://goreportcard.com/badge/github.com/kyverno/kyverno)](https://goreportcard.com/report/github.com/kyverno/kyverno)
![License: Apache-2.0](https://img.shields.io/github/license/kyverno/kyverno?color=blue)
[![GitHub Repo stars](https://img.shields.io/github/stars/kyverno/kyverno)](https://github.com/kyverno/kyverno/stargazers)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5327/badge)](https://bestpractices.coreinfrastructure.org/projects/5327)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/kyverno/kyverno/badge)](https://securityscorecards.dev/viewer/?uri=github.com/kyverno/kyverno)
[![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev)
[![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/kyverno)](https://artifacthub.io/packages/search?repo=kyverno)
[![codecov](https://codecov.io/gh/kyverno/kyverno/branch/main/graph/badge.svg)](https://app.codecov.io/gh/kyverno/kyverno/branch/main)
[![FOSSA Status](https://app.fossa.com/api/projects/git+github.com/kyverno/kyverno.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com/kyverno/kyverno?ref=badge_shield)

[![Kyverno Logo](https://assets.kitploit.com/production/public/readmes/50828/4fb8aae1ab2eac22760efc734b40230d8e0286a3129d7faf0523332fcb75cfb9/e380f93c3564fd4be9fba3f21776911a4ce1581d8c509ac2835ee5b81492e8a1-display-v1.webp)](https://kyverno.io)

## 📑 Table of Contents

* [About Kyverno](#about-kyverno)
* [Non-Goals](#non-goals)
* [Documentation](#-documentation)
* [Demos & Tutorials](#-demos--tutorials)
* [Popular Use Cases](#-popular-use-cases)
* [Explore the Policy Library](#-explore-the-policy-library)
* [Getting Help](#-getting-help)
* [Contributing](#-contributing)
* [Software Bill of Materials](#-software-bill-of-materials)
* [Contributors](#-contributors)
* [License](#-license)

## About Kyverno

Kyverno is a Kubernetes-native policy engine designed for platform engineering teams. It enables security, compliance, automation, and governance through policy-as-code. Kyverno can:

* Validate, mutate, generate, and clean up resources using Kubernetes admission controls and background scans.
* Verify container image signatures for supply chain security.
* Operate with tools you already use — like `kubectl`, `kustomize`, and Git.

[![Open Source Security Index badge](https://opensourcesecurityindex.io/badge.svg)](https://opensourcesecurityindex.io/)

## Non-Goals

Kyverno is only able to impact the policies used by Kubernetes and is **not** designed to address Kubernetes security flaws that are inherent in its design. For example, it cannot protect against vulnerabilities in the Kubernetes API server (e.g. Billion Laughs YAML deserialization, or a faulty Admission Controller implementation) or underlying infrastructure, and Kyverno's policy enforcement may be bypassed if Kubernetes itself has a security flaw. Kyverno does not enforce security requirements that were not explicitly defined — it enforces only the policies that users define and must be actively maintained like any other security product.

Kyverno does not replace, but works in conjunction with, Kubernetes RBAC: RBAC controls access while Kyverno enforces policy compliance. Cluster admins are expected to use RBAC to manage user and service account authorization, and then leverage Kyverno for additional checks that RBAC cannot perform.

Kyverno also does not replace Kubernetes' built-in policy controls like `ValidatingAdmissionPolicies` and `MutatingAdmissionPolicies`, but complements these native controls with additional features such as comprehensive reporting, exception management, and periodic background scanning.

Several capabilities that are out of scope for the core engine are addressed by companion projects in the Kyverno organization: end-to-end testing tooling ([Chainsaw](https://github.com/kyverno/chainsaw)), policy violation reporting and UI ([Policy Reporter](https://github.com/kyverno/policy-reporter)), policy evaluation for non-Kubernetes JSON payloads ([Kyverno JSON](https://github.com/kyverno/kyverno-json)), and authorization policy for service meshes ([Kyverno Envoy Plugin](https://github.com/kyverno/kyverno-envoy-plugin)). These are maintained as separate projects with their own release cycles.

## 📙 Documentation

Kyverno installation and reference documentation is available at [kyverno.io](https://kyverno.io).

* 👉 **[Quick Start](https://kyverno.io/docs/introduction/#quick-start)**
* 👉 **[Installation Guide](https://kyverno.io/docs/installation/)**
* 👉 **[Policy Library](https://kyverno.io/policies/)**

## 🎥 Demos & Tutorials

* ▶️ [Getting Started with Kyverno – YouTube](https://www.youtube.com/results?search_query=kyverno+tutorial)
* 🧪 [Kyverno Playground](https://playground.kyverno.io/)

## 🎯 Popular Use Cases

Kyverno helps platform teams enforce best practices and security standards. Some common use cases include:

### 1. **Security & Compliance**

* Enforce Pod Security Standards (PSS)
* Require specific security contexts
* Validate container image sources and signatures
* Enforce CIS Benchmark policies

### 2. **Operational Excellence**

* Auto-label workloads
* Enforce naming conventions
* Generate default configurations (e.g., NetworkPolicies)
* Validate YAML and Helm manifests

### 3. **Cost Optimization**

* Enforce resource quotas and limits
* Require cost allocation labels
* Validate instance types
* Clean up unused resources

### 4. **Developer Guardrails**

* Require readiness/liveness probes
* Enforce ingress/egress policies
* Validate container image versions
* Auto-inject config maps or secrets

## 📚 Explore the Policy Library

Discover hundreds of production-ready Kyverno policies for security, operations, cost control, and developer enablement.

👉 [Browse the Policy Library](https://kyverno.io/policies/)

## 🙋 Getting Help

We’re here to help:

* 🐞 File a [GitHub Issue](https://github.com/kyverno/kyverno/issues)
* 💬 Join the [Kyverno Slack Channel](https://slack.k8s.io/#kyverno)
* 📅 Attend [Community Meetings](https://kyverno.io/community/#community-meetings)
* ⭐️ [Star this repository](https://github.com/kyverno/kyverno/stargazers) to stay updated

## ➕ Contributing

Thank you for your interest in contributing to Kyverno!

* ✅ Read the [Contribution Guidelines](https://github.com/kyverno/kyverno/blob/main/CONTRIBUTING.md)
* 🤖 Read the [AI Usage Policy](https://github.com/kyverno/community/blob/main/AI_USAGE_POLICY.md)
* 🧵 Join [GitHub Discussions](https://github.com/kyverno/kyverno/discussions)
* 📖 Read the [Development Guide](https://github.com/kyverno/kyverno/blob/main/DEVELOPMENT.md)
* 🏁 Check [Good First Issues](https://github.com/kyverno/kyverno/labels/good%20first%20issue) a...