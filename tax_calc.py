# Your Task is to create a class called person, each person has a name and income
# the income should be private
#You should implement the function get_income, so that one can see the persons income
#You should also implement the function taxes that shows how much taxes this personna has to pay
#in this state taxing is progressive ( see example below)to do this you should use the dictonary with given called "tax_brackets" so that you can calculate the tax
# Also the repr function should be implemeted one should be able to see the persons name, their income and the taxes that they have to pay.
# Example Person A earns 100000
# The first 20000 aren't taxed
#Earnings from 20,000 to 35000 are taxed with 5% 15000*.05=750
#Earnings from 35,000 to 60,000 are taxed with 10% 25000*.10=2500
#Earnings from 60,000 to 90,000 are taxed with 12.5% 30000*.125=3750
#The earnings, the remaing 10,000 are taxed with 15% 10000*.15=1500
#This personna has to pay 8500$.
tax_brackets = {
                20000: .05,
                35000: .10,
                60000: .125,
                90000: .15,
                150000: .20,
                350000: .25}


class Person:
    def __init__(self,name,income):
        self.name=name
        self.__income=income
    def get_income(self):
        return self.__income
    def taxes(self):
        pass


        pass
    def __repr__(self):
        return f"{self.name} earns {self.get_income()}$ and pays"





