---
title: Open Claude Code CLI from Raycast in a new Ghostty window
url: https://robinverton.de/til/claude-cli-raycast/
source: Robin Verton - it-security and software engineering
date: 2026-02-02
fetch_date: 2026-02-03T04:09:01.005340
---

# Open Claude Code CLI from Raycast in a new Ghostty window

[rv](/)
[blog](/blog)
[security](/security)
[TIL](/til)
[uses](/uses)

# Open Claude Code CLI from Raycast in a new Ghostty window

February 2, 2026

[ai](https://robinverton.de/tags/ai/)

[claude](https://robinverton.de/tags/claude/)

[ghostty](https://robinverton.de/tags/ghostty/)

[raycast](https://robinverton.de/tags/raycast/)

The Claude Desktop app is slow as hell and takes multiple seconds to open. I
prefer the CLI version of Claude, which is way faster. However, I also like using
Raycast for quick access to apps and commands.

To open Claude in a scratch folder in a new terminal window from Raycast, you
can use the following Raycast script command:

```
 #!/bin/bash

 # @raycast.schemaVersion 1
 # @raycast.title Claude CLI
 # @raycast.mode silent

 CLAUDE_DIR="$HOME/.claude-scratch"
 mkdir -p "$CLAUDE_DIR"

 osascript <<EOF
 tell application "Ghostty" to activate
 delay 0.1
 tell application "System Events"
     keystroke "t" using command down
     delay 0.1
     keystroke "cd $CLAUDE_DIR && claude"
     key code 36
 end tell
 EOF
```

Now add this script as a Raycast script command, and you can quickly open Claude CLI in a new
Ghostty terminal window by invoking it from Raycast.

### See Also

* ## [./ai](/blog/ai/) [ai](https://robinverton.de/tags/ai/) [software-engineering](https://robinverton.de/tags/software-engineering/)

[Mail](/cdn-cgi/l/email-protection#2f474a4343406f5d404d4641594a5d5b4041014b4a)
•
[Twitter](https://twitter.com/robinverton)
•
[Github](https://github.com/rverton)
• [Imprint](/imprint) •
robinverton.de,
2026