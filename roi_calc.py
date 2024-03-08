#Income method

#1. Ask what the customers rental income is. 
#2. Ask if the property is a duplex. If it is, multiply the rent by 2x.
#(OPTIONAL) ask for laundry, storage, and misc income.
#3. Sum the Total monthly income.

#11. Ask them if they pay or the landlord pays for the (Utilities, HOA fees, lawn/snow care fees,vacancy fees[if its the landlord take 5% off rental income as vacancy])
#3. Ask about the utilities (Electric, Water, Sewer, Garbage, Gas)
#4. Ask about the HOA fees
#5. Ask about the lawn/snow care expenses. 
#6. Ask about the vacancy fees
#12. Ask them if they have a property manager (If not then don't charge them)
#9. Ask about the property management.
#10. Ask for mortgage (if they aren't paying with cash).
#13. Ask them the cost of their current mortgage.    
#Expenses method
#1. Ask what the property tax is.
#2. Ask what the insurance is. 
#7. Ask about the reapir fees.
#8. Ask about the capital expenditures. 
#14. Sum all the monthly expenses. 

#Cash Flow method
#Cash flow is: Income - Expenses

#return on investment method
#1. Ask what the cost of the down payment is
#2. Ask what the closing costs are
#3. Ask for the Rehab budget.
#4. Sum all for total investment
#5. multiply cashflow by 12 for annual total cashflow.
#6. ROI is equals to (annual cash flow / total investment) multiplied by 100. 




class returnOnInvestment():
    def __init__(self,pay_w_cash = None, ren_income = 0, income = 0, expenses = 0, cash_flow = 0):
        pass

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

        print('\nDo you pay for your utilities, HOA fees, lawn/snow care feese, vacancy fees')
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


    def cash_flow(self):
        pass

    def roi(self):
        pass

    def runROI(self):
        self.income()
        self.expenses()

calc = returnOnInvestment()

calc.runROI()