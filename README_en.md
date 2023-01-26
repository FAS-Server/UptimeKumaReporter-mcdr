# UptimeKuma Reporter for MCDR

![MCDReforged](https://img.shields.io/badge/dynamic/json?label=MCDReforged&query=dependencies.mcdreforged&url=https%3A%2F%2Fraw.githubusercontent.com%2FFAS-Server%2FUptimeKumaReporter-mcdr%2Fmaster%2Fmcdreforged.plugin.json&style=plastic) ![license](https://img.shields.io/github/license/FAS-Server/UptimeKumaReporter-mcdr?style=plastic) ![build status](https://img.shields.io/github/workflow/status/FAS-Server/UptimeKumaReporter-mcdr/CI%20for%20MCDR%20Plugin?label=build&style=plastic) ![Release](https://img.shields.io/github/v/release/FAS-Server/UptimeKumaReporter-mcdr?style=plastic) ![total download](https://img.shields.io/github/downloads/FAS-Server/UptimeKumaReporter-mcdr/total?label=total%20download&style=plastic)

**[简体中文](README.md)** | **English**

> A plugin that report server status to uptimekuma.

## Usage

1. In UptimeKuma dashboard, add monitor with the type of `Push`, and copy the Push URL.
2. Add this plugin in your plugin folder (usually `plugins`)
3. Add config in `config/uptime_kuma_reporter/config.json`
4. Load this plugin.

## Config
```json5
{
  // Push URL of the monitor, remember to remove params after `?`
  // e.g. https://example-uptimekuma.site/api/push/abcdefg?status=up&msg=OK&ping=
  // ---> https://example-uptimekuma.site/api/push/abcdefg
  "url": "https://example.com",
  // push interval, default to 60s
  "interval": 60,
  // print log when push status, default to False
  "log_push": false
}
```
