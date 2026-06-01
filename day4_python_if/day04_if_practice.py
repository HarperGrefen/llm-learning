# ========== 第4天：if 条件判断 ==========
token = 1000
model_name = "doubao"

print("=== 第1个判断 ===")
if token > 500:
    print("Token 充足，可以继续调用API")

print("\n=== 第2个判断 ===")
if token < 100:
    print("Token 不足，请检查")
else:
    print("Token 正常")

print("\n=== 第3个判断 ===")
if model_name == "doubao":
    print("当前使用豆包大模型")
else:
    print("使用其他模型")