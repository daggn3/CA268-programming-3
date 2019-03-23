#
#   Arrange a list so that when added to a tree will cause the tree to be completely balanced
#
def make_list(lst, nlst = None):
    lst = sorted(lst)
    if not nlst:
        nlst = list()
    if len(lst) == 0:
        return nlst

    i = len(lst)//2
    if lst[i] not in nlst:
        nlst.append(lst[i])
    return make_list(lst[i+1:], nlst) and make_list(lst[:i], nlst)