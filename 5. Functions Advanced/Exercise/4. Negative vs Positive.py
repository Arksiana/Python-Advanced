numbers = list(map(int, input().split()))
negative = sum(filter(lambda x: x < 0, numbers))
positive = sum(filter(lambda x: x > 0, numbers))

print(negative)
print(positive)

if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")