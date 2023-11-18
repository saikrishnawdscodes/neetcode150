# Nov 18, 23
# Approach : Use 2 pointers. But it's called sliding window as we slide the 2 ptrs , across the array
# in search of best buy and sell time

# l = 0, r = 1 ; until r< len(prices)// unlike keeping 2 ptrs on either side of the array.

# l is ptr for buying, r is ptr for selling. increment each - based on whether there has been a profit.
# if there is a profit, increment the sell ptr r - as the buy price is low and there could be a more profitable day to sell.
# Similarly, increment the l if there is no profit to sell on that day - likely implies that the buy price is too high
# keep updating the max_profit and return it in the end.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        max_profit = 0
        while r< len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)

            else:
                l = r
            r += 1
        return  max_profit

# TC : O(n)
# SC : O(1)