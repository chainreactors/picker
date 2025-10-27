---
title: Breaking Out of Restricted Mode: XSS to RCE in Visual Studio Code
url: https://starlabs.sg/blog/2025/05-breaking-out-of-restricted-mode-xss-to-rce-in-visual-studio-code/
source: Blogs on STAR Labs
date: 2025-05-15
fetch_date: 2025-10-06T22:25:28.370824
---

# Breaking Out of Restricted Mode: XSS to RCE in Visual Studio Code

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Breaking Out of Restricted Mode: XSS to RCE in Visual Studio Code

May 14, 2025 · 7 min · Devesh Logendran

Table of Contents

* [Vulnerability Details](#vulnerability-details)
* [Escalating to RCE](#escalating-to-rce)
* [Proof-of-Concept:](#proof-of-concept)
* [Suggested Mitigations](#suggested-mitigations)
* [Demo](#demo)
* [Timeline](#timeline)

In April 2024, I discovered a high-severity vulnerability in Visual Studio Code (VS Code <= 1.89.1) that allows attackers to escalate a Cross-Site Scripting (XSS) bug into full Remote Code Execution (RCE)—even in Restricted Mode.

The desktop version of Visual Studio Code runs on Electron. Renderer processes are sandboxed and communicate with the main process through [Electron’s IPC mechanism](https://www.electronjs.org/docs/latest/tutorial/ipc).

An XSS vulnerability in the newly-introduced [minimal error rendering](https://code.visualstudio.com/updates/v1_89#_minimal-error-renderer) mode for Jupyter notebooks enables arbitrary JavaScript code to be executed within the `vscode-app` WebView for the notebook renderer. The vulnerability can be triggered by opening a crafted `.ipynb` file if the user has the setting enabled, or by opening a folder containing a crafted `settings.json` file in VS Code and opening a malicious ipynb file within the folder. This vulnerability can be triggered even when Restricted Mode is enabled (which is the default for workspaces that have not been explicitly trusted by the user).

In this post, we’ll walk through how the bug works and how it bypasses VS Code’s Restricted Mode.

## Vulnerability Details[#](#vulnerability-details)

Default installations of Visual Studio provide some in-built support for Jupyter Notebooks and provide default renderers for [some common output types](https://github.com/microsoft/vscode/blob/50f2b2eca8d5c6e19ec95f9d46a59f623e60cac3/extensions/notebook-renderers/src/index.ts#L543). The source code for these renderers can be found at `extensions/notebook-renderers/src/index.ts`. For cells of type `application/vnd.code.notebook.error`, the renderer calls the `renderError` function, which in turn calls [`formatStackTrace`](https://github.com/microsoft/vscode/blob/50f2b2eca8d5c6e19ec95f9d46a59f623e60cac3/extensions/notebook-renderers/src/stackTraceHelper.ts#L6) located in `stackTraceHelper.ts`. That function further calls `linkify`, located in the same file, to convert references to lines located in particular cells to clickable links within VS Code. If minimal error rendering mode is enabled, the program will pass the results from `formatStackTrace` to `createMinimalError`, which performs some further processing and appends the result to the webview’s DOM. Relevent extracts from the code with annotations are reproduced here.

renderError:

```
function renderError(
	outputInfo: OutputItem,
	outputElement: HTMLElement,
	ctx: IRichRenderContext,
	trustHtml: boolean // false if workspace is not trusted
): IDisposable {

    // ...

	if (err.stack) {
		const minimalError = ctx.settings.minimalError && !!headerMessage?.length;
		outputElement.classList.add('traceback');

		const { formattedStack, errorLocation } = formatStackTrace(err.stack);
        // ...
		if (minimalError) {
			createMinimalError(errorLocation, headerMessage, stackTraceElement, outputElement);
		} else {
			// ...
		}
	} else {
		// ...
	}

	outputElement.classList.add('error');
	return disposableStore;
}
```

formatStackTrace and linkify:

```
export function formatStackTrace(stack: string): { formattedStack: string; errorLocation?: string } {
	let cleaned: string;
	// ...

	if (isIpythonStackTrace(cleaned)) {
		return linkifyStack(cleaned);
	}
}

const cellRegex = /(?<prefix>Cell\s+(?:\u001b\[.+?m)?In\s*\[(?<executionCount>\d+)\],\s*)(?<lineLabel>line (?<lineNumber>\d+)).*/;

function linkifyStack(stack: string): { formattedStack: string; errorLocation?: string } {
	const lines = stack.split('\n');

	let fileOrCell: location | undefined;
	let locationLink = '';

	for (const i in lines) {

		const original = lines[i];
		if (fileRegex.test(original)) {
			// ...
		} else if (cellRegex.test(original)) {
			fileOrCell = {
				kind: 'cell',
				path: stripFormatting(original.replace(cellRegex, 'vscode-notebook-cell:?execution_count=$<executionCount>'))
			};
			const link = original.replace(cellRegex, `<a href=\'${fileOrCell.path}&line=$<lineNumber>\'>line $<lineNumber></a>`); // [1]
			lines[i] = original.replace(cellRegex, `$<prefix>${link}`);
			locationLink = locationLink || link; // [2]

			continue;
		}
        // ...
	}

	const errorLocation = locationLink; // [3]
	return { formattedStack: lines.join('\n'), errorLocation };
}
```

createMinimalError:

```
function createMinimalError(errorLocation: string | undefined, headerMessage: string, stackTrace: HTMLDivElement, outputElement: HTMLElement) {
	const outputDiv = document.createElement('div');
	const headerSection = document.createElement('div');
	headerSection.classList.add('error-output-header');

	if (errorLocation && errorLocation.indexOf('<a') === 0) {
		headerSection.innerHTML = errorLocation; // [4]
	}
	const header = document.createElement('span');
	header.innerText = headerMessage;
	headerSection.appendChild(header);
	outputDiv.appendChild(headerSection);

	// ...
	outputElement.appendChild(outputDiv);
}
```

At `[1]` and `[2]`, the code tries to convert sequences such as `Cell In [1], line 6` (optionally with ANSI escape sequences) to HTML tags for links with the form `<a href=vscode-notebook-cell:?execution_count=1&line=6>line 6</a>` and sets the errorLocation variable to this HTML at `[3]`. Crucially, the wildcard at the end of the regular expression it uses will swallow any text that comes after the line number, but any text immediately preceding the `Cell In` sequence will not be affected by the `replace` operation. Thus, an input like `LOLZTEXTHERECell In [1], line 6` in the ipynb. would result in the invalid markup `LOLZTEXTHERE<a href=LOLZTEXTHEREvscode-notebook-cell:?execution_count=1&line=6>line 6</a>`.

In `createMinimalError`, if `errorLocation` is set and begins with `<a`, it is considered to be a link generated by the `formatStackTrace` function and is thus assigned to `headerSection.innerHTML` directly. This element is added to the output DOM regardless of whether the workspace is trusted or not. However, since we have partial control of the markup `formatStackTrace` generates (including the start of the string), we can create a notebook file with the stack trace `<a><img src onerror=console.log(123)>Cell In [1], line 6`, which will result in the value of `errorLocation` being `<a><img src onerror=console.log(123)><a href=<a><img[etc]`. Since this satisfies the condition of beginning with `<a>`, it will be inserted into `headerSection.innerHTML` and rendered in the webview, resulting in the JavaScript being run and `123` being logged to the console.

![javascript execution in console](/blog/2025/images/XSS-to-RCE-in-Visual-Studio-Code_01.png)

## Escalating to RCE[#](#escalating-to-rce)

The XSS vulnerability leads to code execution within an iframe under the `vscode-app` origin, which is a frame under the main workbench window which is under the `vscode-file` origin. The main workbench window contains the `vscode.ipcRenderer` object which enables the renderer frame to send IPC messages to the main frame in order to perform filesystem operations, create and execute commands in PTYs, ...