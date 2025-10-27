---
title: eliep/i3-layouts: Dynamic layouts for i3wm
url: https://buaq.net/go-149995.html
source: unSafe.sh - 不安全
date: 2023-02-19
fetch_date: 2025-10-04T07:29:15.085944
---

# eliep/i3-layouts: Dynamic layouts for i3wm

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

![](https://8aqnet.cdn.bcebos.com/8c904190362b013c6c80cf06862eb4fe.jpg)

eliep/i3-layouts: Dynamic layouts for i3wm

i3-layouts is a small program that enforces dynamic layout on i3 workspace.i3-layo
*2023-2-18 20:12:26
Author: [github.com(查看原文)](/jump-149995.htm)
阅读量:37
收藏*

---

[![test](https://github.com/eliep/i3-layouts/workflows/Test/badge.svg)](https://github.com/eliep/i3-layouts/workflows/Test/badge.svg)
[![pipy](https://github.com/eliep/i3-layouts/workflows/Publish/badge.svg)](https://github.com/eliep/i3-layouts/workflows/Publish/badge.svg)

`i3-layouts` is a small program that enforces dynamic layout on i3 workspace.

[![vstack](https://github.com/eliep/i3-layouts/raw/main/img/vstack.gif)](https://github.com/eliep/i3-layouts/blob/main/img/vstack.gif)

`i3-layouts` comes with 6 configurable layouts:

* `vstack`: one main windows with a vertical stack of windows.
* `hstack`: one main windows with an horizontal stack of windows.
* `spiral`: each new windows split the previous one, split direction alternates between
  horizontal and vertical.
* `2columns`: two vertical stacks of equally sized windows.
* `3columns`: one main windows with two vertical stacks of windows.
* `companion`: each columns is made of one main window and one smaller window.
* `autosplit`: automatically choose between vsplit/hsplit depending on the focused windows
  (inspired by [autotiling](https://github.com/nwg-piotr/autotiling)).

Parameters for each one of these layouts is detailed in the [Layout section](#layouts).

* [Installation](#installation)
  + [Requirements](#requirements)
  + [Installation with pip](#installation-with-pip)
  + [Update with pip](#update-with-pip)
* [Running](#running)
* [Configuration](#configuration)
  + [Assigning a layout to a workspace](#assigning-a-layout-to-a-workspace)
  + [Switching layout](#switching-layout)
  + [Moving windows inside the layout](#moving-windows-inside-the-layout)
  + [Swapping windows](#swapping-windows)
* [Layouts](#layouts)
  + [vstack](#vstack)
  + [hstack](#hstack)
  + [spiral](#spiral)
  + [2columns](#2columns)
  + [3columns](#3columns)
  + [companion](#companion)
  + [autosplit](#autosplit)
* [Limitations](#limitations)

## Installation

### Requirements

Before installing `i3-layouts` be sure to have the following installed on your system:

* python >= 3.7
* [xdotool](https://www.semicomplete.com/projects/xdotool/)
* [i3wm](https://i3wm.org/) or [i3-gaps](https://github.com/Airblader/i3)

### Installation with pip

To install, simply use `pip`

```
$ pip install --user i3-layouts
```

### Update with pip

To update, again use `pip`

```
$ pip install --user i3-layouts -U
```

## Running

`i3-layouts` can be started from a terminal
or better yet, launched from the i3 config file:

## Configuration

Configuration is done directly in the i3 config file (usually `$HOME/.config/i3/config`).

`i3-layouts` reads the entire config file, filter all `$i3l` variables and
keeps the associated values as configuration. Note that user defined variables can be used
within `$i3l` variables, as they will be replaced by their own value.

### Assigning a layout to a workspace

To assign a layout to a workspace, use the name of the layout as value for the `$i3l` variable,
followed by its parameters and then the targeted workspace name.

Note that parameters are optional. However, if given, they must respect the order described
in the [Layouts](#layouts) section.

**Syntax:**

```
set $i3l [vstack|hstack|spiral|3columns|2columns|companion|autosplit] <param> ... to workspace [workspace name]
```

Standard layouts from i3 can also be used:

```
set $i3l [tabbed|splitv|splith|stacking] to workspace [workspace name]
```

**Examples:**

```
set $ws1 1
...
set $i3l vstack to workspace $ws1
set $i3l hstack 0.6 up to workspace $ws2
set $i3l spiral 0.6 to workspace $ws3
set $i3l 3columns 0.66 0.5 2 left to workspace $ws4
set $i3l 2columns right to workspace $ws5
set $i3l companion 0.3 0.4 up to workspace $ws6
set $i3l autosplit to workspace $ws7
```

### Switching layout

It's also possible to dynamically switch the current workspace layout
via the provided `i3l` command with the layout name and its parameters as argument.

* If a layout name is given, and windows are already present,
  they will be rearranged to match the selected layout.
* If `none` is `i3l` first argument, `i3-layouts` will stop managing the current workspace layout.

**Syntax:**

```
i3l [vstack|hstack|spiral|3columns|2columns|companion|autosplit|none] <param> ...
```

**Examples:**

Layout can also be switched with a key binding via `i3l`, for example:

```
bindsym $mod+s exec i3l vstack 0.6
```

Use `notify-send` after the previous command to receive a quick notification of the current layout:

```
bindsym $mod+s exec i3l vstack 0.6 && notify-send 'Layout vstack'
```

### Moving windows inside the layout

[![move](https://github.com/eliep/i3-layouts/raw/main/img/move.gif)](https://github.com/eliep/i3-layouts/blob/main/img/move.gif)

By default, when moving windows, chances are their position will not match the selected layout.
To keep windows within the layout possible positions, `i3-layouts` must manage all `move` command.

So instead of configuring i3 with something like:

```
bindsym $mod+j move left
bindsym $mod+k move down
bindsym $mod+l move up
bindsym $mod+semicolon move right
```

`move` commands can be forwarded to `i3-layouts` via `i3l`:

```
bindsym $mod+j exec i3l move left
bindsym $mod+k exec i3l move down
bindsym $mod+l exec i3l move up
bindsym $mod+semicolon exec i3l move right
```

With this configuration, if a `move` command is executed on a workspace managed by `i3-layouts`,
the moved window will stay within the layout. If the workspace is not managed by `i3-layout`,
`i3-layout` will forward the `move` command to `i3`

### Swapping windows

Because `i3-layout` uses marks to keep track of container position, it must know about all
swap commands occurring within a layout.

Like `move` commands, `swap` commands can be forwarded to `i3-layouts` via `i3l`:

```
bindsym $mod+s exec i3l swap container with mark <arg>
```

Note that currently, only the swap command `with mark` is implemented
(so `swap container with id <arg>` or `swap container with con_id <arg>` will not work).

To swap the focused container with the previously focused one, a custom command is also provided:

```
bindsym $mod+p exec i3l swap container with previous
```

## Layouts

Each layout accept some specific parameters.
These parameters must be given is the order described below.

#### vstack

One main windows with a vertical stack of windows.

[![vstack](https://github.com/eliep/i3-layouts/raw/main/img/vstack.gif)](https://github.com/eliep/i3-layouts/blob/main/img/vstack.gif)

* **main window ratio** (float between `0` and `1`, default `0.5`): ratio of screen width used
  by the main window
* **secondary stack position** (`right` or `left`, default `right`): vertical stack position
  relative to the main window

### hstack

One main windows with an horizontal stack of windows.

[![hstack](https://github.com/eliep/i3-layouts/raw/main/img/hstack.gif)](https://github.com/eliep/i3-layouts/blob/main/img/hstack.gif)

* **main window ratio** (float between `0` and `1`, default `0.5`): ratio of screen height used
  by the window stack
* **secondary stack position** (`up` or `down`, default `down`): horizontal stack position
  relative to the main window

### spiral

Each new windows split the previous one, split direction alternates between
horizontal and vertical.

[![spiral](https://github.com/eliep/i3-layouts/raw/main/img/spiral.gif)](https:...