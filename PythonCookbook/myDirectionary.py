from collections import defaultdict


def normalDict():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    print(d['a'])
    print(d['b'])

from collections import OrderedDict
# 严格按照元素的初始添加顺序排序
# 通常ordereddict的大小是普通字典的两倍，因为需要维护记录词条生成顺序的的链表。
def ordereDict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['grok'] = 4
    d['spam'] = 3

    for key in d:
        print(key, d[key])


if __name__ == '__main__':
    ordereDict()