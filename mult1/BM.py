import time

class BM_search:
    def __init__(self,key,text):#key設定
        #文字とスキップ数の登録
        self.text = text
        self.key = key
        self.n = len(self.key)
        self.m = len(self.text)
        rev_key = []
        for i in range(self.n):#逆順リスト
            rev_key.append(self.key[-(i+1)])
        self.key_list = [[],[]]#二次元配列宣言
        for i,word in enumerate(rev_key):
            if word not in self.key_list[0] and i > 0:
                self.key_list[0].append(word)
                self.key_list[1].append(i)

    def Skip(self,c):
        if self.n > 1: #keyが1文字の時のために作成
            for i,w in enumerate(self.key_list[0]):
                if w == c:
                    return (self.key_list[1][i])
                elif w != c and i == len(self.key_list[0])-1:
                    return self.n
        else:
            return 1

    #BM法
    def search(self):
        pos = self.n - 1
        while pos < self.m:
            if self.text[pos] == self.key[self.n-1]:
                if pos > 0:
                    k = pos - 1
                else:
                    k = 0
                if self.n > 2:
                    j = self.n - 2
                else:
                    j = 0
                while j > 0 and self.text[k] == self.key[j]:
                    k -= 1
                    j -= 1
                if j == 0:
                    print ("{}番目にあります".format(pos-(self.n-1)))
            pos += self.Skip(self.text[pos])

if __name__ == '__main__':
    f = open("sample.txt","r") #ファイルオープン
    text = f.read()
    BM = BM_search("C",text) #インスタンス
    BM.search()
    f.close()#ファイルクローズ
