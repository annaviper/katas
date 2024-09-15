/*
Given a list of numbers
with an odd number of elements,
find the median.

Example:
lst = [5, 3, 1, 2, 4]
find_median(lst) --> returns 3
*/

package hackerrank.prep_kit.day1;

import java.util.Arrays;


public class Median {
    public static void main(String[] args) {
        int[] arr = {0, 1, 2, 4, 6, 5, 3};

        int arrLen = arr.length;
        Arrays.sort(arr);
        int median = arr[arrLen/2];

        System.out.println(median);
    }
}
