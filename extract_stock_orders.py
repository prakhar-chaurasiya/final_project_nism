symbols = []
f = open('symbols.txt', 'r')
s = f.readline()
while(s):
    symbols.append(s.replace('\n',''))
    s = f.readline()
f.close()

file = '/home/suneel/Downloads/CASH_Orders_20012021.DAT'
outputfiles = [s.replace('b','').lower() for s in symbols]

for i,symbol in enumerate(symbols):
    f = open(file, 'r')
    ell = f.readline()
    data = []
    while(ell):
        if(ell[38:48] == symbol):
            session = ell[0:2]
            orderid = ell[6:22]
            time = ell[22:36]
            side = ell[36:37]
            action = ell[37:38]
            dquant = ell[50:58]
            fquant = ell[58:66]
            price = ell[66:74]
            triggerprice = ell[74:82]
            market = ell[82:83]
            stoploss = ell[83:84]
            ioc = ell[84:85]
            row = '|'.join([session, orderid, side, action, time, price, fquant, dquant, market, ioc, stoploss, triggerprice])
            data.append(row)
        ell = f.readline()

    f.close()
    f = open('/home/suneel/Teaching/Finance_Analytics/data/highfreq/' + outputfiles[i]+'.order', 'w')
    data = '\n'.join(data)
    f.write(data)
    f.close()


