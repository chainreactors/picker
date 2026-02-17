---
title: Building a Secure Electron Auto-Updater
url: https://blog.doyensec.com/2026/02/16/electron-safe-updater.html
source: Over Security - Cybersecurity news aggregator
date: 2026-02-16
fetch_date: 2026-02-17T04:21:22.684607
---

# Building a Secure Electron Auto-Updater

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

# Building a Secure Electron Auto-Updater

16 Feb 2026 - Posted by Michael Pastor

## Introduction

In cooperation with the [Polytechnic University of Valencia](https://www.upv.es/index-en.html) and [Doyensec](https://doyensec.com/), I spent over six months during my internship in a research that combines theoretical foundations in code signing and secure update designs with a practical implementation of these learnings.

This motivated the development of [SafeUpdater](https://github.com/doyensec/ElectronSafeUpdater), a macOS updater vaguely based on the update mechanisms used by [Signal Desktop](https://github.com/signalapp/Signal-Desktop), but otherwise designed as a modular extension.

[SafeUpdater](https://github.com/doyensec/ElectronSafeUpdater) is a package designed for MacOS systems, but its interfaces are easily extensible to both Windows and Linux.

**Please note that âSafeUpdaterâ is not intended to be used as a general-purpose package, but as a reference design illustrating how update mechanisms can be built around explicit threat models and concrete attack mitigations.**

> â ï¸ This software is provided as-is, is not intended for production use, and has not undergone extensive testing.

## The State of Electron Auto-Updates

A software update is the process by which improvements, bug fixes, or changes in functionality are incorporated into an existing application. This process is crucial for maintaining the security of the app, improving performance, and ensuring compatibility with different systems. Because updates are central to both the maintenance and evolution of software, the update mechanism itself becomes one of the most sensitive points from a security perspective.

In Electron applications, an updater typically runs with full user privileges, downloading executable code from the Internet, and may install it with little or no user interaction. If this mechanism is compromised, the result is effectively a remote code execution channel.

Being one of the most widely used application frameworks for desktop apps, Electron also represents one of the most attractive targets for attackers. While the official framework update mechanism provides a ready-to-use solution for most applications, it doesnât protect against certain classes of attacks.

Currently, there are two main solutions for implementing an auto-update system in ElectronJS:

### autoUpdater

The first is the built-in [auto-updater](https://www.electronjs.org/docs/latest/api/auto-updater) module provided by Electron itself. This module handles the basic workflow of checking if there are updates available, downloading the update, and applying it, using standard HTTP(S) and relying on code signing and framework-specific metadata for file integrity.

One of the simplest ways to use it is with [`update-electron-app`](https://www.npmjs.com/package/update-electron-app), a Node.js drop-in solution that is based on Electronâs standard `autoUpdater` method without changing its underlying security assumptions. The following code snippet shows an example of its implementation:

```
const { updateElectronApp, UpdateSourceType } = require('update-electron-app')
updateElectronApp({
  updateSource: {
    type: UpdateSourceType.StaticStorage,
    baseUrl: `https://my-bucket.s3.amazonaws.com/my-app-updates/${process.platform}/${process.arch}`
  }
})
```

This module builds on top of Electronâs autoUpdater, providing a higher-level interface:

```
  autoUpdater.setFeedURL({
    url: feedURL,
    headers: requestHeaders,
    serverType,
  });
```

### electron-updater

The second solution is using [Electron-Builder](https://www.electron.build/index.html)âs `electron-updater` library, which offers a more integrated approach for managing application updates. When the application is built, a release file named `latest.yml` is generated, containing metadata about the latest version. These files are then uploaded to the configured distribution target.

The developer is responsible for integrating the updater into the application lifecycle and configuring the update workflow.

### Differences between âautoUpdaterâ and âelectron-updaterâ

| Feature | Electron Official (`autoUpdater`) | Electron-Builder (`electron-updater`) |
| --- | --- | --- |
| **Publication server requirement** | Requires self-hosted update endpoints | Uses built-in providers (e.g. GitHub Releases) |
| **Code signature validation** | macOS only | macOS and Windows (custom and OS validation) |
| **Metadata and artifact management** | Manual upload of metadata and artifacts required | Automatically generates and uploads release metadata and artifacts |
| **Staged rollouts** | Not natively supported | Natively supported |
| **Supported providers** | Custom HTTP(S) only | Multiple providers (GitHub Releases, Amazon S3, and generic HTTP servers) |
| **Configuration complexity** | Higher, especially with a custom server | Minimal configuration |
| **Cross-platform compatibility** | Platform-specific tools (Squirrel.Mac, Squirrel.Windows) | Unified cross-platform support (Windows, macOS, Linux) |

Now that we have a clear picture of the software update mechanisms available in ElectronJS today, we can shift our focus to two specific threats that are not mitigated by any of the existing open-source solutions. It is worth noting that most of the considerations discussed here are not specific to ElectronJS itself, but apply more broadly to software updaters for desktop applications in general.

At the core of these issues lies a fundamental limitation of modern operating systems: the lack of a reliable, built-in mechanism to fully validate the integrity of the software currently running on the system. While macOS, thanks to its relatively closed ecosystem, does provide native capabilities such as code signing and notarization to help verify software integrity at runtime, this is not the case on Windows. As a result, Windows applications cannot rely on the operating system alone to assert that the updater or the application binary has not been tampered with.

Because of this gap, software updaters must implement additional safeguards and workarounds to compensate for the missing integrity guarantees. These compensating controls are often complex, [error-prone](https://blog.doyensec.com/2020/02/24/electron-updater-update-signature-bypass.html), and inconsistently applied across projects, which ultimately leaves room for entire classes of attacks that remain unaddressed even in the most popular desktop applications.

## The Missing Threats

In all software updater implementations, the following assets are considered critical and must be protected:

* *Update Binary*: The new version of the application to be installed
* *Update Manifest*: Contains metadata such as version number, hashes, and file locations
* *Signing Keys*: Cryptographic keys used to sign update binaries and manifests
* *Distribution Channel*: The method used to deliver updates to the client (e.g., a dedicated update server, an S3 bucket, or a CDN).

In this post, we focus only on the threats that are not mitigated by the default ElectronJS software update mechanisms. In fact, given the absence or limited capabilities around software integrity checks at the OS level, the following threats remain unaddressed:

### Attacks Summary

| Threat | Attack Vector | Threat Actor | Potential Impact |
| --- | --- | -...