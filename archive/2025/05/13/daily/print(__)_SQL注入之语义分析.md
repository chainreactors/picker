---
title: SQL注入之语义分析
url: https://www.o2oxy.cn/4414.html
source: print("")
date: 2025-05-13
fetch_date: 2025-10-06T22:29:01.167337
---

# SQL注入之语义分析

![print("")](https://www.o2oxy.cn/wp-content/themes/JieStyle-Two/images/avatar.jpg)

### print("")

* [Home](http://www.o2oxy.cn)
* [信息安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8)
* [WEB前端](https://www.o2oxy.cn/category/web%E5%89%8D%E7%AB%AF)
* [linux](https://www.o2oxy.cn/category/linux)
* [python](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93)
* [监控](https://www.o2oxy.cn/category/%E7%9B%91%E6%8E%A7)
* [生活](https://www.o2oxy.cn/category/%E7%94%9F%E6%B4%BB)
* [Java学习](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/java)
* [宝塔面板最新活动](https://www.bt.cn/huodong)
* [Author](https://www.o2oxy.cn/tags)

# SQL注入之语义分析

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2025-05-12 21:12
阅读次数: 6,404 次

# **一、语义分析介绍**

### **1.1 介绍**

此次分析的语义分析模块使用的是 <https://github.com/wallarm/libdetection>

libdetection 原理是通过用户输入的字符串 使用词法提取的方式生成词法的Token 并标记好

当前Token的危险等级、和操作符，发送给语法分析， 再由语法分析进行提起符合预设的规则判断为攻击行为。

### **1.2 与正则、指纹库方案对比**

|  |  |  |
| --- | --- | --- |
| 名称 | 优点 | 缺点 |
| 语义分析 | 1.准确率高：深入理解 SQL 语句的语义，能准确识别复杂的注入模式，不易被绕过。例如对于利用编码、变形等手段隐藏的注入语句也有较好的检测效果。  2. 适应性强：可以适应不同类型的数据库和 SQL 语法，不局限于特定的规则。  3. 可检测复杂逻辑：能够检测包含复杂逻辑和嵌套结构的注入攻击，如多重条件组合、子查询注入等。 | 1.性能开销大：需要对 SQL 语句进行深度解析和语义理解，计算资源消耗大，处理速度相对较慢，在高并发场景下可能成为性能瓶颈。   1. 实现复杂：需要专业的知识和大量的开发工作来构建语义分析引擎，维护成本较高。 2. 依赖数据质量：分析结果依赖于训练数据和规则的质量，如果数据不全面或规则不准确，可能导致误判或漏判。 |
| 正则表达式 | 1.实现简单：语法相对简单，易于编写和理解，开发成本低。可以快速实现基本的 SQL 注入检测规则。   1. 执行速度快：对于简单的模式匹配，正则表达式的执行效率较高，能够快速处理大量的输入。 2. 灵活性高：可以根据不同的需求灵活编写和调整匹配规则。 | 1.规则维护困难：随着攻击手段的不断变化，需要不断更新和完善正则表达式规则，否则容易出现漏判。   1. 误判率较高：对于一些正常的 SQL 语句，如果其中包含与注入模式相似的字符序列，可能会导致误判。 2. 难以处理复杂情况：对于复杂的 SQL 注入模式，如经过编码、变形或嵌套的注入语句，正则表达式可能无法准确识别。 |
| Libinjection指纹库 | 1.轻量级：代码简洁，资源占用少，对系统性能影响小，适合在资源受限的环境中使用。   1. 检测速度快：采用了高效的算法，能够快速对输入进行检测，响应时间短。 2. 开源且易用：是开源库，有丰富的文档和示例，方便开发者集成到自己的项目中。 | 1.规则有限：预定义的规则可能无法覆盖所有的 SQL 注入场景，对于一些新型的攻击手段可能检测能力不足。   1. 定制性较差：虽然可以进行一定程度的定制，但相比于语义分析和正则表达式，定制的灵活性相对较低。 2. 缺乏上下文理解：主要基于模式匹配，对 SQL 语句的语义理解不够深入，可能会出现误判或漏判的情况。 |

# 二、架构

### 2**.1 框架图**

**[![](https://www.o2oxy.cn/wp-content/uploads/2025/05/捕获.png)](https://www.o2oxy.cn/wp-content/uploads/2025/05/%E6%8D%95%E8%8E%B7.png)**

### **2.2 执行流程图**

**[![](https://www.o2oxy.cn/wp-content/uploads/2025/05/222.png)](https://www.o2oxy.cn/wp-content/uploads/2025/05/222.png)**

# 三、源码分析

### **3.1 处理的总流程图**

[![](https://www.o2oxy.cn/wp-content/uploads/2025/05/whiteboard_exported_image.png)](https://www.o2oxy.cn/wp-content/uploads/2025/05/whiteboard_exported_image.png)

### **3.2 detect\_init 初始化**

初始化现有的所有的一个解析器模块

```
int
detect_parser_init(void)
{
    int rc = 0;
     // 初始化红黑树存储结构
    RB_INIT(&detect_parsers);
    // 顺序加载内置解析器模块
    TRYLOAD(rc, detect_parser_sqli);
    TRYLOAD(rc, detect_parser_pt);
    TRYLOAD(rc, detect_parser_bash);
done:
    // 任一模块加载失败时执行全局清理
    if (rc) {
        detect_parser_deinit();
    }
    return (rc);
}
```

例如：detect\_parser\_sqli

每个模块都是detect\_parser 结构体

```
struct detect_parser detect_parser_sqli = {
    .name = {CSTR_LEN("sqli")},
    .open = detect_sqli_open,
    .close = detect_sqli_close,
    .start = detect_sqli_start,
    .stop = detect_sqli_stop,
    .add_data = detect_sqli_add_data,
};

// 模块的结构体
// 每个对象都是一个函数指针。这样就可以方便的使用入口函数调用模块内的函数
struct detect_parser {
    struct detect_str name;

    detect_parser_init_func init;
    detect_parser_deinit_func deinit;

    detect_parser_open_func open;
    detect_parser_close_func close;
    detect_parser_set_options_func set_options;

    detect_parser_start_func start;
    detect_parser_stop_func stop;
    detect_parser_add_data_func add_data;
};
```

### **3.3 detect\_open 初始化模块上下文**

这里调用的是SQL 那么调用就是sql的detect\_parser\_open\_func 函数指针 最终调用到detect\_sqli\_open

```
static struct detect *
// 创建并初始化SQL注入检测器实例
detect_sqli_open(struct detect_parser *parser)
{
    // 初始化一个detect 结构体
    struct detect *detect;
    unsigned i;
    //
    detect = malloc(sizeof(*detect));
    //初始化检测器基础结构，设置解析器指针
    detect_instance_init(detect, parser);
    // 设置上下文数量（对应枚举SQLI_CTX_LAST的值）
    detect->nctx = SQLI_CTX_LAST;

    // 为所有上下文分配内存
    detect->ctxs = malloc(detect->nctx * sizeof(*detect->ctxs));  // 申请了6块 detect_ctx  指针内存的地址
    for (i = 0; i < detect->nctx; i++) {
        // 每个上下文地址都是detect_ctx 这个结构体指针
        // detect_ctx 结构体包含了  detect_ctx_desc    detect_ctx_result 这两个结构体
        struct sqli_detect_ctx *ctx;
        ctx = calloc(1, sizeof(*ctx));
        ctx->base.desc = (struct detect_ctx_desc *)&sqli_ctxs[i].desc;   // 这里例如第一个就是data
        ctx->base.res = &ctx->res;
        detect_ctx_result_init(ctx->base.res);  // 初始化检测结果结构体
        ctx->type = i;
        ctx->ctxnum = i;
        ctx->detect = detect;  // 指向detect 结构体
        ctx->var_start_with_num = sqli_ctxs[i].var_start_with_num;  // 是否变量以数字开头

        // 这里存储的是sqli_detect_ctx 结构体。
        // 因为sqli_detect_ctx 中第一个成员就是detect_ctx 结构体 所以等价于detect_ctx
        detect->ctxs[i] = (void *)ctx;
    }
    // 返回初始化好的检测器
    return (detect);
}
```

### **3.4 detect\_start 给上下文变量赋值**

内置了5种检测类型

```
static const struct {
    struct detect_ctx_desc desc;
    enum sqli_parser_tokentype start_tok;
    bool var_start_with_num;
} sqli_ctxs[] = {
    // clang-format off
    [SQLI_CTX_DATA] = {
        .desc = {.name = {CSTR_LEN("data")}},
        .start_tok = TOK_START_DATA,  //上下文的开始
        .var_start_with_num = false,
    },
    [SQLI_CTX_IN_STRING] = {
        .desc = {.name = {CSTR_LEN("str")}},
        .start_tok = TOK_START_STRING, //表示SQL字符串上下文的开始
        .var_start_with_num = false,
    },
    [SQLI_CTX_RCE] = {
        .desc = {.name = {CSTR_LEN("rce")}, .rce = true},
        .start_tok = TOK_START_RCE, //表示远程命令执行上下文的开始
        .var_start_with_num = false,
    },
    [SQLI_CTX_DATA_VAR_START_WITH_NUM] = {
        .desc = {.name = {CSTR_LEN("data_num")}},
        .start_tok = TOK_START_DATA, //数据上下文的起始令牌
        .var_start_with_num = true,
    },
    [SQLI_CTX_IN_STRING_VAR_START_WITH_NUM] = {
        .desc = {.name = {CSTR_LEN("str_num")}},
        .start_tok = TOK_START_STRING,  //字符串上下文的起始令牌
        .var_start_with_num = true,
    },
    [SQLI_CTX_RCE_VAR_START_WITH_NUM] = {
        .desc = {.name = {CSTR_LEN("rce_num")}, .rce = true},
        .start_tok = TOK_START_RCE, //远程命令执行上下文的起始令牌
        .var_start_with_num = true,
    },
};
```

detect\_sqli\_start 函数都会给每个上下文进行初始化。给这个上下文最开始的一个状态。

这里使用了detect\_sqli\_push\_token 进行写入状态

```
static int
detect_sqli_start(struct detect *detect)
{
    unsigned i;
    // 遍历所有上下文
    for (i = 0; i < detect->nctx; i++) {
        struct sqli_detect_ctx *ctx = (void *)detect->ctxs[i];
        // 如果当前上下文已经完成，则跳过
        if (ctx->res.finished){
            printf("ctx %u finished\n", i);
            continue;
        }

        // yypstate_new
        ctx->pstate = sqli_parser_pstate_new();
        sqli_lexer_init(&ctx->lexer);
        if (detect_sqli_push_token(ctx, sqli_ctxs[ctx->type].start_tok, NULL) != 0)
            break;
    }
    return (0);
}
```

# 四、词法分析

**re2c 代码如下**

https://github.com/wallarm/libdetection/blob/master/lib/sqli/sqli\_lexer.re2c

### **4.1 detect\_add\_data 添加Token到语法分析中**

首先是通过sqli\_get\_token 来获取到上下文的的一个Token 那么这个Token 是怎么产生的。如下

```
static int
detect_sqli_add_data(struct detect *detect, const void *data, size_t siz, bool fin)
{
    unsigned i;
    union SQLI_PARSER_STYPE token_arg;
    int rv = 0;
    // 遍历所有上下文
    for (i = 0; i < detect->nctx; i++) {
        // 打印一下i对应的start_tok
        printf("[DEBUG] 开始检测上下文: %u\n", i);
        struct sqli_detect_ctx *ctx = (void *)detect->ctxs[i];
        //
        int token;
         // 如果当前上下文的解析已经完成，则跳过该上下文
        if (ctx->res.finished)
            continue;
        sqli_lexer_add_data(ctx, data, siz, fin);
        do {
            memset(&token_arg, 0, sizeof(token_arg)); // 清空token_arg结构体
            token = sqli_get_token(ctx, &token_arg);

done:
    return (rv);
}
```

### **4.2 Token 产生的过程**

以用户输入1′ union select 1,2,3,4 — 为例子

ctx->lexer.instring 为true的状态下

最开始进入到词法分析中

```
<> {
 // 检查是否在字符串处理模式
  if (c...