
class BinNode:
    def __init__(self, left, value, right):
        self.__left = left
        self.__value = value
        self.__right = right
    def GetValue(self):
        return self.__value
    def GetRight(self):
        return self.__right
    def GetLeft(self):
        return self.__left
    def SetRight(self, right):
        self.__right = right
    def SetLeft(self, left):
        self.__left = left
    def SetValue(self, value):
        self.__value = value

def PreOrder(t):
    if t != None:
        print(t.GetValue(), end= "  ")
        PreOrder(t.GetLeft())
        PreOrder(t.GetRight())

def InOrder(t):
    if t != None:
        InOrder(t.GetLeft())
        print(t.GetValue(), end= "  ")
        InOrder(t.GetRight())

def PostOrder(t):
    if t != None:
        PostOrder(t.GetLeft())
        PostOrder(t.GetRight())
        print(t.GetValue(), end= "  ")


def PrintLeavs(t):
    if (t!=None):
        if (t.GetRight() == None and t.GetLeft() == None):
            print(t.GetValue(), end = '  ')
            return
        PrintLeavs(t.GetLeft())
        PrintLeavs(t.GetRight())
def CountNodes(t):
    if(t==None):
        return 0
    return 1+CountNodes(t.GetLeft())+CountNodes(t.GetRight())
def SumValues(t):
    if(t==None):
        return 0
    return t.GetValue() + SumValues(t.GetLeft()) + SumValues(t.GetRight())
def Height(t):
    if(t==None):#
        return 0




b = BinNode(None, 3, None)
Height(b)
b.SetLeft(BinNode(None, 8, None))
b.GetLeft().SetRight(BinNode(None, 7, None))
b.GetLeft().SetLeft(BinNode(None, 5, None))
print(SumValues(b))
b.GetLeft().GetLeft().SetLeft(BinNode(None, 13, None))
b.SetRight(BinNode(None, 4, None))
b.GetRight().SetLeft(BinNode(None, 2, None));
b.GetRight().SetRight(BinNode(None, 1, None))
b.GetRight().GetRight().SetRight(BinNode(None, 7, None))
b.GetRight().GetRight().SetLeft(BinNode(None, 0, None));
print(CountNodes(b))
print(SumValues(b))
SumValues(b)

PreOrder(b)
print()
InOrder(b)
print()
PostOrder(b)
print()
PrintLeavs(b)
CountNodes(b)
