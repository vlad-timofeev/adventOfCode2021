val INPUT =
"""forward 5
down 3
up 6
forward 7"""

data class Position(val horizontal: Int, val depth: Int, val aim: Int)

fun move(position: Position, commandLine: String): Position {
    val(command, valueStr) = commandLine.split(" ")
    val value = valueStr.toInt()

    return when (command) {
        "down" -> Position(position.horizontal, position.depth, position.aim + value)
        "up" -> Position(position.horizontal, position.depth, position.aim - value)
        "forward" -> Position(position.horizontal + value, position.depth + value * position.aim, position.aim)
        else -> TODO("unknown command '$command'")
    }
}

fun main() {
    val finalPosition = INPUT.split('\n').fold(Position(0, 0, 0), ::move);
    println(finalPosition.horizontal * finalPosition.depth)
}
