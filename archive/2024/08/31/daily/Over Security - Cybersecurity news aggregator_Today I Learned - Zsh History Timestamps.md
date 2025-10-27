---
title: Today I Learned - Zsh History Timestamps
url: https://dfir.ch/posts/today_i_learned_zsh_timestamps/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:08:08.818617
---

# Today I Learned - Zsh History Timestamps

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Today I Learned - Zsh History Timestamps

7 May 2024

**Table of Contents**

* [Zsh Timestamps](#zsh-timestamps)
* [man page](#man-page)

## Zsh Timestamps

In Zsh, which serves as the default shell for Kali, Gentoo, and macOS (replacing Bash in macOS Catalina), among others, the shell session retains the command history with timestamps in memory. Throughout the session, each executed command is logged in the history along with a timestamp denoting its execution time.

To view the command history on a live system, we can execute one of the following commands, which not only display the history but also include the timestamps adjacent to the commands:

* fc -lf
* fc âli 100

Here is a snippet from my machine:

![Different timestamps](/images/zsh_timestamps/accureate_timestamps.png "Different timestampst")

Figure 1: Different timestamps

**This functionality applies only within the current session and remains effective until the system is rebooted or the session is closed.** Upon rebooting or closing the shell session, the timestamps of previous commands will be reset to the same date (in my limited testing, the timestamp resembled the date and time the session was opened, Figure 2). This feature is valuable in Incident Response scenarios, mainly when the default shell is Zsh instead of the widely used Bash.

Figure 2 also depicts my history file, but the timestamp is the same this time.

![Same timestamps](/images/zsh_timestamps/same_timestamp.png "Same timestampst")

Figure 2: Same timestamps

These commands (without timestamps) are extracted from the history file. Similar to the .bash\_history file, the Zsh history file is located within ~/.zsh\_history. If you want to do your IR team a favor: Configure the HISTTIMEFORMAT variable to include the date and the time of the executed command - and make the change permanent within the Zsh or bash profile file. Thank you 🙏

## man page

fc is a Zsh built-in command. Following is an excerpt from zshbuiltins [man page](https://linux.die.net/man/1/zshbuiltins):

> * -d prints timestamps for each command
> * -f prints full time-date stamps in the US `MM/DD/YY hh:mm’ format
> * -E prints full time-date stamps in the European `dd.mm.yyyy hh:mm’ format
> * -i prints full time-date stamps in ISO8601 `yyyy-mm-dd hh:mm’ format
> * -D prints elapsed times; may be combined with one of the options above.

---

*What I learned today: Short blog posts about novel information for me.*

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).