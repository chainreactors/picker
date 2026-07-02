---
title: 使用trae+MCP+sklil进行自动化挖掘漏洞 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/20999711
source: 博客园 - 渗透测试中心
date: 2026-07-01
fetch_date: 2026-07-02T05:57:00.097948
---

# 使用trae+MCP+sklil进行自动化挖掘漏洞 - 渗透测试中心

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [使用trae+MCP+sklil进行自动化挖掘漏洞](https://www.cnblogs.com/backlion/p/20999711 "发布于 2026-07-01 13:25")

### 一、trae下对 burpsuit http mcp工具进行添加

<https://www.trae.ai/download>

![image-20260530150005966](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132504647-1093782383.png)

![image-20260530134359718](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132505648-181432532.png)

![image-20260530134415018](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132506362-1546434620.png)

将下面代码添加到MCP中：

```
 {
   "mcpServers": {
     "burp-ai-agent": {
       "url": "http://127.0.0.1:9876"
     }
   }
 }
```

![image-20260530134455356](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132506930-856481558.png)

### 二、挖掘漏洞的SKILL添加

![image-20260530134638427](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132507570-1950981368.png)

![image-20260530134831664](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132508166-657483666.png)

![image-20260530135002057](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132508999-1223646820.png)

三、bupust的MCP插件添加

通过bupsuit自带的商店插件进行安装mcp 插件

![image-20260530135204988](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132509900-2092323276.png)

然后启动burpsuit MCP,并将本次历史记录中要测试的域名如：www.yunming.com进行添加。

![image-20260530135119062](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132510792-1573337080.png)

四、大模型的选择

这里我选择deepske V4模型，国内的阿里云qianwen3.7max,MIMIMAX2.7都快可以，国内对渗透测试的道德限制少。国外的codex,claude都会有道德限制。特别是codex需要安全身份认证才能用。cluade也能用，需要绕过词进行绕过。

进入deepsek的API后台中心进行购买，且添加key

<https://platform.deepseek.com/api_keys>

![image-20260530140104692](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132511967-467027447.png)

![image-20260530140129513](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132513241-568956959.png)

trae下添加自定义deepsek v4.0版本

![image-20260530135938215](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132513929-87874668.png)

选择自定义模型deepsek

![image-20260530140223674](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132514609-1883152078.png)

![image-20260530140241887](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132515251-368449259.png)

五、站点漏洞测试

<http://testasp.vulnweb.com/showforum.asp?id=0>

对其该网站每个功能都点击测试。

![image-20260530140648044](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132515907-1615798213.png)

在bupsuit中http历史记录中有很多URL连接地址

![image-20260530140726795](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132516615-74415469.png)

对测试的目标在MCP中添加域名

![image-20260530141141205](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132517292-1701565464.png)

然后调用AI对http历史记录进行漏洞分析。

![image-20260530141956030](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132517824-1602582502.png)

![image-20260530142027199](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132518383-448048817.png)

![image-20260530142040308](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132518992-632180836.png)

![image-20260530142051627](https://img2024.cnblogs.com/blog/1049983/202607/1049983-20260701132519593-219784716.png)

[来自为知笔记(Wiz)](http://www.wiz.cn/i/86eb9c97 "来自为知笔记(Wiz)")

posted @
2026-07-01 13:25
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(18)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fbacklion%2Fp%2F20999711&targetId=20999711&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202606/35695-20260624232537069-2004904122.webp)](https://developer.huawei.com/consumer/cn/forum/topic/0201215860119833282?fid=0109140870620153026&ha_source=bky0609&ha_sourceId=89000059)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)