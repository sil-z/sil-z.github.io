---
layout: default
title: "杂项 / 便签"
author: "Silhouette"
permalink: /other/
---

  <div class="tags-header">
    <h2 class="tags-header-title">杂项</h2>
    <div class="tags-header-line"></div>
  </div>

展示你的专辑列表：[Topsters 3](https://topsters.org/)

我的专辑列表（2025）：

![my_chart.png](/assets/images/my_chart.png)

## 书法网站

- 练习格线生成器：[lanquach.com](https://lanquach.com/)
- The Zanerian Manual 教材 @loc.gov：[The Zanerian Manual](https://www.loc.gov/item/18009979/)
- The Universal Penman 教材 @loc.gov：[The Universal Penman](https://www.loc.gov/item/11026301/)
- Scranton 大学图书馆：[digitalservices.scranton.edu](https://digitalservices.scranton.edu/digital/collection/zanerbloser/search)

## Windows 系统重装步骤

- 有以下几种渠道获取系统安装镜像：使用 UUP dump 获取 Windows 系统镜像；msdn.itellyou.cn 的文件必须使用 P2P 下载器，国外似乎无法下载；从微软官方下载 ISO 文件，最稳定，但完全无法下载旧版。
- 使用除 Windows 系统之外的系统登录 microsoft.com/en-us/software-download/windows10，或者进入浏览器开发者工具 -> 更多工具 -> Network conditions 中将 User agent 改成 Chrome - Mac 或者随便其他什么版本，总之不能是 Windows，即可在这个页面中下载最新的 Windows 10 ISO 文件。使用 Rufus 创建启动盘，使用 Microsoft Activation Scripts (MAS) 激活。
- 使用专业版比较合适，企业版也可以；不建议用奇怪的版本，可能出现不可预知的问题。
- 安装系统时断开网络连接；安装完 Windows 系统之后跑一遍更新并确保驱动没有问题，之后使用 github.com/tsgrgo/windows-update-disabler 禁用自动更新；驱动有问题时去硬件（笔记本电脑）官方网站找对应版本，无法解决时重装，这在隔离了用户文件的情况下不应耗时；不下载 360 驱动等工具的原因是由于软件功能需求使用时必须给联网权限，且不能保证将其完全从电脑上清除；适当对系统和软件进行手动更新。
- 新电脑在重装前必须确保 BitLocker 已经关闭。

## 必需软件
- 从 github.com/henrypp/simplewall 下载联网控制工具，默认禁用所有软件的联网功能
- Everything，文件索引工具，非开源软件
- 从 github.com/Xanashi/Icaros 下载媒体文件预览工具，非开源软件
- 从 dl.google.com/pinyin/v2/GooglePinyinInstaller.exe 下载谷歌拼音输入法，该输入法已下架，链接可能随时消失，非开源软件 
- 从 github.com/rime/weasel 下载小狼毫输入法
- 从 nomacs.org 下载 nomacs 图片查看器
- 从 peazip.github.io 下载 PeaZip 压缩和解压软件
- 从 github.com/clsid2/mpc-hc 下载 Media Player Classic 视频播放器
- SumatraPDF，用于各种文档查看
- WireGuard，VPN 软件，使用 protonvpn.com 提供的免费服务
- 从 learn.microsoft.com/en-us/sysinternals/downloads/autoruns 下载启动项管理工具

## 浏览器工具
- 从 github.com/ungoogled-software/ungoogled-chromium 下载纯净的 Chromium 浏览器
- 从 github.com/xifangczy/cat-catch 下载猫抓插件，用于网页视频和音频抓取
- 从 github.com/NeverDecaf/chromium-web-store 下载插件，使 Ungoogled Chromium 能够正常访问 Chrome 应用商店
- 安装 Free Download Manager 软件和浏览器插件，非开源软件
- 从 tampermonkey.net 下载篡改猴浏览器插件，从 greasyfork.org 获取脚本
- 从 github.com/Bistutu/FluentRead 下载浏览器翻译插件

## 可选软件
- 从 github.com/ashaduri/gsmartcontrol 下载 SSD 状态检测工具
- DiskGenius，磁盘工具，非开源软件
- LibreOffice，办公软件
- 从 veracrypt.io 下载 VeraCrypt，用于创建加密卷
- 从 github.com/microsoft/PowerToys 下载 Windows 系统工具集，这个其实没什么用
- OBS Studio，屏幕录制软件
- 从 mythicsoft.com/filelocatorpro 下载文件内容检索软件，非开源软件
- 从 jam-software.com/treesize 下载磁盘空间分析软件，非开源软件
- 从 github.com/WerWolv/ImHex 下载十六进制编辑器
- VMWare，虚拟机软件，非开源软件
- 从 fonts.google.com/noto 下载 Noto 字体
- GIMP，位图编辑软件
- Inkscape，矢量图编辑软件
- qBittorrent，P2P 下载器
- Sandboxie Plus，沙箱软件
- 从 github.com/marktext/marktext 下载 Markdown 编辑和格式转换器
- 从 github.com/microsoft/terminal 下载 Windows Terminal，微软特色，下载很容易莫名其妙失败，因此最好保留一份可用版本
- 从 github.com/VSCodium/vscodium 下载去微软的 VSCodium
- FFmpeg
- 从 github.com/hiroi-sora/Umi-OCR 下载 OCR 工具


## 一些操作步骤

当删除文件出现需要 TrustedInstaller 许可的警告时，以管理员权限运行 PowerShell，使用以下命令删除：

```
takeown /f <file_path> /r /d y
icacls <file_path> /grant administrators:F /t
Remove-Item <file_path> -Recurse -Force
```

---

系统搜索栏中有一个 Trending searches 的牛皮癣，清除方法：在注册表 Computer\HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer 下新建 DWORD 32 值，命名为 DisableSearchBoxSuggestions，值为 1

---

慎重在 Windows 文件资源管理器中使用 Ctrl + Z 撤回操作。如果新建了一个文件并编辑了内容，使用 Ctrl + Z 撤回新建文件的动作，将导致文件内容永久性丢失。重新使用 Ctrl + Y 只能重新创建一个空文件，原来编辑过的内容几乎无法找回。
