---
title: Securing the software supply chain with the SLSA framework
url: https://blog.trailofbits.com/2024/10/01/securing-the-software-supply-chain-with-the-slsa-framework/
source: Trail of Bits Blog
date: 2024-10-02
fetch_date: 2025-10-06T18:53:46.426901
---

# Securing the software supply chain with the SLSA framework

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Securing the software supply chain with the SLSA framework

Cliff Smith

October 01, 2024

[application-security](/categories/application-security/)

Software supply chain security has been a hot topic since the Solarwinds breach back in 2020. Thanks to the Supply-chain Levels for Software Artifacts (SLSA) framework, the software industry is now at the threshold of sustainably solving many of the biggest challenges in securely building and distributing open-source software.

SLSA is a security standard that helps a consumer verify the process by which an open-source software artifact was created. Its cornerstone is a provenance file, a document signed by a build platform attesting to how a binary, container image, or other file was generated from source code through a project-specific build pipeline. However, SLSA is a relatively new standard (version 1.0 was released in April 2023), and in order for its benefits to be fully realized, multiple parties need to adopt and implement it. In addition to the technical work involved, it will also take time to build awareness and drive demand for SLSA-compliant tooling.

To expedite adoption of SLSA, we’ve drafted [PEP 740](https://peps.python.org/pep-0740/#provenance-objects), a specification that adds support for SLSA provenance to PyPI and leverages the power of [trusted publishing](https://blog.trailofbits.com/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/). However, there’s no need to wait for all of this work to be fully realized to realize the benefits of SLSA. Read on to learn how you can take advantage of existing SLSA support and help promote good supply chain security practices among your customers and vendors.

### Overview of SLSA

[SLSA 1.0](https://slsa.dev/spec/v1.0/onepage) specifies three different levels of compliance, called SLSA Build Level 1, 2 and 3, that can be achieved through the publication of a suitable build provenance file. This file identifies the build platform itself (usually a hosted CI/CD platform, such as GitHub Actions or Google Cloud Build) and the configuration parameters used to generate the final build artifact. In the case of a GitHub Actions build, the provenance file will identify the workflow definition file, the repository and tag that were built, and any other applicable inputs, such as the ID of the pull request that triggered the build. Additionally, the platform should make a best-effort attempt to list all of the project’s direct and indirect dependencies.

Level 1 compliance provides visibility into the build process so that honest mistakes can be caught: the provenance file need only include the data described above and be published in an accessible location. Level 2 ensures the authenticity of the build provenance file. The key requirements are that the provenance file must be signed by the build platform, and the build must be run on dedicated infrastructure. At Level 3, additional build platform hardening prevents forgery of the provenance file. The build platform must prevent user-defined steps in the build process from accessing the signing key, and no two builds should be able to influence each other in any way, whether they run in series or in parallel.

Most attacks against build and distribution processes will face substantial obstacles if the targeted project has reached SLSA Level 3 compliance. An attacker who compromises package upload credentials would still need to compromise the provenance signing key in order to forge a valid provenance file for their malicious binary or container image. If an attacker somehow tampered with the parameters to the build process, any changes would be reflected in the provenance file. (Starting at Build Level 2, the build parameters shown in the provenance must be read directly from the build platform, not provided separately by the entity invoking the build.) Moreover, if signed provenance is uploaded to a service with a public transparency log like Sigstore, any such attack would be conducted in the open with immediate visibility into each build that was altered.

A growing list of build platforms have built-in support for SLSA, allowing projects to reach Level 3 by invoking pre-written build pipeline steps. From the consumer side, the [slsa-verifier](https://github.com/slsa-framework/slsa-verifier) project provides configurable tooling to verify a published provenance file.

### The final step: Integration into package ecosystems

With all this tooling already implemented, it seems like the benefits of SLSA are already within reach. But there’s one more piece to the puzzle: integration of this SLSA-compliant tooling into the package distribution tools developers use on a daily basis. This final step requires operational decisions that are in the purview of the package management system, not the SLSA framework itself. For example, how does a downstream user know which build platforms a project will use? When is a project permitted to switch build platforms between versions? Is it acceptable for some releases to have signed Level 3 provenance, but others to have only Level 1 provenance?

If these questions are left unanswered, some threats can slip through the cracks. Suppose an attacker steals package upload credentials for a project that normally provides signed Level 3 provenance files, then uploads an artifact with unsigned Level 1 provenance. How can consumers protect themselves in that scenario? The community would need to agree on a convention for handling SLSA level downgrades, preferably with automatic enforcement in package publishing and distribution tools.

These outstanding issues are the reason why the benefits of SLSA are not yet fully realized. The reference implementations of SLSA tooling lay the groundwork, but it is up to each package management system to operationalize the framework so that consumers do not have to manually resolve ambiguities.

### PEP 740 and provenance in PyPI

Now would be a good time to highlight the in-progress [PEP 740](https://peps.python.org/pep-0740/#provenance-objects), a draft specification authored by Trail of Bits engineers William Woodruff and Facundo Tuesca to add support for SLSA provenance to PyPI. Thanks to the existing support for [trusted publishing](https://blog.trailofbits.com/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/), each package’s build platform itself provides the trust mechanism for PyPI uploads through OIDC tokens issued to each build run. Provenance can piggyback on this process by using the same OIDC tokens to generate keyless signatures through Sigstore, then upload the provenance file to the registry along with the package. This design reduces the entire system’s attack surface so that a bad actor can only submit untrusted artifacts into PyPI by compromising the package source code, or by forging a GitHub OIDC token.

### Taking advantage of SLSA as a consumer

Development teams need not wait for PEP 740 and adoption of similar standards by other package managers to reap the benefits of SLSA incrementally. Some package managers already have built-in support for downloading and verifying signed provenance. With a little extra effort, slsa-verifier can be invoked independently in the case of software distribution tools that have not yet completed their integrations.

As of this writing, the package ecosystem with the most deeply integrated SLSA support is npm. Each package’s page on npmjs.com summarizes the latest version’s build provenance with a link to the relevant Sigstore transparency log. On the client side, the npm audit signatures command will automatically verify all available provenance for a project’s dependencies. This command’s output includes the number of packages with verified build attestation, but does not say which packages those are. Thus...