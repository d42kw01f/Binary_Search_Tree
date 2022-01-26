import random


def simple_math_issue(_number, count):
    count += 1
    print(count, _number)
    if _number == 1:
        print('\t ---Reached 1---', count)
        exit()

    if (_number % 2) == 0:
        simple_math_issue(_number//2, count)
    else:
        simple_math_issue(_number//3+1,count)

if __name__ == '__main__':
    simple_math_issue(random.randint(0, 10),count=0)