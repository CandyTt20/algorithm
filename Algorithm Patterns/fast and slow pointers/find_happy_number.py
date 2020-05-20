def squre_sum(num):
    sum_num = 0

    while num != 0:
        remain = num % 10
        num = num // 10
        sum_num += remain * remain
    return sum_num

def find_happy_number(num):
    # TODO: Write your code here
    slow, fast = num, num
    while True:
        slow = squre_sum(slow)
        fast = squre_sum(squre_sum(fast))
        if slow == fast:
            break

    return slow==1


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()