---
title: Hijacking the Binary Ninja UI for Fun and Profit
url: https://buaq.net/go-149915.html
source: unSafe.sh - 不安全
date: 2023-02-18
fetch_date: 2025-10-04T07:20:18.233595
---

# Hijacking the Binary Ninja UI for Fun and Profit

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

![]()

Hijacking the Binary Ninja UI for Fun and Profit

First and foremost, when we originally implemented UI plugins, the following was not the use-cas
*2023-2-17 19:33:7
Author: [binary.ninja(查看原文)](/jump-149915.htm)
阅读量:28
收藏*

---

First and foremost, when we [originally implemented UI plugins](https://github.com/Vector35/binaryninja-api/issues/305), the following was not the use-case we had in mind. That said, [UI Plugins](https://docs.binary.ninja/dev/api.html#ui-elements) are extremely powerful, and allow you to customize Binary Ninja’s interface to your heart’s content, for fun *and* for profit!

To get started writing a UI plugin, we need to import the UI elements we’re going to use.

```
from binaryninjaui import UIActionHandler, UIAction, Menu, UIActionContext
```

We currently don’t have these elements documented in our Python API, but you can see some information in the [C++ API documentation](https://api.binary.ninja/cpp/group__uiapi.html) or the [header files in the API repository on GitHub](https://github.com/Vector35/binaryninja-api/tree/dev/ui).

## Fun

Extending the UI is relatively easy. We have dedicated APIs for doing everything from [adding custom actions to the command palette](https://api.binary.ninja/binaryninja.plugin-module.html#binaryninja.plugin.PluginCommand.register) to [adding custom widgets to the sidebar](https://github.com/Vector35/binaryninja-api/blob/dev/python/examples/hellosidebar.py). Using those APIs, you’ll be handed the appropriate contexts for the scope of your actions — `BinaryView`, `Function`, `AddressRange`, `ViewFrame`, etc.

We, however, want more. We want the context of the main view so that we can customize it. And, more than that, we need to be given the context of the main view every time “*something*” happens so we can change its behavior. What code gets passed the entire view’s context for every event? Menu options, of course! Menu options get checked to see if they’re still valid every time the cursor moves to a new location, views change, binary content gets modified, and more. When this happens, it receives a `UIActionContext`.

So, instead of [registering a toolbar menu option using the plugin APIs](https://api.binary.ninja/binaryninja.plugin-module.html#binaryninja.plugin.PluginCommand.register), we want to register a toolbar menu option manually:

```
UIAction.registerAction("Hijack UI")
UIActionHandler.globalActions().bindAction("Hijack UI", UIAction(lambda context: None, hijack_ui))
Menu.mainMenu("Tools").addAction("Hijack UI", "", 0)
```

Where the prototype for `hijack_ui` is `def hijack_ui(context: UIActionContext) -> None`.

Throw this in [your OS-specific user plugin directory](https://docs.binary.ninja/guide/plugins.html#using-plugins), and you’re nearly ready to start turning a profit.

## Profit

We can do interesting things with `UIActionContext` fields like `context`, `view`, and `widget`. But, for the purposes of this blog post, we’re going to use the `view` to customize the options in the right click menu.

```
def hijack_rightclick_menu(context: UIActionContext):
  if context is not None:
    if context.view is not None:
      view = context.view
      context_menu = view.contextMenu()
```

From here, you can add or remove options to your heart’s content:

```
def hijack_rightclick_menu(context: UIActionContext):
  if context is not None:
    if context.view is not None:
      view = context.view
      context_menu = view.contextMenu()
      for action in view.contextMenu().getActions().keys():
        if action.startswith('Plugins'):
          context_menu.removeAction(action)

      for command in PluginCommand:
        context_menu.addAction(command._name, "Plugins")

      UIAction.registerAction("Print something")
      action_handler = view.actionHandler()
      action_handler.bindAction("Print something", UIAction(lambda context: log_error("something"), lambda context: True))
```

Note that if you start getting errors like `RuntimeError: Internal C++ object X already deleted.`, this generally means that Python helpfully garbage collected your object when it went out of scope, which deleted the reference you’re now trying to use. The easiest way around this is to assign things to a variable in an outer scope (like the `view = context.view` line above) to prevent it from being destructed before you’re done with it.

Bringing this all together, here’s a theoretical plugin that could clean up the right-click context menu a bit by modifying the actions it presents:

```
from binaryninja import PluginCommand
from binaryninja.log import log_error

from binaryninjaui import UIActionHandler, UIAction, Menu, UIActionContext, HexEditor

def hijack_rightclick_menu(context: UIActionContext):
  if context is not None:
    view = context.view
    if view is not None:
      context = context.context
      context_menu = view.contextMenu()
      for action in view.contextMenu().getActions().keys():
        if action.startswith('Highlight'):
          context_menu.removeAction(action)
        elif action.startswith('Enter Comment'):
          context_menu.removeAction(action)
        elif action.startswith('Change Type'):
          context_menu.removeAction(action)
        elif action.startswith('Add Cross Reference'):
          context_menu.removeAction(action)
        elif action.startswith('Bookmarks'):
          context_menu.removeAction(action)
        elif action.startswith('Current Function Analysis'):
          context_menu.removeAction(action)
        elif action.startswith('Rename Current Function'):
          context_menu.removeAction(action)
        elif action.startswith('Plugins'):
          context_menu.removeAction(action)

        if context is not None:
          view_frame = context.getCurrentViewFrame()
          if view_frame is not None:
            if not view_frame.getCurrentView().startswith('Hex'):
              if action.startswith('Cut'):
                context_menu.removeAction(action)
              elif action.startswith('Paste'):
                context_menu.removeAction(action)
            else:
              if action.startswith('Make Function at This Address'):
                context_menu.removeAction(action)
              elif action.startswith('Patch'):
                context_menu.removeAction(action)

      # Unfolds plugins
      for command in PluginCommand:
        context_menu.addAction(command._name, "Plugins")

# Register a junk action that'll be called 'every time something happens'.
# We register this way instead of PluginCommand.register because we want the UI
# context this gives us, as well as being able to tuck the command out of the
# way (e.g. not in the Plugins subfolder/area).
UIAction.registerAction("Hijack Rightclick Menu")
UIActionHandler.globalActions().bindAction("Hijack Rightclick Menu", UIAction(lambda context: None, hijack_rightclick_menu))
Menu.mainMenu("Tools").addAction("Hijack Rightclick Menu", "", 0)
```

UI Plugins are super powerful, and allow you to customize just about anything. With a little creativity (and a little `print(dir(object.parent))`), you too can hijack parts of the Binary Ninja UI for fun and profit!

文章来源: https://binary.ninja/2023/02/17/hacking-the-binary-ninja-ui-for-fun-and-profit.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)