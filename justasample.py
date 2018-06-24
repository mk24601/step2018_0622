#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):#2点間の都市の距離を計算する関数
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):#問題を解く関数
    N = len(cities) #Nは都市の数

    dist = [[0] * N for i in range(N)] #各都市間の経路を保存する配列を定義
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j]) #関数distanceを使って各都市間の経路を算出

    current_city = 0 #現在0番の点にいる
    unvisited_cities = set(range(1, N)) #まだ訪れてない点のリストを作成
    tour = [current_city] #通路を保持する

    while unvisited_cities: #まだ訪れてない点が存在する限り
        #############################################
        #############################################
        ### ここで何かしらの処理をしてnext_cityを決める(それが宿題のメイン！)
        next_city = 
        #############################################
        #############################################
        
        current_city = next_city #next_cityに移動
    return tour #経路を処理結果として返す


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
