# 预习 Day1：第一个大模型对话程序
import os  # 用于读取系统环境变量
import requests  # 用于发送 HTTP 请求
from dotenv import load_dotenv  # 用于加载 .env 文件中的环境变量

# 加载环境变量，使程序可以通过 os.getenv 读取 .env 文件里的变量
load_dotenv()

# 定义一个函数，用于将用户输入发送给 AI 聊天接口并返回回复
def chat_with_ai(user_input):
    # 从环境变量中读取 API 密钥
    api_key = os.getenv("ARK_API_KEY")
    # 目标接口地址，这里使用 ARK 聊天完成接口
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

    # 准备请求头，包含授权信息和请求内容类型
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 准备请求主体，指定模型和用户消息
    data = {
        "model": "doubao-1.5-pro",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    # 发送 POST 请求，json 参数传递请求数据，headers 参数传递请求头
    response = requests.post(url, json=data, headers=headers)
    # 将服务器返回的 JSON 字符串解析为 Python 字典
    res_json = response.json()
    # 从返回结果中取出 AI 的回复内容并返回
    return res_json["choices"][0]["message"]["content"]

# 当模块作为脚本直接执行时，运行以下代码
if __name__ == "__main__":
    # 启动提示
    print("🎉 AI 聊天机器人已启动（输入退出结束）")
    while True:
        # 读取用户输入
        msg = input("你：")
        # 如果用户输入退出关键词，则结束循环
        if msg in ["退出", "exit", "quit"]:
            print("👋 程序结束")
            break
        # 调用聊天函数获取 AI 回复
        reply = chat_with_ai(msg)
        # 打印 AI 回复并换行分隔
        print("AI：", reply, "\n")