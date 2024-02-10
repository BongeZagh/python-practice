import tkinter as tk
import openai

# 创建主窗口
window = tk.Tk()
window.title("OpenAI API 流量监控")

# 创建标签来显示流量余额和当日使用量
balance_label = tk.Label(window, text="流量余额：")
balance_label.pack()

usage_label = tk.Label(window, text="当日使用量：")
usage_label.pack()

# 创建输入框和标签来输入和显示 API 密钥
api_key_label = tk.Label(window, text="API 密钥：")
api_key_label.pack()

api_key_entry = tk.Entry(window)
api_key_entry.pack()

# 获取账户信息函数
def get_account_info():
    # 获取输入框中的 API 密钥
    api_key = api_key_entry.get()

    # 设置 OpenAI API 密钥
    openai.api_key = api_key

    try:
        # 获取账户信息
        balance = openai.Account.balance()
        usage = openai.Account.usage()

        # 更新标签文本
        balance_label.config(text="流量余额：" + str(balance['total']))
        usage_label.config(text="当日使用量：" + str(usage['usage']))
    except Exception as e:
        balance_label.config(text="获取账户信息出错：" + str(e))
        usage_label.config(text="")

# 创建按钮来触发获取账户信息函数
button = tk.Button(window, text="获取账户信息", command=get_account_info)
button.pack()

# 运行主循环
window.mainloop()

