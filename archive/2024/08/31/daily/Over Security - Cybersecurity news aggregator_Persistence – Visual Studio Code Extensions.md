---
title: Persistence – Visual Studio Code Extensions
url: https://pentestlab.blog/2024/03/04/persistence-visual-studio-code-extensions/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:06:35.356434
---

# Persistence – Visual Studio Code Extensions

[Skip to content](#content)

[Penetration Testing Lab](https://pentestlab.blog/)

Offensive Techniques & Methodologies

Menu

* [Methodologies](https://pentestlab.blog/methodologies/)
  + [Red Teaming](https://pentestlab.blog/methodologies/red-teaming/)
    - [Credential Access](https://pentestlab.blog/methodologies/red-teaming/credential-access/)
    - [Persistence](https://pentestlab.blog/methodologies/red-teaming/persistence/)
* [Resources](https://pentestlab.blog/resources/)
  + [Papers](https://pentestlab.blog/resources/papers/)
    - [Web Application](https://pentestlab.blog/resources/papers/web-application/)
  + [Presentations](https://pentestlab.blog/resources/presentations/)
    - [Defcon](https://pentestlab.blog/resources/presentations/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/presentations/derbycon/)
    - [Tools](https://pentestlab.blog/resources/presentations/tools/)
  + [Videos](https://pentestlab.blog/resources/videos/)
    - [BSides](https://pentestlab.blog/resources/videos/bsides/)
    - [Defcon](https://pentestlab.blog/resources/videos/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/videos/derbycon/)
    - [Hack In Paris](https://pentestlab.blog/resources/videos/hack-in-paris/)
* [Contact](https://pentestlab.blog/contact-the-lab/)
  + [About Us](https://pentestlab.blog/contact-the-lab/about-us/)

Posted on [March 4, 2024March 2, 2024](https://pentestlab.blog/2024/03/04/persistence-visual-studio-code-extensions/)

# Persistence – Visual Studio Code Extensions

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[Leave a Comment on Persistence – Visual Studio Code Extensions](https://pentestlab.blog/2024/03/04/persistence-visual-studio-code-extensions/#respond)

It is not uncommon developers or users responsible to write code (i.e. detection engineers using [Sigma](https://marketplace.visualstudio.com/items?itemName=humpalum.sigma)) to utilize Visual Studio Code as their code editor. The default capability of the product can be extended using extensions such as debuggers and tools to support the development workflow. However, in a development environment that has been compromised during a red team exercise, an arbitrary Visual Studio Code extension can be used for persistence since it will also enable the red team to blend in with the underlying environment. The technique was originally discussed by the company [Secarma](https://twitter.com/Secarma).

## Extension Development

Prior to starting the development of a Visual Studio Code Extension the environment requires the following packages:

* [Visual Studio Code](https://code.visualstudio.com/)
* [NodeJS](https://nodejs.org/en/download/)
* [Yeoman](https://yeoman.io/)
* [Npm Generator Code](https://www.npmjs.com/package/generator-code)

Execution of the following commands from the command prompt will install Yeoman and the generator code.

```
npm install -g yo
npm install -g yo generator-code
```

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-extensions-yeoman-generator-code.png?w=932)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-extensions-yeoman-generator-code.png)

Yeoman & Code Generator

The command *yo code* initiates the extension generator which will generate the necessary files of the extension.

```
yo code
```

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-generator.png?w=938)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-generator.png)

Extension Generator

Using the following commands from the extension folder will initiate Visual Studio Code. Once Visual Studio Code starts, will request for the permission of the user prior to adding any files into the workspace.

```
cd persistence-pentestlab
code .
```

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-folder.png?w=1016)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-folder.png)

Extension Folder

The files of interest in an extension are:

* package.json
* extension.ts

By default the contents of these files will look similar to the pictures below:

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-package-file.png?w=1022)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-package-file.png)

Package File

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-file.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-file.png)

Extension File

Executing the command *HelloWorld* will display the HelloWorld information message as it will call the function *showInformationMessage* from the extension.ts file.

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-hello-world.png?w=1018)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-hello-world.png)

Hello World Extension

According to the Visual Studio Code there are a number of *[activation events](https://code.visualstudio.com/api/references/activation-events)* which can be declared in the *package.json* file. These events could provide a variety of persistence options such as execute a command when a specific language file is opened or during start of Visual Studio Code. The activation event “\*” will enforce the extension to execute every time that Visual Studio Code starts.

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-package-persistence.png?w=1016)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-package-persistence.png)

Extension Package Persistence

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extension-activation-events.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extension-activation-events.png)

Activation Events

The following code can be used in the *extension.ts* file in order to display a message a proof of concept once Visual Studio Code initiates.

```
import * as vscode from 'vscode';
export function activate(context: vscode.ExtensionContext) {
let disposable = vscode.commands.registerCommand('persistence-pentestlab.Install', () => {
vscode.window.showInformationMessage('Implant is executed');
    });    context.subscriptions.push(disposable);
    vscode.commands.executeCommand('persistence-pentestlab.Install');
}
export function deactivate() {}
```

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-message.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-message.png)

Extension Message

The image below demonstrates that the message “*Implant is executed*” has been displayed on the next run of Visual Studio Code.

[![](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-show-information-message.png?w=1018)](https://pentestlab.blog/wp-content/uploads/2024/02/visual-studio-code-extensions-extension-show-information-message.png)

Extension Show Information Message

## Command Execution

Now that there is a verification that code can be executed during start, the extension code can be modified to run a command. The following code snippet uses the *child\_process* library to run the *whoami* command and log the output into the console.

```
import * as vscode from 'vscode';
export function activate(context: vscode.ExtensionContext) {
let disposable = vscode.commands.registerCommand('persistence-pentestlab.Install', () => {
vscode.window.showInformationMessage('Imp...