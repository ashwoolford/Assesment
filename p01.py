'''
Time and Memory complexity analysis

-->Time complexity<--

* every step program print one element until the total number of keys,

so costs of the program as follows: 1+2+3+.....+n

Hence time complexity of this program is linear or O(n)

-->Space/Memory<--

* The recursive calls of this program does not save its state to the Stack, 
and there are no other data structure to store data,
So we can consider the Space complexity of this program is O(1).

'''

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}


def print_depth(data, depth=1):
    for key in data:
        print(key, depth)
        if isinstance(data[key], dict):
            print_depth(data[key], depth+1)


# print_depth(a)
