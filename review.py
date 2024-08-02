import unittest
from typing import List
from threading import Lock


# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


# Review 2
def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."


# Review 3
class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count


# Review 4
import threading


class SafeCounter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


# Review 5

def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1
        else:
            counts[item] = 1
    return counts


# Please find below as my review and fix solutions. -- Patrick
"""
Review 1
Issue found: 
In the provided code, if you call the method like below twice, you will not get 2 lists as expected. Instead, 
you will get a list contains the 2 elements. The reason is the default value of a parameter is evaluated only 
once when the function is defined, not each time the function is called.
add_to_list(1)
add_to_list(2) 
Test method test_to_reproduce_review_1_issue() below can reproduce this issue.

Fix: 
Below is my fix, additional check is added. So we can make sure everytime we call the method, either we get a 
new list, or we get our list back with value added.
Test method test_add_to_list_fixed() below shows the fix is in place.
"""


def add_to_list_fixed(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list
# End of fix for review 1


"""
Review 2
Issue found: 
In the provided code, the input params: name and age are not reflected output string. Grammar issue in  
f-string, AKA "formatted string literal.", has caused this issue.
Test method test_format_greeting_issue() below can reproduce this issue.

Fix: 
Grammar issue has been corrected for f-string. 
Test method test_format_greeting_fixed() below shows the issue is fixed.
"""


def format_greeting_fixed(name, age):
    return f"Hello, my name is {name} and I am {age} years old."
# End of fix for review 2


"""
Review 3
Issue found: 
In this simple implementation of object counter class, while the counter is not working, since the count attribute is 
a instance attribute. Instance attribute is not shared accross objects.
Test method test_Counter() below can reproduce the issue. 
Fix:
The count should be class attribute.
Test method test_CounterFixed() shows the above issue is fixed.
"""


class CounterFixed:
    count = 0

    def __init__(self):
        CounterFixed.count += 1

    def get_count(self):
        return self.count
# End of fix for review 3


"""
Review 4
Issue found: 
The SafeCounter class provided appears to implement a thread safe manner.  While in the increment() method, when 
multiple threads are access the counter object's count attribute. This is a multi-thread race condition issue.

Fix: 
To eliminate the race condistion, we need to make sure only one thread can access the resource at on point of time.
So a Lock is needed, when update the value of 'count' attribute. The fix of code would be in SafeCounter class.
"""


class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()  # Create a lock

    def increment(self):
        with self.lock:     # Each thread needs to get the lock before entering the critical zone
            self.count += 1     # Thread will release lock after updating shared resource: count


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
# End of fix for review 4


"""
Review 5
Issue found: 
The count_occurrences(lst) tries to count the occurrences of each element in list, while there is a grammar issue
"counts[item] =+ 1", which is causing issue. What is does here is assign +1 to the expression on the left side of 
the equal operator.

Fix:
"counts[item] =+ 1" -> "counts[item] += 1"
"""


def count_occurrences_fixed(lst):
    counts = {}
    for item in lst:
        if item in counts:
            # print(f"{item} is in counts, which is {counts}")
            counts[item] = counts[item] + 1
        else:
            # print(f"{item} is not in counts, which is {counts}")
            counts[item] = 1
        # print(counts)
    return counts
# End of fix for review 5


class UnitTest(unittest.TestCase):

    # Test cases for review 1
    def test_add_to_list_issue(self):
        """
        This is used for reproducing issue of review 1.
        """
        add_to_list(1)
        list_2: List[int] = add_to_list(2)
        self.assertNotEqual(list_2, [2])

    def test_add_to_list_fixed(self):
        """
        This test case will pass. This is used for testing fixed code of review 1.
        """
        add_to_list_fixed(1)
        list_2: List[int] = add_to_list_fixed(2)
        self.assertListEqual(list_2, [2])
    # End of Test cases for review 1

    # Test cases for review 2
    expect_string: str = "Hello, my name is Alice and I am 18 years old."

    def test_format_greeting_issue(self):
        """
        This is used for reproducing issue of review 2.
        """
        self.assertNotEqual(self.expect_string, format_greeting("Alice", 18))

    def test_format_greeting_fixed(self):
        """
        This test case will pass. This is used for testing fixed code of review 2.
        """
        self.assertEqual(self.expect_string, format_greeting_fixed("Alice", 18))
    # End of Test cases for review 2

    # Test cases for review 3
    def test_Counter(self):
        """
        This is used for reproducing issue of review 3.
        """
        counter1: Counter = Counter()
        counter2: Counter = Counter()
        self.assertNotEqual(2, counter1.get_count())
        self.assertNotEqual(2, counter2.get_count())

    def test_CounterFixed(self):
        """
        This test case will pass. This is used for testing fixed code of review 3.
        """
        counter1: CounterFixed = CounterFixed()
        self.assertEqual(1, counter1.get_count())
        counter2: CounterFixed = CounterFixed()
        self.assertEqual(2, counter2.get_count())
        counter3: CounterFixed = CounterFixed()
        self.assertEqual(3, counter2.get_count())
    # End of Test cases for review 3

    # Test cases for review 5
    list1: List[int] = [9, 9, 8, 7, 6, 5, 5]
    occurrences: dict[int: int] = {9: 2, 8: 1, 7: 1, 6: 1, 5: 2}

    def test_count_occurrences(self):
        """
        This is used for reproducing issue of review 5.
        """
        self.assertNotEqual(self.occurrences, count_occurrences(self.list1))

    def test_count_occurrences_fixed(self):
        """
        This test case will pass. This is used for testing fixed code of review 5.
        """
        self.assertDictEqual(self.occurrences, count_occurrences_fixed(self.list1))
    # End of Test cases for review 5

