import requests


def get_mortgages(salary, expenditure, deposit):
    url = 'https://formsdss-v3.uk.barclays/dss/service/co.uk/mortgages/borrowcalculator/borrowcalculatorservice'
    headers = {
        'currentState': 'default_current_state',
        'action': 'default',
        'Origin': 'https://www.barclays.co.uk',
        'Referer': 'https://www.barclays.co.uk/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest',
    }
    data = {'header': {'flowId': "0"},
            'body': {
                'applicant1GrossBasicSalaryAmount': salary,
                'applicant2GrossBasicSalaryAmount': 0,
                'applicant3GrossBasicSalaryAmount': 0,
                'applicant4GrossBasicSalaryAmount': 0,
                'applicationDepositAmount': deposit,
                'applicationMonthlyPayment': expenditure,
                'applicationPurchasePrice': 0,
                'applicationPurposeForResidential': "FTBP",
                'applicationTypeOfLending': "RES"
            }
            }

    r = requests.post(url, json=data, headers=headers)
    results = r.json()
    return results['body']


get_mortgages(65000, 1000, 32000)
