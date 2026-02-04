---
title: Auditing Outline. Firsthand lessons from comparing manual testing and AI security platforms
url: https://blog.doyensec.com/2026/02/03/outline-audit-q32025.html
source: Over Security - Cybersecurity news aggregator
date: 2026-02-03
fetch_date: 2026-02-04T04:07:55.053336
---

# Auditing Outline. Firsthand lessons from comparing manual testing and AI security platforms

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2026
* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Auditing Outline. Firsthand lessons from comparing manual testing and AI security platforms

03 Feb 2026 - Posted by Luca Carettoni

In July 2025, we performed a brief audit of [Outline](https://www.getoutline.com/) - an OSS wiki similar in many ways to Notion. This activity was meant to evaluate the overall posture of the application, and involved two researchers for a total of 60 person-days. In parallel, we thought it would be a valuable firsthand experience to use three AI security platforms to perform an audit on the very same codebase. Given that all issues are now fixed, we believe it would be interesting to provide an overview of our effort and a few interesting findings and considerations.

![Generate an image that well describe the content of this blog post](../../../public/images/humanvsaiaudits.png)

### Disclaimer: Outline

While this activity was not sufficient to evaluate the entirety of the Outline codebase, we believe we have a good understanding of its quality and resilience. **The security posture of the APIs was found to be above industry best practices. Despite our findings, we were pleased to witness a well-thought-out use of security practices and hardening**, especially given the numerous functionalities and integrations available.

It is important to note that Doyensec audited only Outline OSS ([v0.85.1](https://github.com/outline/outline/releases/tag/v0.85.1)). On-premise enterprise and cloud functionalities were considered out of scope for this engagement. For instance, multi-tenancy is not supported in the OSS on-prem release, hence authorization testing did not
consider cross-tenant privilege escalations. Finally, testing focused on Outline code only, leaving all dependencies out of scope. Ironically, several of the bugs discovered were actually caused by external libraries.

### Disclaimer: AI platforms evaluated during this dry run

Large Language Models and AI security platforms are evolving at an exceptionally rapid pace. The observations, assessments, and experiences shared in this post reflect our hands-on exposure at a specific point in time and within a particular technical context. As models, tooling, and defensive capabilities continue to mature, some details discussed here may change or become irrelevant.

### Instrumentation

When performing an in-depth engagement, it is ideal to set up a testing environment with debugging capabilities for both frontend and backend. Outlineâs extensive documentation makes this process easy.

We started by setting up a local environment as documented in [this guide](https://docs.getoutline.com/s/hosting/doc/local-development-5hEhFRXow7), and executing the following commands:

```
echo "127.0.0.1 local.outline.dev" | sudo tee -a /etc/hosts
mkdir files
```

The following `.env` file was used for the configuration(non-empty settings only):

```
NODE_ENV=development
URL=https://local.outline.dev:3000
PORT=3000
SECRET_KEY=09732bbde65d4...989
UTILS_SECRET=af7b3d5a6cc...2f1
DEFAULT_LANGUAGE=en_US
DATABASE_URL=postgres://user:pass@127.0.0.1:5432/outline
REDIS_URL=redis://127.0.0.1:6379
FILE_STORAGE=local
FILE_STORAGE_LOCAL_ROOT_DIR=./files/
FILE_STORAGE_UPLOAD_MAX_SIZE=262144000
FORCE_HTTPS=true
OIDC_CLIENT_ID=web
OIDC_CLIENT_SECRET=secret
OIDC_AUTH_URI=http://127.0.0.1:9998/auth
OIDC_TOKEN_URI=http://127.0.0.1:9998/oauth/token
OIDC_USERINFO_URI=http://127.0.0.1:9998/userinfo
OIDC_DISABLE_REDIRECT=true
OIDC_USERNAME_CLAIM=preferred_username
OIDC_DISPLAY_NAME=OpenID Connect
OIDC_SCOPES=openid profile email
RATE_LIMITER_ENABLED=true
# âââââââââââââ  DEBUGGING  ââââââââââââ
ENABLE_UPDATES=false
DEBUG=http
LOG_LEVEL=debug
```

Zitadelâs [OIDC server](https://github.com/zitadel/oidc) was used for authentication

```
REDIRECT_URI=https://local.outline.dev:3000/auth/oidc.callback USERS_FILE=./users.json go run github.com/zitadel/oidc/v3/example/server
```

Finally, VS Code debugging was set up using the following `.vscode/launch.json`

```
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "attach",
      "name": "Attach to Outline Backend",
      "address": "localhost",
      "port": 9229,
      "restart": true,
      "protocol": "inspector",
      "skipFiles": ["<node_internals>/**"],
      "cwd": "${workspaceFolder}"
    }
  ]
}
```

We also facilitated front-end debugging by adding the following setting at the top of the `.babelrc` file in order to have source maps.

```
"sourceMaps": true
```

### Findings

Doyensec researchers discovered and reported **seven (7) unique vulnerabilities** affecting Outline OSS.

| ID | Title | Class | Severity | Discoverer |
| --- | --- | --- | --- | --- |
| OUT-Q325-01 | Multiple Blind SSRF | SSRF | Medium | ð¤ðââï¸ |
| OUT-Q325-02 | Vite Path Traversal | Injection Flaws | Low | ðââï¸ |
| OUT-Q325-03 | CSRF via Sibling Domains | CSRF | Medium | ðââï¸ |
| OUT-Q325-04 | Local File Storage CSP Bypass | Insecure Design | Low | ðââï¸ |
| OUT-Q325-05 | Insecure Comparison in VerificationCode | Insufficient Cryptography | Low | ð¤ðââï¸ |
| OUT-Q325-06 | ContentType Bypass | Insecure Design | Medium | ðââï¸ |
| OUT-Q325-07 | Event Access | IDOR | Low | ð¤ |

Among the bugs we discovered, there are a few that require special mention:

**OUT-Q325-01** ([GHSA-jfhx-7phw-9gq3](https://github.com/outline/outline/security/advisories/GHSA-jfhx-7phw-9gq3)) is a standard Server-Side Request Forgery bug allowing redirects, but having limited protocols support. Interestingly, this issue affects the self-hosted version only as the cloud release is protected using [request-filtering-agent](https://www.npmjs.com/package/request-filtering-agent). While giving a quick look at this dependency, we realized that versions 1.x.x and earlier contained a vulnerability ([GHSA-pw25-c82r-75mm](https://github.com/azu/request-filtering-agent/security/advisories/GHSA-pw25-c82r-75mm)) where HTTPS requests to 127.0.0.1 bypass IP address filtering, while HTTP requests are correctly blocked. While newer versions of the library were already out, Outline was still using an old release, since no GitHub (or other) advisories were ever created for this issue. Whether intentionally or accidentally, this issue was silently fixed for many years.

**OUT-Q325-02** ([GHSA-pp7p-q8fx-2968](https://github.com/sapphi-red/vite-plugin-static-copy/security/advisories/GHSA-pp7p-q8fx-2968)) turned out to be a bug in the `vite-plugin-static-copy` npm module. Luckily, it only affects Outline in `development` mode.

**OUT-Q325-04** ([GHSA-gcj7-c9jv-fhgf](https://github.com/outline/outline/security/advisories/GHSA-gcj7-c9jv-fhgf)) was already exploited in this [type confusion attack](https://blog.calif.io/p/type-confusion-attacks-in-prosemirror). In fact, browsers like Chrome and Firefox do not block script execution even if the script is served with `Content-Disposition: attachment` as long as the content type is a valid `application/javascript`. Please note that this issue does not affect the cloud-hosted version given itâs not using the local file storage engine altogether.

Investigating this issue led to the discovery of **OUT-Q325-06**, an even more interesting issue.

Outline allows inline content for specific (safe) types of files as defined in `server/storage/files/BaseStorage.ts`

```
  /**
   * Returns the c...