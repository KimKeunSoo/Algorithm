# Algorithm



## maximum subarray problem

주어진 배열에서 합이 가장 큰 구간을 찾는 문제.



O(N^3^) - Brute-force solution, 전체를 순서대로 탐색하는 방법

C++로 짤때, 모든 **여러 배열**의 합을 모두 탐색

```c
int maxSubarraySum()  
{  
    int input [] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};  
    size_t size = sizeof(input)/sizeof(int);  
  
    int i, j, k, sum;  
    int value = 0xFFFFFFFF;  
    for (i = 0; i < size; i++) {  
        for (j = 0; j < size; j++) {  
            sum = 0;  
            for (k = i; k <= j; k++) {  
                sum += input[k];  
            }  
            value = max(value, sum);   
        }  
    }  
    trace("%d\n", value);  
    return value;  
}  
```



O(N^2^) - Brute-force solution, 전체를 순서대로 탐색하는 방법

js로 짤때, 특정(인접안해도됨) **두 배열**의 합을 모두 탐색

```javascript
function maxSubarraySum(arr) {
  var n = arr.length;
  var sumArr = 0;
  //배열의 길이를 늘려나가는 반복문을 생성한다.
  for(var i = 1; i < n + 1; i++){
    //부분 배열의 시작점이 되는 반복문을 생성한다.
    for(var j = 0; j < n - i + 1; j++){
      //arr배열을 부분배열로 만든다.
      var cutArr = arr.slice(j, j + i);
      //부분 배열의 합을 구한다.
      var sumCutArr = cutArr.reduce(function(a, b){
        return a + b;
      })
      //합이 이 전의 합보다 크다면 변수를 바꾸고 그렇지 않다면 기존대로 유지한다.
      if(sumArr < sumCutArr){
        sumArr = sumCutArr;
      }
    }
  }
  return sumArr;
}
```



O(N^2^) - Brute-force solution, 전체를 순서대로 탐색하는 방법

C++로 짤때, 인접한 **두 배열**의 합을 모두 탐색

```c
int maxSubarraySum()
{  
    int input [] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};  
    size_t size = sizeof(input)/sizeof(int);  
  
    int i, j, sum;  
    int value = 0xFFFFFFFF;  
    for (i = 0; i < size; i++) {  
        sum = 0;  
        for (j = i; j < size; j++) {  
            sum += input[j];  
            value = max(value, sum);   
        }  
    }  
    trace("%d\n", value);  
    return value;  
}  
```



O(nlogn) - **Divide and Conquer algorithm**

```c
int input [] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};  
size_t size = sizeof(input)/sizeof(int);  
  
trace("%d\n", maxSubarraySum(input, 0, size - 1));  
  
int maxSubarraySum(int input[], int lo, int hi)  
{  
    // 하나 뿐일 때  
    if (lo == hi) return input[lo];  
  
    int mid = (lo + hi) / 2;  
  
    int left = 0xFFFFFFFF, right = 0xFFFFFFFF;  
    int sum = 0;  
  
    for (int i = mid; i >= lo; i--) {  
        sum += input[i];  
        left = max(left, sum);  
    }  
  
    sum = 0;  
    for (int j = mid + 1; j <= hi; j++) {  
        sum += input[j];  
        right = max(right, sum);  
    }  
  
    int single = max(maxSubarraySum(input, lo, mid), maxSubarraySum(input, mid+1, hi));  
    return max(left + right, single);  
}  
```



O(n) - Kadane's algorithm

```c
int maxSubarraySum()  
{  
    int input [] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};  
    size_t size = sizeof(input)/sizeof(int);  
  
    int max_so_far = input[0], max_ending_here = input[0];  
    for (int i = 1; i < size; i++) {  
        if (max_ending_here < 0) {  
            max_ending_here = input[i];  
            // begin_temp = i;  
        }  
        else {  
            max_ending_here += input[i];  
        }  
  
        max_so_far = max(max_ending_here, max_so_far);  
        //if (max_ending_here > max_so_far) {  
            // begin = begin_temp;  
            // end = i;  
        //}  
    }  
  
    trace("%d\n", max_so_far);  
    return max_so_far;  
}  
```



## Insertion Sort



```python
def insertion_sort(arr):
    for j in range(2, len(arr)):
        key = arr[j]
        i = j - 1 ## 바로 이전 값에 위치 가르킴
        while i > 0 and arr[i] > key: ## 몇번째 자리에 값을 넣어야하는지 찾는 과정
            arr[i + 1], arr[i] = arr[i], arr[i + 1] ## 조건 만족하면 바꾸기
            i -= 1
        arr[i + 1] = key
```





##  Merge Sort

합병 정렬. 

1. Divide (분할) : 입력 배열을 같은 크기의 2개의 부분 배열로 분할한다.

2. Conquer (정복) : 부분 배열을 정렬한다. 부분 배열의 크기가 충분히 작지 않으면 **순환 호출**을 이용하여 다시 분할 정복 방법을 적용.

3. Combine (결합) : 정렬된 부분 배열들을 하나의 배열에 합병한다.

   

항상 O(NlogN)이다. 또한 pivot에 무관하다는 점이 장점이다. 

하지만, 추가적인 메모리가 필요하고 데이터가 최악일때 별로 이다.



![img](README%20assets/merge-sort-concepts.png)



C 코드 구현

```c
#include <stdio.h>
#define MAX_SIZE 8
int sorted[MAX_SIZE]; // 추가적인 공간이 필요

    // i: 정렬된 왼쪽 리스트에 대한 인덱스
    // j: 정렬된 오른쪽 리스트에 대한 인덱스
    // k: 정렬될 리스트에 대한 인덱스
    /* 2개의 인접한 배열 list[left...mid]와 list[mid+1...right]의 합병 과정 */
    /* (실제로 숫자들이 정렬되는 과정) */
    void merge(int list[], int left, int mid, int right)
{
    int i, j, k, l;
    i = left;
    j = mid + 1;
    k = left;

    /* 분할 정렬된 list의 합병 */
    while (i <= mid && j <= right){
        if (list[i] <= list[j])
            sorted[k++] = list[i++];
        else
            sorted[k++] = list[j++];
    }

    // 남아 있는 값들을 일괄 복사
    if (i > mid){
        for (l = j; l <= right; l++)
            sorted[k++] = list[l];
    }
    // 남아 있는 값들을 일괄 복사
    else{
        for (l = i; l <= mid; l++)
            sorted[k++] = list[l];
    }

    // 배열 sorted[](임시 배열)의 리스트를 배열 list[]로 재복사
    for (l = left; l <= right; l++){
        list[l] = sorted[l];
    }
}

void merge_sort(int list[], int left, int right)
{
    int mid;

    if (left < right){
        mid = (left + right) / 2 ;          // 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
        merge_sort(list, left, mid); // 앞쪽 부분 리스트 정렬 -정복(Conquer)
        merge_sort(list, mid + 1, right);  // 뒤쪽 부분 리스트 정렬 -정복(Conquer)
        merge(list, left, mid, right);     // 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)
    }
}

void main()
{
    int i;
    int n = MAX_SIZE;
    int list[n] = {21, 10, 12, 20, 25, 13, 15, 22};

    // 합병 정렬 수행(left: 배열의 시작 = 0, right: 배열의 끝 = 7)
    merge_sort(list, 0, n - 1);

    // 정렬 결과 출력
    for (i = 0; i < n; i++){
        printf("%d\n", list[i]);
    }
}
```



#### 시간복잡도

- 분할 단계

  - 비교 연산과 이동 연산이 수행되지 않는다.

  

- 합병 단계

  ![img](README%20assets/sort-time-complexity-etc.png)

  - 비교 횟수

    - 순환 호출의 깊이 (합병 단계의 수) 

    - 레코드의 개수 n이 2의 거듭제곱이라고 가정(n=2^k^)했을 때, n=2^3^의 경우, 2^3^ -> 2^2^ -> 2^1^ -> 2^0^ 순으로 줄어들어 순환 호출의 깊이가 3임을 알 수 있다. 이것을 일반화하면 n=2^k^의 경우, k(k=log₂n)임을 알 수 있다.
    - k=log₂n

    

  - 각 합병 단계의 비교 연산

    - 크기 1인 부분 배열 2개를 합병하는 데는 최대 2번의 비교 연산이 필요하고, 부분 배열의 쌍이 4개이므로 24=8번의 비교 연산이 필요하다. 다음 단계에서는 크기 2인 부분 배열 2개를 합병하는 데 최대 4번의 비교 연산이 필요하고, 부분 배열의 쌍이 2개이므로 42=8번의 비교 연산이 필요하다. 마지막 단계에서는 크기 4인 부분 배열 2개를 합병하는 데는 최대 8번의 비교 연산이 필요하고, 부분 배열의 쌍이 1개이므로 8*1=8번의 비교 연산이 필요하다. 이것을 일반화하면 하나의 합병 단계에서는 최대 n번의 비교 연산을 수행함을 알 수 있다.
    - 최대 n번





- 순환 호출의 깊이 만큼의 합병 단계 * 각 합병 단계의 비교 연산 = nlog₂n

  - 이동 횟수

    - 순환 호출의 깊이 (합병 단계의 수)

      - k=log₂n

    - 각 합병 단계의 이동 연산

      - 임시 배열에 복사했다가 다시 가져와야 되므로 이동 연산은 총 부분 배열에 들어 있는 요소의 개수가 n인 경우, 레코드의 이동이 2n번 발생한다.

      - 순환 호출의 깊이 만큼의 합병 단계 * 각 합병 단계의 이동 연산 = 2nlog₂n

        

- T(n) = nlog₂n(비교) + 2nlog₂n(이동) = 3nlog₂n = O(nlog₂n)





## Heap Sort



Array object, 하지만 binary tree와 매우 비슷

왼쪽부터 채움, 배열같이.

먼저 Heap에 넣고 Heapify를 한다. 그리고 나서 제일 상단의 노드를 빼서 맨 뒤로 놔두고 다시 Heapify를 한다.

추가적인 메모리가 필요없는 장점이 있다. 항상 O(nlogn)인 장점이 있다.

데이터 상태에 따라 조금 느릴 수 있다. Bestcase인 경우 Quick보다 느리다. 



length : 배열의 element의 수 

heap-size : heap에서의 element의 수

![image-20201015152752676](README%20assets/image-20201015152752676.png)



in c++

```c++
#include <iostream>
using namespace std;

// To heapify a subtree rooted with node i which is
// an index in arr[]. n is size of heap
void heapify(int arr[], int n, int i)
{
    int largest = i;   // Initialize largest as root
    int l = 2 * i + 1; // left = 2*i + 1
    int r = 2 * i + 2; // right = 2*i + 2

    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;

    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;

    // If largest is not root
    if (largest != i)
    {
        swap(arr[i], arr[largest]);

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

// main function to do heap sort
void heapSort(int arr[], int n)
{
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // One by one extract an element from heap
    for (int i = n - 1; i >= 0; i--)
    {
        // Move current root to end
        swap(arr[0], arr[i]);

        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}

/* A utility function to print array of size n */
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    cout << "\n";
}

// Driver program
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    heapSort(arr, n);

    cout << "Sorted array is \n";
    printArray(arr, n);
}
```







## Quick Sort

pivot을 설정하여 작은건 왼쪽 큰건 오른쪽에 둔다.

pivot을 설정하는 방법은 랜덤으로 줄 수도 있고 맨 왼쪽에도 줄수 있고 맨 오른쪽에도 줄 수 있다.

평균 case에 효율적이며, 가상 메모리 환경에서 사용하기 좋다. 하지만, pivot을 어떻게 설정하느냐에 따라 퍼포먼스가 매우 다름. Worst case인 unbalanced인 경우에는 오히려 Insertion Sort가 더 좋다.

Worst-case running time : Θ(n^2^)

Expected running time : Θ(nlogn)



![img](README%20assets/quick-sort2.png)



[left pivot]

```c
#include <stdio.h>
#include <stdlib.h> //랜덤함수 호출

void Swap(int arr[], int a, int b) // a,b 스왑 함수 
{
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
int Partition(int arr[], int left, int right)
{
    int pivot = arr[left]; // 피벗의 위치는 가장 왼쪽에서 시작
    int low = left + 1;
    int high = right;
 
    while (low <= high) // 교차되기 전까지 반복한다 
    {
        while (low <= right && pivot >= arr[low]) // 피벗보다 큰 값을 찾는 과정 
        {
            low++; // low를 오른쪽으로 이동 
        }
        while (high >= (left+1)  && pivot <= arr[high]) // 피벗보다 작은 값을 찾는 과정 
        {
            high--; // high를 왼쪽으로 이동
        }
        if (low <= high)// 교차되지 않은 상태이면 스왑 과정 실행 
        {
            Swap(arr, low, high); //low와 high를 스왑 
        }
    }
    Swap(arr, left, high); // 피벗과 high가 가리키는 대상을 교환 
    return high;  // 옮겨진 피벗의 위치정보를 반환 
 
}
 
 
void QuickSort(int arr[], int left, int right)
{
    if (left <= right)
    {
        int pivot = Partition(arr, left, right); // 둘로 나누어서
        QuickSort(arr, left, pivot - 1); // 왼쪽 영역을 정렬한다.
        QuickSort(arr, pivot + 1, right); // 오른쪽 영역을 정렬한다.
    }
}
 
//메인함수
int main()
{
    int n,i;
    int arr[100];

	
    printf("몇개의 숫자로 정렬하시겠습니까?\n");
    scanf("%d",&n);

	for(i = 0 ; i < n ; i++)
		 arr[i]=rand()%1000;

	 printf("정렬전 배열 :");
	 for(i = 0 ; i < n ; i++)
        printf("%d ", arr[i]);
	 printf("\n");

    QuickSort(arr,0,n-1);

	printf("정렬후 배열 :");
    for(i = 0 ; i < n ; i++)
        printf("%d ", arr[i]);
	printf("\n");

    return 0;
}
```



pseudo code

```c
QUICKSORT(A, p, r)
if p < r
	then q <- PARTITION(A, p, r)
		QUICKSORT(A, p, q-1)
		QUICKSORT(A, q+1, r)
//Initial call is QUICKSORT(A, 1, n)
    
PARTITION(A, p, r)
    x = A[r]
    i = p-1
    for j = p to r - 1
        if A[j] <= x
            i = i+1
            exchange A[i] with A[j]
    exchange A[i+1] with A[r]
    return i+1
```





## Q1. Find largest number possible from set of given numbers.

ex) 

input : {10, 68, 75, 7, 21, 12}

output : 77568211210



**Idea : 글자 자체를 XY 와 YX를 비교함. X>Y이라 할지라도 XY<YX 면 X<Y로 sorting**

[C++]

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;
 
// sort using a custom function object
struct {
    bool operator()(string a, string b)
    {
        string value1 = a + b;
        string value2 = b + a;
 
        return value1 > value2;
    }
} customCompare;
 
int main()
{
    vector<string> numbers = { "10", "68", "97", "9", "21", "12" };
 
    // custom sort
    sort(begin(numbers), end(numbers), customCompare);
 
    // print the sorted sequence
    for (const auto& elem : numbers) {
        cout << elem;
    }
 
    return 0;
}
```

Time complexity : O(nlog(n))

auxiliary space : O(1)



## Q2. Sort Binary Array in Linear Time

ex)

input : { 1,0,1,0,1,0,0,1 }

output : { 0,0,0,0,1,1,1,1 }



**Idea : 0의 갯수 확인 후 출력**

[Python]

```python
# Function to sort binary list in linear time
def sort(A):
    
    zeros = A.count(0)
    
    k = 0
    while zeros:
        A[k] = 0
        zeros = zeros - 1
        k = k + 1
 
    for k in range(k, len(A)):
        A[k] = 1
 
if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
 
    sort(A)
 
    # print the rearranged list
    print(A)
 
```

Time complexity : O(n)

Auxiliary space : O(1)



## Q3. Segregate positive and negative integers in linear time.

ex )

Input : [9, -3, 5, -2, -8, -6, 1, 3]

Output : [-3, -2, -8, -6, 5, 9, 1, 3]



**Idea : pivot을 0으로 둬서 Quicksort 사용**

[C++]

```c++
#include <iostream>
#include <algorithm>
using namespace std;
 
void partition(int a[], int start, int end)
{
    int pIndex = start;
 
    // each time we find a negative number, pIndex is
    // incremented and that element would be placed before
    // the pivot
    for (int i = start; i <= end; i++)
    {
        if (a[i] < 0)   // pivot is 0
        {
            swap(a[i], a[pIndex]);
            pIndex++;
        }
    }
}
 
int main()
{
    int a[] = { 9, -3, 5, -2, -8, -6, 1, 3 };
    int n = sizeof(a)/sizeof(a[0]);
 
    partition(a, 0, n - 1);
 
    // print the rearranged array
    for (int i = 0 ; i < n; i++)
        cout << a[i] << " ";
 
    return 0;
}
```

Time complexity : O(n)

Auxiliary space : O(1)



[Python]

```Python
def swap(a, i, j):
 
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
 
 
def partition(a, start, end):
 
    pIndex = start
 
    # each time we find a negative number, pIndex is incremented
    # and that element would be placed before the pivot
    for i in range(start, end + 1):
        if a[i] < 0:  # pivot is 0
            swap(a, i, pIndex)
            pIndex = pIndex + 1
 
 
if __name__ == '__main__':
 
    a = [9, -3, 5, -2, -8, -6, 1, 3]
    partition(a, 0, len(a) - 1)
    print(a)
```

Time complexity : O(n)

Auxiliary space : O(1)



## Linked List

![image-20201208160408069](README%20assets/image-20201208160408069.png)



Doubly linked list 의 장점

- 순방향 / 역방향 모두 이동 가능
- 삭제시 더 효율적
- 삽입시 더 효율적, 이전 노드를 가지고 오기 위해 순회될 필요 없이 이전 노드를 통해 빠르게 가능



Doubly linked list 의 단점

- DLL의 모든 노드 이전 포인터를 위한 추가 공간 필요(하지만, 단일 포인터(this)로 DLL 구현 가능)



Circular linked list 의 장점

- 모든 노드가 시작점이 될 수 있음
- Queue 구현에 효율적임 - 매번 맨앞에 포인터 두개를 가르키게 할 필요가 없음. 마지막 삽입 노드에 대해 포인터 유지, 항상 front는 end 다음으로 볼 수 있음.
- 애플리케이션에서 주기적으로 list를 반복 탐색하는데에 효율적임



## Stack

**블록 쌓아서 위에서부터 떼내기**

![image-20201208161458529](README%20assets/image-20201208161458529.png)



(LIFO) Last-in First-out

push & pop



## Queue

**들어온 순서대로 내보내기**

![image-20201208161517918](README%20assets/image-20201208161517918.png)

(FIFO) First-in First-out

Insertion (end에다가) & Deletion (front를)



## Q4. How do you find the middle element of a singly linked list in one pass?

1. 전체 갯수 탐색
   - 전체 연결 목록을 탐색하여 번호 계산 count를 계산하여 count/2의 노드 반환
2. 두개 포인터 사용
   - 하나의 포인터는 1만큼 이동하고 다른 포인터는 2만큼 이동.
   - 빠른 포인터가 끝에 도달하면 느린 포인터 반환



## Q5. How to find if a linked list has a loop?



1. **노드를 하나씩 순회하며 해쉬 테이블에 저장. 다음 노드가 1) NULL에 도달하면 false 반환, 2) Hash에 이전에 저장된 노드중 하나를 가르키면 true 반환**



```c++
#include <bits/stdc++.h> 
using namespace std; 

struct Node { 
    int data; 
    struct Node* next; 
}; 
  
void push(struct Node** head_ref, int new_data) 
{ 
    struct Node* new_node = new Node; 
  
    new_node->data = new_data;
    new_node->next = (*head_ref); 
    (*head_ref) = new_node; 
} 
 
bool detectLoop(struct Node* h) 
{ 
    unordered_set<Node*> s; 
    while (h != NULL) { 
        
        if (s.find(h) != s.end()) 
            return true; 
   
        s.insert(h); 
        h = h->next; 
    } 
  
    return false; 
} 
  
int main() 
{ 
    struct Node* head = NULL; 
  
    push(&head, 20); 
    push(&head, 4); 
    push(&head, 15); 
    push(&head, 10); 
  
    head->next->next->next->next = head; 
  
    if (detectLoop(head)) 
        cout << "Loop found"; 
    else
        cout << "No Loop"; 
  
    return 0; 
} 
```

Time Complexity : O(n)

Auxiliary Space : O(n)



2. **순회하며 flag 사용. 다음 노드가 flag가 1일시 true 반환.**



```c++
#include <bits/stdc++.h> 
using namespace std; 
  
struct Node { 
    int data; 
    struct Node* next; 
    int flag; 
}; 
  
void push(struct Node** head_ref, int new_data) 
{ 
    struct Node* new_node = new Node; 
    new_node->data = new_data; 
    new_node->flag = 0; 
  
    new_node->next = (*head_ref); 
  
    /* move the head to point to the new node */
    (*head_ref) = new_node; 
} 
  
// Returns true if there is a loop in linked list 
// else returns false. 
bool detectLoop(struct Node* h) 
{ 
    while (h != NULL) { 
        // If this node is already traverse 
        // it means there is a cycle 
        // (Because you we encountering the 
        // node for the second time). 
        if (h->flag == 1) 
            return true; 
  
        // If we are seeing the node for 
        // the first time, mark its flag as 1 
        h->flag = 1; 
  
        h = h->next; 
    } 
  
    return false; 
} 
  
/* Driver program to test above function*/
int main() 
{ 
    /* Start with the empty list */
    struct Node* head = NULL; 
  
    push(&head, 20); 
    push(&head, 4); 
    push(&head, 15); 
    push(&head, 10); 
  
    /* Create a loop for testing */
    head->next->next->next->next = head; 
  
    if (detectLoop(head)) 
        cout << "Loop found"; 
    else
        cout << "No Loop"; 
  
    return 0; 
} 
```

Time Complexity : O(n)

Auxiliary Space : O(n)



3. **Floyd의 주기 찾기 알고리즘 사용**
   - 하나의 포인터(slow_p)를 1만큼씩 이동하고 다른 포인터(fast_p)를 2만큼씩 이동한다.
     - 이러한 두개의 포인터가 동일한 노드에서 만나면 루프가 있다.
     - 이러한 두개의 포인터가 만나지 않으면 루프가 없다.



```c++
#include <bits/stdc++.h> 
using namespace std; 
 
class Node { 
public: 
    int data; 
    Node* next; 
}; 
  
void push(Node** head_ref, int new_data) 
{ 
    Node* new_node = new Node(); 
    new_node->data = new_data; 
    new_node->next = (*head_ref); 
  
    (*head_ref) = new_node; 
} 
  
int detectLoop(Node* list) 
{ 
    Node *slow_p = list, *fast_p = list; 
  
    while (slow_p && fast_p && fast_p->next) { 
        slow_p = slow_p->next; 
        fast_p = fast_p->next->next; 
        if (slow_p == fast_p) { 
            return 1; 
        } 
    } 
    return 0; 
} 
  
int main() 
{ 
    Node* head = NULL; 
  
    push(&head, 20); 
    push(&head, 4); 
    push(&head, 15); 
    push(&head, 10); 
  
    head->next->next->next->next = head; 
    if (detectLoop(head)) 
        cout << "Loop found"; 
    else
        cout << "No Loop"; 
    return 0; 
} 
```

Time Complexity : O(n)

Auxiliary Space : O(1)



## Q6. Reverse stack using recursion

**Idea : Stack이 빌때까지 모든 값을 가지고 있다가 비면 다시 밑에서부터 넣음**

```c++
#include<bits/stdc++.h> 
using namespace std; 
  
// using std::stack for stack implementation 
stack<char> st; 
  
// intializing a string to store result of reversed stack 
string ns; 
  
// Below is a recursive function that inserts an element at the bottom of a stack. 
char insert_at_bottom(char x) 
{ 
  
    if(st.size() == 0) 
    st.push(x); 
  
    else
    { 
        char a = st.top(); 
        st.pop(); 
        insert_at_bottom(x); 
  
        st.push(a); 
    } 
} 
  
char reverse() 
{ 
    if(st.size()>0) 
    { 
          
        // Hold all items in Function Call Stack until we reach end of the stack  
        char x = st.top(); 
        st.pop(); 
        reverse(); 
          
        // Insert all the items held in Function Call Stack one by one from the bottom  
        // to top. Every item is inserted at the bottom  
        insert_at_bottom(x); 
    } 
} 
  
// Driver Code 
int main() 
{ 
  
    st.push('1'); 
    st.push('2'); 
    st.push('3'); 
    st.push('4'); 
      
    cout<<"Original Stack"<<endl; 
      
    cout<<"1"<<" "<<"2"<<" "<<"3"<<" "<<"4"
        <<endl; 
      
    reverse(); 
    cout<<"Reversed Stack"
        <<endl; 
      
    while(!st.empty()) 
    { 
        char p=st.top(); 
        st.pop(); 
        ns+=p; 
    } 
      
    cout<<ns[3]<<" "<<ns[2]<<" "<<ns[1]<<" "<<ns[0]<<endl; 
    return 0; 
} 
```



## Graph

: G = (V, E)

**weight** for edge ==  w:E → R

**vertex** : 위치라는 개념으로 node라고도 부른다

**edge** : 위치간의 관계, node를 연결하는 선인 link라고도 부른다.

**degree** : Undirected graph에서 하나의 vertex에 인접한 vertex 수

- Undirected graph : (v1, v2) = 서로 연결되어 있다.
- Directed graph : <v1, v2> = v1 -> v2 로 연결되어 있다.

![image-20201208195959389](README%20assets/image-20201208195959389.png)

**Complete graph**

- Undirected graph = n(n-1)/2
- Directed graph = n(n-1)



**Planar graph** (평면 그래프)

평면상에 그래프를 그렸을때, 두 변이 꼭짓점 이외에 만나지 않도록 그릴 수 있는 그래프를 의미함

![image-20201208201255319](README%20assets/image-20201208201255319.png)

Euler's formula : n-m+r = 2

n : vertex의 개수
m : edge의 개수
r : 바깥쪽을 포함한 영역의 개수



## Tree

- Free tree
  - Undirected graph이지만 cycle이 없는 그래프
- T가 n 개의 vertex로 구성된 tree 라면,
  - T의 적어두 두개의 vertex가 하나의 path로 연결되어 있다.
  - T는 n-1개의 edge를 가지고 있다.
  - 한개의 edge를 추가하면 cycle이 된다.



Tree Traversal

![image-20201208203750910](README%20assets/image-20201208203750910.png)

- **Preoreder traversal**

  - Root 먼저, Top down

- **Inorder traversal**, 보통 Binary Search Tree를 순회할때는 이 방법을 사용

  - Subtree - root - Subtree

  - ```c
    Inorder-Tree-Walk(x)
    if x != NIL
    	then Inorder-Tree-Walk(left[x])
    		 print key[x]
    		 Inorder-Tree-Walk(right[x])
    ```

- **Postorder traversal**

  - Subtrees - root



## Binary Search Tree

![An Intro to Binary Search Trees. Beginner's guide to Binary Search Trees… |  by Eli Kantor | Level Up Coding](https://miro.medium.com/max/1194/1*ziYvZzrttFYMXkkV9u66jw.png)

8보다 작으니까 3은 왼쪽, 크니까 10은 오른쪽 



- h : height of tree
- root[T] : tree의 root
- key : node identification
- left, right : point to left, right
- p : parents
  - p[root[T]] = NIL



### 1. Retrieve/Find

**Find D using searching algorithm**

작으면 왼쪽 크면 오른쪽이라는 Binary Search Tree의 특성을 사용

```c
Tree-Search(x,k)
if x = NIL or k = key[x]
	then return x
if k < key[x]
	then return Tree-Search(left[x],k)
	else return Tree-Search(right[x],k)
	
//Initial call is Tree-Search(root[T],k)
```

Running time : O(h)		// h = heigt of tree



**Find Maximum and Minimum**

```c
Tree-Maximum(x)
while left[x] != NIL
    do x <- left[x]
return x
        
Tree-Minimum(x)
while right[x] != NIL
    do x <- right[x]
return x
```





### 2. Insert

**Insertion**

```c
Tree-Insert(T, z)
y <- NIL
x <- root[T]
while x != NIL
    do y <- x
        if key[z] < key[x]
            then x<- left[x]
		else x <- right[x]
p[z] <- y
if y = NIL
    then root[T] <- z		// Tree T was empty
else if key[z] < key[y]
    then left[y] <- z
else right[y] <- z
```

Running time : O(h) [linked list의 삽입의 Time complexity는 O(1)이므로 무시 가능]



### 3. Delete

**Deletion**

- Case 1 : 삭제할 노드 z의 child가 없을 경우
  - z 노드 삭제 후 z의 parent의 포인터를 NIL로 두기
- Case 2 :  삭제할 노드 z의 child가 1개 있을 경우
  - z 노드 삭제 후 z의 parent와 z의 child를 연결시켜주기
- Case 3 :  삭제할 노드 z의 child가 2개 있을 경우
  1. z의 Successor 노드를 찾는다.
  2. Successor의 값을 z에 덮어씌운다.
  3. Successor 노드를 삭제한다.





```c++
Node* deleteNode(Node* root, int k)
{
    // Stage 0. 기본 경우
    if (root == NULL)
        return root;
 
    // Stage 1. 삭제하고자 하는 node의 parent를 가르키는 root값 반환해주게함
    if (root->key > k) {
        root->left = deleteNode(root->left, k);
        return root;
    }
    else if (root->key < k) {
        root->right = deleteNode(root->right, k);
        return root;
    }
 
    // 일치 조건은 없기에 이 뒤로의 root는 삭제하려는 노드값을 가르키고 있음.
 
    // Stage 2-1. root의 child가 하나 또는 없는 상황, temp에 붙일 재료를 저장
    if (root->left == NULL) {
        Node* temp = root->right;
        delete root;
        return temp;
    }
    else if (root->right == NULL) {
        Node* temp = root->left;
        delete root;
        return temp;
    }
 
    // Stage 2-2. root의 child가 두개 모두 있는 상황.
    else {
        
        Node* succParent = root;
 
        // Stage 2-2-1. 우선, successor를 찾는다.
        Node* succ = root->right;
        while (succ->left != NULL) {
            succParent = succ;
            succ = succ->left;
        }
        
        // Stage 2-2-2-A. successor는 항상 succParent의 왼쪽 child이기 때문에,
		// 				  successor의 오른쪽 child를 successor의 자리에 붙일 수 있다.
        if (succParent != root)
            succParent->left = succ->right;
       
        // Stage 2-2-2-B. successor가 없으면, succParent->right에 succ->right를 할당한다.
        else
            succParent->right = succ->right;
 
        // Stage 2-2-3. 삭제하려던 root의 값에 successor의 값을 덮어씌운다.
        root->key = succ->key;
 
        // Stage 2-2-4. successor를 삭제하고 root로 return 한다.
        delete succ;
        return root;
    }
}
```





**Predecessor**
삭제 대상 노드의 왼쪽의 서브트리의 노드들 중에 제일 큰 값,
즉, Binary Search Tree를 Inorder traversal 했을때 삭제 대상보다 바로 전으로 작은 왼쪽의 수

Binary Search Tree의 구조상 <u>predecessor는 child가 무조건 하나이거나, 존재하지 않는다.</u>

**Successor** 
삭제 대상 노드의 오른쪽 서브트리의 노드들 중에 제일 작은 값,
즉, Binary Search Tree를 Inorder traversal 했을때 삭제 대상보다 바로 다음으로 큰 오른쪽의 수

Binary Search Tree의 구조상 <u>successor는 child가 무조건 하나이거나, 존재하지 않는다.</u>

```c
//Pseudo Code
Tree-Successor(x)
if right[x] != NIL
    then return Tree-Minimum(right[x])

y <- p[x]
while y != NIL && x = right[y]
    do x <- y
       y <- p[y]
return y
        
//C++ Code
Tree-Successor(x){
	Node* succ = x->right;
    while (succ->left != NULL) {
    	succParent = succ;
        succ = succ->left;
	}
return succ;
}

```

Running time : xx



## Balanced Tree의 종류

1. Red-Black Tree
2. AVL Tree



## 1. Red-Black Tree

- 얘도 Binary Search Tree(이진 탐색 트리)임. 여기다가 1bit를 더 써서 Black인지 Red인지를 나타냄
- Binary Search Tree는 search 연산이 최악의 경우 O(h)이지만 Red-Black Tree는 Balanced Binary Search Tree임.
- 따라서 h는 logn에 바운드되기 때문에 Red-Black Tree의 search 연산은 **O(logn)**의 Time Complexity를 가짐



![image-20201209170737006](README%20assets/image-20201209170737006.png)





### 가. Red-Black Tree의 조건

1. **Root Property** : **root node**의 색깔은 **검정(Black)**이다.
2. **External Property** : 모든 **external node**들은 **검정(Black)**이다.
3. **Internal Property** : **빨강(Red)노드의 자식**은 **검정(Black)**이다. 
   == No Double Red(빨간색 노드가 연속으로 나올 수 없다.)
4. **Depth Property** : **모든 leaf 노드**에서 **Black Depth는 같다.** 
   == 즉, <u>모든 NIL 노드는 Black</u>이며, 모든 노드에 대해서 자손인 leaf 노드에까지 이르는 모든 경로에는 동일한 개수의 블랙 노드가 존재해야 한다.



![image-20201209170957811](README%20assets/image-20201209170957811.png)

![image-20201209171036140](README%20assets/image-20201209171036140.png)





### 나. Double Red를 해결하는 전략

**현재 insert된 node [z]의 <u>uncle node[w]의 색깔</u>**에 따라 수행하는 과정이 다름.

Insertion 할때

1. **Restructuring** : 부모의 형제인 <u>w가 검정</u> 혹은 <u>NULL</u>일때

   W가 NULL이면,

      1. v가 조부모의 right child이면 left-rotation

      2. v가 조부모의 left child 이면 right-rotation


         이거 다하고


   1. 나[z]와 부모[v], 증부모를 오름차순으로 정렬
   2. 무조건 가운데 있는 값을 부모로 만들고 나머지 둘을 자식으로 만듬
   3. 올라간 가운데 있는 값을 검정(Black)으로 만들고 나머지 두 자식들을 빨강(Red)로 만듬

2. **Recoloring** : 부모의 형제인 <u>w가 빨강</u>일때

   1. 부모[v], uncle[w]를 검정(Black)으로 하고 증부모를 빨강(Red)로 한다.
   2. 증부모가 Root node가 아니었을 시 Double Red가 다시 발생할 수 있다.
      즉, 만약 증부모가 Root node이면 Black이여되는데 Red이니까 다시 올라가서 Restructuring과 Recoloring을 해야함 

Deletion 할때는 BST와 같음, 
대신 Red자리에 Black을 넣을시에는, Red로 변환해서 넣기
대신 Red자리에 Red 또는 NIL을 넣을시에는, 아무것도 안함

대신 Black자리에 Red를 넣을시에는, Black으로 변환해서 넣기

- Case 1 : 삭제할 노드 z의 child가 없을 경우
  - z 노드 삭제 후 z의 parent의 포인터를 NIL로 두기
- Case 2 :  삭제할 노드 z의 child가 1개 있을 경우
  - z 노드 삭제 후 z의 parent와 z의 child를 연결시켜주기
- Case 3 :  삭제할 노드 z의 child가 2개 있을 경우
  1. z의 Successor 노드를 찾는다.
  2. Successor의 값을 z에 덮어씌운다.
  3. Successor 노드를 삭제한다.

### 다. 변수명 및 특징



![image-20201209183026026](README%20assets/image-20201209183026026.png)

대략적인 구현 설계도. 실제 구현된 모습은 여기서 key 26의 노드가 NIL을 참조하고 있어야 완벽함.



- h(x) : Red-Black Tree의 높이, 자신으로부터 leaf 노드 까지 가장 긴경로에 포함되는 edge의 갯수

- Bh(x) : Black 높이, 자신으로부터 leaf노드까지의 경로상의 블랙 노드의 갯수(노드 자신은 포함X)
- 존재하지 않는 노드를 NIL 이라는 노드에 할당, Color Attribute를 Black으로 처리하여 프로그래밍
- 모든 Leaf의 포인터가 해당 NIL이라는 Leaf 노드를 참조하도록 프로그래밍



여기서 알 수 있는 것은,

1. 높이가 h인 노드의 Black height, Bh(x) >= h/2		(조건 : 레드는 연속될 수 없으므로)



### 라. Red-Black Tree 의 장점

- 빈번한 Insertion과 Deletion이 필요할 때 유용함.
-  Binary Tree의 Balance를 자체적으로 항상 유지하므로 런타임 O(logn)가 보장됨.
  반면, BST(Binary Search Tree)는 O(h)이라서 안좋음.
- 다양한 시나리오에서 상대적으로 적은 상수들로 구현 가능.



### 마. Red-Black Tree의 주요 함수 정리

위에 Insert를 위한 rule들을 적용할때 uncle node인 [w]가 null이면 rotation을 한다.

![image-20201209184752607](README%20assets/image-20201209184752607.png)

![image-20201209192010701](README%20assets/image-20201209192010701.png)

![image-20201209192036483](README%20assets/image-20201209192036483.png)

![image-20201209192122919](README%20assets/image-20201209192122919.png)



```c++
//주요 함수만 정리했음.
#include <iostream>
#include <string>
using namespace std;

// 레드블랙트리의 색깔을 지정하기 위한 상수값 표현
namespace Color 
{
	const enum NODE_COLOR : bool { BLACK = false, RED = true };
}

// 레드블랙트리의 노드를 의미하는 클래스
class Node 
{
private:
	int key;	
	bool color;
	Node* parent, * left, * right;
	... 생략
};

// grandPrents 노드를 반환해주는 함수
Node* RedblackTree::getGrandNode(Node* cur)
{
	// 사실 이 조건문은 없어도 된다. 모든 노드는 생성시 nullptr대신 nil로 연결되기 때문.
	if (cur == nullptr || cur->parent == nullptr) return nullptr;
	return cur->parent->parent;
}

// uncle 노드를 반환해주는 함수
Node* RedblackTree::getUncleNode(Node* cur)
{000000000000000000000000000000
	Node* tempGrand(getGrandNode(cur));
	if (tempGrand == nullptr) return nullptr;
	// 조부모의 오른쪽 자식노드가 부모노드면 왼쪽이 삼촌노드다.
	if (cur->parent == tempGrand->left) return tempGrand->right;
	// 조부모의 왼쪽 자식노드가 부모노드면 오른쪽이 삼촌노드다.
	else return tempGrand->left;
}

// 트리를 left rotate하는 함수
void RedblackTree::leftRotate(Node* cur)
{
	// 과정 1) 좌회전시 오른쪽 자식노드를 가리키는 임시 포인터 생성.
	Node* temp = cur->right;
	// 과정 2) cur과 temp를 분리시키면서, temp의 왼쪽 자식노드를 cur이 인수인계함.
	cur->right = temp->left;
	// 과정 3) 방금 인수인계한게 nil이 아니라면, 인수인계한 노드의 부모를 cur로 지정.
	if (temp->left != nil) temp->left->parent = cur;
	// 과정 4) temp의 부모를 cur에서 cur->parent로 바꿔준다.
	temp->parent = cur->parent;
	// 과정 5) cur의 현재 상태에 따라서 temp를 이어주는 경우의 수가 나뉨.
	if (cur->parent == nil) nil->right = temp;
	else if (cur == cur->parent->left) cur->parent->left = temp;
	else cur->parent->right = temp;
	// 과정 6) 이제 모든 사전준비가 끝났으니 temp의 왼쪽 자식노드를 cur로 지정함.
	temp->left = cur;
	// 과정 7) 이제 cur의 부모가 temp가 되면 좌회전 완료.
	cur->parent = temp;
}

// 트리를 right rotate하는 함수
void RedblackTree::rightRotate(Node* cur)
{
	// left Rotate에서 right과 left만 바뀌고 나머지는 똑같다.
	Node* temp = cur->left;
	cur->left = temp->right;

	if (temp->right != nil) temp->right->parent = cur;

	temp->parent = cur->parent;

	if (cur->parent == nil) nil->right = temp;
	else if (cur == cur->parent->left) cur->parent->left = temp;
	else cur->parent->right = temp;

	temp->right = cur;
	cur->parent = temp;
}

// 레드블랙트리의 특성을 만족하도록 트리 구조 수정하는 함수
void RedblackTree::insertFix(Node* cur)
{	// 부모가 root 노드일 때 까지 반복한다. (root노드는 흑색)
	while (cur->parent->color == Color::RED) 
	{
		Node* grandNode(getGrandNode(cur));		// 조부모 노드
		Node* uncleNode(getUncleNode(cur));		// 삼촌 노드
		if (cur->parent == grandNode->left) 
		{	// [CASE 1]: 부모도 삼촌도 모두 빨간색인 경우
			if (uncleNode->color == Color::RED) 
			{	// 부모와 삼촌 그리고 조부모 노드의 색깔을 반전시켜준다.
				cur->parent->color = uncleNode->color = Color::BLACK;
				grandNode->color = Color::RED;
				cur = grandNode;	// cur을 조부모로 올려서 다음 loop를 준비한다.
			}
			else 
			{// [CASE 2]: 삼촌이 흑색이고, cur이 오른쪽 자식노드인 경우
				if (cur == cur->parent->right)
				{ 
					cur = cur->parent;	// cur을 한 칸 올리고,
					leftRotate(cur);	// 좌회전 한다.
				}
				// [CASE 3]: 삼촌이 흑색이고, cur이 왼쪽 자식노드인 경우
				cur->parent->color = !cur->parent->color;	// 부모 색깔 반전
				grandNode->color = !grandNode->color;		// 조부모 색깔 반전
				rightRotate(grandNode);	// 우회전 한다. (주의! grandNode로 우회전)
			}
		}
		else 
		{
			if (uncleNode->color == Color::RED) 
			{
				cur->parent->color = uncleNode->color = Color::BLACK;
				grandNode->color = Color::RED;
				cur = grandNode;
			}
			else
			{
				if (cur == cur->parent->left)
				{
					cur = cur->parent;
					leftRotate(cur);
				}
				cur->parent->color = !cur->parent->color;
				grandNode->color = !grandNode->color;
				rightRotate(grandNode);
			}
		}
	}
	nil->right->color = Color::BLACK;
}

void RedblackTree::insertNode(Node* root, const int& data)
{
	Node* parent, * tail;
	parent = nil;				// 일반적으로 parent가 nil을 가리킨다.
	tail = nil->right;			// 일반적으로 tail이 root 노드를 가리킨다.
	while (tail != nil)			// [과정 1]: 삽입할 위치를 찾는다.
	{		
		parent = tail;			// parent를 tail로 한 칸 내려야 tail을 이동시킬 수 있다.
		int var = tail->key;
		if (data == var)		// [오류]: 트리에 이미 값이 존재할 경우 uniqueness에 위반된다.
		{		
			cout << "[ERROR] Duplicated input value!" << endl;
			return;
		}
		// 삽입할 값이 현재 노드의 key보다 작다면 왼쪽 자식노드로 내려간다.
		else if (data < var) tail = tail->left;
		// 삽입할 값이 현재 노드의 key보다 크다면 오른쪽 자식노드로 내려간다.
		else tail = tail->right;
	}	// 반복문을 탈출함 = 삽입할 위치가 parent에 저장되었음을 의미한다.
	tail = new Node(data, Color::RED, parent, nil, nil);	// new 함수를 이용해 새로운 노드를 만든다.
	if (parent == nil)	// root 노드를 삽입하는 경우,
	{
		parent->right = tail;	// nil->right = tail로 root노드로 만들어주고
		tail->color = Color::BLACK;	// root 노드는 반드시 반드시 흑색이어야 한다.
	}
	// 삽입할 값이 삽입 위치의 노드의 key보다 작다면 왼쪽 자식노드에 삽입한다.
	// 삽입할 값이 삽입 위치의 노드의 key보다 크다면 오른쪽 자식노드에 삽입한다.
	else if (data < parent->key) parent->left = tail;
	else parent->right = tail;

	this->numOfElement++;		// 트리의 노드 개수를 1 증가시킨다.
	insertFix(tail);		// 레드블랙트리의 특성을 만족하도록 매 삽입연산 때 트리 구조를 수정한다.
}
```



## Hash Table

#### : **해시 테이블은 associatvie array(연관배열 구조)를 이용하여 key에 결과 값 value를 저장하는 자료구조이다.**

mapping function을 hash function이라고 한다. key로 index를 받고 그 index로 어디 저장할지를 정한다



##### 연관배열 구조(associative array)란,

키(key) 1개와 값(value) 1개가 1:1로 연관되어 있는 자료구조이다. 따라서 키(key)를 이용하여 값(value)을 도출할 수 있다.

##### 연관배열 구조는 다음의 명령을 지원한다.

- 키(key)와 값(value)이 주어졌을 때, 연관 배열에 그 두 값(key & value)을 저장하는 명령
- 키(key)가 주어졌을 때, 연관되는 값(value)을 얻는 명령
- 키(key)와 새로운 값(value)이 주어졌을 때, 원래 키에 연관된 값(value)을 새로운 값(value)으로 교체하는 명령
- 키(key)가 주어졌을 때, 그 키(key)에 연관된 값(value)을 제거하는 명령

위의 명령은 해시테이블에서도 동일하게 적용이 된다.



### 1. 해시 테이블의 구조(Hash Table Data Structure)

![img](README%20assets/1iHTnDFd3sR5FqjHD1FDu9A.png)

##### 해시 테이블은 키(Key), 해시함수(Hash Function), 해시(Hash), 값(value), 저장소(Bucket, Slot)로 이루어져 있다.

##### 키(key)는 해시함수(hash function)를 통해 해시(hash)로 변경이 되며 해시는 값(value)과 매칭되어 저장소에 저장이 된다.

- 키(key) : 고유한 값이며, 해시 함수의 input이 된다. 다양한 길이의 값이 될 수 있다. 이 상태로 최종 저장소에 저장이 되면 다양한 길이 만큼의 저장소를 구성해 두어야 하기 때문에 해시 함수로 값을 바꾸어 저장이 되어야 공간의 효율성을 추구할 수 있다.
- 해시함수(Hash Function) : 키(key)를 해시(hash)로 바꿔주는 역할을 한다. 다양한 길이를 가지고 있는 키(key)를 일정한 길이를 가지는 해시(hash)로 변경하여 저장소를 효율적으로 운영할 수 있도록 도와준다. 다만, 서로 다른 키(key)가 같은 해시(hash)가 되는 경우를 해시 충돌(Hash Collision)이라고 하는데, 해시 충돌을 일으키는 확률을 최대한 줄이는 함수를 만드는 것이 중요하다.
- 해시(Hash) : 해시 함수(Hash Function)의 결과물이며, 저장소(bucket, slot)에서 값(value)과 매칭되어 저장된다.
- 값(Value) : 저장소(bucket, slot)에 최종적으로 저장되는 값으로 키와 매칭되어 저장, 삭제, 검색, 접근이 가능해야 한다.

![img](README%20assets/1yCYrVNOVhKJccNFkN76QHw.jpeg)



### 2. Collision Resolution



#### 가. Chaining 시간 복잡도 (Big-O) - 1

복잡도를 계산하기 전, 한 가지를 추가하자면 해시 테이블의 저장소(Bucket)의 길이를 ‘n’, 키(key)의 수를 ‘m’이라고 가정했을 때, 평균적으로 저장소에서 1개의 hash당 (m/n)개의 키가 들어있다. 이를 load factor인  ‘α’라고 정의한다.

```null
m/n = α (1개의 Hash당 평균적으로 α개의 키가 들어있다.)
```

chaining기법은 collision이 있다고 하더라도 chaining을 통해 같은 slot에 넣는다.

#### Insertion(저장)

해시 테이블에서 자료를 저장하기 위해서는 해시 함수(Hash Fucntion)으로 키(key)를 해시(hash)로 변경해야 한다. 위의 사진처럼 해시 함수가 input key를 7로 나눈 나머지로 변경해서 출력했을 때, 키(key)는 ‘76’, 해시(Hash)는 ‘6’이다.

그러면 미리 준비해놓은 0, 1, 2, 3, 4, 5, 6의 저장소(bucket, slot) 중에 맞는 해시(hash)값을 찾아 해당 값(value)를 저장한다.

해시 함수로 해시를 산출하는 과정에서 서로 다른 key가 같은 hash로 변경되는 문제가 발생할 수 있는데, 이는 key 와 value가 1:1로 매칭이 되어야 한다는 규칠을 위배한 것이되므로 이 문제를 해결하면서 저장되어야 한다. 이는 **해시 충돌(Hash Collision)** 이라고 하며 해시출동 해결에 대한 내용은 후술 하겠다.

##### Insertion Big-O

저장 단계의 시간복잡도는 O(1)이다. 키(key)는 고유하며 해시함수(hash function)의 결과로 나온 해시(hash)와 값(value)를 저장소에 넣으면 되기 때문이다. 이 때, 해시함수의 시간복잡도는 함께 고려하지 않는다.
하지만, 최악의 경우 O(n)이 될 수 있다. 해시 충돌로 인해 모든 bucket의 value들을 찾아봐야 하는 경우도 있기 때문이다. 이에 관해서도 해시충돌과 함께 후술하겠다.



#### Deletion(삭제)

**저장되어 있는 값을 삭제할 때는 저장소에서 해당 key와 매칭되는 값(value)를 찾아서 삭제하면 된다. (저장소에는 hash와 value가 함께 저장되어 있으므로 함께 지우면 된다.)**

##### Deletion Big-O

삭제 단계의 시간복잡도는 O(1)이다. 키(key)는 고유하며 해시함수(hash function)의 결과로 나온 해시(hash)에 매칭되는 값(value)를 삭제하면 되기 때문이다. 이 때, 해시함수의 시간복잡도는 함께 고려하지 않는다.
하지만, 최악의 경우 O(n)이 될 수 있다. 해시 충돌로 인해 모든 bucket의 value들을 찾아봐야 하는 경우도 있기 때문이다. 이에 관해서도 해시충돌과 함께 후술하겠다.



#### Search(검색)

키(key)로 값(value)를 찾아내는 과정은 Deletion 과정과 비슷한다. 
1) 키로 hash를 구한다. 
2) hash로 값(value)를 찾는다.

##### Search Big-O

저장 단계의 시간복잡도는 O(1)이다. 키(key)는 고유하며 해시함수(hash function)의 결과로 나온 해시(hash)에 매칭되는 값(value)를 찾으면 되기 때문이다. 이 때, 해시함수의 시간복잡도는 함께 고려하지 않는다.
하지만, 최악의 경우 O(n)이 될 수 있다. 해시 충돌로 인해 모든 bucket의 value들을 찾아봐야 하는 경우도 있기 때문이다. 



### 3. Open Addressing(개방주소법)

개방주소법은 데이터의 해시(hash)가 변경되지 않았던 chaining과는 달리 비어있는 해시(hash)를 찾아 데이터를 저장하는 기법이다. 따라서 개방주소법에서의 해시테이블은 1개의 해시와 1개의 값(value)가 매칭되어 있는 형태로 유지된다.

![img](README%20assets/19O8Eyd9wEhZKhwrXzKJaw-1607584344636.png)

위의 그림을 보면, Sandra가 저장될때 해시가 John으로 채워져 있어서 그 다음 Hash에 Sandra를 저장했다. 그리고 Ted의 해시도 Sandra가 저장되어 있으므로 그 다음 해시에 Ted를 저장했다. 이처럼 비어있는 해시를 찾아 저장하는 방법을 Open Addressing라고 한다.

이 때, 비어있는 해시(Hash)를 찾는 과정은 동일해야 한다.(일정한 규칙을 따라 찾아가야 한다.)

Open Addressing는 위에서 언급한 비어있는 해시를 찾는 규칙에 따라 다음과 같이 구분할 수 있다.

- 선형 탐색(Linear Probing): 다음 해시(+1)나 n개(+n)를 건너뛰어 비어있는 해시에 데이터를 저장한다.
- 제곱 탐색(Quadratic Probing): 충돌이 일어난 해시의 제곱을 한 해시에 데이터를 저장한다.
- 이중 해시(Double Hashing): 다른 해시함수를 한 번 더 적용한 해시에 데이터를 저장한다.



#### Open Addressing의 장단점

장점 :
1) 또 다른 저장공간 없이 해시테이블 내에서 데이터 저장 및 처리가 가능하다.
2) 또 다른 저장공간에서의 추가적인 작업이 없다.
단점 :
1) 해시 함수(Hash Function)의 성능에 전체 해시테이블의 성능이 좌지우지된다.
2) 데이터의 길이가 늘어나면 그에 해당하는 저장소를 마련해 두어야 한다.



Chaining 에서 정의한 ‘α’를 Open Addressing 에서도 정의하자면, 해시 테이블의 저장소(Bucket)의 길이를 ’n’, 키(key)의 수를 ‘m’이라고 가정했을 때, ‘α’는 1보다 작거나 같다. 저장소 1개 버킷 당 1개의 값(value)만 가지기 때문이다.

```null
m/n = α (α <= 1)
```



#### Insertion & Deletion & Search :

삽입, 삭제, 검색 모두 대상이 되는 Hash를 찾아가는 과정에 따라 시간복잡도가 계산이 된다. 해시함수를 통해 얻은 Hash가 비어있지 않으면 다음 버킷을 찾아가야 한다. 이 찾아가는 횟수가 많아지면 많아질 수록 시간복잡도가 증가한다. 최상의 경우 O(1) ~ 최악의 경우 (O(n)).

따라서 Open Addressing에서는 비어있는 공간을 확보하는 것(= 저장소가 어느 정도 채워졌을 때 저장소의 사이즈를 늘려주는 것)이 필요하다.

최악의 경우 저장소를 모두 살펴보아야 하는 경우가 생길 수 있다.(O(n))





### 4. Hashing 함수



이번엔 해시함수로 해시충돌을 완화하는 방법을 살펴본다. 해시테이블의 크기가 m이라면, 좋은 해시함수는 임의의 키값을 임의의 해시값에 매핑할 확률이 1/m이 될 것이다. 다시 말해, 특정 값에 치우치지 않고 해시값을 고르게 만들어내는 해시함수가 좋은 해시함수라고 볼 수 있다.

### division method

나눗셈법은 간단하면서도 빠른 연산이 가능한 해시함수이다. 숫자로 된 키를 해시테이블 크기 m으로 나눈 나머지를 해시값으로 반환한다. m은, 대개 <u>소수(prime number)</u>를 쓰며 특히 2의 제곱수와 거리가 먼 소수를 사용하는 것이 좋다. 다시 말해 해시함수 특성 때문에 해시테이블 크기가 정해진다는 단점이 있다.

### multiplication method

숫자로 된 키가 k이고 <u>A는 0과 1 사이의 실수</u>일 때 곱셈법은 다음과 같이 정의된다. <u>m은 보통 2의 제곱수</u>로 정한다. 나눗셈법보다는 몇개의 연산을 해야되기 때문에 다소 느리다. 2진수 연산에 최적화한 컴퓨터 구조를 고려한 해시함수이다.

h(k) = floor( ( k A mod 1) × m )

### universal hasing

다수의 해시함수를 만들고, 이 해시함수의 집합 H에서 무작위로 해시함수를 선택해 해시값을 만드는 기법이다. H에서 무작위로 뽑은 해시함수가 주어졌을 때, 임의의 키값을 임의의 해시값에 매핑할 확률을 1/m로 만드려는 것이 목적이다. 다음과 같은 특정 조건의 해시함수 집합 H는 1/m으로 만드는 게 가능하다고 수학적으로 증명됐다.

- 해시테이블의 크기 m를 소수로 정한다.
- 키값을 다음과 같이 r+1개로 쪼갠다 : k0, k1,…, kr
- 0부터 m−1 사이의 정수 가운데 하나를 무작위로 뽑는다. 분리된 키값의 개수(r+1)만큼 반복해서 뽑는다. 이를 a=[a0,a1,…,ar]로 둔다. 따라서 a의 경우의 수는 모두 mr+1가지이다.
- 해시함수를 다음과 같이 정의한다 : ha(x)=Σri=0(aikimod m)
- a가 mr+1가지이므로 해시함수의 집합 H의 요소 수 또한 mr+1개이다.

위와 같은 조건에서는 키가 동일하더라도 a가 얼마든지 랜덤하게 달라질 수 있고, 이에 해당하는 해시함수 ha 또한 상이해지기 때문에 H는 유니버설 함수가 된다.



### 5. Hash Table Data Structure의 단점

- **<u>순서가 있는 배열에는 어울리지 않는다.</u>**
  : 상하관계가 있거나, 순서가 중요한 데이터의 경우 Hash Table은 어울리지 않다. 순서와 상관없이 key만을 가지고 hash를 찾아 저장하기 때문이다.
- **<u>공간 효율성이 떨어진다.</u>**
  : 데이터가 저장되기 전에 미리 저장공간을 확보해 놓아야 한다. 공간이 부족하거나 아예 채워지지 않은 경우가 생길 가능성이 있다.
- **<u>Hash Function의 의존도가 높다.</u>**
  : 평균 데이터 처리의 시간복잡도는 O(1)이지만, 이는 해시 함수의 연산을 고려하지 않는 결과이다. 해시함수가 매우 복잡하다면 해시테이블의 모든 연산의 시간 효율성은 증가할 것이다.

해시 테이블은 키를 가지고 빠르게 value에 접근하고 조작할 수 있는 장점이 있어서 많이 사용된다. 예를 들어 주소록 저장형태의 경우 이름 — 전화번호의 매칭을 이용하여 데이터를 처리한다. 





## DFS(Depth-first Search, 깊이 우선 탐색)

**Stack** 혹은 **재귀** 사용

이동할때 마다 가중치가 붙어서 이동한다거나 이동 과정에서 여러 제약이 있을 경우 사용

Time : 𝛳(V+E) , 모든 vertex와 edge가 실행되는것이 보장되기 때문에 O가 아님.

```c
DFS(G, u)
    u.visited = true
    for each v ∈ G.Adj[u]
        if v.visited == false
            DFS(G,v)
 
init() 
    For each u ∈ G
        u.visited = false
     For each u ∈ G
       DFS(G, u)
```

1. 스택에 시작 노드를 넣는다.
2. 스택이 비어있으면 실행을 멈추고 False를 반환한다.
3. 스택의 맨 위 노드가 찾고자 하는 노드라면 탐색을 종료하고 True를 반환한다.
4. 스택의 맨 위 노드가 찾고자 하는 노드가 아니라면 해당 노드를 POP한다. 스택에 들어온 적이 없는 POP한 노드의 모든 이웃노드를 찾아서 순서대로 스택에 넣는다.
5. 3번으로 돌아간다.



![img](README%20assets/dfs_1.png)

A를 시작노드로 한다.

![img](README%20assets/dfs_2.png)

A에 인접한 B, C가 스택에 저장된다.

![img](README%20assets/dfs_3.png)

스택의 맨 위에 있는 C를 꺼내서 Visited 배열에 넣는다. C의 인접한 노드인 D, F가 스택에 저장된다.

![img](README%20assets/dfs_4.png)

스택의 맨 위에 있는 F를 꺼내서 Visited 배열에 넣는다. F에 인접한 노드인 D는 이미 Stack에 있으므로 넘어간다.

![img](README%20assets/dfs_5.png)

스택의 맨 위에 있는 D를 꺼내서 Visited 배열에 넣는다. D에 인접한 C, F는 Visited 배열에 있으며 B는 스택에 있으므로 넘어간다.

![img](README%20assets/dfs_6.png)

스택의 맨 위에 있는 B를 꺼내서 Visited 배열에 넣는다. 스택이 비어있으므로 탐색을 종료한다.

### ⭕ DFS 장점

- 현 경로상의 노드를 기억하기 때문에 적은 메모리를 사용한다.
- 찾으려는 노드가 깊은 단계에 있는 경우 BFS 보다 빠르게 찾을 수 있다.

### ❌ DFS 단점

- 해가 없는 경로를 탐색 할 경우 단계가 끝날 때까지 탐색한다. 효율성을 높이기 위해서 미리 지정한 임의 깊이까지만 탐색하고 해를 발견하지 못하면 빠져나와 다른 경로를 탐색하는 방법을 사용한다.
- DFS를 통해서 얻어진 해가 최단 경로라는 보장이 없다. DFS는 해에 도착하면 탐색을 종료하기 때문이다.



## BFS(Breadth-first Search, 너비 우선 탐색)

FIFO(First-in First-out)의  **Queue**를 사용한다.

**최단거리 탐색할 시 사용**

O(V + E) : 모든 vertex가 한번씩은 enqueue 된다.

```python
create a queue Q 
mark v as visited and put v into Q 
while Q is non-empty 
    remove the head u of Q 
    mark and enqueue all (unvisited) neighbors of u
```



### 그림으로 보기

![img](README%20assets/bfs_1.png)

A노드 부터 탐색을 시작한다.

![img](README%20assets/bfs_2.png)

A노드를 Visited 리스트에 넣는다. A노드에 인접한 B, C를 큐에 넣는다.

![img](README%20assets/bfs_3.png)

큐의 맨 앞에 있는 B를 Visited 리스트에 넣는다. B에 인접한 노드 D를 큐에 넣는다.

![img](README%20assets/bfs_4.png)

큐의 맨 앞에 있는 C를 Visited 리스트에 넣는다. C에 인접한 노드 F를 큐에 넣는다.

![img](README%20assets/bfs_5.png)

큐의 맨 앞에 있는 D를 Visited 리스트에 넣는다. D에 인접한 F는 이미 큐에 있으므로 넘어간다.

![img](README%20assets/bfs_6.png)

큐의 맨 앞에 있는 F를 Visited 리스트에 넣는다. 큐는 비어있게 되므로 탐색을 종료한다.

### ⭕ BFS 장점

- 답이 되는 경로가 여러 개인 경우에도 최단경로임을 보장한다.
- 최단 경로가 존재하면 깊이가 무한정 깊어진다고 해도 답을 찾을 수 있다.

### ❌ BFS 단점

- 경로가 매우 길 경우에는 탐색 가지가 급격히 증가함에 따라 보다 많은 기억 공간을 필요로 하게 된다.
- 해가 존재하지 않는다면 유한 그래프(finite graph)의 경우에는 모든 그래프를 탐색한 후에 실패로 끝난다.
- 무한 그래프(infinite graph)의 경우에는 결코 해를 찾지도 못하고, 끝내지도 못한다.

