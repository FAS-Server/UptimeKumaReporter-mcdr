# Mount

![MCDReforged](https://img.shields.io/badge/dynamic/json?label=MCDReforged&query=dependencies.mcdreforged&url=https%3A%2F%2Fraw.githubusercontent.com%2FFAS-Server%2FUptimeKumaReporter-mcdr%2Fmaster%2Fmcdreforged.plugin.json&style=plastic) ![license](https://img.shields.io/github/license/FAS-Server/UptimeKumaReporter-mcdr?style=plastic) ![build status](https://img.shields.io/github/workflow/status/FAS-Server/UptimeKumaReporter-mcdr/CI%20for%20MCDR%20Plugin?label=build&style=plastic) ![Release](https://img.shields.io/github/v/release/FAS-Server/UptimeKumaReporter-mcdr?style=plastic) ![total download](https://img.shields.io/github/downloads/FAS-Server/UptimeKumaReporter-mcdr/total?label=total%20download&style=plastic)

**简体中文** | **[English](README_en.md)**

> 一个向UptimeKuma上报服务器运行状况的插件。


## 使用说明

1. 在 UptimeKuma 的控制台, 添加一个类型为 `Push` 的监控项，并拷贝其推送 URL。
2. 将此插件放置在插件目录下 (通常是 `plugins`)。
3. 在 `config/uptime_kuma_reporter/config.json` 写入配置文件。
4. 加载此插件。

## 配置文件
```json5
{
  // 监控项的推送地址，记得删掉 `？` 之后的参数
  // 例如  https://example-uptimekuma.site/api/push/abcdefg?status=up&msg=OK&ping=
  // ---> https://example-uptimekuma.site/api/push/abcdefg
  "url": "https://example.com",
  // 推送的间隔, 默认是 60 秒
  "interval": 60,
  // 是否在推送时输出日志, 默认为 False
  "log_push": false
}
```
