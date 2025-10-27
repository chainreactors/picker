---
title: Google Cloud Platform Data Destruction via Cloud Build
url: https://blog.talosintelligence.com/gcp-data-destruction-via-cloud-build/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-07
fetch_date: 2025-10-06T20:39:45.699370
---

# Google Cloud Platform Data Destruction via Cloud Build

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Google Cloud Platform Data Destruction via Cloud Build

By
[Darin Smith](https://blog.talosintelligence.com/author/darin/)

Thursday, February 6, 2025 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[Threats](https://blog.talosintelligence.com/category/threats/)

### Background & Public Research

Google Cloud Platform (GCP) [Cloud Build](https://cloud.google.com/build/docs/overview) is a Continuous Integration/Continuous Deployment (CI/CD) service offered by Google that is utilized to automate the building, testing and deployment of applications. Orca Security [published an article](https://orca.security/resources/blog/bad-build-google-cloud-build-potential-supply-chain-attack-vulnerability/) describing certain aspects of the threat surface posed by this service, including a supply chain attack vector they have termed “Bad.Build”. One specific issue they identified, that Cloud Build pipelines with the default Service Account (SA) could be utilized to discover all other permissions assignments in a GCP project, was resolved by Google after Orca reported it. The general threat vector of utilizing Cloud Build pipelines to perform malicious actions, however, is still present. A threat actor with just the ability to submit and run a Cloud Build job (in other words, who has the *cloudbuild.builds.create* permission) can execute any *gcloud* GCP command line interface (CLI) command that the Cloud Build SA has the permissions to perform. A threat actor could perform these techniques either by obtaining credentials for a GCP user or SA [(Mitre ATT&CK T1078.004)](https://attack.mitre.org/techniques/T1078/) or by pushing or merging code into a repository with a Cloud Build pipeline configured [(Mitre T1195.002)](https://attack.mitre.org/techniques/T1195/002/). Orca Security focused on utilizing this threat vector to perform a supply chain attack by adding malicious code to a victim application in GCP Artifact Registry. Talos did not extensively examine this technique since Orca’s research was quite comprehensive, but confirmed it is still possible.

### Original Research

Cisco Talos research detailed below focused on malicious actions enabled by the *storage.\** permission family, while the original Orca research detailed a supply chain attack scenario enabled by the *artifactregistry.\** permissions. Beyond the risk posed by the default permissions, any additional permissions assigned to the Cloud Build SA could potentially be leveraged by a threat actor with access to this execution vector, which is an area for potential future research. While Orca mentioned that a Cloud Build job could be triggered by a merge event in a code repository, in their article they utilized the *gcloud* Command Line Interface (CLI) tool to trigger the malicious build jobs they performed. Talos meanwhile utilized commits to a GitHub repository configured to trigger a Cloud Build job, since this is a form of Initial Access vector that would allow a threat actor to target GCP accounts without access to an identity principal for the GCP account.

Unlike the Orca Security findings, Talos does not assess that the attack path illustrated in the following research represents a vulnerability or badly architected service. There are legitimate business use cases for every capability and default permission that we utilized for malicious intent, and Google has provided robust security recommendations and defaults. This research, instead, should be taken as an instructive illustration of the risks posed by these capabilities for cloud administrators who may be able to limit some of the features that were misused if they are not needed in a particular account. It can also be a guide for security analysts and investigators who can monitor the Operations Log events identified, threat hunt for their misuse, or identify them in a post-incident incident response workflow.

### Defensive Recommendations Summary

Talos recommends creating an anomaly model-style threat detection for the default Cloud Build SA performing actions that are not standard for it to execute in a specific environment. As always, properly applying the principle of least privilege by assigning Cloud Build a lower privileged Service Account with just the permissions needed in a particular environment will also reduce the threat surface identified here. Finally, review the configuration applied to any repositories that can trigger Cloud Build or other CI/CD service jobs, require manual approval for builds triggered by Pull Requests (PRs) and avoid allowing anyone to directly commit code to GitHub repositories without a PR. More details on all three of these topics are described below.

## Lab Environment Setup

Talos has an existing Google Cloud Platform lab environment utilized for offensive security research. Within that environment, a [Cloud Storage](https://cloud.google.com/storage/docs/introduction) bucket was created and the Cloud Build Application Programming Interface (API) were enabled. Additionally, a target GitHub repository was created; For research purposes, this repository was set to private, but an actual adversary would likely take advantage of a public repository in most cases. The Secrets Manager API is also needed for Cloud Build to integrate with GitHub, so that was also enabled. These actions can be performed using the [*gcloud*](https://cloud.google.com/sdk/gcloud) and GitHub [*gh*](https://cli.github.com/)CLI tools using the following commands:

```
gcloud storage buckets create BUCKET_NAME --location=LOCATION --project=PROJECT_ID
gcloud services enable cloudbuild.googleapis.com --project=PROJECT_ID\
gcloud services enable secretmanager.googleapis.com --project=PROJECT_ID
gh repo create REPO_NAME --private --description "Your repository description"
``...