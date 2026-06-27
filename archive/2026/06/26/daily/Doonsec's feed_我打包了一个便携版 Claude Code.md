---
title: 我打包了一个便携版 Claude Code
url: https://mp.weixin.qq.com/s/ekNU6n-zsYOGOLX_a6Tn8g
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:49:23.679147
---

# 我打包了一个便携版 Claude Code

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LjdkpgSF7Pd612t5BEgJEWFMtATTDWaGudmbPU28P11bQkRibiaSdtMZWpibR5wOjbiaCoO7YlpIKic9VwfrmvEkEpKAepC8DjHYhU83mpA1tobk/0?wx_fmt=jpeg)

# 我打包了一个便携版 Claude Code

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Windows 下批量安装Claude Code可不可行？

答案：可行

直接在 Claude Code 中提需求，要求把当前可运行环境打包成便携版。方便在其它 Windows 上运行。要求直接解压就可以运行，不需要做任何配置。

最终输出的目录结构：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PdkNRlLjmgn6BOrgewmBibfH9aGK4dfLW64jf9jqfseicehOcGbydKpnXodxibdZ69MPsibTfY1VBdSVmqic9uzEiblAAy26LBJQodiaQ/640?wx_fmt=png&from=appmsg)

便携版启动脚本：

```
#!/bin/bash# Claude Code 便携版启动脚本 (Git Bash)
# 获取脚本所在目录SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# 清理可能影响的环境变量unset ANTHROPIC_API_KEY
# 创建 ~/.local/bin 目录（claude 会检查此目录）mkdir -p "$HOME/.local/bin"
# 如果 ~/.local/bin 中没有 claude.exe，则从便携版复制if [ ! -f "$HOME/.local/bin/claude.exe" ]; then    cp "$SCRIPT_DIR/bin/claude.exe" "$HOME/.local/bin/claude.exe"    echo "✓ 已复制 claude.exe 到 $HOME/.local/bin"fi
# 设置配置目录（便携版内部）export CLAUDE_CONFIG_DIR="$SCRIPT_DIR/config"
# 禁用自动更新（便携版手动更新）export DISABLE_AUTOUPDATER=true
# 内置 API 配置export ANTHROPIC_BASE_URL="https://ark.cn-beijing.volces.com/api/coding"export ANTHROPIC_MODEL="ark-code-latest"export ANTHROPIC_AUTH_TOKEN="ark-your-key"
# 启动 Claude Code（优先使用 ~/.local/bin 的）exec "$HOME/.local/bin/claude.exe" "$@"
```

实际上主要有用的就是 config 目录，将之前的 ~/.claude 目录拷贝过去即可。我对照了一下，两个目录几乎一样。制作便携版前需要对会话和历史信息进行清理，给多人使用有信息泄露风险。

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PdBoxdMo0ibVgQByx3cnnxpoOI3XuCk7kgs6cicWXY8tnPJ1TTy7YvqbiaiaobgcUb0WzMiaK2IiaStv54Vc2kPyFk4I5qO99Z8ys6nc/640?wx_fmt=png&from=appmsg)

实际上原版 Claude Code 安装也不复杂，但给无基础的人使用还是尽量简单一点。目前主要是给内部同事用，AI agent 推广的第一步，先让大多数人用上 Claude Code。

全文完。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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