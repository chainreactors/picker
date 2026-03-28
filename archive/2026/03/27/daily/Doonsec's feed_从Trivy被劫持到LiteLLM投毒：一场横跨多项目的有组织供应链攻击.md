---
title: 从Trivy被劫持到LiteLLM投毒：一场横跨多项目的有组织供应链攻击
url: https://mp.weixin.qq.com/s/bG62FbTyIllXv_rNrHRJtQ
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:15:16.673443
---

# 从Trivy被劫持到LiteLLM投毒：一场横跨多项目的有组织供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquMVmP4d1srYSeLmJicNPbAH76J5zyNUr3LwB88mJADUWaCZyNc80t6KTeUc1sJJfns2Hya3ZRCWs82NBtTc8N8Ot2CJ0Ua1KlRI/0?wx_fmt=jpeg)

# 从Trivy被劫持到LiteLLM投毒：一场横跨多项目的有组织供应链攻击

Wtttthi
Wtttthi

船山信安

![]()

在小说阅读器中沉浸阅读

# 一个安全扫描器是怎么变成投毒入口的：LiteLLM供应链攻击

        事情发生在3月24号，LiteLLM的两个版本（1.82.7和1.82.8）被发现在PyPI上挂了恶意代码。这个包每天下载量三百多万次，两个坏版本在PyPI上待了大概三个小时才被隔离。

        攻击者叫TeamPCP，他们不是直接黑进LiteLLM的账号，而是绕了个弯：先搞了Trivy开源安全扫描器，LiteLLM的CI/CD流程里用到了这个工具。然后通过Trivy偷到了PyPI的发布凭证，顺手把LiteLLM的包给换了。

## 攻击链扩散时间

        2月底的时候，Trivy的CI被人利用`pull_request_target`这个workflow搞了一波，偷走了`aqua-bot`的凭证。3月19号，攻击者把Trivy的GitHub Action的tag指向了一个恶意版本（v0.69.4）。这个版本里藏着偷凭证的代码。

        LiteLLM的CI在跑的时候，会从apt装Trivy，而且没锁版本号。于是恶意版本的Trivy在CI环境里跑起来，偷到了`PYPI_PUBLISH`这个token。有了这个，攻击者就能以LiteLLM维护者的身份往PyPI上发包了。

        3月24号10:39，1.82.7上传；13分钟后，1.82.8上传。两个版本都有恶意代码，但藏的方式不一样。

## 两种投毒方式

**1.82.7**：恶意代码直接嵌在`litellm/proxy/proxy_server.py`里。只要代码里`import litellm.proxy`，payload就会触发。

**1.82.8**：这个版本更阴。它在`site-packages/`下面放了一个`litellm_init.pth`文件。Python的`.pth`文件在解释器启动时就会自动执行，不管你在跑什么代码——哪怕你只是`pip install`一下，或者IDE的language server启动，它都会触发。

        更离谱的是，`.pth`文件在wheel的RECORD里是正经声明的，hash对得上，所以`pip install --require-hashes`也拦不住。这种攻击手法在MITRE ATT&CK里叫T1546.018（Python Startup Hooks）。

## 三阶段payload

把恶意代码解码出来之后，可以看到它分了三个阶段干活：

**第一阶段：偷数据**

        它能偷的东西包括：SSH私钥、.env文件、Git凭证、shell历史里的API key、各种CI/CD配置、AWS/GCP/Azure的凭证文件、甚至Kubernetes的service account token。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquNh5LTicmt1jRa5x9wVwhBnO4FtwL8GaZmdMoqoib04SVdJM0lL1IicvE3oggOibARSrZYkj6En2VMbCkxU4yRAwd6nPZK3JGGkD4o/640?wx_fmt=webp&from=appmsg)

**第二阶段：加密外传**

        C2域名`models.litellm.cloud`是3月23号注册的，比投毒早一天。RSA公钥跟Trivy、KICS攻击里用的是同一个，这是最硬的证据链。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquNlsWXziartaaU0T1UaNC3qaOXx3wkRXnPwntRuicCwNgSc8rnRQuumbascdkbRLruNjlIo7xSx3oJFb3n3w2C5dibqKvib9KPtklc/640?wx_fmt=webp&from=appmsg)

**第三阶段：持久化和横向移动**

        后门装好之后，攻击者还得保证它不跑丢。所以第三阶段干的其实是两件事：一是把后门钉死在系统里，二是往K8s集群里扩散。

        本地持久化这块，他们在`~/.config/sysmon/`下面塞了个`sysmon.py`，又配了个systemd用户服务，名字叫“System Telemetry Service”。每5分钟去`checkmarx.zone/raw`问一次：下一步干啥？要干啥就从那边拉个文件下来，扔到`/tmp/pglog`里跑起来。当时那个接口返回的是YouTube链接，但想也知道，只要攻击者愿意，随时能换成真正的恶意载荷。

        K8s这边就是另外一种情况了。脚本会先看标准路径下有没有K8s service account token。有的话，它就遍历所有namespace把secrets全翻一遍。然后直接在`kube-system`里给每个节点起一个特权pod，用`alpine:latest`镜像，把宿主机根目录挂进去，再把那个`sysmon.py`后门装到节点上。这些pod名字都带`node-setup-`前缀，一眼就能认出来。

## 发现过程

        发现这事儿的人是FutureSearch的Callum McMahon。他在测试一个Cursor插件的时候，LiteLLM作为依赖被装上了。装完之后机器开始卡、内存爆了。追查发现是`.pth`文件触发了一个fork bomb——payload起了子进程，子进程又触发`.pth`，套娃了。这个fork bomb不是故意的，是个bug，但反而让问题暴露得更快。

## 怎么判断自己中招了

```
# 检查版本
pip show litellm | grep Version

# 检查后门文件
ls -la ~/.config/sysmon/sysmon.py
ls -la ~/.config/systemd/user/sysmon.service

# 检查临时文件残留
ls /tmp/tpcp.tar.gz /tmp/session.key /tmp/payload.enc

# 检查.pth文件
find $(python3 -c "import site; print(' '.join(site.getsitepackages()))") -name "*.pth" -exec grep -l "base64\|exec" {} \;

# 检查K8s
kubectl get pods -A | grep node-setup-
```

## 修复建议

**没装过坏版本的**直接锁版本到`<=1.82.6`

**装过的**别只升级。payload在pip install的时候就已经跑过了。建议：

1. 删掉后门文件，`rm -f ~/.config/sysmon/sysmon.py` 和对应的systemd服务
2. **换所有能换的凭证，**SSH key、云服务key、Git token、数据库密码、钱包助记词
3. 检查Kubernetes集群里有没有`node-setup-*`的pod
4. 重新部署在干净环境里，别在原系统上修修补补

##

这个事暴露了几个问题：

* GitHub Actions的`pull_request_target` workflow设计上有风险
* CI/CD里用apt装工具不锁版本是裸奔
* `.pth`文件作为Python的启动钩子，目前pip没有任何安全检查
* 流行的AI工具链成了供应链攻击的新靶子——LiteLLM、Trivy、KICS都是这类

        攻击者用了同样的RSA key、同样的`tpcp.tar.gz`命名、同样的Telegram频道，横跨三个项目，说明他们是成体系地在做这件事。

参考英文链接:

https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/#stage-3-persistence-and-lateral-movement

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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