---
title: Hijacking the Binary Ninja UI for Fun and Profit
url: https://binary.ninja/2023/02/17/hacking-the-binary-ninja-ui-for-fun-and-profit.html
source: Binary Ninja
date: 2023-02-18
fetch_date: 2025-10-04T07:22:54.397906
---

# Hijacking the Binary Ninja UI for Fun and Profit

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Hijacking the Binary Ninja UI for Fun and Profit

* [Kyle Martin](https://github.com/ElykDeer)
* 2023-02-17
* [meta](/tag/meta)

First and foremost, when we [originally implemented UI plugins](https://github.com/Vector35/binaryninja-api/issues/305), the following was not the use-case we had in mind. That said, [UI Plugins](https://docs.binary.ninja/dev/api.html#ui-elements) are extremely powerful, and allow you to customize Binary Ninjaâs interface to your heartâs content, for fun *and* for profit!

To get started writing a UI plugin, we need to import the UI elements weâre going to use.

```
from binaryninjaui import UIActionHandler, UIAction, Menu, UIActionContext
```

We currently donât have these elements documented in our Python API, but you can see some information in the [C++ API documentation](https://api.binary.ninja/cpp/group__uiapi.html) or the [header files in the API repository on GitHub](https://github.com/Vector35/binaryninja-api/tree/dev/ui).

## Fun

Extending the UI is relatively easy. We have dedicated APIs for doing everything from [adding custom actions to the command palette](https://api.binary.ninja/binaryninja.plugin-module.html#binaryninja.plugin.PluginCommand.register) to [adding custom widgets to the sidebar](https://github.com/Vector35/binaryninja-api/blob/dev/python/examples/hellosidebar.py). Using those APIs, youâll be handed the appropriate contexts for the scope of your actions â `BinaryView`, `Function`, `AddressRange`, `ViewFrame`, etc.

We, however, want more. We want the context of the main view so that we can customize it. And, more than that, we need to be given the context of the main view every time â*something*â happens so we can change its behavior. What code gets passed the entire viewâs context for every event? Menu options, of course! Menu options get checked to see if theyâre still valid every time the cursor moves to a new location, views change, binary content gets modified, and more. When this happens, it receives a `UIActionContext`.

So, instead of [registering a toolbar menu option using the plugin APIs](https://api.binary.ninja/binaryninja.plugin-module.html#binaryninja.plugin.PluginCommand.register), we want to register a toolbar menu option manually:

```
UIAction.registerAction("Hijack UI")
UIActionHandler.globalActions().bindAction("Hijack UI", UIAction(lambda context: None, hijack_ui))
Menu.mainMenu("Plugins").addAction("Hijack UI", "", 0)
```

Where the prototype for `hijack_ui` is `def hijack_ui(context: UIActionContext) -> None`.

Throw this in [your OS-specific user plugin directory](https://docs.binary.ninja/guide/plugins.html#using-plugins), and youâre nearly ready to start turning a profit.

## Profit

We can do interesting things with `UIActionContext` fields like `context`, `view`, and `widget`. But, for the purposes of this blog post, weâre going to use the `view` to customize the options in the right click menu.

```
def hijack_rightclick_menu(context: UIActionContext):
  if context is not None:
    if context.view is not None:
      view = context.view
      context_menu = view.contextMenu()
```

From here, you can add or remove options to your heartâs content:

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

Note that if you start getting errors like `RuntimeError: Internal C++ object X already deleted.`, this generally means that Python helpfully garbage collected your object when it went out of scope, which deleted the reference youâre now trying to use. The easiest way around this is to assign things to a variable in an outer scope (like the `view = context.view` line above) to prevent it from being destructed before youâre done with it.

Bringing this all together, hereâs a theoretical plugin that could clean up the right-click context menu a bit by modifying the actions it presents:

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
Menu.mainMenu("Plugins").addAction("Hijack Rightclick Menu", "", 0)
```

UI Plugins are super powerful, and allow you to customize just about anything. With a little creativity (and a little `print(dir(object.parent))`), you too can hijack parts of the Binary Ninja UI for fun and profit!

## About Us

Binary Ninja is brought to you by Vector 35, a group of hacke...