# Sequential Search 구현
# key : 내가 찾으려는 값
# array : 검색을 할 시퀀스형 ( 리스트, 튜플, 문자열 등 )
# 시퀀스형 : 순서들을 가진 요소들의 집합이라는 뜻
# cf) Dictionary : 시퀀스형이 아니다! 순서를 가지고 있지 않는 집합의 형태이므로.

from typing import Any, Sequence

def sequential_search(array : Sequence, key : Any) -> int:     #int 값을 return한다는 의미

    for i in range(len(array)): # array의 길이만큼 for 구문 적용
        if array[i] == key:     # 찾으려는 값(key)이 리스트 안에 있다면
            return i            # 그 값의 리스트 인덱스 반환
    return -1                   # -1은 못 찾았다는 의미


if __name__ == "__main__":

    print("\narray가 리스트인 경우---------")

    # array가 리스트인 경우
    array1 = ['a', 'b', 'c', 'd']
    key = 'c'
    print(sequential_search(array1, key))

    print("\narray가 튜플인 경우----------")

# array가 튜플인 경우
    array2 = ('a', 'b', 'c', 'd')
    key = 'c'
    print(sequential_search(array2, key))

    print("\narray가 문자열인 경우---------")
    # array가 문자열인 경우
    array3 = "abcd"
    key = "c"
    print(sequential_search(array3, key))