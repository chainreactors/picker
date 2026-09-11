---
title: serverless sf-core@4.42.0
url: https://kitploit.com/en/posts/github-serverless-serverless-sf-core4420
source: Kitploit
date: 2026-09-10
fetch_date: 2026-09-11T06:51:40.366880
---

# serverless sf-core@4.42.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50832/e987c7aea737c207de190530e4b108d3acd7412b0114a7febd525e312468bc4f-display-v1.webp)

New releaseSep 10, 2026

# serverless [[email protected]](/cdn-cgi/l/email-protection)

CLI framework for deploying and managing serverless applications on AWS Lambda with YAML infrastructure, local development, and multi-language runtime support.

Share

[![Serverless Framework AWS Lambda AWS DynamoDB AWS API Gateway](https://assets.kitploit.com/production/public/readmes/50832/e9e62fbf0dba2c8da3b3b8718db14502371596d4097b58a99f2b13db488a5ad8/c57f1273c99a5fe138a8b9df063cfde629a89e5d52cba049ad1400ba04be8f88-display-v1.webp)](https://serverless.com)

[Website](https://serverless.com)
 •
[Documentation](https://serverless.com/framework/docs/)
 •
[X / Twitter](https://twitter.com/goserverless)
 •
[Community Slack](https://serverless.com/slack)
 •
[Forum](https://forum.serverless.com)

**The Serverless Framework** – Makes it easy to use AWS Lambda and other managed cloud services to build applications that auto-scale, cost nothing when idle, and result in radically low maintenance.

The Serverless Framework is a command-line tool with approachable YAML syntax to deploy both your code and cloud infrastructure needed to make tons of serverless application use-cases, like APIs, front-ends, data pipelines and scheduled tasks. It's a multi-language framework that supports Node.js, Typescript, Python, Go, Java, and more. It's also completely extensible via over 1,000 plugins which add more serverless use-cases and workflows to the Framework.

Actively maintained by [Serverless Inc](https://www.serverless.com).

# Serverless Framework - V.4

[![Serverless Framework V.4 Overview Video](https://assets.kitploit.com/production/public/readmes/50832/be27a32e339f60c5234e1f13e7a4aa223f55bc36fdde08668ca814105c2500d3/8a82b1816ed248c728a3552401d6a44372d984ca4c687cf862b0008150c8e2c4-display-v1.webp)](https://www.youtube.com/watch?v=UQL_PPJUFOU)

**July 2026** – V.4 continues to feature significant updates. Review them all below. Recent releases added Sandboxes (isolated, ephemeral compute on AWS Lambda), native Amazon Bedrock AgentCore support, Managed Instances, Durable Functions, and built-in AWS Login & SSO. As always, we are more excited about the serverless future than ever.

## New Features In V.4

Here's a list of everything that's new in V.4, so far:

* **Sandboxes** – Deploy isolated, ephemeral compute environments on AWS Lambda — ideal for untrusted or per-session workloads such as AI agents and code execution. [More info here](https://www.serverless.com/framework/docs/providers/aws/guide/sandboxes).
* **Amazon Bedrock AgentCore Support** – Define AI agents, memory, tools, gateways, browsers, and code interpreters directly in `serverless.yml` via the `ai` property, and manage them with the `serverless agent` commands. [More info here](https://www.serverless.com/framework/docs/providers/aws/guide/agents).
* **AWS Login & SSO** – Set up AWS credentials via browser-based flows with [`serverless login aws`](https://www.serverless.com/framework/docs/providers/aws/cli-reference/login-aws) and [`serverless login aws sso`](https://www.serverless.com/framework/docs/providers/aws/cli-reference/login-aws-sso).
* **Deployment Diffs** – Preview how a deployment will change your live AWS CloudFormation stack before deploying with [`serverless diff`](https://www.serverless.com/framework/docs/providers/aws/cli-reference/diff).
* **Reconcile Command** – Keep usage records in sync with your AWS accounts when stacks are removed outside the CLI, via [`serverless reconcile`](https://www.serverless.com/framework/docs/providers/aws/cli-reference/reconcile).
* **Managed instances** – Native support for EC2-backed Lambda execution to enable higher throughput, predictable capacity, and long-running workloads.
* **Durable functions** – Built-in support for durable, stateful workflows and long-running orchestrations.
* **Lambda tenant isolation mode:** Use tenant isolation mode to create distinct Lambda compute environments per tenant to help reduce noisy neighbor effects and isolate high-traffic customers more cleanly.
* **HTTP response streaming:** Stream logs, long-running reports, partial responses, or AI LLM responses from Lambda with API Gateway HTTP APIs.
* **Per-function IAM roles:** Add per-function IAM policies or switch the entire service to use per-function policies.
* **Built-in plugins**: Popular community plugins are now first-class, built-in features of the framework, including Python requirements, AppSync, Prune, API Gateway Service Proxy, and more.
* **Improved Custom Domain Support:** You no longer need an external plugin to automatically configure custom domains and SSL certificates for your APIs and more. It's now built into the [Serverless Framework CLI](https://www.serverless.com/framework/docs/providers/aws/guide/domains).
* **Integration with Doppler:** You can now easily fetch Secrets from Doppler via [Serverless Framework Variables](https://www.serverless.com/framework/docs/guides/variables/doppler).
* **Introducing [Serverless MCP](https://www.serverless.com/framework/docs/guides/mcp):** Built for Cursor, Windsurf, and other AI-powered IDEs, it auto-detects cloud resources from your code, fetching logs, state, and config from AWS, enabling you to debug serverless apps directly in your IDE — no AWS console visit needed! Supports Serverless Framework, Cloudformation, and more.
* **Support for AWS SAM, AWS CloudFormation, & Traditional Serverless Framework Projects:** Now, you can use one tool to deploy all three of these IaC project files. [More info here](https://www.serverless.com/framework/docs/guides/sam)
* **Native TypeScript Support:** You can now use `.ts` handlers in your AWS Lambda functions in `serverless.yml` and have them build automatically upon deploy. [ESBuild](https://esbuild.github.io/) is now included in the Framework which makes this possible. [More info here](https://www.serverless.com/framework/docs/providers/aws/guide/building).
* **The AWS AI Stack:** V.4 is optimized for [the AWS AI Stack](https://github.com/serverless/aws-ai-stack). Deploy a full-stack, serverless, boilerplate for AI applications on AWS, featuring LLMs via Amazon Bedrock and much more.
* **New Dev Mode:** Run `serverless dev` to have events from your live architecture routed to your local code, enabling you to make fast changes without deployment. [More info here](https://www.serverless.com/framework/docs/providers/aws/cli-reference/dev).
* **Latest Runtime Support:** Support for Node.js 24 (`nodejs24.x`), Python 3.14 (`python3.14`), and Java 25 (`java25`) on AWS Lambda.
* **Latest Region Support:** Support for all major regions, including the newly announced `ap-southeast-6` in New Zealand.
* **New Stages Property:** Easily organize stage-specific config via `stages` and set `default` config to fallback to.
* **Improved Compose Experience:** Serverless Compose now has a beautiful new CLI experience that better demonstrates what is being deployed.
* **New Terraform & Vault Integrations:** Pull state outputs from several Terraform state storage solutions, and secrets from Vault. [Terraform Docs](https://www.serverless.com/framework/docs/guides/variables/hashicorp/terraform) [Vault Docs](https://www.serverless.com/framework/docs/guides/variables/hashicorp/vault)
* **Support Command:** Send support requests to our team [directly from the CLI](https://www.serverless.com/framework/docs/providers/aws/cli-reference/support), which auto-include contextual info which you can review before sending.
* *...