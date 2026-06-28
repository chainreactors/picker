---
title: K8sPenTool：一款面向Kubernetes集群的综合渗透测试评估平台
url: https://mp.weixin.qq.com/s/iEhLsvzuTH4MdTEiqn0Q3g
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:09:31.943941
---

# K8sPenTool：一款面向Kubernetes集群的综合渗透测试评估平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicJVBc6MjvDDmHLIIrceHVic6B9XL6XBlBSyiaEVSya3j0sOiaLNOjLbicQn9hup3icicncH8NB7RnvdQoKfYFcBnoYXVdz40YNLN65LU/0?wx_fmt=jpeg)

# K8sPenTool：一款面向Kubernetes集群的综合渗透测试评估平台

原创

KivenMitnick
KivenMitnick

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[CTF²: 推荐一个比较全面的CTF靶场](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487722&idx=1&sn=f12056918c209179a318d1f904d05210&scene=21#wechat_redirect)

·[Bug Hunter：一个代码安全审计的skills](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487714&idx=1&sn=b02dcacd5efb02443bd0a213b80ef99e&scene=21#wechat_redirect)

·[NextWQ：一款QQ小程序安全测试分析工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487701&idx=1&sn=91f799ebe8d87bb92f33a04230e5814c&scene=21#wechat_redirect)

·[MPScan：微信小程序自动化敏感信息审计工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487683&idx=1&sn=1c45d8b5233e471633e7f430d93c0ec3&scene=21#wechat_redirect)

·[cloudTools：一款集成多平台的OSS接管和管理工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487669&idx=1&sn=1ddc86d05e10c5fc4219df5917374322&scene=21#wechat_redirect)

·[Misc-Galaxysail：一站式 CTF Misc 杂项分析工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487649&idx=1&sn=1b5cc549bc0dafeb13bad7fea73beae2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**背景分析**

![Kubernetes安全架构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicL7vTpB06iaz35A3OwQeQiaVlZPLBm9J1I2fomLf1QFSIUmNyJpUpE4fREwjRBsqgoXXicMGyJZNyvibuO1Z0DiccahTwYib1tPdAygQ/640?wx_fmt=jpeg&from=appmsg)

随着云原生技术的广泛部署与深入应用，**Kubernetes（K8s）**已成为现代容器编排领域的事实标准。然而，在Kubernetes集群的复杂架构中，安全威胁呈现出多元化、隐蔽化的特征，传统的安全检测手段已难以满足对容器化环境的全面安全评估需求。

**K8sPenTool**是由安全研究者**T3Y**开发的一款基于**JavaFX框架**构建的Kubernetes综合渗透测试工具。该工具采用图形化用户界面（GUI）设计理念，将Kubernetes攻击链中的关键环节进行系统化整合，覆盖从信息收集、初始访问、命令执行到横向移动的完整渗透测试流程，为安全研究人员提供一站式的K8s安全态势评估能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**工具架构**

从技术架构视角分析，K8sPenTool采用模块化设计思想，基于**MVC（Model-View-Controller）**模式实现功能解耦。其核心架构包括：

**表示层**

：基于JavaFX 17构建的FXML声明式界面，提供直观的可视化操作面板

**业务逻辑层**

：按功能域划分为七大处理模块（Handler），分别对应不同的渗透测试阶段

**数据访问层**

：通过K8sHttpUtil封装HTTP请求逻辑，实现对Kubernetes API Server的标准化调用

**工具支撑层**

：集成Gson JSON解析库及Maven Shade Plugin打包方案

该工具的设计遵循**MIT开源协议**，代码托管于GitHub平台（https://github.com/trymonoly/K8sPenTool），截至目前已获得137个Star关注，体现了社区对该工具实用价值的认可。

## 功能模块体系

K8sPenTool的功能架构涵盖Kubernetes渗透测试的全生命周期，具体可分为以下七个核心模块：

| 模块标识 | 功能名称 | 核心能力描述 |
| --- | --- | --- |
| 🔍 | **信息搜集** | 容器环境辨别、特权模式检测、Linux Capabilities解码分析、K8s服务端口扫描、Service Account Token枚举 |
| 🚪 | **初始访问** | APIServer未授权访问检测、Kubelet API接口利用、Etcd数据存储未授权访问、Dashboard控制台检测、Kubeconfig配置文件解析 |
| ⚡ | **命令执行** | 通过APIServer/Kubelet实现Pod内命令执行、后门Pod自动化部署、反弹Shell载荷生成、RBAC权限矩阵检查 |
| 🔒 | **权限维持** | 高权限Service Account创建、CronJob/DaemonSet持久化机制部署、影子Kubeconfig生成、宿主机级持久化 |
| 🔓 | **权限提升** | 特权容器逃逸利用、挂载逃逸技术（procfs/docker.sock/disk）、内核漏洞利用辅助 |
| 🌐 | **横向移动** | Kubernetes Secret资源凭证窃取、集群内部网络探测、污点容忍策略横向扩展 |
| 🛠 | **kubectl操作** | 常用kubectl快捷命令集成、自定义命令执行环境、后门Pod生命周期管理 |

![渗透测试流程图](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJ9z0j1D6ms2tG1CMZIgfUpjWHJnEzUQgmHXWxq9JiaoEzVsCvZJZMNiafTicaXicN33Dwq8CpbHlSRDzOTJp22Q4ay8ZZgU4iahljw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

下载与环境配置

3.1 环境依赖要求

**运行环境前置条件：**

* JDK 17或更高版本（推荐使用Oracle JDK或OpenJDK）
* Maven 3.6+ 构建工具
* 操作系统支持：Windows / macOS / Linux（跨平台兼容）

### 3.2 源码编译与部署

进入GitHub项目仓库获取源代码：

```
git clone https://github.com/trymonoly/K8sPenTool.gitcd K8sPenToolmvn clean package
```

编译完成后，生成的可执行JAR文件位于 `target/k8s-pen-tool-1.0.0.jar` 路径下。该JAR包采用Maven Shade Plugin进行依赖打包，形成独立的Fat JAR，无需额外配置classpath即可直接运行。

### 3.3 启动方式

```
java -jar target/k8s-pen-tool-1.0.0.jar
```

*提示：若系统PATH中未配置Java环境变量，需指定JDK完整路径，例如：
/path/to/jdk-17/bin/java -jar target/k8s-pen-tool-1.0.0.jar*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**使用演示**

4.1 主界面概览

启动K8sPenTool后，将呈现基于JavaFX构建的主操作界面。界面采用标签页（Tab Pane）布局设计，各功能模块以独立Tab形式组织，便于测试人员在不同攻击阶段间快速切换。

### 4.2 信息搜集模块

信息搜集是渗透测试的首要阶段。该模块提供以下核心功能：

**容器环境自动识别**

：通过检测/.dockerenv文件、cgroup信息等特征判断当前是否处于容器化环境

**特权模式检测**

：分析当前容器的安全上下文（Security Context），识别特权容器风险

**Capabilities枚举**

：解析/proc/1/status文件，提取并解码当前进程拥有的Linux Capabilities集合

**端口扫描**

：针对Kubernetes集群内部常见端口（6443、10250、10257、2379等）进行存活探测

**SA Token提取**

：自动挂载点/var/run/secrets/kubernetes.io/serviceaccount/token读取与解析

![命令执行](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicKYBviayNkNDw2UWUEdMPtdiaP6V3rvvoCv0Sa0kicnsVV4JokOlFAC3FfYNp3UNy8ZPoFrWF7OTMicicL8ejc6baZXPcFaBt6mgsjw/640?wx_fmt=jpeg&from=appmsg)

### 4.3 初始访问模块

初始访问模块聚焦于Kubernetes集群边界的攻击面探测：

**APIServer未授权检测**

：尝试匿名访问/api/v1、/apis等端点，判断是否存在未授权访问漏洞

**Kubelet API利用**

：探测节点级Kubelet API（默认端口10250）的匿名访问与Pod exec能力

**Etcd未授权访问**

：检测Etcd存储（默认端口2379）是否存在未认证访问风险

**Dashboard安全检测**

：扫描Kubernetes Dashboard服务的暴露状态与认证绕过可能

**Kubeconfig解析**

：导入并解析kubeconfig文件，提取集群连接信息与凭证

### 4.4 命令执行模块

命令执行是实现深度渗透的关键环节：

**APIServer Exec**

：通过Kubernetes API Server的exec子资源实现Pod内命令执行

**Kubelet Exec**

：直接调用Kubelet API的/exec接口执行容器命令

**后门Pod部署**

：一键生成并部署包含反向Shell的恶意Pod YAML清单

**反弹Shell生成**

：支持Bash、Python、Perl、NC等多种语言的反弹Shell载荷模板

**RBAC权限检查**

：查询当前Service Account绑定的Role/ClusterRole规则，评估可操作资源范围

![权限维持](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicLeEOViaEG8ospibcXIHxtgUCpGHfiasQZRu9OibCsp7TdgmQ896vEjHxshz6c8mQMGpGegV7tt7NW88KeqZ31XpiauSbAVX9RGKBDU/640?wx_fmt=jpeg&from=appmsg)

### 4.5 权限维持模块

该模块提供多种持久化方案，模拟攻击者在获取初始访问后的驻留行为：

**Admin SA创建**

：自动生成具有cluster-admin权限的Service Account及其RBAC绑定

**CronJob持久化**

：通过CronJob资源实现定时任务级别的持久化

**DaemonSet持久化**

：利用DaemonSet的调度特性确保每个节点均运行后门实例

**影子Kubeconfig**

：生成伪造的高权限kubeconfig配置文件

### 4.6 权限提升模块

针对容器逃逸场景提供专项检测与利用支持：

**特权容器逃逸**

：检测privileged:true配置并提供逃逸利用路径指引

**挂载逃逸检测**

：识别procfs（/proc）、docker.sock、磁盘设备等危险挂载

**内核漏洞关联**

：结合当前内核版本匹配已知CVE漏洞数据库

![kubectl](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicJhFa8fjWke2Cxt0cBk3cKl47qPphOXRVvqIRweibUIlwialeoUxE7SmM9Q7USHRgGo0dKlSgfc27939ibSywic9CiaMicd0upibVNKHc/640?wx_fmt=jpeg&from=appmsg)

### 4.7 横向移动模块

横向移动模块聚焦于集群内部的攻击路径扩展：

**Secret窃取**

：枚举命名空间内的Secret资源，提取敏感凭证（如镜像仓库密码、TLS证书等）

**内网探测**

：从Pod内部发起对Cluster IP、Node IP段的端口与服务扫描

**污点容忍扩展**

：利用tolerations配置突破节点调度限制，实现跨节点横向移动

### 4.8 kubectl集成操作

内置kubectl命令执行环境，支持：

预设常用kubectl命令快捷按钮

自定义命令输入与执行

后门Pod的一键创建与清理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**项目地址**

```
https://github.com/trymonoly/K8sPenTool/tree/v1.0.0
```

我们创建了交流群，一起来交流吧！！！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicKTkN71udiawPU6nyoiaxxXdY2iajL1xq7qgWwegPW1eIbkaflnamoic58ws2lPpEoqewIh0AynkY4TcQMq5xtoJt93j9YCTLrA91o/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过