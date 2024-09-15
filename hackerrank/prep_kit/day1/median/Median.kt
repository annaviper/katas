package hackerrank.prep_kit.day1

fun calculateMedian(args: Array<Int>): Int {
    val arrLen = args.size
    val median = args[arrLen/2]
    return median
}

fun main() {
    val numbers = arrayOf(1, 3, 5, 7, 9)
    val median = calculateMedian(numbers)
    println(median)
}