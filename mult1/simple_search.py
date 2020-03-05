import time

class Simple_search:
    def __init__(self,key,text):
        self.key = key
        self.text = text
        self.n = len(self.key)
        self.m = len(self.text)


    def search(self):
        for i in range(self.m-self.n+1):
            for j in range(self.n):
                if self.text[i+j] != self.key[j]:
                    break
                if j == self.n-1:
                    print("{}番目にあります".format(i))

if __name__ == '__main__':
    f = open("sample.txt","r")
    text = f.read()
    Simple = Simple_search("C",text)#インスタンス生成
    Simple.search()
