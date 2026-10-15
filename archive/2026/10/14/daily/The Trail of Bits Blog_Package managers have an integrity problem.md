---
title: Package managers have an integrity problem
url: https://blog.trailofbits.com/2026/10/14/package-managers-have-an-integrity-problem/
source: The Trail of Bits Blog
date: 2026-10-14
fetch_date: 2026-10-15T06:43:59.247620
---

# Package managers have an integrity problem

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Package managers have an integrity problem

[Keegan Ryan](/authors/keegan-ryan/)

October 14, 2026

[supply-chain](/categories/supply-chain/), [cryptography](/categories/cryptography/), [ecosystem-security](/categories/ecosystem-security/)

Page content

* [Simulating malicious package repositories](#simulating-malicious-package-repositories)
  + [HTTPS is (almost) everywhere](#https-is-almost-everywhere)
* [Hash functions don’t always provide integrity](#hash-functions-dont-always-provide-integrity)
  + [Hashes in lockfiles](#hashes-in-lockfiles)
  + [Hashes present, but not for integrity](#hashes-present-but-not-for-integrity)
  + [Lockfiles have many roles besides supply-chain integrity](#lockfiles-have-many-roles-besides-supply-chain-integrity)
* [Signatures are common; verification is not](#signatures-are-common-verification-is-not)
  + [Repository signing](#repository-signing)
  + [Developer signing](#developer-signing)
  + [Identity-based signing](#identity-based-signing)
  + [Verification code is skipped, unconfigured, or nonexistent](#verification-code-is-skipped-unconfigured-or-nonexistent)
* [Go package management and transparency logs](#go-package-management-and-transparency-logs)
* [A proposed cryptographic design for package managers](#a-proposed-cryptographic-design-for-package-managers)
* [Acknowledgments](#acknowledgments)

I tested 25 of the most popular package managers to check whether they detect a compromised package repository injecting malicious code into legitimate packages. This code integrity problem could be solved using cryptographic hashes or signatures, but many package managers are still vulnerable to this threat. Of the 25 package managers reviewed[1](#fn:1), fewer than half used lockfiles that checked for tampering by default, and only two verified the integrity of every package they downloaded.

Supply-chain attacks caused by developer compromise are a common story, but imagine what happens if ongoing mitigation attempts, including work by Trail of Bits[2](#fn:2), are successful. If developers of popular packages are no longer the easiest targets, attackers will shift their focus to the next weakest link in the system: the package repositories that serve the code. The cryptographic answers to this problem are more subtle than they appear, and many implementations fall short due to deliberate design choices, resource prioritization, or the complexity of developer-friendly solutions.

One natural answer is to include a cryptographic hash of a package’s contents in a lockfile and compare hashes after downloading the package. This automatic verification was the default behavior in about half of the package managers I tested, but others required extra configuration to include or verify these hashes, used hashes in a cryptographically insecure way, or lacked hashes entirely. This is summarized in the following table.

|  |  |
| --- | --- |
| **Verifies integrity** | Go, vcpkg |
| **Verifies if lockfile is present** | Bun, Bundler, Cargo, npm, pnpm, Poetry, SwiftPM, uv, Yarn |
| **Verifies with lockfile + extra steps** | Conda, Gradle, Pip, NuGet, Pub |
| **Does not verify with lockfile or N/A** | CocoaPods, Composer, Conan, cpanminus, Gem, Maven, PowerShellGet, PSResourceGet, R |

*Table 1: Lockfile-based security of a package manager fetching dependencies from a malicious repository, categorized by how much work it takes a developer to achieve integrity. Experimentally verified for a particular configuration. Caveats detailed below.*

Another natural approach is to use signatures, avoiding the need to securely distribute a hash for every package. However, in my tests, only Go verified signatures by default; others required extra configuration, lacked verification code, or did not support signatures.

|  |  |
| --- | --- |
| **Verifies signatures** | Go |
| **Verifies with configuration** | Bundler, Gem, Gradle, Maven, npm, NuGet |
| **Missing or incomplete verification** | Bun, cpanminus, Pip, pnpm, Poetry, PowerShellGet, PSResourceGet, uv, Yarn |
| **No signatures available for verification** | Cargo, CocoaPods, Composer, Conan, Conda, Pub, R, SwiftPM, vcpkg |

*Table 2: Signature-based security of various package managers. Also experimentally verified and subject to similar caveats.*

As both tables show, I found a surprising variation in the cryptographic designs and the level of protection they provide. Despite the challenges, I also found several communities on the frontier of this integrity problem that are bringing improved designs to reality. This post explores those variations, showing where certain designs fall short, why code integrity is harder to solve than it appears, and what cryptographic designs might be adopted in the future.

## Simulating malicious package repositories

Studying the cryptographic behavior of 25 package managers is quite the challenge. I wanted to minimize manual analysis, but also be 100% confident when I claim an attack from a malicious package repository is possible. To solve this problem, I built a testing harness based on Docker containers and [mitmproxy](https://www.mitmproxy.org/) that dynamically evaluates the security of package managers against a malicious server.

![“Figure showing experimental design of the test harness used to simulate malicious package repositories”](/2026/10/14/package-managers-have-an-integrity-problem/package-manager-integrity-banner-figure-1_hu_c095267cc912b4da.webp)

Figure 1: Experimental design of the test harness used to simulate malicious package repositories

The Ubuntu-based Docker images include a package manager, sample code, and optionally a lockfile. There are [conflicting opinions](https://arxiv.org/abs/2505.04834v3) about whether to include lockfiles in source code repositories, so I tested both configurations. The harness instructs the package manager to fetch dependencies from the repository, and the resulting network request [routes](https://docs.mitmproxy.org/stable/concepts/modes/#wireguard) through a WireGuard network to a custom mitmproxy addon.

Because the mitmproxy TLS CA is installed in the Docker image, the addon can fully manipulate the plaintext from the package repository, simulating a compromised server. I assumed any web-facing server could be compromised (e.g., Composer fetches metadata from Packagist and packages from GitHub), but backend resources, like any private signing keys, remain secure. The simulated repository embeds malicious code into the downloaded packages, and if the sample code executes the malware, the attack is successful.

I tried to keep the experimental setup reflective of real-world usage, but there are limitations. I installed the latest package manager versions, followed quickstart guides for setting up sample projects inside the container, and picked popular packages from public repositories to infect. I ran package manager commands with default flags to see if extra steps, like modifying the project manifest or running extra commands, were needed to enforce cryptographic integrity. However, I am limited to testing a single package with a single package manager version on a single platform, and the test conditions (e.g., PowerShell and CocoaPods on Ubuntu) may not represent the most common usage patterns. The setup isn’t meant to show that every developer is vulnerable to a malicious package repository, just that a developer following reasonable conventions is.

With the package managers installed and network intercept functional, one (mostly) promising observation is clear.

### HTTPS is (almost) everywhere

Our harness architecture captures all network traffic, so it’s easy to test that package managers are using TLS and validating the certificates. In almost every package manager, they are.

The exception is cpanminus, the [frequently](https://www.cpan...