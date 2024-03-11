class returnOnInvestment():
    def __init__(self,pay_w_cash = False, ren_income = 0, utilities_amt = 0, other_inc_amt = 0, is_duplex = False ,have_other_inc = False, p_tax = 0, insurance_amt = 0, pays_utilities = False, 
                vacancy = 0 ,repair_fees = 0, cap_expend = 0, has_manager = False, manager_amt = 0, mortgage = 0, income = 0, expenses = 0, cash_flow = 0):
        self.utilities_amt = utilities_amt
        self.other_inc_amt = other_inc_amt
        self.vacancy = vacancy
        self.pay_w_cash = pay_w_cash
        self.ren_income = ren_income
        self.is_duplex = is_duplex
        self.have_other_inc = have_other_inc
        self.p_tax = p_tax
        self.insurance_amt = insurance_amt
        self.pays_utilities = pays_utilities
        self.repair_fees = repair_fees
        self.cap_expend = cap_expend 
        self.has_manager = has_manager
        self.manager_amt = manager_amt
        self.mortgage = mortgage

    #handles the y/n confirmations
    def yn_confirm(self):
        while True:
            inp = input('(y/n): ')
            result = None

            if inp == 'y':
                result = True
                return result
            elif inp == 'n':
                result = False
                return result
            else:
                print('\nPlease enter an appropriate response("y" for yes, "n" for no): ')

    # handles the money inputs to avoid repeating try/except blocks and avoid errors
    def money_confirm(self):
        while True:
            try:
                money = float(input('Please enter an amount: $'))
                return money
            except:
                print('That was not an appropriate amount, please enter a correct amount: ')

        
    # responsible for getting the information on income
    def income(self):
        # v Asks the user for the base information to calculate v
        print('Do you pay with cash')
        self.pay_w_cash = self.yn_confirm()

        print('\nWhat is your current rental income')
        self.ren_income = self.money_confirm()

        print('\nIs your current rental property a duplex ("y" for yes, "n" for no)')
        self.is_duplex = self.yn_confirm()

        print('\nDo you have other incomes? (laundry, storage, misc...): ')
        self.have_other_inc = self.yn_confirm()
        if self.have_other_inc == True:
            print('\nWhat is the total amount of other income')
            self.other_inc_amt = self.money_confirm()
        else:
            pass

        # v Calculates the sum of the total monthly income given the above inputs v
        if self.is_duplex == True and self.have_other_inc == True:   #rental, w duplex, other incomes
            self.income = (self.ren_income * 2) + self.other_inc_amt
            print(f'\nYour total Income is ${round(self.income, 2)}.')
            return self.income, self.ren_income, self.pay_w_cash
        
        elif self.is_duplex == True and self.have_other_inc == False:    #rental, w duplex, no other incomes
            self.income = (self.ren_income * 2)
            print(f'\nYour total Income is ${round(self.income, 2)}.')
            return self.income, self.ren_income, self.pay_w_cash
        
        elif self.is_duplex == False and self.have_other_inc == True:     #rental, no duplex, other incomes
            self.income = self.ren_income + self.other_inc_amt
            print(f'\nYour total Income is ${round(self.income, 2)}.')
            return self.income, self.ren_income, self.pay_w_cash
        
        else:                                                           #rental, no duplex, no other incomes
            self.income = self.ren_incomeren_inc
            print(f'\nYour total Income is ${round(self.income, 2)}.')
            return self.income, self.ren_income, self.pay_w_cash


    #responsible for the house expenses
    def expenses(self):
        # asks/skips for information depending on if its needed
        print('\nWhat is your current property tax')
        self.p_tax = self.money_confirm()

        print('\nHow much do you spend on house insurance')
        self.insurance_amt = self.money_confirm()

        print('\nDo you pay for your utilities, HOA fees, lawn/snow care fees, vacancy fees')
        self.pays_utilities = self.yn_confirm()
        if self.pays_utilities:
            print('\nHow much do you spend on all of the above collectively')
            self.utilities_amt = self.money_confirm()
        else:
            # v Video said if landlord pays for utilities 5% of the income goes towards the vacancy.
            self.vacancy = self.ren_income * 0.05
            print(f'\nSince the landlord pays for utilities, 5% of your rental income will be used as vacancy.\nVacancy cost given the amount ${self.ren_income} is: ${self.vacancy}.')
            self.ren_income = self.ren_income - self.vacancy
            

        print('\nHow much do you set aside for repair fees')
        self.repair_fees = self.money_confirm()

        print('\nHow much do you set aside for capital expenditures')
        self.cap_expend = self.money_confirm()

        print('\nDo you have a property manager')
        self.has_manager = self.yn_confirm()
        if self.has_manager:
            print('\nHow much do you spend on your property manager')
            self.manager_amt = self.money_confirm()
        else:
            pass

        if self.pay_w_cash:
            print('\nSince you pay with cash you don\'t need to pay mortgage')
        else:
            print('\nHow much do you spend on your mortgage')
            self.mortgage = self.money_confirm()
            


        # v Should be all use cases given the above information
        if self.pays_utilities and self.has_manager and self.pay_w_cash:
            self.expenses = self.p_tax + self.insurance_amt + self.repair_fees + self.cap_expend + self.utilities_amt + self.manager_amt
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses

        elif self.pays_utilities == False and self.has_manager and self.pay_w_cash:
            self.expenses = self.p_tax + self.insurance_amt + self.repair_fees + self.cap_expend + self.manager_amt + self.vacancy
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif self.pays_utilities and self.has_manager == False and self.pay_w_cash:
            self.expenses = self.p_tax + self.insurance_amt + self.repair_fees + self.cap_expend + self.utilities_amt
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif self.pays_utilities and self.has_manager and self.pay_w_cash == False:
            self.expenses = self.p_tax + self.insurance_amt + self.repair_fees + self.cap_expend + self.utilities_amt + self.manager_amt + self.mortgage
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif self.pays_utilities == False and self.has_manager == False and self.pay_w_cash:
            self.expenses = self.p_tax + self.insurance_amt + self.repair_fees + self.cap_expend + self.vacancy
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif self.pays_utilities == False and self.has_manager and self.pay_w_cash == False:
            self.expenses = self.p_tax + self.insurance_amt + self.repair_fees + self.cap_expend + self.manager_amt + self.mortgage + self.vacancy
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif self.pays_utilities and self.has_manager == False and self.pay_w_cash == False:
            self.expenses = self.p_tax + self.insurance_amt + self.repair_fees + self.cap_expend + self.utilities_amt + self.mortgage
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif self.pays_utilities == False and self.has_manager == False and self.pay_w_cash == False:
            self.expenses = self.p_tax + self.insurance_amt + self.repair_fees + self.cap_expend + self.mortgage + self.vacancy
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses


    #responsible for calculating the cash flow
    def cash_flow(self):
        self.cash_flow = self.income - self.expenses
        print(f'\nYour total cash flow from your current invesment is: ${self.cash_flow}.')
        return self.cash_flow


    #responsible for calculating the total investment/ annual cashflow
    #/and the final total roi with the last given values
    def roi(self):
        print('\nWhat was the cost of the down payment placed on the house')
        down_payment = self.money_confirm()

        print('\nWhat were the cloing costs of the house')
        closing_cost = self.money_confirm()

        print('\nWhat was the rehab budget for the house')
        rehab_budget = self.money_confirm()

        total_investment = down_payment + closing_cost + rehab_budget
        print(f'\nThis is the total investment of the home: ${total_investment}.')

        annual_cashflow = self.cash_flow * 12
        print(f'\nThis is the annual cash flow of the home: ${annual_cashflow}')

        print(f'\nPay with cash: {self.pay_w_cash}\nRental Income: ${self.ren_income}\nIs duplex: {self.is_duplex}\nHas Other Income: {self.have_other_inc}\nOther income amount: ${self.other_inc_amt}',
              f'\nProperty Tax: ${self.p_tax}\nInsurance Amount: ${self.insurance_amt}\nPays Utilites: {self.pays_utilities}\nUtilities Amount: ${self.utilities_amt}\nVacancy Amount: ${self.vacancy}',
              f'\nRepair Fees: ${self.repair_fees}\nCapital Expenditure: ${self.cap_expend}\nHas Property Manager: {self.has_manager}\nManager Cost: ${self.manager_amt}\nMortgage: ${self.mortgage}',
              f'\nDown Payment: ${down_payment}\nClosing Cost: ${closing_cost}\nRehab Budget: {rehab_budget}\n{"~" * 40}')

        total_roi = (annual_cashflow / total_investment) * 100
        print(f'The total Return On Investment for the current property is {round(total_roi, 2)}%.')

        return


    #responsible for actually going through the class methods and
    #running them for the user.
    def runROI(self):
        self.income()
        self.expenses()
        self.cash_flow()
        self.roi()

calc = returnOnInvestment()

calc.runROI()