# Claude Code با گیسو

Claude Code (ابزار خط فرمان و افزونهٔ VS Code ساخت Anthropic) با کلید گیسو کار می‌کند، چون نشانی گیسو Messages API
شرکت Anthropic را می‌فهمد. کلید را در [بخش API اپ گیسو](https://gisoo.pro/app/api?utm_source=github&utm_medium=referral&utm_campaign=gisoo&utm_content=claude-code) بسازید.

| فایل | کجا |
|---|---|
| [`env.sh`](env.sh) | bash و zsh، فقط برای همان پنجره: `source claude-code/env.sh && claude` |
| [`env.ps1`](env.ps1) | PowerShell در ویندوز: `. .\claude-code\env.ps1` و بعد `claude` |
| [`settings.json`](settings.json) | همیشگی: بخش `env` را در `~/.claude/settings.json` بگذارید و کلید را عوض کنید |
| [`vscode-settings.json`](vscode-settings.json) | افزونهٔ Claude Code در VS Code: این خط را به تنظیمات VS Code اضافه کنید تا ورود به حساب Anthropic نخواهد، بعد پنجره را دوباره بارگذاری کنید (Developer: Reload Window) |

- نشانی را **بدون** `/v1` بگذارید: `https://gisoo.pro/api`.
- نام‌هایی مثل `claude-sonnet-5-5`، `claude-opus-5-5` و `claude-haiku-4-5` (با یا بدون تاریخ) کار می‌کنند؛ نامی که با `[1m]` تمام شود شناخته نمی‌شود.
- جست‌وجوی وب داخلی Claude Code از راه گیسو کار نمی‌کند و «thinking» نادیده گرفته می‌شود.
- می‌توانید کلید را از دکمهٔ «مدل‌های مجاز» فقط به مدل‌های Claude محدود کنید و برایش سقف هزینه بگذارید.

راهنمای کامل: [gisoo.pro/docs/anthropic](https://gisoo.pro/docs/anthropic?utm_source=github&utm_medium=referral&utm_campaign=gisoo&utm_content=claude-code) ·
آموزش قدم‌به‌قدم در VS Code: [gisoo.pro/blog/claude-code-vscode-gisoo](https://gisoo.pro/blog/claude-code-vscode-gisoo?utm_source=github&utm_medium=referral&utm_campaign=gisoo&utm_content=claude-code) ·
فیلم ساخت کلید: [gisoo.pro/tutorials/api-key](https://gisoo.pro/tutorials/api-key?utm_source=github&utm_medium=referral&utm_campaign=gisoo&utm_content=claude-code)

**English:** set `ANTHROPIC_BASE_URL=https://gisoo.pro/api` (no `/v1`) and `ANTHROPIC_AUTH_TOKEN=<your sk-gisoo-v1 key>`,
pick models like `claude-sonnet-5-5`, and for the VS Code extension add `"claudeCode.disableLoginPrompt": true`.
