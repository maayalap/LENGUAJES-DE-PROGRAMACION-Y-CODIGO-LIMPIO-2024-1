"""
Parameters:
    total_amount : Total price of the house or dwelling
    interest : This is the interest that will be applied to the loan
    quotas : If requested, this is the number of installments at which the Loan will be made
    interest_housing: It is the interest that will be applied to the normal price of the house
"""

def MortgageLifetimeInverse(total_amount, interest, interest_housing, age, gender):

    """
        Definition:
            Lifetime reverse mortgage: the client collects the annuity until he or she dies. The function returns the calculation

        Returns:
            float: The amount of money to be received periodically in a lifetime reverse mortgage.
    """

    months = LifeExpectancyCalculation(age, gender) * 12
    monthly_fee = ((total_amount * interest_housing) / months) 
    return monthly_fee + monthly_fee*(interest * months)

def MortgageTemporaryReverse(total_amount, interest, interest_housing, quotas):

    """
        Definition:
            Temporary reverse mortgage: the rent is obtained for a set period of time.
        Returns:
            float: The total amount of money to be received during the established installment period.
    """    
    monthly_fee = ((total_amount * interest_housing) / quotas) 
    return monthly_fee + monthly_fee*(interest * quotas)

def MortgageSingleReverse(total_amount, interest_housing):

    """
        Definition:
            Single-draw reverse mortgage: The value to be received will be the total sale value of the home.
        Returns:
            float: The total value of the home.
    """
    return total_amount * interest_housing

def LifeExpectancyCalculation(age, gender):
    "Retorna el calculo de la esperanza de vida en base al genero y la edad"
    if age < 65:
        raise E.Invalid_age()
    if gender == "M" or gender=="m":
        return 80 - age
    if gender == "F" or gender=="f":
        return 74 - age    
