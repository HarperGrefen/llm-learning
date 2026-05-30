import os
from dotenv import load_dotenv
from volcenginesdkarkruntime import Ark

# ==============================================
# 加载环境变量（你只需要配置 .env 文件即可）
# ==============================================
load_dotenv()

# ==============================================
# 初始化火山方舟客户端（使用 AK/SK 鉴权）
# ==============================================
client = Ark(
    ak=os.getenv("VOLC_AK"),
    sk=os.getenv("VOLC_SK"),
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

# ==============================================
# 多轮对话历史
# ==============================================
messages = []

print("=" * 60)
print("🔥 火山引擎 豆包 Deep 2.0 Lite 聊天界面")
print("✅ 已连接：你的推理端点")
print("💬 输入内容聊天，输入【退出】结束程序")
print("=" * 60)

# ==============================================
# 循环聊天
# ==============================================
while True:
    # 输入你的问题
    user_input = input("\n你：")

    # 退出条件
    if user_input.strip() == "退出":
        print("\nAI：再见！期待下次和你聊天～")
        break

    # 把用户消息加入历史
    messages.append({"role": "user", "content": user_input})

    try:
        # 调用豆包 API
        completion = client.chat.completions.create(
            model=os.getenv("ARK_ENDPOINT_ID"),  # 你的 ep-xxxx
            messages=messages,
            temperature=0.7,
            max_tokens=2000
        )

        # 获取 AI 回复
        ai_reply = completion.choices[0].message.content

        # 显示回复
        print("\nAI：", ai_reply)

        # 把 AI 回复加入历史（实现上下文记忆）
        messages.append({"role": "assistant", "content": ai_reply})

    except Exception as e:
        print("\n❌ 调用出错：", str(e))
        print("请检查 AK/SK/端点ID 是否正确")