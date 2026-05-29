---
title: Deepfake Forensics Workflow for Image Analysis
url: https://blog.ampedsoftware.com/2026/05/27/deepfake-forensics-workflow-for-image-analysis
source: Instapaper: Unread
date: 2026-05-28
fetch_date: 2026-05-29T06:06:37.829893
---

# Deepfake Forensics Workflow for Image Analysis

[Skip to main content](#main)

[![Amped Blog](https://blog.ampedsoftware.com/wp-content/uploads/2023/04/logo_w400.png)](https://ampedsoftware.com "Amped Blog")
/
[Blog](https://blog.ampedsoftware.com)

* [Amped Blog Home](https://blog.ampedsoftware.com "Amped Blog Home")
* [Posts by Category](https://blog.ampedsoftware.com/posts-by-category "Posts by Category")
* [Archive](https://blog.ampedsoftware.com/archive "Archive")
* [Contact Us](https://ampedsoftware.com/contacts "Contact Us")

* [How to Amped Authenticate](https://blog.ampedsoftware.com/category/how-tos/how-to-amped-authenticate)

# Deepfake Forensics Workflow for Image Analysis

![](https://secure.gravatar.com/avatar/3fd6f8f549aedd79b88f459840c9fffda4bdc90ee3e969a10e783af1688b216e?s=450&d=mm&r=g)Massimo Iuliani

May 27, 2026

Reading time:  8 min

*Analyzing suspected deepfakes requires more than detection alone. This post explains a forensically sound workflow for image and video analysis that helps investigators produce findings that are explainable, reproducible, and defensible.*

![Deepfake forensics workflow for image analysis](https://blog.ampedsoftware.com/wp-content/uploads/2026/05/image4.jpg)

The research community developed several tools for detecting and analyzing deepfakes under various circumstances. But **where should a practitioner begin when an image is suspected of being a deepfake?**

**Contents**
hide

[Key Takeaways](#Key_Takeaways)

[Watch the Podcast Episode: Beyond the Deepfake Detection Button](#Watch_the_Podcast_Episode_Beyond_the_Deepfake_Detection_Button)

[How to Analyze a Suspected Deepfake: A Forensically Sound Workflow](#How_to_Analyze_a_Suspected_Deepfake_A_Forensically_Sound_Workflow)

[Why AI-based Detection Should Be Used for Triage, Not Evidence](#Why_AI-based_Detection_Should_Be_Used_for_Triage_Not_Evidence)

[Metadata Analysis in Deepfake Forensics](#Metadata_Analysis_in_Deepfake_Forensics)

[Format Analysis: JPEG vs Non-JPEG](#Format_Analysis_JPEG_vs_Non-JPEG)

[Using Geometric Analysis to Detect Inconsistencies](#Using_Geometric_Analysis_to_Detect_Inconsistencies)

[Conclusion](#Conclusion)

[FAQ: Deepfake Forensics Workflow](#FAQ_Deepfake_Forensics_Workflow)

In this post, we outline a scientific workflow and the underlying reasoning required to analyze an image or video. This workflow is based on a forensically sound methodology designed not just to detect manipulation, but to produce evidence through an approach that is explainable, reproducible, and defensible. Before starting: note that this post is written for forensic practitioners who are already familiar with the fundamentals of digital imaging and core forensic approaches.

The analysis generally starts from the “naive” question: “**Is it a deepfake**?”
However, to a forensic expert, the technical interpretation is much broader.
For this specific talk, we will consider the detection of generated images and natural images modified through AI technologies, i.e., the image is “contaminated” in some way with AI-based editing techniques.

## Key Takeaways

* **Deepfake analysis should follow a forensically sound workflow**, not a single-tool detection approach.
* The goal is to identify possible manipulation and to produce findings that are **explainable, reproducible, and defensible**.
* A robust workflow combines **AI-based triage, metadata inspection, format analysis, geometric checks, and pixel-level analysis**.
* **AI detection alone is not evidential** and should be treated as a starting point for further forensic examination.
* Scientific image and video analysis depends on **methodology, validation, and consistency**, especially when results may need to support an investigation or legal process.
* **A structured forensic workflow helps analysts turn an initial AI flag into documented, corroborated, and defensible findings.**

## Watch the Podcast Episode: Beyond the Deepfake Detection Button

Want to go deeper into the reasoning behind this workflow?

In this episode of the Amped Podcast, “***Deepfake Forensics: Beyond the Deepfake Detection Button***”, we discuss why suspected AI-generated or AI-manipulated media cannot be assessed with a single detector alone.

The conversation explores how forensic practitioners can combine AI-based triage with metadata, format, compression, geometric, and pixel-level analysis to build explainable and defensible findings.

## How to Analyze a Suspected Deepfake: A Forensically Sound Workflow

A forensically sound deepfake analysis should follow a structured process. In practice, the workflow can include these stages:

1. **AI-based triage (non-evidential)**
   Use AI tools as an initial screening step to flag possible signs of manipulation. These results can help prioritize analysis, but they should not be treated as evidence on their own.
2. **Metadata and container inspection**
   Examine file metadata, codec information, timestamps, software markers, and container structure to identify inconsistencies, processing history, or signs of re-encoding.
3. **Compression analysis**
   Assess whether the image has been compressed twice or exposes local compression inconsistencies.
4. **Geometric consistency checks**
   Evaluate whether spatial relationships in the image or video are physically plausible, including perspective, proportions, facial alignment, lighting direction, and scene geometry.
5. **Image-domain forensic checks**
   Analyze pixel-level and signal-level characteristics such as noise patterns, compression traces, local artifacts, resampling indicators, and other statistical anomalies.
6. **Cross-validation of findings**
   Compare results across methods rather than relying on a single indicator. A defensible conclusion should be supported by converging evidence from multiple forensic techniques.
7. **Documentation and reproducibility**
   Record each analytical step, tool, assumption, and result so that the examination can be explained, reproduced, and defended if challenged.

## Why AI-based Detection Should Be Used for Triage, Not Evidence

The first single-shot weapon in our arsenal is “using AI to fight AI”.AI-based tools are excellent for triage but are not forensically reliable as standalone evidence due to limited explainability (see our related [post](https://blog.ampedsoftware.com/2025/08/05/deepfake-forensics) for why).

They are particularly useful when processing large datasets: In front of a massive amount of images, the manual inspection of each piece of media can be unfeasible.  The batch analysis of the data, instead, can make the selection of relevant content easier and faster. In this case, a tool that automatically flags synthetic-generation clues can be a game-changer for the analyst in terms of processing time.

In practice, they act as an initial filter, helping analysts prioritize which content requires deeper forensic inspection.

![AI-generated image of a girl](https://blog.ampedsoftware.com/wp-content/uploads/2026/05/image10.png)

In the example above, the **Authenticate Diffusion Model Detection filter triggers a red flag! This suggests the image was likely generated by an AI tool**. However, while this filter has a low false-alarm rate on photorealistic images, AI-based results alone cannot stand up in court.

## Metadata Analysis in Deepfake Forensics

Another check that can lead to a “quick win” is the analysis of metadata and file format information. In certain instances, the traces of a generative system are stored directly within the textual metadata. See, for instance, the following examples:

![Screenshot of metadata fields showing “Item0When” with the timestamp “2023-11-24T16:21:06Z” and “Item0Description” labeled as “AI Generated Image.”](https://blog.ampedsoftware.com/wp-content/uploads/2026/05/image8-1.png)

![Screenshot of metadata fields showing “Claim_generator” set to “Microsoft Responsible AI/1.0” and “Claim_Generator_InfoName” set to “Microsoft Responsible AI Image Provenance.”](https://blog.am...