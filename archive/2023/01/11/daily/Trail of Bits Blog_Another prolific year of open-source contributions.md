---
title: Another prolific year of open-source contributions
url: https://blog.trailofbits.com/2023/01/10/open-source-contributions-2022/
source: Trail of Bits Blog
date: 2023-01-11
fetch_date: 2025-10-04T03:31:26.540586
---

# Another prolific year of open-source contributions

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Another prolific year of open-source contributions

Samuel Moelius

January 10, 2023

[year-in-review](/categories/year-in-review/)

[This time last year](https://blog.trailofbits.com/2021/12/31/celebrating-our-2021-open-source-contributions/), we wrote about the more than 190 Trail of Bits-authored pull requests that were merged into non-Trail of Bits repositories in 2021. In 2022, we continued that trend by having more than 400 pull requests merged into non-Trail of Bits repositories!

Why is this significant? While we take great pride in the [tools that we develop](https://github.com/orgs/trailofbits/repositories), we recognize that we benefit from tools maintained outside of Trail of Bits. When one of those tools doesn’t work as we expect, we try to fix it. When a tool doesn’t fill the need we think it was meant to, we try to improve it. In short, we try to give back to the community that gives so much to us.

Here are a few highlights from the list of PRs at the end of this blog post:

* [Clippy](https://github.com/rust-lang/rust-clippy) is a collection of [over 550 lints](https://rust-lang.github.io/rust-clippy/master/index.html) to catch common mistakes and improve Rust code. We added the [crate\_in\_macro\_def](https://github.com/rust-lang/rust-clippy/pull/8576) and [unnecessary\_find\_map](https://github.com/rust-lang/rust-clippy/pull/8489) lints, and contributed improvements and bugfixes to lints such as [empty\_line\_after\_outer\_attribute](https://github.com/rust-lang/rust-clippy/pull/8892), [expect\_used/unwrap\_used](https://github.com/rust-lang/rust-clippy/pull/8802), [extra\_unused\_lifetimes](https://github.com/rust-lang/rust-clippy/pull/8737), [needless\_borrow](https://github.com/rust-lang/rust-clippy/pull/9136), [needless\_lifetimes](https://github.com/rust-lang/rust-clippy/pull/9743), [unnecessary\_to\_owned](https://github.com/rust-lang/rust-clippy/pull/10027), and [unnecessary\_filter\_map](https://github.com/rust-lang/rust-clippy/pull/8479).
* [HEVM](https://github.com/ethereum/hevm) is an implementation of the Ethereum virtual machine with symbolic execution capabilities. Our contributions to HEVM included [simplifying its use of the SMT solver](https://github.com/ethereum/hevm/pull/43), [improving its performance](https://github.com/ethereum/hevm/pull/73), [fixing a memory leak](https://github.com/ethereum/hevm/pull/45), and [adding tests](https://github.com/ethereum/hevm/pull/56).
* [Envoy](https://github.com/envoyproxy/envoy/) is a high-performance open source edge and service proxy that makes the network transparent to applications. We implemented the initial version of the Unified Header Validation (UHV) component within Envoy for [validating all request](https://github.com/envoyproxy/envoy/pull/19786) and response headers for [HTTP/1 and HTTP/2](https://github.com/envoyproxy/envoy/pull/22537). We took the existing header validation logic, consolidated it into the UHV component, performed an assessment to determine where the logic was not fully RFC compliant, and then fixed or implemented any gaps to ensure that the default configuration strictly adheres to the RFC standards. The new component provides [a single entry point](https://github.com/envoyproxy/envoy/pull/22078) for all HTTP request and response validation that makes it a much easier code base to maintain, audit, extend, customize, and fix any newly discovered attack vectors.
* [pyca/cryptography](https://github.com/pyca/cryptography) is a package that provides cryptographic recipes and primitives to Python developers. We improved its support for [Certificate Transparency](https://github.com/pyca/cryptography/pull/7207) and made numerous [usability improvements](https://github.com/pyca/cryptography/pull/7878).
* [Vcpkg](https://github.com/microsoft/vcpkg) is a C/C++ package manager for Windows, Linux, and MacOS. We fixed a bug in [Vcpkg itself](https://github.com/microsoft/vcpkg/pull/26240) and made improvements to packages such as [flatbuffers](https://github.com/microsoft/vcpkg/pull/24208), [grpc](https://github.com/microsoft/vcpkg/pull/26199), [gtest](https://github.com/microsoft/vcpkg/pull/23780), [ixwebsocket](https://github.com/microsoft/vcpkg/pull/23548). [libcpplocate](https://github.com/microsoft/vcpkg/pull/23173), [llvm](https://github.com/microsoft/vcpkg/pull/23399), [mbedtls](https://github.com/microsoft/vcpkg/pull/23787), [tcb-span](https://github.com/microsoft/vcpkg/pull/23393), and [z3](https://github.com/microsoft/vcpkg/pull/26429).
* [Warehouse](https://github.com/pypi/warehouse) is the software that powers [PyPI](https://pypi.org/), the official package index for the Python programming language. We made numerous feature improvements and bugfixes, including support for [expiring API tokens](https://github.com/pypi/warehouse/pull/11122), support for [credential-free package uploads with OIDC](https://github.com/pypi/warehouse/pull/11272), a refactor of [core permissions internals](https://github.com/pypi/warehouse/pull/11218), enhancements to PyPI’s [vulnerability feed](https://github.com/pypi/warehouse/pull/11858), and improvements to [user-facing error messages](https://github.com/pypi/warehouse/pull/11885).

The projects named below represent software of the highest quality. Software of this caliber doesn’t come from just merging PRs and publishing new releases; it comes from careful planning, prioritizing features, familiarity with related projects, and an understanding of the role that a project plays within the larger software ecosystem. We thank these projects’ maintainers both for the work the public sees and for innumerable hours spent on work the public doesn’t see.

We wish you a happy, safe, and similarly productive 2023!

### Some of Trail of Bits’s 2022 Open-Source Contributions

### Cryptography

* [arkworks-rs/algebra](https://github.com/arkworks-rs/algebra/)
  + [Fix evaluation of dense polynomials over domains smaller than the degree #521](https://github.com/arkworks-rs/algebra/pull/521)
* [pyca/cryptography](https://github.com/pyca/cryptography/)
  + [x509/CT: expose more SCT internals #7207](https://github.com/pyca/cryptography/pull/7207)
  + [CT: add `SignedCertificateTimestamp.extensions` #7237](https://github.com/pyca/cryptography/pull/7237)
  + [CT: `extensions` -> `extension\_bytes` #7238](https://github.com/pyca/cryptography/pull/7238)
  + [X.509/Certificate: Add `tbs\_precertificate\_bytes` property #7279](https://github.com/pyca/cryptography/pull/7279)
  + [x509: add `load\_pem\_x509\_certificates` #7878](https://github.com/pyca/cryptography/pull/7878)
* [pyca/pyopenssl](https://github.com/pyca/pyopenssl/)
  + [Make `X509StoreContextError`’s message friendlier #1133](https://github.com/pyca/pyopenssl/pull/1133)
* [RustCrypto/formats](https://github.com/RustCrypto/formats/)
  + [asn1/octet\_string: add `OctetStringRef::decode\_into` #817](https://github.com/RustCrypto/formats/pull/817)
  + [x509-cert: add `Display` impl for `SerialNumber` #820](https://github.com/RustCrypto/formats/pull/820)
* [str4d/rage](https://github.com/str4d/rage/)
  + [age/ssh: make `ssh::Identity: Clone` #329](https://github.com/str4d/rage/pull/329)
* [veraison/go-cose](https://github.com/veraison/go-cose/)
  + [Upload the Trail of Bits public security assessment report #94](https://github.com/veraison/go-cose/pull/94)

### Tech Infrastructure

* [abodelot/jquery.json-viewer](https://github.com/abodelot/jquery.json-viewer/)
  + [Fix JSON object key displaying #26](https://github.com/abodelot/jquery.json-viewer/pull/26)
* [aio-libs/aiohttp](https://github.com/aio-libs/aiohttp/)
  + [Fix unicode errors (#7044) #7099](https://github.com/aio-libs/aiohttp/pull/7099)
* [curl/curl](https://github.com/curl/curl/)
  + [url: allow non-HTTPS HSTS-matching for debug builds #9728](https://github.com/curl/curl/pull/9728)
...