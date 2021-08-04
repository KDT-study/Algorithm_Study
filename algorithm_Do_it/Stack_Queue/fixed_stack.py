# 고정 길이의 스택 클래스 FixedStack 구현하기
# Do it! 실습 4-1 [A]

# typing 모듈, 타입 지정에 사용된다.
from typing import Any

# 고정된 크기의 stack 클래스 만들기
class FixedStack:

    # 예외 클래스를 만들어서 예외처리를 할 때 쓰인다.
    # https://dojang.io/mod/page/view.php?id=2401
    class Empty(Exception):
        """비어 있는 FixedStack에 pop 또는 peek를 호출할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedStack에 push를 호출할 때 내보내는 예외 처리"""
        pass

    # capacity를 지정해주지 않을 경우, 256이라는 capacity의 스택을 만든다.
    def __init__(self, capacity: int = 256) -> None:
        # stk는 capacity라는 크기로 이루어진 리스트
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity      # 스택의 크기
        # ptr, 스택 포인터라고 한다. 스택 포인터는 데이터의 개수를 말하면서,
        # bottom부터 top까지 데이터가 차있는 개수를 의미하기도 한다.
        self.ptr = 0                  # 스택 포인터

    """ stack에 쌓여 있는 데이터의 개수를 확인하는 함수, ptr을 반환한다. """
    def __len__(self) -> int:
        return self.ptr

    """스택이 비어 있는지의 True, False를 확인하는 함수"""
    def is_empty(self) -> bool:
        return self.ptr <= 0

    """스택은 가득 찼는지를 확인하는 함수, True False 를 리턴해준다."""
    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    """데이터를 넣는 push 함수"""
    def push(self, value: Any) -> None:
        """스택에 value를 푸시"""
        if self.is_full():             # 가득 차있는 경우에는 넣지 못한다.
            raise FixedStack.Full
        self.stk[self.ptr] = value      # 가득 차있지 않은 경우에는, ptr 자리에 값을 넣는다.
        self.ptr += 1                   # ptr의 위치를 1 올린다.

        # ex. 스택에 아무것도 없는 상태에서 push를 수행하면?
        # 데이터, value를 넣고 나서
        # ptr = 0+1 = 1이 된다.
        # 데이터는 스택의 index=0에 있을 것이고, 그 다음에 또 push를 수행할 때에는 index=1에 들어갈 것이다.

    """데이터를 빼내는 pop 함수, """
    # 데이터의 종류는 int 뿐만 아니라 여러가지 종류가 다 될수 있으므로 return은 Any, 데이터 타입을 의미
    def pop(self) -> Any:
        if self.is_empty():             # 스택이 비어 있음
             raise FixedStack.Empty     # 예외처리
        self.ptr -= 1                   # ptr은 top의 데이터 위치 다음을 가리키고 있으므로 -1을 먼저 해주고,
        return self.stk[self.ptr]       # top의 데이터를 뽑아온다.


    """ pop함수와 Peek 함수를 헷갈리지 말자! 헷갈릴 경우 Push pop! 이라고 외우자. """

    """ top의 데이터의 value가 무엇인지 확인하는 peek 함수"""
    # 데이터의 value를 리턴하므로, 리턴값은 Any 타입
    def peek(self) -> Any:
        if self.is_empty():             # 스택이 비어 있음
            raise FixedStack.Empty      # 예외를 수행하는 문이 raise
                                        # 그대로 실행하는 문장인데, raise로 표시해서 예외의 경우를 실행한다는 뜻
                                        # 눈에 보이는 코드로 작성했다고 보면 된다.

        return self.stk[self.ptr - 1]   # ptr-1의 데이터를 리턴해야 한다.

    """ stack 내의 모든 데이터를 비워버리는 함수 """
    def clear(self) -> None:
        self.ptr = 0


    """ stack 내에 그 데이터가 있는지를 확인하는 find 함수 """
    # __contains__ 메소드에서는 있는지 없는지의 여부(True, False)만을 알려준다.
    # find 함수에서는 그 데이터의 위치를 return한다.
    def find(self, value: Any) -> Any:
        # ptr-1(꼭대기)부터 0(맨 아래)까지 순차적으로 검색
        # why? 스택 안에 우리가 찾는 데이터가 2개 이상, 즉 여러 개가 있다고 가정해보자.
        # 우리가 그 데이터를 꺼내야 하는 경우 맨 꼭대기 기준으로 가장 가까이에 있는 데이터를 꺼내야 하기 때문이다.
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:        # 내가 찾으려는 값이 stack 안에 있는 경우!
                return i  # 검색 성공         # 그 데이터의 위치를 return
        return -1         # 검색 실패         # 아닐 경우에는 -1, 못 찾았다는 뜻


    """ 스택 안에 그 value가 몇 개가 들어 있는지 개수를 확인하는 count 함수 """
    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.ptr):  # index=0부터 index=ptr-1까지 순차 검색(선형 검색)
            if self.stk[i] == value:
                c += 1             # 들어 있음
        return c                    # 만일 아예 없는 경우라면 0을 return할 것이다.
                                    # 0은 bool 값으로 False


    # 클래스에 내장되어 있는 컨테이너 메소드라고 한다.
    # stack에 value가 있는지를 확인하는 메소드로 많이 쓰인다.
    def __contains__(self, value: Any) -> bool:
        return self.count(value)            # count 함수에서 True False로 리턴될 것이다.


    """ stack 안의 데이터를 전부 출력하는 함수 ( bottom부터 top까지 출력 )"""
    def dump(self) -> None:
        if self.is_empty():  # 스택이 비어 있음
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])  # 0~ ptr-1까지 출력된다.