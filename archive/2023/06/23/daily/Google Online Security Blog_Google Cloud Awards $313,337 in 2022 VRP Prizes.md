---
title: Google Cloud Awards $313,337 in 2022 VRP Prizes
url: http://security.googleblog.com/2023/06/google-cloud-awards-313337-in-2022-vrp.html
source: Google Online Security Blog
date: 2023-06-23
fetch_date: 2025-10-04T11:44:23.844841
---

# Google Cloud Awards $313,337 in 2022 VRP Prizes

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Google Cloud Awards $313,337 in 2022 VRP Prizes](https://security.googleblog.com/2023/06/google-cloud-awards-313337-in-2022-vrp.html "Google Cloud Awards $313,337 in 2022 VRP Prizes")

June 22, 2023

Anthony Weems, Information Security Engineer

2022 was a successful year for Google's Vulnerability Reward Programs (VRPs), with over 2,900 security issues identified and fixed, and over $12 million in bounty rewards awarded to researchers. A significant amount of these vulnerability reports helped improve the security of [Google Cloud](http://cloud.google.com) products, which in turn helps improve security for our users, customers, and the Internet at large.

We first [announced](https://security.googleblog.com/2019/08/awarding-google-cloud-vulnerability.html) the Google Cloud VRP Prize in 2019 to encourage security researchers to focus on the security of Google Cloud and to incentivize sharing knowledge on Cloud vulnerability research with the world. This year, we were excited to see an increase in collaboration between researchers, which often led to more detailed and complex vulnerability reports. After careful evaluation of the submissions, today we are excited to announce the winners of the 2022 Google Cloud VRP Prize.

2022 Google Cloud VRP Prize Winners

1st Prize - $133,337: Yuval Avrahami for the report and write-up [Privilege escalations in GKE Autopilot](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/). Yuval's excellent write-up describes several attack paths that would allow an attacker with permission to create pods in an Autopilot cluster to escalate privileges and compromise the underlying node VMs. While these VMs are accessible to customers in GKE Standard, this research led to several [hardening improvements](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2022-009) in Autopilot that make it a better [secure-by-default](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security) Kubernetes offering.

2nd Prize - $73,331: Sivanesh Ashok and Sreeram KL for the report and write-up [SSH Key Injection on GCE](https://blog.stazot.com/ssh-key-injection-google-cloud/). Their write-up describes the journey of discovering a vulnerability that would allow an attacker to gain access to a user's GCE VM by tricking them into clicking a link. They demonstrate the importance of persistence and turned a strange behavior in user creation into an injection of arbitrary SSH public keys.

3rd Prize -  $31,337: Sivanesh Ashok and Sreeram KL for the report and write-up [Bypassing Authorization in Cloud Workstations](https://blog.stazot.com/auth-bypass-in-google-cloud-workstations/). Their write-up describes their research process for analyzing Cloud Workstations and then a full-chain exploit to steal a user's access token by abusing the format of an OAuth state parameter.

4th Prize - $31,311: Sreeram KL and Sivanesh Ashok for the report and write-up [Client-Side SSRF to Google Cloud Project Takeover](https://blog.geekycat.in/client-side-ssrf-to-google-cloud-project-takeover/). Their write-up combines a client-side SSRF, a CSRF bypass, and a clever 3xx redirect by "deactivating" a Feedburner proxy. An attacker could use this vulnerability to steal a Vertex AI user's access token by tricking them into clicking a link.

5th Prize - $17,311: Yuval Avrahami and Shaul Ben Hai for the report and write-up [Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms). Their whitepaper covers privilege escalation vectors in Kubernetes and describes vulnerabilities in many Kubernetes hosting providers, including Azure's AKS, Amazon's EKS, and GKE.

6th Prize - $13,373: Obmi for the report and write-up [A Few Bugs in the Google Cloud Shell](https://obmiblog.blogspot.com/2022/12/gcp-2022-few-bugs-in-google-cloud-shell.html). Obmi discovered vulnerabilities in the Cloud Shell file upload functionality that would have allowed an attacker to write arbitrary files to a user's Cloud Shell via cross-site request forgery.

7th Prize - $13,337: Bugra Eskici for the report and write-up [Command injection in Cloud Shell](https://bugra.ninja/posts/cloudshell-command-injection/). Bugra found a very curious injection point in a Cloud Shell script that led to a URL query parameter being directly injected into a Python script. This vulnerability would have given an attacker arbitrary code execution in a user's Cloud Shell if they clicked on an attacker-controlled link.

Congratulations to all the winners and happy hacking! Follow us on [@GoogleVRP](http://twitter.com/googlevrp) for future news and updates.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/7168887645384771558)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/06/supply-chain-security-for-go-part-2.html "Newer Post")

[**](https://security.googleblog.com/2023/06/protect-and-manage-browser-extensions.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog.com/search/label/android%20tr)
* [app security](https://security.googleblog.com/search/label/app%20security)
* [big data](https://security.googleblog.com/search/label/big%20data)
* [biometrics](https://security.googleblog.com/search/label/biometrics)
* [blackhat](https://security.googleblog.com/search/label/blackhat)
* [C++](https://security.googleblog.com/search/label/C%2B%2B)
* [chrome](https://security.googleblog.com/search/label/chrome)
* [chrome enterprise](https://security.googleblog.com/search/label/chrome%20enterprise)
* [chrome security](https://security.googleblog.com/search/label/chrome%20security)
* [connected devices](https://security.googleblog.com/search/label/connected%20devices)
* [CTF](https://security.googleblog.com/search/label/CTF)
* [diversity](https://security.googleblog.com/search/label/diversity)
* [encryption](https://security.googleblog.com/search/label/encryption)
* [federated learning](https://security.googleblog.com/search/label/federated%20learning)
* [fuzzing](https://security.googleblog.com/search/label/fuzzing)
* [Gboard](https://security.googleblog.com/search/label/Gboard)
* [google play](https://security.googleblog.com/search/label/google%20play)
* [google play protect](https://security.googleblog.com/search/label/google%20play%20protect)
* [hacking](https://security.googleblog.com/search/label/hacking)
* [interoperability](https://security.googleblog.com/search/label/interoperability)
* [iot security](https://security.googleblog.com/search/label/iot%20security)
* [kubernetes](https://security.googleblog.com/search/label/kubernetes)
* [linux kernel](https://security.googleblog.com/search/label/linux%20kernel)...