---
title: 再谈WP更新逻辑
url: https://h4ck.org.cn/2025/11/21910
source: obaby@mars
date: 2025-11-04
fetch_date: 2025-11-05T03:09:54.945162
---

# 再谈WP更新逻辑

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

黑客程序媛 / 逆向工程师 / 人工智能学徒 / 用爱发电的独立开发者

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 再谈WP更新逻辑

2025年11月4日
[42 条评论](https://h4ck.org.cn/2025/11/21910#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/微信图片_20251104101904_354_42.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20251104101904_354_42.jpg)

最近发现一个问题就是，wp 的后台打开速度越来越慢了，不过用屁股想想也能猜到肯定是 wp 后台的各种更新检查导致的。

网上通用的办法是直接禁用掉各种更新检查，但是鉴于安全问题其实我并不想直接这么干。现在各种漏洞扫描利用太频繁了，新版本能一定程度上降低被利用的风险。

wp 的更新的代码，本质上是有缓存机制的：

```
function _maybe_update_core() {
    $current = get_site_transient( 'update_core' );

    if ( isset( $current->last_checked, $current->version_checked )
        && 12 * HOUR_IN_SECONDS > ( time() - $current->last_checked )
        && wp_get_wp_version() === $current->version_checked
    ) {
        return;
    }

    wp_version_check();
}
```

检查更新的时候会判断是否在 12 小时内已经执行过，然而，这个破玩儿的问题在于，写入transient的时候不知道为什么失败了，于是每次进入后台都看到一堆 http 请求。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251104-101625.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251104-101625.jpg)

这 tm 就贼啦智障了，多的时候七八个请求，一个请求一秒钟，全部请求完都十几秒了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251104-101413-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251104-101413.jpg)

所以，我直接基于 redis 做了个缓存机制，避免重复请求。在 24 小时内请求过就不会再次请求了。直接对请求进行拦截。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251104-101249-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251104-101249.jpg)

既避免了无法检查更新，也解决了每次都检查更新的问题。

代码如下：

```
<?php
/**
 * 使用 Redis 缓存控制所有 WordPress 更新检查
 *
 * 控制以下更新检查的频率：
 * 1. wp_version_check() - WordPress 核心版本检查
 * 2. wp_update_themes() - 主题更新检查
 * 3. wp_update_plugins() - 插件更新检查
 * 4. wp_check_browser_version() - 浏览器版本检查
 * 5. wp_check_php_version() - PHP 版本检查
 *
 * 不依赖 WordPress 的 transient，直接使用 Redis 缓存
 * 如果 24 小时内更新过，跳过更新检查
 *
 * 使用方法：
 * 将此代码添加到主题的 functions.php 文件末尾
 * 或添加到插件的初始化函数中
 * https://h4ck.org.cn/wp-admin/index.php?debug_all_checks=1#qm-overview
 */

// ==========================================
// 配置项
// ==========================================

// 缓存键名
define('WP_CORE_UPDATE_CHECK_KEY', 'wp_core_update_check_time');
define('WP_THEMES_UPDATE_CHECK_KEY', 'wp_themes_update_check_time');
define('WP_PLUGINS_UPDATE_CHECK_KEY', 'wp_plugins_update_check_time');
define('WP_BROWSER_VERSION_CHECK_KEY', 'wp_browser_version_check_time');
define('WP_PHP_VERSION_CHECK_KEY', 'wp_php_version_check_time');

// 缓存有效期（24 小时）
define('WP_UPDATE_CHECK_EXPIRATION', DAY_IN_SECONDS);

// ==========================================
// 1. WordPress 核心版本检查 (wp_version_check)
// ==========================================

/**
 * 拦截 _maybe_update_core 函数
 * 在 admin_init 优先级 0 中移除 _maybe_update_core，使用 Redis 缓存控制
 */
add_action('admin_init', function() {
    // 移除 WordPress 原来的 _maybe_update_core 钩子
    remove_action('admin_init', '_maybe_update_core', 1);

    // 检查 Redis 缓存，看是否在 24 小时内更新过
    $last_check_time = wp_cache_get(WP_CORE_UPDATE_CHECK_KEY);

    if ($last_check_time !== false && is_numeric($last_check_time)) {
        $time_since_check = time() - $last_check_time;

        // 如果在 24 小时内，直接 return，跳过更新检查
        if ($time_since_check < WP_UPDATE_CHECK_EXPIRATION) {
            error_log('[Redis Core Check] 跳过核心版本检查 - 距离上次检查: ' . human_time_diff($last_check_time, time()));
            return; // 直接返回，不执行更新检查
        }
    }

    // 如果缓存过期或不存在，执行原来的更新检查逻辑
    _maybe_update_core();
}, 0); // 优先级 0，在 _maybe_update_core (优先级 1) 之前执行

/**
 * 监控 wp_version_check 的执行，设置 Redis 缓存
 * 注意：只有在缓存不存在时才设置，避免频繁刷新时重置缓存时间
 */
add_action('wp_version_check', function() {
    $existing_cache = wp_cache_get(WP_CORE_UPDATE_CHECK_KEY);
    if ($existing_cache === false) {
        wp_cache_set(
            WP_CORE_UPDATE_CHECK_KEY,
            time(),
            '',
            WP_UPDATE_CHECK_EXPIRATION
        );
        error_log('[Redis Core Check] wp_version_check 执行，已设置 Redis 缓存');
    }
}, 10);

/**
 * 通过过滤器拦截 update_core transient 设置，设置 Redis 缓存
 * 注意：只有在缓存不存在时才设置，避免频繁刷新时重置缓存时间
 */
add_filter('pre_set_site_transient_update_core', function($value, $transient_name) {
    $existing_cache = wp_cache_get(WP_CORE_UPDATE_CHECK_KEY);
    if ($existing_cache === false) {
        wp_cache_set(
            WP_CORE_UPDATE_CHECK_KEY,
            time(),
            '',
            WP_UPDATE_CHECK_EXPIRATION
        );
    }
    return $value;
}, 999, 2);

// ==========================================
// 2. 主题更新检查 (wp_update_themes)
// ==========================================

/**
 * 拦截 _maybe_update_themes 函数
 * 在 admin_init 优先级 0 中移除 _maybe_update_themes，使用 Redis 缓存控制
 */
add_action('admin_init', function() {
    // 移除 WordPress 原来的 _maybe_update_themes 钩子
    remove_action('admin_init', '_maybe_update_themes', 1);

    // 检查 Redis 缓存，看是否在 24 小时内更新过
    $last_check_time = wp_cache_get(WP_THEMES_UPDATE_CHECK_KEY);

    if ($last_check_time !== false && is_numeric($last_check_time)) {
        $time_since_check = time() - $last_check_time;

        // 如果在 24 小时内，直接 return，跳过更新检查
        if ($time_since_check < WP_UPDATE_CHECK_EXPIRATION) {
            error_log('[Redis Themes Check] 跳过主题更新检查 - 距离上次检查: ' . human_time_diff($last_check_time, time()));
            return; // 直接返回，不执行更新检查
        }
    }

    // 如果缓存过期或不存在，执行原来的更新检查逻辑
    _maybe_update_themes();
}, 0); // 优先级 0，在 _maybe_update_themes (优先级 1) 之前执行

/**
 * 监控 wp_update_themes 的执行，设置 Redis 缓存
 * 注意：只有在缓存不存在时才设置，避免频繁刷新时重置缓存时间
 */
add_action('wp_update_themes', function() {
    $existing_cache = wp_cache_get(WP_THEMES_UPDATE_CHECK_KEY);
    if ($existing_cache === false) {
        wp_cache_set(
            WP_THEMES_UPDATE_CHECK_KEY,
            time(),
            '',
            WP_UPDATE_CHECK_EXPIRATION
        );
        error_log('[Redis Themes Check] wp_update_themes 执行，已设置 Redis 缓存');
    }
}, 10);

/**
 * 通过过滤器拦截 update_themes transient 设置，设置 Redis 缓存
 * 注意：只有在缓存不存在时才设置，避免频繁刷新时重置缓存时间
 */
add_filter('pre_set_site_transient_update_themes', function($value, $transient_name) {
    $existing_cache = wp_cache_get(WP_THEMES_UPDATE_CHECK_KEY);
    if ($existing_cache === false) {
        wp_cache_set(
            WP_THEMES_UPDATE_CHECK_KEY,
            time(),
            '',
            WP_UPDATE_CHECK_EXPIRATION
        );
    }
    return $value;
}, 999, 2);

// ==========================================
// 3. 插件更新检查 (wp_update_plugins)
// ==========================================

/**
 * 方法1：在 HTTP 请求级别拦截插件更新 API
 * 直接拦截到 api.wordpress.org/plugins/update-check/ 的请求
 */
add_filter('pre_http_request', function($preempt, $args, $url) {
    // 检查是否是插件更新检查的 API 请求
    if (strpos($url, 'api.wordpress.org/plugins/update-check/') !== false) {
        // 检查 Redis 缓存，看是否在 24 小时内更新过
        $last_check_time = wp_cache_get(WP_PLUGINS_UPDATE_CHECK_KEY);

        if ($last_check_time !== false && is_numeric($last_check_time)) {
            $time_since_check = time() - $last_check_time;

            // 如果在 24 小时内，返回假数据，跳过 API 请求
            if ($time_since_check < WP_UPDATE_CHECK_EXPIRATION) {
                error_log('[Redis Plugins Check] 跳过插件更新检查 API 请求 - 距离上次检查: ' . human_time_diff($last_check_time, time()));

                // 返回一个符合 WordPress API 格式的响应
                // WordPress 期望的完整格式：
                // - plugins: 需要更新的插件数组
                // - n...