# Given a string, print the frequency of the word

string = """
data science machine learning data analysis machine
learning statistics data models data training data validation features
features labels prepocoessing data augmentation models data optimization
gradient descent neural networks data trnsors matrices visualization
exploration pandas numpy matplotlib seabone scikitlearn tensorflow pytorch
deployment inference production monitoring reproducibility experiments results
metrics accuracy precision recall f1 cross validation data machine
"""

words = string.split()

count = {}

for word in words:
   count[word] = count.get(word,0) + 1

for k,v in count.items():
   print(f"Count of {k} is {v}")


