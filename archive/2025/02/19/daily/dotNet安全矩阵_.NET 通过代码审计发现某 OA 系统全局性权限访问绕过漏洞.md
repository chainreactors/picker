---
title: .NET 通过代码审计发现某 OA 系统全局性权限访问绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498952&idx=1&sn=a08ebc1ce872683b07a16218dbcbc8e9&chksm=fa595225cd2edb33e2e0624ce93a8e1ad168afdaa762794a6062913e3d523289e1c16b3749af&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-19
fetch_date: 2025-10-06T20:47:26.177969
---

# .NET 通过代码审计发现某 OA 系统全局性权限访问绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8gCOsRWBfquZ6F6Qs5uexSRrJpRNicKaB5ftB3iazMqia9XycpBjypMSy4CqhYzJYhicwZbJjribPicfTg/0?wx_fmt=jpeg)

# .NET 通过代码审计发现某 OA 系统全局性权限访问绕过漏洞

原创

专攻.NET安全的

dotNet安全矩阵

![图片](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

在 .NET 应用程序中，安全漏洞时常成为攻击者突破防线的关键入口。近日，一项全局绕过漏洞的发现引起了广泛关注。该漏洞源自两个组件的协同作用，攻击者只需构造一个特定的URL请求，便能实现对任意接口的未授权访问。

**01. OA系统漏洞背景**

某和OA协同办公管理系统软件共有20多个应用模块，从功能型的协同办公平台上升到管理型协同管理平台，并不断的更新完善，全面支撑企业发展。此系统外部已公开的多个漏洞详情，不难发现都有一些共同的特点，那就是URL里的 .aspx后都会加上一个 / ，然后再进行传递参数。

比如 /RssModulesHttp.aspx/?interfaceID=1，为此有一些对.NET感兴趣的群友们在星球陪伴的微信群里问起这个原因。于是笔者带着群友们这些疑问点抽空研究总结了一下，于是便有了此文。

## 1.1 无扩展名方式

笔者对.NET系统进行漏洞挖掘时第一步喜欢看一下Web.config配置文件，因为此文件包含了一些关于HTTP请求需要经过的管道或者自定义方法，如下图所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9HSnFOVkwZ3rPCKhT0h4WHFI2sC6Kia6TQsLMzLaJkyEUMWCtzpYtOXbLGoc7yh6tDAiboibxAURuLw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

如果觉得图上XML代码看不清楚的话，也可以参考如下这段Web Handler以及Modules配置详情。

```
```
    <modules runAllManagedModulesForAllRequests="true">
      <add name="JHSoft.CustomQuery" type="JHSoft.CustomQuery.HttpUploadModule, JHSoft.CustomQuery">
      </add>
      <add name="HttpUploadModule" type="JHWeb.qqfly.Upload.HttpUploadModule, JHWeb.qqfly.Upload">
      </add>
      <add name="JHSoft.Log" type="JHSoft.Log.LogHttpModule, JHSoft.Log">
      </add>
    </modules>
    <handlers accessPolicy="Read, Script">
      <remove name="ExtensionlessUrlHandler-Integrated-4.0">
      </remove>
      <remove name="OPTIONSVerbHandler">
      </remove>
      <remove name="TRACEVerbHandler">
      </remove>
      <add name="AjaxMethod" verb="POST,GET" path="ajax/*.ashx" type="Ajax.PageHandlerFactory, Ajax">
      </add>
      <add name="scissors" path="scissors.axd" verb="*" type="BitmapCutter.Core.HttpHandler.BitmapScissors,BitmapCutter.Core">
      </add>
      <add name="ExtensionlessUrlHandler-Integrated-4.0" path="*." verb="*" type="System.Web.Handlers.TransferRequestHandler" preCondition="integratedMode,runtimeVersionv4.0">
      </add>
    </handlers>
```
```

上述配置中，我们发现了一个名为ExtensionlessUrlHandler的一般处理程序。关于此handle背景知识是这样的：.NET WebForms框架早期版本中对于URL请求的设计和管理一直沿用经典的ASP风格，通常URL地址上包含文件及扩展名，比如 UserName.aspx、CheckUser.ashx 等。

随着 Web 开发的进步和用户体验需求的提升，陆续出现像MVC框架对无扩展名 URL的需求，即 extensionless URL。

无扩展名 URL 更简洁、易读，用户更容易记住和输入。例如，/about 比 /about.aspx 更直观和易记。

因此.NET框架在后来4.0发布时引入了一个ExtensionlessUrlHandler这是一个专门用于处理无扩展名 URL 请求的 .NET Handler。当启用该配置后基于WebForms框架实现的Web应用便可以像MVC那样通过使用 / 分割路径和参数。

## 1.2 IIS配置映射

比如常见的 /Mall/Product/GetById/10 ，使用该组件时需要当运行在IIS7以上版本，配置Web.config后将会正常处理上面这种 extensionless URL。IIS经典模式用的是aspnet\_isapi.dll，映射DefaultHttpHandler进行处理，如下配置所示。

```
```
<system.webServer>
    <handlers>
        <add name="ExtensionlessUrl-ISAPI-4.0_32bit" path="*." verb="GET,HEAD,POST,DEBUG" modules="IsapiModule"
scriptProcessor="%WINDIR%\Microsoft.NET\Framework\v4.0.30319\aspnet_isapi.dll"
  preCondition="classicMode,runtimeVersionv4.0,bitness32"
  responseBufferLimit="0" />
    </handlers>
</system.webServer>
```
```

集成模式下会映射到System.Web.Handlers.TransferRequestHandle来处理，某和OA便使用此方法进行映射。如下配置所示。

```
```
<system.webServer>
    <handlers>
      <remove name="ExtensionlessUrlHandler-Integrated-4.0" />
      <remove name="OPTIONSVerbHandler" />
      <remove name="TRACEVerbHandler" />
      <add name="ExtensionlessUrlHandler-Integrated-4.0" path="*." verb="*" type="System.Web.Handlers.TransferRequestHandler" preCondition="integratedMode,runtimeVersionv4.0" />
    </handlers>
</system.webServer>
```
```

这段配置中path="\*." 匹配所有无扩展名的 URL 请求，verb="\*" 表示谓词，就是IIS处理所有 HTTP 请求方法，包含了GET/POST/DELETE/PUT 等。

ExtensionlessUrlHandler 的引入就是为了满足当时WebForms应用具备现代 Web 架构对无扩展名 URL 的需求。随着.NET后续版本的迭代和更新，Web框架已不再需要此项配置便可实现无扩展名的URL。

**02. 漏洞代码分析**

我们知道在 .NET 应用程序中，HTTP Modules用于处理进入的 HTTP 请求的生命周期事件。通过自定义 HTTP Modules可以为应用程序添加日志记录、安全验证防护等功能。在企业级应用某和OA中，我们可以看到对 HTTP 模块做了如下配置，例如：

```
```
<modules runAllManagedModulesForAllRequests="true">
    <add name="JHSoft.Log" type="JHSoft.Log.LogHttpModule, JHSoft.Log">
    </add>
</modules>
```
```

上述配置指定HTTP请求需要经过JHSoft.Log.LogHttpModule模块，从名称上看应该是记录请求等日志数据的，其实反编译后发现不仅做了日志的处理，还有对整个请求做了安全校验。具体代码如下所示。

```
```
public class LogHttpModule : IHttpModule
 {
  public void Init(HttpApplication application)
  {
   application.BeginRequest += this.Application_BeginRequest;
   application.AcquireRequestState += this.application_AcquireRequestState;
   application.EndRequest += this.Application_EndRequest;
   application.Error += this.application_Error;
  }
}
```
```

Init 方法用于初始化自定义的模块，并注册一系列事件处理程序，其中AcquireRequestState事件在获取当前请求的状态时触发，常用于检查请求的数据。具体定义如下所示。

```
```
private void application_AcquireRequestState(object sender, EventArgs e)
  {
   HttpApplication httpApplication = (HttpApplication)sender;
   HttpContext context = httpApplication.Context;
   string text = context.Request.Path.ToLower();
   if (!text.EndsWith(".aspx"))
   {
    text.EndsWith(".ashx");
   }
   if (text.EndsWith(".aspx"))
   {
    if (this.SqlFilter(context.Request))
    {
     context.Response.Write("传递的字符中含有敏感字符，操作已停止。");
     context.Response.End();
    }
  }
```
```

代码中对aspx做了深入的处理，通过 context.Request.Path.ToLower(); 获取请求路径并转换为小写，然后text.EndsWith(".aspx") 判断请求路径是否以 .aspx 结尾，如果是则调用 SqlFilter 方法检查请求是否包含敏感字符，这是一个防御SQL注入的方法。这么看如果是.ashx或者.asmx文件有注入漏洞则完全不受该约束，可以顺利的进行SQL注入攻击。

如果没有注入的风险，程序会继续向下执行，通过 if ((context.Session == null || context.Session["UserCode"] == null) ... 检查会话是否为空。

接着通过类似的判断text.IndexOf("/jhsoft.web.login/password.aspx") == -1 排除特定的页面，除此之外所有的请求都会被强制重定向至登录页，如下图所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9HSnFOVkwZ3rPCKhT0h4WHWAia3BcFZ7qpRZOjLibsmQCMOgPSt6O2icf4cr6VNNHskvMsoWn6hDic0A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这里摘抄了一段代码，和某通一样在此处定义了很多需要排除验证的文件，如下所示。

```
```
if ((context.Session  null|| context.Session["UserCode"]null)&& text.IndexOf("/jhsoft.web.login/password.aspx")-1&& text.IndexOf("/jhsoft.web.login/passwordmode.aspx")-1&& text.IndexOf("/jhsoft.web.login/newpass.aspx")-1&& text.IndexOf("/jhsoft.web.epass/epasslogin.aspx")-1&& text.IndexOf("/jhsoft.web.epass/epassloginverify.aspx")-1&& text.IndexOf("/jhsoft.web.epass/epasspersonrepin.aspx")-1&& text.IndexOf("/jhsoft.web.login/installationcontrol.aspx")-1&& text.IndexOf("/jhsoft.web.login/clientcheck.aspx")-1){
  string[] array = text.Split(new char[]
      {
       '/'
      });
      if (array.Length  6)
      {
       context.Response.Redirect("../../../JHSoft.Web.Login/PassWord.aspx");
      }
      else if (array.Length  5)
      {
       context.Response.Redirect("../../JHSoft.Web.Login/PassWord.aspx");
      }
      else
      {
       context.Response.Redirect("~/JHSoft.Web.Login/PassWord.aspx");
      }
}
```
```

我们选择一个文件名测试，访问 /jhsoft.web.workflat/isconnect.aspx 返回了预期的结果，并没有重定向到登录页，如下图所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9HSnFOVkwZ3rPCKhT0h4WHVTAqzzELwrojTibAibEsuuOx9FibBBYCE62BlT2KRW9ibkNicplMJERlcOw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**03. 漏洞实战复现**

经过上面两小节的分析得知，某和OA支持像MVC那样无扩展名的路由请求，而在全局用于检查的AcquireRequestState事件中错误的使用了EndsWith方法判断URL请求是否包含.aspx。

因此，我们可以构造出如下请求达到绕过全局的校验。比如输入/SetImageModule.aspx/id/121212，或者使用 /SetImageModule.aspx/?id=2222 均可以实现未授权访问。效果如下图所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9HSnFOVkwZ3rPCKhT0h4WH9joXBSFeqhFA8FV6CMMsMQKax3KuJCjHNsDbGSVNVopdzyWKgReHZw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

我们以外部公开的RssModulesHttp.aspx存在SQL注入漏洞为例，查看此文件的Page\_Load方法，发现参数 interfaceID 从 Request.QueryString客户端获取后并没有做任何过滤和处理便进入了 GetRssInfo函数，如下图所示

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9HSnFOVkwZ3rPCKhT0h4WHqq9lJ0EUbsAXLGXP1ric59l8uqeIqApq7GVS68OyTwFhPaOOGzPbvxg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

GetRssInfo 方法用于从数据库中获取特定 RSS 接口的信息。它使用传入的 interfaceID 参数来查询数据库中的 WFRssModule 表，并返回查询结果，具体代码如下图所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9HSnFO...