# Deepseek LLM 文本摘要演示

一个基于 Gradio 的文本摘要应用，通过 Deepseek LLM API 实现智能文本总结功能。

## 功能特点

- 简洁的 Web 界面，支持长文本输入
- 基于 Deepseek 大语言模型的智能摘要
- 使用 OpenAI 兼容的 API 接口
- 支持 macOS 和 Ubuntu 16.04 ECS 部署

## 环境要求

- Python 3.7+
- OpenAI API Key (Deepseek)
- macOS 或 Ubuntu 16.04

## 快速开始

### 环境设置

### 创建虚拟环境
```bash
# 安装虚拟环境工具
python3 -m pip install virtualenv

# 创建虚拟环境
python3 -m virtualenv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate
# Windows:
# .\venv\Scripts\activate

# 退出虚拟环境
deactivate
```

### macOS 环境

1. 安装依赖
```bash
# 确保已激活虚拟环境
source venv/bin/activate

pip install -r requirements_macos.txt
```

2. 设置环境变量
```bash
export DEEPSEEK_API_KEY=your_api_key
```

3. 运行应用
```bash
python app_macos.py
```

### Ubuntu 16.04 ECS 环境

1. 安装依赖
```bash
# 确保已激活虚拟环境
source venv/bin/activate

pip install -r requirements_ecs_ubuntu.txt
```

2. 设置环境变量
```bash
export DEEPSEEK_API_KEY=your_api_key
```

3. 运行应用
```bash
python app_ecs_ubuntu.py
```

## 访问应用

应用启动后，在浏览器中访问：
- 本地环境：http://localhost:7860
- ECS 环境：https://www.yueduhezi.com/summarize/

## 版本说明

### macOS 版本
- `app_macos.py`: 使用最新版本 OpenAI SDK
- `requirements_macos.txt`: 最新依赖版本

### 阿里云ECS Ubuntu 版本
- `app_ecs_ubuntu.py`: 适配旧版本 OpenAI SDK
- `requirements_ecs_ubuntu.txt`: 特定版本依赖

#### Ubuntu 16.04 特别说明
由于系统限制：
- OpenSSL 版本为 1.0.2g，需要使用 urllib3 < 2.0.0
- 使用 OpenAI SDK 0.28.1 以避免兼容性问题
- Gradio 使用 3.50.2 版本以确保稳定性

## 部署建议

### 本地开发环境
推荐使用 macOS 版本，支持最新特性。

### 生产环境 (ECS)
1. 使用 Screen 后台运行
```bash
# 创建新的 screen 会话
screen -S text-summary

# 激活虚拟环境
source venv/bin/activate

# 运行应用
python app_ecs_ubuntu.py

# 分离会话：按 Ctrl+A，然后按 D

# 重新连接到会话
screen -r text-summary

# 查看所有会话
screen -ls
```

4. 配置安全组
- 开放 80 端口（HTTP）
- 开放 443 端口（HTTPS）
- 关闭 7860 端口（应用端口）
- 设置访问控制策略

## 技术栈

- [Deepseek API](https://api-docs.deepseek.com/)
- [Gradio](https://www.gradio.app)
- [OpenAI SDK](https://github.com/openai/openai-python)

## 常见问题

1. 依赖安装失败
   - macOS: 使用最新版本依赖
   - Ubuntu: 使用指定版本依赖

2. API 调用错误
   - 检查 API Key 设置
   - 确认网络连接

## 许可证

MIT License
