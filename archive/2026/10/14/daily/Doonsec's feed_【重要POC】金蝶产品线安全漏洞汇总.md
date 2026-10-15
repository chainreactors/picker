---
title: 【重要POC】金蝶产品线安全漏洞汇总
url: https://mp.weixin.qq.com/s/XmioDZX0SquMgir32tQKgg
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:42:31.288013
---

# 【重要POC】金蝶产品线安全漏洞汇总

# 【重要POC】金蝶产品线安全漏洞汇总

原创

mourenzheng
mourenzheng

网络安全民工

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 金蝶产品线安全漏洞汇总

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribRHXPZlnZibPmZnibIk6K5OlJOQE4J5DynvCaDpos5wBPudvG8JWzsXtphSCs3icjjU6yqjZoH8ibuXUUxpZMV5AU16icJVICY4SqDE/640?wx_fmt=png&from=appmsg)

> 整理范围：金蝶云星空（K3Cloud）、金蝶 EAS / EAS Cloud、金蝶 Apusic 应用服务器、金蝶 KIS 云、金蝶 AI 苍穹 / 星瀚，以及部分历史产品线。
>  用途：安全自查、漏洞管理、补丁跟踪、WAF/IPS 规则梳理。
>  注意：请仅用于授权安全测试与防御加固，禁止未授权攻击。

---

## 目录

* 一、金蝶云星空（K3Cloud / Cloud-Starry-Sky）
* 二、金蝶 EAS / EAS Cloud
* 三、金蝶 Apusic 应用服务器（天燕中间件）
* 四、金蝶 KIS 云
* 五、金蝶 AI 苍穹 / 星瀚
* 六、金蝶医疗 / 云之家（历史）
* 七、新增漏洞清单速览
* 八、通用修复与缓解建议
* 九、参考来源

---

# 一、金蝶云星空（K3Cloud / Cloud-Starry-Sky）

## 1.1 反序列化远程代码执行（BinaryFormatter RCE）

### 1.1.1 `.kdsvc` 接口 BinaryFormatter 反序列化 RCE

* **漏洞标题**：金蝶云星空管理中心/应用层 BinaryFormatter 反序列化远程代码执行漏洞
* **漏洞概述**：管理中心通信层默认采用 BinaryFormatter，序列化与反序列化过程未签名或校验。攻击者可篡改序列化数据，在服务端反序列化时造成远程命令执行，完全控制服务器。
* **影响版本**：

+ 6.x：≤ 6.2.1012.4
+ 7.x：7.0.352.16 ~ 7.7.0.202111
+ 8.x：8.0.0.202205 ~ 8.1.0.20221110

* **漏洞 URL**：已公开 9 个 `.kdsvc` 接口，路径前缀 `/K3Cloud/`：

1. `Kingdee.BOS.ServiceFacade.ServicesStub.User.UserService.SaveUserPassport.common.kdsvc?dcInfo=11`
2. `Kingdee.BOS.ServiceFacade.ServicesStub.InOutDataService.GetImportOutData.common.kdsvc`
3. `Kingdee.BOS.ServiceFacade.ServicesStub.DevReportService.GetBusinessobjectData.common.kdsvc`
4. `Kingdee.BOS.ServiceFacade.ServicesStub.ServiceGateway.GetServiceUri.common.kdsvc`
5. `Kingdee.BOS.ServiceFacade.ServicesStub.DynamicForm.DynamicFormService.CloseForm.common.kdsvc`
6. `Kingdee.BOS.ServiceFacade.ServicesStub.AppDesigner.AppDesignerService.RecordCurDevCodeInfo.common.kdsvc`
7. `Kingdee.BOS.ServiceFacade.ServicesStub.BusinessData.BusinessDataService.BatchLoad.common.kdsvc`
8. `Kingdee.BOS.ServiceFacade.ServicesStub.Account.AccountService.GetDataCenterList.common.kdsvc`
9. `Kingdee.BOS.ServiceFacade.ServicesStub.BusinessData.BusinessDataService.Audit.common.kdsvc`

* **POC/利用要点**：

+ 请求方法：`POST`
+ `Content-Type: text/json`
+ 参数格式示例：`ap0/ap1/ap2` 按方法参数位置传入序列化数据，`format=3` 或 `format=Binary`
+ 也支持 `parameters` 参数格式
+ 请求头 `cmd` 可指定命令；仅部分链支持回显

* **漏洞编号**：QVD-2023-14179 / CNVD-2024-13011
* **修复建议**：升级官方补丁；限制 `.kdsvc` 接口暴露；禁用不安全 BinaryFormatter；增加签名校验与白名单。

### 1.1.2 ServiceGateway.GetServiceUri.common 反序列化漏洞

* **漏洞标题**：金蝶云星空 ServiceGateway.GetServiceUri.common 接口反序列化漏洞
* **漏洞概述**：`servicegateway-getserviceuri-common` 存在反序列化漏洞，外部攻击者可通过恶意手段获取权限，进而接管服务器控制权。
* **影响版本**：金蝶云星空 6.x / 7.x / 8.x 私有云和混合云部署
* **漏洞 URL**：`/Kingdee.BOS.ServiceFacade.ServicesStub.ServiceGateway.GetServiceUri.common.kdsvc`
* **漏洞编号**：攻击 ID 1070210427
* **备注**：2024 年攻防演练中列为高危漏洞。

### 1.1.3 UserService 反序列化漏洞

* **漏洞标题**：金蝶云星空 UserService 接口反序列化漏洞
* **漏洞概述**：`UserService` 接口存在反序列化漏洞，未授权攻击者可直接利用此漏洞执行系统命令，获取服务器权限。
* **影响版本**：金蝶云星空
* **漏洞 URL**：`/Kingdee.BOS.ServiceFacade.ServicesStub.User.UserService.*`
* **检测**：已有公开 Nuclei 模板 `kingdee-cloud-user-deserialization-vuln`，严重级别 critical。
* **漏洞编号**：原文未提供

### 1.1.4 BusinessDataService.BatchLoad.common.kdsvc 代码执行漏洞

* **漏洞标题**：金蝶云星空 BatchLoad 接口代码执行漏洞
* **漏洞概述**：`BatchLoad.common.kdsvc` 接口存在代码执行漏洞。
* **影响版本**：金蝶云星空
* **漏洞 URL**：`/kingdee.BOS.ServiceFacade.ServicesStub.BusinessData.BusinessDataService.BatchLoad.common.kdsvc`
* **漏洞编号**：CVD-2025-3153
* **备注**：关联资产数约 541，全系产品可检测、可验证。

### 1.1.5 kdsvc 通用反序列化漏洞

* **漏洞标题**：金蝶云 K3 API `common.kdsvc` 反序列化漏洞
* **漏洞概述**：客户端发出的数据可被攻击者恶意篡改，写入包含恶意代码的序列化数据，达到在服务端远程命令执行的效果。
* **影响版本**：金蝶云星空、金蝶 OA 等使用 `.kdsvc` 接口的产品
* **漏洞 URL**：`/Kingdee.BOS.ServiceFacade.ServicesStub.DevReportService.GetBusinessObjectData.common.kdsvc`
* **漏洞编号**：攻击 ID 1070210290 / 1070210447

### 1.1.6 管理中心反序列化 RCE（默认 8000 端口）

* **漏洞标题**：金蝶云星空管理中心反序列化命令执行漏洞
* **漏洞概述**：管理中心通信层默认采用二进制数据格式，序列化/反序列化过程未签名或校验，攻击者可篡改数据实现 RCE。管理中心默认开放于 8000 端口。
* **影响版本**：金蝶云星空 6.x 等
* **漏洞 URL**：管理中心默认端口 8000
* **利用方式**：公开资料提及“反序列化 RCE + 内存马”利用方式。
* **漏洞编号**：原文未提供

---

## 1.2 任意文件上传

### 1.2.1 ScpSupRegHandler 任意文件上传

* **漏洞标题**：金蝶云星空私有云任意文件上传漏洞（ScpSupRegHandler）
* **漏洞概述**：`ScpSupRegHandler` 接口未严格验证上传路径和后缀，可通过路径穿越上传恶意脚本，执行任意代码。POC/EXP 已公开流传，存在在野利用。
* **影响版本**：V6.2（含 17 年 12 月补丁）至 V8.1（含 23 年 9 月补丁）；企业版私有云、企业版私有云（订阅）、标准版私有云（订阅）。
* **漏洞 URL**：`/k3cloud/SRM/ScpSupRegHandler`
* **POC/检测要点**：

+ 上传表单字段：`dbId_v`、`FID`、`FAtt`
+ 文件名示例：`../../../../uploadfiles/test.ashx.`
+ 访问路径示例：`/K3Cloud/uploadfiles/Test.ashx`
+ Snort 检测规则：

  text

  ```
  alert tcp any any -> any any (msg:"Kingdee Upload Vulnerability(QVD-2023-44581)"; flow:to_server,established; content:"POST"; http_method; content:"ScpSupRegHandler"; http_uri; sid:1000001;)
  ```

* **漏洞编号**：QVD-2023-44581 / KDPSIRT-2023-00023

### 1.2.2 MOBFileUpload 任意文件上传

* **漏洞标题**：金蝶云星空 MOBFileUpload 任意文件上传漏洞
* **漏洞概述**：`MOBFileUpload` 接口存在任意文件上传漏洞，已纳入 Xray 等主流扫描器检测规则。
* **影响版本**：金蝶 K3 Cloud 财务软件系统
* **漏洞 URL**：`/K3Cloud/MOBFileUpload`
* **POC/检测要点**：

  http

  ```
  POST /K3Cloud/MOBFileUpload HTTP/1.1 Content-Type: multipart/form-data
  ```
* **漏洞编号**：原文未提供

---

## 1.3 任意文件读取/下载

### 1.3.1 CommonFileServer 任意文件读取

* **漏洞标题**：金蝶云星空 CommonFileServer 接口任意文件读取漏洞
* **漏洞概述**：`CommonFileServer` 未做权限校验和路径过滤，可读取服务器任意文件。该接口同时被 CNVD-2021-86835 收录（管理中心任意文件读取）。
* **影响版本**：V7.X、V8.X 所有私有云和混合云版本
* **漏洞 URL**：`/K3Cloud/CommonFileServer/` 或 `/CommonFileServer/`（管理中心）
* **POC/检测要点**：

  http

  ```
  GET /K3Cloud/CommonFileServer/../../../../Windows/win.ini HTTP/1.1
  ```

  http

  ```
  GET /CommonFileServer/c%3A%2Fwindows%2Fwin.ini HTTP/1.1
  ```
* **漏洞编号**：CNVD-2021-86835

### 1.3.2 FileProxyHandler.kdfile 任意文件下载

* **漏洞标题**：金蝶云星空 FileProxyHandler.kdfile 接口任意文件下载漏洞
* **漏洞概述**：`FileProxyHandler.kdfile` 存在任意文件下载漏洞，可读取配置文件、数据库凭据等。
* **影响版本**：金蝶云星空
* **漏洞 URL**：`/K3Cloud/FileProxyHandler.kdfile`
* **POC/检测要点**：

  http

  ```
  GET /K3Cloud/FileProxyHandler.kdfile?path=../../../Windows/win.ini HTTP/1.1
  ```
* **漏洞编号**：原文未提供

---

## 1.4 模板引擎注入（SSTI）

### 1.4.1 Freemarker 模板引擎注入

* **漏洞标题**：Kingdee Cloud-Starry-Sky Enterprise Edition Freemarker 模板引擎注入漏洞
* **漏洞概述**：Freemarker 引擎组件中 `plugin.buildMobilePopHtml` 函数未对模板特殊元素过滤，可利用 SSTI 执行恶意代码。官方修复版将 Freemarker 设置为 `ALLOWS_NOTHING_RESOLVER`。
* **影响版本**：6.x / 7.x / 8.x / 9.0
* **漏洞 URL**：`/k3/o2o/bos/webapp/action/DynamicForm4Action.class`（`plugin.buildMobilePopHtml` 函数）
* **CVE 编号**：CVE-2025-6761

---

## 1.5 远程命令执行（RCE）

### 1.5.1 星空私有云 BBC 系统远程命令执行

* **漏洞标题**：星空私有云 BBC 系统存在远程命令执行漏洞
* **漏洞概述**：BBC 系统存在命令注入，攻击者可远程执行未授权命令，获取服务器敏感数据。漏洞等级为严重。
* **影响版本**：星空私有云 BBC 系统
* **漏洞 URL**：KDPSIRT-2025-00090（官方安全公告，具体接口未公开）
* **POC**：官方未公开
* **关联编号**：KDPSIRT-2025-00090 / 00091 / 00093 / 00097 / 00100；修复方案已合并，解决 KDPSIRT-2025-00100 即可。

---

## 1.6 XML 实体注入（XXE）

### 1.6.1 金蝶云 K3 Cloud XML 实体注入

* **漏洞标题**：金蝶云 K3 Cloud 存在 XML 实体注入漏洞
* **漏洞概述**：未对 XML 外部实体有效过滤，可利用 XXE 读取服务器敏感文件。
* **影响版本**：金蝶云 K3Cloud v6.0
* **漏洞 URL**：CNVD-2019-37191，具体接口未公开
* **POC**：CNVD 附件暂不公开

---

## 1.7 业务逻辑漏洞

### 1.7.1 金蝶云星空管理中心业务逻辑漏洞

* **漏洞标题**：金蝶云星空管理中心业务逻辑漏洞
* **漏洞概述**：管理中心业务接口存在业务逻辑漏洞，会导致业务处理异常，无法正常访问。漏洞等级为高危。
* **影响版本**：企业版私有云、企业版私有云（订阅）、标准版私有云（订阅）
* **漏洞位置**：`\k3\o2o\bos\webapp\action\DynamicForm4Action.class`
* **组件**：Freemarker Engine
* **利用方式**：利用 Freemarker 模板注入语法执行任意命令
* **漏洞 URL**：KDPSIRT-2026-00036（具体接口未公开）
* **POC**：官方未公开

---

# 二、金蝶 EAS / EAS Cloud

## 2.1 反序列化/远程代码执行

### 2.1.1 `appUtil.jsp` Fastjson 反序列化命令执行

* **漏洞标题**：金蝶 EAS `appUtil.jsp` 存在 Fastjson 反序列化命令执行漏洞
* **漏洞概述**：`appUtil.jsp` 使用 Fastjson 解析 `list` 参数，可构造恶意 JSON 触发反序列化，实现 RCE。
* **影响版本**：金蝶 EAS 8.0/8.1/8.2/8.5、EAS Cloud 8.6/8.6.1/8.8
* **漏洞 URL**：`/easportal/tools/appUtil.jsp`
* **POC/检测要点**：

  http

  ```
  GET /easportal/tools/appUtil.jsp?list=%7B%22x%22%3A%7B%22%40type%22%3A%22java.net.Inet4Address%22%2C%22val%22%3A%22dnslog地址%22%7D%7D HTTP/1.1
  ```

  解码后 JSON：

  json

  ```
  {"x":{"@type":"java.net.Inet4Address","val":"dnslog地址"}}
  ```

  Nuclei 检测：`nuclei -t kingdee-eas-apputil-rce.yaml -l targets.txt`
* **漏洞编号**：原文未提供

### 2.1.2 `autoLogin.jsp` Fastjson 远程代码执行

* **漏洞标题**：金蝶 EAS Cloud `autoLogin.jsp` Fastjson 远程代码执行漏洞
* **漏洞概述**：`autoLogin.jsp` 同样使用 Fastjson 解析参数，与 `appUtil.jsp` 属于同源漏洞...