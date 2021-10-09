def annuity_rate_R(n,r,facevalue):
    q = 1 + r
    part1 = pow(q,n)*r
    part2 = pow(q,n)-1
    return (part1/part2)*facevalue
    
def annuity_redemption(S0, r, n, t):
    part1 = r
    part2 = pow(1+r,n)-1
    return (part1/part2) *S0* pow(1+r,t-1)
  
def calc_mortgage(f,n,r):    
    redemption_payments = []
    interest_payments = []
    labels = []
    cashflow_table = []
    facevalue = int(f)
    r = float(r)
    n = int(n)
    r_new = r/100
    rate = annuity_rate_R(n,r_new,facevalue)
    rate_monthly = annuity_rate_R(n*12,r_new/12,facevalue)

    balance = facevalue
    total_interest_paid = 0
    
    for year in range(1,n+1):
        red_rate = round(annuity_redemption(facevalue, r/100, n, year),2)
        redemption_payments.append(red_rate)
        # print('red_rate',red_rate)
        interest_paymnet = round(rate - red_rate,2)
        balance = round(balance - red_rate,2)
        interest_payments.append(interest_paymnet)
        cashflow_table.append({'year':year,'rate':round(rate,2),'interest':interest_paymnet,'redemption':red_rate,'balance':balance})
        labels.append(year)
        total_interest_paid = total_interest_paid + interest_paymnet

    print('total_interest_paid',total_interest_paid)

    return {
        'labels':labels,
        'cashflows':[{'data': interest_payments,'label':'Interest'},{'data': redemption_payments,'label':'Principal'}],
        'cashflow_table':cashflow_table,
        'rate':rate,
        'total_interest_paid':total_interest_paid,
        'mortgage_size':facevalue,
        'rate_monthly':rate_monthly}
