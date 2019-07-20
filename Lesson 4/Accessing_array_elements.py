import numpy as np


def test_run1():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    element = a[3, 2]

    # print(a[0, 1:3])

    # print(a[0:2, 0:2])

    print(a[:, 0:3:2])


def test_run2():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    a[0, 0] = 1

    # Assigning a list to a column in array
    a[:, 3] = [1, 2, 3, 4, 5]
    print("\nModified:\n", a)


def test_run3():
    a = np.random.rand(5)

    indices = np.array([1, 1, 2, 3])

    print(a[indices])


def test_run4():
    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0),(0, 2, 50, 20, 0, 1, 28, 5, 0)])

    mean = a.mean()
    print(mean)

    a[a < mean] = mean  # replaces values in array less than mean with mean as int value

    print(a)


def test_run5():
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    # print("\nDiv by 2\n", a / 2.0)

    b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
    # print(a + b)

    x = np.array([(5, 6), (7, 8)])
    y = np.array([(1, 0), (0, 1)])  # Identity matrix

    print(np.dot(x, y))


test_run5()
