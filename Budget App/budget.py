class Category:
    def __str__(self):
        title = ((30-len(self.name)) // 2 * "*") + self.name + ((30-len(self.name)) // 2 * "*")
        list_item = title + "\n"
        for i in self.ledger:
            list_item += i["description"][:23]
            desc_len = len(i["description"])
            if (desc_len < 23):
                list_item += ((23 - desc_len) * " ")
            list_item += "{:>7.2f}\n".format(i["amount"])
        list_item += "Total: {:.2f}".format(self.get_balance())
        return list_item

    def __init__(self, name):
        self.fund = 0
        self.ledger = []
        self.name = name
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.fund += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.fund -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.fund
    
    def transfer(self, amount, target):
        if self.check_funds(amount):
            description = "Transfer to {}".format(target.name)
            self.fund -= amount
            self.ledger.append({"amount": -amount, "description": description})

            description = "Transfer from {}".format(self.name)
            target.fund += amount
            target.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.fund:
            return False
        else:
            return True


def create_spend_chart(categories):
    total_withdraw = 0
    list_withdraw = []
    list_name= []
    for i in categories:
        temp = 0
        for j in i.ledger:
            if j["amount"] < 0:
                temp += abs(j["amount"])
        total_withdraw += temp
        list_withdraw.append(temp)
        list_name.append(i.name)
    for i in range(len(list_withdraw)):
        list_withdraw[i] = list_withdraw[i] / total_withdraw * 100
    chart = "Percentage spent by category\n"
    for i in reversed(range(0,101,10)):
        chart += "{:>3}| ".format(str(i))
        for j in range(len(list_withdraw)):
            if list_withdraw[j] >= i:
                chart += "o"
            else:
                chart += " "
            chart += "  "
        chart += "\n"
    chart += ((4 * " ") + ((3 * len(list_withdraw) + 1) * "-") + "\n")
    for i in range(len(max(list_name, key=len))):
        chart += (5 * " ")
        for j in range(len(list_name)):
            if i >= len(list_name[j]):
                chart += "   "
            else:
                chart += "{}  ".format(list_name[j][i])
        if i < len(max(list_name, key=len)) - 1:
            chart += "\n"
    return chart
