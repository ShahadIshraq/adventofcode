package ishraq.shahad.adventofcode2024.day5


private fun isSafe(
    list: List<Int>,
    dependencies: MutableMap<Int, List<Int>>
): Boolean {
    return list.withIndex().all { (i, item) ->
        list.drop(i + 1).none { dependencies[item]?.contains(it) == true }
    }
}

private fun makeSafe(
    list: List<Int>,
    dependencies: MutableMap<Int, List<Int>>
): List<Int> {
    var mutableList = list
    while (!isSafe(mutableList, dependencies)) {
        mutableList = attemptToMakeSafe(mutableList, dependencies)
        println(mutableList)
    }

    return mutableList
}

private fun attemptToMakeSafe(
    list: List<Int>,
    dependencies: MutableMap<Int, List<Int>>
): List<Int> {
    val mutableList = list.toMutableList()
    var i = 0
    while (i < list.size - 1) {
        var j = i + 1
        while (j < list.size) {
            if (dependencies[mutableList[i]]?.contains(mutableList[j]) == true) {
                mutableList.add(i, mutableList.removeAt(j))
            }
            j++
        }
        i++
    }
    return mutableList
}

class Input(
    val dependencies: MutableMap<Int, List<Int>>,
    val pageLists: List<List<Int>>
) {
    operator fun component1() = dependencies
    operator fun component2() = pageLists
}

fun loadInput(loadFromFile: Boolean): Input {
    var input = """
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47""".trimIndent()

    if (loadFromFile) {
        input = object {}.javaClass.classLoader.getResourceAsStream("day5input")
            ?.bufferedReader()
            .use { it?.readText().toString() }
    }

    val dependencies = mutableMapOf<Int, List<Int>>()
    val pageLists = mutableListOf<List<Int>>()

    var blankFound = false
    input.lines()
    .forEach { line ->
        if (line.isBlank()) {
            blankFound = true
            return@forEach
        }
        if (!blankFound) {
            val (from, to) = line.split("|").map { it.toInt() }
            // if to is not in the map, then add it with an empty list
            dependencies[to] = dependencies.getOrDefault(to, emptyList()) + from
        } else {
            val list = line.split(",").map { it.toInt() }
            pageLists.add(list)
        }
    }

    return Input(dependencies, pageLists)
}

fun part1(input: Input): Int {
    val (dependencies, pageLists) = input
    return pageLists.filter { isSafe(it, dependencies) }
        .sumOf { it[it.size / 2] }
}

fun part2(input: Input): Int {
    val (dependencies, pageLists) = input
    return pageLists.filter { !isSafe(it, dependencies) }
        .sumOf { makeSafe(it, dependencies)[it.size / 2] }
}

fun main() {
    val input = loadInput(true)
    println("Part 1: ${part1(input)}")
    println("Part 2: ${part2(input)}")
}