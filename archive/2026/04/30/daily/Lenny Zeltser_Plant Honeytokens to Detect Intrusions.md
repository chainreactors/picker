---
title: Plant Honeytokens to Detect Intrusions
url: https://zeltser.com/plant-honeytokens
source: Lenny Zeltser
date: 2026-04-30
fetch_date: 2026-05-01T05:39:56.271976
---

# Plant Honeytokens to Detect Intrusions

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# Plant Honeytokens to Detect Intrusions

Plant decoy credentials, configs, and URLs to surface an attack the rest of your stack might miss. Deployment scenarios include MCP server entries, AWS API keys, and Cloudflare Workers serving fake admin pages.

![Plant Honeytokens to Detect Intrusions - illustration](/assets/plant-honeytokens.CNZJoYK1_Z263Ex.webp)

A honeytoken is a piece of data whose sole purpose is to alert you when it is accessed. Classic forms include a user account, file, and link that no one is supposed to use, open, or click. Plant honeytokens among the secrets, configs, and credentials that attackers pursue after infecting the system. You’ll learn about an intrusion the moment someone reaches for what they shouldn’t.

## Canarytokens give you tripwires without infrastructure to maintain.

[Canarytokens](https://canarytokens.org) are an open-source family of honeytokens from [Thinkst](https://thinkst.com). Thinkst hosts a free Canarytokens service that can generate honeytokens and contact you when one fires. There’s nothing to deploy and no account required. If you prefer to keep token data on your own infrastructure, [you can self-host](https://github.com/thinkst/canarytokens-docker).

Canarytokens supports dozens of token types. Examples include a URL that an adversary would fetch, a hostname they would resolve, and an AWS key they would try to use. Honeytoken files come as Word, PDF, MySQL dump, or kubeconfig formats. The [token guide](https://docs.canarytokens.org/guide/) lists them all.

The workflow is the same for every token. You visit the Canarytokens site, pick a token type, and supply the email address or webhook that should receive alerts. Deploy the resulting artifact, a file, URL, key, or DNS name, wherever you want the trap. When something interacts with the artifact, you get a notification with details (depending on token type), such as the source IP, user agent, timestamp, and geolocation.

## Plant tokens where attackers will look for what’s valuable.

A token works best where attackers expect to find value, but legitimate users rarely look.

**Decoy MCP server entry in your AI agent’s config.** Point an MCP server entry at a [honeytoken URL](https://docs.canarytokens.org/guide/http-token.html), then configure your agent not to auto-connect. In Claude Code, add it to .mcp.json and list the server name under `disabledMcpjsonServers` in settings.json so your own agent doesn’t access the URL. An attacker reading your configuration might connect to the MCP server and trip the wire. (I’ll show how to build a deeper MCP server decoy in an upcoming article.)

**AWS API Keys in your secrets directory.** Create an AWS API Keys Canarytoken. Drop the resulting access key and secret into a backup file such as ~/.aws/credentials.legacy, or into a fake `[backup]` profile inside your real ~/.aws/credentials file. If an attacker exfiltrates these secrets and uses the key against AWS, you get an alert. The [AWS API Keys doc](https://docs.canarytokens.org/guide/aws-keys-token) explains how to set this up.

**Honeytoken files in your project root.** Drop a Word, PDF, or MySQL dump honeytoken into your documents folder or repo as something an attacker would target. Names such as budget-final.docx or production-credentials.sql should work well. The token fires if they open the document or import the dump.

**DNS token in a fake config string.** Embed the unique hostname from a DNS honeytoken in a config file as a fake database hostname, internal API URL, or webhook target. If the attacker’s tool parses the config and tries to reach the hostname, the token fires. The [DNS token doc](https://docs.canarytokens.org/guide/dns-token) covers an extra trick where you can encode incident-specific data into the resolved name.

**Honeytoken URL in your repo’s docs and instructions.** Plant a honeytoken URL in your README, internal wiki, or AI-agent instruction files as a fake “internal docs” or “admin dashboard” reference. Anyone or anything that follows the link fires the alert. These URLs are the noisiest because people click on links, and CI runners and doc indexers fetch any URL they hit.

Disguise the bait if your threat model includes a sophisticated attacker. Thinkst-hosted Canarytokens have [known fingerprints that researchers have cataloged](https://trufflesecurity.com/blog/canaries), so for high-stakes deployments, consider self-hosting. Otherwise, surround the artifact with realistic content and plausible neighbors so the bait doesn’t stand out.

## Detect AWS intrusions with the same approach.

Beyond your local secrets directory, the AWS API Keys Canarytoken belongs in the S3 buckets, Lambda functions, and infrastructure-as-code files where teams keep credentials:

* A fake terraform.tfvars.bak in repos that contain real Terraform
* A fake AWS access key listed as “admin” diagnostic credentials in an S3 bucket README
* An unused env var on a Lambda function that holds the fake key

AWS Canarytoken alerts pass through Thinkst’s AWS CloudTrail logs before they reach you, which [can introduce a 2 to 30 minute delay](https://docs.canarytokens.org/guide/aws-keys-token.html) between the attacker’s action and the notification.

## Deploy a Cloudflare Worker to host your bait.

Another way to trigger a honeytoken is to plant it on an internet-accessible system that an attacker might probe. Cloudflare Workers, [available in the free pricing tier](https://developers.cloudflare.com/workers/platform/pricing), are a convenient way to do this without setting up and managing a full web server.

As a minimal example, the Worker below serves a fake admin login form. When someone submits the form, the Worker fetches a honeytoken URL, which fires the alert. Scaffold the project with the [`npm create cloudflare@latest`](https://developers.cloudflare.com/workers/get-started/guide/) command, then replace the generated src/index.js with the code below. Or ask your AI coding assistant to handle this for you.

```
export default {
  async fetch(request, env, ctx) {
    if (request.method === "POST") {
      const ip = request.headers.get("cf-connecting-ip") || "unknown";
      const ua = request.headers.get("user-agent") || "unknown";
      const url = `<full-token-url-from-canarytokens.org>?ip=${encodeURIComponent(ip)}&ua=${encodeURIComponent(ua)}`;
      ctx.waitUntil(fetch(url));
      return new Response("Invalid credentials", { status: 401 });
 }
    return new Response(`<!doctype html>
<html><body>
 <h1>Internal Admin</h1>
 <form method="post" action="/login">
 <input name="username" placeholder="username" />
 <input name="password" type="password" placeholder="password" />
 <button>Sign in</button>
 </form>
</body></html>`, {
      headers: { "content-type": "text/html" },
 });
 },
};
```

Deploy with the [`npx wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/) command. If your Cloudflare login covers multiple accounts, set `account_id` in wrangler.jsonc or export `CLOUDFLARE_ACCOUNT_ID` first, otherwise the deploy stalls in non-interactive mode.

The Worker gets a free URL under the workers.dev domain. If your domain is on Cloudflare DNS, you can also bind the Worker to a subdomain such as *admin.example.com*. Custom subdomains land in Certificate Transparency logs, which attackers monitor for fresh recon targets.

The Canarytoken alert’s source IP address will show Cloudflare’s edge, and the user agent field will show whatever default your fetch sends. Look at the URL parameters for the attacker’s real IP and user agent.

> The example above relies on Thinkst’s alerting layer to handle attacker-controlled headers securely. For real deployments, sanitize these inputs before forwarding them downstream. If the Worker source might land in a public repo, store the honeytoken URL as a Wrangler secret; use `npx wrangler ...