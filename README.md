# 문제

* n개의 원소(0..n-1)를 일렬로 순서를 정해 늘어놓아야 한다. 순열 중 가능한한 점수가 높은 순열을 찾고 싶다.
* 순열의 점수는 점수 배열 W를 사용해 다음과 같이 정의된다.
* i < j인 모든 숫자 쌍 (i, j)에 대해 순열에 숫자 i가 숫자 j보다 먼저 올 경우, W[i][j]를 더한다.
* 각 입력 파일마다 30초의 시간이 주어진다.

# 입력 파일 형식

* 입력 파일은 텍스트 파일로 주어진다.
* 텍스트 파일의 첫 줄에는 원소의 개수 n(10 <= n <= 100)이 주어진다.
* 그 후 n줄에는 각 n개의 실수로 점수 배열 W가 주어진다. i+1번째 줄의 j+1번째 숫자는 W[i][j]를 나타낸다.

# 알고리즘

* n개의 원소를 일렬로 늘어놓는 방법의 수는 n!인데, n이 20만 되어도 19자리 숫자가 된다. 따라서 시간제한 안에 모든 순열을 검사해 최적해를 찾아내는 것은 불가능하다.
* 따라서 시간 안에 적절한 근사해를 찾아내기 위해, 메타 휴리스틱 알고리즘인 [담금질 기법](http://en.wikipedia.org/wiki/Simulated_annealing)을 사용하도록 하자. ([한글 위키피디아 링크](http://ko.wikipedia.org/wiki/%EB%8B%B4%EA%B8%88%EC%A7%88_%EA%B8%B0%EB%B2%95))