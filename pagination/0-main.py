if __name__ == "__main__":
    index_range = __import__('0-simple_helper_function').index_range

    res = index_range(1, 7)
    print(type(res))  # <class 'tuple'>
    print(res)        # (0, 7)

    res = index_range(3, 15)
    print(type(res))  # <class 'tuple'>
    print(res)        # (30, 45)
