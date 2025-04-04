<!-- markdownlint-disable MD031 MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/LuoChu-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# nonebot-plugin-noadpls

_✨ NoneBot 插件简单描述 ✨_

<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/badge/pdm-managed-blueviolet" alt="pdm-managed">
</a>
<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb.svg" alt="wakatime">
</a>

<br />

<!-- <a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v1.json" alt="Pydantic Version 1" >
</a> -->
<!-- <a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json" alt="Pydantic Version 2" >
</a> -->
<a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/pyd-v1-or-v2.json" alt="Pydantic Version 1 Or 2" >
</a>
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/LuoChu-NB2Dev/nonebot-plugin-noadpls.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-noadpls">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-noadpls.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-noadpls">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-noadpls" alt="pypi download">
</a>

<br />

<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-noadpls:nonebot_plugin_noadpls">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin%2Fnonebot-plugin-noadpls" alt="NoneBot Registry">
</a>
<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-noadpls:nonebot_plugin_noadpls">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin-adapters%2Fnonebot-plugin-noadpls" alt="Supported Adapters">
</a>

</div>

这是一个 nonebot2 插件项目的模板库, 你可以直接使用本模板创建你的 nonebot2 插件项目的仓库

模板库使用方法:

1. 点击仓库中的 `Use this template` 按钮, 输入仓库名与描述, 点击 `Create repository from template` 创建仓库
2. 全局替换 `nonebot-plugin-noadpls` 为插件名;  
   全局替换 `nonebot_plugin_noadpls` 为包名;  
   修改 python 徽标中的版本为你插件的运行所需版本;  
   替换 WakaTime 的徽标
3. 修改 `README.md` 中的插件名和插件描述, 并在下方填充相应的内容

## 📖 介绍

这里是插件的详细介绍部分

## 💿 安装

以下提到的方法 任选**其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-noadpls
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-noadpls
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-noadpls
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-noadpls
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-noadpls
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_noadpls"
]
```

</details>

## ⚙️ 配置

在 nonebot2 项目的 `.env` 文件中添加下表中的必填配置

|  配置项  | 必填 | 默认值 |   说明   |
| :------: | :--: | :----: | :------: |
| 配置项 1 |  是  |   无   | 配置说明 |
| 配置项 2 |  否  |   无   | 配置说明 |

## 🎉 使用

### 指令表

|  指令  | 权限 | 需要@ | 范围 |   说明   |
| :----: | :--: | :---: | :--: | :------: |
| 指令 1 | 主人 |  否   | 私聊 | 指令说明 |
| 指令 2 | 群员 |  是   | 群聊 | 指令说明 |

### 效果图

如果有效果图的话

## 📞 联系

QQ：3214528055  
Discord：[@洛初](https://discordapp.com/users/959299637049700355)  
Telegram：[@Furinature](https://t.me/Furinature)  
吹水群：[611124274](https://qm.qq.com/q/BS2k2XIfxS)  
邮箱：<gongfuture@outlook.com>

## 💡 鸣谢

如果有要鸣谢的人的话

## 💰 赞助

**[赞助我](https://afdian.com/a/luochu)**

感谢大家的赞助！你们的赞助将是我继续创作的动力！

## 📝 更新日志

芝士刚刚发布的插件，还没有更新日志的说 qwq~
