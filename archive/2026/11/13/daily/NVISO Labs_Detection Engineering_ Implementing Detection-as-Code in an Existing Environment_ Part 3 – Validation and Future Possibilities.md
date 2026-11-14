---
title: Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 3 – Validation and Future Possibilities
url: https://blog.nviso.eu/2026/11/13/detection-engineering-implementing-detection-as-code-in-an-existing-environment-part-3-validation-and-future-possibilities/
source: NVISO Labs
date: 2026-11-13
fetch_date: 2026-11-14T08:20:31.445924
---

# Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 3 – Validation and Future Possibilities

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

# Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 3 – Validation and Future Possibilities

[Felix Hartmond](https://blog.nviso.eu/author/felix-hartmond/)

[Blue Team](https://blog.nviso.eu/category/detect/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

November 13, 2026November 13, 2026
8 Minutes

This entry is part 3 in the series [Detection Engineering: Implementing Detection-as-Code in an Existing Environment](https://blog.nviso.eu/series/detection-engineering-implementing-detection-as-code-in-an-existing-environment/ "Detection Engineering: Implementing Detection-as-Code in an Existing Environment")

---

In Part 2, we described how we restructured the data to move all detection data into the new repository while preserving the existing Git history.

In this third part, we examine data quality and the use of the data beyond the internal needs of the Detection Engineering team. We cover how systematic validation improved data quality, the first practical uses of the consolidated data, larger planned initiatives, and future opportunities to further improve and automate the Detection Engineering process.

## Consistency Validation

At this point, all detection data had been successfully consolidated in the new repository. The format of the different files was largely kept unchanged to make the migration as easy as possible for detection developers and to avoid introducing additional friction. This also means that some information is stored in multiple files. For example, platform and severity levels are stored in both the metadata file and the implementation, while title and description are stored in the metadata file, the implementation, and the Atomic Red Team test definition.

This is not inherently problematic; the data had been structured this way for a long time. However, it creates issues when the different files contain inconsistent values. If the metadata file states a different severity from that in the actual implementation, analyses and reports based on the metadata files are incorrect. Therefore, such inconsistencies needed to be identified and corrected, and we needed to ensure that no new inconsistencies would be introduced into the repository.

To accomplish this, a validator was implemented. This validator contains numerous test cases that check files against defined requirements. These checks cover different questions:

* Whether files are parseable, preventing malformed files from breaking other scripts and automations.
* Whether files fulfil the defined schema, identifying missing, misspelled, or surplus keys.
* Whether values stored in multiple files are consistent.

The checks are divided into different levels:

* `required`: These checks must always pass.
* `required_on_change`: These checks must pass when a detection is modified; for existing, unchanged detections, they are considered optional.
* `optional`: These checks create remarks for the developer but do not block a change.

The differentiation between these levels makes the initial improvement of consistency manageable. While some issues need to be fixed before the data can be relied upon, such as severity values, MITRE ATT&CK IDs, and platforms, other data should be consistent long-term but would require too much effort to correct in a single step. Their inconsistency does not cause immediate problems, for example where Atomic Red Team test cases do not match a naming schema. These non-urgent checks become mandatory once a developer modifies the affected detection; until then, they remain optional.

Furthermore, there are scenarios in which fields that are usually identical differ for legitimate reasons. For example, some descriptions contain variables in the implementation that are populated in the Splunk UI, while the description in the metadata document remains generic.

The validator is built as a library that is used in two ways.

Firstly, it is available as a CLI tool. This tool has parameters that define which levels of checks to report. With this tool, we identified inconsistencies and corrected them manually. This sometimes required research in old tickets to determine which of two values for a field was correct, as an error could have been introduced either when defining the metadata file or when implementing the detection.

Secondly, validation is integrated into the development process through CI pipelines. When a pull request is opened, the CI pipeline runs the validation checks on the detection folders included in the pull request changeset. The result and detailed output are displayed in a GitHub check in the pull request to provide direct feedback to the detection developer. If any `required` or `required_on_change` checks fail, the pull request is automatically blocked from merging. When optional checks fail, the output is displayed in the check, but the pull request is not blocked. This ensures that the data in the repository remains consistent over the long term and that non-urgent inconsistencies are corrected over time.

## Automations, Reports and Other Integrations

At this point, we had achieved several important results:

* We designed a new data structure tailored to the workflows of the Detection Engineering team.
* We reorganized the existing data into this new structure.
* We migrated additional information scattered across manually updated Excel files and reports into the repository.
* We removed existing inconsistencies in the data and technically ensured that no new inconsistencies are introduced during the development process.

This allowed us to establish the Git repository as the single source of truth for all detection-related data. The validator also ensures consistency across all files in the repository – for example, between the metadata documents and the corresponding technical implementations. As a result, the metadata documents can be used reliably for analysis and reporting, as they consistently...