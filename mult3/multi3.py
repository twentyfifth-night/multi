import cv2
import glob
import numpy as np
import sys


#ヒストグラム作成
def make_histogram(file):
    img = cv2.imread(file) #bgrの順番
    b = img[:,:,0] / 16 #blue
    b = b.astype(np.uint8)#切り捨てint
    b = b.ravel() #一次元に
    g = img[:,:,1] / 16 #green
    g = g.astype(np.uint8)
    g = g.ravel()
    r = img[:,:,2] / 16 #red
    r = r.astype(np.uint8)
    r = r.ravel()
    count_r = [0 for i in range(16)]#リスト宣言
    count_g = [0 for i in range(16)]
    count_b = [0 for i in range(16)]
    for i in r:
        count_r[i] += 1
    for i in g:
        count_g[i] += 1
    for i in b:
        count_b[i] += 1
    counter = [[count_r],[count_g],[count_b]]
    counter = np.ravel(counter)#一次元に
    return counter

#ユークリッド距離計算
def euc_distance(tg_histo,histo):#48次元
    #tgのヒストグラムとlist内のヒストグラムのユークリッド距離をとる
    # return 距離
    distance = 0
    for i in range(48):
        distance += (histo[i] - tg_histo[i])**2
    return distance

if __name__ == '__main__':
    data_path = '/Users/harakazuki/Desktop/univ/multi/101_ObjectCategories/BACKGROUND_Google/'#パス
    jpg_path = data_path + "*jpg"
    img_list = glob.glob(jpg_path)#カレントディレクトリ内のjpgファイルをリストにぶち込む
    img_list.sort()#順番に
    args = sys.argv #コマンドライン引数取ってくる
    tg_path = data_path + args[1] #targetのパス
    #tgのヒストグラム作成
    tg_histo = make_histogram(tg_path)

    euc_list = []
    for file in img_list:
        h_count = make_histogram(file) #ヒストグラム
        euc_dis = euc_distance(tg_histo,h_count) #tgとの距離計算
        euc_list.append(euc_dis) #リストへ入れていく
    euc_dic = dict(zip(img_list,euc_list))
    score_sorted = sorted(euc_dic.items(), key=lambda x:x[1])
    score_top = score_sorted[:10]
    for i in range(10):
        print("{}. {}".format(i+1,score_top[i][0]))
        print("(ユークリッド距離:{})".format(score_top[i][1]))
