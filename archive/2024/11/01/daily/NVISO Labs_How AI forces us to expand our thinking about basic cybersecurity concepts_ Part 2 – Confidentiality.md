---
title: How AI forces us to expand our thinking about basic cybersecurity concepts: Part 2 – Confidentiality
url: https://blog.nviso.eu/2024/10/31/how-ai-forces-us-to-expand-our-thinking-about-basic-cybersecurity-concepts-part-2-confidentiality/
source: NVISO Labs
date: 2024-11-01
fetch_date: 2025-10-06T19:15:59.804937
---

# How AI forces us to expand our thinking about basic cybersecurity concepts: Part 2 – Confidentiality

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# How AI forces us to expand our thinking about basic cybersecurity concepts: Part 2 – Confidentiality

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[Artifical Intelligence](https://blog.nviso.eu/category/artifical-intelligence/)

October 31, 2024November 19, 2024
6 Minutes

## Introduction

[In the first part of this mini-series](https://blog.nviso.eu/2024/10/30/how-ai-forces-us-to-expand-our-thinking-about-basic-cybersecurity-concepts-part-1-introduction/), we explored briefly what kind of impacts AI may have on the CIA Triad and whether we should adjust this fundamental framework. The goal of this and subsequent blogposts is assessing the pillars of the proposed Information Security Hexagon, starting with Confidentiality.

Maintaining confidentiality in Artificial Intelligence (AI) systems leveraging Machine Learning (ML) introduces new challenges. However, the purpose of Confidentiality remains unchanged: ensuring sensitive information is protected from unauthorised access and exposure.

This post distinguishes three separate pillars of Confidentiality in AI implementations: Access Control, Accurate Training, and Intellectual Property Protection. Access Control and Intellectual Property Protection are well-established concepts, but they require a revision when talking about AI. With ML models being used in AI, the Accurate Training of these models also increases in importance. The considerations made require organisations to rethink their current approach to Confidentiality.

## Revised pillars for Confidentiality

### Access Control

Solid access control to systems, applications and databases is a long-established foundation of cybersecurity. Consequently, these same controls should be applied to AI applications and their associated training and production datasets. However, embedding confidentiality in AI systems requires stepping up access control mechanisms. This pertains to data access rights granted to AI systems.

A core principle consists of limiting data access for AI systems to the one granted to its users. Excessive access by AI systems quickly leads to undesired data propagation. Consider, for example, the scenario where an employee uses an organisational AI tool to gather basic information on specific clients. If the tool enjoys broader access rights than the employee, it could implicitly or unintentionally expose confidential data the employee is not authorised to view, thereby creating a breach in confidentiality.

Aligning AI system access rights with user access rights may therefore limit the quality and depth of the AI system’s responses, as it has to base its conclusions on the dataset accessible by the user, thereby limiting its potential. This may not only be the case in production systems, but also during the training of a ML model. If such a model is trained on a broader set of data, some of them not accessible by its users, it could present findings or derive conclusions that could never be reached by its users. In this case, the concept of Confidentiality is not limited to unwanted access or exposure, but also covers the possible findings or conclusions that can only be derived by assessing confidential data.

### Accurate Training

ML models require training, often with large datasets. These should be correctly prepared, to ensure they do not contain confidential information, which could later leak as it was formally absorbed by the model during its training process.

Imagine a hospital trains a ML model to predict the likelihood of patients developing certain medical conditions based on their medical history, lab results, and/or other medical information. The training dataset consists of numerous entries containing sensitive patient information, such as diagnoses, treatment plans, and outcomes. The hospital then offers access to this model to external healthcare providers for a fee. When submitting a patient’s details, the model provides a confidence score/probability of the patient developing a specific condition.

An attacker, knowing some medical history of a specific individual, could attempt to perform a membership inference attack. This attack involves determining whether the individual’s information was included in the original training dataset of the ML model by providing the individual’s known information to the model and looking at confidence scores of the development of a certain condition. Superficially, this knowledge may not cause harm, but deeper analysis shows more reason for concern. High confidence scores indicate that the individual’s medical information might have been part of the training dataset, through which an attacker can infer that the person has a relationship with the hospital. Furthermore, the confidence score can indicate that the individual might be suffering from certain medical conditions. All of this information could be exploited further to uncover more sensitive data, such as specific diagnoses, treatment regimens, or even genetic information.

The example above is completely fictitious, as hospitals are not likely using any production data when training ML models. Not using production data to train models is the best remedy to privacy protection.

However, certain production data, generated in large volumes with wide diversity, might be highly interesting to train ML models with. This is, for example, the case for health statistics obtained from hospitals and public health records. This data could enable a ML model to predict future trends. In this case, simply not using the data needs to be balanced against the potential benefits of improved healthcare outcomes and public health interventions.

If direct production data is used, anonymisation techniques and overfitting prevention are essential prerequisites to prevent unwanted privacy leaks as much as possible. The former involves masking personal data so that individuals cannot be directly or indirectly identified. This can, for example, be done by adding “noise” to training datasets or by using fictive personae with distinctive profile elements. Preferably, any real-world information is only used in training datasets if it has been sufficiently scrubbed to prevent unintended leakage. Overfitting can be avoided by limiting the presence of redundant model features or by splitting a large data set of masked data, one part for tr...