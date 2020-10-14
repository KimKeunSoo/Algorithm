# Algorithm



## maximum subarray problem

주어진 배열에서 합이 가장 큰 구간을 찾는 문제.



O(N^3) - 전체를 순서대로 탐색하는 방법

C로 짤때

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

js로 짤때

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



O(N^2)

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



O(nlogn) - Divide and Conquer algorithm

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

