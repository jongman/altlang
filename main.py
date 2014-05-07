# -*- coding: utf-8 -*-
from glob import glob
from time import time

TIME_LIMIT = 10

def solve(W):
    "점수 배열 W가 주어질 때 가능한 좋은 답을 찾는다."
    return range(len(W))

def score(W, perm):
    "순열과 점수 배열이 주어질 떄 점수를 반환한다."
    return sum(W[perm[i]][perm[j]]
               for j in xrange(len(W))
               for i in xrange(j))

def read_data(filename):
    "파일 경로가 주어질 때 점수 배열 W를 읽어들인다."
    with open(filename) as f:
        n = int(f.readline())
        W = [map(float, f.readline().strip().split())
             for i in xrange(n)]
    return W

def testbench():
    "data 디렉토리의 모든 파일을 읽어들여 풀어본다."
    for f in glob('data/input*.txt'):
        W = read_data(f)
        print f, 'n =', len(W)
        perm = solve(W)
        print 'score = %.4lf' % score(W, perm)


if __name__ == '__main__':
    testbench()
