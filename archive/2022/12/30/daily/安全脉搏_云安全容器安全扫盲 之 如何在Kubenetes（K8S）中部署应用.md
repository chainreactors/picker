---
title: 云安全容器安全扫盲 之 如何在Kubenetes（K8S）中部署应用
url: https://www.secpulse.com/archives/194329.html
source: 安全脉搏
date: 2022-12-30
fetch_date: 2025-10-04T02:43:51.948018
---

# 云安全容器安全扫盲 之 如何在Kubenetes（K8S）中部署应用

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 云安全容器安全扫盲 之 如何在Kubenetes（K8S）中部署应用

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Ms08067安全实验室](https://www.secpulse.com/newpage/author?author_id=11195)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-29

9,131

******文章来源 | MS08067****** ******安全实验室******

本文作者：**Taoing（Web安全攻防讲师）**

一.部署pod

1. kubectl run 直接部署pod

```
kubectl run testapp --image=ccr.ccs.tencentyun.com/k8s-tutorial/test-k8s:v1
```

2. 使用yaml文件创建pod

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672296977.png)

apiVersion：API版本

kind：类型

metadata：数据元

name：定义pod的名字

spec：规格

containers：容器

name：容器名字

image：镜像地址

```
kubectl apply -f pod.yaml
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672296978.png)

这里我没有拉取到，使用别人的图解释下。

test-k8s 是使用yaml文件创建的

testapp 是使用 命令行创建的。

3.部署

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-16722969781.png)

Deployment 通过 label 关联起来 Pods

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672296979.png)

4. pod 常用操作命令

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672296984.png)![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672296993.png)

部署应用

kubectl apply -f app.yaml

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672296995.png)

kubectl get pod -o wide

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297000.png)

describe查看 pod 详情

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297001.png)

查看pod运行日志

kubectl logs pod-name

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297004.png)

exec进入 Pod 容器终端

kubectl exec -it pod-name -- bash

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297006.png)

复制文件操作

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297007.png)

pod集群内端口映射到节点

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297008.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297010.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297011.png)

kubectl get all 查看全部

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297012.png)

更多命令

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297013.png)

二.部署service

1. service特性

·Service 通过 label 关联对应的 Pod

·Service 生命周期不跟 Pod 绑定，不会因为Pod 重建 改变IP

·提供负载均衡功能，自动转发流量到不同的Pod

·可以对集群外部提供访问端口

·集群内部可通过服务名字访问

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-16722970131.png)

2. 创建service

通过标签test-k8s跟对应的 Pod 关联上

该service的名字是test-k8s；

通过标签app: test-k8s与pod进行关联。

service.yaml

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297014.png)

应用配置 kubectl apply -f service.yaml
查看服务 kubectl get svc

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297016.png)

查看服务详情 kubectl describe svc test-k8s

可以发现 Endpoints 是各个 Pod 的 IP，也就是他会把流量转发到这些节点。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297018.png)

服务的默认类型是ClusterIP，只能在集群内部访问，我们可以进入到 Pod 里面访问：
kubectl exec -it pod-name -- bash
curl http://test-k8s:8080

如果要在集群外部访问，可以通过端口转发实现（只适合临时测试用）：
kubectl port-forward service/test-k8s 8888:8080

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297019.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297021.png)

如果你用 minikube，也可以这样minikube service test-k8s

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-16722970211.png)

多端口

多端口时必须配置 name

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297022.png)

总结

ClusterIP

默认的，仅在集群内可用

NodePort

暴露端口到节点，提供了集群外部访问的入口
端口范围固定 30000 ~ 32767

LoadBalancer

需要负载均衡器（通常都需要云服务商提供，裸机可以安装METALLB测试）
会额外生成一个 IP 对外服务。

三.部署StatefulSet

1. 什么是 StatefulSet

StatefulSet 是用来管理有状态的应用，例如数据库。

之前我们部署的应用，都是不需要存储数据，不需要记住状态的，可以随意扩充副本，每个副本都是一样的，可替代的。

而像数据库、Redis 这类有状态的，则不能随意扩充副本。

StatefulSet 会固定每个 Pod 的名字

2. 部署 StatefulSet 类型的 Mongodb

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297023.png)![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297024.png)

kubectl apply -f mongo.yaml

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297025.png)

kubectl get StatefulSet

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-16722970251.png)

StatefulSet 特性

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-1672297026.png)

Service的CLUSTER-IP是空的，Pod 名字也是固定的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194329-16722970261.png)

Pod 创建和销毁是有序的，创建是顺序的，销毁是逆序的。

![](https://secpu...