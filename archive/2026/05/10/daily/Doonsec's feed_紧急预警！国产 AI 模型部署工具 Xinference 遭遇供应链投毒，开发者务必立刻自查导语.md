---
title: 紧急预警！国产 AI 模型部署工具 Xinference 遭遇供应链投毒，开发者务必立刻自查导语
url: https://mp.weixin.qq.com/s/zngc0JC95f1asOkByI9L0Q
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:53:05.338331
---

# 紧急预警！国产 AI 模型部署工具 Xinference 遭遇供应链投毒，开发者务必立刻自查导语

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquP6blibShIicSmonMv4jh8cWLjgvErIiahMMqvVd6audK6DJUFUcYea4YkcwDvt7kVE30qU6ib9nZMWH4ibaxzztWd05EGKPic3038sM/0?wx_fmt=jpeg)

# 紧急预警！国产 AI 模型部署工具 Xinference 遭遇供应链投毒，开发者务必立刻自查导语

原创

OOO
OOO

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquM2G5xOXasyebdbSzpQl9y2epc0B6ad8Zb7LfH8icxfURJIRmia91tHOiaIw5rPGbuHZLh3qL7PANVM0aYuy9XrAFIlAaeeFOrnrY/640?wx_fmt=jpeg&from=appmsg)

近期开源圈曝出重大供应链安全事件：国产热门大模型一键部署工具Xinference遭遇供应链投毒，恶意版本已混入公共仓库，安装即中招，可导致源码泄露、服务器被控、数据被盗等严重后果。所有使用 Xinference 做 AI 模型私有化部署、本地部署、企业内网部署的开发者、运维、AI 创业团队，务必立即自查版本、停止高危安装、做好应急处置。

# 一、事件核心概况

## 1. 涉事项目

Xinference 是国内广泛使用的开源大模型部署推理工具，支持 LLaMA、Qwen、Llama 3、通义千问、百川等几乎所有主流国产 / 开源大模型，主打一键部署、多模型管理、分布式推理，大量个人开发者、高校实验室、中小企业、AI 初创公司都在日常使用。

## 2. 投毒方式

攻击者通过PyPI 第三方包供应链污染方式进行投毒，伪造与官方同名、近似名的恶意包上传至 PyPI 公共源，利用开发者习惯直接pip install xinference的惯性，诱导安装恶意版本，恶意包植入后门木马、远程控制脚本、敏感信息窃取逻辑。

## 3. 影响范围

直接影响：Python 环境下通过 PyPI 直接 pip 安装 Xinference 的个人开发者、服务器、云主机、内网机器；

间接影响：企业私有化 AI 部署、实验室模型训练环境、个人本地开发机、容器 Docker 镜像构建环境；

高危人群：未锁定版本、未换国内可信源、习惯无脑 pip 安装、服务器对外暴露端口的用户。

# 二、恶意版本危害有多大？

一旦误装被投毒的 Xinference 恶意包，攻击者可实现以下高危操作

窃取本地敏感数据读取本机 SSH 密钥、配置文件、数据库账号密码、API 密钥、私有大模型权重路径、项目源码。

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquN8CWgAD5Czc3yHT8jkSiaNpzKujppNNQ4D8mkuMlibReIoiahveAISZMLgMUnoIknicNrdS8VDFOwT4oxGpY9hLnZEgS7HhzUVpib0/640?wx_fmt=png&from=appmsg)

远程控制服务器植入后门实现持久化驻留，任意执行系统命令、上传下载文件、接管服务器权限。

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMwicLDsib1zFMzc7EeQmeDgDgmL98S0amSvSRiavFxm4Fa2sAntT99n3Z92ia7hibcwibFKiatmRDet30U4fnaacnz92ZbfCXSxGCia5Q/640?wx_fmt=png&from=appmsg)

污染模型与业务数据篡改模型推理逻辑、窃取对话业务数据、企业知识库私有数据，造成数据泄露和业务风控事故。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquPApZqebkH4g8uicV0xU1r5oKvxibBlXllznkMbhIpmib0Uvc5OauxE9ZEmbP2aLtQdvZq2uAeaXibxWS8HLHHIGtWQwKVe4kH0BeU/640?wx_fmt=png&from=appmsg)

挖矿与资源占用植入挖矿程序，占用 GPU/CPU 算力，导致模型推理卡顿、服务器资源被耗尽。

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquPEj2kPicR4vSrrv9OexYSiaNkgiaNwGFB0w2ibVzMsVnKJkBBUB9IdpvQ2wwj0Tmn7KeBnUEyRG8ATeLluBxmvn7L5hpY2snbsiaoU/640?wx_fmt=png&from=appmsg)

# 三、为什么这次供应链投毒极易中招？

使用门槛低、受众极广Xinference 作为轻量化大模型部署神器，小白到专业运维都在用，很多人不校验源码、不核对版本。

安装习惯存在巨大漏洞绝大多数用户直接执行：

```
pip install xinference
```

不指定镜像源、不校验哈希、不锁定版本，直接拉取 PyPI 源包，极易被污染包劫持。

名称高度迷惑恶意包刻意模仿官方命名，普通用户很难从包名分辨真伪，没有看官方仓库安装指引的习惯。

开发 / 生产环境混用很多企业直接在生产服务器用默认 pip 源安装，无安全基线、无软件准入审核。

# 四、立即自查：你有没有中招？

## 1. 检查是否安装恶意版本

执行命令查看已安装包信息：

```
pip show xinference
```

核对作者、版本号、仓库地址是否为官方正版。

## 2. 检查 pip 安装源

查看是否使用默认公共 PyPI 源，未配置国内可信镜像源。

```
pip config list
```

## 3. 排查异常进程与网络连接

检查是否有陌生后台进程、异常对外外联 IP、定时任务新增未知脚本。

## 4. 排查 Docker 镜像

若通过 Dockerfilepip install构建镜像，立即停止复用旧镜像，重新基于可信基础镜像构建。

# 五、紧急处置方案

## 1. 立即卸载可疑版本

```
pip uninstall -y xinference
```

## 2. 仅从官方源码仓库安装

拒绝直接 pip 公共源安装，改用官方 GitHub 源码编译安装：

```
git clone https://github.com/xorbitsai/inference.gitcd inferencepip install -e .
```

## 3. 配置可信 Python 镜像源

切换国内安全镜像源，避免被公共 PyPI 污染包劫持。

## 4. 服务器安全加固

限制服务器外网端口暴露，定期排查定时任务、开机自启、陌生用户，重要机器禁止直接公网 pip 安装开源工具，企业内部建立软件白名单，禁止随意安装未知开源包。

## 5. 已中招机器应急处理

立刻断网隔离，防止横向扩散，备份重要数据后全盘查杀，重置所有账号密码、SSH 密钥、数据库凭证，排查日志，确认是否有数据外泄、恶意命令执行记录。

AI 开源生态高速发展的同时，供应链投毒已从传统 Python 包、NPM 包，全面蔓延到大模型部署、推理框架、量化工具等热门项目。Xinference 此次投毒不是个案，未来还会有更多 AI 工具被盯上。

建议大家转发给身边做大模型部署、AI 开发、运维实验室、企业技术团队的朋友，及时排查止损，守住服务器和私有数据安全。

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