# Best Time to Buy and Sell Stock

**LeetCode #121** — Easy

## Problem

Given an array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit you can achieve by choosing a single day to buy and a single day to sell (you must buy before you sell). Return `0` if no profit is possible.

## Approach

Single pass (O(n) time, O(1) space):

- Track the minimum price seen so far (`x`) as the best potential buy day.
- At each step, compute the profit if sold today (`prices[i] - x`).
- Keep a running maximum of all such profits.

## Complexity

| | Complexity |
|---|---|
| Time | O(n) |
| Space | O(1) |

## Example

```python
prices = [7, 1, 5, 3, 6, 4]
# Buy on day 2 (price=1), sell on day 5 (price=6)
# Max profit = 5
```

## Usage

```python
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(sol.maxProfit([7, 6, 4, 3, 1]))      # 0
```
