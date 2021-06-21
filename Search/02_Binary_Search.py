# Sequential Search 구현
# key : 내가 찾으려는 값
# array : 검색을 할 시퀀스형 ( 리스트, 튜플, 문자열 등 )

from typing import Any, Sequence

# 이 함수의 중요한 특성은?! re
def binarySearch(array : Sequence, key : Any, left, right) -> int:

    if left > right:		# 예외 처리 ( 크기가 2인 시퀀스에서 찾는 경우 )
        return False
    mid = (left + right) // 2  # 나누기를 했을 때 나머지는 신경 안쓴다.

    # 이 아래가 비교하는 part
    if key < array[mid]:			# 우리가 찾는 값이 가운데 값보다 왼쪽에 있다면?
        return binarySearch(array, key, left, mid-1)

    elif array[mid] < key:		# 우리가 찾는 값이 가운데 값보다 오른쪽에 있다면?
        return binarySearch(array, key, mid+1, right)

    else:
        return mid



if __name__ == "__main__":

    array1 = [1, 3, 10, 26, 50, 198]
    key = 50
    print(binarySearch(array1, key, 0, len(array1)-1))

# array가 다른 시퀀스형인 경우는 생략