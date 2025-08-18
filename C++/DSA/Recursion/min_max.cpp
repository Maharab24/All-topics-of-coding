// C++ code using recursion to find min
// and max in an array
#include <iostream>
#include <vector>
using namespace std;

int getMinRec(vector<int> &arr, int n) {

    // Base case: only one element
    if (n == 1) {
        return arr[0];
    }

    // Recursive case: find min in rest of the array
    int minInRest = getMinRec(arr, n - 1);

    // Return the smaller value between
    // last element and recursive min
    if (arr[n - 1] < minInRest) {
        return arr[n - 1];
    } else {
        return minInRest;
    }
}

int getMaxRec(vector<int> &arr, int n) {

    // Base case: only one element
    if (n == 1) {
        return arr[0];
    }

    // Recursive case: find max in rest of the array
    int maxInRest = getMaxRec(arr, n - 1);

    // Return the larger value between last
    // element and recursive max
    if (arr[n - 1] > maxInRest) {
        return arr[n - 1];
    } else {
        return maxInRest;
    }
}

// Main function to find min and max
vector<int> findMinMax(vector<int> &arr) {

    int n = arr.size();

    int minValue = getMinRec(arr, n);
    int maxValue = getMaxRec(arr, n);

    return {minValue, maxValue};
}

int main() {

    vector<int> arr = {1, 4, 3, -5, -4, 8, 6};

    vector<int> res = findMinMax(arr);

    cout << "min = " << res[0] << ", max = " << res[1];

    return 0;
}