---
title: 【代码审计】Fortify浅用
url: https://mp.weixin.qq.com/s/hp9GEmRuD61yUl7jTmzlKg
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:51:12.837162
---

# 【代码审计】Fortify浅用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ocg1gpicEs1uXOTVia4ATn3HJ6ZicLkfyFhVTzyYgzwcnhlOr7icLKmssiaTicvEbiclCXk0JzPnUmnwF2tFV6EM5G3Q24mU3wSJQY6QeDve18X8cU/0?wx_fmt=jpeg)

# 【代码审计】Fortify浅用

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 快乐的一天从摸鱼开始，又从摸鱼结束

## 目录

1. 启动`Fortify`工具
2. 选择项目`JDK`版本
3. 扫描参数配置
4. 启动漏洞扫描
5. 扫描漏洞数量分析（含`Maven`依赖配置）
6. 漏洞抽样分析（以`SQL`注入为例）
7. 审计报告导出
8. `Fortify`工具获取与安装

---

## 1. 启动Fortify

启动`Fortify`工具后，首先需区分项目类型，重点区分`Java`项目与其他类型项目，便于后续针对性配置扫描规则。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1ttKib6YDDFHV0WaBtLvHrprFtVb5zlC8yQOkVIyCv4Mu9xicmR54Jt3nJzhQvGOSkGMXoxoURlMaLVsicTfX5kctOJeibfLMgiajHQ/640?wx_fmt=png&from=appmsg)

## 2. 选择项目的JDK版本

根据当前审计项目的实际`JDK`版本进行选择，确保扫描环境与项目运行环境一致，避免因版本不匹配导致扫描异常或结果偏差。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1tQvYQ1wS2BlicDbFyEibCPNibbugCQCEyTgKsUcnsIziapxOleDChtAvBKHQzFKCZHWtAwvKPThLKH2qB2M9TJGOtKibDqrkDNZd2k/640?wx_fmt=png&from=appmsg)

## 3. 扫描配置

进入扫描配置界面，按以下标准配置参数，兼顾安全风险覆盖与代码质量检测，适配`Java EE`项目场景：

1. 安全关注度：`Show me all issues that may have security implications` 覆盖全量安全风险，适配远程+本地双重防护，不遗漏潜在安全隐患；
2. 代码质量：`Show me all code quality issues` 兼顾安全检测与代码规范、项目稳定性，同步排查代码层面的非安全类问题；
3. 是否`Java EE`应用：`Yes` 启用`Java EE`专属扫描规则，针对性检测`Java EE`项目特有的安全漏洞；
4. 是否高权限运行：`Yes` 强化高权限场景下的风险检测，确保高权限操作相关的漏洞无遗漏。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1v5uG2LicabURnqW7Ue1tkibxBwx9ickkiaTnZ0Ju6VvLkGklywKXkicpJM1nbAo2XfNp1PPEUqNE4qwEiaSqlIicKk1M3lNkjk63Z3X4/640?wx_fmt=png&from=appmsg)

## 4. 开始扫描

配置完成后，点击开始扫描，扫描时长根据项目大小而定，期间无需手动操作，等待扫描完成即可。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1shxNloQ3x42g5B2wqlAvibe1siaPcz0KjC05llzexh1eKl2zSN88twxSX0edmicStMS73ArFlPFZdmfgePpxoOdhBpMXNGEYBbbg/640?wx_fmt=png&from=appmsg)

## 5. 扫描漏洞数量分析

扫描完成后，查看初步扫描结果，会发现存在较多漏报情况——甚至基础的`SQL`注入漏洞都未被检测出来。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1sHofsOibbianApIdwA6DHX1svlkoGkZfCPc0nzUnag2FBElnLW1XjS8UpM15nNAibrdnP6Svu4mxuL1wtIcAwfd4ChmMXygZrY9U/640?wx_fmt=png&from=appmsg)

核心原因是**未导入项目完整依赖**，导致`Fortify`无法全面解析项目代码，扫描结果不准确。因此，需通过`Maven`导入项目完整依赖，同时配置国内镜像解决网络访问问题，具体操作如下。

### 5.1 配置Maven镜像与本地仓库

在用户目录（路径：`C:\Users\xxx\.m2\`）下，找到`settings.xml`文件（若不存在则新建），添加如下配置：

```
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">

    <!-- 阿里云镜像（解决Maven网络访问问题）-->
    <mirrors>
        <mirror>
            <id>aliyunmaven</id>
            <mirrorOf>central</mirrorOf>
            <name>Aliyun Maven</name>
            <url>https://maven.aliyun.com/repository/public</url>
        </mirror>
    </mirrors>

    <!-- 本地仓库位置（建议修改到指定路径，避免C盘占用过大） -->
    <localRepository>D:/local_repository</localRepository>

</settings>
```

### 5.2 导入项目依赖

打开项目根目录（含`pom.xml`文件），执行如下`Maven`命令，导入项目所有第三方依赖：

```
mvn clean compile
```

### 5.3 项目迁移（无Maven环境场景）

若需将项目迁移到无`Maven`环境的电脑上进行审计，可执行如下命令，将所有第三方依赖包合并到项目中，便于直接移动整个项目：

```
mvn dependency:copy-dependencies
```

执行完成后，所有依赖`jar`包会自动复制到项目目录下的 `target/dependency/` 文件夹中。

### 5.4 重新扫描验证

导入完整依赖后，重启`Fortify`工具，重新执行扫描操作，得到的扫描结果会大幅完善，之前未检测出的`SQL`注入等漏洞也能被精准识别。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1unwMtuZI9CffJhgCPaGxcibFpZQmR21akGichwmWoIOSMXfl9h7LeQu4RCbLc3LOk2e4bAWxrQkeictu0YJgABANE3oblFvOyXZ4/640?wx_fmt=png&from=appmsg)

## 6. 漏洞抽样分析

选取扫描结果中的一个`SQL`注入漏洞，结合`Fortify`的`Diagram`视图进行深度分析，可清晰发现：数据从`source`（输入源）到`sink`（执行点）的传输过程中，未经过任何过滤处理，且未使用预编译语句，最终导致SQL注入漏洞产生。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1tfW0bXjmTibicSGNNGtwI2RZsJXXvVG92WYf0AhWaaMImvUS3AGJF5cNpIM0ZccOEP1ze9jDqaz3STktXgWlSgbMaAUD9yQklEE/640?wx_fmt=png&from=appmsg)

同时，`Fortify`提供完整的函数调用栈，可直观追溯漏洞产生的代码路径，便于快速定位问题根源、分析漏洞危害。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1vCDCL36gfO95icKvcOiaLplDC8SA6YVThFJzpXQV78wCiaUbpMibhibCSDG5mia47GLCaK2zYj5vIs4icYb7Q9ibz3SdhnD2EdMJ3V8gA/640?wx_fmt=png&from=appmsg)

**注：** 其他漏洞不再详细分析，该靶场代码已在前期通过手工方式完整审计过。

## 7. 报告导出

实际审计工作中，一般不使用`Fortify`自带的报告导出功能，相关操作界面参考如下。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1v93BaSnvhk6WYQaiaeKGNyKtx7w69SJAqxr7kYhnY1ahR8BNe4ic6Hic7JIJ5Bb5ZcMDLbhX5O5bSpfsGcHbHyWpEHWy9DuVUw4w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tzcLmffMCtYW063ROyZjNdz7Kn4vpEdEMNYqnJrCkiakn4JKSZBLs9meRY7DTGLryLY2CL8XHLoBapGib43Wyy7sWtliaIwYHsHU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1s4I52evNket6gYf9WYw8VhsrYCIJoicObg9Xadnv4ZOOSfOWvKCa8seE5QwuicEYeRPCsyKHXH8BjIfE4qZwgfo5rsvdo3jTN30/640?wx_fmt=png&from=appmsg)

## 8. Fortify工具获取以及安装教程

网上一大把，不写了。

摸鱼跑路，byby~~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

十月的进阶之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

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