---
title: Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 2 – Execution
url: https://blog.nviso.eu/2026/11/04/detection-engineering-implementing-detection-as-code-in-an-existing-environment-part-2-execution/
source: NVISO Labs
date: 2026-11-04
fetch_date: 2026-11-05T08:43:39.225557
---

# Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 2 – Execution

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/prevent/application-security/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 2 – Execution

[Felix Hartmond](https://blog.nviso.eu/author/felix-hartmond/)

[Blue Team](https://blog.nviso.eu/category/detect/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

November 4, 2026November 4, 2026
10 Minutes

This entry is part 2 in the series [Detection Engineering: Implementing Detection-as-Code in an Existing Environment](https://blog.nviso.eu/series/detection-engineering-implementing-detection-as-code-in-an-existing-environment/ "Detection Engineering: Implementing Detection-as-Code in an Existing Environment")

---

In Part 1, we described the starting position and roadmap for introducing Detection-as-Code in an existing environment, this second part explains how we executed that roadmap.

Some of the content in this part of the series is rather technical. If you are not a technical reader, feel free to skim this part, but do not miss Part 3, which returns to conceptual and strategic topics.

## Preparation

The documents associated with a detection, but not directly part of its implementation, were intended to be machine-readable. In practice, however, many were not. The issues ranged from character-encoding problems and indentation errors to random null bytes in files. Furthermore, some files did not comply with the intended schema because keys were missing or incorrect.

This did not cause significant problems in the old process. The documents were written, sometimes in plain-text editors without syntax highlighting, placed on file shares, and left there. In the new setup, however, the repository was intended to become the central single source of truth. All documents therefore needed to be parseable so that their correctness could be validated. Their contents were also required to execute the migration; for example, the metadata documents contained paths to the Atomic Red Team tests.

To systematically correct these documents, we implemented a parsing library containing functions to read the different file types, validate them against a defined schema using `strictyaml` and `jsonschema`, and return the parsed results. These functions were used throughout the migration and later in automations.

Using these parsers, we attempted to parse all files and identified issues requiring correction. While some issues could be addressed semi-automatically with scripts, for example by identifying and converting encodings, many had to be corrected manually, file by file.

Because the existing deployment procedures required detection data in platform-specific formats, we needed tooling to generate those formats. For Splunk, this meant an `apps` directory that could be copied to the Splunk infrastructure.

For Splunk, the process was relatively straightforward. The configuration files for a Splunk app, namely `savedsearches.conf`, `transforms.conf`, and `macros.conf`, could be created by concatenating the corresponding snippets, `splunk-searches.conf`, `splunk-transforms.conf`, and `splunk-macros.conf`, from all active detections assigned to a specific app. Lookup files were copied unchanged to the `lookups` folder of the relevant app.

In the customer environment, Splunk detections were distributed across different Splunk apps based on their categories. The deployment script therefore iterated through all detection folders in the new repository, determined the target app from the data in `meta.yml`, and added the relevant configuration snippets and files to that app. Folders containing detections targeting platforms other than Splunk were skipped.

Deployment scripts for the other platforms were created in the same way. They used the new detection repository as input and, without requiring additional parameters, generated the artefacts expected by the existing deployment processes.

We also created a script for Atomic Red Team tests because the framework expects each test to be stored in a separate folder with a specific name. The script built the required path from information in `meta.yml` and copied the contents of each test file to the required location.

After preparing the current data for the migration and the tooling required to continue deployment after the migration, the next step was to focus on the migration itself. The migration was scripted using Jupyter notebooks, which used the previously implemented parsers and operating-system libraries to copy, move, and edit files. The detailed migration process is covered in the next section.

With the scripted migration and the CLI tools, we performed multiple dry runs. For each dry run, we executed the migration locally on a copy of all data and used the developed CLI tools to regenerate the deployment artefacts, which were expected to match the current data structure. Comparing the generated artefacts with the pre-migration data enabled us to identify and fix open issues, such as incorrect filenames or references in metadata files, until the generated artefacts matched the initial input.

Lastly, before starting the short repository freeze and executing the migration in production, we prioritised completing as many ongoing developments as possible and merging their feature branches into the main branch. This reduced the necessary cleanup work after the migration, as the migration covered only the main branches. Feature branches no longer matched the repository structure after the migration and therefore required their diffs to be migrated manually.

## Execution of the Data Restructuring

Because some data had already been stored and tracked in Git repositories for some time, we wanted to preserve its history in full. We therefore needed to perform all moves in a way that Git could trace the history. Git does not store file moves directly; instead, it infers them by comparing file versions. We therefore structured the migration so that Git could recognise moved files rather than treat them as entirely new ...