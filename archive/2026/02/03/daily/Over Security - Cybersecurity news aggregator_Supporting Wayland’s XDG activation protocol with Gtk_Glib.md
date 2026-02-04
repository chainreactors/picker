---
title: Supporting Wayland’s XDG activation protocol with Gtk/Glib
url: https://palant.info/2026/02/03/supporting-waylands-xdg-activation-protocol-with-gtk/glib/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-03
fetch_date: 2026-02-04T04:08:03.540233
---

# Supporting Wayland’s XDG activation protocol with Gtk/Glib

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Supporting Waylandâs XDG activation protocol with Gtk/Glib

2026-02-03
 [Linux](/categories/linux/)
 4 mins
 [0 comments](/2026/02/03/supporting-waylands-xdg-activation-protocol-with-gtk/glib/#comments)

One of the biggest sore points with Wayland is its focus stealing protection. The idea is good: an application should not be able to bring itself into focus at an unexpected time, only when the currently active application allows it. Support is still lacking however, which might also be due to Gtk/Glib implementing the required XDG activation protocol but not really documenting it. It took me a bit of time to figure this out without any public information, this article will hopefully make things easier for other people.

#### Contents

* [How the XDG activation protocol works](#how-the-xdg-activation-protocol-works)
* [State of implementation in Gtk/Glib](#state-of-implementation-in-gtk-glib)
* [Starting applications via Gio.AppInfo](#starting-applications-via-gio-appinfo)
* [Starting applications by other means](#starting-applications-by-other-means)

## How the XDG activation protocol works

The main idea behind the XDG activation protocol is that focus transfer from one application to another requires consent. With X11 a file manager could just launch the browser for an HTML file and the browser would immediately take focus, even if that browser was already running. With Wayland the file manager has to indicate that the browser is *allowed* to take focus.

It does that by giving the browser its XDG activation token, typically via `XDG_ACTIVATION_TOKEN` environment variable. The browser can then use that activation token to prove consent and take focus. For this to work the protocol has to be supported on both ends: the file manager must know how to retrieve an activation token and pass it on via `XDG_ACTIVATION_TOKEN` environment variable, and the browser has to know how to use that token.

## State of implementation in Gtk/Glib

The receiving side has been implemented in Gtk with [merge request 7118](https://gitlab.gnome.org/GNOME/gtk/-/merge_requests/7118) and is available starting with Gtk 4.14.6 and 4.15.1. This is the unproblematic part: it is handled automatically and doesnât require the application developer to change anything.

The sending side has been implemented in Gtk with [merge request 3502](https://gitlab.gnome.org/GNOME/gtk/-/merge_requests/3502) and Glib with [merge request 3090](https://gitlab.gnome.org/GNOME/glib/-/merge_requests/3090), so it is available starting with Gtk 4.10.0 and Glib 2.75.1. This is the part which might require some changes to the application â changes that I couldnât find documented anywhere.

## Starting applications via Gio.AppInfo

When a Gtk-based file manager wants to open an HTML file, this usually involves [Gio.AppInfo](https://docs.gtk.org/gio/iface.AppInfo.html) and [g\_app\_info\_launch](https://docs.gtk.org/gio/method.AppInfo.launch.html) or similar:

```
GAppInfo* app_info = g_app_info_get_default_for_type("text/html", TRUE);

GList *list = NULL;
list = g_list_append(list, "https://example.com/");

GdkDisplay *display = gdk_display_get_default();
GdkAppLaunchContext* context = (display ?
  gdk_display_get_app_launch_context(display) :
  NULL);

g_app_info_launch_uris(app_info, list, G_APP_LAUNCH_CONTEXT(context), NULL);
g_list_free(list);
```

This should normally transfer focus to the browser automatically. That app launch context parameter is important however, you cannot omit it. Also, this will only work if the desktop file corresponding to the `AppInfo` has the [StartupNotify key](https://specifications.freedesktop.org/desktop-entry/1.2/recognized-keys.html#key-startupnotify) set â the Gtk developers decided to merge the handling of X11 startup notifications and XDG activations.

## Starting applications by other means

But what if you are using something like [execve function](https://man7.org/linux/man-pages/man2/execve.2.html) to start applications? You can still set `XDG_ACTIVATION_TOKEN` environment variable manually. Itâs important to know however that the token has to be retrieved via [g\_app\_launch\_context\_get\_startup\_notify\_id](https://docs.gtk.org/gio/method.AppLaunchContext.get_startup_notify_id.html) (please pardon my C):

```
char** extend_env(char** env, char* value)
{
  int env_size = 0;
  while (env[env_size])
    env_size++;

  char **new_env = malloc((env_size + 2) * sizeof(char*));
  memcpy(new_env, env, env_size * sizeof(char*));
  new_env[env_size++] = value;
  new_env[env_size++] = NULL;
  return new_env;
}

char *argv[] = {"/usr/bin/firefox", "https://example.com/", NULL};
char *default_env[] = {NULL};
char **env = default_env;
bool should_free_env = FALSE;

GdkDisplay *display = gdk_display_get_default();
if (display)
{
  GdkAppLaunchContext* context = gdk_display_get_app_launch_context(display);
  env = g_app_launch_context_get_environment(G_APP_LAUNCH_CONTEXT(context));

  char* sn_id = g_app_launch_context_get_startup_notify_id(
    G_APP_LAUNCH_CONTEXT(context), NULL, NULL);
  if (sn_id)
  {
    char token_var[256];
    snprintf(token_var, sizeof(token_var), "XDG_ACTIVATION_TOKEN=%s", sn_id);
    env = extend_env(env, token_var);
    should_free_env = TRUE;
  }
}

if (!fork())
  execve(argv[0], argv, env);

if (should_free_env)
  free(env);
```

As before, itâs worth noting that Gtk developers decided to merge the handling of X11 startup notifications and XDG activations, hence the function name to retrieve the token. The last two parameters of `g_app_launch_context_get_startup_notify_id` are unused for Wayland, these are only relevant for X11 startup notifications. *If* you pass in an `AppInfo` instance here you might actually get an X11 notification ID back that you should write into the `DESKTOP_STARTUP_ID` environment variable. However, if you have an `AppInfo` instance it should be easier to use one of its launch functions as described above, these will do it automatically.

Share on:

#### Comments

There are currently no comments on this article.

#### Leave a comment

Name \*

Email

Only if you want to be notified about my reply.

Website

Message \*
You can use [Markdown syntax](https://www.markdownguide.org/basic-syntax/) here.

By submitting your comment, you agree to your comment being published here under the terms of the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
Submit

[Impressum](/impressum/)
[Privacy Policy](/privacy/)

[![Creative Commons Attribution-ShareAlike 4.0 International License](/icons/cc-by-sa.477d847f9c6c2086d518f53033712141.svg)](http://creativecommons.org/licenses/by-sa/4.0/)
Content under [CC BY-SA 4.0 license](http://creativecommons.org/licenses/by-sa/4.0/)
Powered by [Hugo](https://github.com/gohugoio/hugo) |
Theme is [MemE](https://github.com/reuixiy/hugo-theme-meme)