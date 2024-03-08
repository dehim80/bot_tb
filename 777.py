balance = {'info': {'retCode': '0', 'retMsg': 'OK', 'result': {'list': [{'totalEquity': '11.14514498', 'accountIMRate': '0', 'totalMarginBalance': '11.14514498', 'totalInitialMargin': '0', 'accountType': 'UNIFIED', 'totalAvailableBalance': '11.14514498', 'accountMMRate': '0', 'totalPerpUPL': '0', 'totalWalletBalance': '11.14514498', 'accountLTV': '0', 'totalMaintenanceMargin': '0', 'coin': [{'availableToBorrow': '', 'bonus': '0', 'accruedInterest': '0', 'availableToWithdraw': '11.14584717', 'totalOrderIM': '0', 'equity': '11.14584717', 'totalPositionMM': '0', 'usdValue': '11.14514498', 'unrealisedPnl': '0', 'collateralSwitch': True, 'spotHedgingQty': '0', 'borrowAmount': '0.000000000000000000', 'totalPositionIM': '0', 'walletBalance': '11.14584717', 'cumRealisedPnl': '-0.04211513', 'locked': '0', 'marginCollateral': True, 'coin': 'USDT'}]}]}, 'retExtInfo': {}, 'time': '1709207979875'}, 'timestamp': 1709207979875, 'datetime': '2024-02-29T11:59:39.875Z', 'USDT': {'free': 11.14584717, 'used': 0.0, 'total': 11.14584717, 'debt': 0.0}, 'free': {'USDT': 11.14584717}, 'used': {'USDT': 0.0}, 'total': {'USDT': 11.14584717}, 'debt': {'USDT': 0.0}}
print(type(balance))
print(balance['info']['result'])
print(balance['info']['result']['list'])
print(balance['info']['result']['list'][0])
print(balance['info']['result']['list'][0]['coin'])
unrealisedPnl = (balance['info']['result']['list'][0]['coin'][0]['unrealisedPnl'])
cumRealisedPnl = (balance['info']['result']['list'][0]['coin'][0]['cumRealisedPnl'])

[{'availableToBorrow': '', 'bonus': '0', 'accruedInterest': '0', 'availableToWithdraw': '11.14584717', 'totalOrderIM': '0',
  'equity': '11.14584717', 'totalPositionMM': '0', 'usdValue': '11.14620383', 'unrealisedPnl': '0', 'collateralSwitch': True,
  'spotHedgingQty': '0', 'borrowAmount': '0.000000000000000000', 'totalPositionIM': '0', 'walletBalance': '11.14584717',
  'cumRealisedPnl': '-0.04211513', 'locked': '0', 'marginCollateral': True, 'coin': 'USDT'}]

[{'availableToBorrow': '', 'bonus': '0', 'accruedInterest': '0', 'availableToWithdraw': '9.35472958', 'totalOrderIM': '0',
  'equity': '11.11359969', 'totalPositionMM': '0.19225811', 'usdValue': '11.11397755', 'unrealisedPnl': '-0.0131',
  'collateralSwitch': True, 'spotHedgingQty': '0', 'borrowAmount': '0.000000000000000000', 'totalPositionIM': '1.75887011',
  'walletBalance': '11.12669969', 'cumRealisedPnl': '-0.06126261', 'locked': '0', 'marginCollateral': True, 'coin': 'USDT'}]
