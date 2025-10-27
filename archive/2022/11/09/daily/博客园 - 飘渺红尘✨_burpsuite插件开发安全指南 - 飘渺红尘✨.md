---
title: burpsuite插件开发安全指南 - 飘渺红尘✨
url: https://www.cnblogs.com/piaomiaohongchen/p/16869829.html
source: 博客园 - 飘渺红尘✨
date: 2022-11-09
fetch_date: 2025-10-03T22:05:43.991685
---

# burpsuite插件开发安全指南 - 飘渺红尘✨

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/piaomiaohongchen/)

# [飘渺红尘](https://www.cnblogs.com/piaomiaohongchen)

## 永远年轻永远热泪盈眶,永远在路上 星光不问赶路人,时光不负有心人

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/piaomiaohongchen/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E9%A3%98%E6%B8%BA%E7%BA%A2%E5%B0%98%E2%9C%A8)
* 订阅
* [管理](https://i.cnblogs.com/)

# [burpsuite插件开发安全指南](https://www.cnblogs.com/piaomiaohongchen/p/16869829.html "发布于 2022-11-08 15:16")

我想写一篇文章，关于burpsuite插件开发入门。去年我写了一些burp插件，用于辅助渗透和漏洞挖掘，这给我带来了很多方便，可以捡到一些安全漏洞。

   本人以第一视角说下本人是如何学习burpsuite插件开发的。本文只是入门，如果想要深入学习插件开发，还需要更多的学习和参考。

**1.环境配置和搭建**

```
idea+maven+jdk14(可按照需求,自定义设置jdk版本):

(1)idea创建maven项目  忽略步骤:
```

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108143630815-166838464.png)

   删除掉<properties>标签里的内容

  (2)新增Burp API依赖,pom中引入相关依赖:

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108143717154-1373146280.png)

```
<dependencies>
        <!-- https://mvnrepository.com/artifact/net.portswigger.burp.extender/burp-extender-api -->
        <dependency>
            <groupId>net.portswigger.burp.extender</groupId>
            <artifactId>burp-extender-api</artifactId>
            <version>1.7.22</version>
        </dependency>
    </dependencies>
```

 刷新maven加载jar包:

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108143751396-1036252879.png)

 至此引入依赖成功:

**2. 插件开发基础部分:**

 需求:UI控制台打印hello world:

```
package com.test.DevDemo;

import burp.IBurpExtender;
import burp.IBurpExtenderCallbacks;
import burp.IExtensionHelpers;

import java.io.PrintWriter;

public class BurpExtender implements IBurpExtender {
    private IExtensionHelpers helpers;
    private  IBurpExtenderCallbacks callbacks;
    private PrintWriter stdout;
    @Override
    public void registerExtenderCallbacks(IBurpExtenderCallbacks iBurpExtenderCallbacks) {
        this.callbacks = iBurpExtenderCallbacks;
        //设置插件名字
        this.callbacks.setExtensionName("第一个程序,这是我们的插件名字");
        //打印信息在UI控制台页面,打印内容为hello world
        this.stdout = new PrintWriter(callbacks.getStdout(),true);
        stdout.println("hello world");
    }
}
```

**目录名必须设置成burp目录，类名即文件名必须是BurpExtender:**

**![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108143919387-16307862.png)**

(2)mvn打包jar包，配置打包jar包所需的依赖:

```
<build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                </configuration>
            </plugin>
        </plugins>
    </build>
```

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108143949465-1928872292.png)

(3)idea打开当前终端，输入打包jar包命令:

```
mvn clean install
```

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144022238-87559673.png)

(4)打开当前目录→target

```
open . 打开当前目录
```

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144053317-1175914068.png)

点击target目录，选择BurpPlugDev-1.0-SNAPSHOT-jar-with-dependencies.jar 这个带dependencies的jar包

解释:

```
BurpPlugDev-1.0-SNAPSHOT.jar 为不带依赖的jar包
BurpPlugDev-1.0-SNAPSHOT-jar-with-dependencies.jar 为带依赖的jar包
```

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144120195-94165756.png)

(5)burpsuite引入我们打包的jar包

1.选择插件，选择ADD添加

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144141052-582337311.png)

2.选择jar包，点击NEXT下一步

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144203524-1573842940.png)

3.加载成功，显示插件名字并且打印输出hello world

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144218262-444029569.png)

第一部分结束。

**Burp监听器，侦听器 测试demo使用:**

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144306036-575396763.png)

```
IExtensionStateListener
IHttpListener
IProxyListener
IScannerListener
IScopeChangeListener
```

编写测试代码，参考官方案例:

<https://github.com/PortSwigger/example-event-listeners/blob/master/java/BurpExtender.java>

复制粘贴抄下:

```
package burp;

import burp.IBurpExtender;
import burp.IBurpExtenderCallbacks;
import burp.IExtensionHelpers;

import java.io.PrintWriter;

public class BurpExtender implements IBurpExtender, IHttpListener,
        IProxyListener, IScannerListener, IExtensionStateListener{
    private IExtensionHelpers helpers;
    private  IBurpExtenderCallbacks callbacks;
    private PrintWriter stdout;
    @Override
    public void registerExtenderCallbacks(IBurpExtenderCallbacks iBurpExtenderCallbacks) {
        this.callbacks = iBurpExtenderCallbacks;
        //设置插件名字
        this.callbacks.setExtensionName("第一个程序,这是我们的插件名字");
        //打印信息在UI控制台页面,打印内容为hello world
        this.stdout = new PrintWriter(callbacks.getStdout(),true);
        stdout.println("hello world");
        //一定要注册监听器，不然下面的函数无法生效
        callbacks.registerHttpListener(this);
        callbacks.registerProxyListener(this);
        callbacks.registerScannerListener(this);
        callbacks.registerExtensionStateListener(this);
    }

    @Override
    public void extensionUnloaded() {
        stdout.println("Extension was uploaded");
    }

    @Override
    public void processHttpMessage(int i, boolean b, IHttpRequestResponse iHttpRequestResponse) {
        stdout.println(
                (b ? "HTTP request to ":"HTTP response from ")+iHttpRequestResponse.getHttpService()+"["+callbacks.getToolName(i)+"]"
        );
    }

    @Override
    public void processProxyMessage(boolean b, IInterceptedProxyMessage iInterceptedProxyMessage) {
        stdout.println(
                (b ? "Proxy request to ":"Proxy response from ")+iInterceptedProxyMessage.getMessageInfo().getHttpService()
        );
    }

    @Override
    public void newScanIssue(IScanIssue iScanIssue) {
        stdout.println("New scan issue "+ iScanIssue.getIssueName());
    }
}
```

按照前面说的方法，进行打包运行:

挂上代理访问网站:

可以发现在控制台可以看到Proxy请求信息和HTTP request的请求信息

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144356959-949595335.png)

发现其他信息并没有打印输出?

首先是IScannerListener接口含义，简单来说就是想触发这个接口，需要调度Burpsuite的Scanner扫描功能

![](https://img2022.cnblogs.com/blog/1090320/202211/1090320-20221108144412951-854988013.p...