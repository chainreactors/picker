---
title: Jwt-Hack: Reborn in Rust
url: https://www.hahwul.com/blog/2025/jwt-hack-v2/
source: HAHWUL
date: 2025-06-07
fetch_date: 2025-10-06T22:54:13.895396
---

# Jwt-Hack: Reborn in Rust

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/blog/2025/jwt-hack-v2/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/blog/2025/jwt-hack-v2/)

[한국어](https://www.hahwul.com/ko/blog/2025/jwt-hack-v2/)

JUNE 06, 2025

# Jwt-Hack: Reborn in Rust

jwt-hack v2 is a complete Rust rewrite, boosting performance, safety, and stability.

Back in October 2020, I created a tool called [jwt-hack](https://github.com/hahwul/jwt-hack) to make security testing for JSON Web Tokens (JWTs) a bit more convenient. At the time, this Go-based tool was a project born out of my own necessity, focusing on its core `crack` feature to find JWT signing secrets using wordlists or brute force.

Truth be told, for the nearly five years since, the project has been somewhat neglected compared to my other work. While I made small improvements here and there, a part of me always felt it deserved more. That's why I finally decided to take the plunge and give the project a complete reboot, leading to the release of a new major version: jwt-hack v2.

![](/projects/jwt-hack/jwt-hack.jpg)

In this post, I'd like to briefly share what the key changes in jwt-hack v2 are and where the project is headed next.

## From Go to Rust: The Core Change

The biggest change in v2 is the complete switch from Go to Rust. Rewriting all the existing Go code in Rust took a fair amount of effort, but I believe it was a worthwhile endeavor.

The primary reason was stability. Frankly, v1 would occasionally run into unexpected memory-related issues. Thanks to Rust's Ownership system and its strict compile-time checks, I was able to prevent these kinds of bugs at the source, resulting in a much more stable tool.

Of course, a performance boost came along as a bonus. Even a simple benchmark shows a pretty satisfying speed improvement.

| Metric | jwt-hack `v1` | jwt-hack `v2` |
| --- | --- | --- |
| **Time (mean ± σ)** | 1.874 s ± 0.033 s | 678.6 ms ± 165.8 ms |
| **Range (min … max)** | 1.834 s … 1.935 s | 623.5 ms … 1150.4 ms |
| **User Time** | 7.312 s | 3516.7 ms |
| **System Time** | 1.985 s | 491.1 ms |
| **Runs** | 10 | 10 |

*Performance comparison of the `crack` feature under identical conditions (`$ jwt-hack crack eyJ0e... --mode brute --max 4`)*

## Strengthening the Foundation

This wasn't just about changing the language; I also focused on strengthening the project's foundation.

### Test Coverage

One of the areas I paid the most attention to during v2's development was the test code. I wrote far more thorough tests compared to the previous version, creating a solid base to minimize side effects from future code changes and maintain stability as new features are added.

![Codecov result](https://github.com/user-attachments/assets/b7178cc9-37d4-40a3-b83c-29b88a833f2f)

### Compatibility

Even though it's a major version release, all the command-line options and usage patterns from v1 are fully inherited. This means you can update and apply it to your existing scripts or pipelines without any migration work.

## Expanded Features

Building on the stability and development convenience gained from the switch to Rust, I've added several features that I'd long felt were necessary.

### Support for More Algorithms

While it previously focused on HMAC-based algorithms (HS256, HS384, HS512), jwt-hack now supports asymmetric encryption algorithms like RSA (RS\*) and ECDSA (ES\*).

### New Key-Based Functionality

Going beyond simple secret-based testing, it's now possible to generate, verify, and test tokens using private/public keys. For example, you can easily create a JWT signed with a private key like this:

```
ssh-keygen -t rsa -b 4096 -E SHA256 -m PEM -P "" -f RS256.key
jwt-hack encode '{"a":"z"}' --private-key RS256.key --algorithm=RS256
```

![Make JWT with Private key](https://github.com/user-attachments/assets/21a2c1b4-f4da-4f7b-abfa-89a0c90c5ad9)

### New Verify Mode

Truth be told, the previous version lacked even the basic functionality to verify if a JWT's signature was valid. This update introduces a `verify` mode that allows you to check a token's signature with a secret or a public key, making the tool more complete for token testing.

### Broader Attack Vector Support

One of jwt-hack's core features is generating tokens for known attack vectors. In addition to the existing `none` algorithm and `jku/x5u` attacks, it now supports a wider range of vectors and will continue to expand in the future:

* Algorithm Confusion (tampering with the `alg` header to HS256)
* SQL Injection in `kid` (inserting an SQLi payload into the `kid` header)
* Other known attack techniques

## Installation

### Cargo

If you're a Rust developer, you can install it directly via `cargo`.

```
cargo install jwt-hack
```

### Homebrew

And for one of the most exciting pieces of news: jwt-hack is now included in the official `homebrew-core`! You can install and update it with a simple command, no need to tap a separate repository.

```
brew install jwt-hack
```

### More

You can also get jwt-hack through various other channels, including the [Snapcraft Package](https://snapcraft.io/jwt-hack), [Docker Hub](https://hub.docker.com/repository/docker/hahwul/jwt-hack/general), and [GHCR](https://github.com/hahwul/jwt-hack/pkgs/container/jwt-hack).

## Final Thoughts

Breathing new life into a long-neglected project was more enjoyable than I expected. It was great to see the tool improve, but what made it particularly fun was the process of getting to know the Rust language more deeply.

Going forward, I plan to build jwt-hack into a comprehensive tool packed with various features for JWT security testing. If you have any ideas for necessary features or improvements, please don't hesitate to leave a comment on the [GitHub Issues](https://github.com/hahwul/jwt-hack/issues). Your interest is the driving force behind this project.

[#sec](https://www.hahwul.com/tags/sec/)
[#jwt-hack](https://www.hahwul.com/tags/jwt-hack/)
[#rust](https://www.hahwul.com/tags/rust/)

[ ]

[ ]

### Table of Contents

[From Go to Rust: The Core Change](https://www.hahwul.com/blog/2025/jwt-hack-v2/#from-go-to-rust-the-core-change)

[Strengthening the Foundation](https://www.hahwul.com/blog/2025/jwt-hack-v2/#strengthening-the-foundation)

[Test Coverage](https://www.hahwul.com/blog/2025/jwt-hack-v2/#test-coverage)
[Compatibility](https://www.hahwul.com/blog/2025/jwt-hack-v2/#compatibility)

[Expanded Features](https://www.hahwul.com/blog/2025/jwt-hack-v2/#expanded-features)

[Support for More Algorithms](https://www.hahwul.com/blog/2025/jwt-hack-v2/#support-for-more-algorithms)
[New Key-Based Functionality](https://www.hahwul.com/blog/2025/jwt-hack-v2/#new-key-based-functionality)
[New Verify Mode](https://www.hahwul.com/blog/2025/jwt-hack-v2/#new-verify-mode)
[Broader Attack Vector Support](https://www.hahwul.com/blog/2025/jwt-hack-v2/#broader-attack-vector-support)

[Installation](https://www.hahwul.com/blog/2025/jwt-hack-v2/#installation)

[Cargo](https://www.hahwul.com/blog/2025/jwt-hack-v2/#cargo)
[Homebrew](https://www.hahwul.com/blog/2025/jwt-hack-v2/#homebrew)
[More](https://www.hahwul.com/blog/2025/jwt-hack-v2/#more)

[Final Thoughts](https://www.hahwul.com/blog/2025/jwt-hack-v2/#final-thoughts)

[Previous

The Art of Agentic Coding](https://www.hahwul.com/blog/2025/agentic-coding/)

[Next

Jekyll to Zola](https://www.hahwul.com/blog/2025/jekyll-to-zola/)

[Contact](/contact)
[Thanks](/thanks)
[Sitemap](/sitemap.xml)
Random
[Feeds](/feeds)

© 2025 HAHWUL
Developed and Designed by Me

* [WHO](/about/)
* [BLOG](/blog/)
* [SEC](/sec/)
* [DEV](/dev/)
* [PROJECTS](/projects/)

---

* Language
  + [ENGLISH](https://www.hahwul.com/blog/2025/jwt-hack-v2/)
  + [한국어](https://www.hahwul.com/ko/blog/2025/jwt-hack-v2/)