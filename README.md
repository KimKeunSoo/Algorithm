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

