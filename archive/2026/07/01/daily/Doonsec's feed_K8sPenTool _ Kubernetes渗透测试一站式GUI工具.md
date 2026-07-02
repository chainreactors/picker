---
title: K8sPenTool | Kubernetes渗透测试一站式GUI工具
url: https://mp.weixin.qq.com/s/VNR3IEuwlsc8m5U7BVjzQw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:54:23.169040
---

# K8sPenTool | Kubernetes渗透测试一站式GUI工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CFR489vPHAbzRuACu7GomRDqQB28siaztyDlmqL0A4H2OapEtyZDVPaWLBEcDfSVbuYKD3ibe1lY6p1M2ICptRgdEcEWaHB3vLuMFLgSYvfdE/0?wx_fmt=jpeg)

# K8sPenTool | Kubernetes渗透测试一站式GUI工具

原创

予辉安全
予辉安全

予辉安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2K4EpvaFFClay5IHWNuY8h7ATvaibnex5580qxT68BjT8K3c9zP3aOBTWbBRRky1z9dJ3RrS6iaxIPgepnTKEO6g/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAamAqcSDJ3CPHw9hjiaWWpKlqVPUNiaLshSw4grRroibfbib7E8AyCIC8ZNDzBsooCYlAfPtFViblUZZnmictoKK3hst0qKM7c4oibfVg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAbbMb1atCO66ib9b8qWb0yDT8ibbk3uZcO3gHSzplAhtz1LHs9uXhwx9mY3ZcicN4g7TL9zkB9BDuKxEj9X2wJn2NdEVjPjUFb0js/640?wx_fmt=png&from=appmsg)

**-前言-**

---

在针对Kubernetes集群的安全测试或攻防演练中，你是不是经常遇到这些问题：

* 🔧 **命令太多记不住**：kubectl get pods、kubectl describe、kubectl exec……参数一多就容易翻车
* 🔗 **工具切换繁琐**：这个环节用这个脚本，那个环节用另一个工具，来回切换效率低
* 🧩 **攻击链不连贯**：信息搜集完忘了做提权检测，提权检测完忘了做持久化，容易遗漏环节
* 📊 **结果分散不好看**：不同阶段的结果散落在各个终端窗口里，汇总分析很麻烦

**K8s渗透测试本应是链条式的攻击路径，却常常因为工具分散、操作繁琐变成碎片化的体力活。**

![](https://mmbiz.qpic.cn/mmbiz_png/CFR489vPHAbYRlRB0CYIpv9w8wcic8GKPPV50ha43xicIibeIyvzp8DiaCeboBe3kicACW4RetziaOAiaXh3DF5icupxWXDsfjbXOpKMN6O1Xib1MBWc/640?wx_fmt=png&from=appmsg)

**-工具简介-**

---

**K8sPenTool**是一款基于JavaFX的Kubernetes渗透测试GUI工具，将常见K8s攻击链集成到统一图形界面中，覆盖从**信息搜集 → 初始访问 → 命令执行 → 权限维持 → 权限提升 → 横向移动**的完整渗透流程，帮助安全研究人员快速评估Kubernetes集群的安全态势。

| 场景 | 传统方式 | K8sPenTool |
| --- | --- | --- |
| 信息搜集 | 手动敲kubectl命令 | **点一下按钮，信息全出来** |
| 命令执行 | 写YAML部署Pod | **界面配置，一键部署** |
| 权限维持 | 手写CronJob YAML | **模块化配置，自动生成** |
| 容器逃逸 | 查资料记命令 | **集成常见逃逸手法** |
| 横向移动 | 手动探测内网 | **内置探测功能** |

**-核心功能-**

---

### 🔍 信息搜集模块

攻击的第一步永远是信息搜集。K8sPenTool在这个阶段集成了：

* **容器环境辨别**：判断当前是否在容器内运行
* **特权检测**：检查容器是否以特权模式运行
* **Capabilities解码**：解析Linux Capabilities权限
* **K8s端口扫描**：扫描集群中常见服务端口（6443、10250、2379等）
* **SA Token枚举**：枚举Service Account挂载的Token

有了这些信息，攻击者就能快速评估自己“手里有什么牌”。

### 🚪 初始访问模块

信息搜集完成后，下一步是寻找进入集群的突破口：

* **APIServer未授权检测**：检测是否允许匿名访问
* **Kubelet API利用**：检查Kubelet是否开放了未授权接口
* **Etcd未授权检测**：检测etcd是否暴露了数据
* **Dashboard检测**：发现Kubernetes Dashboard并检测弱口令
* **Kubeconfig解析**：解析和利用泄露的kubeconfig文件

### ⚡ 命令执行模块

拿到入口之后，核心就是执行命令了：

* **APIServer exec**：通过API Server在Pod中执行命令
* **Kubelet exec**：直接通过Kubelet API执行命令
* **后门Pod部署**：一键部署带后门的Pod（支持反弹Shell）
* **反弹Shell生成**：内置多种反弹Shell Payload
* **RBAC权限检查**：检查当前身份是否有足够权限

### 🔒 权限维持模块

权限维持是保证访问通道不丢失的关键：

* **Admin SA创建**：创建一个拥有cluster-admin权限的ServiceAccount
* **CronJob持久化**：通过CronJob定期触发后门
* **DaemonSet持久化**：在集群中每个节点上运行后门Pod
* **影子Kubeconfig**：在目标集群中植入隐藏的kubeconfig
* **宿主机持久化**：在宿主机上建立持久化访问通道

### 🔓 权限提升模块

从Pod权限提升到宿主机权限，这是K8s渗透中最关键的一步：

* **特权容器逃逸**：利用privileged容器逃逸到宿主机
* **挂载逃逸**：利用procfs、docker.sock、宿主机磁盘挂载等方式逃逸
* **内核漏洞利用**：集成常见容器逃逸内核漏洞利用

### 🌐 横向移动模块

拿到一个节点后，继续向集群中其他节点和Pod横向扩散：

* **Secret凭证窃取**：从集群中窃取其他服务的认证凭证
* **集群内网探测**：发现集群内部的其他服务和资产
* **污点容忍横向扩展**：利用污点容忍机制扩展控制范围

### 🛠 kubectl操作模块

工具还集成了kubectl快捷操作面板：

* 快捷kubectl命令按钮
* 自定义命令执行框
* 后门Pod管理界面

**-工具获取-**

---

后台回复：20260701

源码适用JDK 17或更高版本、Maven 3.6+命令mvn clean package编译

windows版直接下载使用

**End**

![](https://mmbiz.qpic.cn/mmbiz_png/2K4EpvaFFClay5IHWNuY8h7ATvaibnex5noCLyoyaxx7l2ChafzmKwtcOibIpFtuGcicwpdlpFLbHQhyqpnhTKwYg/640?wx_fmt=png&from=appmsg)

**文章都看完了，还不点个赞**

**回顾往期内容**

[MemShellParty丨一键生成主流Web中间件](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247484346&idx=1&sn=074fefe9b882ba8168110cae8d061f50&scene=21#wechat_redirect)

[HeapDump敏感信息一键提取图形化工具](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247484331&idx=1&sn=5e5dd90215404083398f8f6d54a53244&scene=21#wechat_redirect)

[一款用于发现未授权接口与敏感信息的BurpSuite插件](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247484317&idx=1&sn=09b7f854548de2d57f01d2aee2d9bb3b&scene=21#wechat_redirect)

[SQL注入靶场显错注入（一）](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247483818&idx=1&sn=41542d23e0391d2c390fd3bcadf9e179&scene=21#wechat_redirect)

[Sunny网络中间件](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247483798&idx=1&sn=2c9305a9af4c7bc3d31e0228d87f0ebb&scene=21#wechat_redirect)

[JAVA代码审计：鉴权漏洞深度分析](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247483756&idx=1&sn=57e00393f90e7753835dbb3fc6cf2941&scene=21#wechat_redirect)

[你不知道的表网、深网与暗网世界](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247483745&idx=1&sn=f2d316ae89039789bd168250bac5cb14&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAZUUSBMsWSmlOWp9D3ozPMI1Txp8Y9jy1cNvCjsok413nTBZP9SxUXLkicl8Hqd6S0eHHtqwEs1Fibk7LSk9oNWJqMxC9zbCULyQ/0?wx_fmt=png)

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