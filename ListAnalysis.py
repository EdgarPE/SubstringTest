import unittest


def identifySublist(digitCharList):
    """
    O(N) algorithm to find longest balanced sub-list.

    :param digitCharList: list
    :return: tuple (int, int) or (False, False)
    """
    idxBeg, idxEnd = False, False
    sumMap = {0: -1}
    sum = 0
    bestLen = 0
    for (pos, item) in enumerate(digitCharList):
        sum += (1 if type(item) == str else -1)
        if sum in sumMap:
            if pos - sumMap[sum] + 1 > bestLen:
                bestLen = pos - sumMap[sum] + 1
                idxBeg, idxEnd = sumMap[sum] + 1, pos
        else:
            sumMap[sum] = pos

    return idxBeg, idxEnd


class TestListAnalysis(unittest.TestCase):

    def testIdentifySublist(self):
        self.assertEqual((1, 6), identifySublist([0, 'a', 'c', 4, 1, 2, 'b', 0, 2, 3]))
        self.assertEqual((1, 4), identifySublist([0, 0, 'a', 0, 'a']))
        self.assertEqual((0, 5), identifySublist([0, 0, 'a', 0, 'a', 'a']))
        self.assertEqual((0, 1), identifySublist(['a', 0, 0, 0, 0, 'a']))
        self.assertEqual((0, 7), identifySublist(['a', 0, 0, 'a', 'a', 0, 0, 'a']))
        self.assertEqual((3, 6), identifySublist(['a', 0, 0, 0, 0, 'a', 'a', 0, 0, 0, 0, 'a']))
        self.assertEqual((0, 15), identifySublist(['a', 0, 0, 0, 0, 'a', 'a', 'a', 'a', 'a', 'a', 0, 0, 0, 0, 'a']))
        self.assertEqual((False, False), identifySublist(['a', 'a', 'a', 'a', 'a', 'a']))
        self.assertEqual((5, 6), identifySublist(['a', 'a', 'a', 'a', 'a', 'a', 0]))
        self.assertEqual((4, 7), identifySublist(['a', 'a', 'a', 'a', 'a', 'a', 0, 0]))
        self.assertEqual((3, 8), identifySublist(['a', 'a', 'a', 'a', 'a', 'a', 0, 0, 0]))
        self.assertEqual((2, 9), identifySublist(['a', 'a', 'a', 'a', 'a', 'a', 0, 0, 0, 0]))
        self.assertEqual((1, 10), identifySublist(['a', 'a', 'a', 'a', 'a', 'a', 0, 0, 0, 0, 0]))
        self.assertEqual((0, 11), identifySublist(['a', 'a', 'a', 'a', 'a', 'a', 0, 0, 0, 0, 0, 0]))
        self.assertEqual((False, False), identifySublist([0]))
        self.assertEqual((False, False), identifySublist(['a', 'a']))


if __name__ == '__main__':
    unittest.main()
