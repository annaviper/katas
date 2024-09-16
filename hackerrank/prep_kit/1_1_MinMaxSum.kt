/*
Given five positive integers, find the minimum
and maximum values that can be calculated
by summing exactly four of the five integers.

Example:
arr = [1, 3, 5, 7, 9]
The minimum sum is `1 + 3 + 5 + 7 = 16`
The maximum sum is `3 + 5 + 7 + 9 = 24`
The function prints: 16 24
*/

package hackerrank.prep_kit.day1

fun minMaxSum(args: List<Int>) {
    val args = args.sorted()

    val minSumList = args.slice(0..3)
    println(minSumList)
    val maxSumList = args.slice(1..4)
    println(maxSumList)

    val minSum = minSumList.sum()
    val maxSum = maxSumList.sum()

    println("$minSum $maxSum")
}

fun main() {
    val arr = listOf(1, 2, 5, 3, 4)
    minMaxSum(arr)
}