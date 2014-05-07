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
    initial_temp = 250

    start_time = time()
    time_limit = start_time + TIME_LIMIT
    
    iterations = 0
    while True:
        if iterations % 100 == 0:
            latest_time = time()
            elapsed = latest_time - start_time
            if latest_time >= time_limit:
                break
        iterations += 1

        # 현재 온도를 계산한다. 온도는 경과 시간에 맞춰 변화한다.
        # TODO: 선형 외 다른 온도 낮추는 방법을 사용해 본다
        t = (time_limit - latest_time) / TIME_LIMIT * initial_temp

        # TODO: 다른 perturbation 방법을 적용해 본다
        # TODO: 점수 계산을 더 빨리 해본다
        i, j = randint(0, n-1), randint(0, n-1)
        if i == j: continue
        sol[i], sol[j] = sol[j], sol[i]
        new_score = score(W, sol)
        
        # 최적해 갱신되었는가?
        if new_score > best_score:
            print ' time %.2lf iteration %d: best score update %.4lf => %.4lf' % \
                    (elapsed, iterations, best_score, new_score)
            best_score = new_score
            best = list(sol)

        # 이 변화를 받아들일 것인가?
        if ((t > 1e-8 and exp((new_score - current_score) / t) >= random()) or
            (t <= 1e-8 and new_score > current_score)):
            current_score = new_score
        else:
            sol[i], sol[j] = sol[j], sol[i]

    print 'ran %d iterations' % iterations
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
        print 'score = %.4lf' % avg_score
        scores.append(avg_score)

    print 'Scores =', scores
    print 'Average = %.4lf' % (sum(scores) / len(scores))


if __name__ == '__main__':
    testbench()
