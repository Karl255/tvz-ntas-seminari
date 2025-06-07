from binaryTree import Movie

import fnmatch
import random

from basicBinaryTree import *
from binaryTree import lr, dr, BinaryTree


def searchInTree(root, item):
    if root:
        if fnmatch.fnmatch(root.value.short, item):
            return root.value
        else:
            if root.value.short > item:
                return searchInTree(root.left, item)
            else:
                return searchInTree(root.right, item)
    return "Doesn't exist!"


def searchRankInTree(root, start, end, l=[]):
    if root:
        if root.value.short.lower() >= start.lower() and root.value.short.lower() <= end.lower():
            l = [root.value]
            if root.left:
                l = searchRankInTree(root.left, start, end) + l
            if root.right:
                l = l + searchRankInTree(root.right, start, end)
        elif root.value.short.lower() < start.lower():
            l = l + searchRankInTree(root.right, start, end)
        elif root.value.short.lower() > end.lower():
            l = searchRankInTree(root.left, start, end) + l

        '''
        if root.value.short.lower() > start.lower() and root.value.short.lower()<end.lower():
            l = [root.value]
        if root.left:
            l = searchRankInTree(root.left, start, end) + l
        if root.right:
            l = l + searchRankInTree(root.right, start, end)
            '''
    return l


def getMinInTree(root, mini=None):
    if root:
        if not mini:
            mini = root.value
        if root.value.short < mini.short:
            mini = root.value
        if root.left:
            mini = getMinInTree(root.left, mini)
        return mini


def getMaxInTree(root, maxi=None):
    if root:
        if not maxi:
            maxi = root.value
        if root.value.short > maxi.short:
            maxi = root.value
        if root.right:
            maxi = getMaxInTree(root.right, maxi)
        return maxi


def ispisRotacijaKodDodavanja(tree, item):
    tree.add(item, True)


def stepenice(root, d=dict(), b=0):
    if root:
        if b < 10:
            d[b].append(root.value)
        else:
            return d
        if root.left or root.right:
            b += 1
            if root.left:
                stepenice(root.left, d, b)
            if root.right:
                stepenice(root.right, d, b)
    return d


def ispisStabla(myTree):
    d = dict()
    for i in range(10):
        d[i] = []
    d = stepenice(myTree.root, d)
    for i in d:
        if i % 2 == 1:
            print(i, ": ", sorted(d[i], reverse=True))
        else:
            print(i, ": ", d[i])


def usporediStabla(items):
    vals=items.copy()
    br = random.randint(1, len(vals) - 1)
    l = []
    for i in range(br):
        if len(vals)>0:
            l.append(vals.pop(random.randint(0, len(vals)-1)))
        else:
            l.append(vals.pop())
    root = None
    for item in l:
        item = Movie(item)
        root = addItem(root, item)
    myTree = BinaryTree()
    for i in l:
        myTree.add(i)
    print("Basic tree - ", root.height, "   :   ", end="")
    print(myTree.root.height, " -  AVL tree")
