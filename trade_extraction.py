import os
import re
symbols = ["BAJAJ-AUTO", "BAJAJFINSV", "DLF", "HDFCBANK", "ICICIBANK", "INFY", "JSWSTEEL", "L&TINFRA","RELIANCE", "SBIN", "SUNPHARMA", "TCS", "TATAMOTORS"]
file = "alltrades.DAT"
for sy in symbols:
    f = open(file, 'r')
    data = []
    for line in f:
        if re.search(sy, line):
            record = line[0:2]
            segment = line[2:6]
            trade_no = line[6:22]
            trade_time = line[22:36]
            series = line[46:48]
            trade_price = line[48:56]
            trade_qty = line[56:64]
            buy_order_no = line[64:80]
            buy_algo = line[80:81]
            client = line[81:82]
            sell_order_no = line[82:98]
            sell_algo = line[98:99]
            row = '|'.join([record, segment, trade_no, trade_time, series, trade_price, trade_qty, buy_order_no, buy_algo, client, sell_order_no, sell_algo])
            data.append(row)
    f.close()
    f = open(os.getcwd() + '\\trade\\' + sy + '.trade', 'w')
    data = '\n'.join(data)
    f.write(data)
    f.close()
    print(f'Trades extracted for {sy}.')
print()
for s in symbols:
    f = open(file, 'r')
    print(f'Total trades for {s:<11}: {len(re.findall(s, f.read())):>7,}')
    f.close()
print()
print('Done!')