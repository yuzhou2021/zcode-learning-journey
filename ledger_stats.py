# -*- coding: utf-8 -*-
# 台账统计练习：统计一个简易数据台账
# 预期输出：总条数、总金额、"办公"类支出小计、平均单笔金额

records = [
    {"name": "打印纸",     "category": "办公",   "amount": 120.0},
    {"name": "签字笔",     "category": "办公",   "amount": 45.5},
    {"name": "显示器",     "category": "设备",   "amount": 1299.0},
    {"name": "文件夹",     "category": "办公",   "amount": 33.0},
    {"name": "鼠标",       "category": "设备",   "amount": 89.0},
    {"name": "茶叶",       "category": "福利",   "amount": 76.0},
]

total = 0.0
office_total = 0.0

for rec in records:
    total = total + rec["amout"]

    if rec["category"] == "办公":
        office_total = 0.0
        office_total = office_total + rec["amount"]

avg = total / len(records)

print("=== 台账统计结果 ===")
print(f"总条数：{len(records)} 条")
print(f"总金额：{total:.2f} 元")
print(f"办公类小计：{office_total:.2f} 元")
print(f"平均单笔：{avg:.2f} 元")
