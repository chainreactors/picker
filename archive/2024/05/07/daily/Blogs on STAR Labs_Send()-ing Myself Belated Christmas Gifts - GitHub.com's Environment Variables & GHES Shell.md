---
title: Send()-ing Myself Belated Christmas Gifts - GitHub.com's Environment Variables & GHES Shell
url: https://starlabs.sg/blog/2024/04-sending-myself-github-com-environment-variables-and-ghes-shell/
source: Blogs on STAR Labs
date: 2024-05-07
fetch_date: 2025-10-06T17:16:59.792964
---

# Send()-ing Myself Belated Christmas Gifts - GitHub.com's Environment Variables & GHES Shell

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Send()-ing Myself Belated Christmas Gifts - GitHub.com's Environment Variables & GHES Shell

May 6, 2024 · 15 min · Ngo Wei Lin (@Creastery)

Table of Contents

* [Backstory](#backstory)
* [A Quick Primer on Ruby Reflections](#a-quick-primer-on-ruby-reflections)
* [Discovering the Vulnerability](#discovering-the-vulnerability)
* [In Search of Impact](#in-search-of-impact)
* [Triaging Candidate Methods](#triaging-candidate-methods)
* [Getting the Environment Variables](#getting-the-environment-variables)
* [The Actual Impact](#the-actual-impact)
* [Getting Remote Code Execution (RCE)](#getting-remote-code-execution-rce)
* [Exploit Conditions](#exploit-conditions)
* [Suggested Mitigations](#suggested-mitigations)
* [Detection Guidance](#detection-guidance)
* [Timeline](#timeline)
* [Closing Thoughts](#closing-thoughts)

Earlier this year, in mid-January, you might have come across [this security announcement](https://github.blog/2024-01-16-rotating-credentials-for-github-com-and-new-ghes-patches/) by GitHub.

In this article, I will unveil the shocking story of how I discovered [CVE-2024-0200](https://www.cve.org/CVERecord?id=CVE-2024-0200), a deceptively simple, one-liner vulnerability which I initially assessed to likely be of low impact, and how I turned it into one of the most impactful bugs in GitHub’s bug bounty history.

***Spoiler:** The vulnerability enabled disclosure of **all** environment variables of a production container on `GitHub.com`, including numerous access keys and secrets. Additionally, this vulnerability can be further escalated to achieve remote code execution (RCE) on GitHub Enterprise Servers (GHES), but not on `GitHub.com`. More on this later.*

## Backstory[#](#backstory)

Back in early December 2023, I was performing some research on GHES. On the day before I went on vacation, I located a potential (but likely minor) bug. Fast-forward to the day after Christmas, I finally found some time to triage and analyse this potential vulnerability. At that point, I still had zero expectations of the potential bug to be *this* impactful… until an accident happened.

## A Quick Primer on Ruby Reflections[#](#a-quick-primer-on-ruby-reflections)

Before I spill the tea, allow me to begin with a brief introduction to Ruby.

Similar to JavaScript, almost everything (e.g. booleans, strings, integers) is an `Object` in Ruby. The `Object` includes the `Kernel` module as a mixin, rendering methods in the `Kernel` module accessible by every Ruby object. Notably, it is possible to do reflection (i.e. indirect method invocation) by using `Kernel#send()` as such:

```
class HelloWorld
  def print(*args)
    puts("Hello " + args.join(' '))
  end
end

obj = HelloWorld.new()
obj.print('world') # => 'Hello World'
obj.send('print', 'world') # => 'Hello World'
```

As shown above, it is possible to dynamically invoke a method using `Kernel#send()` to perform reflection on any object.
Naturally, this makes it an obvious code sink to search for, since having ability to invoke arbitrary methods on an object can be disastrous. For example, **unsafe reflections with 2 controllable arguments** can easily lead to arbitrary code execution:

```
user_input1 = 'eval'
user_input2 = 'arbitrary Ruby code here'

obj.send(user_input1, user_input2)
# is equivalent to:
obj.send('eval', 'arbitrary Ruby code here')
# which is equivalent to:
Kernel.eval('arbitrary Ruby code here')
# which has the same effect as:
eval('arbitrary Ruby code here')
# note: because everything is an object, including the current context
```

If you have more than **2 controllable arguments**, then it is also trivial to achieve arbitrary code execution by calling `send()` repeatedly:

```
obj.send('send', 'send', 'send', 'send', 'eval', '1+1')
# will call:
obj.send('send', 'send', 'send', 'eval', '1+1')
# ...
obj.send('eval', '1+1')
# to finally call:
eval('1+1')
```

You can read more about unsafe reflections in [Phrack Issue 0x45](http://phrack.org/issues/69/12.html#:~:text=2.3.3%20Indirections) by [@joernchen](https://twitter.com/joernchen) or this [Ruby security discussion published on Seebug](https://paper.seebug.org/1951/) (in Chinese).

Interestingly enough, I did not come across any discussions on unsafe reflections with only **1 controllable argument** in `Kernel#send()` as shown below:

```
user_input = 'method_name_here'
obj.send(user_input)
```

At first glance, it seems rather difficult to escalate impact at all in this scenario. From the list of default methods inherited from `Object`, I identified the following useful methods:

```
# Disclosing filepaths:
obj.send('__dir__') # leak resolved absolute path to directory containing current file
obj.send('caller')  # return execution call stack, and may leak filepaths

# Disclosing class name
obj.send('class')

# Disclosing method names
obj.send('__callee__')
obj.send('__method__')
obj.send('matching_methods')
obj.send('methods') # Object#methods() returns list of public and protected methods
obj.send('private_methods')
obj.send('protected_methods')
obj.send('public_methods')
obj.send('singleton_methods')

# Disclosing variable names
obj.send('instance_variables')
obj.send('global_variables')
obj.send('local_variables')

# Stringify variable
obj.send('inspect') # calls to_s recursively
obj.send('to_s')    # string representation of the object

# Read from standard input
obj.send('gets')
obj.send('readline')
obj.send('readlines')

# Terminates process (please exercise caution)
obj.send('abort')
obj.send('fail')
obj.send('exit')
obj.send('exit!')
```

These methods may come in handy when attempting to gather more information on the target, especially when performing blind, unsafe reflections.

However, in the case of GitHub, this won’t be necessary since we can audit the source code of GHES, which is largely identical to the one deployed on `GitHub.com`. Now, we are ready to move on to discuss the vulnerability.

## Discovering the Vulnerability[#](#discovering-the-vulnerability)

***Note:** The source code presented below were extracted from **GitHub Enterprise Server (GHES) 3.11.0** to pinpoint the root cause of the vulnerability.*

Doing a quick search on the codebase, I found an unvalidated `Kernel#send()` call in `Organizations::Settings::RepositoryItemsComponent` found in `app/components/organizations/settings/repository_items_component.rb`:

```
...
class Organizations::Settings::RepositoryItemsComponent < ApplicationComponent
  def initialize(organization:, repositories:, selected_repositories:, current_page:, total_count:, data_url:, aria_id_prefix:, repository_identifier_key: :global_relay_id, form_id: nil)
    @organization = organization
    @repositories = repositories
    @selected_repositories = selected_repositories
    @show_next_page = current_page * Orgs::RepositoryItemsHelper::PER_PAGE < total_count
    @data_url = data_url
    @current_page = current_page
    @aria_id_prefix = aria_id_prefix
    @repository_identifier_key = repository_identifier_key # [2]
    @form_id = form_id
  end
  ...
  def identifier_for(repository)
    repository.send(@repository_identifier_key) # [1]
  end
  ...
end
```

At [1], `repository.send(@repository_identifier_key)` is invoked in the `identifier_for()` method without any prior input validation on `@repository_identifier_key` (set at [2]). This allows all methods accessible by the object (including private or protected methods, and any other methods inherited ...