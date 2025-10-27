---
title: nyoom-engineering/oxocarbon.nvim: A dark and light Neovim theme written in fennel, inspired by IBM Carbon.
url: https://buaq.net/go-139473.html
source: unSafe.sh - 不安全
date: 2022-12-12
fetch_date: 2025-10-04T01:14:39.661965
---

# nyoom-engineering/oxocarbon.nvim: A dark and light Neovim theme written in fennel, inspired by IBM Carbon.

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/fb78c3e0aad1e165c69555c427def292.jpg)

nyoom-engineering/oxocarbon.nvim: A dark and light Neovim theme written in fennel, inspired by IBM Carbon.

Note: The old rust version can be found on the rust branch of this repositoryOxocarbo
*2022-12-11 00:2:43
Author: [github.com(查看原文)](/jump-139473.htm)
阅读量:75
收藏*

---

**Note:** The old rust version can be found on the `rust` branch of this repository

**Oxocarbon is looking for ports!** If you're a user of another editor or tool, join our discord to learn more about porting oxocarbon to other applications. <https://discord.gg/5R5DvQs9>

A dark and light Neovim theme written in fennel, inspired by [IBM Carbon](https://carbondesignsystem.com/guidelines/color/overview/#themes). This is the reference implementation of the oxocarbon theme.

The color palette expands on Nyoom's unique aesthetic and represents a contemporary and ever-changing IBM. Balancing mankind and machine, the colors are harmonious with nature, yet chosen for their luminous quality in the digital world. The oxocarbon color palette is a subset of the broader IBM palette.

The colorscheme is centered around a vibrant set of blues, combined with an industrial set of grays. The full palette extends from the blue family to the edges of the blue spectrum—even the reds contain a hint of blue.

The resulting palette is a set of colors that portrays a singular IBM. Of the world and digital. Useful and judicious. Having multiple gray families gives each design the opportunity for nuance and meaningful moments of color. Each experience should be dominated by the grays and the core colors of black, white, and the blue family, allowing the other color families to have vibrancy and provide purpose.

[![merged](https://user-images.githubusercontent.com/71196912/206819503-736cbede-fdf2-4be3-baaa-d640c8498abf.png)](https://user-images.githubusercontent.com/71196912/206819503-736cbede-fdf2-4be3-baaa-d640c8498abf.png)

[![image](https://user-images.githubusercontent.com/71196912/181996667-f1bf7ab0-eba2-4f80-b914-b5f48f51a03e.png)](https://user-images.githubusercontent.com/71196912/181996667-f1bf7ab0-eba2-4f80-b914-b5f48f51a03e.png)

## Features

* Support for popular plugins, such as Lsp, Treesitter, and Semantic Highlighting
* Fast and Featureful. Supports all the highlights you'll ever need without making a dent on startuptime
* Uses `Termguicolors` but its compatible with 16-color terminals as well

### Plugin support

The colorscheme explicitly adds highlights for the following plugins:

* Vim Diagnostics
* Vim LSP
* Nvim-Treesitter
* Telescope
* Nvim-Notify
* Nvim-Cmp
* NvimTree
* Neogit
* Gitsigns
* Hydra

And many others should "just work!" If you have a plugin that needs explicit highlights, feel free to open an issue or PR and I would be happy to add them.

## Install

The colorscheme requires the latest stable or nightly neovim (> `v0.7.0`)

### Packer.nvim

```
use {'nyoom-engineering/oxocarbon.nvim'}
```

### Usage

For neovim nightly users:

```
vim.opt.background = "dark" -- set this to dark or light
vim.cmd.colorscheme "oxocarbon"
```

For neovim stable users:

```
vim.opt.background = "dark" -- set this to dark or light
vim.cmd("colorscheme oxocarbon")
```

For nyoom.nvim users:
Nyoom comes bundled with a version of oxocarbon. Enable the `ui.nyoom` module

## License

The project is licensed under the MIT license

文章来源: https://github.com/nyoom-engineering/oxocarbon.nvim
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)