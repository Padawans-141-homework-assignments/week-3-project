class returnOnInvestment():
    def __init__(self,pay_w_cash = None, ren_income = 0, income = 0, expenses = 0, cash_flow = 0):
        self.pay_w_cash = pay_w_cash
        self.ren_income = ren_income

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
        is_duplex = self.yn_confirm()

        print('\nDo you have other incomes? (laundry, storage, misc...): ')
        have_other_inc = self.yn_confirm()
        if have_other_inc == True:
            print('\nWhat is the total amount of other income')
            other_inc_amt = self.money_confirm()
        else:
            pass

        # v Calculates the sum of the total monthly income given the above inputs v
        if is_duplex == True and have_other_inc == True:   #rental, w duplex, other incomes
            self.income = (self.ren_income * 2) + other_inc_amt
            print(f'\nYour total Income is ${round(self.income, 2)}.')
            return self.income, self.ren_income, self.pay_w_cash
        
        elif is_duplex == True and have_other_inc == False:    #rental, w duplex, no other incomes
            self.income = (self.ren_income * 2)
            print(f'\nYour total Income is ${round(self.income, 2)}.')
            return self.income, self.ren_income, self.pay_w_cash
        
        elif is_duplex == False and have_other_inc == True:     #rental, no duplex, other incomes
            self.income = self.ren_income + other_inc_amt
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
        p_tax = self.money_confirm()

        print('\nHow much do you spend on house insurance')
        insurance_amt = self.money_confirm()

        print('\nDo you pay for your utilities, HOA fees, lawn/snow care fees, vacancy fees')
        pays_utilities = self.yn_confirm()
        if pays_utilities:
            print('\nHow much do you spend on all of the above collectively')
            utilities_amt = self.money_confirm()
        else:
            pass

        print('\nHow much do you set aside for repair fees')
        repair_fees = self.money_confirm()

        print('\nHow much do you set aside for capital expenditures')
        cap_expend = self.money_confirm()

        print('\nDo you have a property manager')
        has_manager = self.yn_confirm()
        if has_manager:
            print('\nHow much do you spend on your property manager')
            manager_amt = self.money_confirm()
        else:
            pass

        if self.pay_w_cash:
            print('\nSince you pay with cash you don\'t need to pay mortgage')
        else:
            print('\nHow much do you spend on your mortgage')
            mortgage = self.money_confirm()
            


        # v Should be all use cases given the above information
        if pays_utilities and has_manager and self.pay_w_cash:
            self.expenses = p_tax + insurance_amt + repair_fees + cap_expend + utilities_amt + manager_amt
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses

        elif pays_utilities == False and has_manager and self.pay_w_cash:
            self.expenses = p_tax + insurance_amt + repair_fees + cap_expend + manager_amt
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif pays_utilities and has_manager == False and self.pay_w_cash:
            self.expenses = p_tax + insurance_amt + repair_fees + cap_expend + utilities_amt
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif pays_utilities and has_manager and self.pay_w_cash == False:
            self.expenses = p_tax + insurance_amt + repair_fees + cap_expend + utilities_amt + manager_amt + mortgage
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif pays_utilities == False and has_manager == False and self.pay_w_cash:
            self.expenses = p_tax + insurance_amt + repair_fees + cap_expend
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif pays_utilities == False and has_manager and self.pay_w_cash == False:
            self.expenses = p_tax + insurance_amt + repair_fees + cap_expend + manager_amt + mortgage
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif pays_utilities and has_manager == False and self.pay_w_cash == False:
            self.expenses = p_tax + insurance_amt + repair_fees + cap_expend + utilities_amt + mortgage
            print(f'\nThis is the total amount of expenditures: ${self.expenses}')
            return self.expenses
        
        elif pays_utilities == False and has_manager == False and self.pay_w_cash == False:
            self.expenses = p_tax + insurance_amt + repair_fees + cap_expend + mortgage
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

        total_roi = (annual_cashflow / total_investment) * 100
        print(f'\nThe total Return On Investment for the current property is {round(total_roi, 2)}%.')

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