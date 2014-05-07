# -*- coding: utf-8 -*-
from glob import glob
from time import time
from math import exp, sqrt, log
from random import random, randint, seed

TIME_LIMIT = 3

def score(W, perm):
    "순열과 점수 배열이 주어질 떄 점수를 반환한다."
    return sum(W[perm[i]][perm[j]]
               for j in xrange(len(W))
               for i in xrange(j))

def perturb(W, perm, current_score):
    "순열을 적당히 바꾼 결과와 새 점수를 반환한다."
    n = len(W)
    i, j = randint(0, n-1), randint(0, n-1)
    if i > j: i, j = j, i
    
    perturbed = list(perm)
    perturbed[i], perturbed[j] = a, b = perturbed[j], perturbed[i]
    
    # .. b [] [] [] [] a .. 에서
    # .. a [] [] [] [] b .. 로 바뀌었을 때 점수 변화는?
    for k in xrange(i+1, j):
        m = perturbed[k]
        current_score += W[m][b] - W[b][m]
        current_score += W[a][m] - W[m][a]
    current_score += W[a][b] - W[b][a]

    return current_score, perturbed

def perturb2(W, perm, current_score):
    "두 원소의 위치를 바꾸는 대신 한 원소를 골라 다른 곳에 끼워넣는다."
    
    n = len(W)
    i, j = randint(0, n-1), randint(0, n-1)
    perturbed = list(perm)
    
    # perturbed[i]가 perturbed[j]로 간다
    moved = perturbed[i]
    if i < j:
        for k in xrange(i, j):
            perturbed[k] = perturbed[k+1]
            current_score += W[perturbed[k]][moved] - W[moved][perturbed[k]] 
        perturbed[j] = moved
    elif i > j:
        for k in xrange(i, j, -1):
            perturbed[k] = perturbed[k-1]
            current_score += W[moved][perturbed[k]] - W[perturbed[k]][moved] 
        perturbed[j] = moved
    return current_score, perturbed

def solve(W):
    "점수 배열 W가 주어질 때 가능한 좋은 답을 찾는다."

    n = len(W)

    # 초기해를 정한다
    # TODO: 그리디로 초기해를 정해본다
    sol = range(n)
    current_score = score(W, sol)

    # 현재까지의 최적해를 저장한다
    best = list(sol)
    best_score = current_score

    # 초기 온도를 정한다
    # TODO: 크기에 따라 초기 온도를 바꿔본다
    initial_temp = 10 

    start_time = time()
    time_limit = start_time + TIME_LIMIT
    
    iterations = 0
    while True:
        if iterations % 100 == 0:
            latest_time = time()
            elapsed = latest_time - start_time
            remaining = time_limit - latest_time
            if latest_time >= time_limit:
                break
        iterations += 1

        # 현재 온도를 계산한다. 온도는 경과 시간에 맞춰 변화한다.
        # t = (time_limit - latest_time) / TIME_LIMIT * initial_temp
        # 온도를 선형보다 빨리 낮춘다
        t = ((time_limit - latest_time) / TIME_LIMIT) ** 2 * initial_temp
        # t = ((time_limit - latest_time) / TIME_LIMIT) ** 1.5 * initial_temp
        # t = ((time_limit - latest_time) / TIME_LIMIT) ** 3 * initial_temp

        # TODO: 다른 perturbation 방법을 적용해 본다
        # TODO: 점수 계산을 더 빨리 해본다
        # new_score, new_sol = perturb(W, sol, current_score)
        new_score, new_sol = perturb2(W, sol, current_score)
        
        # 최적해 갱신되었는가?
        if new_score > best_score:
            # print ' time %.2lf iteration %d: best score update %.4lf => %.4lf' % \
            #         (elapsed, iterations, best_score, new_score)
            best_score = new_score
            best = list(new_sol)

        # 이 변화를 받아들일 것인가?
        # TODO: 입력 크기에 비례해 받아들일지 결정하기
        if ((new_score > current_score) or
            (t > 0 and exp((new_score - current_score) / t) >= random())):
            current_score = new_score
            sol = new_sol

    print 'ran %d iterations. score %.4lf' % (iterations, best_score)
    return best

def read_data(filename):
    "파일 경로가 주어질 때 점수 배열 W를 읽어들인다."
    with open(filename) as f:
        n = int(f.readline())
        W = [map(float, f.readline().strip().split())
             for i in xrange(n)]
    return W

def testbench():
    "data 디렉토리의 모든 파일을 읽어들여 풀어본다."
    seed(0xdeadbeef)
    scores = []
    for f in glob('data/input*.txt'):
        W = read_data(f)
        n = len(W)
        print f, 'n =', n
        perm = solve(W)
        avg_score = score(W, perm) / (n * sqrt(n * log(n) - n))
        print 'raw score = %.4lf avg score = %.4lf' % (score(W, perm), avg_score)
        scores.append(avg_score)

    print 'Scores =', scores
    print 'Average = %.4lf' % (sum(scores) / len(scores))


if __name__ == '__main__':
    testbench()
