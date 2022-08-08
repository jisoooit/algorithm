
# 1. binary search란?
  
  
오름차순으로 정렬된 배열에서 원하는 숫자(target)을 찾는 알고리즘입니다.

- 배열 전체의 중간값을 target 값과 비교
- 중간값이 target 값보다 크면 왼쪽 부분만 선택
- 왼쪽부분의 중간값을 다시 target 과 비교

# 2.  이진 탐색의 시간 복잡도
  
  
- 이진 탐색은 탐색 횟수별로 확인하는 데이터의 개수가 절반씩 줄어들기 때문에 시간 복잡도가 O(log N) 입니다.

# 3. 이진 탐색의 구현

## 반복문

'''python
target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

while left<=right:
    mid = (left+right)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid]>target:
        right = mid-1
    else :
        left = mid+1
'''

## 재귀
'''python
def binarySearch(array, target, left, right):
    middle_idx = (left+right)//2
    print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        print('answer {}'.format(middle_idx))
    elif middle > target:
        binarySearch(array, target,left,middle_idx-1)
    elif middle < target:
        binarySearch(array, target,middle_idx+1,right)
    else: 
        return False

target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

binarySearch(m_list,target,0,right)
'''
