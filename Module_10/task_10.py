from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for i in self.data:
            if i > 0:
                sum += i
        
        return sum
    


payment = AmountPaymentList([1, -2, 3, -6, 1])
print(payment.amount_payment())