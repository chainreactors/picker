---
title: InQL v6.1.0 Just Landed with New Features & Contribution Swag! 🚀
url: https://blog.doyensec.com/2025/12/02/inql-v610.html
source: Over Security - Cybersecurity news aggregator
date: 2025-12-02
fetch_date: 2025-12-03T03:16:52.504314
---

# InQL v6.1.0 Just Landed with New Features & Contribution Swag! 🚀

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

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# InQL v6.1.0 Just Landed with New Features & Contribution Swag! ð

02 Dec 2025 - Posted by Bartek GÃ³rkiewicz

## Introduction

We are excited to announce a new release of our Burp Suite Extension - [InQL v6.1.0](https://github.com/doyensec/inql)! The complete re-write from Jython to Kotlin in our previous update ([v6.0.0](https://github.com/doyensec/inql/releases/tag/v6.0.0)) laid the groundwork for us to start implementing powerful new features, and this update delivers the first exciting batch.

This new version introduces key features like our new **GraphQL schema brute-forcer** (which abuses âdid you meanâ¦â suggestions), **server engine fingerprinter**, **automatic variable generation** when sending requests to Repeater/Intruder, and various other quality-of-life and performance improvements.

## Key New Features

### The GraphQL Schema Brute-Forcer

Until now, InQL was most helpful when a server had introspection enabled or when you already had the GraphQL schema file. With v6.1.0, the tool can now attempt to reconstruct the backend schema by abusing the âdid you meanâ¦â suggestions supported by many GraphQL server implementations.

This feature was inspired by the excellent [Clairvoyance CLI tool](https://github.com/nikitastupin/clairvoyance). We implemented a similar algorithm, also based on regular expressions and batch queries. Building this directly into InQL brings it one step closer to being the all-in-one Swiss Army knife for GraphQL security testing, allowing researchers to access every tool they need in one place.

**How It Works**

When InQL fails to fetch a schema because introspection is disabled, you can now choose to âLaunch schema bruteforcerâ. The tool will then start sending hundreds of batched queries containing field and argument names guessed from a wordlist.

InQL then analyzes the serverâs error messages, by looking for specific errors like `Argument 'contribution' is required` or `Field 'bugs' not found on type 'inql'`. It also parses helpful suggestions, such as `Did you mean 'openPR'?`, which rapidly speeds up discovery. At the same time, it probes the types of found fields and arguments (like `String`, `User`, or `[Episode!]`) by intentionally triggering type-specific error messages.

This process repeats until the entire reachable schema is mapped out. The result is a reconstructed schema, built piece-by-piece from the serverâs own validation feedback. All without introspection.

Be aware that the scan can take time. Depending on the schemaâs complexity, server rate-limiting, and the wordlist size, a full reconstruction can take anywhere from a few minutes to several hours. We recommend visiting the InQL settings tab to properly set up the scan for your specific target.

[![

Your browser does not support the video tag.
](../../../public/images/inql_bruteforcer.png)](../../../public/images/inql_bruteforcer.mp4)

### The GraphQL Server Engine Fingerprinter

The new version of InQL is now able to fingerprint the GraphQL engine used by the back-end server. Each GraphQL engine implements slightly different security protections and insecure defaults, opening door for abusing unique, engine-specific attack vectors.

The fingerprinted engine can be looked up in the [GraphQL Threat Matrix](https://github.com/nicholasaleks/graphql-threat-matrix) by [Nick Aleks](https://github.com/nicholasaleks). The matrix is a fantastic resource for confirming which implementation may be vulnerable to specific GraphQL threats.

**How It Works**

Similarly to the [graphw00f CLI tool](https://github.com/dolevf/graphw00f), InQL sends a series of specific GraphQL queries to the target server and observes how it responds. It can differentiate the specific engines by analyzing the unique nuances in their error messages and responses.

For example, for the following query:

```
query @deprecated {
    __typename
}
```

An **Apollo** server typically responds with an error message stating `Directive \"@deprecated\" may not be used on QUERY.`. However, a **GraphQL Ruby** server, will respond with the `'@deprecated' can't be applied to queries` message.

When InQL successfully fingerprints the engine, it displays details about its implementation right in the UI, based on data from the [GraphQL Threat Matrix](https://github.com/nicholasaleks/graphql-threat-matrix).

[![

Your browser does not support the video tag.
](../../../public/images/inql_fingerprinter.png)](../../../public/images/inql_fingerprinter.mp4)

### Automatic Variable Generation (Default Values)

While previous InQL versions were great for analyzing schemas, finding circular references, and identifying points-of-interest, actually crafting a valid query could be frustrating. The tool didnât handle variables, forcing you to fill them in manually. The new release finally fixes that pain point.

Now, when you use âSend to Repeaterâ or âSend to Intruderâ on a query that requires variables (like a `search` argument of type `String`), InQL will automatically populate the request with placeholder values. This simple change significantly improves the speed and flow of testing GraphQL APIs.

Here are the default values InQL will now use:

```
"String" -> "exampleString"
"Int" -> 42
"Float" -> 3.14
"Boolean" -> true
"ID" -> "123"
ENUM -> First value
```

### Usability and Performance Improvements

We also implemented various usability and performance improvements. These changes include:

* Search inside the InQL Scanner tab, and in the Repeater/Intruder
* Improved POI Regex matching
* Improved caching for better performance
* Added a delayed POI and cycle detection to improve the schema parsing speed
* Various bugs and UI fixes

## Join the InQL Community (And Get Swag!)

InQL is an open-source project, and we welcome every contribution. We want to take this opportunity to thank the community for all the support, bug reports, and feedback weâve received so far!

With this new release, **weâre excited to announce a new initiative to reward contributors**. To show our appreciation, weâll be sending exclusive Doyensec swag and/or gift cards to community members who fix issues or create new features.

To make contributing easy, make sure to read the projectâs `README.md` file and review the existing [issues on GitHub](https://github.com/doyensec/inql/issues). We encourage you to start with tasks labeled `Good First Issue` or `Help Wanted`.

Some of the good first issues we would like to see your contribution for:

* [Add functionality to send GraphQL requests in non-standard formats #124](https://github.com/doyensec/inql/issues/124)
* [Customizable input arguments values #113](https://github.com/doyensec/inql/issues/113)
* [Add export to JSON / CSV #169](https://github.com/doyensec/inql/issues/169)
* [Search across InQL Scanner tab #68](https://github.com/doyensec/inql/issues/68)
* [Track the GraphQL operations from the Burp History (when introspection is not enabled) #170](https://github.com/doyensec/inql/issues/170)

If you have an idea for a new feature or have found a bug, please open a new issue to discuss it before you start building. This helps everyone get on the same page.

We canât wait to see your pull requests!

## Conclusion

As weâve mentioned, we are extremely excited about this new release and the direction InQL is heading. We hope to see more contributions from the ever-growing cybersecurity c...