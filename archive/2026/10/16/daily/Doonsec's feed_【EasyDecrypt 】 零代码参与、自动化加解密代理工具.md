---
title: 【EasyDecrypt 】 零代码参与、自动化加解密代理工具
url: https://mp.weixin.qq.com/s/njpu5ruPsSUCu5HFJLOnbw
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:30:32.323514
---

# 【EasyDecrypt 】 零代码参与、自动化加解密代理工具

# 【EasyDecrypt 】 零代码参与、自动化加解密代理工具

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 问题背景

在现代应用中（App、小程序、Web），大量接口具备以下特征：

* 请求包/响应包数据加密（AES/SM4/RSA等）

* 服务端校验签名、随机数、时间戳（Sign/Nonce/Timestamp等）

导致安全测试人员在使用 Burp/Yakit 等抓包工具时面临几个常见问题：

* Burp/Yakit 只能看到**加密后的密文**

* 修改参数后**签名校验失败**

* 重放数据包每次都需要**修改报文**的 Nonce 等防重放字段

## 工具介绍

1、该工具基于 Python + Mitmproxy 构建一个上下游代理架构，主要用于解决安全测试中流量加密不可见、验签无法绕过的难题。工具亮点：

* **无需编写代码**来处理加解密/签名，工具内置“加解密/签名/字符串处理/编码转化”等规则

* 配置好规则即可对请求/响应报文按规则处理，对用户完全透明

2、上游代理：

* 负责拦截来自浏览器/小程序的请求报文，对业务层加密报文进行自动解密和结构还原，使 Burp 等抓包工具能够直接查看和修改明文数据

* 接收 Burp 修改后的明文响应，自动完成重新加密与签名生成，确保数据能够以符合业务协议的形式正确发往浏览器/小程序

3、下游代理：

* 负责接收 Burp 修改后的明文请求，自动完成重新加密与签名生成，确保数据能够以符合业务协议的形式正确发送到目标服务器

* 介绍来自服务器的响应报文，对加密的响应报文进行自动解密和结构还原，使 Burp 等抓包工具能够直接查看和修改明文数据

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj55khRBeQWuG768EKfnRdibwwv6Cm9u9U8hcvaiaZBmn9oXzefm82ZDjzjomRKmtkaJuPdf7MbA9BqDT3CBeBAuBXf8HrxictFPibXE/640?wx_fmt=png&from=appmsg)

## 界面介绍

1、启动上/下游代理规则界面主要用于管理整个代理链路的规则加载与监听端口设置，核心由三部分组成：

* 上/下游代理规则：用于展示当前可用的规则集，并支持按需选择和加载不同的规则

* 监听端口：用于设置代理链路的关键通信端口，其中包括

+ 上游监听端口（用于接收浏览器/小程序流量，默认为 8081）

+ Burp监听端口（作为中间抓包与调试节点，默认为 8080）

+ 下游监听端口（用于转发至目标服务器的出口端口，默认为 8082）

* 日志窗体：记录执行规则过程中报错接口、报错信息等内容。方便排查问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj54qibH1iaojoROILHR6NaT1DKiakdzyuhqFPjRmueTOYTRKKxDYibqR6m7pqg1EWbwCFBlnJ0oSIFW8JnHe4GJDrfzPWibianlYFXwgo/640?wx_fmt=png&from=appmsg)

2、上/下游代理规则配置页面， 其核心目标是将请求/响应的加密、解密、签名逻辑抽象为可配置的规则集合，并在代理链路中动态生效。该界面具体组件如下

* **规则基础内容**：

+ 规则名称：唯一主键，保存后无法修改

+ 匹配域名：用于匹配请求/响应包的域名

+ 匹配路径： 支持多路径精确匹配（暂不支持正则匹配）

+ 请求/响应：分为request和response两种类型

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj54ib0pPRJF7BibIRb4cT1nFQqqH0QDfOrWnzPDQrefTA0Aia5ba2W7fFIKlibIETptB0ibAqMwRhoRNrib5NhCXXOFjkJ8AiaicAia4l2N8/640?wx_fmt=png&from=appmsg)

* **规则集合管理**：记录上/下游保存过的所有规则（上/下游规则通过菜单栏的 Upstream 和 Downstream 区分）

+ 橘子图标：点击后展示指定规则的“基础内容”和对请求报文的“操作函数集合”

+ 青苹果图标：点击后展示指定规则的“基础内容”和对响应报文的“操作函数集合”

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj577veQNYbsbebeKHD4SeZ6vXvMzJrJtvqnFqMtkibcjKwia4mzyLm0LZRv47jGd9dXgACOgvft5SQP6kBZmBpvfLmgBB3dG3BZhQ/640?wx_fmt=png&from=appmsg)

* **操作函数集合**：用于定义和展示某条规则内部的处理逻辑链路

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj550EPeP96W78ybrtN94lt1031eIwIHDO8dibdlILTbHeyia7BHoicSic3d8bFiaTh1mm6n5LXVPVzLSnMFTKOcQE4ezvETUIK2QGCiaY/640?wx_fmt=png&from=appmsg)

* **操作函数配置窗体**：点击新增按钮弹出操作函数配置窗口，通过“函数选择 + 输入输出变量选择”的方式定义请求/响应报文的处理逻辑

+ 函数类别/Type1： 用于定义操作函数的一级分类，例如编码/解码、加密/解密、哈希算法、时间戳生成等，用于确定操作函数的功能域

+ 具体函数实现/Type2：在 Type1 分类基础上进一步细化具体算法或实现方式，具体可用函数如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj56gDKumPQVKwmoRPCgS5ZXJSjGJeWcick9YPHAsUCVnKo9wtGZcRqhibSlo1fnlLfD3ev7zt1bk6Z24XZPpK41uDuORMkWWru6H4/640?wx_fmt=png&from=appmsg)

+ 输出变量定义/Output： 用于定义当前操作函数的结果变量名，执行结果将绑定至该变量，可在后续函数节点中作为输入被继续调用

+ 输入参数绑定/Input： 根据 Type1 与 Type2 的选择动态生成对应的输入参数结构， 用于从请求/响应报文中提取变量或引用上游节点的输出变量，实现跨节点数据流传递

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj55JicMlXos0CJL6Bw29E8QpSZ9Iu9b6TDwGpgrr3ZHj7Dw1vlAPuNYShCzXAJY3Xe5G2I8PyBQqqEqk0RydFLzCYZQNc6mTVYIY/640?wx_fmt=png&from=appmsg)

* **规则执行与验证**：

+ 验证规则：点击下方验证按钮。自上而下执行操作函数，并将执行结果输出到执行日志窗口，同时会将当前配置的“规则基础内容 + 操作函数集合 + 请求/响应报文”保存

+ 左边文本框中保存为待处理的请求/响应报文，可通过在 Burp 等抓包工具中直接复制

+ 右边文本框中保存为执行规则后的请求/响应报文

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj550RPqFd2c7ThCmhs54WXggFdwiaU5uGAOkCKyuMib1voZ35oYGvrol6ibokA2l05L5uTJ4nZZic4RomryviaNG7wh0KtgPpW6fhPBY/640?wx_fmt=png&from=appmsg)

## 工具使用过程

* Upstream/Downstream 窗体

+ 输入规则名称、匹配域名、匹配路径、请求/响应

+ 根据请求/响应的类型，在左边文本框中复制 Burp 的请求/响应报文

+ 添加操作函数，对请求/响应报文进行逻辑处理（建议每添加一个操作函数做一次验证，这样既能实时保存进度，也能查看当前步骤是否存在问题）

+ 验证规则的可用性（至此规则保存后可重复使用，无需再次配置）

* Start 窗体

+ 选择保存的上/下游规则

+ 输入上游、下游、Burp监听端口，启动上/下游代理

* 本机代理配置

+ 配置浏览器/小程序的下一跳代理到“上游监听端口”

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj577xO4wKQZgCqTEh2G0BjxmXia4AZTgbibaQebtiaW7BrUEJ1DMo4miaF27b5TVPQROrP513bN1EhTov6O1Z75WnoZBoWcJOexibc9A/640?wx_fmt=png&from=appmsg)

+ 配置 Burp 的下一跳代理到“下游监听端口”

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj54QsrXPmzXXzuMaxvlbW1EDYsRqIgIHTT1DicYBdBzN0DmnVibK4NvAhz2KyEEAFwibP2PmsicsjItwHiaFd0bp1b6xZy6YA4y1ibOLw/640?wx_fmt=png&from=appmsg)

* Mitmproxy 证书安装（火狐浏览器需要在浏览器中安装证书，具体安装方式可以自行百度）

+ windows 主机选择 Cert 文件夹下的 .cer 证书

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj54jiaWDnTAGqqGJMT4Yn7ITJ5zibBBBNFYeibXFc5KibNowyppxdsib9AIuk7icMicWKg4ic5tZB93iarQhU7iaRRhVmta8giagv7ENMbiaVfI/640?wx_fmt=png&from=appmsg)

+ 双击证书-安装证书-收信人的根证书颁发机构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57ySevM39uVatv2uyWkMHCYW5cb4icYeAsY760FMxpzULCKmTbHeBtfS7MyKKpY0WWibXdIECG35swDvw1eu3rW5bGOF0ZibwfWjs/640?wx_fmt=png&from=appmsg)

* 正常访问指定规则的网站，在 Burp 中查看请求/响应报文是否按照规则修改

## 靶场实战

### 防重放测试

* 以 encrypt-labs 靶场测试，输入账号+密码并选择禁止重放选项

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj55xLWPQlibuCExQNKrAAlo096hFaHyMOribb9kAt2Tqa3Rsibo1uapAopVTUJfOBBfYl2dK8T1AiaJxibJkDqaAcP7Uibam9Ho2RYO9k/640?wx_fmt=png&from=appmsg)

* 在 Burp 中重放请求包提示 No Repeater，该接口存在防重放机制。整个数据包中只有 random 可能是防重放校验字段

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj559vesdH2Qf9b3M7sFCShy8FLCmeQXYCTw9U64nLQuzPfdtHDNhHQAhicLANwEpakhXp6pksazLAiasbnLRteXAPrCKFDk9pPdK0/640?wx_fmt=png&from=appmsg)

* 前端代码分析 random 的生成方式，得到 random = RSA(timestamp())

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj570RiaUu3RlAnNgsUjg3a2O3J05dIpA2RGtAoz5yvo2CDiaUjcKOHYF0up1G75g8dicKibSjvGLqseicggJriagPtsfXfUbTenueQEcU/640?wx_fmt=png&from=appmsg)

* 分析整个浏览器 -&gt; Burp -&gt; 目标服务器的流量链路，上游代理无需介入业务参数处理。所有与请求相关的动态修改（例如 random 值的重写）只需要在下游代理中完成

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57TuuI6ick4avjRUcyly0Jo9XPJticcVxKwbK4MndpnmBPExr9Z449uV75XyzTecZDiaHSHtzlPIiceBTse37uKV2JIjDoBpJOnzcI/640?wx_fmt=png&from=appmsg)

* 了解了需要设置下游代理、业务参数处理逻辑后，在 Downstream 下游代理规则配置页面配置操作函数

+ 首先是通过 Time 函数获取当前时间戳并赋值到 time 变量

+ 接下来通过 RSA 加密函数对 time 变量进行加密并赋值到 random 变量

+ 最后通过 SetParams 函数将 random 变量赋值给 POST 的 random 字段

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56cAnBxibibvLawtd55AdHXt2zj8n8JiaN9sznOFk5Oofdja2Zkg0CrzwpyuT83udWvOvVcXKmdRJyc6q0X8Bay3xBUCqMc4KYKicE/640?wx_fmt=png&from=appmsg)

* 配置好规则后点击验证按钮，可以在右侧文本框中看到修改后的请求包，且在执行日志中看到每个步骤的执行过程

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57QoIsrRLHibia0aaUKJD2x1OS462VuWH4sdaXd6y2YAafu6PicU4cCiakcE7aiakPHlhtk9h9B13fo3IRoicyzX9iaEXUPwaX1BgpNy0/640?wx_fmt=png&from=appmsg)

* 最后去 Start 页面去选择要加载的规则，只需要开启下游代理来处理来自 Burp 的请求包

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56tXJBRicuicsxL2PghfVkCa3O6BnLRsUgeQNr54TNmEU49vTrNNMcMXPuGA578dDnQ20NkXGdRCH18nJeFUALGkVXbeeENCuwbE/640?wx_fmt=png&from=appmsg)

* 在 Burp 中修改请求包且给 random 随便改个值，响应包看到仍绕过了重放检验。

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56ibBDa4xp8hibDAzmPPFIRgvvHZgwOKZunTicCRzdzZQY3zcfGHCBARSmqiaE3ibXmRrXibBnRgx5iaEG4tKypoC3l8DVPXJWjVp4MVI/640?wx_fmt=png&from=appmsg)

### AES加解密测试

* 同样以 encrypt-labs 靶场测试，输入账号+密码并选择 AES 固定 Key 选项

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57JqHYkuWlMTFHQfTVY8ibKMRS1mnQIBjlxMqvOuR7WXXhCV1owv400JqlGR5qtbtSdft40eKNLjSziaIArIbcasv519Hdj14qWo/640?wx_fmt=png&from=appmsg)

* 在 Burp 中看到请求包的 encryptedData 字段加密，无法对字段中的内容进行随意修改

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj55M41RzuWOKLfX28eIJ5wFLmicjib5JgSMzicwocMr7HQUEwiauxDPnicIFVxsKEmEIRZVDcQfqkNXqIeycgtsP9mTbZuSrIp0x1rRQ/640?wx_fmt=png&from=appmsg)

* 前端代码分析 encryptedData 的生成方式，得到 encryptedData = AES(data)

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57h1HI7eX67qpSPna6xxicY0uAQoMAyEooU8E6nn4ic6Clee7PocDOyZriaYfS3VpTPayiab3jrgxLuiaQPVZAaUibjvY8KEOfAlXcAI/640?wx_fmt=png&from=appmsg)

分析整个浏览器 -&gt; Burp -&gt; 目标服务器的流量链路，上游代理需要对 encryptedData 字段进行解密。而 Burp 得到明文可以进行任意修改，而下游代理需要对明文内容进行重新加密。

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57d0Y6nEIsl7O6ZhrSwTV9iciaiaFxWTUcTWgdiaoAXbng9vn8DYQHouiacdiahNKiaowvBnDsZxmILlS322k8ypUoUn3q1aEbW3nxqDM/640?wx_fmt=png&from=appmsg)

* 了解了需要设置上下游代理、业务参数处理逻辑后，分别在 Upstream/Downstream 上下游代理规则配置页面配置操作函数，这里简单以上游代理为例

+ 首先是通过 GetParams 函数获取请求包中 POST 的 encryptedData 字段并赋值为 encryptedData 变量

+ 接下来通过生成字符串函数新建 iv 和 key 变量用于后续 AES 加密

+ 通过 AESDecrypt 函数将对 encryptedData 变量进行加密并赋值给 decdata 变量

+ 最后通过 SetParams 函数将 decdata 变量赋值给 POST 的 encryptedData 字段

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj552k0VhcibHy4yX0pHbJfXR1icUur0NhWV9yUc...