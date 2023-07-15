# 导入Tkinter模块
import tkinter as tk
import re

# 定义替换规则
patterns = [
    (r'\bBRB\b', 'bear body'),
    (r'\bTTR\b', 'tight trading range'),
    (r'\bOB\b', 'outside bar'),
    (r'\bIB\b', 'inside bar'),
    (r'\bFBO\b', 'failed breakout'),
    (r'\bMTR\b', 'major trend reversal'),
    (r'\bPW\b', 'parabolic wedge'),
    (r'\bL2\b', 'low 2'),
    (r'\bHOD\b', 'high of today'),
    (r'\bLOD\b', 'low of today'),
    (r'\bHPW\b', 'wait for higher probability'),
    (r'\bBRE2\b', 'bear exit above'),
    (r'\bBRE4\b', 'bear exit above'),
    (r'\bBOP\b', 'breakout point'),
    (r'\bSPBR\b', 'surprise bear bar'),
    (r'\bPP\b', "60% or higher probability"),
    (r'\bS\b', 'bear bar'),
    (r'\bSB\b', 'seller below'),
    (r'\bPS\b', 'lower than 50% probability'),
    (r'\bMGB\b', 'magnet below'),
    (r'\bMMD\b', 'measured move down'),
    (r'\bY\b', 'yesterday'),
    (r'\bBO\b', 'breakout'),
    (r'\bLOY\b', 'low of yeste/rday'),
    (r'\bREV\b', 'reversal'),
    (r'\bBR\b', 'bears'),
    (r'\bCH\b', 'channel'),
    (r'\bDD\b', 'doji'),
    (r'\bBL\b', 'bulls'),
    (r'\bBRN\b', 'big round number'),
    # (r'\bSS\b', 'sell signal'),
    # (r'\bBL\b', 'bulls'),
    (r'\bSBDM\b', 'surprise bears dominant major trend'),
    (r'\bSBU\b', 'Surprisingly big bulls'),
    (r'\bPL\b', "50% or lower probability"),
    (r'\bS2\b', "Weak Trader's Equation wait for higher probability sell"),
    (r'\bSS2\b', "Weak Trader's Equation so higher probability to wait for a 2nd sell signal or for a strong bear breakout, which means 2 or 3 bear bars closing near their lows; or, need wide stop and better if can scale in."),
    (r'\bBL\b', "bulls"),
    (r'\bSC\b', 'spike and channel'),
    (r'\bPTG\b', 'profit taking'),
    (r'\bBRTP\b', 'bear trap, failed bear breakout'),
    (r'\bSTC\b', 'sell the close'),
    (r'\bMRV\b', 'minor reversal '),
    (r'\bBUDC\b', 'BUDC 60% probability of trading range'),
    (r'\bNS\b', 'Not high enough probability for stop entry traders to scalp'),
    (r'\bMBO\b', 'Minor Breakout, 60% will last 1-5 bars'),
    (r'\bNWS\b', "need wide stop"),
    (r'\bBBRBC\b', "big bear bar Closing near its low"),
    (r'\bBRCH\b', "bear channel"),
    (r'\bNWS\b', "need wide stop"),

 #   (r'\b\b', ""),
    (r'\bTGT\b', "target"),
    (r'\bBR\b', "bears"),
    (r'\bSP\b', "support"),
    (r'\bTR\b', "trading range"),
    (r'\bSCBR\b', "Spike and Channel Bear Trend, at least 2 legs down, often in a wedge bottom"),
    (r'\bSPBR\b', "Small PullBack Bear trend. Most pullbacks are small and only last 1 or 2 bars. 60% or higher probability sellers above prior bar."),
    (r'\bW\b', "wedge,or anything similar, like any 3 push pattern"),
    (r'\bREVU\b', "reversal up"),
    (r'\bBLD\b', "bull doji"),
    (r'\bMW\b', "micro Wedge, a wedge formed by only 3 - 4 bars"),
    (r'\bMDRU\b', "Midday reversal up is a bull trend reversal in the middle of the day, sometimes exactly at bar 40 or 41, and sometimes leads to bull trend for rest of day"),
    (r'\bCCBRBC\b', "Consecutive Big Bear Bars Closing near their lows makes at least a small 2nd leg down likely"),
    (r'\bLBLM\b', "Limit order Bull scalpers have been making Money, which increases chance of trading range"),
    (r'\bLPS\b', "Low Probability Short, probably buyers below, and sideways more likely than down"),
    (r'\bNS\b', "Not high enough probability for stop entry traders to scalp, but reward can be big enough compared to risk to offset low probability so ok swing trade. 50% probability will not get strong move, and disappointed traders will scalp out."),
    (r'\bCCBBRBC\b', "Consecutive Big Bear Bars Closing near their lows makes at least a small 2nd leg down likely"),
    (r'\bBBBR\b', "Big Bar or Bars so Big Risk. If you take the trade, trade small enough position size so that the risk of the trade is no bigger than on any other trade. If in Tight TR, better to wait for breakout or 2nd signal since low probability, bad for stop entries."),
    # (r'\bG\b', "gap"),
    (r'\bOU\b', "outside up bar"),
    (r'\bFT\b', "follow through"),
    (r'\bRB\b', "Reversal Bar."),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', ""),
    # (r'\b\b', "")
]

# 定义替换函数
def replace_text():
    # 获取输入文本
    input_text = input_textbox.get("1.0", "end-1c")
    # 替换指定字符串
    output_text = input_text
    for pattern, replacement in patterns:
        output_text = re.sub(pattern, replacement, output_text)
    # 显示输出文本
    output_textbox.delete("1.0", "end")
    output_textbox.insert("1.0", output_text)

# 定义编辑规则函数
def edit_rules():
    # 弹出一个新窗口，显示当前的替换规则
    rules_window = tk.Toplevel(root)
    rules_window.title("Edit Rules")
    rules_window.geometry("400x300")
    rules_label = tk.Label(rules_window, text="Current Rules:")
    rules_label.pack()
    rules_listbox = tk.Listbox(rules_window)
    for pattern, replacement in patterns:
        rules_listbox.insert("end", f"{pattern} -> {replacement}")
    rules_listbox.pack()
    # TODO: 添加添加，删除，修改规则的功能

# 创建主窗口
root = tk.Tk()
root.title("Text Replacer")
root.geometry("700x500")

# 创建输入文本框
input_label = tk.Label(root, text="Input Text:")
input_label.pack()
input_textbox = tk.Text(root)
input_textbox.pack(side="left", fill="both", expand=True)

# 创建输出文本框
output_label = tk.Label(root, text="Output Text:")
output_label.pack()
output_textbox = tk.Text(root)
output_textbox.pack(side="right", fill="both", expand=True)

# 创建替换按钮
replace_button = tk.Button(root, text="Replace", command=replace_text)
replace_button.pack()

# 创建编辑规则按钮
edit_button = tk.Button(root, text="Edit Rules", command=edit_rules)
edit_button.pack()

# 进入主循环
root.mainloop()