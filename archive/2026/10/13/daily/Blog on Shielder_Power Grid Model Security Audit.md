---
title: Power Grid Model Security Audit
url: https://www.shielder.com/blog/2026/10/power-grid-model-security-audit/
source: Blog on Shielder
date: 2026-10-13
fetch_date: 2026-10-14T06:53:14.875270
---

# Power Grid Model Security Audit

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage")

* [Home](https://www.shielder.com/ "Home")
* [Company](https://www.shielder.com/company "Company")
* [Services](https://www.shielder.com/services "Services")
* [Advisories](https://www.shielder.com/advisories "Advisories")
* [Blog](https://www.shielder.com/blog "Blog")
* [Careers](https://www.shielder.com/careers "Careers")
* [Contacts](https://www.shielder.com/contacts "Contacts")
* ENG

  [ENG](https://www.shielder.com/blog/2026/10/power-grid-model-security-audit/ "ENG")
  [ITA](https://www.shielder.com/it/blog/2026/10/power-grid-model-security-audit/ "ITA")

# Power Grid Model Security Audit

## TL;DR

In 2026, Shielder was hired by [OSTIF](https://ostif.org/) to perform a security audit of [Power Grid Model](https://github.com/PowerGridModel/power-grid-model), an open-source library for steady-state distribution power system analysis, developed under the [LF Energy](https://lfenergy.org/) umbrella and maintained by Alliander.

**Today, we are publishing the [full report](https://github.com/ShielderSec/public-reports/blob/main/2026/%5BOSTIF%5D%20Power%20Grid%20Model%20-%20Report%20v1.2.pdf) in our [dedicated repository](https://github.com/ShielderSec/public-reports/)**.

## Context

Power Grid Model (PGM) is a high-performance computational backend for electrical distribution grids: given a model of the grid (nodes, lines, transformers, loads, generators…), it performs Power Flow, State Estimation and Short Circuit calculations. It is used across the energy sector for grid planning, expansion, reliability and congestion studies.

Under the hood, PGM is made of three layers:

* A core C++ library, which implements the actual calculations.
* A C API shim, which exposes the C++ object instantiation and method calls.
* A Python package, built on top of the C API, which exposes user-friendly methods and leverages NumPy structured arrays for its data structures.

On top of that, the auxiliary [power-grid-model-io](https://github.com/PowerGridModel/power-grid-model-io) library takes care of converting grid data from and to other formats (e.g., Excel/CSV files from other grid tools) using YAML mapping files. Given how often it is used to feed data into PGM, we included it in scope.

See it in action:

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` from power_grid_model import PowerGridModel from power_grid_model.utils import json_deserialize_from_file  # load a grid model from a JSON file input_data = json_deserialize_from_file("input.json")  # build the model and run a power flow calculation model = PowerGridModel(input_data) output = model.calculate_power_flow()  print(output["node"]["u_pu"]) ``` |

As with every audit, we started with threat modeling. With libraries, we have found this to be crucial: the code alone can’t tell you how developers in the “real world” are using it, where the interesting inputs come from. So we studied the documentation, examples and integrations to understand **how end-users install, configure and use the project**, then refined the model as the code review progressed.

As a result, three main points emerged:

1. PGM is a library, so its attack surface is whatever data the embedding application feeds it. Grid models are routinely exchanged between tools and organizations, which makes the **deserialization pipeline** (JSON and msgpack) and the **file ingestion layer** (`power-grid-model-io` converters and their YAML mappings) the most likely entry points for untrusted input.
2. The heavy lifting is done in C++, a memory-unsafe language. The Python package performs a fair amount of input validation, but the **C API boundary** can also be used directly (e.g., from other language bindings), skipping those checks entirely.
3. PGM is distributed as pre-built wheels on PyPI, so a compromise of the **release process** would propagate to every downstream integrator.

With these attack scenarios in mind, we have performed the audit by combining manual and tool-assisted source code review (with SAST tooling such as `semgrep` and publicly available C/C++ rules), a fuzzing campaign, and a review of the GitHub workflows for supply-chain attack scenarios.

## Fuzzing

Since PGM was not on-boarded on [OSS-Fuzz](https://github.com/google/oss-fuzz) yet, we developed a harness using the de facto standard libFuzzer `LLVMFuzzerTestOneInput` interface, running on the AFL++ engine. As untrusted input reaches the library through a sequence of stages â a document is parsed, written into buffers, turned into a model and finally solved â the team wrote one harness for each of these, so that every stage could be fuzzed at its own speed and depth. The harnesses exercise the following C APIs:

* `PGM_create_deserializer_from_binary_buffer` and `PGM_dataset_info_*`, to turn the fuzzer input into an in-memory dataset and expose its metadata.
* `PGM_deserializer_parse_to_buffer`, to access the deserialized dataset.
* `PGM_create_model`, `PGM_copy_model` and `PGM_get_indexer`, which build the in-memory model.
* `PGM_calculate`, which performs the calculation on the model.
* `PGM_update_model`, to apply an update document to an existing model.

Since randomly mutated inputs are mostly rejected early by the parser, we then enhanced the fuzzer with a custom mutator that generates structurally valid inputs, so that more test cases could reach the core calculation logic.

The harness was contributed to the project in PR [#1617](https://github.com/PowerGridModel/power-grid-model/pull/1617) and will soon be onboarded on OSS-Fuzz, so the project will keep benefiting from it after the audit ended.

## Findings

While auditing, we have discovered three vulnerabilities (one with High severity, one with Medium, one with Low) that we reported through the GitHub Security portal of the [power-grid-model](https://github.com/PowerGridModel/power-grid-model/security/advisories) and [power-grid-model-io](https://github.com/PowerGridModel/power-grid-model-io/security/advisories) repositories.

**Arbitrary Method Invocation via YAML Mapping ([CVE-2026-84457](https://github.com/PowerGridModel/power-grid-model-io/security/advisories/GHSA-m3mm-w2xx-jvv7))**

power-grid-model-io’s Tabular Converter uses YAML mapping files to describe how to convert tabular data (e.g., Excel sheets) into PGM components. Mappings can reference Python functions by their dotted path, to transform values while converting. These paths were resolved by a `get_function()` helper with a plain `import_module()` + `getattr()`, and the resulting function was then invoked with keyword arguments taken from the input data columns.

Although the project’s `SECURITY.md` mentioned an allow-list to prevent the execution of arbitrary functions, no such check was actually implemented in the Tabular Converter. Therefore, a malicious mapping could reference, for instance, `os.popen`, map its `cmd` argument to a data column, and achieve code execution as soon as the mapping is used to load input data.
The severity was set to High: the impact is full code execution in the host process, but the attacker needs to control the YAML mapping (and, to pass arguments, the input data as well).

The maintainers fixed this in power-grid-model-io version `2.0.0` by implementing an allow-list of functions that can be used in the Tabular Converter configuration.

**Unbounded JSON Nesting Leads to Denial of Service ([CVE-2026-76912](https://github.com/PowerGridModel/power-grid-model/security/advisories/GHSA-jch4-ggwc-h4q5))**

PGM’s `json_deserialize()` uses nlohmann’s JSON SAX parser under the hood, with a custom visitor that pushes a new buffer every time it encounters a `[` or `{` token. Since there was no depth check, a deeply nested JSON payload could keep pushing entries until the host process ran out of memory and got killed by the OOM-killer. With an amplification factor of roughly 4000x...