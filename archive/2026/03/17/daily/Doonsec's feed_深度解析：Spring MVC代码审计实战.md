---
title: 深度解析：Spring MVC代码审计实战
url: https://mp.weixin.qq.com/s/eguNMDeMClkV9t7MMoi-Fw
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:16:56.974753
---

# 深度解析：Spring MVC代码审计实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RDiaL6j1Wgd5iayyxTDjia9246C3rDQQrF6icRdnbuibcrdMjWC3nZgiay15Ricof6b5xPAC50xQfnSr9icArzThspiaXUEqoCXLYgGMkzPS8t3egzibA/0?wx_fmt=jpeg)

# 深度解析：Spring MVC代码审计实战

原创

尘佑不尘
尘佑不尘

泷羽Sec-尘宇安全

![]()

在小说阅读器中沉浸阅读

# 前言

现在绝大多数的新项目都是基于Spring Boot的Spring MVC实现，这里也主要以Spring MVC框架展开讲解。在Spring3.0版本,引入了Java注解，我们只需要使用Spring MVC注解就可以轻松完成Spring MVC的配置了。下面介绍一下Spring 注解配置

### Spring Controller 类级别注解

#### 1. `@Controller`

* **作用**：标识一个类为 **Spring MVC 的控制器（Controller）**。

**示例**：

```
@Controller
public class GoodsController {

    @Resource
    private NewBeeMallGoodsService newBeeMallGoodsService;
    @Resource
    private NewBeeMallCategoryService newBeeMallCategoryService;

    @GetMapping({"/search", "/search.html"})
    public String searchPage(@RequestParam Map<String, Object> params, HttpServletRequest request) {
        if (StringUtils.isEmpty(params.get("page"))) {
            params.put("page", 1);
        }
```

#### 2. `@RestController`

* **作用**：是 `@Controller + @ResponseBody` 的组合注解。
* **示例**：

```
@RestController
public class ApiUserController {
    @GetMapping("/api/user/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.findById(id);
    }
}
```

#### 3. `@RepositoryRestController`

* **作用**：用于**扩展 Spring Data REST 自动生成的 REST 接口**。
* **示例**：

```
@RepositoryRestController
public class CustomProductController {
    @GetMapping("/products/search/byName")
    public ResponseEntity<?> searchByName(@RequestParam String name) {
    }
}
```

**简单总结**：

* 做页面跳转 → 用 `@Controller`
* 做 API 接口 → 用 `@RestController`
* 扩展 Spring Data REST → 用 `@RepositoryRestController`

**Spring MVC请求配置注解:**

|  |  |  |
| --- | --- | --- |
| 注解 | 对应 HTTP 方法 | 说明 |
| `@RequestMapping` | 任意（可指定） | 通用映射注解，可通过 `method = RequestMethod.GET`  指定方法 |
| `@GetMapping` | `GET` | `@RequestMapping(method = GET)`   的快捷方式 |
| `@PostMapping` | `POST` | 用于提交数据（如表单、JSON） |
| `@PutMapping` | `PUT` | 用于**全量更新**资源 |
| `@DeleteMapping` | `DELETE` | 用于删除资源 |
| `@PatchMapping` | `PATCH` | 用于**部分更新**资源 |

所以我们的思路就是先查看项目的开发框架、根据框架特性查找所有的API接口，然后查看从接口接收的参数，并跟踪参数,判断参数数据进入的每一个代码逻辑是否有可利用的点,此处的代码逻辑可以是一个函数，或者是个条件判断语句
对于Spring框架，我们可以直接看他的controller，这里的文件包含了所有的路由信息，从这里开始跟接收参数，就不会漏掉

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5rJcAmtjETCTSoytGWGBNLQkj9F8vspJVIKQib3bPbG68C05EPkEOxdLrtoSbS6mB1DAIibyYO3VjB16xcTGGbKchmxsAzjXxWk/640?wx_fmt=png&from=appmsg)

当然区分前台路由和后台路由也很重要，一般admin目录下的都是后台路由，这时候就需要去看它的鉴权逻辑了

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd6jt0vtmsV06HdTyEepWJ1GsnxslmptshFEBsO5o6ibVpYat1tnjHSxIhk0icLPtjPDRQ9iaJzmbiaTBHgLOXAJcAsnppE7aVRb9x8/640?wx_fmt=png&from=appmsg)

这里有一个admin登录的拦截器，里面写了admin路由的鉴权逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7OaYkMhPaFjd4joSfHMicN8gEF4OErp8KEqvQoWJ7pf7eSpRqq0Olt4jJVGvocf2OSmMjjQyHaNRiaYeXYhDS98HOGA6ECkpYico/640?wx_fmt=png&from=appmsg)

# 权限绕过

这里使用了 request.getRequestURI() 方法获取路径，使用该方法获取的路径进行权限判断是极易出现权限绕过漏洞，这里有一个if判断，首先判断 url 路径中是否以/admin开头，并且判断Session 中的 loginUser 属性是否为 null，都为真就登录，总的来说就是以admin开头的路由都要进行鉴权，但是这里使用的 getRequestURI 方法获取的原始路径，那么我们可以找一些特殊字符绕过路径判断，并且不影响整体接口，比如：分号;，正斜杠/，就不会再进行鉴权操作了

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd69JwrljpPlhZOEn2sdgxv6AFHdp8OibQjNibd1iaT9ZiaxQd2wg35qLAXvJsWib2QyPYesibRmKdOzG600Fj2nnWYTwibVp3N4F3BnQI/640?wx_fmt=png&from=appmsg)

就像这样：

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4Tib4ouAAPUSv0YBGgyXp1CaJ4zGr5YV9wribW5fLV217ejEk3bZT8PUlW8ZGb5PAYPLj6zO7rpJlnKw9n2BBibRafOQl0tfDm9w/640?wx_fmt=png&from=appmsg)

比如说这里的后台首页为/admin/index，我没有登录肯定是进不去的

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4lWhe1lV2slJ8NibEk3YZLtyOULerqMMhlUFY1TeocPe8fG4bBaIG3xaIWBcfZqZRBVqCkX0tVE1gPJbFwnkwg5vS7Yic5xetkA/640?wx_fmt=png&from=appmsg)

然后我使用分号进行绕过，就可以跳转到后台

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5FGrsw9QnibToicpnVELFClWYiaibSkCIKorlnDfhx0dJOz7zq84zPc9Qjd6PR6UxZEnfYdgwEFRiaV5tEx3V43Ij9XulmdynBLqicE/640?wx_fmt=png&from=appmsg)

# 任意文件上传

直接从controller开始看路由，由于upload太明显了，先看这个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd6ZVqy7iav3MlGulias81zE0TYibyP85lrfy1y3e4VPF9vAyvwiaSBQcsIia9ibzAzibZjLOm6PUaavpBySJ5npVI13Kj7HQl3kFNNuaU/640?wx_fmt=png&from=appmsg)

这里首先获取原始文件名；提取后缀名；生成新文件名，格式：`yyyyMMdd_HHmmss + 随机数 + 后缀`；将文件保存到 `Constants.FILE_UPLOAD_DIC` 目录；最后返回文件访问路径，这里未对上传文件类型做校验，但是由于是后台路由，但是可以通过分号绕过

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd78iapbKSNiafDqj1QwJicA834fxcRG3TGskSHo9DKHqAKEhkQtib8IJ47l0hz8rO4DQomRvnFjF9ZsiahbWrRe2TIhuAe6JI23rVYI/640?wx_fmt=png&from=appmsg)

# 支付漏洞

这是一个前台路由， 该 `paySuccess` 接口未验证支付真实性，仅凭用户传入的订单号就标记支付成功

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4RribIkyvF5icUaUBABB6rjhwTvrzDHT3EiaFiacHZGEiaOXY7ke1pJa9RVPJqytjZtKfRyREXRic6ajrM4WJVZibpDJP9KGhUNvK2EU/640?wx_fmt=png&from=appmsg)

看一下它的核心方法payducces，这里首先根据orderNo查询订单状态，如果查询到是已支付状态就不管，如果是待支付状态就返回支付成功

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd6CXxKqgGTp0CUTy8ibmaIVM0GFZQVbkRpIIUx94zD8ibYWHIe5iaTWZ2ZWraHT34ibKbfERTECXWB1DdT8jfE4ibMesrNHDkF2Mu3c/640?wx_fmt=png&from=appmsg)

这里有个15698039249771093的订单号未支付

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5q8s8SvwzviaibOPxrrPEUHGicLqUIIq7WCp0bPYazmG9DgkDAwbiaA8EbCgIrE0WTuKKPYsnrDsyl8SFdjYZdNGSLHJuia4dHzdibk/640?wx_fmt=png&from=appmsg)

在`paySuccess` 接口传入该订单号

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd57wzsrB4icLx6vxUV4vHoKRm5lWicTPy2VPE9WB5zdeR2F8mjZB542Wtiajy4MlDqWCSPEvmfibm8D22qeFQMxGNgLicj7ZVbibTS1o/640?wx_fmt=png&from=appmsg)

显示支付成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd68iblPgXvw0qCbZN1ybC9l3ZHW9icByR8ibdP8YkkfHGtRqk15AgDpibzSjILwlOE8L70ZyeibjcyWMiaNZCnOeecsiaBnSycwZ81h3U/640?wx_fmt=png&from=appmsg)

# 越权1

这里有个更新个人信息的前台接口

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5cwpXqTkian9ZBxgml385AXrIWnkHxnZeFkZqmiauZJC1ibzpsfZLg84OljRLsatKS269BNaBrXKsVEfSB5QK9QIiaE6NPvfQ6Fb0/640?wx_fmt=png&from=appmsg)

看一下怎么更新的，跟进updateUserinfo方法,这里先是通过 ID 查询用户信息并赋值给 user,如果 user 不为 null，进行了三个 set 操作，其中如果传入的参数是来自 mallUser。就将查询到的用户信息中的内容设置成了用户输入的内容了，通过调用 mallUserMapper.updateByPrimaryKeySelective(user) 方法，将更新后 的用户信息保存到数据库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd712gJch6JKeWGAJ90lgUDcz5mk23g7sdUYzypAYoPiag2d7sneZsZDU0o9AcMZ0BLemu4nU5wGhzficp9IgxG7nQt6YKBHVlCiaU/640?wx_fmt=png&from=appmsg)

这里没有对id进行鉴权，导致任何人都可以更改

# 越权2

接口未校验 `newBeeMallShoppingCartItemId` 是否属于当前登录用户，只要知道订单号id即可删除任意订单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4khBI0bf0E3UsS5QZl75ba93RJMcszJkhhHqoHgkjP3DtmVEDnEJI5jTWrL0KaOVkBhjleI5mTiaUVGzVllTTVSyibILRcYHOBQ/640?wx_fmt=png&from=appmsg)

注意请求方式为DELETE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd6TmDqXzqZMjHMiav5gvOhHvb6RHHg6esObkg9jhrlvvFKWNSTK92iakI9aVSauHzmvFGuqmGazLCCGdnmDVgUxxVgAHVy5OkIIg/640?wx_fmt=png&from=appmsg)

# sql注入1

还有一种就是直接看pom依赖， 查看应用是否使用了带有已知漏洞的第三方组件或中间件

本项目使用 **MyBatis** 作为持久层框架，用于操作数据库。在 MyBatis 中，拼接 SQL 语句时常用两种占位符：`#{}` 和 `${}`。

* `**#{}**`：安全方式。MyBatis 会将其转换为 **预编译语句**的参数，能有效防止 SQL 注入。
* `**${}**`：危险方式。MyBatis 会在 SQL 解析阶段直接把变量值原样插入 SQL 中，**会造成 SQL 注入漏洞**。

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5TUsqJpB7E9IjODeWibZxOialR860MdqkgYJgyYsmpd4ngib07lgTyJ7p4RiaQpEjq4BBAwaF72hgwydJ2DTjqktZ9psN0gmWuBGg/640?wx_fmt=png&from=appmsg)

MyBatis 的 SQL 映射文件（Mapper 文件）通常是 `.xml` 格式，所以可以指定文件类型更加精准搜索，直接搜索${，发现4个xml文件，先来看第一个NewBeeMallGoodsMapper.xml

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4ziaGK0aib2aLyib7icFwNteOm5ibnR7eamkFeMu2S0seTiaa0PtyZZISDEduo8aVYXsYotCmBhwhkhRraI1NHfSUwibY0ybA6nOhm6A/640?wx_fmt=png&from=appmsg)

找到漏洞位置，这里可以发现`${goodsName}`**直接将参数值插入 SQL 字符串中**，不做任何转义或预编译处理。如果 `goodsName` 来自用户输入，那么就会造成sql注入漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4ickg2OPKPmfjiaLH07FbRdiblSeqIWjk2olC670gaTuqIxuMib8QovJWSKPbveznBHEEXicTd3DnRBg0SUuzXac6JRHmkJ4Lky2QE/640?wx_fmt=png&from=appmsg)

接下来需要找到映射的接口，ctrl+左键点击id跳转

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd6Rcryk1odt9lUFtBpZ8AHLUXAcR1lXMHMTiaiaA6jeKy3yxribYt9AEZx3ONxibiaqNtG8EFKpwSBKmyg8xjSdmC8pnh4EEPBvwmwI/640?wx_fmt=png&from=appmsg)

一样的ctrl+左键看哪里调用了这个接口中的方法

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd51Eic9RxELkSkt8e3qPU6BKeoOUa8muib1KYZfWmLxFb6ib85Es1a6SfSlETE6lfKdrqItCZibX0jHElLbkoSki...