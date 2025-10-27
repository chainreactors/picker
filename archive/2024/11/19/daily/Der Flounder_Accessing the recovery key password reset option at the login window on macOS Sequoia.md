---
title: Accessing the recovery key password reset option at the login window on macOS Sequoia
url: https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/
source: Der Flounder
date: 2024-11-19
fetch_date: 2025-10-06T19:15:59.896718
---

# Accessing the recovery key password reset option at the login window on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [FileVault 2](https://derflounder.wordpress.com/category/filevault-2/), [macOS](https://derflounder.wordpress.com/category/macos/) > Accessing the recovery key password reset option at the login window on macOS Sequoia

## Accessing the recovery key password reset option at the login window on macOS Sequoia

November 18, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

If the following situation occurs:

1. You forgot the password to the local account you use to log into your Mac.
2. You have FileVault enabled.
3. You have the [FileVault recovery key](https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac) available.

You can use the FileVault recovery key to authenticate changing your local account to use a new password. Apple has documentation on how to do this available here:

<https://support.apple.com/102633> (please see the **Reset it using your recovery key** instructions)

However, it looks like Apple made a change at the login window for macOS Sequoia. Apple’s instructions reference clicking on a **( ? )** symbol, which doesn’t appear in my testing on Apple Silicon Macs. Without that, how do you access the recovery key entry blank to enter the recovery key?

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-18-at-4.20.png?w=595 "Screenshot 2024-11-18 at 4.20.png")

In the absence of the **( ? )** symbol appearing at the login window, you should be able to use the following keyboard shortcut to get the recovery key entry blank:

**Shift+Option+Return**

![Apple keyboard keys highlighted.](https://derflounder.wordpress.com/wp-content/uploads/2024/11/apple_keyboard_keys_highlighted.png?w=595 "apple_keyboard_keys_highlighted.png")

Clicking that combination of keyboard keys on an Apple Silicon Mac should cause the recovery key entry blank to appear at the login screen.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-18-at-4.20-1.png?w=595 "Screenshot 2024-11-18 at 4.20.png")

**Note:** I was not able to verify that this also works on Intel Macs, so please let me know in the comments if Intel Macs have different behavior.

Here’s how the login window should appear when you enter the keyboard shortcut in this scenario:

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [FileVault 2](https://derflounder.wordpress.com/category/filevault-2/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (11)
[Leave a comment](#respond)

1. ![Franck Sartori's avatar](https://1.gravatar.com/avatar/73d271aaa2fa683a1a0b90af770d16a09617010c2e2da611e03a73da0c198304?s=32&d=identicon&r=G)

   Franck Sartori

   November 18, 2024 at 11:58 pm

   [Reply](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?replytocom=72566#respond)

   Hi. According to this article :

   <https://support.apple.com/en-gb/guide/deployment/dep0a2cb7686/web>

   On a Mac with Apple silicon using macOS 12.0.1 or later, press Option-Shift-Return to reveal the entry field for the PRK, then press Return (or click the arrow).

   So as far as I know, Apple silicon only.

   Franck Sartori
2. ![Jako Verstraate's avatar](https://0.gravatar.com/avatar/c4b577bd4a02df25e5658eb20a6c2b2c78f6d3846a03ffcc4d20990aed556d54?s=32&d=identicon&r=G)

   [Jako Verstraate](http://jverstraate.wordpress.com)

   November 22, 2024 at 3:42 pm

   [Reply](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?replytocom=72570#respond)

   Hi, I just checked on my Intel MacBook Air. I still see the ? next to my account. Unfortunately I cannot add a picture to this comment

   * ![aarondavidpolley's avatar](https://2.gravatar.com/avatar/8c9dee801f12862bd578f48bcb3e5d0e4e835087236a3d9d0de5a464fa93929b?s=32&d=identicon&r=G)

     [aarondavidpolley](https://www.aarondavidpolley.com)

     November 24, 2024 at 9:53 am

     [Reply](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?replytocom=72574#respond)

     The login windows on Apple Silicon and Intel are technically different so this makes sense.
3. ![Eddie's avatar](https://2.gravatar.com/avatar/2e7bc86c3f0b91d6e6fbb0bb935a59c9081fd3d1910a6389a8c8882b0c520e8e?s=32&d=identicon&r=G)

   Eddie

   December 4, 2024 at 7:13 pm

   [Reply](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?replytocom=72584#respond)

   In my quick test, I went straight back to to login screen after entering the recovery key on macOS Sonoma. Curious to know if anyone had better luck.
4. ![test02's avatar](https://2.gravatar.com/avatar/82814c05e88f52c0bf90782b9d0b69913f5a826b9b95494a777f2916b6a53786?s=32&d=identicon&r=G)

   test02

   December 27, 2024 at 6:29 am

   [Reply](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?replytocom=72629#respond)

   Same thing I went back to the login screen right after I typed the recovery key in macOS Sonya in the test. Can’t I apply the settings?
5. ![test02's avatar](https://2.gravatar.com/avatar/82814c05e88f52c0bf90782b9d0b69913f5a826b9b95494a777f2916b6a53786?s=32&d=identicon&r=G)

   test02

   December 27, 2024 at 6:32 am

   [Reply](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/?replytocom=72630#respond)

   I will revise my comments.
   It’s not Sonoma, it’s Sequoia
6. ![test02's avatar](https://2.gravatar.com/avatar/82814c05e88f52c0bf90782b9d0b69913f5a826b9b95494a777f2916b6a53786?s=32&d=identicon&r=G)

   test02

   December 2...