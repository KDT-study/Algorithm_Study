# Open Hashing

from __future__ import annotations
from typing import Any, Type
import hashlib

# enum이란?
from enum import Enum

# 버킷의 속성 ( Enum 이해 )
# 열거형 타입이다.
# https://docs.python.org/ko/3/library/enum.html
class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1     # 비어 있음
    DELETED = 2   # 삭제 완료

# 해시 테이블을 구성하는 bucket class
class Bucket:

    def __init__(self, key: Any = None, value: Any = None,
                       stat: Status = Status.EMPTY) -> None:
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    # Bucket의 모든 value setting ( add 함수에 사용 )
    def set(self, key: Any, value: Any, stat: Status) -> None:

        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    # stat만 바꾸는 함수, remove 함수에 필요하다
    def set_status(self, stat: Status) -> None:
        self.stat = stat    # 속성만 setting


# open addressing 구현하는 hash 클래스
class OpenHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity                 # 해시 테이블의 크기를 지정
        self.table = [Bucket()] * self.capacity  # 안에는 빈 버킷으로
                                                 # capacity의 용량만큼 이루어져 있는 해시 테이블

    # chained hash와 동일한 hash function
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)


    # rehash function, 재해시를 해야 하는 경우 사용
    def rehash_value(self, key: Any) -> int:
        return(self.hash_value(key) + 1) % self.capacity


    # key를 넣고, 그 키와 일치하는 버킷의 위치 return
    def search_node(self, key: Any) -> Any:
        """키가 key인 버킷을 검색"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목

        for i in range(self.capacity):      # 한바퀴 다 돌면서 찾기

            # empty status 이면 그냥 없다고 판단
            if p.stat == Status.EMPTY:      # EMPTY 만나면 Key에 맞는 노드는 없다.
                break

            # OCCUPIED : 데이터 저장되어 있다!
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p                    # p의 위치 return

            # OCCUPIED 상태인데 key가 같지 않다면, 그 위치의 데이터는 재해시되서 들어온 값이다.
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]

        return None                         # return의 값은 None 아니면 버킷의 index


    # key를 가지고 검색을 해서, 그 key에 맞는 value return
    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value  # 검색 성공
        else:
            return None     # 검색 실패


    # 빈 버킷을 찾아서 key & value를 추가하는 함수
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 요소를 추가"""
        if self.search(key) is not None:        # 검색 실패가 아닌 경우!
            return False             # 이미 등록된 키

        hash = self.hash_value(key)  # 추가하는 키의 해시값 구하기
        p = self.table[hash]         # 버킷을 주목
        for i in range(self.capacity):      # 왜 range(self.capacity) 만큼일까?
                                            # 원래 처음 버킷부터 한바퀴를 다 돌아야 하므로.
                                            # empty or delete된 경우에는 그 자리에 추가!
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]

        # 모든 버킷이 가득 차 있는 경우, 추가하지 못한다.
        return False


    # key에 해당하는 데이터를 제거하는 함수
    def remove(self, key: Any) -> int:
        p = self.search_node(key)  # 버킷을 주목( 일단 찾기 )
        if p is None:              # 못 찾은 경우!
            return False           # 이 키는 등록되어 있지 않음
        p.set_status(Status.DELETED)
        return True

    # 출력 함수
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i] .stat == Status.DELETED:
                print('-- 삭제 완료 --')


if __name__ == "__main__":
    pass
