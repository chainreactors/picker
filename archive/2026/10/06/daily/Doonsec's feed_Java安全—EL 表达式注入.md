---
title: Java安全—EL 表达式注入
url: https://mp.weixin.qq.com/s/Qm5yMaZVICpowh3IUtp3aA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:54:51.472188
---

# Java安全—EL 表达式注入

# Java安全—EL 表达式注入

原创

lys
lys

绿洲安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/yucJ5603pv6y9MicQevnPpS4CsCLTb4vl1TvOp58mSichNPWK2ibaZVbjg7xCnL6M4RDBu4PpbibwK9NszHvNfvHJA/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/mhIicicHPJQWHJs7GmXyfEYSLiadDbOoO8fdkFSzWf6j1blmwDCmIWqgnzJwkryWsJ6CtOskUMHnnEIuicHtyCq4jQ/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

**由于传播、利用本公众号绿洲安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号绿洲安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢**

```
参考连接https://drun1baby.top/2022/09/23/Java-%E4%B9%8B-EL-%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B3%A8%E5%85%A5/
```

## 0x01 前言

继续

## 0x02 EL 表达式的前世今生

* 要简单了解一下 EL 表达式的背景，有助于我们更好的学习。

师傅们在学习 JSP 的时候，一定有过这样的问题：

感觉 JSP 代码的可读性非常差

感觉 JSP 的代码很难写

比如我们看一个 JSP 的 demo

### JSP Demo

* Target —>

![](https://mmbiz.qpic.cn/mmbiz_png/goxicFBGKAF7JMpbm2Rj7qNj442r7qhOHE0bm2yVCUwSYhI8k5mmCLxheDUK6Yz53hcmmicUU5ic6oRfxeClRNPIEmBmicR0VZzdF3t2JM7wHRc/640?wx_fmt=png&from=appmsg)

如果作为静态页面出现的话，应该是这样的

```
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%    // 查询数据库    List<Brand> brands = new ArrayList<Brand>();    brands.add(new Brand(1,"三只松鼠","三只松鼠",100,"三只松鼠，好吃不上火",1));    brands.add(new Brand(2,"优衣库","优衣库",200,"优衣库，服适人生",0));    brands.add(new Brand(3,"小米","小米科技有限公司",1000,"为发烧而生",1));
%><!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>Title</title></head><body><input type="button" value="新增"><br><hr><table border="1" cellspacing="0" width="800">    <tr>        <th>序号</th>        <th>品牌名称</th>        <th>企业名称</th>        <th>排序</th>        <th>品牌介绍</th>        <th>状态</th>        <th>操作</th>
    </tr>    <tr align="center">        <td>1</td>        <td>三只松鼠</td>        <td>三只松鼠</td>        <td>100</td>        <td>三只松鼠，好吃不上火</td>        <td>启用</td>        <td><a href="#">修改</a> <a href="#">删除</a></td>    </tr>
    <tr align="center">        <td>2</td>        <td>优衣库</td>        <td>优衣库</td>        <td>10</td>        <td>优衣库，服适人生</td>        <td>禁用</td>
        <td><a href="#">修改</a> <a href="#">删除</a></td>    </tr>
    <tr align="center">        <td>3</td>        <td>小米</td>        <td>小米科技有限公司</td>        <td>1000</td>        <td>为发烧而生</td>        <td>启用</td>
        <td><a href="#">修改</a> <a href="#">删除</a></td>    </tr>

</table>
</body></html>
```

但是现在我们要实现动态性，也就是通过循环遍历的方式，获取到数据库里面的数据（当然这里做的没有这么复杂）

先写一个实体类

**Brand.java**

```
package com.drunkbaby.basicjsp.pojo;
/** * 品牌实体类 */
public class Brand {
    private Integer id;    private String brandName;    private String companyName;    private Integer ordered;    private String description;    private Integer status;

    public Brand() {    }
    public Brand(Integer id, String brandName, String companyName, String description) {        this.id = id;        this.brandName = brandName;        this.companyName = companyName;        this.description = description;    }
    public Brand(Integer id, String brandName, String companyName, Integer ordered, String description, Integer status) {        this.id = id;        this.brandName = brandName;        this.companyName = companyName;        this.ordered = ordered;        this.description = description;        this.status = status;    }
    public Integer getId() {        return id;    }
    public void setId(Integer id) {        this.id = id;    }
    public String getBrandName() {        return brandName;    }
    public void setBrandName(String brandName) {        this.brandName = brandName;    }
    public String getCompanyName() {        return companyName;    }
    public void setCompanyName(String companyName) {        this.companyName = companyName;    }
    public Integer getOrdered() {        return ordered;    }
    public void setOrdered(Integer ordered) {        this.ordered = ordered;    }
    public String getDescription() {        return description;    }
    public void setDescription(String description) {        this.description = description;    }
    public Integer getStatus() {        return status;    }
    public void setStatus(Integer status) {        this.status = status;    }
    @Override    public String toString() {        return "Brand{" +                "id=" + id +                ", brandName='" + brandName + '\'' +                ", companyName='" + companyName + '\'' +                ", ordered=" + ordered +                ", description='" + description + '\'' +                ", status=" + status +                '}';    }}
```

接着，来实现动态的 JSP 代码

```
<%@ page import="com.drunkbaby.basicjsp.pojo.Brand" %>  <%@ page import="java.util.List" %>  <%@ page import="java.util.ArrayList" %>  <%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%      // 查询数据库      List<Brand> brands = new ArrayList<Brand>();      brands.add(new Brand(1,"三只松鼠","三只松鼠",100,"三只松鼠，好吃不上火",1));      brands.add(new Brand(2,"优衣库","优衣库",200,"优衣库，服适人生",0));      brands.add(new Brand(3,"小米","小米科技有限公司",1000,"为发烧而生",1));
%>

<!DOCTYPE html>  <html lang="en">  <head>   <meta charset="UTF-8">   <title>Title</title>  </head>  <body>  <input type="button" value="新增"><br>  <hr>  <table border="1" cellspacing="0" width="800">   <tr>   <th>序号</th>   <th>品牌名称</th>   <th>企业名称</th>   <th>排序</th>   <th>品牌介绍</th>   <th>状态</th>   <th>操作</th>   </tr>   <%          for (int i = 0; i < brands.size(); i++) {              Brand brand = brands.get(i);      %>      <tr align="center">   <td><%=brand.getId()%></td>   <td><%=brand.getBrandName()%></td>   <td><%=brand.getCompanyName()%></td>   <td><%=brand.getOrdered()%></td>   <td><%=brand.getDescription()%></td>   <td><%=brand.getStatus() == 1 ? "启用":"禁用"%></td>   <td><a href="#">修改</a> <a href="#">删除</a></td>   </tr>   <%          }      %>  </table>  </body>  </html>
```

成功！

![](https://mmbiz.qpic.cn/mmbiz_png/goxicFBGKAF5icaKIxI9Vs6lBR3RznXmuNVaQnkUEk7BykzRn7svxb4QrSCOGRuYRDrOALnByVXGWW4YRl0dMGQKYWOkf2ic9VzjfSMrtOFwgA/640?wx_fmt=png&from=appmsg)

### JSP 缺点

通过上面的案例，我们可以看到 JSP 的很多缺点。

由于 JSP页面内，既可以定义 HTML 标签，又可以定义 Java代码，造成了以下问题：

难写难读难维护。

书写麻烦：特别是复杂的页面

既要写 HTML 标签，还要写 Java 代码

阅读麻烦

上面案例的代码，相信你后期再看这段代码时还需要花费很长的时间去梳理

复杂度高：运行需要依赖于各种环境，JRE，JSP 容器，JavaEE…

占内存和磁盘：JSP 会自动生成 `.java` 和 `.class` 文件占磁盘，运行的是 `.class` 文件占内存

调试困难：出错后，需要找到自动生成的.java文件进行调试

不利于团队协作：前端人员不会 Java，后端人员不精 HTML

如果页面布局发生变化，前端工程师对静态页面进行修改，然后再交给后端工程师，由后端工程师再将该页面改为 JSP 页面

由于上述的问题， JSP 已逐渐退出历史舞台，以后开发更多的是使用 HTML + Ajax 来替代。Ajax 是异步的 JavaScript。有个这个技术后，前端工程师负责前端页面开发，而后端工程师只负责前端代码开发。

![](https://mmbiz.qpic.cn/mmbiz_png/goxicFBGKAF5hnqpoicKPSqf6RWqyvichLuiaNBQ4gv69hKqqEYraOMkVYg6aNibJcua4A52AkZljSz3nUibCHORqJkTRt7VcWCNAew0LHic0W9RnY/640?wx_fmt=png&from=appmsg)

但是有时候又不得不使用 JSP 进行开发，这时候就要隆重介绍我们今天的主角了 —————— EL 表达式

## 0x03 EL 表达式的基础语法

### 概述

EL（全称 **Expression Language** ）表达式语言。

**作用：**

* 1.用于简化 JSP 页面内的 Java 代码。
* 2.主要作用是 **获取数据**。其实就是从**域对象**中获取数据，然后将数据展示在页面上。

**用法：**

要先通过 page 标签设置不忽略 EI 表达式

```
<%@ page contentType="text/html;charset=UTF-8" language="java" isELIgnored="false" %>
```

**语法：**

`${expression}`

在 JSP 中我们可以如下写：

`${brans}`，这到底是啥意思呢？比较玄，但是却是一个很有趣，并且很合理的机制。

`${brans}` 是获取域中存储的 key 作为 brands 的数据。

而 JSP 当中有四大域，它们分别是：

* page：当前页面有
* request：当前请求有效
* session：当前会话有效
* application：当前应用有效

el 表达式获取数据，会依次从这 4 个域中寻找，直到找到为止。而这四个域对象的作用范围如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/goxicFBGKAF6RF5d5Vf0TocstQhia1icIoxicrKvw477XDdx1cscO5GacespiciaxRsA4ibyHvl1Nz5xlbqzCI85eZtzN0kibv3GXFue4nsazF3bYws/640?wx_fmt=png&from=appmsg)

例如： `${brands}`，el 表达式获取数据，会先从 `page` 域对象中获取数据，如果没有再到 `requet` 域对象中获取数据，如果再没有再到 `session` 域对象中获取，如果还没有才会到 `application` 中获取数据。

其实是有那么一点双亲委派的味道在里面的。

### EL 表达式 Demo

要使用 EL 表达式来获取数据，需要按照顺序完成以下几个步骤。

* 获取到数据，比如从数据库中拿到数据
* 将数据存储到 request 域中
* 转发到对应的 jsp 文件中

先定义一个 Servlet

```
@WebServlet("/demo1")public class ServletDemo1 extends HttpServlet {    @Override    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {        //1. 准备数据        List<Brand> brands = new...