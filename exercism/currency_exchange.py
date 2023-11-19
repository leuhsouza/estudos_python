def exchangeable_value(budget, exchange_rate, spread, denomination):
    
    
    spread_value = ((exchange_rate + spread)/100)
    total_value = budget * (exchange_rate+spread_value)

    return int(total_value // denomination) 


exchangeable_value(127.25, 1.20, 10, 20)
