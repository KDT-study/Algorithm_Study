# 고정 길이 큐 클래스 FixedQueue 구현하기
# Do it! 실습 4-3 [A]

""" ring buffer 를 이용한 Queue 구현 """

# type 지정 모듈 사용
from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue에 대해 deque 또는 peek를 호출할 때 내보내는 예외처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedQueue에 enque를 호출할 때 내보내는 예외처리"""
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0     # 현재 데이터 개수
        self.front = 0  # 맨앞 원소 커서
        self.rear = 0   # 맨끝 원소  커서
        self.capacity = capacity      # 큐의 크기
        self.que = [None] * capacity  # 큐의 본체(리스트)

    """ queue 안에 몇개의 데이터가 있는지! """
    def __len__(self) -> int:
        return self.no


    """ queue 안에 데이터가 비어있는지 확인하는 is_empty 함수 """
    def is_empty(self) -> bool:
        return self.no <= 0

    """ queue 안에 데이터가 가득 찼는지 확인하는 is_full 함수"""
    def is_full(self) -> bool:
        return self.no >= self.capacity     # queue의 데이터 개수와 queue 용량을 비교.
            # >= 라고 표기한 이유는, 혹시나 생길 예외적인 상황? 을 대비한 듯 함.
            # 하지만 그냥 = 이라고 해도 가능! 문제는 없습니다.

    """ queue에 데이터를 넣는 enque 함수"""
    def enque(self, x: Any) -> None:

        if self.is_full():
            raise FixedQueue.Full   # 큐가 가득 찬 경우 예외처리를 발생
                                    # fixed_stack의 링크 참고
                                    # raise가 발생하고 나면, 아래 코드는 실행하지 않고 끝난다.
        self.que[self.rear] = x     # 데이터를 넣을 rear 위치에 넣는다.
        self.rear += 1              # rear은 가장 최근에 들어온 데이터 다음 위치를 가리켜야 한다.
        self.no += 1                # 큐 안의 데이터 개수 + 1

        # ring buffer이 적용되는 중요한 부분!
        if self.rear == self.capacity:  # 이 경우는 rear의 위치가 리스트의 맨 끝 index 다음에 있는 경우!
                                        # ( 즉, 리스트의 뒷쪽 index가 꽉 차있는 경우 )
            self.rear = 0               # rear을 0으로 옮겨야 한다. 맨 끝 index 다음 index는 0이다!

    """ queue에서 데이터를 빼는 deque 함수 """
    def deque(self) -> Any:

        if self.is_empty():
            raise FixedQueue.Empty  # 큐가 비어 있는 경우 예외처리를 발생

        x = self.que[self.front]    # 맨 앞의 데이터를 빼낼 것이므로, front의 데이터를 뺀다.
        self.front += 1             # front의 값을 1 더한다. 원래 맨 앞의 데이터 값이 빠져 나갔으니깐.
        self.no -= 1                # queue 데이터 개수 - 1하고

        # ring buffer이 적용되는 부분!
        if self.front == self.capacity:     # front가 리스트의 맨 끝 index에서 다음에 있는 경우!!
            self.front = 0                  # 맨 끝 index 다음 index는 0이다!
        return x                    # 데이터 return

    """ 우리가 바로 빼낼 수 있는 맨 앞의 데이터를 들여다보는 peek 함수 """
    def peek(self) -> Any:

        if self.is_empty():
            raise FixedQueue.Empty  # 큐가 비어 있으면 예외처리를 발생
        return self.que[self.front] # 맨 앞의 데이터를 return한다. 하지만 값을 뽑아내는 것은 아니다. 명심!

    """ Queue 내에서 value를 찾아, 그 index을 반환하는 find 함수 """
    def find(self, value: Any) -> Any:
        # for 구문에서, 우리가 가장 먼저 확인해야 하는 위치는 front이다.
        # for에서 i가 계속 커지는데, rear이 capacity를 넘어서 배열의 앞 index에 있을 수도 있다.
        # 그러므로 (i+self.front) % self.capacity는, front부터 검사할 때,
        # 배열의 맨 끝에 도달해서 맨 앞으로 가야 하는 경우까지 고려한 식이다.
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 검색 성공
                return idx              # 바로 만난 경우에 idx의 위치를 return
                                        # 중요한 점은, idx 다음 어딘가의 index에도 같은 데이터가 있을 수는 있다.
                                        # queue에 있을 때 value가 같은 데이터가 여러개가 있을 수 있는데,
                                        # dequeue 하기에 있어서 가장 가까운 위치의 index를 return하는 것이다.
        return -1  # 검색 실패


    """ queue에 value값이 같은 데이터가 몇 개가 있는지 확인하는 count """
    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.no):  # 큐 데이터를 선형 검색
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 검색 성공
                c += 1  # 들어있음
        return c

    """ 컨테이너 메소드, 클래스 내에 이미 정의되어 있는 __contains__ 메소드이다."""
    """ 여기서는 queue 내에 데이터가 있는지 확인하는 메소드로 만들었다."""
    def __contains__(self, value: Any) -> bool:
        """큐에 value가 포함되어 있는지 판단합니다"""
        return self.count(value)

    """ 큐의 데이터 모두 비우는 clear 함수 """
    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    """ 모든 데이터를 맨 앞에서 맨 끝 순서로 출력하는 dump 함수"""
    def dump(self) -> None:
        if self.is_empty():  # 큐가 비어 있으면 예외처리를 발생
            print('큐가 비어 있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()