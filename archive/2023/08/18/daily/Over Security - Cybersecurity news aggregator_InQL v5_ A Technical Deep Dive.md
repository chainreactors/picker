---
title: InQL v5: A Technical Deep Dive
url: https://blog.doyensec.com//2023/08/17/inql-v5.html
source: Over Security - Cybersecurity news aggregator
date: 2023-08-18
fetch_date: 2025-10-04T12:00:34.673474
---

# InQL v5: A Technical Deep Dive

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

# InQL v5: A Technical Deep Dive

17 Aug 2023 - Posted by Andrew Konstantinov

Weâre thrilled to pull back the curtain on the latest iteration of our
widely-used Burp Suite extension - [InQL](https://github.com/doyensec/inql).
Version 5 introduces significant enhancements and upgrades, solidifying its
place as an indispensable tool for penetration testers and bug bounty hunters.

* [Introduction](#introduction)
* [The Journey So Far: From Jython to Kotlin](#the-journey-so-far-from-jython-to-kotlin)
  + [The Challenges of Converting a Burp Extension Into Kotlin](#the-challenges-of-converting-a-burp-extension-into-kotlin)
  + [Sidestepping the need for stickytape](#sidestepping-the-need-for-stickytape)
* [Introducing GQLSpection: The Core of InQL v5.x](#introducing-gqlspection-the-core-of-inql-v5x)
* [New Features](#new-features)
  + [Points of Interest](#points-of-interest)
  + [Improved Logging](#improved-logging)
  + [In-line Annotations](#in-line-annotations)
* [The Future of InQL and GraphQL Security](#the-future-of-inql-and-graphql-security)
* [InQL: A Great Project for Students and Contributors](#inql-a-great-project-for-students-and-contributors)
* [Conclusion](#conclusion)

![InQL v5.0](../../../public/images/inql.png)

# Introduction

The cybersecurity landscape is in a state of constant flux. As GraphQL adoption
surges, the demand for an adaptable, resilient testing tool has become
paramount. As leaders in GraphQL security, Doyensec is proud to reveal the most
recent iteration of our open-source testing tool - [InQL v5.x](https://github.com/doyensec/inql/releases). This isnât merely
an update; itâs a comprehensive revamp designed to augment your GraphQL testing
abilities.

# The Journey So Far: From Jython to Kotlin

Our journey with InQL started on the Jython platform. However, as time went by,
we began to experience the limitations of Jython - chiefly, its lack of support
for Python 3, which made it increasingly difficult to find compatible tooling
and libraries. It was clear a transition was needed. After careful
consideration, we chose Kotlin. Not only is it compatible with Java (which Burp
is written in), but it also offers robustness, flexibility, and a thriving
developer community.

## The Challenges of Converting a Burp Extension Into Kotlin

We opted to include the entire Jython runtime (over 40 MB) within the Kotlin
extension to overcome the challenges of reusing the existing Jython code.
Although it wasnât the ideal solution, this approach allowed us to launch the
extension as Kotlin, initiate the Jython interpreter, and delegate execution to
the older Jython code.

```
class BurpExtender: IBurpExtender, IExtensionStateListener, BurpExtension {

    private var legacyApi: IBurpExtenderCallbacks? = null
    private var montoya: MontoyaApi? = null

    private var jython: PythonInterpreter? = null
    private var pythonPlugin: PyObject? = null

    // Legacy API gets instantiated first
    override fun registerExtenderCallbacks(callbacks: IBurpExtenderCallbacks) {

        // Save legacy API for the functionality that still relies on it
        legacyApi = callbacks

        // Start embedded Python interpreter session (Jython)
        jython = PythonInterpreter()
    }

    // Montoya API gets instantiated second
    override fun initialize(montoyaApi: MontoyaApi) {
        // The new Montoya API should be used for all of the new functionality in InQL
        montoya = montoyaApi

        // Set the name of the extension
        montoya!!.extension().setName("InQL")

        // Instantiate the legacy Python plugin
        pythonPlugin = legacyPythonPlugin()

        // Pass execution to legacy Python code
        pythonPlugin!!.invoke("registerExtenderCallbacks")
    }

    private fun legacyPythonPlugin(): PyObject {
        // Make sure UTF-8 is used by default
        jython!!.exec("import sys; reload(sys); sys.setdefaultencoding('UTF8')")

        // Pass callbacks received from Burp to Python plugin as a global variable
        jython!!.set("callbacks", legacyApi)
        jython!!.set("montoya", montoya)

        // Instantiate legacy Python plugin
        jython!!.exec("from inql.extender import BurpExtenderPython")
        val legacyPlugin: PyObject = jython!!.eval("BurpExtenderPython(callbacks, montoya)")

        // Delete global after it has been consumed
        jython!!.exec("del callbacks, montoya")

        return legacyPlugin
    }
```

## Sidestepping the need for stickytape

Our switch to Kotlin also solved another problem. Jython extensions in Burp
Suite are typically a single `.py` file, but the complexity of InQL necessitates a
multi-file layout. Previously, we used the
[stickytape](https://github.com/mwilliamson/stickytape) library to compress the
Python code into a single file. However, stickytape introduced subtle bugs and
inhibited access to static files. By making InQL a Kotlin extension, we can now
bundle all files into a JAR and access them correctly.

# Introducing GQLSpection: The Core of InQL v5.x

A significant milestone in our transition journey involved refactoring the core
portion of InQL that handles GraphQL schema parsing. The result is
[GQLSpection](https://github.com/doyensec/gqlspection) - a standalone library
compatible with Python 2/3 and Jython, featuring a convenient CLI interface.
Weâve included all GraphQL code examples from the GraphQL specification in our
test cases, ensuring comprehensive coverage.

As an added advantage, it also replaces the standalone and CLI modes of the
previous InQL version, which were removed to streamline our code base.

![GQLSpection](../../../public/images/inql_v5_gqlspection.png)

# New Features

Our clients rely heavily on cutting-edge technologies. As such, we frequently
have the opportunity to engage with real-world GraphQL deployments in many of our
projects. This rich exposure has allowed us to understand the challenges
InQL users face and the requirements they have, enabling us to decide which
features to implement. In response to these insights, weâve introduced several
significant features in InQL v5.0 to support more effective and efficient audits
and investigations.

## Points of Interest

One standout feature in this version is âPoints of Interestâ. Powered by
GQLSpection and with the initial implementation contributed by
[@schoobydrew](https://github.com/doyensec/inql/pull/82), this is essentially a
keyword scan equipped with several customizable presets.

![Points of Interest settings](../../../public/images/inql_v5_poi_settings.png)

The Points of Interest scan proves exceptionally useful when analyzing extensive
schemas with over 50 queries/mutations and thousands of fields. It produces
reports in both human-readable text and JSON format, providing a high-level
overview of the vast schemas often found in modern apps, and aiding pentesters
in swiftly identifying sensitive data or dangerous functionality within the
schema.

![Points of Interest results](../../../public/images/inql_v5_poi.png)

## Improved Logging

One of my frustrations with earlier versions of the tool was the lack of useful error
messages when the parser broke on real-world schemas. So, I introduced
configurable logging. This, coupled with the fact that parsing functionality is
now handled by GQLSpection, has made InQL v5.0 much more reliable and user-friendly.

## In-line Annotations

Another important addition to I...