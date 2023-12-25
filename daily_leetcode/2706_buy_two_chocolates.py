class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        min_price = min(prices)
        prices.remove(min_price)
        sec_price = min(prices)
        
        return money if min_price + sec_price > money else money - min_price - sec_price