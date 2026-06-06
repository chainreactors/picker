---
title: Welcoming OpenRelik to the OSDFIR Infrastructure family
url: https://osdfir.blogspot.com/2026/06/welcoming-openrelik-to-osdfir.html
source: Instapaper: Unread
date: 2026-06-05
fetch_date: 2026-06-06T05:51:31.309539
---

# Welcoming OpenRelik to the OSDFIR Infrastructure family

[Skip to main content](#main)

# [Open Source DFIR](https://osdfir.blogspot.com/)

A security blog for the digital forensics community on how to perform digital forensic incident response with open source tools.

### Welcoming OpenRelik to the OSDFIR Infrastructure family

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Wajih Yassine](https://www.blogger.com/profile/11522657792247401394 "author profile")

[June 05, 2026](https://osdfir.blogspot.com/2026/06/welcoming-openrelik-to-osdfir.html "permanent link")

Authored by Johan Berggren and Wajih Yassine

## Overview

If you’ve been keeping a close eye on the [OSDFIR Infrastructure](https://github.com/google/osdfir-infrastructure) repository over the last few months, you might have noticed a new face in the lineup. While many of you have already begun the migration, we are excited (and perhaps a little overdue!) to announce that OpenRelik is available for use through the OSDFIR Infrastructure project!

![](https://blogger.googleusercontent.com/img/a/AVvXsEhqRMEKIJhkkAy2Mpzu-xVT6n58INv2GLofsdPQrmo4MUNY3BopROUCdwTz0F_tzY2hmjEfaHWQWT0yaZLjmx7-aO-NNVTk8jMAAsgWGgySzK-CIg6pha0DD8NtLC5BUoq0t5Yc5KkhHEFytOtsDxs8Rg8Mr1U6MUKmWqFvLKpi3g-aVdfoGhA_B0imwjaY)

## What is OpenRelik?

[OpenRelik](https://openrelik.org/) is an open-source platform designed to support collaborative digital forensic investigations. It provides a modular processing pipeline for DFIR teams, combining an interface for workflow management, real-time collaboration features, and a centralized repository for shared artifacts. The platform addresses challenges related to running disparate tools, managing isolated dependencies, and tracking intermediate data across different systems.

The primary goal of OpenRelik is to automate the processing of forensic artifacts while using a resilient, distributed architecture. It allows teams to integrate custom workflows, run analysis tasks in parallel, and share methodologies across different cases. By decoupling the architecture, the system enables users to add new tools without relying on the core system, providing a consistent and scalable approach to incident response.

### A Look Inside an OpenRelik Workflow

The image below illustrates how OpenRelik visualizes a processing pipeline. Instead of running command-line tools sequentially and losing track of outputs, analysts can build and execute a workflow that processes evidence dynamically and in parallel.

![](https://blogger.googleusercontent.com/img/a/AVvXsEiESdtHtxNDLx0tCmyJmd0QTjz6JP50KTsaZRdx09U1m2sELKLmoRtw7HKjvnJ-5QxdP6NNmAq6AnDlX4mh7PvKpH7KnCnKxYG3PFVHDlni5qmQ7PCL6rqQF-zIVnPSdrNFDNDGXnnWiXuQam7GC4DCneSo0a4MMdodDOkqvQFog9xclLUIKifbeoYZ_9bK)

Here is a breakdown of what is happening in this specific triage flow:

* The Source Evidence: The pipeline originates from a single piece of initial evidence on the left, in this case, a raw disk image (2020JimmyWilson.E01).
* Targeted & Parallel Extraction: The workflow branches out to perform specific, concurrent extractions. The top branch pulls Windows Event Logs (WindowsEventLogs), while the bottom branch targets a suspicious executable (setup.exe).
* Automated Tool Chaining: Once the files are extracted, they are automatically handed off to the right tools. The event logs are fed into Hayabusa (generating HTML reports and CSV timelines) and Plaso. Simultaneously, setup.exe is routed to Capa for malware analysis and a Strings extraction for basic analysis.
* The Timesketch Handoff: Trailing the Hayabusa node, you can see Upload to Timesketch flow. As soon as the timeline is generated, OpenRelik pushes the data directly into Timesketch, eliminating the manual download/upload step.
* Granular Visibility: Selecting any node, like the highlighted Plaso Psort CSV task; gives you a transparent view of the exact command executed (psort.py), how long it took to run, and the resulting output file (a 27.25MB CSV), which is ready for immediate download.

Finally, because these processes are highly repeatable, you can use the Save workflow as a template feature. This allows you to standardize workflows and deploy this exact triage pipeline for future investigations with just a few clicks.

### A Growing Ecosystem of Specialized Workers

The true power of OpenRelik lies in its extensible, containerized worker architecture. Instead of relying on a monolithic application, you can construct your workflows using a diverse library of specialized forensic tools.

![](https://blogger.googleusercontent.com/img/a/AVvXsEiRqvPZS7rdF-XsU9f9vhllBwWatWJdJxChP01x9IHA52-jYSLqu-wc5LpA8vWTjU76FkDGkWIdoThkZYOqAmX_fXsQVLE_y0VhMd_NOdIFHlBFgvyd9vjm4W4bezGfmxtQy6Z3PgqHDt1q-UquJoT77_hWBM2ZjtAWb6aIkMQsmbzM5GHYYy4WPDqdxAlv)

As shown in the marketplace view above, the ecosystem supports a wide range of DFIR tasks out of the box, including:

* Timeline Generation: Create super timelines from disk images using Plaso, or parse Windows event logs with Hayabusa.
* Malware & Binary Analysis: Detect capabilities in suspicious executables with Capa, or extract and deobfuscate strings using the FLARE Obfuscated String Solver (FLOSS).
* Data Extraction & Export: Pull structured information with **b**ulk\_extractor, or seamlessly push your processed timelines directly into Timesketch.
* Utility & AI Integrations: Leverage utility workers like Grep for pattern matching, or use the LLM Prompter to run automated prompts against parsed text files.

Because each worker operates independently within its own sandbox, adding new tools or updating existing ones won't disrupt your underlying environment. To explore the ever expanding library of available integrations, head over to the [OpenRelik Workers Page](https://openrelik.org/workers/).

## How does OpenRelik integrate with the OSDFIR stack?

OpenRelik integrates directly with Timesketch; a platform for collaborative forensic timeline analysis. The integration works by allowing processed timelines, typically generated by workers like Plaso or Hayabusa to be sent directly into Timesketch seamlessly from your OpenRelik workflow, avoiding manual data juggling.

When configuring the Upload to Timesketch task, OpenRelik provides a dedicated interface to control how the data lands in Timesketch:

![](https://blogger.googleusercontent.com/img/a/AVvXsEi9KV0i2W-IdgL7QzpNTA8wc39wUyzKE6o9keCJU_rX6HFaAS-R58HyH9ksRt6HAmqwKUBtfetpUQGATUgywifdVq5LrUmsnjaWHyNyM3b1xlTOMVkfkWftitKXFIN9fsaFfA5cBjgFNPMwOo5JOMmzOfQaE2OliqAXAypDWBNm69RLS4yYuYd6CK9h4Kkf)

From this configuration pane, you can:

* Target a Sketch: Choose to append the data to an existing Timesketch Sketch using its numerical ID, or create a new Sketch.
* Customize the Timeline: Set a descriptive name for the incoming timeline to keep your investigations organized.
* Trigger Downstream Analyzers: Pre-select which Timesketch Analyzers (such as browser searches, account finders, or Yeti threat intelligence lookups) should run automatically upon import.
* Note: Additional settings, such as managing access for specific users and groups, are also available further down the configuration menu.

Once saved, this task acts as a seamless bridge at the tail end of your processing chain:

![](https://blogger.googleusercontent.com/img/a/AVvXsEjCQNC8_b14EFI9GHsK9tsBsUY-y8-XSuqpqUYkrObY7ah3F2HNlzr50_F0hXwfOYEsj92a2INjeCji4UiUavnF_Af8zx7KoRgFnnu7vMHvGScPW4aAn_czrgEfZeTqlkY3APty31mUCRE4eD3VrkEA6SCIIB2uRWzzatvguPNGOOH2S6EScF5QZjuYfMJZ)

As shown in this workflow:

* The raw evidence file (artifact\_disk.dd) is processed via Plaso.
* The output (artifact\_disk.dd.plaso) is automatically picked up by the Upload to Timesketch worker.
* The worker triggers the Timesketch Importer Client and displays a direct hyperlink to the active case (e.g., sketch/1).

Clicking the link takes the investigator directly from the data processing stage straight into a fully parsed, indexed, and enriched collaborative timeline interface.

### Looking Ahead: OpenRelik & Yeti Integratio...