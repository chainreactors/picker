---
title: Duping Cloud Functions: An emerging serverless attack vector
url: https://blog.talosintelligence.com/duping-cloud-functions-an-emerging-serverless-attack-vector/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-21
fetch_date: 2025-10-06T22:29:17.472465
---

# Duping Cloud Functions: An emerging serverless attack vector

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

![](/content/images/2025/05/Duping-Cloud-Functions.jpg)

# Duping Cloud Functions: An emerging serverless attack vector

By
[William Charles Gibson](https://blog.talosintelligence.com/author/william/)

Tuesday, May 20, 2025 06:00

[Vulnerability Spotlight](/category/vulnerability-spotlight/)

## Summary and background

Google Cloud Platform (GCP) [Cloud Functions](https://cloud.google.com/functions#documentation) are event-triggered, serverless functions that automatically scale and execute code in response to specific events like Hypertext Transfer Protocol (HTTP) requests or data changes. Tenable Research published an [article](https://www.tenable.com/blog/confusedfunction-a-privilege-escalation-vulnerability-impacting-gcp-cloud-functions) discussing a vulnerability they discovered within GCP’s Cloud Functions serverless compute service and its Cloud Build continuous integration and continuous delivery or deployment (CI/CD) pipeline service.

“When a GCP user creates or updates a Cloud Function, a multi-step backend process is triggered,” Tenable author Liv Matan writes. “This process, among other things, attaches a [default Cloud Build service account](https://cloud.google.com/build/docs/cloud-build-service-account) to the Cloud Build instance that is created as part of the function’s deployment.” This default Cloud Build Service Account (SA) previously gave users excessive Cloud Function permissions. An attacker who has gained the ability to create or update a cloud function could utilize the function’s deployment process to escalate privileges to the default Cloud Build service account or assign a higher privileged SA. Google has since partially addressed Tenable’s discovery to ensure the default Cloud Build service account no longer provides users with excessive permissions.

Based on Tenable’s research, Cisco Talos conducted a series of offensive tests within Cisco’s Google Cloud Platform (GCP) to identify additional threats that may affect customer environments.

During its research, Talos discovered that the technique Tenable identified could be adapted to perform other malicious activities. By implementing different malicious console commands into the Node Package Manager (NPM) ‘package.json’ file used in this technique, threat actors could execute behaviors such as environment enumeration.

Talos furthered this research by attempting to replicate similar behaviors in Amazon Web Services (AWS) and Microsoft Azure to determine if these techniques could be employed to perform similar malicious activities in other cloud-based environments.

## Research

### Prerequisites

To utilize this attack vector, certain prerequisites must be met. Talos set up a Debian Linux server within the GCP environment with Node Package Manager (NPM) and Ngrok installed. However, the virtual machine for this research can be created in any cloud environment.

![](https://blog.talosintelligence.com/content/images/2025/05/carbon.png)

After installing NPM and Ngrok, Talos configured both tools to function as intended.

![](https://blog.talosintelligence.com/content/images/2025/05/carbon2.png)

Once NPM and Ngrok were configured, a Python server was created to output the data received from the cloud function.

![](https://blog.talosintelligence.com/content/images/2025/05/carbon4.png)

With NPM, Ngrok, and the Python server set up and configured, the next step was to create and modify the NPM package.

![](https://blog.talosintelligence.com/content/images/2025/05/carbon--1-.png)

Talos then replaced the content of the package.json file with the following code:

![](https://blog.talosintelligence.com/content/images/2025/05/carbon--2-.png)

Finally, once all the necessary files are created and configured, Talos set up the environment to visually display the data output from deploying the functions. To achieve this, Talos activated both the Ngrok server and the Python server created earlier.

![](https://blog.talosintelligence.com/content/images/2025/05/carbon--3-.png)

To replicate the GCP behavior discussed in Tenable’s article, Talos created/updated an SA with function build and cloud build permissions. This SA was then assigned to the GCP Cloud Run Function to allow the code to be executed with privileged access.

Once the servers and service accounts were online and configured to receive and output data, the emulation of the behavior could begin.

### Emulation

With the package.json file configured to be utilized by the build function, Talos began emulating the technique described in Tenable’s research article.

The first step in Talos’ replication involved the utilizing a misconfigured GCP function to extract the default Cloud Build service account token. To initiate this process, the "malicious" package.json was updated on the virtual machine, ensuring that it contains code similar to that used by Tenable.

![](https://blog.talosintelligence.com/content/images/2025/05/carbon--4-.png)

Once the package.json file was modified as desired, it needed to be published to the public NPM registry. To do this, Talos executed the following command:

![](https://blog.talosintelligence.com/content/images/2025/05/carbon--5-.png)

With the package.json file uploaded to the NPM public registry, it was time to deploy the GCP Cloud Run Function so that the package.json can execute the provided code. To do this, the user must to navigate to their GCP Cloud Run Functions page and select or create a Cloud Run Function, ensuring it is assigned a service account with Cloud Build permissions.

![](https://blog.talosintelligence.com/content/images/2025/05/data-src-image-dc0a0e8b-b378-4e15-b2bd-a766be4a42ed.png)

Figure 1. Google Cloud Run Function displaying the assigned service account.

As Talos created or selected our existing GCP Cloud Run Function, we navigated to the s...