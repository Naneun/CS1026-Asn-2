from random import random


class InvestmentMachine:
    def __init__(self):
        """
        In this case, when you initialize this InvestmentMachine instance, we assume there are fixed two investment machines
        with fixed winning probabilities [0.6, 0.7] that will be assigned to these two machines randomly
        The reward rate will be 200%, eg. if you invest $1, play first machine(NO. is 1) and you win, you will get $2
        """
        self.total_machines = 2
        self.reward_rate = 2
        self.reward_probability_distribution = [0, 0]
        if(random() <= 0.5):
            self.reward_probability_distribution = [0.4, 0.6]
        else:
            self.reward_probability_distribution = [0.6, 0.4]

    def invest(self, machine_number, investment_amount):
        """
        @param: armNo: arm number you pull, in this case, should be 1 / 2
                inputCoin: coins you put for this round of play
        @return: reward coins count if you win, otherwise return 0
        """
        if machine_number not in [1, 2]:
            raise Exception("INVESTMENT MACHINE][ERROR] the machine NO. " + str(machine_number) + " is out of range, total machines count is " +str(self.total_machines)+" please set 1/2 as argument")
        win_probability = self.reward_probability_distribution[machine_number - 1]
        if(random() <= win_probability):
            return self.reward_rate*investment_amount
        else:
            return 0
print()
