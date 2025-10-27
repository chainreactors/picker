---
title: gdk_window_get_state: assertion ‘GDK_IS_WINDOW (window)’ failed 报错解决
url: https://zgao.top/gdk_window_get_state-assertion-gdk_is_window-window-failed-%e6%8a%a5%e9%94%99%e8%a7%a3%e5%86%b3/
source: Zgao's blog
date: 2024-04-09
fetch_date: 2025-10-04T12:14:59.871069
---

# gdk_window_get_state: assertion ‘GDK_IS_WINDOW (window)’ failed 报错解决

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# gdk\_window\_get\_state: assertion ‘GDK\_IS\_WINDOW (window)’ failed 报错解决

* [首页](https://zgao.top)
* [gdk\_window\_get\_state: assertion ‘GDK\_IS\_WINDOW (window)’ failed 报错解决](https://zgao.top:443/gdk_window_get_state-assertion-gdk_is_window-window-failed-%E6%8A%A5%E9%94%99%E8%A7%A3%E5%86%B3/)

[12月 8, 2023](https://zgao.top/2023/12/)

### gdk\_window\_get\_state: assertion ‘GDK\_IS\_WINDOW (window)’ failed 报错解决

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/gdk_window_get_state-assertion-gdk_is_window-window-failed-%E6%8A%A5%E9%94%99%E8%A7%A3%E5%86%B3/)

使用VNC远程连接Linux，运行局域网传输工具localsend报错如下：

```
└─# localsend_app

(localsend_app:4185182): Gdk-CRITICAL **: 15:20:28.434: gdk_window_get_state: assertion 'GDK_IS_WINDOW (window)' failed

** (localsend_app:4185182): WARNING **: 15:20:28.450: Failed to start Flutter renderer: 没有可用的 GL 实现
```

这个错误信息表明`localsend_app`在尝试启动Flutter渲染器时，没有可用的OpenGL（GL）实现而失败了。因为标准的VNC服务器并不支持OpenGL图形加速，而Flutter应用依赖于OpenGL进行渲染。

文章目录

[ ]

* [解决方案](#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88 "解决方案")
* [卸载默认的vnc（可选）](#%E5%8D%B8%E8%BD%BD%E9%BB%98%E8%AE%A4%E7%9A%84vnc%EF%BC%88%E5%8F%AF%E9%80%89%EF%BC%89 "卸载默认的vnc（可选）")
* [安装TurboVNC](#%E5%AE%89%E8%A3%85TurboVNC "安装TurboVNC")
* [安装OpenGL库](#%E5%AE%89%E8%A3%85OpenGL%E5%BA%93 "安装OpenGL库")
  + [使用 glxgears 测试](#%E4%BD%BF%E7%94%A8_glxgears_%E6%B5%8B%E8%AF%95 "使用 glxgears 测试")

## 解决方案

Linux默认安装的vnc都是tightVNC（本身不支持GL渲染），所以需要将其更换为支持OpenGL的vnc，比如TurboVNC。

## 卸载默认的vnc（可选）

```
apt remove --purge tightvncserver
```

可以选择卸载或者是同时保留不同的vncserver，最后替换配置文件中vnc路径即可。

## 安装TurboVNC

直接从官方网站下载能获取到最新版本TurboVNC。

```
https://sourceforge.net/projects/turbovnc/files/
```

![](https://zgao.top/wp-content/uploads/2024/04/image-1024x787.png)

选择对应的包下载安装。

```
dpkg -i turbovnc_3.1_amd64.deb
```

安装完成后turbovnc默认的路径为：

```
/opt/TurboVNC/bin/vncserver
```

修改配置文件，替换原本的vncserver路径。

```
# cat /etc/systemd/system/vncserver@.service
[Unit]
Description=Start TightVNC server at startup
After=syslog.target network.target
[Service]
Type=forking
User=root
Group=root
WorkingDirectory=/root
PIDFile=/root/.vnc/%H:%i.pid
ExecStartPre=-/bin/rm -f /tmp/.X11-unix/X%i /tmp/.X%i-lock
ExecStart=/opt/TurboVNC/bin/vncserver -depth 32  -geometry 2560x1440 :%i
ExecStop=/opt/TurboVNC/bin/vncserver -kill :%i
Restart=on-failure
RestartSec=5
[Install]
WantedBy=multi-user.target
```

![](https://zgao.top/wp-content/uploads/2024/04/image-2-1024x563.png)

修改了服务文件，需要重新加载并启动服务。

```
sudo systemctl daemon-reload
sudo systemctl restart vncserver@1
sudo systemctl status vncserver@1
```

![](https://zgao.top/wp-content/uploads/2024/04/image-3-1024x526.png)

就表明turbovnc运行成功了。

## 安装OpenGL库

```
apt install libgl1-mesa-dev
```

### 使用 `glxgears` 测试

```
apt install mesa-utils
```

`glxgears` 是一个简单的3D动画程序，包含在`mesa-utils`包中。运行`glxgears`可以快速检查系统是否能运行OpenGL程序。

![](https://zgao.top/wp-content/uploads/2024/04/image-1-1024x536.png)

如果看到一个窗口出现，并且有齿轮在转动，这意味着OpenGL正在正常工作。

重新运行flutter程序也就不会出现报错了。

![](https://zgao.top/wp-content/uploads/2024/04/image-4-1024x567.png)

而且替换为turbovnc后，画面的传输质量也更好了。

Post Views: 567

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/gdk_window_get_state-assertion-gdk_is_window-window-failed-%E6%8A%A5%E9%94%99%E8%A7%A3%E5%86%B3/#respond)

Δ

版权©2020 Author By : Zgao