# Search



## Search, 검색 알고리즘이란?

내가 원하는 `데이터를 찾는다`는 뜻이다.

예를 들어, `list1 = ['a', 'b', 'c', 'd']`라는 `배열(리스트)`가 있다고 할 때

'c'가 있는 위치의 index를 찾는 것이 Search 입니다.



### Search 종류는?

1. __linear Search__
2. __Binary Search__
3. __Hash__



## Linear Search



### Linear Search란?

- 순차검색, Sequential Search 라고도 합니다. 차례대로 검색한다는 뜻



아까의 예시를 다시 들어볼까요? 코드로 구현해보면,

~~~python
def search(array, key):				# 찾으려는 값

	for i in range(array):			# 리스트에서 for
		if list1[i] == key:			# 찾으려는 값이 리스트 안의 값과 같다면
			return i				# 그 값의 리스트 인덱스 반환

        
array1 = ['a', 'b', 'c', 'd']
key = 'c'

print(search(array1, key))

~~~



< 해석 >

- list1의 index들에 대해서 차례대로 검색을 합니다.
- List의 0번 index부터 차례대로 내가 찾으려는 value가 맞는지 확인을 하는데, 
- 진행 중에 리스트의 어떤 위치에서 내가 찾는 key 값을 찾았다면?!
- 그러면 for을 더 수행하지 않고 return

​     -> 맨 뒤에서부터 차례대로 검색해도 상관 없다.



* 가장 쉬운 검색 알고리즘이고, 누구나 익숙하게 생각하는 알고리즘이다.



* Sequential Search의 최악의 경우 Time Complexity

  O(n) = n

  



<< __problem__ >>

* 하지만 0~99까지의 index를 가지고 있는 list 안에서 찾으려는 key가 list의 맨 끝에 있다고 한다면?

​      -> Sequential Search는 맨 앞에서부터 총 100번의 compare를 해야 한다.



* 1000개의 데이터 중에서 찾는다면? 1000번 비교

  -> 데이터의 개수가 많아질수록 힘들어진다.



* 수많은 데이터에서 하나를 찾는다고 생각하면 비교하는 part에서 시간 낭비가 된다.

​       그래서 Sequential Search보다 더 효율적인 알고리즘이 있다.!





## Binary Search



### Binary Search란?



* 한국말로 이진 검색, sequence형을 2개로 잘라서 검색하는 알고리즘.



< 가장 중요한 점! >

1. <u>__정렬(Sort)__</u>이 되어 있어야 합니다.

   오름차순 혹은 내림차순 정렬이 되어 있어야 한다는 뜻.

   

__ex__ ) list2 = [11, 12, 13, 14, 15, __16__, 17, 18, 19, 20, 21]



11개의 데이터가 들어있는 리스트에서, 14의 index를 찾는다고 합시다.

먼저 리스트에서 가운데 index의 데이터를 봅니다.

가운데 index를 계산하는 방법 = ( 맨 왼쪽의 index + 맨 오른쪽의 index) / 2 )

위의 예시에서는 (0 + 10) / 2 = 5

List[5] = 16이므로, 우리가 찾는 14가 아닙니다. 14는 16보다 작네요?

그 list에서 왼쪽의 리스트에 있겠구나! 라고 생각을 하는 거에요.

왼쪽 부분으로 제한을 해서 가운데를 보면, 13입니다!

13은 14보다 작으니, 13에서 오른쪽만 보는거에요.

left = 3, right = 4, (left + right) / 2 = 3

( 이렇게 배열에서 중간을 찾기 애매한 경우에는 나머지를 떼고 계산한 index를 사용하면 됩니다. )

index=3의 데이터를 보니, 14가 맞으니, 찾은겁니다.

비교를 하고, 아! 여기보다는 왼쪽에 있구나, 오른쪽에 있구나.

라고 판단을 해야 하기 때문에 기본적으로 정렬이 되어 있어야 한다.





```python
def BinarySearch(array, key, low, high)
	if low > high:		# 예외 처리
    	return false

	mid = (low+high) / 2  # 나누기를 했을 때 나머지는 신경 안쓴다.

	if value < array[mid]:			# 우리가 찾는 값이 가운데 기준 왼쪽에 있다는 의미
		return binarySearch(array, value, low, mid-1)
	elif array[mid] < value:		# 우리가 찾는 값이 가운데 기준 오른쪽에 있다는 의미
		return binarySearch(array, value, mid+1, high)
	else:
    	return mid
```



* Binary Search의 최악의 경우 Time Complexity

  : O(n) = log(n)







### Binary Search와 Linear Search 비교



* 비교하는 입장에서만 생각해 보면?



* 최소의 경우에는?!

  `Linear Search` : 최소 1번의 비교

  `Binary Search` : 최소 1번의 비교

  → 어떻게 보더라도, `Binary Search`가 유리합니다.



* 최악의 경우에는?

`Linear Search` : 데이터가 10개라고 하면 __최대 10번__의 비교 수행

`Binary Search` : 데이터가 10개라고 하면, __최대 4번__의 비교 수행

  →  가장 오래 비교한다고 했을 때, `Binary Search`가 압도적으로 유리해요.



* 기본적인 차이점은,

`Linear Search` : 정렬이 되든, 안되든 상관이 없다. 한 쪽에서부터 순차적으로 같은지만 확인한다.

`Binary Search` : 필수적으로 정렬이 되어 있는 상태이어야 한다.









## Hash, 해시법

* 데이터의 검색 뿐만 아니라, 추가, 삭제 등에도 용이한 알고리즘

  

### hash의 특징

- 해싱된 키(Hash Key)를 가지고 배열의 인덱스로 사용하기 때문에 **삽입, 삭제, 검색이 매우 빠르다**.
- 해시 함수(Hash Function)를 사용하는데 **추가적인 연산이 필요**하다.
- 해시 테이블(Hash Table)의 크기가 유한적이고 해시 함수(Hash Function)의 특성상 **해시 충돌(Hash Collision)이 발생**할 수 밖에 없다.
- 충돌이 없거나 적으면 O(1)의 상수 시간에 가까워지고, 충돌이 발생하면 할수록 성능은 점점 O(n)에 가까워진다. ( 극단적 경우 )



* int 값들이 들어있는 key의 해시 함수는 ```나누기``` 함수가 대표적이다.



Ex. list3 = [ 5, 7, 20, 31, 37, 53, 78, 6 ]이 있다고 하면,

​	해시 함수 : x % 7, key를 7로 나눈 나머지가 해시 값이 된다.



| list3                        | 5    | 7    | 20   | 31   | 37   | 53   | 78   | 6    |
| ---------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| key를 해싱한 값 ( 나누기 7 ) | 5    | 0    | 6    | 3    | 2    | 4    | 1    | 6    |



* hash Table에는 이렇게 들어간다.

| hash index | 0    | 1    | 2    | 3    | 4    | 5    | 6    |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| hash value | 5    | 78   | 37   | 31   | 53   | 5    | 20   |
|            |      |      |      |      |      |      | 6    |



~~~python
# 체인법으로 해시 구현, linked list의 형태가 된다.

# 해시 내용 참고 ( 자세히 설명 )
# https://mangkyu.tistory.com/102

# __future__ 모듈 ( class constructor에서 자기 자신을 받을 수 있는 방법 )
# https://ryanking13.github.io/2018/07/12/python-37-whats-new.html
from __future__ import annotations

# typing 모듈 ( Sequence형 등을 지정할 수 있다. )
from typing import Any, Type

# 해시 function에 사용되는
# 해시값을 구하기 위한 라이브러리, str형, 문자열도 해시값을 구할 수 있다.
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
~~~



* Hash Function을 통해서 나누기를 했는데, 같은 해시값이 나올 수 있다!



ex. 예를 들어 % 7이 hash function이라고 했을 때, 2개의 데이터의 key가 각각 8, 15라고 한다면,

​     둘 다 나누기 7을 한 나머지는 1이 된다. List의 index 1에는 데이터가 하나만 들어갈 수 있지 않을까?



<< 여기서 해결 방법은? >>

1. chained hash을 활용한다.
2. open hash을 활용한다.





### Chained hash



* chained hash는 해시 함수를 통해 나온 값이 같은 데이터를, chain 모양의 linked list(연결 리스트)로 연결하는 방법이다.



```python
# Chained Hash 

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
        if isinstance(key, int):             # key == 어떤 type인지 확인하는 함수( 내장함수 )
            return key % self.capacity      # int값인 key인 데이터들은 대부분 배열의 크기를 나눈 나머지로 구한다.


    # value를 넣을 필요가 없다. 즉,해시에서 데이터를 찾을 때에는 'key'만을 이용해서 찾는다.
    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value_int(key)  # 검색하는 키의 해시값을 구한다.
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
                    				 # 이 문제에 따라 chained hash 와 open hash 2가지로 나뉜다!
               
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
```





### Open Addressing



* open addressing는 hash collision이 발생 했을 때 rehashing(재해시)를 통해 빈  버킷을 찾아 데이터를 추가하는 방법이다.

* open addressing

* chaining처럼 지정한 메모리 외에 추가적인 저장공간이 필요가 없다.

* 삽입,삭제시 오버헤드가 적다.

  * **오버헤드**(overhead)는 어떤 처리를 하기 위해 들어가는 간접적인 처리 시간 · 메모리 등을 말한다.

* 저장할 데이터가 적을 때 더 유리하다. 

    → 저장할 데이터가 많을 경우에는 chained hash가 더 유리할 수 있다.



```python
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


```

