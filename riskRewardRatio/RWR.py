with open('data.txt', 'r') as file:
    data = file.readlines()

total_profit = 0
total_loss = 0
trade_count = 0

for value in data:
    numeric_value = float(value)
    if numeric_value > 0:
        total_profit += numeric_value
    else:
        total_loss += abs(numeric_value)
    trade_count += 1

risk = total_loss / trade_count
profitability = total_profit / trade_count
risk_reward_ratio = profitability / risk

print("Risk =", risk)
print("Reward =", profitability)
print("Reward/Risk =", risk_reward_ratio)
