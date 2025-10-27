---
title: Neovim Go Template Formatting
url: https://robinverton.de/til/neovim-go-template-formatting/
source: Robin Verton - developer, software engineer and red teamer
date: 2024-08-11
fetch_date: 2025-10-06T18:02:25.663468
---

# Neovim Go Template Formatting

[rv](/)
[blog](/blog)
[security](/security)
[TIL](/til)
[uses](/uses)

# Neovim Go Template Formatting

August 10, 2024

[neovim](https://robinverton.de/tags/neovim/)

[html/template](https://robinverton.de/tags/html/template/)

[go](https://robinverton.de/tags/go/)

[hugo](https://robinverton.de/tags/hugo/)

This cost me some time googling and fiddling around with my config, so here is
a quick setup on how to get Go’s `html/template` format working with neovim.
This template syntax is also used by Hugo (which I use for this page).

First, install a formatter which is able to format Go’s template syntax:

`npm install --save-dev prettier prettier-plugin-go-template`

To tell prettier to use this plugin for the current folder (and subfolders),
use the following `.prettierrc` file:

```
{
    "plugins": [
        "prettier-plugin-go-template"
    ],
    "overrides": [
        {
            "files": [
                "*.html"
            ],
            "options": {
                "parser": "go-template"
            }
        }
    ]
}
```

Now all thats left is tell neovim to run prettier when formatting. This depends on the formatting setup you are using. Because I am using [conform.nvim](https://github.com/stevearc/conform.nvim), I configured it to use prettier by default for HTML:

```
return {
  "stevearc/conform.nvim",
  event = { "BufReadPre", "BufNewFile" },
  cmd = { "ConformInfo" },
  keys = {
    -- [...]
  },
  opts = {
    formatters_by_ft = {
      templ = { "templ" },
      go = { "goimports", "gofmt" },
      html = { "prettier" }
    },
    format_on_save = { timeout_ms = 500, lsp_format = "fallback" },
  },
}
```

Thats it! Saving the file will now autoformat with the correct formatting for
Go’s `text/html` templates.

### See Also

* ## [Improved validation with generics in Go](/blog/go-echo-generic-validation/) [go](https://robinverton.de/tags/go/)
* ## [Serverless Go web app on AWS with SWR](/til/serverless-go-web-app-on-aws-with-swr/) [go](https://robinverton.de/tags/go/) [aws](https://robinverton.de/tags/aws/) [cdk](https://robinverton.de/tags/cdk/) [lambda](https://robinverton.de/tags/lambda/)
* ## [tevents: event logger and job monitor for tailnets](/blog/tevents-private-event-logging-and-job-monitoring/) [go](https://robinverton.de/tags/go/) [tailscale](https://robinverton.de/tags/tailscale/)
* ## [Queueing with PostgreSQL and Go](/blog/queueing-with-postgresql-and-go/) [go](https://robinverton.de/tags/go/) [postgres](https://robinverton.de/tags/postgres/)
* ## [hntr, shareable workspaces for target data](/blog/hntr-shareable-workspaces-for-target-data/) [security](https://robinverton.de/tags/security/) [go](https://robinverton.de/tags/go/) [postgres](https://robinverton.de/tags/postgres/)

[Mail](/cdn-cgi/l/email-protection#caa2afa6a6a58ab8a5a8a3a4bcafb8bea5a4e4aeaf)
•
[Twitter](https://twitter.com/robinverton)
•
[Github](https://github.com/rverton)
• [Imprint](/imprint) •
robinverton.de,
2025