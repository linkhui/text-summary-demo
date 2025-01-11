import os
import gradio as gr
import openai  # 旧版本导入方式

# 旧版本 API 初始化方式
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com"

def summarize_text(text):
    """
    调用Deepseek API生成文本摘要
    """
    if not text.strip():
        return "请输入需要总结的文本"
        
    try:
        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个专业的文本摘要助手。请对用户输入的文本进行简洁的总结，突出重点内容。"},
                {"role": "user", "content": f"请总结以下文本：\n\n{text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"发生错误: {str(e)}"

# 创建Gradio界面
demo = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, label="输入文本"),
    outputs=gr.Textbox(label="摘要结果"),
    title="文本摘要生成器",
    description="输入长文本，获取AI生成的摘要",
)

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1", 
        server_port=7860,
        root_path="/summarize"
    )