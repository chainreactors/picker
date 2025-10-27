---
title: .NET 通过代码审计发现某办公系统逻辑绕过漏洞可泄露管理员账户和密码
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247499017&idx=1&sn=c17b802fed118434bf2134310fadc29e&chksm=fa5953e4cd2edaf2ec66ff6e982d6bf1f1641351ca4a8a43050c08709373f498234341967b72&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-28
fetch_date: 2025-10-06T20:38:24.179049
---

# .NET 通过代码审计发现某办公系统逻辑绕过漏洞可泄露管理员账户和密码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Yicg4uU8WY8RBMv1Ofe7sfGnAaImVkjILib5dwxTJpF9C8B5dIOuiadudnSqNhWLGCnuhARffakM8oBw/0?wx_fmt=jpeg)

# .NET 通过代码审计发现某办公系统逻辑绕过漏洞可泄露管理员账户和密码

原创

专攻.NET安全的

dotNet安全矩阵

![图片](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

在 .NET 应用程序中，安全漏洞时常成为攻击者突破防线的关键入口。近日，一项逻辑绕过漏洞的发现引起了广泛关注。攻击者只需构造一个特定的URL请求，便能实现让接口泄露管理员敏感信息，包括用户名和密码，因此，在日常的代码审计和评估的环节需要格外留意该漏洞类型引发的安全漏洞。

**01. 逻辑绕过漏洞**

某个系统的一个公开的接口存在敏感信息泄露漏洞，可导致攻击者通过请求该接口获取后台管理员账户和密码。具体的数据包如下所示。

```
```
POST /Sys**.ashx HTTP/1.1
Host: xx.xx.xx.xx
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36

page=1&arr_search=%7B%22username%22%3A%22%22%2C%22memo%22%3A%22%22%7D&funcName=get****
```
```

上述请求构造的POST请求，参数arr\_search是一段URL编码的JSON字符串，包含了搜索参数，其中username和memo都是空字符串，发送请求后在页面返回显示所有的系统用户和密码等信息。如下图所示

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9A5E6ZOibCjEJ2xs5OaGL2l2yykukrHa58MJ529MwzvcFsMeCAybWsu3gZXnWEviaIc8HiczHERibpNg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

为此有一些对.NET感兴趣的群友们在星球陪伴的微信群里问起这个原因。于是笔者带着群友们这些疑问点抽空研究总结了一下。

**02. 逻辑漏洞分析**

存在漏洞的是一个.NET Handler，首先从HTTP请求的表单数据中获取arr\_search参数，用JSON库进行解析，提取username和memo字段的值，接着，调用getOperators方法，根据解析的username和memo参数查询数据，具体方法的实现代码如下所示。

```
```
public static DataSet getOperators(string name, string roles, int pageSize, int pageIndex)
{
    SqlParameter[] expr_06 = new SqlParameter[]
    {
        new SqlParameter("@name", "%" + name + "%"),
        new SqlParameter("@roles", roles)
    };
    string str = "select * from admin where 1=1";
    string statisticSql = "select count(1) userCount from qx where 1=1";
    string where = "";
    if (name != "")
    {
        where += " and username like @name";
    }
    if (roles != "")
    {
        where += " and admin in(select node from people where people_name=@roles)";
    }
    str += where;
    statisticSql += where;
    return SqlHelper.GetPageList(expr_06, str, "admin", pageSize, pageIndex, statisticSql);
}
```
```

该方法内部据传入的参数name和roles，构建SQL查询条件，这里使用了参数化查询避免了SQL注入漏洞，但是此处却是模糊查询导致为空的情况下搜索出所有的用户敏感数据。

## 小结

综上，该系统虽然不存在SQL注入漏洞，但是这样的逻辑代码却引发了另一个逻辑漏洞导致泄露管理员的账户和密码等敏感信息，也证明了 Web应用程序在配置和权限管理上的薄弱环节，因此不当的配置可能导致严重的安全漏洞。

**03. NET代码审计学习**

微软的.NET技术广泛应用于全球企业级产品，包括其知名的**Exchange**、**SharePoint**等，国内如 **某友的Cloud**、**某通的T系列**、**某蝶的云产品**等也广泛采用。各行业核心业务均依赖于此技术。这些基于.NET的系统频繁遭攻击，问题涵盖任意文件上传、反序列化漏洞、SQL注入、文件下载漏洞、命令执行漏洞等。

截至目前，星球已推出近**100节内容** (还在持续增加)，包括**70个视频+30份PDF文档**。我们已将内容细致划分为15个分类，并随新漏洞类型的出现持续扩展。在这里您将学到包括但不限于以下漏洞类型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8fTUcmnHC8g2WjE6SZJIjwdR00lAaNpUuDDlI6Gk1uEEPZxUMlb4FkDvOBLYq92InlzpwmzWeibjQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

详细的内容与结构，请参考下方的星球大纲版块，包括但不限于OWASP十大漏洞类型，涉及SQL注入漏洞、文件上传下载漏洞、任意文件操作漏洞、XML外部实体注入漏洞、跨站脚本攻击漏洞、反序列化漏洞、命令执行漏洞、未授权和越权漏洞、第三方组件漏洞等等。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8fTUcmnHC8g2WjE6SZJIjwMahhN19jbtUiax5UWVU0R3n4eick9XQEHyf3lhjE3wvCic9ZFD3h9tWsQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 专属福利

1. 学习模式: 代码审计知识星球**在线录播视频** +后续漏洞挖掘直播、内部专属交流社区答疑解惑；

2. 优享福利：加入.NET代码审计星球后**赠送永久**dot.Net安全基础入门星球。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkE3ACnPUtfbn99XZmI6ANI9DCxS2KHkqiaXBk22ZevuRm08onmEibIUvdEy5zJGCoHg4HAsrgQ22w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 课程评价

欢迎对.NET代码审计关注和关心的同学加入我们 [dot.Net安全代码审计] ，目前已有近 100+ 位朋友抢先预定。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yicg4uU8WY8RBMv1Ofe7sfGnpcCfEUPuS43icYEwibLpibKKKdLHr6PsQic3VDl3ibyfOB3P0RvBW882g4Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yicg4uU8WY8RBMv1Ofe7sfGnyoVeAYtJVBnLCiaxsQibuJEK5bR98xBUQBVicfKCVlOqffxXfeFxVwgTA/640?wx_fmt=png&from=appmsg)

星球门票后期价格随着内容和质量的不断沉淀会适当提高，**越早加入越划算！** 现在加入星球可享受星球早鸟价，并可**领取100元优惠券**，期待在这里能遇到有情有义的小伙伴，大家聚在一起做一件有意义的事，**可扫描下方老师二维码了解更多详情。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkE3ACnPUtfbn99XZmI6ANBJ4t8XC4ibbWjhzj0447zAJcWgwV9wcDhcibNiax3P7iagSYwn31GEkTBw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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