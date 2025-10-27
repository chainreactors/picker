---
title: crusj/bookmarks.nvim: Remember file locations and sort by time and frequency.
url: https://buaq.net/go-130893.html
source: unSafe.sh - 不安全
date: 2022-10-15
fetch_date: 2025-10-03T19:55:03.717129
---

# crusj/bookmarks.nvim: Remember file locations and sort by time and frequency.

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

![](https://8aqnet.cdn.bcebos.com/99e4e33c19f51492913be08e50743a8d.jpg)

crusj/bookmarks.nvim: Remember file locations and sort by time and frequency.

Remember file locations and sort by time and frequency.DescriptionThis plugin is use
*2022-10-14 19:6:11
Author: [github.com(查看原文)](/jump-130893.htm)
阅读量:38
收藏*

---

Remember file locations and sort by time and frequency.

## Description

This plugin is used to mark any position of the file and jump to it. It can add notes when marking and persist the mark to the file when nvim exits for the next load.

Each time you jump from a bookmark, the update time of the current bookmark will be updated and the usage frequency will be increased by one. You can sort bookmarks by time or frequency when browsing the bookmark list.

The data file is based on the **cwd** of each project for separate storage.

Support switching between multiple sessions.

Show virt text at the end of bookmarked lines.

The storage location is under`echo stdpath("data")`, mac is `~/.local/share/nvim/bookmarks/`.

The storage data is lua code and load with `dofile`:

```
require("bookmarks.list").load{
    filename = '/Users/crusj/Project/bookmarks.nvim/README.md',
    description = 'readme',
    fre = 3,
    id = '429b65925c650553dfcc8576231837a2',
    line = 2,
    updated_at = 1651588531,
}
require("bookmarks.list").load{
    filename = '/Users/crusj/Project/bookmarks.nvim/lua/bookmarks/config.lua',
    description = 'keymap',
    fre = 11,
    id = 'a22afa41979db45c6a8215cb7df6304f',
    line = 6,
    updated_at = 1651588572,
}
require("bookmarks.list").load{
    filename = '/Users/crusj/Project/bookmarks.nvim/lua/bookmarks/event.lua',
    description = 'add keymap',
    fre = 5,
    id = 'a2e79c4b86b533f43fe3aa5a545a5073',
    line = 10,
    updated_at = 1651580490,
}
```

## screenshots

### bookmarks list

[![](https://github.com/crusj/bookmarks.nvim/raw/main/screenshots/shot1.png)](https://github.com/crusj/bookmarks.nvim/blob/main/screenshots/shot1.png)

## Install

### Requirment

* **Neovim >= 0.7**

**packer**

```
{
	'crusj/bookmarks.nvim',
	branch = 'main',
	requires = { 'kyazdani42/nvim-web-devicons' }
}
```

### Start

```
require("bookmarks").setup()
```

## Usage

### Default config

```
require("bookmarks").setup({
	keymap = {
		toggle = "<tab><tab>", -- Toggle bookmarks
		add = "\\z", -- Add bookmarks
		jump = "<CR>", -- Jump from bookmarks
		delete = "dd", -- Delete bookmarks
		order = "<space><space>", -- Order bookmarks by frequency or updated_time
		delete_on_virt = "\\dd", -- Delete bookmark at virt text line
	},
    width = 0.8, -- Bookmarks window width:  (0, 1]
    height = 0.6, -- Bookmarks window height: (0, 1]
    preview_ratio = 0.4, -- Bookmarks preview window ratio (0, 1]
    preview_ext_enable = false, -- If true, preview buf will add file ext, preview window may be highlighed(treesitter), but may be slower.
    fix_enable = true, -- If true, when saving the current file, if the bookmark line number of the current file changes, try to fix it.
    hl_cursorline = "guibg=Gray guifg=White" -- hl bookmarsk window cursorline.

    virt_text = "💫" , -- Show virt text at the end of bookmarked lines
    virt_pattern = { "*.go", "*.lua", "*.sh", "*.php", "*.rust" } -- Show virt text only on matched pattern
})
```

## TODO

* Fix bookmarks when file changed
* Categorize

文章来源: https://github.com/crusj/bookmarks.nvim
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)