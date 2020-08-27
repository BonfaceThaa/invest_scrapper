import pandas as pd
import numpy as np


def gen_loan_table(loan, rate, term):
    """
    A function that generates the amortization schedule for a loan
    :param loan:
    :param rate:
    :param term:
    :return:
    """
    payment = np.round(-np.pmt(rate/12, term, loan), 2)
    balance = loan

    index = range(0, term+1)
    columns = ['month', 'payment', 'interest', 'principal', 'balance']
    df = pd.DataFrame(index=index, columns=columns)

    df.iloc[0]['month'] = 0
    df.iloc[0]['balance'] = balance

    for i in range(1, term + 1):
        interest = round(rate/12 * balance, 2)
        principal = payment - interest
        balance = balance - principal

        df.iloc[i]['month'] = i
        df.iloc[i]['payment'] = payment
        df.iloc[i]['interest'] = interest
        df.iloc[i]['principal'] = principal
        df.iloc[i]['balance'] = balance

    return df


loan = 3000
pineapple = gen_loan_table(loan, 0.0575, 14)
print(pineapple)
orange = gen_loan_table(loan, 0.0399, 20)
print(orange)
banana = gen_loan_table(loan, 0.0889, 8)
print(banana)
