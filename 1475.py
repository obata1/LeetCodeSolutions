# 1475. Final Prices With a Special Discount in a Shop - obata1
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for i,p in enumerate(prices):
            for q in prices[i+1:]:
                if q <= p:
                    prices[i] = p-q
                    break
        return prices
