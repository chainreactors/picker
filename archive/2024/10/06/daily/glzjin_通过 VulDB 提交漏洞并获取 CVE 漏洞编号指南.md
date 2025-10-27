---
title: 通过 VulDB 提交漏洞并获取 CVE 漏洞编号指南
url: https://www.zhaoj.in/read-9027.html
source: glzjin
date: 2024-10-06
fetch_date: 2025-10-06T18:49:32.014797
---

# 通过 VulDB 提交漏洞并获取 CVE 漏洞编号指南

[![glzjin](https://www.zhaoj.in/wp-content/uploads/2016/04/1460635478e753758d45e5fb95f465e8ceaaabe897.png)](https://www.zhaoj.in/ "glzjin")

西兴街道物理安全研究员 | 原学生@北京联合大学 | 信息安全爱好者 | 全栈开发 | OSCP | OSWE | OSEP | OSED | OSCE3 | OSWA | OSWP | OSDA | OSMR | KLCP | CISSP | ASCP | S+ | PMP | 为心中的美好而战

* [上一篇文章](https://www.zhaoj.in/read-8958.html)
* [下一篇文章](https://www.zhaoj.in/read-9046.html)

* [Glzjin](https://www.zhaoj.in/read-author/glzjin "作者简介")

切换导航

* [首页](https://www.zhaoj.in "首页")
* [Support Me!](https://www.zhaoj.in/support-me "Support Me!")

## [通过 VulDB 提交漏洞并获取 CVE 漏洞编号指南](https://www.zhaoj.in/read-9027.html)

张贴在 [2024年10月5日](https://www.zhaoj.in/read-date/2024/10/05 "通过 VulDB 提交漏洞并获取 CVE 漏洞编号指南") 来自 [Glzjin](https://www.zhaoj.in/read-author/glzjin) in  [技术](https://www.zhaoj.in/read-category/tech "查看技术中的全部文章")

Table of Contents

Toggle

* [前言](#%E5%89%8D%E8%A8%80 "前言")
* [步骤](#%E6%AD%A5%E9%AA%A4 "步骤")

## 前言

通过 VulDB 来提交漏洞并获取 CVE 编号确实比直接邮件去提交和获取 CVE 编号快很多，来记录和分享一下。

## 步骤

1.先准备好你的漏洞文档，可以按照如下的格式来书写。

```
## Title: SQL Injection Vulnerability in WebAppX ≤ 1.2.3

**BUG_Author:** your_username

**Affected Version:** WebAppX ≤ 1.2.3

**Vendor:** [WebAppX GitHub Repository](https://github.com/example/WebAppX)

**Software:** [WebAppX](https://github.com/example/WebAppX)

**Vulnerability Files:**
- `app/controller/user.class.php`

## Description:

1. **SQL Injection via User Login:**
   - In the file `app/controller/user.class.php`, the login function does not properly sanitize user input before using it in an SQL query.
   - This can be exploited by sending a crafted request to the login endpoint with malicious SQL code.

2. **Exploiting the SQL Injection:**
   - By injecting SQL commands into the username or password fields, an attacker can manipulate the SQL query to bypass authentication or extract sensitive information from the database.

3. **Example SQL Injection Payload:**
   - The following payload can be used to bypass authentication:
     ```
     Username: ' OR '1'='1
     Password: ' OR '1'='1
     ```

4. **Requesting the Login Endpoint:**
   - Make a request to the login endpoint with the SQL injection payload:
     ```
     http://<target-ip>/index.php?user/login
     ```
   - Use the above payload in the username and password fields.

5. **Verifying the Exploit:**
   - If the injection is successful, the attacker will be logged in as an authenticated user without needing valid credentials.

## Proof of Concept:

1. Access the login page of the vulnerable application:
   ```
   http://<target-ip>/index.php?user/login
   ```

2. Use the following credentials to attempt login:
   ```
   Username: ' OR '1'='1
   Password: ' OR '1'='1
   ```

3. If successful, the application will log in the attacker without requiring valid credentials.
```

2. 然后把写好的漏洞文档放到某个可以被公开访问的链接上，比如我是放到自己的笔记库里。也可以放到飞书文档或者石墨文档，开公开分享即可。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/17281152246c304fd4f93b8ddcef1691095cb422a9-1024x739.png)
![](https://www.zhaoj.in/wp-content/uploads/2024/10/172811524176e9d7475666b5b14d0120d231719f01-1024x532.png)

3. 然后打开 <https://vuldb.com/>，选择到 Signup，注册一个新账号。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/17281154815dfb4ac88a1b4b84728bfe7a7084d457-1024x718.png)

然后填入相关信息，进行注册。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/172811550715bf644feac0db07f72bc374b29c3d37-1024x604.png)

点击“Signup”提交注册请求。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/17281156383250983a01ba347162a001134829add7-1024x305.png)

4. 然后到邮箱里点击链接确认注册请求。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/17281157564d03720f13f1e581a1407db949928ed1-1024x569.png)

然后在打开的链接里设定用户名和密码，点击“Signup”完成注册。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/1728115805e5f3ab60bc910646514023f37214954f-1024x534.png)

5. 然后点击 ENTRIES->ADD，进入漏洞提交页面。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/1728116542a1cf5b681f9faf1a520e0ecfc54cb486-1024x753.png)

用英语填写漏洞信息。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/1728116733b0fa72667837fa349b89be8650751629-1024x533.png)

切记要把最后请求这个 CVE 编号的按钮点上。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/17281169133398716996039fa8941e08a90391b4b3-1024x533.png)

6. 然后点击“ADD”完成提交。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/1728117008625c9c6cc044fc03216312f98c85277c-1024x310.png)

7. 在审核通过后，就会直接分配CVE编号了。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/1728117053bd4a3f847b574b96a316f8ceb7db91bd-1024x37.png)

一般几个小时后就可以被检索到了。

![](https://www.zhaoj.in/wp-content/uploads/2024/10/17281172525fef58afed143de420dca7ad79f5f423-1024x561.png)
![](https://www.zhaoj.in/wp-content/uploads/2024/10/17281172410d55a0b1e32c47be783a5e20646acb44-1024x561.png)

### 发表回复 [取消回复](/read-9027.html#respond)

[ ]

Δ

这个站点使用 Akismet 来减少垃圾评论。[了解你的评论数据如何被处理](https://akismet.com/privacy/)。

搜索：

## 徽章

[![](https://www.zhaoj.in/wp-content/uploads/2023/01/16734445325571d75c6436fa548006cddc04f6ef1c-300x300.png)](https://www.credential.net/654f2e4d-5a2e-459d-94fb-e117222189e9)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/1673444615edb40fbf418bc270edb03369b4b7bbc3-300x300.png)](https://www.credential.net/7e97fcef-5e89-40af-b1f4-44c47c1769a2)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/1673445191c6c3ab3b6e1d855d4792b4ba2d27b500.png)](https://www.credential.net/32a355ca-b457-441c-b389-9d4f6366309a)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/16734452706cbff8050d185a5d2ca8b9692bd97028.png)](https://www.credential.net/2db25872-7a1d-4dc0-86d5-15b791f4a61a)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/167344535978763b8411b74ea06bed1717e8074d75.png)](https://www.credential.net/dc62a4d2-6dc6-4228-9239-41b0da2be656)
[![](https://www.zhaoj.in/wp-content/uploads/2023/02/1676555742e09433176ae66bc87039f0b7b0422118.png)](https://www.credential.net/06524a6d-c8a3-4038-a8eb-090b096a2262)
[![](https://www.zhaoj.in/wp-content/uploads/2023/02/1676555747cb011870763281fa215d0c9455c5e3c1.png)](https://www.credential.net/0bf8a228-9ce4-4483-a8c3-f4ee75f56a5d)
[![](https://www.zhaoj.in/wp-content/uploads/2023/03/1677771656d2008b9c0d3c40d41c002c0864debaf3.png)](https://www.credential.net/8534d4fe-0f91-4681-9b7f-997d198df348)
[![](https://www.zhaoj.in/wp-content/uploads/2023/05/1683419874c9a3e47c563365b54d1b984805089b65.png)](https://www.credential.net/323868a7-3020-4f71-8a6c-8f35c7b9f16e)
[![](https://www.zhaoj.in/wp-content/uploads/2023/08/16920252635e4e7eae17044686e78ab5e5320ec13e.png)](https://www.credential.net/c6114609-71cf-45bd-afd5-1b81279e08fd)
[![](https://www.zhaoj.in/wp-content/uploads/2023/05/168315770646f0d8a9332b8a7dc7279c768e506133.png)](https://www.credly.com/badges/b184262f-6522-4510-a8c7-e6c78f51a3b6/public_url)
[![](https://www.zhaoj.in/wp-content/uploads/2023/10/16974592460a56d06d649541552c71a8b681de164f.png)](https://www.credly.com/badges/7b7bc694-9783-46f8-8f32-2f138abb0139/public_url)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/16734456142f9c80ea30c2f23de9e687e64aa2d9cb.png)](https://www.credly.com/badges/d68f72b5-55c6-4f32-8323-b979d9f46987/public_url)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/1673446237b5cd39a62b1f9bae1ce7b867b9deb321.png)](https://www.credly.com/badges/2cf7a1cb-1265-4de1-80f9-c1219e1d3446/public_url)
[![](https://www.zhaoj.in/wp-content/uploads/2024/01/1706314689e3db153dc97b27d897cbbfafe41adf7a.png)](https://www.credly.com/badges/f632a20c-a32a-4c8c-9c99-d68a0c20fddf/public_url)
[![](https://www.zhaoj.in/wp-content/uploads/2024/01/17063146400e05263b21c2ce75ddcf25fbe71ae4b2.png)](https://www.credly.com/badges/0a8d4753-9e1c-4c22-b392-4b4148950447/public_url)

### 归档

* [2025 年 2 月](https://www.zhaoj.in/read-date/2025/02)
* [2024 年 10 月](https://www.zhaoj.in/read-date/2024/10)
* [2024 年 8 月](https://www.zhaoj.in/read-date/2024/08)
* [2024 年 5 月](https://www.zhaoj.in/read-date/2024/05)
* [2024 年 4 月](https://www.zhaoj.in/read-date/2024/04)
* [2023 年 10 月](https://www.zhaoj.in/read-date/2023/10)
* [2023 年 8 月](https://www.zhaoj.in/read-date/2023/08)
* [2023 年 5 月](...