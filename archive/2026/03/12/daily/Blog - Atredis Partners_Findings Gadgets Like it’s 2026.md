---
title: Findings Gadgets Like it’s 2026
url: https://www.atredis.com/blog/2026/3/12/findings-gadgets-like-its-2026
source: Blog - Atredis Partners
date: 2026-03-12
fetch_date: 2026-03-13T04:06:00.718060
---

# Findings Gadgets Like it’s 2026

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# Findings Gadgets Like it’s 2026

Mar 12

Written By [Stephen Breen](/blog?author=69b2d162741bad041a003fa8)

## Introduction

Java deserialization vulnerabilities have been of interest to me for nearly a decade. In 2016, my team published a blog post titled "[What Do WebLogic, WebSphere, JBoss, Jenkins, OpenNMS, and Your Application Have in Common? This Vulnerability.](https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/)" which kicked off a firestorm of vulnerabilities in high profile enterprise applications. Since that time, the Java ecosystem has taken steps to both eliminate the prevalence of deserialization of untrusted data, and to reduce the number of deserialization gadgets that can be used for malicious purposes.

Tools such as ysoserial have been treated in the penetration testing community as a largely complete catalog of gadgets due to the complexity of discovering new gadget chains. While new chains do surface occasionally, the research process has remained to some degree manual, complex, and unapproachable for those not steeped in the research. The release of new gadgets has slowed significantly, for example, ysoserial has not had new gadgets added for years. A quick review of the research shows very few newly proposed gadget chains. All of the widely used application servers ship in configurations that are rarely vulnerable to any public gadget chains.

As consultants who primarily do platform security assessments, our time is not best spent pursuing novel gadget chains given the complexity of doing so. We wondered if an LLM could automate the task of gadget discovery; exactly the sort of task an LLM should be well suited for. Over the course of just two days, we were able to implement a new methodology for gadget discovery and demonstrate its effectiveness by finding several new chains, including one novel chain that works against WildFly application server and may affect other popular application servers and frameworks.

## Background: Gadget Chains in 60 Seconds

For readers not immersed in the weeds of Java deserialization, a Java deserialization gadget chain is a sequence of method calls that kicks off when methods like `ObjectInputStream.readObject()` processes an attacker-controlled input and ends in a dangerous `sink` method that executes some unintended action that is useful to an attacker. The `sink` methods can trigger things like command execution, file writes, XML External Entity Injection (XXE), or other internal Java methods that have unintended consequences. The deserialization chain relies on Java classes that already exist on the application server classpath and chains them together through various techniques.

There are several key difficulties to identifying useful deserialization chains. A typical application server classpath can contain thousands of classes that implement `Serializable`, all of which are potential entry points that can be sent to the initial `readObject` call. Each `Serializable` class can hold arbitrary subtypes and many times these subtypes are abstract and can therefore map to many different classes. Combine that with dynamic language features such as reflection, and the search space becomes huge. Existing tools like GadgetInspector use static analysis to try and reduce the search space to something that can be manually validated but may miss certain types of chains. This also still requires manual analysis to weed out most of the results which will be false-positives.

The idea behind this project was that an LLM, given the right structure, could use a combination of static analysis, reasoning, and implementation skills to build gadget chains from start to finish. LLMs perform exceedingly well in scenarios where a feedback loop is constructed where the LLM can validate its hypotheses.

## Architecture Overview

The tooling architecture was designed through back and forth prompting with the LLM. It has some interesting properties that cater to the strengths of LLMs. The tool can be broken into 5 separate components:

1. Call Graph Builder - Tooling to build out a graph of sources, sinks, and connections. This is currently stored in a SQLite Database.
2. Graph Query Server - A small HTTP server with REST APIs that expose endpoints which query the call graph database. The LLM agents will use this to search for paths.
3. LLM Agents - Claude Code acts as the LLM agent. It queries the graph, discovers potential chains, and evaluates the chains optionally using the "Dynamic Runner" to help with debugging.
4. Dynamic Runner - Tools for executing and debugging candidate test harnesses. The LLM agent will not always use these, but they are available for it.
5. Evaluation - First evaluate using a test class compiled against the target classpath. Once a chain is confirmed locally, test against a minimal web application deployed in the target environment.

### Call Graph Builder

The goal with building the call graph is to create a graph with every possible source and sink, and all possible paths between the two. The reality is that we need to make some compromises because the number of possibilities is too large. For construction of the call graph, we start with the IBM Watson Libraries for Analysis (WALA) Class Hierarchy Analysis (CHA). CHA is technique for constructing call graphs that is fast but imprecise; not all edges in the CHA call graph will actually be traversable in a real deserialization chain.

The CHA produces a huge graph, especially when applied to the classpath of an application server or complex enterprise application. To prune the graph, we restrict it to classes that implement `Serializable` or `Externalizable` and then expand outward three hops via field types and method signatures. Anything outside of that scope will be excluded from the analysis.

The CHA graph is the base. On top of the CHA graph we do a pass over all target classes and inject additional edges to account for dynamic features in Java, this is done by examining class bytecode with the Java ASM library. A second pass with ASM is done to create edges for possible type confusion scenarios. For every `Serializable` class whose type is an interface or abstract class, it records every class that implements it.

### Graph Query Server

The Graph Query Server is a simple Python-based FastAPI service that exposes HTTP endpoints for the LLM to query. The following endpoints are exposed:

* `/paths` finds all simple paths from an entry point to a sink, with edge types annotated
* `/type_confusion_targets` returns every concrete type injectable into a given field
* `/decompile` runs CFR on any class or method and returns decompiled source
* `/serialization_constraints` tells you which fields survive serialization, and what subtypes can go into each
* `/predecessors` works backward from a sink to find what calls it
* `/classes_implementing` lists all concrete implementors of an interface

These API en...