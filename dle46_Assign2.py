##
# Author: David Le
# Exploration and exploitation of 2 investment machines using an investment strategy
from investment_machine import InvestmentMachine
my_investment_machines = InvestmentMachine()  # initialize investment machine instance

# Variables and constants
total_reward = 0
MONEY_AFTER_SPENDING = 80  # Money after spending $10 in both machines after starting with initial $100
FIXED_INVESTMENT = 1
FIXED_PERCENTAGE = 0.5
SIMULATIONS = 100


def main():
    """
    The investment strategy for putting $1 into both machines 10 times to see which one returns more money. Then
    for the remaining money, invest half the current total assets into the more profitable machine for the last 10 times

    """
    global total_reward  # Calls in the variable into the function
    total_returns = []
    for simulation in range(SIMULATIONS):
        total_reward_machine_1 = 0
        total_reward_machine_2 = 0
        # Investing into both machines 10 times with $1 investment
        total_reward_machine_1 += fixed_amount_investment(1, FIXED_INVESTMENT, 10)
        total_reward_machine_2 += fixed_amount_investment(2, FIXED_INVESTMENT, 10)
        # Adding the money from both machines and the $80 after spending $10 in both machines
        total_reward = MONEY_AFTER_SPENDING + total_reward_machine_1 + total_reward_machine_2
        # Investing half of your total money into the more profitable machine
        if total_reward_machine_1 >= total_reward_machine_2:  # If machine 1 is more profitable
            fixed_percentage_investment(1, FIXED_PERCENTAGE, 10)
        else:  # If machine 2 is more profitable
            fixed_percentage_investment(2, FIXED_PERCENTAGE, 10)
        total_returns.append(total_reward)  # Adds the total reward to the list
    average = sum(total_returns) / SIMULATIONS
    print("The average amount of money with this investment strategy is $%.2f." % average)


def fixed_amount_investment(machine_number, money_invest, times_invested):
    """
    Computes the total reward gain for repeated investment of a fixed amount into a machine using how much you want to invest each time,
    and how many times you want to invest
    @param machine_number: One of the investment machine [1,2]
    @param money_invest: How much you are investing into the machine each trial
    @param times_invested:  How many times you want to invest in the machine
    """
    machine_gain = 0
    for times_machine_amount in range(times_invested):
        machine_gain += my_investment_machines.invest(machine_number, money_invest)  # How much you will gain when you invest into a machine
    return machine_gain


def fixed_percentage_investment(machine_number, percentage, times_invested):
    """
    Computes the total reward gain from repeated investment using a percentage of the current assets into one of the
    machines
    @param machine_number: One of the investment machines [1,2]
    @param percentage: What percentage of the current assets you want to invest
    @param times_invested: How many times you want to invest into a machine
    """
    global total_reward
    for times_machine_amount in range(times_invested):
        single_investment = my_investment_machines.invest(machine_number, total_reward * percentage)
        # Adding the output of the percentage investment into your total reward and removed how much you put in the machine
        total_reward += single_investment - total_reward * percentage


main()  # Calling the main function
