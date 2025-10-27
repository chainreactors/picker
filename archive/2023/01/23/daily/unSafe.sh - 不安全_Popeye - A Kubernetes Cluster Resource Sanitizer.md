---
title: Popeye - A Kubernetes Cluster Resource Sanitizer
url: https://buaq.net/go-146502.html
source: unSafe.sh - 不安全
date: 2023-01-23
fetch_date: 2025-10-04T04:35:03.859743
---

# Popeye - A Kubernetes Cluster Resource Sanitizer

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

![](https://8aqnet.cdn.bcebos.com/25bf3cddaa197249d43442e61b9a0810.jpg)

Popeye - A Kubernetes Cluster Resource Sanitizer

Popeye is a utility that scans live Kubernetes cluster and reports potential issues with d
*2023-1-22 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-146502.htm)
阅读量:28
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjJL4BARM0sbZnQi6bIHFibZYsdjWOx0iMFkzA1ZCW4Z1loiRn5xpoe3-EnWbTU8HNZbgClCOpr9xMJBTdXCHc6iYP-kCl1tETYWLzUowzu9_G0FyfmYjpEHrWpR-iExsnWUJX2UknSwxKMqQesMpCGR3_NfzUNIVWDebWoWO_gYh19qZ0j8B89EL9vlQ=w400-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEjJL4BARM0sbZnQi6bIHFibZYsdjWOx0iMFkzA1ZCW4Z1loiRn5xpoe3-EnWbTU8HNZbgClCOpr9xMJBTdXCHc6iYP-kCl1tETYWLzUowzu9_G0FyfmYjpEHrWpR-iExsnWUJX2UknSwxKMqQesMpCGR3_NfzUNIVWDebWoWO_gYh19qZ0j8B89EL9vlQ)

Popeye is a utility that scans live Kubernetes cluster and reports potential issues with deployed resources and configurations. It sanitizes your cluster based on what's deployed and not what's sitting on disk. By scanning your cluster, it detects [misconfigurations](https://www.kitploit.com/search/label/Misconfigurations "misconfigurations") and helps you to ensure that best practices are in place, thus preventing future headaches. It aims at reducing the cognitive *over*load one faces when operating a Kubernetes cluster in the wild. Furthermore, if your cluster employs a metric-server, it reports potential resources over/under allocations and attempts to warn you should your cluster run out of capacity.

Popeye is a readonly tool, it does not alter any of your Kubernetes resources in any way!

## Installation

Popeye is available on Linux, OSX and Windows platforms.

* Binaries for Linux, Windows and Mac are available as tarballs in the [release](https://github.com/derailed/popeye/releases "release") page.
* For OSX/Unit using Homebrew/LinuxBrew

  ```
  brew install derailed/popeye/popeye
  ```
* Building from source Popeye was built using go 1.12+. In order to build Popeye from source you must:

  1. Clone the repo
  2. Add the following command in your go.mod file

     ```
     replace (
     ```
  3. Build and run the executable

  Quick recipe for the impatient:

  ```
  # Clone outside of GOPATH
  git clone https://github.com/derailed/popeye
  cd popeye
  # Build and install
  go install
  # Run
  popeye
  ```

## PreFlight Checks

* Popeye uses 256 colors terminal mode. On `Nix system make sure TERM is set accordingly.

  ```
  export TERM=xterm-256color
  ```

## Sanitizers

Popeye scans your cluster for best practices and potential issues. Currently, Popeye only looks at nodes, namespaces, pods and services. More will come soon! We are hoping Kubernetes friends will pitch'in to make Popeye even better.

The aim of the sanitizers is to pick up on misconfigurations, i.e. things like port mismatches, dead or unused resources, metrics utilization, probes, container images, RBAC rules, naked resources, etc...

Popeye is not another [static analysis](https://www.kitploit.com/search/label/Static%20Analysis "static analysis") tool. It runs and inspect Kubernetes resources on live clusters and sanitize resources as they are in the wild!

Here is a list of some of the available sanitizers:

|  | Resource | Sanitizers | Aliases |
| --- | --- | --- | --- |
|  | Node |  | no |
|  |  | Conditions ie not ready, out of mem/disk, network, pids, etc |  |
|  |  | Pod tolerations referencing node taints |  |
|  |  | CPU/MEM utilization metrics, trips if over limits (default 80% CPU/MEM) |  |
|  | Namespace |  | ns |
|  |  | Inactive |  |
|  |  | Dead namespaces |  |
|  | Pod |  | po |
|  |  | Pod status |  |
|  |  | Containers statuses |  |
|  |  | ServiceAccount presence |  |
|  |  | CPU/MEM on [containers](https://www.kitploit.com/search/label/Containers "containers") over a set CPU/MEM limit (default 80% CPU/MEM) |  |
|  |  | Container image with no tags |  |
|  |  | Container image using `latest` tag |  |
|  |  | Resources request/limits presence |  |
|  |  | Probes liveness/readiness presence |  |
|  |  | Named ports and their references |  |
|  | Service |  | svc |
|  |  | Endpoints presence |  |
|  |  | Matching pods labels |  |
|  |  | Named ports and their references |  |
|  | ServiceAccount |  | sa |
|  |  | Unused, detects potentially unused SAs |  |
|  | Secrets |  | sec |
|  |  | Unused, detects potentially unused secrets or associated keys |  |
|  | ConfigMap |  | cm |
|  |  | Unused, detects potentially unused cm or associated keys |  |
|  | Deployment |  | dp, deploy |
|  |  | Unused, pod template validation, resource utilization |  |
|  | StatefulSet |  | sts |
|  |  | Unsed, pod template validation, resource utilization |  |
|  | DaemonSet |  | ds |
|  |  | Unsed, pod template validation, resource utilization |  |
|  | PersistentVolume |  | pv |
|  |  | Unused, check volume bound or volume error |  |
|  | PersistentVolumeClaim |  | pvc |
|  |  | Unused, check bounded or volume mount error |  |
|  | HorizontalPodAutoscaler |  | hpa |
|  |  | Unused, Utilization, Max burst checks |  |
|  | PodDisruptionBudget |  |  |
|  |  | Unused, Check minAvailable configuration | pdb |
|  | ClusterRole |  |  |
|  |  | Unused | cr |
|  | ClusterRoleBinding |  |  |
|  |  | Unused | crb |
|  | Role |  |  |
|  |  | Unused | ro |
|  | RoleBinding |  |  |
|  |  | Unused | rb |
|  | Ingress |  |  |
|  |  | Valid | ing |
|  | NetworkPolicy |  |  |
|  |  | Valid | np |
|  | PodSecurityPolicy |  |  |
|  |  | Valid | psp |

You can also see the [full list of codes](https://github.com/derailed/popeye/blob/master/docs/codes.md "full list of codes")

### Save the report

To save the Popeye report to a file pass the `--save` flag to the command. By default it will create a temp directory and will store the report there, the path of the temp directory will be printed out on STDOUT. If you have the need to specify the output directory for the report, you can use the environment variable `POPEYE_REPORT_DIR`. By default, the name of the output file follow the following format : `sanitizer_<cluster-name>_<time-UnixNano>.<output-extension>` (e.g. : "sanitizer-mycluster-1594019782530851873.html"). If you have the need to specify the output file name for the report, you can pass the `--output-file` flag with the filename you want as parameter.

Example to save report in working directory:

```
  $ POPEYE_REPORT_DIR=$(pwd) popeye --save
```

Example to save report in working directory in HTML format under the name "report.html" :

```
  $ POPEYE_REPORT_DIR=$(pwd) popeye --save --out html --output-file report.html
```

### Save the report to S3

You can also save the generated report to an AWS S3 bucket (or another S3 compatible Object Storage) with providing the flag `--s3-bucket`. As parameter you need to provide the name of the S3 bucket where you want to store the report. To save the report in a bucket subdirectory provide the bucket parameter as `bucket/path/to/report`.

Underlying the AWS Go lib is used which is handling the credential loading. For more information check out the official [documentation](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/ "documentation").

Example to save report to S3:

```
popeye --s3-bucket=NAME-OF-YOUR-S3-BUCKET/OPTIONAL/SUBDIRECTORY --out=json
```

If AWS sS3 is not your bag, you can further define an S3 compatible storage (OVHcloud Object Storage, Minio, Google cloud storage, etc...) using s3-endpoint and s3-region as so:

```
popeye --s3-bucket=NAME-OF-YOUR-S3-BUCKET/OPTIONAL/SUBDIRECTORY --s3-region YOUR-REGION --s3-endpoint URL-OF-THE-ENDPOINT
```

### Run public Docker image lo...