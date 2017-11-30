from src.generic.utils import LinkedList


def test_create():
    l = LinkedList()


def test_fill_and_inspect():
    l = LinkedList()
    for x in range(100):
        l.add(x)
    test_values = [x for x in range(100)]
    for elem, test in zip(l, test_values):
        assert elem.data == test
