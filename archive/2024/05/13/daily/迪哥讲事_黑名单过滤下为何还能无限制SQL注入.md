---
title: 黑名单过滤下为何还能无限制SQL注入
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247494600&idx=1&sn=35845981e16f993775516df7f30687d9&chksm=e8a5e1abdfd268bd90e0e675d4e6949544d2285fb75e6800fda86d2d306899481a7366026404&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-05-13
fetch_date: 2025-10-06T17:15:10.479628
---

# 黑名单过滤下为何还能无限制SQL注入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6sUdMSib0r68cBP7yqrzibrfoYsSQ54BiaksoZkQUNvCPUgF0e8IIib4deyWY3eiced1wSt50QCpPWruQ/0?wx_fmt=jpeg)

# 黑名单过滤下为何还能无限制SQL注入

Yu9雨久

迪哥讲事

文章首发于奇安信攻防社区

链接：https://forum.butian.net/share/2905

## 0x01 前言

这周看到了某公众号发的springboot+vue实现的一个后台管理系统。阅读量还挺高的，就下了一下源码翻一翻，发现里边漏洞还挺多的。尤其是SQL方面，作者虽然做了过滤但还是因为配置不当的导致SQL注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1nGbWibkdsKEFznNBoMwKUY4R5PCjbQicf07DZXqX6J4iaj8nYNSE3dfUQ/640?wx_fmt=png&from=appmsg "image-20240405151739486")

image-20240405151739486

后边经过作者的同意，然后把本次代码审计的思路放出来和大家分享一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1vc0dx7MRdmMM86uqLu6Dt9ACQOxQnbNiaghR0n78mYutoVcU8GlNnLw/640?wx_fmt=png&from=appmsg "image-20240405155534442")

image-20240405155534442

## 0x02 SQL注入

mybatis-plus对绝大部分场景进行了预编译处理。但是类似动态表名、orderby这种需要拼接的场景配置不当还是会存在漏洞。本次就是记录一下在代码审计中遇到的一个奇怪的SQL注入，在对请求参数进行黑名单过滤十分严格的情况，代码逻辑不当导致SQL注入！

### 分页SQL注入分析

翻了一下pom.xml文件，发现该项目持久层使用的是Mybatis-puls框架！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1icNfcibV8n8gXlTD8m11g1aq2V2eQ8rFn2TEIiaTy1q9769HXicTTbUS5w/640?wx_fmt=png&from=appmsg "image-20240403021320315")

image-20240403021320315

我对mybatis-plus的理解就是封装了一些sql以减少代码量，其对绝大部分场景进行了预编译处理。但是类似动态表名、orderby这种需要拼接的场景配置不当还是会存在漏洞。

在翻工具类时发现该项目有对sql注入进行过滤

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c11POicibQmR9EUpaUlckr5T799NKicZLeEsvP6pUDF7bicBvEImt9D2DVrg/640?wx_fmt=png&from=appmsg "image-20240403025212716")

image-20240403025212716

那就跟进去看看在哪里做了过滤，只在`com.utils.Query#Query`中有4处调用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1l4z8icqxoias7vmSeOclL58jG9rmEPTtc4rVddbRJISoEoa9CVEbTFug/640?wx_fmt=png&from=appmsg "image-20240411115923581")

image-20240411115923581

跟进`com.utils.Query#Query`看看，发现**该类具有两个重载的构造方法**，接收的参数类型不同

* **JQPageInfo**：封装了分页参数的实体类
* **Mapparams**：集合类型的params参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1GMoMxFMuyTRHLo26iaRYecPlsEJQo2jiazZBoc3flxGb2xAQmqZUyVxQ/640?wx_fmt=png&from=appmsg "image-20240411120600013")

image-20240411120600013

但其对sql注入的防御逻辑都相同，都是对sidx和order参数进行处理后，然后封装成Page对象

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c14DmrSibd9HdpIAXpN6wgZyFenub5Mp3TvrWBR9hB0qwqGr7dJHIFBgA/640?wx_fmt=png&from=appmsg "image-20240411121107373")

image-20240411121107373

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c17WdlUCIPGQibMDflPk0xENfKZUYic1TY2aNL7UWd5NcxDyzwtKLC23cA/640?wx_fmt=png&from=appmsg "image-20240411121146368")

image-20240411121146368

源码：

```
package com.utils;

import java.util.LinkedHashMap;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;

import com.baomidou.mybatisplus.plugins.Page;

/**
 * 查询参数
 */
public class Query<T> extends LinkedHashMap<String, Object> {
    private static final long serialVersionUID = 1L;
    /**
     * mybatis-plus分页参数
     */
    private Page<T> page;
    /**
     * 当前页码
     */
    private int currPage = 1;
    /**
     * 每页条数
     */
    private int limit = 10;

    public Query(JQPageInfo pageInfo) {
        //分页参数
        if(pageInfo.getPage()!= null){
            currPage = pageInfo.getPage();
        }
        if(pageInfo.getLimit()!= null){
            limit = pageInfo.getLimit();
        }

        //防止SQL注入（因为sidx、order是通过拼接SQL实现排序的，会有SQL注入风险）
        String sidx = SQLFilter.sqlInject(pageInfo.getSidx());
        String order = SQLFilter.sqlInject(pageInfo.getOrder());

        //mybatis-plus分页
        this.page = new Page<>(currPage, limit);

        //排序
        if(StringUtils.isNotBlank(sidx) && StringUtils.isNotBlank(order)){
            this.page.setOrderByField(sidx);
            this.page.setAsc("ASC".equalsIgnoreCase(order));
        }
    }

    public Query(Map<String, Object> params){
        this.putAll(params);

        //分页参数
        if(params.get("page") != null){
            currPage = Integer.parseInt((String)params.get("page"));
        }
        if(params.get("limit") != null){
            limit = Integer.parseInt((String)params.get("limit"));
        }

        this.put("offset", (currPage - 1) * limit);
        this.put("page", currPage);
        this.put("limit", limit);

        //防止SQL注入（因为sidx、order是通过拼接SQL实现排序的，会有SQL注入风险）
        String sidx = SQLFilter.sqlInject((String)params.get("sidx"));
        String order = SQLFilter.sqlInject((String)params.get("order"));
        this.put("sidx", sidx);
        this.put("order", order);

        //mybatis-plus分页
        this.page = new Page<>(currPage, limit);

        //排序
        if(StringUtils.isNotBlank(sidx) && StringUtils.isNotBlank(order)){
            this.page.setOrderByField(sidx);
            this.page.setAsc("ASC".equalsIgnoreCase(order));
        }

    }

    public Page<T> getPage() {
        return page;
    }

    public int getCurrPage() {
        return currPage;
    }

    public int getLimit() {
        return limit;
    }
}
```

很完美的防御、不过这里就有点奇怪了，翻了几个sql的xml文件，发现都没有使用到这个`page`对象

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1sTHHicb6r3wRBCrX1IdXQcAypQOLib333lwOab3TNHpa8p9sfEN6tyOw/640?wx_fmt=png&from=appmsg "image-20240411121930477")

image-20240411121930477

那我们从页面中随便找一个带分页的查询请求分析一下，例如：

```
/jixiaokaohe/page?page=1&limit=10&sort=id
```

跟进到他的controller->`com.controller.JixiaokaoheController#page`

调用的是`jixiaokaoheService.queryPage`来进行的查询，使用`MPUtil.sort`来自定义了一个`wrapper`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1lyic3EHKAkGXFx4E0bUjJkYWSzSlruwBJmVvicQWwp9Kn9hqFhYKiaIew/640?wx_fmt=png&from=appmsg "image-20240403032355989")

image-20240403032355989

继续跟进到`com.service.impl.JixiaokaoheServiceImpl#queryPage`

可以看到这块使用了sql过滤的`com.utils.Query#Query(java.util.Map<java.lang.String,java.lang.Object>)`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1lHUD2HkLcBfcvyvgibl5miaJ7hYtmppkLuUfTerriakvewKSp9JqhKmGQ/640?wx_fmt=png&from=appmsg "image-20240403032630418")

image-20240403032630418

继续向下跟

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c18CicDoiaESr0o0ZRP0F7MPbLJbvaNXKdIBJRxdGfasxKH5c5J8vaWQVg/640?wx_fmt=png&from=appmsg "image-20240403033241569")

image-20240403033241569

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1dmWib3I3dS31OacPyrU5KxSviasLIiajmnv4icq75MAdUeiaYCGbicuMse6A/640?wx_fmt=png&from=appmsg "image-20240403033302136")

可以看到最终sql的实现使用的是开头说的自定义的`wrapper`来构建查询条件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1lvKVfD7Bib29600X5pvWKbLIKHgZ1WzbPHFJ6oTKG4v74mHE4h0WKHQ/640?wx_fmt=png&from=appmsg "image-20240403033810081")

image-20240403033810081

跟进去看看->`com.utils.MPUtil#sort`

发现在这块对`sort`参数直接使用了拼接而且没有进行过滤

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1qcW7WxWTq5ILyD1R3UT5z1O47n8U2KGwRhT8jeYkxfIPCkVOf58r5A/640?wx_fmt=png&from=appmsg "image-20240403033917326")

image-20240403033917326

打个poc试一下吧！

```
page=1&limit=10&sort=id+and+updatexml(1,concat(0x7e,database()),0)#
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c1JlXcicK0TptcTnqfhuNgDl6OAtDicbDTYwciaHPeQFt2eOEVJtDZejRew/640?wx_fmt=png&from=appmsg "image-20240403034431648")

image-20240403034431648

### 其他SQL注入分析

从Mybatis-puls的简介中可以看到：**Mybatis-Plus是一个Mybatis（opens new window）的增强工具，在Mybatis的基础上只做增强不做改变，为简化开发。**因此mybatis中实现sql的方式在Mybatis-puls同样适用。

`#{}`预处理、`${}`拼接就不用多说了。直接实现sql的xml搜索`${`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c11kAmuAaMmsPiacr50PoqoMN5OK8ZN32e1dwaQamQMWhKF1lAWvtvJ8w/640?wx_fmt=png&from=appmsg "image-20240403040500351")

image-20240403040500351

可以发现多出使用拼接，那直接选择一个分析一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJndZ07QlzyXg7vR3QvsOia1J1x85c18cRNfTiaJbXlUnZMeHicjnZXovd6Zia72FuJWsCGlNsyRr1CjsicfzYFKQ/640?wx_fmt=png&from=appmsg "image-20240404211942229")

image-20240404211942229

一路向上跟进

`com.service.impl.CommonServiceImpl#remindCount`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HEQJ...