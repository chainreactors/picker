---
title: gitlab-runner-research – PoC for abusing self-hosted GitLab runners
url: https://www.darknet.org.uk/2025/11/gitlab-runner-research-poc-for-abusing-self-hosted-gitlab-runners/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-04
fetch_date: 2025-11-05T03:12:12.784629
---

# gitlab-runner-research – PoC for abusing self-hosted GitLab runners

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# gitlab-runner-research – PoC for abusing self-hosted GitLab runners

November 3, 2025

Views: 122

gitlab-runner-research is a proof-of-concept repository and write-up that demonstrates how attackers can register or abuse self-hosted GitLab runners to execute arbitrary pipeline jobs. The repository contains scripts and job templates that show how an attacker can discover or misuse runner registration tokens, register a runner, run malicious jobs, and access artifacts or secrets when runner configuration and isolation are weak.

![gitlab-runner-research - PoC for abusing self-hosted GitLab runners](https://www.darknet.org.uk/wp-content/uploads/2025/11/gitlab-runner-research-PoC-for-abusing-self-hosted-GitLab-runners-640x427.jpg)

## Overview

Self-hosted GitLab runners execute CI/CD jobs with the privileges and network access available to the runner host. When operator controls are weak, exposed registration tokens, an overbroad runner scope, or missing network isolation, an attacker can weaponise a runner. This PoC documents repeatable techniques for registering runners, pushing malicious pipeline jobs, and using job execution to read artifacts, extract variables, or access internal services.

## Features

* **Registration automation:** scripts to automate runner registration where tokens are discoverable.
* **Malicious job templates:** pipeline examples designed to request artifacts, enumerate environment variables, and probe internal endpoints.
* **Reproducible test harness:** step-by-step instructions for deploying an isolated runner and reproducing the behavior in a lab environment.
* **Defensive checklist:** concise mitigations and detection guidance defenders can apply immediately.

## Installation

Clone the repository locally and review the README and blog writeup before running anything. Do not run these scripts against production systems or environments you do not control.

git clone https://github.com/Frichetten/gitlab-runner-research.git
cd gitlab-runner-research

|  |  |
| --- | --- |
| 1  2 | git clone https://github.com/Frichetten/gitlab-runner-research.git  cd gitlab-runner-research |

Follow the repository README and the author’s blog for environment setup, test guidance, and screenshots.

## Usage

Use the PoC only in a controlled lab. A safe workflow is:

* Deploy a disposable GitLab instance or use a sandboxed test project on an isolated GitLab server.
* Inspect the runner registration scripts and confirm you have a test registration token. Do not use production tokens.
* Register a test runner on a VM or container you control using the test token.
* Run the provided job templates in the isolated project and observe what the job can access (artifacts, variables, network).
* Collect logs, job traces, and network captures to build detection rules and validate mitigations.

## Attack Scenario

**Objective**: convert a discovered registration token into operational access through runner abuse.

1. **Discovery:** search public code, wikis, CI configs, or misconfigured storage for exposed registration tokens or leaked CI variables.
2. **Registration:** use a token to register a runner at project, group, or instance scope, depending on the token’s privileges.
3. **Delivery:** push a CI configuration that triggers a job with steps to read accessible artifacts, call internal services, or fetch secrets from mounted paths.
4. **Execution:** the runner executes the job. If the runner host has network egress or mounted credentials, the job can access sensitive data or pivot further.
5. **Exfiltration/pivot:** job exfiltrates data to an attacker-controlled endpoint or uses recovered credentials to access other systems.

## Red Team Relevance

This PoC provides red teams with a compact, high-impact way to demonstrate CI/CD risk. Use the PoC to produce clear, reproducible evidence of business impact (artifact theft, secret exfiltration, lateral movement) and to drive rapid remediation. For follow-up validation, combine findings with proxy testing using Burp Suite and OWASP ZAP or fuzzing approaches from the Darknet fuzzing archive.

## Detection and Mitigation

* **Disable instance-wide runners:** avoid instance-scoped runners unless required. Prefer project- or group-scoped runners with strict enrollment controls.
* **Protect registration tokens:** treat tokens as secrets, store them in a vault, rotate them regularly, and never commit them to repositories or wikis.
* **Isolate runners:** place runners in restricted networks, enforce egress controls, and run jobs in non-privileged containers without host mounts.
* **Least privilege:** limit IAM and service account privileges available to CI hosts and runners.
* **Hunt and alert:** detect new runner registrations, unusual runner hostnames, or runners picking up jobs outside standard patterns.
* **Pipeline constraints:** require protected branches, enforce merge request approvals for sensitive pipelines, use protected variables and job token scoping.
* **Audit and logging:** centralise CI logs and job outputs, and trigger alerts on attempts to access artifacts across projects or call internal metadata endpoints.

## Comparison

Runner abuse sits alongside other CI/CD threats: leaked secrets, OIDC misconfiguration,s and over-permissioned service accounts. Self-hosted runners increase risk because the runner owner controls the execution environment. This PoC focuses on operational abuse through runtime execution rather than static secret scanning.

Other related tools are [GitLab Watchman – Audit Gitlab For Sensitive Data & Credentials](https://www.darknet.org.uk/2021/02/gitlab-watchman-audit-gitlab-for-sensitive-data-credentials/) and [Anteater – CI/CD Security Gate Check Framework](https://www.darknet.org.uk/2019/08/anteater-ci-cd-security-gate-check-framework/).

## Conclusion

gitlab-runner-research demonstrates how misconfigured self-hosted runners become a high-impact attack surface. Publish a two-part series for maximum operational value: Part 1 that walks the attack chain with screenshots and PoC output, and Part 2 that delivers a concise detection and hardening playbook security teams can action immediately. Protect runners with token hygiene, network isolation, least privilege, and robust logging.

You can read more or download gitlab-runner-research here: <https://github.com/Frichetten/gitlab-runner-research>

## Related Posts:

* [GitLab Watchman - Audit Gitlab For Sensitive Data &…](https://www.darknet.org.uk/2021/02/gitlab-watchman-audit-gitlab-for-sensitive-data-credentials/)
* [XRayC2 - Weaponizing AWS X-Ray for Covert Command…](https://www.darknet.org.uk/2025/10/xrayc2-weaponizing-aws-x-ray-for-covert-command-and-control-c2/)
* [HoneyBee - Misconfigured App Generator for Red Team…](https://www.darknet.org.uk/2025/10/honeybee-misconfigured-app-generator-for-red-team-validation/)
* [Doppler CLI - Streamlined Secre...