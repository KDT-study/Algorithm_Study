# 체인법으로 해시 구현, linked list의 형태가 된다.

# 해시 내용 참고 ( 자세히 설명 )
# https://mangkyu.tistory.com/102

# __future__ 모듈 ( class constructor에서 자기 자신을 받을 수 있는 방법 )
# https://ryanking13.github.io/2018/07/12/python-37-whats-new.html
from __future__ import annotations

# typing 모듈 ( Sequence형 등을 지정할 수 있다. )
from typing import Any, Type

# 해시값을 구하기 위한 라이브러리, str형도 해시값을 구할 수 있다.
import hashlib



class Node:

    # 노드는 key 값, value 값, 다음 노드를 가리키고 있는 next 3가지로 이루어져 있다.
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key   = key    # 키
        self.value = value  # 값
        self.next  = next   # 뒤쪽 노드를 참조


class ChainedHash:

    # 비어있는 해시 테이블을 만든다.
    def __init__(self, capacity: int) -> None:

        self.capacity = capacity             # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언,
                                             # 처음에는 테이블 안에는 모두 None만 있다.


    # 우리가 찾는 key의 해시값을 구하는 func
    def hash_value_int(self, key : Any):
        if isinstance(key, int):             # key == 어떤 타입인지 확인하는 함수( 내장함수 )
            return key % self.capacity      # int값인 key인 데이터들은 대부분 배열의 크기를 나눈 나머지로 구한다.

    # string 등의 type을 가지고 있는 key의 해시값 구하는 func
    # ( int도 가능하게 설정되어 있지만 위에 새로 만들었다. )

    # def hash_value(self, key: Any) -> int:
    #     """해시값을 구함"""
    #     if isinstance(key, int):
    #         return key % self.capacity
    #     return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)


    # value를 넣을 필요가 없다. 즉,해시에서 데이터를 찾을 때에는 'key'만을 이용해서 찾는다.
    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value_int(key)  # 검색하는 키의 해시값을 구한다.
        # hash = self.hash_value(key\
        p = self.table[hash]         # 노드를 노드

        while p is not None:             # 노드가 계속 연결되어 있으면 다음 다음, 가면서 계속 찾는다.
            if p.key == key:             # p의 key와
                 return p.value  # 검색 성공
            p = p.next           # 뒤쪽 노드를 주목

        return None              # 검색 실패

    # 새로운 데이터를 추가하는 함수
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 삽입"""
        hash = self.hash_value_int(key)  # 삽입하는 키의 해시값
        p = self.table[hash]         # 주목하는 노드

        while p is not None:
            if p.key == key:         # 이미 같은 키값이 있는 경우!
                                     # 어떤 문제가 생길 수 있을까?
                return False         # 삽입 실패
            p = p.next               # 뒤쪽 노드에 주목

        temp = Node(key, value, self.table[hash])   # 새로운 노드를 만들고,
                                                    # 원래 table[hash]가 가리키던 노드를 참조해야 한다.
        self.table[hash] = temp      # 노드를 삽입
        return True                  # 삽입 성공

    # key 찾아서 제거하는 함수
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value_int(key)  # 삭제할 키의 해시값
        p = self.table[hash]         # 주목하고 있는 노드
        pp = None                    # 바로 앞 주목 노드
                                    # 왜 바로 앞의 node를 알고 있어야 할까?

        while p is not None:
            if p.key == key:  # key를 발견하면 아래를 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  # key 삭제 성공
            pp = p
            p = p.next       # 뒤쪽 노드에 주목
        return False         # 삭제 실패(key가 존재하지 않음)

    # 해시 테이블 출력 : range(capacity)
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  → {p.key} ({p.value})', end='')  # 해시 테이블에 있는 키와 값을 출력
                p = p.next
            print()