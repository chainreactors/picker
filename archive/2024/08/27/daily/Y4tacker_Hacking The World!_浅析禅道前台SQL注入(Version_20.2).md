---
title: 浅析禅道前台SQL注入(Version<20.2)
url: https://y4tacker.github.io/2024/08/26/year/2024/8/%E6%B5%85%E6%9E%90%E7%A6%85%E9%81%93%E5%89%8D%E5%8F%B0SQL%E6%B3%A8%E5%85%A5-Version-20-2/
source: Y4tacker:Hacking The World!
date: 2024-08-27
fetch_date: 2025-10-06T18:03:23.495641
---

# 浅析禅道前台SQL注入(Version<20.2)

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 正文](#%E6%AD%A3%E6%96%87)
   1. [1.1. 漏洞分析](#%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
   2. [1.2. 踩坑1-环境炸了](#%E8%B8%A9%E5%9D%911-%E7%8E%AF%E5%A2%83%E7%82%B8%E4%BA%86)
   3. [1.3. 踩坑2-如何触发SQL执行](#%E8%B8%A9%E5%9D%912-%E5%A6%82%E4%BD%95%E8%A7%A6%E5%8F%91SQL%E6%89%A7%E8%A1%8C)
2. [2. 修复](#%E4%BF%AE%E5%A4%8D)
3. [3. 其他](#%E5%85%B6%E4%BB%96)

# 浅析禅道前台SQL注入(Version<20.2)

Y4tacker

2024-08-26 (Updated: 2025-09-02)

[PHP](/categories/PHP/)

[PHP](/tags/PHP/), [禅道](/tags/%E7%A6%85%E9%81%93/)

## 正文

### 漏洞分析

代码直接从次新版20.1.1

第一次看zentao的系统，第一步肯定还是需要熟悉框架，还好前人栽树后人乘凉，简单看下面这个链接可以过一下

<https://blog.csdn.net/hjlyffsina/article/details/112280795>

在index.php中，首先创建了应用实例，初始化了一些配置

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 ``` | ``` $app = router::createApp('pms', dirname(dirname(__FILE__)), 'router');  public static function createApp(string $appName = 'demo', string $appRoot = '', string $className = '', string $mode = 'running') {     if(empty($className)) $className = self::class;     return new $className($appName, $appRoot, $mode); }  public function __construct(string $appName = 'demo', string $appRoot = '', string $mode = 'running') {     if($mode != 'running') $this->{$mode} = true;      $this->setPathFix();     $this->setBasePath();     $this->setFrameRoot();     $this->setCoreLibRoot();     $this->setAppRoot($appName, $appRoot);     $this->setTmpRoot();     $this->setCacheRoot();     $this->setLogRoot();     $this->setConfigRoot();     $this->setModuleRoot();     $this->setWwwRoot();     $this->setThemeRoot();     $this->setDataRoot();     $this->loadMainConfig();      $this->loadClass('front',  $static = true);     $this->loadClass('filter', $static = true);     $this->loadClass('form',   $static = true);     $this->loadClass('dbh',    $static = true);     $this->loadClass('sqlite', $static = true);     $this->loadClass('dao',    $static = true);     $this->loadClass('mobile', $static = true);      $this->setCookieSecure();     $this->setDebug();     $this->setErrorHandler();     $this->setTimezone();      if($this->config->framework->autoConnectDB) $this->connectDB();      $this->setupProfiling();     $this->setupXhprof();      $this->setEdition();      $this->setClient();      $this->loadCacheConfig(); } ``` |

在其中通过`loadMainConfig`初始化config参数，加载`config/config.php`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` public function loadMainConfig() {     /* 初始化$config对象。Init the $config object. */     global $config, $filter;     if(!is_object($config)) $config = new config();     $this->config = $config;      /* 加载主配置文件。 Load the main config file. */     $mainConfigFile = $this->configRoot . 'config.php';     if(!file_exists($mainConfigFile)) $this->triggerError("The main config file $mainConfigFile not found", __FILE__, __LINE__, true);     include $mainConfigFile; } ``` |

Config.php如下，简单记录下

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 ``` | ``` <?php /**  * ZenTaoPHP的config文件。如果更改配置，不要直接修改该文件，复制到my.php修改相应的值。  * The config file of zentaophp.  Don't modify this file directly, copy the item to my.php and change it.  *  * The author disclaims copyright to this source code.  In place of  * a legal notice, here is a blessing:  *  *  May you do good and not evil.  *  May you find forgiveness for yourself and forgive others.  *  May you share freely, never taking more than you give.  */  /* 保证在命令行环境也能运行。Make sure to run in ztcli env. */ if(!class_exists('config')){class config{}} if(!function_exists('getWebRoot')){function getWebRoot(){}}  /* 基本设置。Basic settings. */ $config->version       = '20.1.1';             // ZenTaoPHP的版本。 The version of ZenTaoPHP. Don't change it. $config->liteVersion   = '1.2';                // 迅捷版版本。      The version of Lite. $config->charset       = 'UTF-8';              // ZenTaoPHP的编码。 The encoding of ZenTaoPHP. $config->cookieLife    = time() + 2592000;     // Cookie的生存时间。The cookie life time. $config->timezone      = 'Asia/Shanghai';      // 时区设置。        The time zone setting, for more see http://www.php.net/manual/en/timezones.php. $config->webRoot       = '';                   // URL根目录。       The root path of the url. $config->customSession = false;                // 是否开启自定义session的存储路径。Whether custom the session save path. $config->edition       = 'open';               // 设置系统的edition，可选值：open|biz|max。Set edition, optional: open|biz|max. $config->tabSession    = false;                // 是否开启浏览器新标签独立session. $config->clientCache   = false;                // 是否开启客户端缓存。Whether enable client cache or not.  /* 框架路由相关设置。Routing settings. */ $config->requestType = 'PATH_INFO';               // 请求类型：PATH_INFO|PATHINFO2|GET。    The request type: PATH_INFO|PATH_INFO2|GET. $config->requestFix  = '-';                       // PATH_INFO和PATH_INFO2模式的分隔符。    The divider in the url when PATH_INFO|PATH_INFO2. $config->moduleVar   = 'm';                       // 请求类型为GET：模块变量名。            requestType=GET: the module var name. $config->methodVar   = 'f';                       // 请求类型为GET：模块变量名。            requestType=GET: the method var name. $config->viewVar     = 't';                       // 请求类型为GET：视图变量名。            requestType=GET: the view var name. $config->sessionVar  = 'zentaosid';               // 请求类型为GET：session变量名。         requestType=GET: the session var name. $config->views       = ',html,json,mhtml,xhtml,'; // 支持的视图类型。                       Supported view formats. $config->visions     = ',rnd,lite,or,';           // 支持的界面类型。                       Supported vision formats.  /* ZIN 设置。 ZIN settings. */ $config->zin = new stdclass();  /* 支持的主题和语言。Supported themes and languages. */ $config->themes['default'] = 'default'; $config->langs['zh-cn']    = '简体'; $config->langs['zh-tw']    = '繁體'; $config->langs['en']       = 'English'; $config->langs['de']       = 'Deutsch'; $config->langs['fr']       = 'Français'; //$config->langs['vi']       = 'Tiếng Việt'; //$config->langs['ja']       = '日本語';  /* 设备类型视图文件前缀。The prefix for view file for different device. */ $config->devicePrefix['mhtml'] = ''; $config->devicePrefix['xhtml'] = 'x.';  /* 默认值设置。Default settings. */ $config->default = new stdclass(); $config->default->view   = 'html';        //默认视图。 Default view. $config->default->lang   = 'en';          //默认语言。 Default language. $config->default->theme  = 'default';     //默认主题。 Default theme. $config->default->module = 'index';       //默认模块。 Default module. $config->default->method = 'index';       //默认方法。 Default method.  /* 数据库设置。Database settings. */ $config->db = new stdclass(); $config->slaveDB = new stdclass(); $config->db->persistent      = false;     // 是否为持续连接。       Pconnect or not. $config->db->driver          = 'mysql';   // 目前只支持MySQL数据库。Must be MySQL. Don't support other database server yet. $config->db->enco...