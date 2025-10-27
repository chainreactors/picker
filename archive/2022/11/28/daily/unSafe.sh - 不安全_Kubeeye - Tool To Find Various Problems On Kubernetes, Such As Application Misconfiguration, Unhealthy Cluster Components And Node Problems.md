---
title: Kubeeye - Tool To Find Various Problems On Kubernetes, Such As Application Misconfiguration, Unhealthy Cluster Components And Node Problems
url: https://buaq.net/go-137443.html
source: unSafe.sh - 不安全
date: 2022-11-28
fetch_date: 2025-10-03T23:54:48.763163
---

# Kubeeye - Tool To Find Various Problems On Kubernetes, Such As Application Misconfiguration, Unhealthy Cluster Components And Node Problems

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

![](https://8aqnet.cdn.bcebos.com/76fe96dabef8541b0e304ae185aecdd1.jpg)

Kubeeye - Tool To Find Various Problems On Kubernetes, Such As Application Misconfiguration, Unhealthy Cluster Components And Node Problems

KubeEye is an inspection tool for Kubernetes to discover Kubernetes resources (by OPA ), clus
*2022-11-27 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-137443.htm)
阅读量:31
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC9cGVhns7OIQ5LhtNpbL1aINjWADdF_mNpqku1e9V_zqpSTjrTbIhkvksZwzLVAkis2xrWvC8hvrhqyHtLTmlsJISyodcxJKdEItg7nyE_apCR9i2FV9CIf4a9jvz9Twl9v4hfB8L8UnEPaxIJouXo8KHIgQvoZBW0-u_1BjI1rwKHnOwnvKVlOfbZw/w640-h196/kubeeye-logo.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC9cGVhns7OIQ5LhtNpbL1aINjWADdF_mNpqku1e9V_zqpSTjrTbIhkvksZwzLVAkis2xrWvC8hvrhqyHtLTmlsJISyodcxJKdEItg7nyE_apCR9i2FV9CIf4a9jvz9Twl9v4hfB8L8UnEPaxIJouXo8KHIgQvoZBW0-u_1BjI1rwKHnOwnvKVlOfbZw/s1860/kubeeye-logo.png)

KubeEye is an inspection tool for [Kubernetes](https://www.kitploit.com/search/label/Kubernetes "Kubernetes") to discover Kubernetes resources (by [OPA](https://github.com/open-policy-agent/opa "OPA") ), cluster components, cluster nodes (by [Node-Problem-Detector](https://github.com/kubernetes/node-problem-detector "Node-Problem-Detector")) and other configurations are meeting with best practices, and giving suggestions for modification.

KubeEye supports custom inspection rules and plugins installation. Through [KubeEye Operator](https://github.com/kubesphere/kubeeye#kubeeye-operator "KubeEye Operator"), you can view the inspection results and [modification](https://www.kitploit.com/search/label/Modification "modification") suggestions by the graphical display on the web page.

## Architecture

KubeEye get cluster resource details by the Kubernetes API, inspect the resource configurations by inspection rules and plugins, and generate inspection results. See Architecture for details.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg33o65pFnwHA2fiwLVQrRadickYzwNnSdpl2xqAvuptsbzVxzxxyB2yyGY1tcqraLPIDl5M-q8rXsqrtim0pux7lzhVSmptvsk_cH3FcuUg7yqzFfzJMXQpGU91KFfHHEk9Zga3742ny7lyB7q3N7-7Qu7TR0ML4Dsk6wzH0WvvFMaxckWyxjbIJLqqw/w640-h350/kubeeye.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg33o65pFnwHA2fiwLVQrRadickYzwNnSdpl2xqAvuptsbzVxzxxyB2yyGY1tcqraLPIDl5M-q8rXsqrtim0pux7lzhVSmptvsk_cH3FcuUg7yqzFfzJMXQpGU91KFfHHEk9Zga3742ny7lyB7q3N7-7Qu7TR0ML4Dsk6wzH0WvvFMaxckWyxjbIJLqqw/s867/kubeeye.png)

## How to use

* Install KubeEye on your machine

  + Download pre built executables from [Releases](https://github.com/kubesphere/kubeeye/releases "Releases").
  + Or you can build from source code
  > Note: make install will create kubeeye in /usr/local/bin/ on your machine.

  ```
  git clone https://github.com/kubesphere/kubeeye.git
  ```
* [Optional] Install [Node-problem-Detector](https://github.com/kubernetes/node-problem-detector "Node-problem-Detector")

> Note: This will install npd on your cluster, only required if you want detailed report.

* Run KubeEye

> Note: The results of kubeeye sort by resource kind.

```
kubeeye audit
KIND          NAMESPACE        NAME                                                           REASON                                        LEVEL    MESSAGE
Node                           docker-desktop                                                 kubelet has no sufficient memory available   warning    KubeletHasNoSufficientMemory
Node                           docker-desktop                                                 kubelet has no sufficient PID available      warning    KubeletHasNoSufficientPID
Node                           docker-desktop                                                 kubelet has disk pressure                    warning    KubeletHasDiskPressure
Deployment    default          testkubeeye                                                                                                                  NoCPULimits
Deployment    default          testkubeeye                                                                                                                  NoReadinessProbe
Deployment    default          testkubeeye                                                                                                                  NotRunAsNonRoot
Deployment    kube-system      coredns                                                                                                               NoCPULimits
Deployment    kube-system      coredns                                                                                                               ImagePullPolicyNotAlways
Deployment    kube-system      coredns                                                                                                               NotRunAsNonRoot
Deployment    kubeeye-system   kubeeye-controller-manager                                                                                            ImagePullPolicyNotAlways
Deployment    kubeeye-system   kubeeye-controller-manager                                                                                            NotRunAsNonRoot
DaemonSet     kube-system      kube-proxy                                                                                                            NoCPULimits
DaemonSet     k          ube-system      kube-proxy                                                                                                            NotRunAsNonRoot
Event         kube-system      coredns-558bd4d5db-c26j8.16d5fa3ddf56675f                      Unhealthy                                    warning   Readiness probe failed: Get "http://10.1.0.87:8181/ready": dial tcp 10.1.0.87:8181: connect: connection refused
Event         kube-system      coredns-558bd4d5db-c26j8.16d5fa3fbdc834c9                      Unhealthy                                    warning   Readiness probe failed: HTTP probe failed with statuscode: 503
Event         kube-system      vpnkit-controller.16d5ac2b2b4fa1eb                             BackOff                                      warning   Back-off restarting failed container
Event         kube-system      vpnkit-controller.16d5fa44d0502641                             BackOff                                      warning   Back-off restarting failed container
Event         kubeeye-system   kubeeye-controller-manager-7f79c4ccc8-f2njw.16d5fa3f5fc3229c   Failed                                       warning   Failed to pull image "controller:latest": rpc error: code = Unknown desc = Error response from daemon: pull access denied for controller, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
Event         kubeeye-system   kubeeye-controller-manager-7f79c4ccc8-f2njw.16d5fa3f61b28527   Failed                                       warning   Error: ImagePullBackOff
Role          kubeeye-system   kubeeye-leader-election-role                                                                                          CanDeleteResources
ClusterRole                    kubeeye-manager-role                                                                                                  CanDeleteResources
ClusterRole                    kubeeye-manager-role                                                                                                  CanModifyWorkloads
ClusterRole                    vpnkit-controller                                                                                                     CanImpersonateUser
ClusterRole                    vpnkit-controlle...