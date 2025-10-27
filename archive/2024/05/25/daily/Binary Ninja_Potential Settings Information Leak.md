---
title: Potential Settings Information Leak
url: https://binary.ninja/2024/05/24/potential-settings-infoleak.html
source: Binary Ninja
date: 2024-05-25
fetch_date: 2025-10-06T17:17:57.271655
---

# Potential Settings Information Leak

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

## Potential Settings Information Leak

* [Jordan Wiens](https://github.com/psifertex)
* 2024-05-24
* [meta](/tag/meta), [security](/tag/security)

We recently fixed an [information leak](https://docs.sidekick.binary.ninja/issues/ski-1) in our Sidekick plugin.
Specifically, a userâs API keys could be leaked when sharing a `.BNDB` database with someone else. Thankfully, this
issue did not expose user data in any way, but could have been used to gain free access to the service with another
userâs key. Additionally, this issue was discovered during internal testing and we do not have evidence it was
abused externally prior to identifying and correcting the issue.

If we have made this mistake, itâs likely other plugin authors may have as well, so we wanted to write up this post to
provide more details about the issue and what weâve changed in the API itself to mitigate it.

## Using the Settings API

The [Settings APIs](https://api.binary.ninja/binaryninja.settings-module.html) allows for setting various
[scopes](https://docs.binary.ninja/guide/settings.html). If you are making a sensitive setting in a plugin for example
(like we did in Sidekick), and you initialize the setting without ignoring the `SettingsResourceScope`, the setting will be
serialized in any created databases as described in the documentation above:

```
my_settings = Settings()
title = "My UI Plugin"
description = "Enable My UI Plugin table display."
properties = f'{{"title" : "{title}", "description" : "{description}", "type" : "boolean", "default" : true, "ignore" : ["SettingsProjectScope"]}}'
my_settings.register_group("myPlugin", "My Plugin")
my_settings.register_setting("myPlugin.enableTableView", properties)
my_bv = load("/bin/ls", options={'myPlugin.enableTableView' : True})
Settings().get_bool("myPlugin.enableTableView")
```

The correct usage of the API for sensitive values would be to include `SettingsResourceScope` in the `ignore` list of the setting:

```
properties = f'{{"title" : "{title}", "description" : "{description}", "type" : "boolean", "default" : true, "ignore" : ["SettingsProjectScope", "SettingsResourceScope"]}}'
```

Indeed, this is one of the steps weâve taken in our recently updated version of Sidekick available in the plugin
manager.

### Hidden Fields and a Mitigation

While itâs impossible to know for certain whether a setting will contain sensitive information for sure, because we do
have a âhiddenâ [property](https://api.binary.ninja/binaryninja.settings-module.html#binaryninja.settings.Settings),
we have added one new behavior in the latest dev build 4.1.5353.

Specifically, we will automatically reject any
[`register_settings`](https://api.binary.ninja/binaryninja.settings-module.html#binaryninja.settings.Settings.register_setting)
call that specifies a hidden property and does not *explicitly* specify a scope. This prevents the default behavior of
including the setting in the Resource scope, while still maintaining maximum backward compatibility with the current
behavior.

The default of including settings in the settings scope makes sense when you consider that most settings are things like
analysis information that will impact the results of the database. Without consistent analysis settings, when someone
else opens a database youâve shared with them, they might get inconsistent results from what you expect them to see.

## What About Sidekick?

Beyond just fixing the issue going forward, weâve taken the following steps to ensure we mitigate the issue as
thoroughly as possible:

1. Writing up [additional documentation](https://docs.sidekick.binary.ninja/issues/ski-1/) on the issue for Sidekick users
2. Invalidating all API keys that are used with a vulnerable version
3. Prompting users to update their plugin and API key on connection to the server
4. Creating a new feature in the Sidekick account management page to cycle an API key (should users ever accidentally
   leak their key in the future and need to change it without contacting support)
5. Emailing all impacted users

## Wrap Up

We sincerely apologize to all of our existing users who have been inconvenienced by having to update their API key.
Also, while we donât have a formal bug-bounty program, we do welcome all [security
reports](https://github.com/Vector35/binaryninja-api/blob/dev/SECURITY.md) should external users identify any issues in
either Binary Ninja itself, or any of our web properties. Additionally, we are more than willing to compensate reporters
of valid issues with licenses, swag, or even financial consideration depending on the situation.

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2025 Vector 35. All rights reserved.

Binary NinjaÂ® is a registered trademark of Vector 35.

## Contact Us

Vector 35
PO Box 971
Melbourne, FL 32902

[[email protected]](/cdn-cgi/l/email-protection#9cfef5f2fdeee5f2f5f2f6fddceaf9ffe8f3eeafa9b2fff3f1)

+1-866-983-3135

[Slack](https://slack.binary.ninja/)

## [Changelog](/changelog/)

[Software EULA](https://docs.binary.ninja/about/license.html)

[Privacy Policy](/privacy/)