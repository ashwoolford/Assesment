'''
Time and Memory complexity analysis

-->Time complexity<--

* every step program prints one element until the total number of keys,

so total costs of the program as follows: 1+2+3+.....+n

Hence time complexity of this program is linear or O(n)

-->Space/Memory<--

* The recursive calls of this program does not save its state to the Stack, But in order to create 
Dictionary it costs linear space which is proportional to number of keys
So we can consider the Space complexity of this program is O(n)

'''


def print_depth(data, depth=1):
    for key in data:
        print(key, depth)
        if isinstance(data[key], dict):
            print_depth(data[key], depth+1)


# print_depth(a)
