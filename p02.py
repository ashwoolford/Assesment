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


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", None, None)
person_b = Person("User", "2", person_a)


test = {
    "key1": {
        "key2": {
            "key3": 1
        }
    },
    "key4": {
        "key5": {
            "key6": 2
        }
    },
    "key7": {
        "key8": {
            "key9": 3
        }
    }
}


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user1": person_b,
            "key6": {
                "key7": 4,
            }
        }
    }
}


# Print function when it's an instance of Person

def print_for_person(k, depth):
    print(str(k)+': '+str(depth))


# Print function when it's an instance of dictionary

def print_for_dict(k, depth):
    print(str(k)+' '+str(depth))


# Driver function

def print_depth(data, depth=1):

    # If value of a key is Instance of Person

    if isinstance(data, Person):
        for k, v in vars(data).items():

            # Handling all of the properties of Person instance
            if isinstance(v, Person):
                print_for_person(k, depth)
                print_depth(v, depth+1)

            # Handling None property of Person instance
            else:
                print_for_person(k, depth)

    # When value of a key is Instance of dictionary

    else:
        for k, v in data.items():

            # A value of dictionary can be instance of either dict or Person

            # When value of a key is instance of dict

            if isinstance(v, dict):

                print_for_dict(k, depth)
                print_depth(v, depth+1)

            # When value of a key is instance of Person

            elif isinstance(v, Person):
                print_for_person(k, depth)
                print_depth(v, depth+1)

            # If value of a key is not another dict or Person instance
            else:
                print_for_dict(k, depth)


# print_depth(person_b)
