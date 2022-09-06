def divide(x, y):
    # runs the program
    try:
        print(x // y)

    # if there is a zero division error, runs this except
    except ZeroDivisionError:
        print("Tried to divide by 0")

    # if there is a type error, runs this except
    except TypeError:
        print("Not suitable type")

    # runs other any error
    except Exception:
        print("Unknown Error")

    # if there is no errors, codes continue from else
    else:
        print("It works")

    # finally always runs after code finished
    finally:
        print("Finished the program")


if __name__ == '__main__':
    divide(4, 0)
    print("------------")
    divide(4, 2)
    print("------------")
    divide("4",2)
    print("------------")
    # they can not catch the error outside the try except
    divide(math.e, 4)
