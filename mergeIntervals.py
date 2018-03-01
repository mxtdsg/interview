####
#
# merge overlapping invervals
#
# leetcode 56.
#
####


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    re = []
    for i in sorted(intervals, key=lambda i: i.start):
        if re and i.start <= re[-1].end:
            re[-1].end = max(re[-1].end, i.end)
        else:
            re += i,
    return re