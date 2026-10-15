"""
Problem: Clean Images, Then Features (Medium)
Problem statement
You have a folder of face-image IDs for an age-detection toy model. Odd IDs are blurry selfies. Even IDs are clean.
Keep only the clean (even) IDs, then turn each one into a dummy feature by squaring it.
Yes, squaring an ID is a silly feature. The senior said: “First learn filter and map. Fancy embeddings can wait.”
You must use filter() + lambda to keep evens, then map() + lambda to square. Print the final list of features.

Input
First line: integer n (1 ≤ n ≤ 100) — how many IDs.
Second line: n integers — the image IDs.
Output
Print a Python list of squared even IDs, same order. Example: [4, 16, 36].

Example
Input
6
1 2 3 4 5 6
Output
[4, 16, 36]

Hint: আগে ব্লারি ফেস ফেলে দাও (filter), পরে ফিচার বানাও (map)। উল্টো করলে 1-এর স্কয়ারও ঢুকে পড়বে — ডেটাসেট নষ্ট।
"""

# ata problem er statement anujai solve kora hoise

n = int(input())
ids = list(map(int, input().split()))

even_ids = filter(lambda x : x % 2 == 0, ids)

features = list(map(lambda x : x * x, even_ids))

print(features)





# Bikolpo vabe. akhane list comprehension use kore solve kora hoise. problem er statement use kora hoi ni

N = int(input())

numbers = list(map(int, input().split()))

square = [s**2 for s in numbers if s % 2 == 0]
print(square)