---
title: linux内核之Kconfig学习 - potatso
url: https://www.cnblogs.com/potatso/p/18849309
source: 博客园 - potatso
date: 2025-04-28
fetch_date: 2025-10-06T22:02:47.718564
---

# linux内核之Kconfig学习 - potatso

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

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [linux内核之Kconfig学习](https://www.cnblogs.com/potatso/p/18849309 "发布于 2025-04-27 13:51")

# Kconfig语法

Kconfig就是通过图形化界面，配置编译选项，生成makefile变量的一个工具

# 主菜单

mainment，用来修改整个kconfig界面的标题。例如

`mainmenu "Test Menu"`

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/bf99b12808ea4f48af4838eca716bb31.png#pic_center)

# 菜单结构

## menu

菜单选项，选中后会进入一个新的界面，也就是下级目录

通过menu和endmenu关键字明确界定菜单范围，具体如下：

* **语法格式**：

```
menu "菜单名称"

depends on 依赖条件
config 配置项名称

endmenu

menu "Network device support"
      depends on NET

config NETDEVICES
      ...

endmenu
```

* 在“menu”... “endmenu”代码块内的所有条目，都会成为“菜单名称”对应的子菜单。并且，子菜单下的所有子条目会继承该菜单条目的依赖关系 。如示例中NETDEVICES配置选项的依赖列表会自动添加NET依赖。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c2277b9d66e948198997722c0788f6f6.png#pic_center)

## 基于依赖

选中后，会展开目录

生成菜单结构的另一种方式是通过分析依赖关系。如果某个菜单项以某种方式依赖于前一个菜单项，那么它可以成为前一个菜单项的子菜单。具体来说，需要满足两个条件：一是前一个（父）菜单项的符号必须出现在依赖列表中；二是以下两个条件必须满足其一：

1. 如果父菜单项被设置为 `'n'`（即不选择该选项），子菜单项必须变为不可见。
2. 子菜单项仅在父菜单项可见时才可见。

下面是一个示例代码：

```
config MODULES
    bool "Enable loadable module support"

config MODVERSIONS
    bool "Set version information on all module symbols"
    depends on MODULES

comment "module support disabled"
    depends on !MODULES
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c99450814a3341de9cc111669fb209d3.png#pic_center)

**代码解释**

* `config MODULES` 定义了一个布尔类型的配置项，其提示信息为 “Enable loadable module support”（启用可加载模块支持）。用户可以选择启用或不启用该功能。
* `config MODVERSIONS` 同样是一个布尔类型的配置项，提示信息为 “Set version information on all module symbols”（为所有模块符号设置版本信息）。它依赖于 `MODULES`，这意味着只有当 `MODULES` 被启用（即不为 `'n'`）时，`MODVERSIONS` 才会显示出来供用户选择。
* `comment "module support disabled"` 是一条注释信息，它依赖于 `!MODULES`，即只有当 `MODULES` 被设置为 `'n'`（不启用可加载模块支持）时，这条注释才会显示出来。

综上所述，通过分析依赖关系，可以动态地控制菜单项的可见性，从而构建出层次分明的菜单结构。但是可能没有menu这种层级比较分明。linux内核中大量都是这一类。

![外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传](https://img-home.csdnimg.cn/images/20230724024159.png?origin_url=Kconfig%25E8%25AF%25AD%25E6%25B3%2595%25201e266ffcecaf805d96a0c0ac008fa9be%2Fimage%25202.png&pos_id=img-PgxgnbUP-1745732906116)

# Config选项

**配置选项的构成**：在内核配置中，多数条目用于定义配置选项，还有一些条目用于组织这些配置选项。单个配置选项的定义形式如下：

```
config 配置选项名称
    类型 "输入提示信息"
    depends on 依赖条件
    help
        帮助文本内容
```

**配置选项的属性**：配置选项的每一行都以一个关键字开头，后面可跟多个参数。关键字 `config` 用于开启一个新的配置项。后续行用于定义该配置选项的属性，包括：

* **类型**：如 `bool` 表示布尔类型。如果没有类型，参考上面，就是一个类似于目录的结构
* **输入提示**：即双引号内的文本，用于向用户展示该配置选项的说明。
* **依赖关系**：通过 `depends on` 关键字指定该配置选项所依赖的其他条件。有可能通过这个，kconfig工具会组织为一个菜单
* **帮助文本**：使用 `help` 关键字引出，为用户提供关于该配置选项的详细信息和解释。

**配置选项的特殊情况**：一个配置选项可以使用相同的名称被多次定义，但每个定义只能有一个输入提示，并且类型不能冲突。

## 选项的属性

### **类型定义（Type Definition）**

`“bool”/”tristate”/”string”/”hex”/”int”`

* **基本类型**：配置选项必须有类型，基本类型有 `tristate` 和 `string`，其他类型（`bool`、`hex`、`int`）基于这两种。
* **定义形式**：可附带输入提示，如 `bool "Networking support"` 与 `bool; prompt "Networking support"` 等效。
* bool 表示该CONFIG宏只能选择y(编译内核)或者n(不编译),不能选择m(编译为模块) 结果生成 y或空

```
CONFIG_MODULES=y
# CONFIG_MODVERSIONS is not set

# 选中菜单
CONFIG_MODULES=y
CONFIG_MODVERSIONS=y
```

* `tristate` 的结果是y，m， 空
* string 表示该CONFIG宏可以设为一串字符,比如`#define CONFIG_XXX "config test"`
* hex 表示该CONFIG宏可以设为一个十六进制,比如 `#define CONFIG_XXX 0x1234`
* int 表示该CONFIG宏可以设为一个整数,比如`#define CONFIG_XXX 1234`

### **2. 输入提示（Input Prompt）**

`“prompt” <prompt> [“if” <expr>]`

* **数量限制**：每个菜单项最多有一个提示，用于向用户显示。
* **依赖设置**：可通过 `if` 为提示添加依赖。
* **不可见符号**：无提示的配置选项是不可见符号，其值不能由用户直接更改，只能通过 `default` 和 `select` 设置。
* 如果与类型提示的输入提示冲突，则以prompt为主

### **3. 默认值（Default Value）**

`“default” <expr> [“if” <expr>]`

`default` 后面的 `<expr>`，是指：

> 默认赋值表达式（default value expression）

也就是：

* 对于 `bool` / `tristate` 类型，就是默认的布尔值 `y` / `n` / `m`。
* 对于 `int` / `hex` 类型，就是默认的数字。
* 对于 `string` 类型，就是默认的字符串。
* 对于 `choice`，就是默认选中的选项。

总之，**第一个 `<expr>` 就是「我默认想给这个config赋什么值」。**

* **数量与规则**：配置选项可以有多个默认值，若多个可见，仅第一个定义的有效。默认值可在别处定义或被覆盖。
* **默认情况**：默认值故意设为 `n` 以避免构建臃肿，新配置选项一般不应更改。
* **特殊情况设为 `y/m` 的情况**：
  + 以前总是构建的新 Kconfig 选项应为 `default y`。
  + 隐藏 / 显示其他 Kconfig 选项的新守门选项应为 `default y`。
  + 驱动的子驱动行为或类似选项（驱动默认 `n`）可设合理默认值。
  + 大家期望的硬件或基础设施，如 `CONFIG_NET` 或 `CONFIG_BLOCK`。
* **简写形式**：`def_bool`/`def_tristate` 是类型定义加值的简写，可通过 `if` 为默认值添加依赖。

### **4. 依赖关系（Dependencies）**

* **定义方式**：使用 `depends on` 定义，多个依赖用 `&&` 连接。
* **应用范围**：应用于菜单项内所有其他选项，`bool "foo" if BAR; default y if BAR` 与 `depends on BAR; bool "foo"; default y` 等效。

### **5. 反向依赖（Reverse Dependencies）**

`“select” <symbol> [“if” <expr>]`

* **作用**：`select` 用于在选中当前符号后，选中select的符号
* **使用限制**：只能用于布尔或三态符号，应谨慎使用，一般用于不可见符号和无依赖的符号。
* **条件选择**：若 `select <symbol>` 后接 `if <expr>`，被选符号由当前菜单项值和 `<expr>` 的逻辑与决定。

### **6. 弱反向依赖（Weak Reverse Dependencies）**

* **特点**：`imply` 与 `select` 类似，但被 “暗示” 的符号值仍可因直接依赖或可见提示设为 `n`。
* **示例应用**：多个驱动表明能接入子系统，同时允许用户禁用子系统而不取消驱动配置。
* **条件暗示**：若 `imply <symbol>` 后接 `if <expr>`，被暗示符号的默认值由当前菜单项值和 `<expr>` 的逻辑与决定。

### **7. 菜单显示限制（Limiting Menu Display）**

* **作用**：`visible if` 仅适用于菜单块，条件为假时菜单块不显示，但其中符号仍可被其他符号选择，默认 `visible` 为 `true`。

### **8. 数值范围（Numerical Ranges）**

* **功能**：`range` 用于限制 `int` 和 `hex` 符号的输入值范围，用户输入值需在两个符号指定的范围内。

### **9. 帮助文本（Help Text）**

* **定义方式**：使用 `help` 定义，帮助文本结束由缩进级别决定。

### **10. 模块属性（Module Attribute）**

* **作用**：`modules` 声明符号为 `MODULES` 符号，为所有配置符号启用第三模块化状态，最多一个符号可设置该选项。

# comment注释

```
comment "module support disabled"
    depends on !MODULES
```

comment同样也支持依赖

# 引入其他KConfig

`"source" <prompt>`

# 多选

也就是多选一

```
choice
    prompt "Select Operating System Type"
    default LINUX

config LINUX
    bool "Linux"
    help
      Choose this option if you are using a Linux-based OS.

config WINDOWS
    bool "Windows"
    help
      Choose this option if you are using a Windows-based OS.

config MACOS
    bool "MacOS"
    help
      Choose this option if you are using a macOS-based system.

endchoice
```

posted @
2025-04-27 13:51
[potatso](https://www.cnblogs.com/potatso)
阅读(101)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)