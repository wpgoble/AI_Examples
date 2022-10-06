def rangeSum(low, high):
    """ calculates the sum between the low number and high number """
    assert isinstance(low, int), 'low must be an integer'
    assert isinstance(high, int), 'high must be an integer'
    assert low < high, 'low must be less than high'
    rSum = 0
    for i in range(high - low + 1):
        rSum += (high - i)
    return rSum

assert rangeSum(1, 4) == 10, "1...4 is incorrect"
assert rangeSum(2, 5) == 14, "2...5 is incorrect"
assert rangeSum(0, 4) == 10, "0...4 is incorrect"
assert rangeSum(-3, 5) == 9, "-3...5 is incorrect"
print("Success!")


print("Let's add a set of consecutive whole numbers")
higher = int(input("What is the high number? "))
lower = int(input("What is the low number? "))

ans = rangeSum(lower, higher)


print("The sum of those numbers and all integers in between is", ans)
