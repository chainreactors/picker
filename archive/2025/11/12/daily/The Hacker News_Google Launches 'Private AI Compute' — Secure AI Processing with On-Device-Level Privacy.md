---
title: Google Launches 'Private AI Compute' — Secure AI Processing with On-Device-Level Privacy
url: https://thehackernews.com/2025/11/google-launches-private-ai-compute.html
source: The Hacker News
date: 2025-11-12
fetch_date: 2025-11-13T03:16:06.626515
---

# Google Launches 'Private AI Compute' — Secure AI Processing with On-Device-Level Privacy

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Google Launches 'Private AI Compute' — Secure AI Processing with On-Device-Level Privacy](https://thehackernews.com/2025/11/google-launches-private-ai-compute.html)

**Nov 12, 2025**Ravie LakshmananArtificial Intelligence / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7u0YyGlwQEZFWpce5m9bHa4DibuFf1-votoLyZ6m1wkceOdtkkpGLrjkM9tyYHVQJVZSz5KQvJ9FxxCcr7KFlWm_d9DKdDx84iYRRp7J7rQHYRlAMdhF65AYDLZT_T-FWmwdXzULM-r1oHGTPENO8-oluI3HcVTXYUG3Pu-0m4IEhC0M6PLYVxgt_JWaQ/s2600/google-ai.gif)

Google on Tuesday unveiled a new privacy-enhancing technology called **Private AI Compute** to process artificial intelligence (AI) queries in a secure platform in the cloud.

The company [said](https://blog.google/technology/ai/google-private-ai-compute/) it has built Private AI Compute to "unlock the full speed and power of Gemini cloud models for AI experiences, while ensuring your personal data stays private to you and is not accessible to anyone else, not even Google."

Private AI Compute has been described as a "secure, fortified space" for processing sensitive user data in a manner that's analogous to on-device processing but with extended AI capabilities. It's powered by [Trillium](https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus) Tensor Processing Units (TPUs) and [Titanium](https://cloud.google.com/blog/products/compute/titanium-underpins-googles-workload-optimized-infrastructure) Intelligence Enclaves (TIE), allowing the company to use its frontier models without sacrificing on security and privacy.

In other words, the privacy infrastructure is designed to take advantage of the computational speed and power of the cloud while retaining the security and privacy assurances that come with on-device processing.

Google's CPU and TPU workloads (aka trusted nodes) rely on an AMD-based hardware Trusted Execution Environment (TEE) that encrypts and isolates memory from the host. The tech giant noted that only attested workloads can run on the trusted nodes, and that administrative access to the workloads is cut off. Furthermore, the nodes are secured against potential physical data exfiltration attacks.

The infrastructure also supports peer-to-peer attestation and encryption between the trusted nodes to ensure that user data is decrypted and processed only within the confines of a secure environment and is shielded from broader Google infrastructure.

"Each workload requests and cryptographically validates the workload credentials of the other, ensuring mutual trust within the protected execution environment," Google explained. "Workload credentials are provisioned only upon successful validation of the node's attestation against internal reference values. Failure of validation prevents connection establishment, thus safeguarding user data from untrusted components."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The overall process flow works like this: A user client establishes a [Noise protocol](https://noiseprotocol.org) encryption connection with a frontend server and establishes bi-directional attestation. The client also validates the server's identity using an [Oak](https://github.com/project-oak/oak/tree/main/oak_session) end-to-end encrypted attested session to confirm that it's genuine and not modified.

Following this step, the server sets up an Application Layer Transport Security ([ALTS](https://docs.cloud.google.com/docs/security/encryption-in-transit/application-layer-transport-security)) encryption channel with other services in the scalable inference pipeline, which then communicates with model servers running on the hardened TPU platform. The entire system is "ephemeral by design," meaning an attacker who manages to gain privileged access to the system cannot obtain past data, as the inputs, model inferences, and computations are discarded as soon as the user session is completed.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJV9JM86Hoytab_iCU3bEmKwdpmahIbzNBHu1ZhWwG_U2wd-AZ_S8RsKyEVula7PQYDS5Gr5SLJBOptUdbtdJFjLVBxvNoacrlKlEXdXFtNHp_UWoHCFz8SC5WjMGgK0gaBfsByzMcJeovAD62ArXI3YPEhiMFLt7sH2VAFqAuWT8mZrMO1cDcuGgmj0Az/s2600/google.jpeg) |
| Google Private AI Compute Architecture |

Google has also touted the various protections baked into the system to maintain its security and integrity and prevent unauthorized modifications. These include -

* Minimizing the number of components and entities that must be trusted for data confidentiality
* Using [Confidential Federated Compute](https://github.com/google-parfait/confidential-federated-compute) for collecting analytics and aggregate insights
* Encryption for client-server communications
* [Binary authorization](https://cloud.google.com/docs/security/binary-authorization-for-borg) to ensure only signed, authorized code and validated configurations are running across its software supply chain
* Isolating user data in Virtual Machines (VMs) to contain compromise
* Securing systems against physical exfiltration with memory encryption and input/output memory management unit ([IOMMU](https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit)) protections
* Zero shell access on the TPU platform
* Using IP blinding relays operated by third-parties to tunnel all inbound traffic to the system and obscure the true origin of the request
* Isolating the system's authentication and authorization from inference using [Anonymous Tokens](https://github.com/google/anonymous-tokens)

NCC Group, which has conducted an [external assessment](https://www.nccgroup.com/research-blog/public-report-google-private-ai-compute-review/) of Private AI Compute between April and September 2025, said it was able to discover a timing-based side channel in the IP blinding relay component that could be used to "unmask" users under certain conditions. However, Google has deemed it low risk due to the fact that the multi-user...