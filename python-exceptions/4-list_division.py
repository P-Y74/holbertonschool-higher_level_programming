#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements from two lists index by index and handles exceptions.

    Parameters:
        my_list_1 (list): The first list containing any types.
        my_list_2 (list): The second list containing any types.
        list_length (int): Number of elements to attempt to divide.

    Returns:
        list: A list containing the result of the divisions. If a division
              cannot be performed, 0 is added instead and a specific error
              message is printed:
              - "wrong type" if an element is not a number
              - "division by 0" if division by zero is attempted
              - "out of range" if the index is out of bounds

    Note:
        Uses try/except/finally blocks as required. No modules are imported.
    """
    list_results = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            list_results.append(result)
        except ZeroDivisionError:
            print("division by 0")
            list_results.append(0)
        except TypeError:
            print("wrong type")
            list_results.append(0)
        except IndexError:
            print("out of range")
            list_results.append(0)
        finally:
            pass
    return list_results
