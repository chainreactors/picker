---
title: I Built a Claude Code Context Modal Inside of Neovim
url: https://danielmiessler.com/blog/neovim-claude-ai-plugin
source: Daniel Miessler
date: 2025-07-27
fetch_date: 2025-10-06T23:27:06.172640
---

# I Built a Claude Code Context Modal Inside of Neovim

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# I Built a Claude Code Context Modal Inside of Neovim

Sometimes I just wish I had AI right at this moment, right with this text

July 26, 2025

[#tutorial](/archives/?tag=tutorial) [#ai](/archives/?tag=ai) [#productivity](/archives/?tag=productivity)

[![Kai Neovim AI Assistant](/images/neovim-claude-ai-kai-update.png)](/images/neovim-claude-ai-kai-update.png)

Kai: AI-powered coding in Neovim (click for full size)

I use LazyVim, btw. lol

I've been using AI to help with coding for a while now, but going back and forth between my code and AI was getting tedious—even with a highly optimized setup. So I integrated my Digital Assistant, Kai, directly into Neovim.

## The Problem [​](#the-problem)

When working with AI for code editing, you typically want one of these actions:

* **Replace** selected code with an improved version
* **Insert** new code based on context
* **Display** information without modifying anything

It's not perfect but I'm getting there.

Most AI integrations make you tell them exactly what to do. Kai somewhat figures it out from how you ask.

## How It Works [​](#how-it-works)

This entire thing is based on a capability in Claude Code that is **massively** underdiscussed. I just think of it as command-line mode.

bash

```
claude -p
```

1

* You can pipe into this thing
* You could give it a string afterwards and it will just go and execute
* You can even control how it uses different contexts and such.

 Seriously, check the [Claude Code SDK docs](https://docs.anthropic.com/en/docs/claude-code/sdk) It's ridiculous.

bash

```
claude -p "What's the weather like in San Francisco right now?"
```

1

Anyway, that's what's going on under the hood. It's this command-line version of Claude Code that we're actually calling with this plug-in.

### Structure [​](#structure)

The plugin has two main pieces:

1. **Lua plugin** (`kai-neovim.lua`) - Handles Neovim integration, visual selections, and buffer management
2. **Shell script** (`kai-neovim.sh`) - Processes context and communicates with the AI backend

The shell script reads CLAUDE/AGENT.md files for project-specific context

### Smart Context Handling [​](#smart-context-handling)

[![Kai Progress Window](/images/Screen-Shot-2013-09-12-at-9.24.54-PM.png)](/images/Screenshot%202025-07-26%20at%2017.50.27.png)

Kai's enhanced progress window showing detailed processing phases

The plugin always sends the entire buffer as context, but intelligently focuses on:

* **Selected text** when you're in visual mode
* **Cursor position** when you're in normal mode

This approach provides comprehensive context while enabling precise, targeted modifications based on your current selection or cursor position.

Still working on polishing it.

### Intelligent Action Detection [​](#intelligent-action-detection)

The plugin lets you basically tell it anything, and it tries to work it out. Here are some examples.

* "Replace with X" → Replaces selection
* "Add a comment explaining" → Inserts after selection
* "What does this do?" → Shows analysis in a popup
* "Insert an appropriate image here." → Creates a custom image and inserts it at that location

* "Fix the error" → Replaces with corrected code

This is just completely insane. We can just send arbitrary things and have it kind of figure it out. Basically, command-line interaction with AI. And within your text editor.

## The Code [​](#the-code)

This is the basic code for it, but keep in mind it's a work in progress. It might be total garbage. And yes, I had Kai help me build it for sure.

### Main Plugin Code [​](#main-plugin-code)

Save this as `~/.config/nvim/lua/kai-neovim.lua`:

lua

```
local M = {}

-- Function to get visual selection
local function get_visual_selection()
  -- Get the visual selection marks
  local _, start_row, start_col, _ = unpack(vim.fn.getpos("'<"))
  local _, end_row, end_col, _ = unpack(vim.fn.getpos("'>"))

  -- Get the lines
  local lines = vim.api.nvim_buf_get_lines(0, start_row - 1, end_row, false)

  if #lines == 0 then
    return ""
  end

  -- Handle single line selection
  if #lines == 1 then
    lines[1] = string.sub(lines[1], start_col, end_col)
  else
    -- Multi-line selection
    lines[1] = string.sub(lines[1], start_col)
    if end_col > 0 then
      lines[#lines] = string.sub(lines[#lines], 1, end_col)
    end
  end

  return table.concat(lines, "\n")
end

-- Function to escape special characters for shell
local function shell_escape(str)
  return "'" .. str:gsub("'", "'\"'\"'") .. "'"
end

-- Main function to handle Kai Neovim integration
function M.kai_enhance()
  -- Set up subtle blue highlight for the input prompt
  vim.cmd('highlight KaiPrompt guifg=#e0e0e0 guibg=#1a1a2e')

  -- Get the prompt from user with custom highlighting
  vim.cmd('echohl KaiPrompt')
  local prompt = vim.fn.input("🤖 Kai: ")
  vim.cmd('echohl None')

  if prompt == "" then
    print("No instruction provided.")
    return
  end

  -- Check if we're in visual mode
  local mode = vim.fn.mode()
  local is_visual = mode == 'v' or mode == 'V' or mode == ''

  -- Get selection if in visual mode, empty string otherwise
  local selection = ""
  if is_visual then
    selection = get_visual_selection()
  end

  -- Get current file path
  local filepath = vim.fn.expand('%:p')

  -- Get cursor position
  local cursor_row, cursor_col = unpack(vim.api.nvim_win_get_cursor(0))

  -- Get entire buffer content
  local buffer_content = table.concat(vim.api.nvim_buf_get_lines(0, 0, -1, false), "\n")

  -- Create a temporary file for the context
  local context_file = os.tmpname()
  local f = io.open(context_file, "w")
  f:write("CURRENT FILE: " .. filepath .. "\n\n")

  -- Always send the entire buffer
  f:write("FULL BUFFER CONTENT:\n" .. buffer_content .. "\n\n")

  -- Add cursor position
  f:write("CURSOR POSITION: Line " .. cursor_row .. ", Column " .. cursor_col .. "\n\n")

  if is_visual then
    -- Include selection information when text is selected
    local _, start_row, start_col, _ = unpack(vim.fn.getpos("'<"))
    local _, end_row, end_col, _ = unpack(vim.fn.getpos("'>"))

    f:write("SELECTED TEXT (Lines " .. start_row .. "-" .. end_row .. "):\n" .. selection .. "\n\n")
    f:write("MODE: User has selected specific text. Focus on this selection within the context of the entire buffer.\n\n")
  else
    -- When no selection, note cursor position
    f:write("MODE: No selection. User's cursor is at line " .. cursor_row .. ". Make targeted changes based on cursor location unless instructed otherwise.\n\n")
  end

  f:write("INSTRUCTION: " .. prompt .. "\n")
  f:close()

  -- Call Kai script
  local cmd = string.format(
    "~/.config/nvim/scripts/kai-neovim.sh %s %s",
    shell_escape(context_file),
    shell_escape(prompt)
  )

  -- Create progress notification (simplified for blog post)
  print("🤖 Processing with Kai...")

  -- Execute command
  local output = vim.fn.system(cmd)

  -- Clean up temp file
  os.remove(context_file)

  -- Parse the action and content from the response
  local lines = vim.split(output, '\n', { plain = true })
  local action = lines[1]
  local content_lines = {}
  for i = 2, #lines do
    if lines[i] ~= "" or i < #lines then
      table.insert(content_lines, lines[i])
    end
  end
  local content = table.concat(content_lines, '\n')

  -- Remove any trailing newline
  content = content:gsub('\n$', '')

  -- Handle different actions
  if action == "[ACTION:DISPLAY]" then
    -- Create a floating window to display the analysis
    local display_buf = vim.api.nvim_create_buf(false, true)
    local display_lines = vim.split(content, '\n', { plain = true })

    -- Calculate window dimensions
    local width = math.min(80, vim.o.columns - 10)
    local height = math.min(#display_lines + 2, vim.o.lines -...