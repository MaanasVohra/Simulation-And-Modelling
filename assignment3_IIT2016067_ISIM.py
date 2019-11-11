def main() :
    days = int(input())
    [P, Q] = list(map(int, input().split(' ')))
    demand = list(map(float, input().split(' ')))
    
    stock_count = 115
    outstanding_order_days = 0
    
    total_cost = 0
    
    for i in range(days) :
        demand_left = 0
                
        if(outstanding_order_days > 0) : # check for any outstanding orders
            outstanding_order_days -= 1
            if(outstanding_order_days == 0) :
                stock_count += Q
                        
        if(demand[i] >= stock_count) :
            demand_left = demand[i] - stock_count
            stock_count = 0
            
        else: 
            stock_count -= demand[i]
           
        if(demand_left > 0) :
            total_cost += demand_left * 18.0
            
        if(stock_count > 0) :
            total_cost += stock_count * 0.75
        
        if(stock_count <= P and outstanding_order_days == 0) : # only one outstanding order
            outstanding_order_days = 3
            total_cost += 75.0
            
    if(total_cost.is_integer()) :
        print("{0:.0f}".format(total_cost))
    else:
        print("{0:.1f}".format(total_cost))
    
if __name__ == "__main__" :
    main()