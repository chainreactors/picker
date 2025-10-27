---
title: ccls and LSP Semantic Tokens
url: https://maskray.me/blog/2024-10-20-ccls-and-lsp-semantic-tokens
source: MaskRay
date: 2024-10-21
fetch_date: 2025-10-06T18:48:40.447392
---

# ccls and LSP Semantic Tokens

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-10-20](/blog/2024-10-20-ccls-and-lsp-semantic-tokens)

# ccls and LSP Semantic Tokens

I've spent countless hours writing and reading C++ code. For many
years, Emacs has been my primary editor, and I leverage [ccls](https://github.com/MaskRay/ccls/)' (my C++ language
server) rainbow semantic highlighting feature.

The feature relies on two custom notification messages
`$ccls/publishSemanticHighlight` and
`$ccls/publishSkippedRanges`.
`$ccls/publishSemanticHighlight` provides a list of symbols,
each with kind information (function, type, or variable) of itself and
its semantic parent (e.g. a member function's parent is a class),
storage duration, and a list of ranges.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` struct CclsSemanticHighlightSymbol {   int id = 0;   SymbolKind parentKind;   SymbolKind kind;   uint8_t storage;   std::vector<std::pair<int, int>> ranges;    std::vector<lsRange> lsRanges; // Only used by vscode-ccls };  struct CclsSemanticHighlight {   DocumentUri uri;   std::vector<CclsSemanticHighlightSymbol> symbols; }; ``` |

An editor can use consistent colors to highlight different
occurrences of a symbol. Different colors can be assigned to different
symbols.

Tobias Pisani created emacs-cquery (the predecessor to emacs-ccls) in
Nov 2017. Despite not being a fan of Emacs Lisp, I added the rainbow
semantic highlighting feature for my own use in early 2018. My setup
also relied heavily on these two settings:

* Bolding and underlining variables of static duration storage
* Italicizing member functions and variables

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` (setq ccls-sem-highlight-method 'font-lock) (ccls-use-default-rainbow-sem-highlight) ``` |

Key symbol properties (member, static) were visually prominent in my
Emacs environment.

![](/static/2024-10-20-ccls-and-lsp-semantic-tokens/emacs-ccls.webp)

My Emacs hacking days are a distant memory â beyond basic
configuration tweaks, I haven't touched elisp code since 2018. As my
Elisp skills faded, I increasingly turned to Neovim for various editing
tasks. Naturally, I wanted to migrate my C++ development workflow to
Neovim as well. However, a major hurdle emerged: Neovim lacked the
beloved rainbow highlighting I enjoyed in Emacs.

Thankfully, Neovim supports "semantic tokens" from LSP 3.16, a
standardized approach adopted by many editors.

I've made changes to ccls (available on [a
branch](https://github.com/MaskRay/ccls/tree/semantic-tokens); [PR](https://github.com/MaskRay/ccls/pull/972))
to support semantic tokens. This involves adapting the
`$ccls/publishSemanticHighlight` code to additionally support
`textDocument/semanticTokens/full` and
`textDocument/semanticTokens/range`.

I utilize a few token modifiers (`static`,
`classScope`, `functionScope`,
`namespaceScope`) for highlighting:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` vim.cmd([[ hi @lsp.mod.classScope.cpp gui=italic hi @lsp.mod.static.cpp gui=bold hi @lsp.typemod.variable.namespaceScope.cpp gui=bold,underline ]]) ``` |

![treesitter, tokyonight-moon](/static/2024-10-20-ccls-and-lsp-semantic-tokens/neovim-semantic-tokens-basic.webp)

While this approach is a significant improvement over relying solely
on nvim-treesitter, I'm still eager to implement rainbow semantic
tokens. Although LSP semantic tokens don't directly distinguish symbols,
we can create custom modifiers to achieve similar results.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` tokenModifiers: {   "declaration", "definition", "static", ...    "id0", "id1", ... "id9", } ``` |

In the user-provided initialization options, I set
`highlight.rainbow` to 10.

ccls assigns the same modifier ID to tokens belonging to the same
symbol, aiming for unique IDs for different symbols. While we only have
a few predefined IDs (each linked to a specific color), there's a slight
possibility of collisions. However, this is uncommon and generally
acceptable.

For a token with type `variable`, Neovim's built-in LSP
plugin assigns a highlight group
`@lsp.typemod.variable.id$i.cpp` where `$i` is an
integer between 0 and 9. This allows us to customize a unique foreground
color for each modifier ID.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``` | ``` local func_colors = {   '#e5b124', '#927754', '#eb992c', '#e2bf8f', '#d67c17',   '#88651e', '#e4b953', '#a36526', '#b28927', '#d69855', } local type_colors = {   '#e1afc3', '#d533bb', '#9b677f', '#e350b6', '#a04360',   '#dd82bc', '#de3864', '#ad3f87', '#dd7a90', '#e0438a', } local param_colors = {   '#e5b124', '#927754', '#eb992c', '#e2bf8f', '#d67c17',   '#88651e', '#e4b953', '#a36526', '#b28927', '#d69855', } local var_colors = {   '#429921', '#58c1a4', '#5ec648', '#36815b', '#83c65d',   '#419b2f', '#43cc71', '#7eb769', '#58bf89', '#3e9f4a', } local all_colors = {   class = type_colors,   constructor = func_colors,   enum = type_colors,   enumMember = var_colors,   field = var_colors,   ['function'] = func_colors,   method = func_colors,   parameter = param_colors,   struct = type_colors,   typeAlias = type_colors,   typeParameter = type_colors,   variable = var_colors } for type, colors in pairs(all_colors) do   for i = 1,#colors do     for _, lang in pairs({'c', 'cpp'}) do       vim.api.nvim_set_hl(0, string.format('@lsp.typemod.%s.id%s.%s', type, i-1, lang), {fg=colors[i]})     end   end end  vim.cmd([[ hi @lsp.mod.classScope.cpp gui=italic hi @lsp.mod.static.cpp gui=bold hi @lsp.typemod.variable.namespaceScope.cpp gui=bold,underline ]]) ``` |

Now, let's analyze the C++ code above using this configuration.

![tokyonight-moon](/static/2024-10-20-ccls-and-lsp-semantic-tokens/neovide-semantic-tokens.webp)

tokyonight-moon

While the results are visually pleasing, I need help implementing
code lens functionality.

## Inactive code highlighting

Inactive code regions (skipped ranges in Clang) are typically
displayed in grey. While this can be helpful for identifying unused
code, it can sometimes hinder understanding the details. I simply
disabled the inactive code feature.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` #ifdef X ... // colorful #else ... // normal instead of grey #endif ``` |

## Refresh

When opening a large project, the initial indexing or cache loading
process can be time-consuming, often leading to empty lists of semantic
tokens for the initially opened files. While ccls prioritizes indexing
these files, it's unclear how to notify the client to refresh the files.
The existing `workspace/semanticTokens/refresh` request,
unfortunately, doesn't accept text document parameters.

In contrast, with `$ccls/publishSemanticHighlight`, ccls
proactively sends the notification after an index update (see
`main_OnIndexed`).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` void main_OnIndexed(DB *db, WorkingFiles *wfiles, IndexUpdate *update) {   ...    db->applyIndexUpdate(update);    // Update indexed content, skipped ranges, and semantic highlighting.   if (update->files_def_update) {     auto &def_u = *update->files_def_update;     if (WorkingFile *wfile = wfiles->getFile(def_u.first.path)) {       wfile->setIndexContent(g_config->index.onChange ? wfile->buffer_content                                                       : def_u.second);       QueryFile &file = db->files[update->file_id];       // Publish notifications to the file.       emitSkippedRanges(wfile, file);       emitSemanticHighlight(db, wfile, file);       // But how do we send a workspace/semanticTokens/refresh request?????     }   } } ``` |

While the semantic token request supports partial results ...