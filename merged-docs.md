

# README.md

# About the book

`a-Shell` is not only a terminal emulator for iOS/iPadOS, but also an environment with a set of useful libraries, where you can run basic Unix commands and other tricky tools.

This document is a tutorial for newcomers to know how to do various things on this app, from editing text files to compiling big projects.

The tutorial is still in progress. Anyone willing to is encouraged to contribute to this document. See [contribute-to-the-book.md](contribute-to-the-book.md "mention") for details.

This work is published under CC BY-SA 4.0 license. Feel free to share it around.

If you know little about `a-Shell`, you can start by reading [README (1).md](<README (1).md> "mention").

{% hint style="warning" %}
Some parts of this doc are NOT stable. As a new-born document I chose to expose all unstable parts to the readers since they have been under development rather than release them after strict tests so that you can see newest changes at all times. Each unstable part will be marked with a warning hint.
{% endhint %}

### Official links of a-Shell

**GitHub repo:** [**https://github.com/holzschu/a-shell**](https://github.com/holzschu/a-shell)

**Official site:** [**https://holzschu.github.io/a-Shell\_iOS/**](https://holzschu.github.io/a-Shell\_iOS/)

**Discord:** [**https://discord.gg/2KAAfTpnRb**](https://discord.gg/2KAAfTpnRb)


# README (1).md

# A guide for beginners

You may have already found `a-Shell` on the App Store. `a-Shell` is a terminal emulator for iOS/iPadOS, which allows you to run various Unix commands, from importing the `python.rich` module to managing `vim` plugins. You can use `ffmpeg`, `python`, `lua`, `tex`, `perl`, `clang`, `wasm`, `jsc`, etc, and edit text using `vim` or nano-like `pico`. You can even run `JupyterLab`; also, `code-server` may be researched in the future.

### What you can do

#### Basic commands and net commands

As is expected, basic commands like `ls`, `cd` and `cp` are available of course. Many important net commands have been provided as well.

```sh
$ ping google.com -c 4
PING google.com (198.18.0.85): 56 data bytes
64 bytes from 198.18.0.85: icmp_seq=0 ttl=64 time=0.406 ms
64 bytes from 198.18.0.85: icmp_seq=1 ttl=64 time=0.454 ms
64 bytes from 198.18.0.85: icmp_seq=2 ttl=64 time=0.532 ms
64 bytes from 198.18.0.85: icmp_seq=3 ttl=64 time=0.396 ms
--- google.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.396/0.447/0.532/0.054 ms

$ nslookup
> apple.com
Server:         198.18.0.2
Address:        198.18.0.2#53
Non-authoritative answer:
Name:   apple.com
Address: 198.18.0.37
```

`man` command is also provided, so you can read the manuals of basic commands easily.

<figure><img src=".gitbook/assets/68F0411E-EB70-4EEA-8E82-3119770F7787.jpeg" alt=""><figcaption><p>Manual of make</p></figcaption></figure>

#### Get more packages

A tool called `pkg` can be used to install some extra commands. You can use `pkg install` to get more commands:

```sh
$ pkg install zip
```

Use `pkg list` to list all packages already-installed and `pkg search <package name>` to search if a package is available. To see all available packages, use `pkg search`. To remove a package, use `pkg remove <package name>`.

The variable `$PKG_SERVER` defines the address to get packages. If the variable is not set, the default repository [https://github.c\
om/holzschu/a-Shell-commands](https://github.com/holzschu/a-Shell-commands) would be used. You can set the repository you use by setting the variable:

```sh
$ export PKG_SERVER=https://github.com/holzschu/a-Shell-commands 
```

If you can’t get or search for any package, there may be something wrong with `$PKG_SERVER`. Try to unset it to switch to the default repository:

```sh
$ unsetenv PKG_SERVER
```

#### Edit text files

So far three text editors are provided: `vim`, `pico` and `ed`.

Vim users may be happy to see Vim plugins just work, but plugin managers like `vim-plug` have many problems. Therefore, it’s suggested to use Vim 8’s built-in package manager. See [configure-your-vim.md](basic-tutorials/configure-your-vim.md "mention") for details.

<figure><img src=".gitbook/assets/89BA884C-9395-4E53-9284-97E69E3CE2A9.jpeg" alt=""><figcaption><p>Vim interface</p></figcaption></figure>

If you are not used to Vim and looking for a simpler text editor, `pico` will suit your needs. GNU Nano under GPL can’t be included in a-Shell due to FSF’s policy, so `pico` is included to provide a similar experience.

<figure><img src=".gitbook/assets/D884DB64-276A-46D6-8ED6-789FBD167C1C.jpeg" alt=""><figcaption><p>Pico interface</p></figcaption></figure>

A toy, `ed`, is also included. `ed` is a line editor, which allows one to input editing commands line by line. For the example below, `r`, `,p`, `1`, `2`, `3`, `4` and `q` are commands inside, and others are the outputs by `ed`.

```
$ ed
r test.cpp
131
,p
#include<iostream>
using namespace std;
int main(){
        cout << "Hello, world!" << endl;
        int a;
        cin >> a;
        cout << a;
        return 0;
}
1
#include<iostream>
2
using namespace std;
3
4
int main(){
q
$
```

#### Remote SSH/SFTP

SSH connecting is available. Just use `ssh`, `scp` and `sftp` as you’ve got used to. Use `ssh-keygen` to generate SSH keys. `mosh` and `sshd` are not supported yet.

#### Python 3

you can run Python easily.

```sh
$ python
>>> print (“Hello, world!”)
Hello, world!
```

You can also install modules using `pip`. So far `clang` can not deal with Python modules properly, so they must be written in pure Python.

```sh
$ pip install requests
Defaulting to user installation because normal site-packages is not writeable
Collecting selenium
  Downloading selenium-4.8.3-py3-none-any.whl (6.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.5/6.5 MB 2.9 MB/s eta 0:00:00
Requirement already satisfied: urllib3[socks]~=1.26 in /private/var/containers/Bundle/Application/C3889491-0CAD-4C9D-8B01-39773D35A63A/a-Shell.app/Library/lib/python3.11/site-packages (from selenium) (1.26.13)
Collecting trio~=0.17
  Downloading trio-0.22.0-py3-none-any.whl (384 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 384.9/384.9 kB 4.8 MB/s eta 0:00:00
Collecting trio-websocket~=0.9
  Downloading trio_websocket-0.10.2-py3-none-any.whl (17 kB)
Requirement already satisfied: certifi>=2021.10.8 in /private/var/containers/Bundle/Application/C3889491-0
CAD-4C9D-8B01-39773D35A63A/a-Shell.app/Library/lib/python3.11/site-packages (from selenium) (2022.9.24)
Requirement already satisfied: attrs>=19.2.0 in /private/var/containers/Bundle/Application/C3889491-0CAD-4
C9D-8B01-39773D35A63A/a-Shell.app/Library/lib/python3.11/site-packages (from trio~=0.17->selenium) (22.1.0
)
Collecting sortedcontainers
  Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Collecting async-generator>=1.9
  Downloading async_generator-1.10-py3-none-any.whl (18 kB)
Requirement already satisfied: idna in /private/var/containers/Bundle/Application/C3889491-0CAD-4C9D-8B01-
39773D35A63A/a-Shell.app/Library/lib/python3.11/site-packages (from trio~=0.17->selenium) (3.4)
Collecting outcome
  Downloading outcome-1.2.0-py2.py3-none-any.whl (9.7 kB)
Requirement already satisfied: sniffio in /private/var/containers/Bundle/Application/C3889491-0CAD-4C9D-8B
01-39773D35A63A/a-Shell.app/Library/lib/python3.11/site-packages (from trio~=0.17->selenium) (1.3.0)
Collecting exceptiongroup
  Downloading exceptiongroup-1.1.1-py3-none-any.whl (14 kB)
Collecting wsproto>=0.14
  Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)
Collecting PySocks!=1.5.7,<2.0,>=1.5.6
  Downloading PySocks-1.7.1-py3-none-any.whl (16 kB)
Collecting h11<1,>=0.9.0
  Downloading h11-0.14.0-py3-none-any.whl (58 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 kB 2.2 MB/s eta 0:00:00
Installing collected packages: sortedcontainers, PySocks, outcome, h11, exceptiongroup, async-generator, w
sproto, trio, trio-websocket, selenium
Successfully installed PySocks-1.7.1 async-generator-1.10 exceptiongroup-1.1.1 h11-0.14.0 outcome-1.2.0 se
lenium-4.8.3 sortedcontainers-2.4.0 trio-0.22.0 trio-websocket-0.10.2 wsproto-1.2.0
```

#### Lua and Perl

Other script languages like Lua do work.

```sh
$ lua
Lua 5.4.4  Copyright (C) 1994-2022 Lua.org, PUC-Rio
> print ("Hello, world!")
Hello, world!
```

Perl also works.

```
$ perl test.pl
Hello, world!
```

#### JavaScript

The JS environment of WebKit is included. You can use `jsc` to run normal JavaScript codes.

```sh
$ echo 'console.log("Hello, world!");' > test.js
$ jsc test.js
Hello, world!
```

It will be a hard thing to have `node.js` included. Possibilities exist to make them run with `jsc` but so far nobody has tried. In the chapter _Let’s do more for it_ this problem will be talked about.

#### C/C++ and WebAssembly

Thanks to WebAssembly, it’s not impossible to compile projects written in C/C++. With `clang`, we can compile C codes into WebAssembly, and with `wasm`, we can run them easily. In fact, almost all commands installed by `pkg` are distributed in WebAssembly.


# SUMMARY.md

# Table of contents

* [About the book](README.md)
* [Contribute to the book](contribute-to-the-book.md)

## Basic tutorials

* [A guide for beginners](<README (1).md>)
* [A-Shell’s differences](basic-tutorials/a-shells-differences.md)
* [Configure fonts, colors and the toolbar](basic-tutorials/configure-fonts-colors-and-the-toolbar.md)
* [Configure the Shell](basic-tutorials/configure-the-shell.md)
* [Configure lg2 for version controlling](basic-tutorials/configure-lg2-for-version-controlling.md)
* [Configure your Vim](basic-tutorials/configure-your-vim.md)
* [Run Jupyter](basic-tutorials/run-jupyter.md)

## Let’s do more for it

* [Before the hard part](lets-do-more-for-it/before-the-hard-part.md)
* [Submit new packages](lets-do-more-for-it/submit-new-packages.md)
* [Compile a simple command with a-Shell](lets-do-more-for-it/compile-a-simple-command-with-a-shell.md)
* [WebAssembly for a-Shell](lets-do-more-for-it/webassembly-for-a-shell.md)
* [Compile a-Shell yourself](lets-do-more-for-it/compile-a-shell-yourself.md)

***

* [Ended?](ended.md)


# contribute-to-the-book.md

# Contribute to the book

Everyone is encouraged to add anything he wants to this guide. Want to tell others how to compile a project written in Java? Want to provide a solution for a commonly seen issue? Or just want to let the document earlier to finish? This article will guide you to make contributions to this document.

Note that this guide is under CC BY-SA 4.0 license. That is to say all of your contributions will be released under that license.

### Edit existing articles

This guide is stored at a GitHub repository: [https://github.com/HeavySnowJakarta/A-guide-to-a-Shell](https://github.com/HeavySnowJakarta/A-guide-to-a-Shell). When you want to edit the article you are reading, click the three dots on the top right-hand corner of the page, and choose “Edit on GitHub”. You will be led to the GitHub page of that article.

<figure><img src=".gitbook/assets/8AAC1CD5-811D-41DE-B6B1-F2BF41F3B4DF.jpeg" alt=""><figcaption></figcaption></figure>

Then fork the repository as you would for normal GitHub repositories. Clone it into your computer, edit the page, push back, and then send a Pull Request. That’s all you need to do.

### Provide an idea for a new page

You may want to start a new page to include your ideas. Start an issue on the repository above, and I will create a new page in place based on the existing content structure, and then you can start your contributions. If you have any other ideas, do not hesitate to open an issue or discussion.


# basic-tutorials/a-shells-differences.md

# A-Shell’s differences

In this article, we will talk about three topics: a-Shell’s features, limitations, and comparison with alternatives.

### Features

#### Shortcuts

This is one of the most welcomed functions of a-Shell. You can easily find the supported shortcuts on WorkFlow:

<figure><img src="../.gitbook/assets/52D449EE-B42E-4AC7-B5EA-89CB287D8FA7.jpeg" alt=""><figcaption><p>3 supported shortcuts: execute command, get file, and put file</p></figcaption></figure>

With WorkFlow, what you can do with a shell has been greatly expanded.

By default, all files generated by shortcuts are stored at `~shortcuts/`.

#### Jump here and there

`z` command is built-in. With it you can easily jump between directories. What’s more, `z` is lighter and faster than `autojump`, making it more suitable for a-Shell.

Adding bookmarks for directories is also supported. Use `bookmark <name>` to add a bookmark for the current directory, `cd ~<name>` or `jump <name>` to jump to a bookmark, `showmarks` to show all current bookmarks, `renamemark` to revise the name of a bookmark and `deletemark` to delete it.

Any time you run `cd` without a parameter, you will be led to `~/Documents`, the initial directory. `cd -` will lead you to the last directory you were in.

#### iOS/iPadOS interactions

A series of commands are provided to interact with other apps. Use `open <file>` to share a file with other apps:

<figure><img src="../.gitbook/assets/626A2672-C4E6-4F3C-8FAD-EEAEC60882AE.jpeg" alt=""><figcaption><p>The share interace</p></figcaption></figure>

Use `view` to view a file rapidly, which may be helpful for PDF/HTML files or images.

<figure><img src="../.gitbook/assets/58BB49F1-0C92-4FFC-8FCF-A4EA9F0FAB20.jpeg" alt=""><figcaption><p>An HTML page view</p></figcaption></figure>

Use `play` command to play audio/video files.

<figure><img src="../.gitbook/assets/D61372EE-CB56-476C-921D-A720D67B4418.jpeg" alt=""><figcaption><p>An playing audio file</p></figcaption></figure>

Use `internalbrowser` like `internalbrowser https://google.com` to visit web pages within a-Shell, and swipe left or right to jump between pages. When you swipe right on the first page you view, you will go back to the console. This function may be helpful for front-end projects in the future.

Although you can easily share a file _from_ a-Shell via `open`, you can’t share a file _to_ a-Shell directly. Fortunately, you can achieve that using shortcuts. As mentioned earlier, all files shared to a-Shell are saved at `~shortcuts/`. For another location, consider using a shortcut to execute a command automatically.

#### Access to the files

With `pickFolder` command, a-Shell can get access to another location on your iPhone/iPad, iCloud for example.

You can also read/write `~/Documents/` folder with Files. Switch to “My iPhone”/“My iPad”, and you’ll see the directory “a-Shell”. Attention files outside of `~/Documents/` can not be read.

### Limitations

Limitations mainly come from two aspects: those from Apple and those from the FSF.

#### Limitations from Apple

Due to Apple’s limitation, only those directories can be accessed by a-Shell: `~/Documents/`, `~/Library` and `~/tmp`, which has made a-Shell’s file structure uncommon. All user configuration files are stored at `~/Documents/` instead of `~`, and `$HOME` has been set to `~/Documents/` as well. The file structure has made building works, especially cross-compiling more complex, so it should be treated carefully.

Executable files are either native codes for iOS/iPadOS, or WebAssembly files. Due to Apple’s limitation, all native codes must be shipped with the App itself when released. To add a new command with native codes, you have to resign the developer certificate and release the whole app to App Store, and all users would receive the update then.

For native codes, many functions are unavailable on `arm64` for iOS, such as `fork()`, `exec()`, `system()`, etc. a-Shell emulates `fork()` and `exec()` for POSIX programs, which is not perfect but enough. WebAssembly is very limited as well, so that few commands can be compiled to WebAssembly.

`sudo` is also unavailable because of Apple’s limitations, so programs requiring a super-user privilege like `traceroute` does not work.

For jailbroken device users, there may be differences on a-Shell. For example, the entire file system would be able to read/write, which may cause problems. Do not hesitate to open an issue if you meet any of those!

#### Limitations from the FSF (Free Software Foundation)

There are actually many restrictions to use programs under GPL license. It may be not allowed to include GPL codes in the App Store distributions. You may have to ask for all contributors‘ permission, which may be very hard. Thus, it‘s suggested not to include any GPL codes in a-Shell and try to find alternatives under BSD or other licenses. `bash`, `emacs`, `nano` and many other excellent programs can’t be included for this reason.

### Comparisons with alternatives

Here are comparisons between a-Shell and some alternatives. You may find which one suits you better here.

#### iSH

iSH is a Linux emulator for iOS/iPadOS, which uses syscall to translate Linux x86 commands. Of course, it’s interesting to use Alpine with an iOS device without jailbreaking.

With an emulating layer, iSH can do more things than a-Shell. You can run normal bash scripts, compile and run native binary codes or use `apk` to install a great number of packages. But attention iSH can’t do anything you like. `node.js` and some important tools can’t be supported. What’s more, iSH works greatly slower and more unstable than a-Shell. It’s not very happy to wait 10 seconds for a simple Python script or a minute to clone a Git repository, right?

#### Blink Shell

Blink is a remote device connecting tool for iOS/iPadOS, which now provides the best terminal experience on an iOS device. Blink Shell’s command function is based on `ios_system`, the same with a-Shell, so it’s listed here.

Blink Shell has an awesome appearance, an easy-to-use configure menu and a strong remote working ability, so it’s a recommended SSH/Mosh client for iOS/iPadOS. But Blink Shell itself is much weaker than a-Shell, where only basic UNIX commands are supported. You can’t even clone from a repository with it!

Blink Code is another welcomed function of Blink. Imagine coding with VSCode on an iPad everywhere! But attention it’s based on `vscode.dev`. Actually there is not a way to run a native VSCode on iPad yet.

Blink is not completely free of charge as well. Users of the free plan will receive a “it’s time to become a pro” screen every day. They are forced to “rest“ for a while and have to pay for the advanced plan to remove it.

#### NewTerm

NewTerm is a terminal app for Apple devices. For iPhones or iPads, jailbreaking is required. It’s a real terminal emulator that can control the Apple Device completely, which is welcomed by jailbroken users. Of course, the things it can do are much more than what a-Shell can do.

Besides functions, it has a tab-based interface and good font support. However, there are still some jailbroken users who prefer a-Shell for its shortcuts or other features.

#### Termux

Termux is a terminal emulator for Android devices, supporting Linux environments for them. It uses `pkg` to manage packages.

Based on the Linux sub system, Termux has a strong ability to run a lot of programs, no matter `bash`, `zsh` or `fish`. What’s more, a number of developing tools are built-in, allowing users to build or debug. It can also use the API of Android, like reading the SMS box.

It’s even amazing to provide `proot` to allow users to install a complete Linux system here, and then almost everything can be done. On the contrary, the number of what an iOS device can do is much smaller.


# basic-tutorials/configure-fonts-colors-and-the-toolbar.md

# Configure fonts, colors and the toolbar

`config` command is provided to allow users to configure the fonts, the color of the text and the background, and the toolbar.

### In a word

```
usage: config [-s font size][-n font name][-b background color][-f foreground 
color][-c cursor color][-k shape][-dgprth]
```

* `-s font size`: change the size of the text
* `-n font name`: change the font
* `-b background color`: change the background color
* `-f foreground color`: change the text color
* `-c cursor color`: change the color of the cursor
* `-k shape`: change the shape of the cursor, where `shape` can be beam, block or underline

For commands above, `default` can be used to return to the status stored before, and `factory` can be used to go back to the factory status.

* `-d`: do not save the changes and go back to the precious status
* `-g`: apply the change to all the open windows
* `-p`: save the change to apply it permanently
* `-r`: go back to the initial status: white background and black text
* `-t`: generate a toolbar configuration file
* `-h`: print the help text

### Font

First you have to prepare your own console font manually. It’s recommended to use a nerd font from [https://www.nerdfonts.com](https://www.nerdfonts.com), which includes various icons. Download a font file to your device, then use an App like iFonts to have it installed.

In this example, we’ll use `UbuntuMono Nerd Font Mono`. Go back to a-Shell and just run:

```
$ config -n 'UbuntuMono Nerd Font Mono'
```

If you don’t know the name of your font, use `config -n` to open a font menu and choose one then.

<figure><img src="../.gitbook/assets/4D2C7F31-8B19-4CEC-B5D1-B0940275F88C.jpeg" alt=""><figcaption><p>The font menu</p></figcaption></figure>

### Color

You may want a terminal with a black background and white/green text. Let’s run:

```
$ config -b black -f white -c white
```

Use any other colors if you like.

Then save all the settings:

```
$ config -gp
```

Sometimes it looks like:

<figure><img src="../.gitbook/assets/68779072-3337-4915-A0A0-164394ED4052.png" alt=""><figcaption><p>The status bar and keyboard is stIll whIte</p></figcaption></figure>

Wait, why there is still somewhere not dark as the background? These two places are only dark when the device is in dark mode. If you want those to keep light or dark, you can configure it on the Settings App. Start Settings, and you’ll find “a-Shell” at the left menu. Now you see the settings of a-Shell:

<figure><img src="../.gitbook/assets/4E304434-1F28-4CED-AD7B-F85D4060DAAD.jpeg" alt=""><figcaption><p>The setting menu of a-Shell</p></figcaption></figure>

Click “toolbar color”, and you will find four options: `system settings`, `depends on screen color`, `dark mode` and `light mode`. Just choose the one you prefer.

### Toolbar

The buttons of the toolbar at the bottom of the screen is also customizable. First, generate a toolbar configuration file:

```
$ config -t
I have created a toolbar configuration file: ~/Documents/.toolbarDefinition
You can now edit it to add or remove buttons to the toolbar.
Changes will take effect when the app restarts.
```

Then you can edit `.toolbarDefinition` by Vim or Pico. Let‘s see what the file consists of:

```
# Button icon           action          parameter
arrow.right.to.line.alt insertString    \u{0009}
chevron.up.square       systemAction    control
escape                  insertString    \u{001B}
doc.on.clipboard        systemAction    paste
separator
arrow.up                systemAction    up
arrow.down              systemAction    down
arrow.left              systemAction    left
arrow.right             systemAction    right
```

The file is divided into lines, and each line defines a button. There are two parts of it, respectively managing the left and the right end of the toolbar, separated by `separator`.&#x20;

There are three parts of each line: `icon`, `action` and `parameter`. Icons can be a symbol of SF Symbols or a string of characters. For an introduction of SF Symbols, see: [https://developer.apple.com/sf-symbols/](https://developer.apple.com/sf-symbols/), actions can be `insertString`, `systemAction` or `insertCommand`, and parameters defines what to do exactly.&#x20;

`insertString` is to insert a string when pressing the button. At this time, the parameter is the string to be inserted. Special characters like `\n` or `\u{0009}` are supported so keys like Escape are not hard to add. On the contrary, the parameter of `systemAction` can be one of `up`, `down`, `left`, `right`, `control`, `cut`, `copy` or `paste`, and the parameter of `insertCommand` can be a short command. At this time, the output of the command would be inserted at the cursor position.

On iOS/iPadOS 16, when “Use the iOS/iPadOS toolbar” is enabled on the Settings App, buttons can be grouped with brackets. They can be organized conveniently and be configured when to be displayed.&#x20;

Here are some examples included in the generated file:

```
# Example buttons:
#
# delete.backward       insertString    \u{007F}
# return                insertString    \u{000D}
# switch.2              insertString    vim .toolbarDefinition\n
# calendar.badge.clock  insertCommand   date "+%Y_%m_%d"

# Example groups (only with iPads and iOS-style toolbar). Max 15 commands in a submenu
# [
#     scissors                      systemAction    cut
#     arrow.up.doc.on.clipboard     systemAction    copy
#     doc.on.clipboard              systemAction    paste
# ] filemenu.and.cursorarrow

# This one is shown only if no commands are running:
# [="none"
#     ls            insertString    ls -a ~/Documents/
#     uname         insertString    uname -a
#     ping 🍎       insertString    ping www.apple.com
#     date          insertString    date
# ]

# This one appears if you edit a Markdown file in Vim:
# [="vim .*\.md"
#     key               insertString    \u{001B}:q!\n
#     bold              insertString    :s/\\%V.*\\%V./**&**\n
#     italic            insertString    :s/\\%V.*\\%V./*&*\n
#     strikethrough     insertString    :s/\\%V.*\\%V./\\~\\~&\\~\\~\n
# ] contextualmenu.and.cursorarrow
```



# basic-tutorials/configure-the-shell.md

# Configure the Shell

This article focus on configuring the shell of a-Shell. The default (and the only) shell on a-Shell is not `bash`, but `dash`. There are differences between a-Shell’s default shell (the shell you see when you start the App) and `dash` (the shell to execute scripts) and you can run `dash` to see how `dash` works.

### Why dash?

It’s a difficult task to include a shell in a-Shell. Among the various shells we can choose, `dash` is a simpler and lighter one.

Although `bash` is used more commonly, it can‘t be included in a-Shell, because it’s under GPL. `zsh` is much more complex, but it’s on the to-do list. If it can be included successfully, the user’s experience would be greatly improved.

### Execute scripts

As `dash` is POSIX-compatible, standard shell scripts are able to be executed. But one thing should be noticed: a number of scripts relies on `bash` actually. The first lines of some scripts is not `/usr/bin/env sh` but `/usr/bin/env bash`, making it not work, even including original `neofetch`. You can try to change `bash` to `dash` or `sh`, but all scripts using the features of `bash` won’t work anyway. In many cases you have to rewrite the script to avoid that. This may be improved if `zsh` can be added in the future.

### .profile and .bashrc

`~/Documents/.profile` and `~/Documents/.bashrc` are provided to let you define what to do when the shell starts. When a new a-Shell window starts, both `~/Documents/.profile` and `~/Documents/.bashrc` are loaded, and when `dash` starts, only `~/Documents/.profile` is loaded. That’s the difference between them. You can add many things to the two scripts: environment variables, alias, the prompt, etc. For example, add a alias to your `.profile`:

```bash
alias md='mkdir'
```

### Define the prompt

Zsh lovers may be addicted to the colorful prompts of the terminal. The good news is that you can also change what the prompt looks like on a-Shell, but it’s not as easy as how you “set a theme” on `zsh` or `fish`.

What the prompt looks like is defined by the variable `$PS1`. For example, you can set it to a character you like:

```bash
$ export PS1='>'
>
```

Sometimes we want to know the current path or other useful information via the prompt. Here are some parameters you can use:

* `\d`: the current date
* `\u`: the username stored at `$USERNAME`, `mobile` by default
* `\s`: the shell’s name
* `\n`: the end of a line, used to start a new line
* `\t`: the current time, going by hh:mm:ss and 24-hour format
* `\T`: the current time, going by hh:mm:ss and 12-hour format
* `\@`: the current time, going by hh:mm and 12-hour format
* `\A`: the current time, going by hh:mm and 24-hour format
* `\v`: the current version of a-Shell
* `\V`: the current version and build number of a-Shell
* `\w`: the current complete path
* `\W`: the current working dictionary, not the complete path
* `\!` and `\#`: the number of the command, not working correctly now
* `\$`: judge if the account is `root`, `#` if yes while `$` if no (it won’t be yes even if you‘ve jailbroken)
* `\\`: a backslash
* `\[` and `\]`: start or stop a place of non-printed characters, which is used to define controlling characters like changing the color

You can use ANSI controlling characters to define colors or other styles. Here is an example:

```
$ export PS1='\[\033[034m\]\w\[\033[0m\]\$'
```

Add the command to `.bashrc` so that it can be loaded every time a-Shell starts.

Now guess how to get a rainbow-style prompt like this. Nerd fonts will be needed for arrays.

<figure><img src="../.gitbook/assets/34977EE6-3A93-4E5E-A2F4-108E57599302.jpeg" alt=""><figcaption><p>A rainbow-style prompt</p></figcaption></figure>

Attention this feature only works for a-Shell’s default shell (the one when a-Shell starts) but not for `dash`. When you run `dash`, you can only get a series of strange codes.

You may want to add a command to the variable like `` `pwd` ``. However, it doesn’t work with a-Shell, so you can’t see `git status` on the prompt.

### Define colors of ls

{% hint style="info" %}
This part is planned.
{% endhint %}


# basic-tutorials/configure-lg2-for-version-controlling.md

# Configure lg2 for version controlling

A number of users have been seeking for an available version controlling tool for a long time. When it comes to that tool for iOS/iPadOS, many users may look at those for a special purpose, like Working Copy or Git Torch. However, the push functions are all collecting fees——Does anyone can accept a “free” Git client without `git push`? Also some Apps have built-in Git support, but none of them is free of charge, except SpckEditor. You can truly use Git on iSH, but the process of it is slow and unstable. Fortunately, a-Shell has a built-in Git support. This article focus on how to use `lg2` for version controlling on a-Shell.

### Git command?

Some new users have already found there is a `git` package on the repository. However, it will just add a link to `lg2` so that you can use `git` command directly. It may be useful but be careful that there are differences between `git` and `lg2`. Due to FSF’s policy, the original `git` can not be included, but `lg2` is enough for most cases. Attention many tools to manage Git directories won’t work because of the differences even when you have `git` package installed.

Now let’s try to install the `git` command.

```
$ pkg install git
Downloading git
The git command cannot be included with
a-Shell. Would you like to create a
script at $HOME/Documents/bin/git that
wraps lg2 with the following contents?
#!/bin/sh
lg2 "$@"
Keep in mind that git and lg2 options
are not 100% compatible, and they also
do not use the same configuration files
or environment variables.
Create $HOME/Documents/bin/git? (y/n [n]) y
The $HOME/Documents/bin directory does not exist.
Creating it first.
Creating $HOME/Documents/bin/git
Creation complete
Done
```

Now you can use either `git` or `lg2` to manage Git repositories.

### SSH configuration

You may want a SSH key to link to GitHub or other Git repositories. Let’s generate an SSH key first.

```
$ ssh-keygen -t ed25519 -c "<user name>"
```

Some users prefer `rsa`. Attention sometimes RSA keys don’t work for GitHub or some other websites because of a confusing SHA-1 problem. If you meet the problem too, try `ed25519` or `ecdsa`. Choose a path and the name for your keys, set a password or not with the tutorial, and then upload your public key to the Git server. You can get a lot of useful information by searching it about how to upload it to GitHub or somewhere else. Now we’ll test it:

```
$ ssh -T git@github.com
Hi <your name>! You've successfully authenticated, but GitHub does not pr
ovide shell access.
```

That’s good. Now we‘ll configure the user name and the email.

{% hint style="warning" %}
The following part of this chapter is unstable.
{% endhint %}

```
$ lg2 config —-global user.name "<your name>"
$ lg2 config —-global user.email "<your email>"
```

To avoid being prompted for the key to use and your password each time, you can add

```
$ lg2 config —-global user.identityFile "~/Documents/.ssh/<private key filename>"
$ lg2 config —-global user.password "<your password>"
```

If these commands don't work, you can manually create a global configuration file:

```
vim ~/Documents/.gitconfig
```

Then put

```
[user]
       name = <your name>
       email = <your email>
```

in the body of the file. For more information on the configuration possibilities and required syntax, see the [Git Book](https://git-scm.com/docs/git-config#\_configuration\_file). If you put sensitive information in the file, such as SSH key passphrases, you should set file permissions appropriately to limit risks, using `chmod`.

### Cloning and other operations

You can clone any repositories naturally:

```
$ lg2 clone https://github.com/holzschu/a-shell.git
```

Then you’ll see `a-shell.git` on the current dictionary. On the contrary, for a normal computer with standard `git` command, the dictionary would be named `a-shell`. You can remove the `.git` of the url to let it look less outstanding. Actually, all basic commands works well including `lg2 push origin`, but there are still some won’t work, like drawing the commit graph. Enjoy your version controlling trip!

### Does a-Shell support Subversion, CVS or other alternatives?

No. Open an issue if you want.


# basic-tutorials/configure-your-vim.md

# Configure your Vim

### Using Vim 8’s built-in package manager

Many users have got used to package managers like `vim-plug`. Unfortunately, `vim-plug` has many problems with a-Shell. It’s recommended to turn to Vim 8’s native package managers, instead. You can run `:help packages` inside Vim for more information.

#### Installing, updating and removing packages manually

For Vim 8 of a-Shell, packages can be stored at `~/Documents/.vim/pack/*/start` or `~/Documents/.vim/pack/*/opt`, where `*` means any name you like. Each package has its own dictionary, making it easier to upgrade or remove them. All packages located in `~/Documents/.vim/pack/*/start` will be loaded automatically when Vim starts, while all those at `~/Documents/.vim/pack/*/opt` won’t. Themes should be stored at the `opt` dictionaries to avoid unpredictable problems. For example, let’s try to install NERDTree:

```bash
# It’s supposed you’ve already created the dictionary.
$ cd ~/Documents/.vim/pack/mypackages/start/nerdtree
$ lg2 clone https://github.com/preservim/nerdtree.git
```

When you want to update the package, you just need to run `lg2 pull` at its dictionary, and when you want to remove it, just delete it’s dictionary completely would be okay.

#### Importing packages

For packages not to be loaded automatically, we just need to run a command inside Vim to load it:

```
:packadd <package>
```

You can also write the command to `.vimrc` to load it automatically and suitably for complex needs.

### Edit .vimrc file

`.vimrc` stores at `~/Documents` dictionary. Just add anything you want to it to configure your Vim!

### Manage packages automatically

{% hint style="info" %}
This part is planned in the future.
{% endhint %}



# basic-tutorials/run-jupyter.md

# Run Jupyter

{% hint style="warning" %}
This article is unstable and on progress. We are calling any guys who have the experience of using Jupyter Notebook or JupyterLab.
{% endhint %}

JupyterLab and Jupyter Notebook work well on a-Shell. If you just want to run Jupyter Notebook on your device, you may have a look at Carnets. With a built-in interface, you will have an better experience there.

### Run JupyterLab


# lets-do-more-for-it/before-the-hard-part.md

# Before the hard part

> I bet if I blew the conch this minute, they'd come running. Then we'd be, you know, very solemn, and someone would say we ought to build a jet, or a submarine, or a TV set. When the meeting was over they'd work for five minutes, then wander off or go hunting.
>
> \--_Lord of the Flies_

Everyone reading this chapter of the guide book must be unsatisfied by the functions a-Shell already has, and at this chapter we will talk about various possibilities of what this App can do.

Attention that this road is filled with big challenges. Sometimes you have to learn a number of concepts or search on the Internet again and again just to deal with a confusing error. If you are ready now, start your hacking trip!

### How do programs work?

This is one of the most important problems of this topic. All programs working on a-Shell are divided into two kinds:

* Native binary codes, for `ios` and `arm64`. They work just like what normal Apps work, and theoretically they can do anything. To compile these kinds of codes, you need a Mac computer with Xcode installed, and to distribute it, you must resign the App with an developer account. Updates must be pushed to the App Store and all users have no ability to add new functions or remove them.
* WebAssembly codes, called by `wasm`. They can do simpler works and you can use any computer to compile it (even a-Shell itself). They can be added or removed by users and a simple tool `pkg` is provided to manage `wasm` packages.

Consider do you want to compile your codes to native codes or WebAssembly codes, which is decided by whether the project is complex and whether it’ll be welcomed by the majority of the users.

### The file system of a-Shell

Another important problem. According to the limitations of Apple, most paths are not available for non-jailbroken devices. So a-Shell uses a different file structure. In short:

* `~/Library/` just acts like `/usr`.
* `~/Documents` just acts like `/home/your_account`, commonly known as `~` for a normal computer.

You may have noticed a directory `~/Library/usr/` also exists. It's for special needs of `clang`.

### What would be talked about at this chapter?

This part is in progress and not finally determined.

* To compile a project in C/C++ to WebAssembly files with a-Shell’s own tool chain
* To cross-compile a project with a real computer environment’s tool chain to WebAssembly files, with `make`, `cmake` or other tools
* To submit new packages to a-Shell’s extension repository
* To add new commands to a-Shell itself and compile the project
* Go and WebAssembly
* The possibilities of Rust
* Node.js? JSCompiler?
* Some interesting ideas


# lets-do-more-for-it/compile-a-shell-yourself.md

# Compile a-Shell yourself

It's needed when you want to add any native things into a-Shell. FIRST YOU NEED A MAC. Without it you can just do NOTHING.

As I have no Mac, it's almost impossible for me to complete this guide, as well as porting anything to a-Shell natively, including things written in C/C++/Go/Rust/anything else.

What should be discussed on this article is:

+ The architecture of a-Shell, the meanings of the directories.
+ Cross-compile the CLI programs into `aarch64-apple-ios` as libraries and let them be included by a-Shell.
+ Deal with the CPython libraries, and itself.
+ Tips on how to select the CLI programs you want and remove the ones you don't want.

### How to add a command

According to [Holzschu's comment](https://github.com/holzschu/a-shell/issues/151#issuecomment-752739203):

> Hi, these are very good questions. a-Shell does not have any deep dependency to python, python is just treated like one of the many commands available.
> To compile a command, you will need to:
>
> + download the `ios_system.framework` (use the binary release at https://github.com/holzschu/ios_system)
> + compile the command for the iOS architecture: `CC = clang`, `CFLAGS="-arch arm64 -miphoneos-version-min=14.0  -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS14.3.sdk`, `LDFLAGS` is like `CFLAGS`, plus `-F ...Frameworks -framework ios_system`.
> + (once it compiles) make the system create a dynamic library rather than an executable
> + embed that dynamic library inside the executable ("Embed Frameworks", in "Build Phases")
> + add the command to `Resources/commandDictionary.plist`. It's an array of arrays, indexed by the name of the command, with 4 entries for each command:
>   + name of dynamic library
>   +  function to be called inside the library (usually main)
>   +  options (the string that is passed to get_options, can be left empty)
>   +  whether the command operates on files, directories or not (file for a compiler).
> + (once all this is done) start the command and observe what happens, debug any crash.
> + (once it is done) edit the source files for:
>   + output to stdout/stderr should be replaced by output to thread_stout/thread_stderr
>   + reading from stdin should be replaced by reading from thread_stdin
>   + make sure all memory is released when leaving the program
>   + make sure all variables are initialized when we restart the program
>   + (these two are related to a fundamental issue: we never actually exit from a program on iOS, so the system will never reclaim the memory we allocated and reinitialize the variables. It is up to us to do the cleaning).
>   + lines using `std::cout` will have to be replaced by `fprintf(thread_stdout, ...)`, I haven't yet found a way to redirect C++ standard streams.
> + (once all this is done): for AppStore release, convert the dynamic library into a framework (see examples in https://github.com/holzschu/python-aux/)
> + (once all this is done): submit a pull request, if you want the command to become part of the main application. I see your idea about having a third, separate app for a-Shell, targetting rust more than python and TeX.
>
> The first step can be difficult if the package or command insists on guessing the compiler and flags rather than letting you set them.
> If your command is simple and fast (so, not rust or cargo) you can also compile it to webAssembly, which makes things a lot easier.
> If the command uses `fork` and `exec`, you will need to edit the source code a bit more, as `fork()` is a no-op in iOS. `iOS_system` has a fake fork, but we go through both branches in the same thread.

Notice I've never tried things above before.

# lets-do-more-for-it/compile-a-simple-command-with-a-shell.md

# Compile a simple command with a-Shell

This article focus on compiling a small file or project written in C/C++ with a-Shell’s own tool chain. Due to Apple’s limitations, they can only be compiled to WebAssembly instead of native codes, so don’t dream for `emacs` or `fish`!

### Meet clang, clang++ and wasm

Let’s start from compiling a single program file. Here are two examples:

```c
// test.c
#include<stdio.h>

int main(){
    printf("Hello, world!\n");
    return 0;
}
```

```cpp
// test.cpp
#include<iostream>
using namespace std;

int main(){
    cout << "Hello, world!" << endl;
    return 0;
}
```

To compile, we use `clang` and `clang++` respectively. We use `-o` to set the name of the output file (they can end with `.wasm` or not).

```
$ clang test.c -o testc
$ clang++ test.cpp -o testcpp.wasm
```

Then run the compiled files with `wasm`. You can either call `wasm` to run it or execute it directly like binary code.

```
$ ./testc
Hello, world!
$ wasm testcpp.wasm
Hello, world!
```

You may receive a message `wasm: Error:` sometimes. When you do, try to close all the open windows then retry.

### Meet make

{% hint style="warning" %}
This part is on progress and unstable!
{% endhint %}

For big projects, it’ll be a difficult job to input commands to compile all files line by line. Usually, `make` is used to do it automatically. `make` seeks for the makefile of the project and do as it directs when it works. You may have known a famous way to compile and install a project from source codes:

```
$ ./configure
$ make
$ make install
```

For the example above, `./configure` generates the makefile according to your platform, `make` compiles the project according to the makefile, and `make install` installs it to the computer. However, sometimes `./configure` really doesn’t know the difference between a-Shell and WebAssembly, so it may do the wrong work and mess it up.

Now let’s see a simple project: `unrar`. It’s simple enough that there is no script like `configure` to generate makefiles. First of all get the whole source code, and here are parts of the short makefile:

```makefile
# Linux using GCC
CXX=c++
CXXFLAGS=-O2 -Wno-logical-op-parentheses -Wno-switch -Wno-dangling-else
LIBFLAGS=-fPIC
DEFINES=-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DRAR_SMP
STRIP=strip
AR=ar
LDFLAGS=-pthread
DESTDIR=/usr
```

```makefile
COMPILE=$(CXX) $(CPPFLAGS) $(CXXFLAGS) $(DEFINES)
LINK=$(CXX)

WHAT=UNRAR

UNRAR_OBJ=filestr.o recvol.o rs.o scantree.o qopen.o
LIB_OBJ=filestr.o scantree.o dll.o qopen.o

OBJECTS=rar.o strlist.o strfn.o pathfn.o smallfn.o global.o file.o filefn.o filcreat.o \
	archive.o arcread.o unicode.o system.o crypt.o crc.o rawread.o encname.o \
	resource.o match.o timefn.o rdwrfn.o consio.o options.o errhnd.o rarvm.o secpassword.o \
	rijndael.o getbits.o sha1.o sha256.o blake2s.o hash.o extinfo.o extract.o volume.o \
	list.o find.o unpack.o headers.o threadpool.o rs16.o cmddata.o ui.o

.cpp.o:
	$(COMPILE) -D$(WHAT) -c $<
```

Now we’ll revise the makefile to let it suit our tool chain. Before that, we need to know:

* `CXX` means the compiler being used. It’ll be `clang++` for a-Shell.
* `CXXFLAGS` and `DEFINES` means the options of the compiler.
* `-O2` means O2 optimization, working with `clang++`.
* `-Wno-logical-op-parentheses -Wno-switch -Wno-dangling-else` will be not needed.
* `-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DRAR_SMP` is for 32-bit systems to deal with large files. For a 64-bit system, it‘s useless but harmless.
* `/usr` won’t be accessible on a-Shell. Actually `~/Library` acts as `/usr` so it‘ll be used instead.
* `-fPIC` is means Position Independent Code for dynamic link libraries, working with `clang++`.
* `-pthread` means multiple threads, and is not provided by WebAssembly yet, so it doesn’t work with a-Shell.

Then the makefile can be revised to:

```makefile
# a-Shell using clang++
CXX=clang++
CXXFLAGS=-O2
LIBFLAGS=-fPIC
DEFINES=-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DRAR_SMP
STRIP=strip
AR=ar
LDFLAGS=
DESTDIR=~/Library
...
```

Now let’s try to compile it:

```bash
$ make
```

{% hint style="info" %}
Actually this project does not work due to lack of APIs provided by WASI. We are looking for a project that the source code does work with a-Shell’s own tool chain. If you know one, please let us know.
{% endhint %}


# lets-do-more-for-it/submit-new-packages.md

# Submit new packages

Sometimes you want to release your projects to the `pkg` repository so that everyone can use it. So far the most packages are distributed in WebAssembly, but actually almost everything running well with a-Shell can be released(except native binary codes). This article focus on making a project ready for being released at the `pkg` repository.

### The structure of a package

The offical repository is stored at [https://github.com/holzschu/a-Shell-commands](https://github.com/holzschu/a-Shell-commands). To prepare a package, three parts are needed: the install script, the man page and the uninstall script. Let’s see an example `expand`.

Here is its install script:

```bash
#! /bin/sh
# Default install file for packages:

packagename=${0##*/}

# download command:
curl -L https://github.com/holzschu/a-Shell-commands/releases/download/0.1/$packagename -o ~/Documents/bin/$packagename --create-dirs --silent
chmod +x ~/Documents/bin/$packagename
# download man page
curl -L https://raw.githubusercontent.com/holzschu/a-Shell-commands/master/man/man1/$packagename.1 -o ~/Library/man/man1/$packagename.1 --create-dirs --silent
# refresh man database
mandocdb ~/Library/man
# download uninstall information:
curl -L https://raw.githubusercontent.com/holzschu/a-Shell-commands/master/uninstall/$packagename -o ~/Documents/.pkg/$packagename --create-dirs --silent
```

The install script downloads the binary file (scripts sometimes) to `~/Documents/bin/` or `~/Library/bin/` that is stored at `$PATH`, then gets the man page, refreshes the man database,and finally downloads the uninstall script. The binary file(s) can be stored at a repository (anywhere in fact) and for a single command it can be parsed with `curl`. Here’s it’s uninstall script:

```bash
#! /bin/sh

# Default uninstall file for packages:
packagename=${0##*/}

# remove command
rm ~/Documents/bin/$packagename
# remove man page
rm ~/Library/man/man1/$packagename.1
# refresh man database
mandocdb ~/Library/man
```

The uninstall script just clears everything about the package: the binary file, and the man page. For a more comlex project, remember to remove any app data by your package.

Now we have clarified: an install script is needed for `pkg install` to execute while an uninstall script is needed as well, except it is for `pkg uninstall`. Usually the man page is also needed although it isn't required because it isn't always necessary. The install script is stored at the repository and it indicates where the other parts of the package are stored at.

### An example

{% hint style="warning" %}
This part is unstable. You may meet problems running Perl scripts and submitting directories.
{% endhint %}

`cowsay` is an old and famous project written in Perl. To have it installed, we may clone the GitHub mirror repository first:

```
$ lg2 clone https://github.com/schacon/cowsay
```

We can see there is an `install.sh` on the repository. Actually it does not work with a-Shell and `dash` while it’s not essential. We’ll rewrite the installation script for it.

`install.sh` searches for if Perl exists on the computer which is not necessary for a-Shell so this part will not be used. According to the file `MANIFEST` of the repository, the project has the following files:

```
ChangeLog		Changes to recent versions.
INSTALL			Instructions for installing cowsay.
LICENSE			The license for use and redistribution of cowsay.
MANIFEST		This file.
README			Read this first.  Really.
Wrap.pm.diff		Diff for Text/Wrap.pm.
cows/*			Support files used by cowsay.
cowsay			Main cowsay executable.
cowsay.1		Main cowsay manual page.
install.sh		cowsay installation script.
pgp_public_key.txt	Verify the signature file with this key.
```

Among them, three files are important:

* `cowsay`, a script written in Perl, the most important executable file
* `cows/*`, a directory storing the source files used by `cowsay`
* `cowsay.1`, the man page (`man1`) of `cowsay`

The file ending with a single number is the man page here. We just put it into the corresponding `man` directory according to its number. For example, `*.1` files can be stored at the directory `man/man1`.

These files will be copied to where they should be on the computer, `/usr/local/bin` for `cowsay` and `/usr/local/share` for `cows/*`. as what `install.sh` tells us. According to the unique file system of a-Shell, `/usr` will be replaced into `~/Library`. For `cowsay.1`, we'll copy it to `~/Library/man/man1/$packagename.1` just like other packages. Thus, our `install.sh` may seems like this (not considering `cows/*`):

```sh
#!/bin/sh
# install script for cowsay

packagename=${0##*/}

# download command:
curl -L <somewhere> -o ~/Documents/bin/$packagename --create-dirs --silent
chmod +x ~/Document/bin/$packagename
# download man page
curl -L https://raw.githubusercontent.com/holzschu/a-Shell-commands/master/man/man1/$packagename.1 -o ~/Library/man/man1/$packagename.1 --create-dirs --silent
# refresh man database
mandocdb ~/Library/man
# download uninstall information
curl -L https://raw.githubusercontent.com/holzschu/a-Shell-commands/master/uninstall/$packagename -o ~/Documents/.pkg/$packagename --create-dirs --silent
```

There are two assumptions here:

* The executable file is available from GitHub Release. You either let `holzschu` to release it, or fork it to your own account and then release it there.
* The script will be availabe ONCE it's merged into the original repository as the script is trying to get the files from it. It won't work if the files can not be found from the original repository.

Now let's consider `cow/*`. It can be packed into a `tar` archive and be released. Now our script looks like this:

```
```

The uninstall script will be much more simple——it just deletes the files related to the program.

```bash
#! /bin/sh

# Default uninstall file for packages:
packagename=${0##*/}

# remove command
rm ~/Documents/bin/$packagename
# remove "cows"
rm -r ~/Library/local/share/cows
# remove man page
rm ~/Library/man/man1/$packagename.1
# refresh man database
mandocdb ~/Library/man
```

Put the scripts and the man pages to the repository by the file structure of it:

```
a-shell-commands
├─man
│ ├─man1
│ │ ├─others
│ │ └─cowsay.1 # the man page
│ └─man6
├─packages
│ ├─others
│ └─cowsay # the install script
├─uninstall
│ ├─others
│ └─cowsay # the uninstall script
├─list
├─pkg
└─README.md
```

Then add the word `cowsay` into the file `list`:

```
...
column
comm
cowsay
csplit
cut
...
```

Release the excutable file `cowsay` and the directory `cows`, commit your changes, synchronize it to the remote server, and open a Pull Request finally. That's all you need to do to submit a new package.


# lets-do-more-for-it/webassembly-for-a-shell.md

# WebAssembly for a-Shell

{% hint style="warning" %}
This article is unstable.
{% endhint %}

### What is WebAssembly and how it works with a-Shell?

Due to Apple's safety policy, external binary codes outside of the app itself are forbidden to run. Thus theoretically there won't be a compiler for iOS/iPadOS that we can run and test the codes generated by it conveniently. What C/C++ compiler inside both a-Shell and Code App generates are not iOS/iPadOS native binary files but WebAssembly object codes. With the WebAssembly runtime environment, we can test the codes we write. But what is WebAssembly and why it's chosen to work with the C/C++ compiler?

As the speed of JavaScript is slow, some people hope there can be a technology that can introduce low-level program languages to the web browser, thus WebAssembly is born. It seems to be a kind of new "programming language" but actually it's a kind of object code that can be executed on different architectures and systems, and it's well-known for its safety and efficiency.

As some people have noticed WebAssembly's features, they guess it can be used to write cross-platform projects. Thus, there should be a runtime like Java to provide a way to run WebAssembly codes outside of the browser, which is called `wasi` later. WASI itself can be ported to any platforms and it provides a set of APIs for wasm programs. In a word, when a program claims it supports WebAssembly, it may be designed for two cases: either browser environments, or a kind of cross-platform runtime called `wasi`. When a program works with `wasi`, it can certainly be ported to a-Shell.

WASI built-in with a-Shell is specialized. standard `wasi-libc` only allows WebAssembly programs to read from the standard input and write to the standard output. More system calls like reading and writing files and getting directory contents have been added to a-Shell's WASI, but it still has many limits:

* No process-associated clocks. If you try to compile a program that uses `getrusage()`, there will be an explicit warning telling you to use `-D_WASI_EMULATED_PROCESS_CLOCKS` and `-lwasi-emulated-process-clocks`.
* No signal functions. Again, there will be a warning telling you to use: `-D_WASI_EMULATED_SIGNAL` and link with `-lwasi-emulated-signal`.
* No mmap function. There will be a warning telling you to use: `-D_WASI_EMULATED_MMAN` and link with `-lwasi-emulated-mman`.

There is also no `setjmp()/longjmp()`, no `fork()`, and no threads (and no ways to emulate them. There are threads in some versions of webAssembly, but they require a server, not something running locally).

WASI supports threads experimentally via web workers. For web-based projects, web workers are enabled only when the server has set certain flags. For local side, we don't know how to enable it. Apple has disabled it for security reasons.

The ecosystem of WebAssembly is still embarrassed. As a new-born technology, it has been developed for years but its usage outside of the web browser is still greatly limited.

### Cross compile WebAssembly projects with your computer

You can compile projects to WebAssembly not only with a-Shell's own tool chain, but also with a-Shell's specialized `wasi-sdk`: [https://github.com/holzschu/wasi-sdk](https://github.com/holzschu/wasi-sdk), where extra functions like reading or writing files are provided. What's more, normal `wasi-sdk` also works with a-Shell theoretically. See also [https://github.com/WebAssembly/wasi-sdk](https://github.com/WebAssembly/wasi-sdk) for more technical details.

WASI API still continues updating (although VERY SLOW) so new functions may be added in the future in time.

# ended.md

# Ended?

Of course not!

As you can see, many parts are not finished yet! This doc is still in progress and everyone is welcomed to have everything completed, fix errors or share ideas. See [contribute-to-the-book.md](contribute-to-the-book.md "mention") for more information.

### Our current works

* Have [submit-new-packages.md](lets-do-more-for-it/submit-new-packages.md "mention") finished. The `install.sh` should be polished currently.
* Finish the progress of compiling native codes. A Mac is needed!
* Seek for an experienced guy to finish [run-jupyter.md](basic-tutorials/run-jupyter.md "mention").
* Try to talk about the ecosystem of WebAssembly clearly.
* Research on `node.js`, `bun` and `jsc`. Find a way to import JavaScript modules conveniently.
