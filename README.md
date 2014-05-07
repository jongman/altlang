## In progress

## About 

This is a companion for a talk regarding working with domain experts who are not necessarily programming experts. This repository contains a _simulated_ code revision history from someone who wants to solve an arbitrary optimization problem (copied shamelessly from topcoder marathon matches, as the exact background of the probem is less relevant). 

The goal of the exercise is to understand the problem, figure out what the domain expert is trying to do, and then come up with a way to improve the process.

Note the author starts off well, but as she tries different things, she fails to come up with a good workflow and the code starts to rot. Can you improve her process?

Unfortunately, the rest of the process is Korean only.

## 소개

이 리포지토리는 도메인 전문가와 일하는 경험에 관해 이야기하기 위한 도구입니다. 이 리포지토리에는 간단한 최적화 문제를 풀려고 시도하는 어떤 가상의 도메인 전문가의 코드가 들어 있습니다. 이 전문가는 프로그램 전문가는 아니기 때문에, 처음에는 좋은 코드로 시작하지만 다양한 방법들을 시도하면서 코드가 더러워지고, 좀더 효율적인 프로세스의 필요성을 느끼게 됩니다.

이 도메인 전문가가 풀려는 문제가 무엇인지, 어떻게 문제를 풀려고 하는지 이해하고, 프로세스의 병목을 찾아 이를 향상시키는 연습을 해 봅시다. 우리의 프로그래밍 지식으로 어떻게 이 프로세스를 개선할 수 있을까요?

다음 사항들에 유념하세요.

* 도메인 전문가는 자신이 어떤 문제를 갖고 있는지, 어떻게 하면 더 효율적으로 연구를 할 수 있을지 모를 수도 있습니다. 항상 이와 같은 방식으로 연구해왔기 떄문입니다.
* 시간과 자원이 제한되어 있습니다. 이 도메인 전문가의 업무를 개선하는 것은 당신의 주 업무가 아닐 수도 있습니다. 따라서 "20% 시간"에 이와 같은 일을 한다고 생각하세요. 
* 도메인 전문가는 스스로 사용하던 방법/습관에 애착을 가지고 있을 수도 있고, 따라서 당신이 제안하는 방법을 사용하지 않거나 맘에 들어하지 않을 수도 있습니다. 40시간을 들여 거대한 테스트 프레임워크를 만들어 오기 전에, 가능한한 빠르게 이터레이션하고 피드백을 얻을 수 있는 방법이면 좋습니다.

다음은 도메인 전문가의 글입니다.

----

## 문제

* n개의 원소(0..n-1)를 일렬로 순서를 정해 늘어놓아야 한다. 순열 중 가능한한 점수가 높은 순열을 찾고 싶다.
* 순열의 점수는 점수 배열 W를 사용해 다음과 같이 정의된다.
* i < j인 모든 숫자 쌍 (i, j)에 대해 순열에 숫자 i가 숫자 j보다 먼저 올 경우, W[i][j]를 더한다.
* 각 입력 파일마다 30초의 시간이 주어진다.

## 입력 파일 형식

* 입력 파일은 텍스트 파일로 주어진다.
* 텍스트 파일의 첫 줄에는 원소의 개수 n(10 <= n <= 100)이 주어진다.
* 그 후 n줄에는 각 n개의 실수로 점수 배열 W가 주어진다. i+1번째 줄의 j+1번째 숫자는 W[i][j]를 나타낸다.

## 알고리즘

* n개의 원소를 일렬로 늘어놓는 방법의 수는 n!인데, n이 20만 되어도 19자리 숫자가 된다. 따라서 시간제한 안에 모든 순열을 검사해 최적해를 찾아내는 것은 불가능하다.
* 따라서 시간 안에 적절한 근사해를 찾아내기 위해, 메타 휴리스틱 알고리즘인 [담금질 기법](http://en.wikipedia.org/wiki/Simulated_annealing)을 사용하도록 하자. ([한글 위키피디아 링크](http://ko.wikipedia.org/wiki/%EB%8B%B4%EA%B8%88%EC%A7%88_%EA%B8%B0%EB%B2%95))
	* [알고스팟 링크](http://algospot.com/forum/read/1211/)
* 담금질 기법을 사용하기 위해서는 다음과 같은 것들을 정해야 한다:
	* 매 단계에서 어떻게 답을 바꿀 것인가?
	* 온도를 어떻게 변화시킬 것인가?
	* 초기해를 어떻게 정할 것인가?

## 평가 기준

* 점수의 합을 사용할 경우 큰 입력에 너무 유리하기 떄문에, 각 입력에 대해 존재하는 숫자 쌍의 개수로 점수를 나눠 숫자쌍당 평균 점수를 구하도록 하자.
