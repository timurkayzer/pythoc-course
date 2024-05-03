list1 = [1, 2, 3, 4]
list2 = list("abcd")
assert "d" == list2.pop(3)
assert list("abc") == list2
list1.insert(2, 5)
assert [1, 2, 5, 3, 4] == list1
list2.pop(0)
list2.reverse()
assert ["c", "b"] == list2
list3 = list1.copy()
list3.clear()
assert list3 == []
assert [1, 2, 5, 3, 4] == list1