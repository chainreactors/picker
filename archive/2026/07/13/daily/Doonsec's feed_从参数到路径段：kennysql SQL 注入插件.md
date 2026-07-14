---
title: 从参数到路径段：kennysql SQL 注入插件
url: https://mp.weixin.qq.com/s/TJCV37En1eoZ7xAqU9sidA
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:46:24.134724
---

# 从参数到路径段：kennysql SQL 注入插件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yOiat0BJcib59yLGcbYiaRTicYPWYu4F5SeKhogXUJlOXO49ichnDqibchAicRSWgKPibB3lA4lBich149jqq8TT9QFic05eRia0gusZYqc0OdejGHliaks/0?wx_fmt=jpeg)

# 从参数到路径段：kennysql SQL 注入插件

原创

Kenny
Kenny

白昼信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# kennysql：一款面向人工复核的 Burp Suite SQL 注入检测器

## 封面摘要

kennysql 是一款基于 Burp Suite Montoya API 开发的 SQL 注入辅助检测插件，支持常规参数、路径段、请求头和隐藏参数检测，并通过响应差异、数据库错误特征和置信度评分帮助测试人员完成初步筛查与人工复核。

---

## 正文

做 Web 安全测试时，SQL 注入并不总是出现在最显眼的参数里。

有些问题藏在重复使用的后端参数中，有些出现在 URL 路径段，还有一些只会在特定请求头或历史参数重新组合后暴露出来。与此同时，仅凭响应长度变化就下结论，又很容易产生误报。

基于这些实际使用中的痛点，我开发了 **kennysql**。

它是一款运行在 Burp Suite 中的 SQL 注入辅助检测插件，定位不是自动化利用工具，而是帮助测试人员更快完成参数筛查、响应对比和证据整理。

> kennysql 仅用于经过明确授权的安全测试、安全研究、本地靶场和教学环境。

### 一、插件界面

插件加载成功后，Burp Suite 顶部会出现 `kennysql` 标签。

【配图 1：插件主界面】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib5ibkA8EXxgDGammosOyohqPTr08icibs8vwSAnItGaVEEBhTMPXSy9xraKQY4Vy2Xnic6vLwv3SbYEKB2N2JribWO3cb5qwO19E0s44/640?wx_fmt=png&from=appmsg)

界面主要分为任务列表、参数结果、详细数据包和功能设置四个区域。扫描过程中的原始请求、变异请求、原始响应、变异响应、差异和判断证据都可以直接查看，不需要在多个窗口之间来回切换。

目前支持的流量入口包括：

* • Proxy 流量监听
* • Repeater 流量监听
* • Burp 右键菜单手动发送
* • 手动扫描指定参数或全部参数

对于可能改变服务端状态的请求，建议优先采用手动扫描，并在测试前确认已经取得明确授权。

### 二、不只检测普通 Query 参数

kennysql 可以提取并检测以下位置：

* • URL Query 参数
* • 表单参数
* • JSON 嵌套参数
* • Cookie 参数
* • URL 路径段
* • User-Agent、Referer、Origin 和业务类 `X-*` 请求头
* • 从同域名历史请求中提取的隐藏参数

每次检测只修改一个目标位置，其余参数和请求结构尽量保持不变，方便比较变异前后的真实差异。

### 三、隐藏参数检测

一些接口在前端请求中没有显式携带某个参数，但后端公共处理逻辑仍可能读取它。kennysql 可以从 Burp Proxy 历史中提取同域名的 GET、表单和 JSON 参数，形成参数资产。

【配图 2：参数资产提取】

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib5iceMnYfWgouR9rkFckdNdibuxewYTLYH6PIS5YictzYswmicId52GEFdD8nrmmUX3X1rQEf7z6ljEXUhIO2KebuBthZfgckicjiaRJ8/640?wx_fmt=png&from=appmsg)

启用“隐藏参数”后，插件会根据目标请求的域名选择历史参数，并按原始参数类型构造 Query、表单或 JSON 请求。多个参数可以先组合成一条完整请求，再逐个修改当前待测参数。

【配图 3：隐藏参数拼接后的变异请求】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib5icViauINsoXC9G4OCAcQ1JynKx3dCUllc5EWNDmjIYtCqrqySzBficwIx1rhDF4ZYSDibVZd0sNhXwlQBkqBmdkMl4BxW7c3qAPFs/640?wx_fmt=png&from=appmsg)

例如参数资产中存在 `act`、`page` 和 `sign`，检测 `act` 时可以形成：

```
GET /apilist?act=search'&page=1&sign=hpjy HTTP/1.1
```

此时只有 `act` 被修改，其他参数继续作为基线值保留，更接近后端接口的实际调用方式。

### 四、路径段检测

普通扫描器通常更关注 URL 最后的 Query 参数，但某些系统会直接使用路径段参与查询或路由后的业务处理。

kennysql 可以按目录层级识别路径段，并在对应位置构造对比请求，而不是简单地把载荷追加到整条 URL 末尾。

下面是一条实际测试中的路径段检测结果。

【配图 4：成功识别路径段 SQL 注入迹象】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib5ibYbFYhSnWVPHvrWQroBYanicLVb6tmNNhO62cb3IVDO8F847oW2ZAwCHSEezXLIniaCDiaCoQYMEZD1XHlyT2WEkBDWmaCgdbr24/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib5ibk19OUTnCz4JFJV7ErWRMFib1hemE1WdMB1NzcUjnxTjibwS33UvDcvWfrfJxojKEP9hR4K1QhFZ28hH3UaXw044AuN1uC7wKQM/640?wx_fmt=png&from=appmsg)

插件在目标路径位置加入测试字符后，响应中新出现了 MySQL 语法错误信息，结果表中同步记录了参数位置、载荷、响应变化和结论。

【配图 5：变异响应中的数据库错误】

响应中出现 `You have an error in your SQL syntax` 和错误码 `1064`，而基线响应中不存在该特征。这类新增的明确数据库错误属于较强证据，但最终仍建议将原始请求和变异请求发送到 Repeater 进行人工复核。

### 五、自定义扫描方案

除了内置的安全初筛载荷，使用者还可以按完整 URL 创建独立扫描方案，为不同接口配置不同的 Payload 集合。

【配图 6：自定义 SQL 扫描方案】

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib5iciaSLT0LkWGsnuUqYgjwpWMg3aH33Zdpm83vYjQf5ianMxhiaepzHAabXW1g8eXiawnpLESW0RODfyNDZucvlT7jd3CEWoKHIMRII/640?wx_fmt=png&from=appmsg)

方案启用后，仅对匹配的目标 URL 生效。这样可以把日常测试中的不同接口分开管理，避免一套 Payload 无差别作用于所有请求。

自定义内容应控制在已授权测试范围内，不建议加入数据库枚举、文件读取、命令执行或其他利用型载荷。

### 六、请求头检测

部分业务会记录、解析或使用请求头内容。kennysql 提供推荐请求头、敏感请求头和完整 Referer 值检测选项。

【配图 7：请求头扫描设置】

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib5ib3IXPSsg97QrUV6642hGChKsZiaISvhvWLCNp70mOYYM5XHoLhZkOE0anwrQlHyib7CQtIiaoHF6RUCyNicf1fEcVaPBRyevUgtjo/640?wx_fmt=png&from=appmsg)

Authorization、Token、Cookie 等敏感字段默认不建议修改。启用相关选项前，应确认不会影响当前会话或触发业务风险。

### 七、判断结果不是只看长度

kennysql 不会因为响应长度发生变化就直接判断存在 SQL 注入。检测过程会综合参考：

* • 数据库错误特征是否只在变异响应中出现
* • HTTP 状态码是否发生稳定变化
* • 标准化后的正文相似度
* • 响应长度变化
* • 响应时间变化
* • 基线页面是否稳定
* • 多个测试结果之间是否具有一致性
* • 是否出现固定的 WAF、验证码或登录失效页面

每条结果都会保留原始请求、变异请求、原始响应、变异响应、差异和自然语言证据。风险提示的作用是帮助排序和定位，不能代替人工确认。

### 八、下载与安装

项目公开地址：

https://github.com/kenny25526/kennysql

### 九、最后说明

SQL 注入检测不是“响应变了就是漏洞”。一个可供复核的结果，至少应该能够说明修改了什么、服务器返回了什么、差异是否稳定，以及为什么值得继续验证。

kennysql 希望解决的正是这部分工作：把分散在请求、响应和日志中的线索整理到一起，让初筛过程更清楚，也让人工复核更方便。

工具仍在持续完善，欢迎在 GitHub Issues 中反馈真实使用中遇到的问题。

---

**工具名称：** kennysql SQL 注入检测器
**作者：** kenny
**QQ：** 1421946905
**QQ 群：** 1021840891
**感谢：** @白昼信安 @M9 @Constantine @Juneha

**授权声明：** 本工具仅用于经过明确授权的安全测试、安全研究、本地靶场和教学环境。请勿用于未授权目标，使用者应自行承担因不当使用产生的责任。

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XvSe1EahHxV1aarZt3GySkHa2Jkl3D3ic6RGia1yI5ePCVZbOQGBlwbibS0K20rfFSsxTeD6b1GLz3ibhLkibE05ibbw/0?wx_fmt=png)

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