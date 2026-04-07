---
title: Baby Anti-Spam 自建反垃圾评论系统
url: https://zhongxiaojie.cn/2026/04/798/
source: obaby 𝐢‍𝐧⃝ void
date: 2026-04-06
fetch_date: 2026-04-07T04:29:26.290140
---

# Baby Anti-Spam 自建反垃圾评论系统

[![obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/wp-content/uploads/2026/01/new-logo-27.png)](https://zhongxiaojie.cn)

程序媛 / 独立开发者 / 智商不稳定的女神经

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

 [Menu](#mobilemenu)

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

[程序媛](https://zhongxiaojie.cn/category/code-girl/)

# Baby Anti-Spam 自建反垃圾评论系统

2026年4月6日 18:05
[33 条评论](https://zhongxiaojie.cn/2026/04/798/#comments)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/330A0347-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/330A0347.jpg)

很久之前，就经常收到akismet的授权提醒，对应一个错误码10010。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/BaiduShurufa_2026-4-6_14-13-58.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/BaiduShurufa_2026-4-6_14-13-58.png)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/BaiduShurufa_2026-4-6_14-16-0.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/BaiduShurufa_2026-4-6_14-16-0.png)

刚开始还以为是多域名访问导致的授权校验出问题了。后来换了n个key，同时添加了插件hook掉所有的垃圾评论检测逻辑，让全部走统一的域名，结果前几天又收到这个提醒了。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Screenshot-2026-04-06-202533.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Screenshot-2026-04-06-202533.png)

插件代码：

```
<?php
/**
 * Plugin Name: Akismet 单一主域名（多域名站点）
 * Description: 当站点配置了多个域名时，强制发往 Akismet 的请求只使用一个主域名，避免被计为多站点触发 10010。
 * Version: 1.0
 * Author: obaby
 *
 * 使用：在下方设置 AKISMET_CANONICAL_HOME 为主域名（或留空则用 WordPress「设置」里的站点地址）。
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * 主域名（规范 URL，不要末尾斜杠）。留空则使用 get_option( 'home' )。
 * 例如: https://www.example.com
 */
if ( ! defined( 'AKISMET_CANONICAL_HOME' ) ) {
    define( 'AKISMET_CANONICAL_HOME', 'https://zhongxiaojie.cn' );
}

/**
 * 获取发往 Akismet 时使用的唯一主域名 URL。
 */
function akismet_single_domain_get_canonical_home() {
    $home = AKISMET_CANONICAL_HOME;
    if ( $home === '' || $home === null ) {
        $home = get_option( 'home' );
    }
    return untrailingslashit( $home );
}

/**
 * 将任意 URL 替换为使用主域名的版本（只改 host，保留 path/query）。
 */
function akismet_single_domain_normalize_url( $url, $canonical_home ) {
    if ( empty( $url ) || ! is_string( $url ) ) {
        return $url;
    }
    $parsed = wp_parse_url( $url );
    $canon  = wp_parse_url( $canonical_home );
    if ( empty( $canon['scheme'] ) || empty( $canon['host'] ) ) {
        return $url;
    }
    $scheme = isset( $parsed['scheme'] ) ? $parsed['scheme'] : $canon['scheme'];
    $host   = $canon['host'];
    $path   = isset( $parsed['path'] ) ? $parsed['path'] : '/';
    $query  = isset( $parsed['query'] ) ? '?' . $parsed['query'] : '';
    $frag   = isset( $parsed['fragment'] ) ? '#' . $parsed['fragment'] : '';
    return $scheme . '://' . $host . $path . $query . $frag;
}

/**
 * 统一 verify-key / get-subscription / get-stats 的 blog 为主域名。
 */
add_filter( 'akismet_request_args', function ( $request_args, $path ) {
    $paths = array( 'verify-key', 'get-subscription', 'get-stats' );
    if ( ! in_array( $path, $paths, true ) ) {
        return $request_args;
    }
    $canon = akismet_single_domain_get_canonical_home();
    if ( ! empty( $request_args['blog'] ) ) {
        $request_args['blog'] = $canon;
    }
    return $request_args;
}, 10, 2 );

/**
 * 统一 comment-check（以及 recheck）的 blog、permalink，并把请求里的 HTTP_HOST 等改为主域名。
 */
add_filter( 'akismet_request_args', function ( $request_args, $path ) {
    if ( $path !== 'comment-check' ) {
        return $request_args;
    }
    $canon = akismet_single_domain_get_canonical_home();
    $parsed = wp_parse_url( $canon );
    if ( empty( $parsed['host'] ) ) {
        return $request_args;
    }
    $canon_host = $parsed['host'];

    $request_args['blog'] = $canon;
    if ( ! empty( $request_args['permalink'] ) ) {
        $request_args['permalink'] = akismet_single_domain_normalize_url( $request_args['permalink'], $canon );
    }

    // 让服务端看到的“当前请求”也统一为主域名，减少被计为多站点
    if ( isset( $request_args['HTTP_HOST'] ) ) {
        $request_args['HTTP_HOST'] = $canon_host;
    }
    if ( isset( $request_args['REQUEST_URI'] ) ) {
        $uri = $request_args['REQUEST_URI'];
        $request_args['REQUEST_URI'] = ( is_string( $uri ) && ( $p = wp_parse_url( $uri, PHP_URL_PATH ) ) !== null ) ? $p : '/';
    }
    if ( isset( $request_args['DOCUMENT_URI'] ) ) {
        $uri = $request_args['DOCUMENT_URI'];
        $request_args['DOCUMENT_URI'] = ( is_string( $uri ) && ( $p = wp_parse_url( $uri, PHP_URL_PATH ) ) !== null ) ? $p : '/';
    }
    return $request_args;
}, 10, 2 );

/**
 * 统一 submit-spam / submit-ham 的 blog、permalink。
 */
add_filter( 'akismet_request_args', function ( $request_args, $path ) {
    if ( ! in_array( $path, array( 'submit-spam', 'submit-ham' ), true ) ) {
        return $request_args;
    }
    $canon = akismet_single_domain_get_canonical_home();
    $request_args['blog'] = $canon;
    if ( ! empty( $request_args['permalink'] ) ) {
        $request_args['permalink'] = akismet_single_domain_normalize_url( $request_args['permalink'], $canon );
    }
    return $request_args;
}, 10, 2 );
```

这次授权的密钥撑得时间稍微长了点，但是最终还是收到了这个提醒，意思是需要订购商业版授权。我这个人站点为了发垃圾评论订购一个商业版授权，确实有些难以接受。

于是，我决定自建反垃圾评论系统，基于scikit-learn实现了现在的这套垃圾评论检测系统，训练数据一部分来源于github的开源数据，另外一个就是我自己博客的评论数据。为了保证样本正例和负例数量差别不至于过大，经过各种方式进行了多轮数据清洗。

如果想要评论识别更加准确，可以提供自己的博客评论数据，如果能提供垃圾评论更好。现在欠缺的主要是垃圾评论数据，正常的评论数据我已经提供几千条数据。

效果测试：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Screenshot-2026-04-06-175352-scaled.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Screenshot-2026-04-06-175352.png)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Screenshot-2026-04-06-175539-scaled.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Screenshot-2026-04-06-175539.png)

测试地址：<https://anti-spam.zhongxiaojie.cn/test/spam>

简介：

面向 **中英混合** 评论的 WordPress 垃圾识别方案：PHP 插件在评论入库前调用 **本机 Python 服务**，由小型多语种向量模型 + 分类器（或演示用规则）给出垃圾概率。

适合评论量不大、单机部署（例如 **4 核 / 8GB RAM** 的 Ubuntu），服务与 WordPress 同机时使用 `127.0.0.1` 即可。

目录结构：

```
baby_anti_spam/
├── README.md
├── screenshots/             # 文档：服务启动与 curl 自测示意
│   ├── service.png
│   └── test.png
├── service/                 # Python FastAPI 侧车服务
│   ├── .env.example
│   ├── requirements.txt
│   ├── requirements-ml.txt
│   ├── run.py
│   ├── app/
│   │   └── stats_backends/   # 统计存储：sqlite / mysql
│   └── scripts/
│       ├── init_stats_mysql.sql
│       └── init_stats_mysql.py
│       ├── train_sklearn.py
│       ├── download_embedding_model.py
│       └── download_embedding_model.sh
└── wordpress/baby-anti-spam/
    └── baby-anti-spam.php # WordPress 插件
```

关键配置：

```
| 变量 | 说明 |
|------|------|
| `SPAM_HOST` | 监听地址，同机建议 `127.0.0.1` |
| `SPAM_PORT` | 端口，默认 `8765` |
| `SPAM_API_SECRET` | **单密钥模式（兼容旧版）**：未配置 `SPAM_API_KEYS` 且未配置 `SPAM_API_KEYS_FILE` 时，仅此密钥有效，等价于 name=`default`、不限流（`max_rpm=0`）。与 WP 插件里填写的密钥一致 |
| `SPAM_API_KEYS` | **多密钥**：JSON 数组。每项为 `name`（唯一，用于统计与限流分组）、`key` 或 `secret`（与请求头一致）、`max_rpm` 或 `rpm`（每分钟最大请求数，`0` 表示不限制）。与 `SPAM_API_KEYS_FILE` 合并时：**先读文件条目，再追加本变量** |
| `SPAM_API_KEYS_FILE` | 可选，指向 JSON 文件，根节点为与上表相同结构的**数组**。文件必须存在，否则进程启动失败 |
| `SPAM_MODEL_PATH` | 训练得到的 `*.joblib` 路径；留空则取决于 `SPAM_FALLBACK_RULES` |
| `SPAM_FALLBACK_RULES` | 无模型文件时是否启用内置极简规则（演示用）；生产训练后应设为 `false` 并配置 `SPAM_MODEL_PATH` |
| `SPAM_LABEL_THRESHOLD` | 可选，默认 `0.8`。`spam_score` ≥ 此值时 JSON 中 `label` 为 `spam`，否则为 `normal` |
| `SPAM_DFA_ENABLED` | 默认 `true`。为 `true` 时使用 `dfa-python-filter/keywords` 做敏感词检测；命中则直接 `spam_score=1`、`detail=dfa_sensitive`（早于 sklearn） |
| `SPAM_DFA_KEYWORDS_PATH` | 可选，自定义敏感词文件路径；留空则用 `service/dfa-python-filter/keywords` |
| `SPAM_NON_CHINESE_FLOOR_ENABLED` | 默认 `true`。为 `true` 时若合并后的 author/email/u...