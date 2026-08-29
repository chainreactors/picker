---
title: pyrite
url: https://kitploit.com/en/tools/gitlab/renich/pyrite
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:31:04.432889
---

# pyrite

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

pyrite — Hardware-bound & Cloud-gated binary execution, cryptographic provenance, and anti-tamper envelope sealing for Crystal. | Kitploit

[Tools](/en/tools)/![GitLab](/providers/gitlab.png)GitLab/renich/pyrite

![](https://assets.kitploit.com/production/public/tools/53411/4944554f95db928b7cd1d9feffc5c5e9865cb3bd73a6664fc0c94c6d7b073774-display-v1.webp)

[Cryptography](/en/categories/cryptography)[Cloud Security](/en/categories/cloud-security)[DevSecOps](/en/categories/devsecops)[Hardware Security](/en/categories/hardware-security)[Binary Analysis](/en/categories/binary-analysis)[Supply Chain Security](/en/categories/supply-chain-security)

![GitLab](/providers/gitlab.png)renich/pyrite

# pyrite

Hardware-bound & Cloud-gated binary execution, cryptographic provenance, and anti-tamper envelope sealing for Crystal.

[View Repository](https://gitlab.com/renich/pyrite)

351 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![pyrite.cr banner](https://gitlab.com/renich/pyrite/-/raw/master/assets/pyrite-banner.svg)

**Hardware-Bound & Cloud-Gated Binary Execution and Anti-Tamper Envelope Sealing for Crystal.**

[![Version 0.1.0](https://img.shields.io/badge/version-v0.1.0-blue.svg?style=flat-square)](https://gitlab.com/renich/pyrite/-/releases)
[![Crystal >= 1.21.0](https://img.shields.io/badge/crystal-%3E=%201.21.0-black.svg?style=flat-square&logo=crystal&logoColor=white)](https://crystal-lang.org/)
[![GitLab CI Passing](https://img.shields.io/badge/pipeline-passing-brightgreen.svg?style=flat-square&logo=gitlab)](https://gitlab.com/renich/pyrite/-/pipelines)
[![Specs Passing](https://img.shields.io/badge/specs-99%20passing-success.svg?style=flat-square&logo=crystal)](https://gitlab.com/renich/pyrite)
[![Ameba Clean](https://img.shields.io/badge/ameba-0%20violations-brightgreen.svg?style=flat-square)](https://github.com/crystal-ameba/ameba)
[![Flaw Clean](https://img.shields.io/badge/flaw-0%20findings-brightgreen.svg?style=flat-square)](https://github.com/kdairatchi/flaw)

[![Sphinx Documentation](https://img.shields.io/badge/docs-Sphinx%20Portal-orange.svg?style=flat-square&logo=sphinx&logoColor=white)](https://renich.gitlab.io/pyrite/)
[![Crystal API Documentation](https://img.shields.io/badge/api-Crystal%20Docs-8A2BE2.svg?style=flat-square&logo=crystal&logoColor=white)](https://renich.gitlab.io/pyrite/technical/api/)
[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg?style=flat-square)](LICENSE)
[![Donate using Liberapay](https://img.shields.io/liberapay/receives/Renich.svg?logo=liberapay&style=flat-square)](https://liberapay.com/Renich/donate)

---

## What is Pyrite?

**Pyrite** ensures that your compiled Crystal binary **only executes on your authorized infrastructure**. If an adversary extracts, leaks, steals, or modifies the binary, execution halts immediately before any application logic or secrets are exposed.

### Core Security Guarantees

1. **Hardware & Cloud Execution Binding**: The binary is *incomplete at rest*. Core operational configuration and keys are sealed inside an envelope that can only be decrypted by the physical motherboard's **TPM 2.0 chip** (`systemd-creds`) or **Google Cloud Run IAM / Cloud KMS**.
2. **Real-Time Self-Integrity (Anti-Tamper)**: At boot, Pyrite calculates the SHA-256 digest of `/proc/self/exe` and compares it against the authorized hash decrypted from the envelope. Any 1-byte alteration halts the process instantly.
3. **Anti-Reverse Engineering**: Stripped native LLVM machine code (`strip -s`) contains zero symbol tables, reflection metadata, or plaintext configuration. Decompilation yields only a dead decryption wrapper.
4. **Zero Runtime Overhead**: The cryptographic gate runs once during startup (~15–25ms) and adds **0.00% overhead** to ongoing request handling. Zero external shard dependencies.

---

## Quickstart

### 1. Add to `shard.yml`

root@kitploit:~

```
dependencies:
  pyrite:
    github: renich/pyrite
    version: ~> 0.1.0
```

### 2. Bootstrap in Application Code

root@kitploit:~

```
require "pyrite"
require "kemal"

# Define strongly-typed application configuration
struct AppConfig
  include JSON::Serializable

  getter database_url : String
  getter session_secret : String
  getter api_token : String
end

# 1-line verification & bootstrap:
config = Pyrite.bootstrap!(AppConfig)

puts "Pyrite verified binary integrity. Starting application..."

get "/" do
  "Secure service running on authorized hardware."
end

Kemal.run
```

### 3. Local Development Mode

During development or unit testing (`crystal spec`), you do not need active cloud credentials or a physical TPM. Simply create `.pyrite.dev.json` or set `PYRITE_DEV=1`:

root@kitploit:~

```
{
  "database_url": "postgresql://postgres:pass@localhost:5432/dev",
  "session_secret": "insecure-dev-secret-key",
  "api_token": "dev-token"
}
```

Pyrite will print a clear visual warning in the terminal and pass through your local configuration.

---

## Build & Sealing CLI (`bin/pyrite`)

When installed, Pyrite provides a compiled CLI tool to automate LLVM compilation, ELF symbol stripping, SHA-256 digest hashing, and envelope sealing.

root@kitploit:~

```
# Build & Seal for Google Cloud Run (KMS):
bin/pyrite build \
    --input=src/main.cr \
    --output=bin/app \
    --target=gcp \
    --kms-key="projects/my-p/locations/global/keyRings/my-r/cryptoKeys/app-key" \
    --config=config/production.json

# Build & Seal for Bare-Metal Fedora (TPM 2.0 / systemd-creds):
bin/pyrite build \
    --input=src/main.cr \
    --output=bin/app \
    --target=baremetal \
    --pcr=0,7 \
    --config=config/production.json
```

---

## Supported Trust Anchors

---

## Documentation

Exhaustive technical documentation, specifications, and architecture decision records are maintained in reStructuredText under [`docs/`](https://gitlab.com/renich/pyrite/-/blob/master/docs/index.rst):

---

## Contributing & Code of Honor

All contributions must adhere to the [Universal Code of Honor](https://gitlab.com/renich/pyrite/-/blob/master/CODE_OF_HONOR.rst) and [Contributing Guidelines](https://gitlab.com/renich/pyrite/-/blob/master/CONTRIBUTING.rst).

---

## License

* **Software**: GNU General Public License v3.0 or later ([LICENSE](https://gitlab.com/renich/pyrite/-/blob/master/LICENSE)).
* **Documentation**: GNU Free Documentation License v1.3 or later ([LICENSE-DOCS](https://gitlab.com/renich/pyrite/-/blob/master/LICENSE-DOCS)).

Copyleft © 2026 Rénich Bon Ćirić <[[email protected]](/cdn-cgi/l/email-protection#176572797e747f577261767b7e79626f3974787a)>.

---

## Support & Donations

If you find Pyrite useful and wish to support its ongoing development, please consider donating:

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/Renich/donate)

[Download Tool](https://gitlab.com/renich/pyrite)

| Environment | Provider | Root of Trust | Protection |
| --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
| **Google Cloud ...