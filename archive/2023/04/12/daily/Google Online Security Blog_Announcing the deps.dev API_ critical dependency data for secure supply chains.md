---
title: Announcing the deps.dev API: critical dependency data for secure supply chains
url: http://security.googleblog.com/2023/04/announcing-depsdev-api-critical.html
source: Google Online Security Blog
date: 2023-04-12
fetch_date: 2025-10-04T11:29:58.172685
---

# Announcing the deps.dev API: critical dependency data for secure supply chains

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Announcing the deps.dev API: critical dependency data for secure supply chains](https://security.googleblog.com/2023/04/announcing-depsdev-api-critical.html "Announcing the deps.dev API: critical dependency data for secure supply chains ")

April 11, 2023

Posted by Jesper Sarnesjo and Nicky Ringland, Google Open Source Security Team

Today, we are excited to announce the [deps.dev API](https://docs.deps.dev/api/v3alpha), which provides free access to the deps.dev dataset of security metadata, including dependencies, licenses, advisories, and other critical health and security signals for more than 50 million open source package versions.

Software supply chain attacks are increasingly common and harmful, with high profile incidents such as [Log4Shell](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html), [Codecov](https://about.codecov.io/security-update), and the recent [3CX hack](https://www.securityweek.com/mandiant-investigating-3cx-hack-as-evidence-shows-attackers-had-access-for-months/). The overwhelming complexity of the software ecosystem causes trouble for even the most diligent and well-resourced developers.

We hope the deps.dev API will help the community make sense of complex dependency data that allows them to respond to—or even prevent—these types of attacks. By integrating this data into tools, workflows, and analyses, developers can more easily understand the risks in their software supply chains.

# The power of dependency data

As part of Google’s ongoing efforts to [improve open source security](https://blog.google/technology/safety-security/shared-success-in-building-a-safer-open-source-community/), the Open Source Insights team has built a reliable view of software metadata across 5 packaging ecosystems. The deps.dev data set is continuously updated from a range of sources: package registries, the [Open Source Vulnerability database](https://osv.dev/), code hosts such as GitHub and GitLab, and the software artifacts themselves. This includes 5 million packages, more than 50 million versions, from the Go, Maven, PyPI, npm, and Cargo ecosystems—and you'd better believe we're counting them!

We collect and aggregate this data and derive transitive dependency graphs, advisory impact reports, [OpenSSF Security Scorecard](https://securityscorecards.dev/) information, and more. Where the [deps.dev website](http://deps.dev) allows human exploration and examination, and the [BigQuery dataset](https://docs.deps.dev/bigquery/v1/) supports large-scale bulk data analysis, this new API enables programmatic, real-time access to the corpus for integration into tools, workflows, and analyses.

The API is used by a number of teams internally at Google to support the security of our own products. One of the first publicly visible uses is the [GUAC integration](https://github.com/guacsec/guac/tree/main/pkg/handler/collector/deps_dev), which uses the deps.dev data to enrich [SBOMs](https://security.googleblog.com/2022/06/sbom-in-action-finding-vulnerabilities.html). We have more exciting integrations in the works, but we’re most excited to see what the greater open source community builds!

We see the API as being useful for tool builders, researchers, and tinkerers who want to answer questions like:

* What versions are available for this package?
* What are the licenses that cover this version of a package—or all the packages in my codebase?
* How many dependencies does this package have? What are they?
* Does the latest version of this package include changes to dependencies or licenses?
* What versions of what packages correspond to this file?

Taken together, this information can help answer the most important overarching question: how much risk would this dependency add to my project?

The API can help surface critical security information where and when developers can act. This data can be integrated into:

* IDE Plugins, to make dependency and security information immediately available.
* CI/CD integrations to prevent rolling out code with vulnerability or license problems).
* Build tools and policy engine integrations to help ensure compliance.
* Post-release analysis tools to detect newly discovered vulnerabilities in your codebase.
* Tools to improve inventory management and mystery file identification.
* Visualizations to help you discover what your dependency graph *actually* looks like:

  [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJqRDg5P2-UNST05w_PQEeBji_cHb_vNnrGZLJWpjzE7aVKivtu9k9O7CBcka2CGkFpcMjDc46ie6WeXrUXgFig0bQWP2eVY8MREwHlkB_56P4QUWfCYxCOgF_KOTP5R15auiar3GgCDE4VC7CEKnSxEds7oDyF4fSKhJdGgOtDG-L45CCzItgsrkOLA/s1600/dependency_graph_imagined_vs_actual.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJqRDg5P2-UNST05w_PQEeBji_cHb_vNnrGZLJWpjzE7aVKivtu9k9O7CBcka2CGkFpcMjDc46ie6WeXrUXgFig0bQWP2eVY8MREwHlkB_56P4QUWfCYxCOgF_KOTP5R15auiar3GgCDE4VC7CEKnSxEds7oDyF4fSKhJdGgOtDG-L45CCzItgsrkOLA/s1600/dependency_graph_imagined_vs_actual.png)

  # Unique features

  The API has a couple of great features that aren’t available through the deps.dev website.

  ## Hash queries

  A unique feature of the API is hash queries: you can look up the hash of a file's contents and find all the package versions that contain that file. This can help figure out what version of which package you have even absent other build metadata, which is useful in areas such as SBOMs, container analysis, incident response, and forensics.

  ## Real dependency graphs

  The deps.dev dependency data is not just what a package declares (its manifests, lock files, etc.), but rather a full dependency graph computed using the same algorithms as the packaging tools (Maven, npm, Pip, Go, Cargo). This gives a real set of dependencies similar to what you would get by actually installing the package, which is useful when a package changes but the developer doesn’t update the lock file. With the deps.dev API, tools can assess, monitor, or visualize expected (or unexpected!) dependencies.

  ## API in action

  For a demonstration of how the API can help software supply chain security efforts, consider the questions it could answer in a situation like the Log4Shell discovery:

  + **Am I affected?** - A CI/CD integration powered by the free API would automatically detect that a new, critical vulnerability is affecting your codebase, and alert you to act.
  + **Where?** - A dependency visualization tool pulling from the deps.dev API transitive dependency graphs would help you identify whether you can update one of your direct dependencies to fix the issue. If you were blocked, the tool would point you at the package(s) that are yet to be patched, so you could contribute a PR and help unblock yourself further up the tree.
  + **Where else?** - You could query the API with hashes of vendored JAR files to check if vulnerable log4j versions were unexpectedly hiding therein.
  + **How much of the ecosystem is impacted?** - Researchers, package managers, and other interested observers could use the API to understand how their ecosystem has been affected, as we did in [this blog post about Log4Shell’s impact](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html).

  # Getting started

  The API service is globally replicated and highly available, meaning that you and your tools can depend on it being there when you need it.

  It's also free and immediately available—no need to register for an API key. It's just a simple, unauthenticated HTTPS API that returns JSON objects:

  ```
  # List the advisories affecting log4j 1.2.17
  $ curl https://api.deps.dev/v3alpha/systems/mav...