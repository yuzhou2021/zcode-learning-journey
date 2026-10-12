# -*- coding: utf-8 -*-
# 台账统计练习：参考答案（ledger_stats.py 的修复版，2026-09-22 补）
#
# 原题（ledger_stats.py）故意留了两处问题：
#   1) rec["amout"] 拼写错误，应为 rec["amount"]
#      —— 显性 bug：一运行就 KeyError，报错信息直接指出行号，容易定位
#   2) office_total 在循环内部被重置为 0.0，每遇到一条"办公"记录就清零一次
#      —— 隐性 bug：程序不报错、能跑完，但办公小计只等于最后一条办公记录（33.0）
#      累加变量的正确写法：循环外初始化一次，循环内只做累加
#
# 预期输出：总条数 6、总金额 1662.50、办公类小计 198.50、平均单笔 277.08

records = [
    {"name": "打印纸",     "category": "办公",   "amount": 120.0},
    {"name": "签字笔",     "category": "办公",   "amount": 45.5},
    {"name": "显示器",     "category": "设备",   "amount": 1299.0},
    {"name": "文件夹",     "category": "办公",   "amount": 33.0},
    {"name": "鼠标",       "category": "设备",   "amount": 89.0},
    {"name": "茶叶",       "category": "福利",   "amount": 76.0},
]

total = 0.0
office_total = 0.0            # 修复 2：初始化放在循环外，只做一次

for rec in records:
    total += rec["amount"]    # 修复 1：拼写 amout -> amount

    if rec["category"] == "办公":
        office_total += rec["amount"]   # 修复 2：只累加，不再重置

avg = total / len(records)

print("=== 台账统计结果 ===")
print(f"总条数：{len(records)} 条")
print(f"总金额：{total:.2f} 元")
print(f"办公类小计：{office_total:.2f} 元")
print(f"平均单笔：{avg:.2f} 元")
