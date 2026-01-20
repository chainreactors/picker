---
title: 代码审计之SpringBoot_Servlet_MVC框架
url: https://mp.weixin.qq.com/s/6GX4vUt_Xh0mEvoYPAcylQ
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:47.665971
---

# 代码审计之SpringBoot_Servlet_MVC框架

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKQd7pf9d27Py6uHaNkoyiaCQNQBR7HWticic4UPCK7yu68lK9jDcdy1DIA/0?wx_fmt=jpeg)

# 代码审计之SpringBoot\_Servlet\_MVC框架

原创

secureyang
secureyang

secureyang

![]()

在小说阅读器中沉浸阅读

本公众号所发文章仅用于技术交流学习，不得用于任何违法犯罪目的，一切后果自行承担，与本公众号以及作者无关。

SpringBoot\_Servlet\_MVC框架搭建tomcat容器，开启web服务servlet生命周期servlet路由方式我们首先学习第一种路由方式：注解路由web.xml 路由方式参数传递Spring框架M（module）V（view）C（Controller）框架

# SpringBoot\_Servlet\_MVC框架

首先，打开我的IDEA2021.3

第一步：新建项目

![image-20250525102816286](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKNJXbWmBHIS2RDsUibbBmjFaDJgribYVvQ7ga8kGayIEulNuxuK8ZgJNw/640?wx_fmt=png&from=appmsg)

第二步：新建 maven 模块

![image-20250525102914600](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKTMbRQ3V7gzqXeZobqR3br3T3fjX2EiafUibYDBfEoN3n8NL3Pl9MJM0w/640?wx_fmt=png&from=appmsg)

![image-20250525102950780](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKDfRGIH9Vc5dzSzPpibkAecQaDiamAZiaibJiadse4LMw4fuLic2YBrJDYVUA/640?wx_fmt=png&from=appmsg)

创建完项目之后，

第三步：添加框架支持，直接添加 WEB应用程序

![image-20250525103044040](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKFeTpVe7cBNTZgwu5RKAN8E9JnoSZ3uicIRC96vA2iaTmia3kJC39YAtibQ/640?wx_fmt=png&from=appmsg)

![image-20250525103123426](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKS7wWvBOLjWNFTx27VxDibicKLn7GPicviaWyJA1lwBxOJAjgDg98AYmIVg/640?wx_fmt=png&from=appmsg)

**此时，项目的路由方式就有两种，分别是 web.xml 路由，还有就是在代码中使用注解进行路由**

## 搭建tomcat容器，开启web服务

进入 tomcat 官网https://tomcat.apache.org/去下载一个tomcat，我这里是

![image-20250525103634195](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKiaAC7icpmKGcdjaztmgBx8wVvsxq4Djb0wYrOnP80yL8ZyWcnbjSQlwA/640?wx_fmt=png&from=appmsg)

![image-20250525103928741](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKKSccsXyZsNLHRcticM5JHYeens1sMhgZ76RgYOQsOQtMhTMVQNBGGuQ/640?wx_fmt=png&from=appmsg)

然后在IDEA中添加tomcat框架

![image-20250525110712916](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKddwson4wCIicm4uoqCF1S17ESQiakcCTVMk13EczzeoQ0ynjPrawtqkA/640?wx_fmt=png&from=appmsg)

![image-20250525110747027](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKUX0kUEttyo0EBjjsicCkibk6mDmmyEIuwlz1jexG9e29LKhlice9uQeQQ/640?wx_fmt=png&from=appmsg)

![image-20250525110940222](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKkYSojxiaNbH5GRFaBGdibKE7WibO3DsWuMXcIGtadqNnV5kILic5Dsxsvw/640?wx_fmt=png&from=appmsg)

在这里配置好你的URL，以及端口信息

![image-20250525111039496](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKz5uiaiajkXVmvf4ibibXjviajiak6SFzajDZiaaDoic3rXlE9vD1fiaTq84wC9g/640?wx_fmt=png&from=appmsg)

![image-20250525111228604](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK98ARz3lwFa1aKVWPlrzSY5Na2IjMXx4RN7KGj2XantHt7kOTgFQeibA/640?wx_fmt=png&from=appmsg)

如果不删掉的话，我们在访问页面的时候就要写这么一长串，很影响体验感

完成之后，点击

![image-20250525111917795](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKRwNfPKEBV0PVYndatRr1bZZA7VTrJO5ZF1Ev2bV0qr8W58U60cS4DA/640?wx_fmt=png&from=appmsg)

运行 tomcat 容器

最终结果，如下所示，其实正是我们 index.jsp 默认页面的代码展示效果

![image-20250525111957341](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKd6uF5ZOeOnsDI86QCUEFlApd0QAtMEk3vCQm0sq7w6xCzZCJjV1xqQ/640?wx_fmt=png&from=appmsg)

![image-20250525112027819](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKSN5ic5VpRGg1P36qAUZ6zlxK0dCQYZntzrPtpV96mLOibhou520sk1zA/640?wx_fmt=png&from=appmsg)

## servlet生命周期

servlet的生命周期主要是三个阶段，分别是如下所示，同时，代码的运行顺序，也是与生命周期一致的。

init（初始化状态） -》 service（服务状态） -》 destroy（销毁状态）

## servlet路由方式

首先，Servlet第一步，要给项目添加一个java库，这个java的库就是tomcat里携带的库。

![image-20250525113029178](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKen7uJCvnkFsiap8MVsQjqUmP4oPsbDt4QHwunO4RVic7kic8ib7LicrqgvA/640?wx_fmt=png&from=appmsg)

![image-20250525113048437](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKYLeNBROAFw1bUlddfEC6mnBjnodKPTIpAeaHB2sYcJ63nvtnQzMpkg/640?wx_fmt=png&from=appmsg)

![image-20250525113159888](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKUqS4piaxRm9XSc7yVhLMEc4uznz5JGPLzDT1ibqPmACkfRP2s9ibiaVzNQ/640?wx_fmt=png&from=appmsg)

![image-20250525113233074](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKvibXBoMytygBqJdmq5p2I7x0zZQDicxIyd4pMVrvib5f2iay483NDBVmGQ/640?wx_fmt=png&from=appmsg)

然后这个库其实就可以帮我们完成http的各种请求，传参等操作，就有点类似于在 python 中 import requests 差不多。只不过 tomcat 中库非常多，一个一个导入很复杂，所以直接导入 lib

![image-20250525152210995](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKk14SeadPetlLoOc4AK91laLVpB4E4EwsXiasJzveQZntjf9MrhhL4zA/640?wx_fmt=png&from=appmsg)

![image-20250525152229251](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKuYnUzQoHxyd4XWbFvaa1M7v5u9hATsPziabU3uN7epHIUEQaz7iaScLw/640?wx_fmt=png&from=appmsg)

![image-20250525152302170](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKT5CgQFMDymtrGwOFxicGricHc7TmibJFh5WYGR59RtuYgdAjTWznKr26w/640?wx_fmt=png&from=appmsg)

按住 ctrl 就可以多选

然后我们重写 doGet 和 doPost 方法

### 我们首先学习第一种路由方式：注解路由

如图所示：

![image-20250525152510025](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKNibAviaNSWD15sPnz449xLiaWCZeibUPlYziafEMmf3KCA9Sfib3ezrz8KKA/640?wx_fmt=png&from=appmsg)

此时我们访问站点的时候跟上 /helloservlet 即可实现访问该页面路由，因为这种访问方式是以GET方式请求的

![image-20250525152720000](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKDChWTN4AKia3CqRIeibkcEsnOxrw5gFtoEe5CTIdkGc3MiaHCOJlaDcsw/640?wx_fmt=png&from=appmsg)

此时在日志当中就会输出 doGet

![image-20250525152738401](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK5YoshoW3jLF1uTPnqiaxUBIW65gsYxoXY2NeySiavO3pibQkoaSfPrg9Q/640?wx_fmt=png&from=appmsg)

我们再试试以POST方式请求

![image-20250525153454492](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKfTcCgl5fibsB2Sbm8WCYF88pjZHib4KGF2Qvk4M5uibjlRVqy4B1BfFGQ/640?wx_fmt=png&from=appmsg)

当然，针对上面的 doGet 和 doPost 路由方式，在 servlet 里面有一个总的路由方式，就是生命周期里面的service方法

访问这个方法，它会自动去判断，到底是 doGet 还是 doPost

![image-20250525160345963](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK1cknZLXdichqs26xSdzmPpwJHjVu39uVuXmdbIUer5FwLUVS8qkQicfA/640?wx_fmt=png&from=appmsg)

但我不知道为什么此时doGet方法不调用了，只调用 service 方法

而 destroy 生命周期方法一般是在该程序运行结束

### web.xml 路由方式

![image-20250525161652777](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKwspiaREShQ4EGcOt6dqgguogKrTSMa9pPv59j8pv2AxJ5aCJRNKCj5g/640?wx_fmt=png&from=appmsg)

![image-20250525161738253](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKQ3X6FK89ceDeYoHJribYNQiaRmIibAGDSCey4aeeYoTBy4AC33xGFCLMA/640?wx_fmt=png&from=appmsg)

一样可以

> 经过验证之后，如果两种路由方式都有的话，那么都可以正常使用。
>
> 但此时可能就会有人问了，如果 web.xml 的路由方式与 注解路由方式的路由名称是一样的，那会先运行哪个代码呢？我们来试一下
>
> 好的，报错了
>
> ![image-20250525162246111](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKJQBOxW3OjnbA7BvQIqzPfic4jcvEbkeeDuicwey1JMpuTOQ3BR7Gn0hA/640?wx_fmt=png&from=appmsg)

## 参数传递

![image-20250525162731472](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKjMJAdwicpTGOOvMn4cqhUdwbKdiaZVWSbhS6m5RZBPHTOF3TYOyff0hQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKKziboNYgYvwjOY1Jpe93UAibtsR4Pu6Aa4mYoNtJsJybeOrJqbDicOUiag/640?wx_fmt=png&from=appmsg)

像这种直接响应我们输入内容的，就是典型的xss

![image-20250525164802666](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKWnSLGypnLic8miadrczaHhSlwFVuZ3ISJ63TCdIkloBkaAicus0vAibA9w/640?wx_fmt=png&from=appmsg)

> 如何让我们不用重启tomcat也可以随时更新编写的代码
>
> ![image-20250525163225760](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKAPUtydX81jXeG0Y4fbp2hs6U06Qic27O6Hy7TUf2xVcTZZyV1SIf47Q/640?wx_fmt=png&from=appmsg)
>
> ![image-20250525163351664](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKNuEMcedicUADjibMKTviayabBiaE4WnwJV3VrSLTzEqkAXE2XYgKVANrnQ/640?wx_fmt=png&from=appmsg)
>
> 在部署里面，选择war exploded方式，这...