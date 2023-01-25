def maxProfit(prices):
        temp_max_pro=0
        rgt,lft = 1,0
        while rgt < len(prices):
            curr_pro=prices[rgt]-prices[lft]
            # curr_pro=prices[rgt]-prices[lft]
            if prices[rgt] > prices[lft]:
                print(temp_max_pro, curr_pro)
                temp_max_pro=max(temp_max_pro, curr_pro)
                print(temp_max_pro)
            else :
                lft=rgt
            rgt+=1
        return temp_max_pro 

maxProfit([7,1,2,6,3,1,5])