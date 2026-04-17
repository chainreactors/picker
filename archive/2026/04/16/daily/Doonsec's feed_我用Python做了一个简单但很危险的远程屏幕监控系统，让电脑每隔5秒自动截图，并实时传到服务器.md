---
title: 我用Python做了一个简单但很危险的远程屏幕监控系统，让电脑每隔5秒自动截图，并实时传到服务器
url: https://mp.weixin.qq.com/s/fSWT7EN1aS0gO5FxelS_6w
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:43:18.709368
---

# 我用Python做了一个简单但很危险的远程屏幕监控系统，让电脑每隔5秒自动截图，并实时传到服务器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjUqReVpicMxGoCIcCDIbYOf4qnMnbtjibzeUaLbO5lyjwhT5TLZa2LsMqp3SDzaLhKXMWLZVkNUXDxSr8iaEbGzs3GadCQt3GibIyw/0?wx_fmt=jpeg)

# 我用Python做了一个简单但很危险的远程屏幕监控系统，让电脑每隔5秒自动截图，并实时传到服务器

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今天我灵光一闪

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXq2zFs5FKXta4Fj7QVLayGNpDibN3RicCTffxIoNX7HpcPanRfEGjmobr9KxUW5EuG8E5Wr5icicekwibu05hQgtHcR2TTjjb9qxPQ/640?wx_fmt=png&from=appmsg)

我就在想，如果我不在电脑前，我能不能“看它正在干什么？”

或者说我能看别人电脑在干什么。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjVMCdNklY1uWlb5nBR8IyLkAlA52iccIoYMeqZKIdVZc7ZwGiaia1IKIqFa9q7947o3gf6SEQrcUDTMDPiblp4XO3jjHrvKke9BPxE/640?wx_fmt=jpeg&from=appmsg)

于是乎，我就简单写了一个程序：

👉 它会每隔几秒自动截图，并上传到服务器。

然后我打开网页，就能看到那台电脑的屏幕。

就像远程监控一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXIQia5NGX5eFKURX70ECNpibEdvf6TnLEsGH5B2dgWDzdvll4htNIF7zgYBczsGSgaSHJA2nLVb2GmoyCJgsrOFKETEjmgdB5tM/640?wx_fmt=png&from=appmsg)

事先声明

* 仅用于学习/测试
* 不涉及他人设备
* 不用于非法用途

这个系统实现了：

* 📸 客户端定时截图上传
* 🌐 服务端实时接收并存储
* 🖥️ Web 页面实时展示截图
* 👥 多用户隔离
* ⚡ WebSocket 实时刷新
* 🖼️ 缩略图优化 + 图片放大预览

技术栈：

* Python 3
* Flask
* Flask-SocketIO
* gevent
* Pillow
* pyautogui

先看效果：

服务器环境准备

⚙️ 更新系统、安装Python&pip环境、安装项目依赖：

```
apt update && apt upgrade -yapt install python3 python3-pip -ypip3 install flask flask-socketio gevent gevent-websocket pillow
```

📁 创建项目结构

```
mkdir screen-monitorcd screen-monitortouch app.pymkdir uploadsmkdir templatestouch templates/index.html
```

将以下图中代码写入到app.py文件中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWIxcEgKv7DCxY6XDDvzaC941UZTwqXrKHaYZjQJxkRaRGmE4Vc5ZDZT1jOMaC1o4nR3nGtIFAJePJRRDt1BxEugsnwNvQ7xGQ/640?wx_fmt=png&from=appmsg)

```
app = Flask(__name__)app.secret_key = "super_secret_key"socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')
UPLOAD_FOLDER = 'uploads'THUMB_FOLDER = 'thumbs'
os.makedirs(..., exist_ok=True)
USERS = {    "admin": "123456",    "user1": "111111"}
```

**作用：**

* 创建 Flask 应用
* `secret_key 用于登录 session`
* 启用 WebSocket（实时推送）
* `uploads：存原图`
* `thumbs：存缩略图`
* `自动创建目录（避免报错）`
* `简单账号密码（写死的），用于登录验证`

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVmKPXeZERmy6x1HZZEBKsMFicuZyBfHyGTe1WROd55OG1PvJPTBQyCnFn3skGdVjpWAFstrvacfMM8zCyVUpRxwWPdbmTM5ep0/640?wx_fmt=png&from=appmsg)

```
@app.route('/login')
@app.route('/')
```

登录核心逻辑和首业访问控制：

* POST：校验用户名密码
* 成功 → 写入 `session['user']`
* 失败 → 返回错误
* 未登录 → 跳转 `/login`
* `已登录 → 渲染页面`

```
@app.route('/upload', methods=['POST'])
```

`上传接口（核心）：`

**做了4件事：**

1. 接收图片 + user + device
2. 按用户创建目录
3. 保存原图
4. 生成缩略图
5. 用户数据隔离

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXuSayXCyTvSjCM0dycLcJGhRyemGiaPGj3C6xQiblBFheOxdT3djeNJicMHUVq5O1qvR0sia1DV9ZqxPoA5n338IBtIicpHQkJiceq0/640?wx_fmt=png&from=appmsg)

```
socketio.emit('new_image', {...})
```

⚡WebSocket 推送

👉 告诉前端：有新图片了

```
@app.route('/delete/<filename>')
```

🗑️ 删除功能

**作用：**

* 只删除“当前登录用户”的图片
* 同时删原图 + 缩略图
* 通知前端同步删除

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjVgldbntUzicxy227hTCk8TMb3eC5micB7R7cI1wiafklfHHTdicDKkiac6ZoLNib8fOat4mqaBWPZ2yVbobuk12B47dwiaNXNHNalteU/640?wx_fmt=png&from=appmsg)

```
@app.route('/api/images')
/uploads/<user>/<filename>/thumbs/<user>/<filename>
```

图片列表 API和图片访问接口：

作用：

* 只返回当前用户的图片
* 不会看到别人的数据
* 提供图片访问路径
* 前端通过 URL 加载图片

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUV2ZJoicmicebTZmVadIJeJqKcUaickJRoaBWrPxh6n0yVzhRdtcnyNM1dJleKZZuLRTDMPPUiaqnC13W5cBCt87Rqcic5D8dEeQP4/640?wx_fmt=png&from=appmsg)

🚀 启动服务

```
socketio.run(app, host='0.0.0.0', port=5000)
```

**作用：**

* 启动 Web 服务 + WebSocket
* 监听所有 IP

网页样式

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUJcBkOnaTQxVia9XMvBu72NtBibk0jlia0UK5ytWOR44GxzM6XEQianJCHgCiaxk7953jQ7RmpzMw4SfYf9Skn626xJ0jArdgpTsoY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXMjibk6wUYhzVvaguk5vMQnPHyZOjn5AbK2qQGtaWXaibhzpgH9kZbswjh0RbNA6icCe3I7YAkOYicCHynbXiaEjjZc9hwibyk8cMzM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXyj5Fk4S7y8V25bRIfEbLR0omic7l7wDJlgF9vpwFOb5u0ETZG4ZvCBhiaXB3a3guXrGv9Phv1Ot1RKiaALPplKX0uhogWzZrRpQ/640?wx_fmt=png&from=appmsg)

之后服务端就已经配置完成，就可以启动项目：

```
nano app.py
```

运行之后看到：

```
Running on http://0.0.0.0:5000
```

或者没有任何输出，则证明启动成功，只要不报错就行。

这时你可以访问：

```
http://你的服务器IP:5000/login
```

就能进入到页面。

客户端

我这里使用的是PyCharm进行编码，然后打包exe程序。

你需要安装依赖：

```
pip install pyautogui requests pyinstaller
```

创建一个client.py的文件，然后将以下代码输入进去：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjW8JIUSibJVQNicdF2VfqxYvWMWqO6B5hcM19V1DiaJLJFOPgib8rqCg1DcucbJF5OXCZgtYX34wiaT75w2HEQWjicxoMicMXKyjMmssk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVpm1r5AEuPddliatT5eAzJnjKPzUjtAnyolicQTVuMpXeMVQQM0E9KiaFicLxgXs7g0LC40FJW4AEkV7HibDDEYln1s0icKuGvgJGBw/640?wx_fmt=png&from=appmsg)

打包成exe：

进入 `client.py` 所在目录，执行打包命令：

```
pyinstaller -F -w client.py
```

## 参数解释

* `-F`

  👉 打包成单个 exe 文件
* `-w`

  👉 不显示黑窗口（后台运行）

## 打包完成后

会生成：

```
dist/client.exe
```

之后就可以运行客户端，运行之后后台会有进程，不会有任何窗口。

之后回到网页，你就能在网页看到上传到服务器的屏幕截图，每5秒截一次。

这个项目还可以扩展很多，例如：键盘记录、实时视频流等。你们可以自行发挥。

本期内容到此结束。

三连加关注，追文不迷路。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_02.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_80@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_64@2x.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXibu188DgR2icXAYBQtNf01bhpxic7jqf6urQPOCpmib4T38DSJQ1bdm1hkrqeCwSNPWCjicD9GAj5icWHicBWTI9sHU19kFibKaVtJ50/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

W不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

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