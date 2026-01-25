---
title: 屏幕监控工具
url: https://mp.weixin.qq.com/s/9zeK6j3wkew5XJczbqzsEA
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:51:39.160881
---

# 屏幕监控工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hMZ0ictzVvTsMUAZnDQD18PmmXXEUHEDGYwm47JM6pMhFynXkibibZ7EoDvbKQ1UvmqNblxJdLWpUBEXT5kuhNK6w/0?wx_fmt=jpeg)

# 屏幕监控工具

原创

鬼麦子
鬼麦子

鬼麦子

![]()

在小说阅读器中沉浸阅读

昨被msf和cs的屏幕监控功能背刺了，耽误事，局域网环境桥接网卡的传输速率就是一坨，常规的监控软件对目标软件又有基础检测，手搓+vibe coding，昨晚四十分钟屏幕截图工具搞定，现在屏幕监控工具搞定，支持截图与录屏，720\1080\原画...

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hMZ0ictzVvTsMUAZnDQD18PmmXXEUHEDGRGpRMKasAMPEh6PCowuF1STyeJQbMb2RJZRw7hE6DMDB6ibl491fWibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hMZ0ictzVvTsMUAZnDQD18PmmXXEUHEDGZBZDdHlibWslFj5cbzRia7Q8vl0b3fyHSeK8wvcQ3SLWEiaezpCrJpP0g/640?wx_fmt=jpeg&from=appmsg)

ai coding的开发效率是真可以，不得不夸。

https://github.com/guimaizi/luping

这玩意的优势就是够轻量，够有用，不花哨。

## 项目介绍

这是一个基于 Python 的屏幕监视系统，采用 C/S 架构，支持多客户端监控、实时屏幕显示、手动截图和录屏功能。

### 主要功能

* **多客户端监控**：支持同时连接多个客户端，通过 IP 地址切换不同的监控画面
* **实时屏幕显示**：WebUI 实时显示客户端屏幕画面，无闪屏现象
* **手动截图**：点击按钮手动截取当前客户端屏幕，保存为 JPG 格式
* **手动录屏**：点击按钮开始/停止录屏，保存为 MP4 格式
* **配置化参数**：客户端支持配置帧率、分辨率等参数
* **自动重连**：客户端连接失败后自动重试
* **本地存储**：WebUI 会保存用户选择的客户端，页面刷新后自动恢复之前的选择
* **稳定性优化**：多客户端连接时不会出现画面闪烁或切换混乱的情况

## 技术栈

### 服务端

* Flask：Web 框架
* Flask-SocketIO：WebSocket 通信
* OpenCV：视频/图像处理
* HTML/CSS/JavaScript：WebUI 界面

### 客户端

* Python：核心语言
* socketio-client：WebSocket 客户端
* PyAutoGUI：屏幕截图
* OpenCV：图像处理
* JSON：配置文件
* screeninfo：获取屏幕分辨率

## 项目结构

```
luping/
├── client/              # 客户端目录
│   ├── client.py        # 客户端主程序
│   └── config.json      # 客户端配置文件
├── server/              # 服务端目录
│   ├── server.py        # 服务端主程序
│   ├── templates/       # WebUI 模板
│   │   └── index.html   # WebUI 界面
│   ├── videos/          # 录屏文件存储目录
│   └── images/          # 截图文件存储目录
├── README.md            # 项目说明文档
└── config_example.txt   # 配置文件示例
```

## 快速开始

### 1. 安装依赖

#### 服务端依赖

```
pip install flask flask-socketio opencv-python
```

#### 客户端依赖

```
pip install socketio-client pyautogui opencv-python pillow screeninfo python-socketio
```

### 2. 配置

#### 客户端配置

编辑 `client/config.json` 文件：

```
{
    "server": {
        "host": "localhost",  // 服务端 IP 地址
        "port": 5000,          // 服务端端口
        "path": "socket.io"
    },
    "screencast": {
        "fps": 15,             // 帧率
        "quality": 0.8,        // 图像质量 (0-1)
        "resolution": 2        // 分辨率等级 (0:720p, 1:1080p, 2:原画)
    },
    "reconnect": {
        "timeout": 5           // 重连超时时间（秒）
    }
}
```

### 3. 运行

#### 启动服务端

```
cd server
python server.py
```

#### 启动客户端

```
cd client
python client.py
```

### 4. 访问 WebUI

打开浏览器，访问：`http://localhost:5000`

## 使用说明

### WebUI 操作

1. **客户端切换**：在下拉菜单中选择要监视的客户端 IP，系统会自动保存您的选择
2. **本地存储**：WebUI 会将您选择的客户端保存到浏览器本地存储中，页面刷新或重新连接后会自动恢复之前的选择
3. **截图**：点击"截图"按钮，系统会保存当前客户端的屏幕截图到 `server/images` 目录
4. **录屏**：点击"开始录屏"按钮开始录制，点击"停止录屏"按钮停止录制，视频会保存到 `server/videos` 目录
5. **稳定性**：多客户端连接时，WebUI 只会显示当前选中客户端的屏幕画面，不会出现画面闪烁或切换混乱的情况

### 分辨率设置

客户端配置文件中的 `resolution` 参数支持以下值：

* `0`：720p (1280x720)
* `1`：1080p (1920x1080)
* `2`：原画（使用当前屏幕分辨率）

### 帧率设置

客户端配置文件中的 `fps` 参数控制屏幕截图的频率，建议值为 10-20 fps，根据网络带宽和性能调整。

## 注意事项

1. 确保服务端和客户端在同一网络环境下，或客户端能够访问服务端 IP
2. 客户端需要有足够的权限进行屏幕截图
3. 高帧率和高分辨率会增加网络带宽和系统资源消耗，请根据实际情况调整
4. 多客户端同时连接时，可能会影响性能，请合理控制连接数量

## 常见问题

### 1. 客户端连接失败

* 检查服务端是否正在运行
* 检查服务端 IP 和端口配置是否正确
* 检查网络连接是否正常

### 2. 截图或录屏失败

* 确保已选择正确的客户端
* 确保客户端正在发送屏幕数据
* 检查服务端的 `images` 和 `videos` 目录权限

### 3. 视频播放速度异常

* 客户端和服务端的帧率设置已默认匹配，无需手动调整

本项目仅供学习和研究使用，请勿用于非法用途。

写段小字，之后会尽快发一个facai安全工具，很好使的。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

鬼麦子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

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