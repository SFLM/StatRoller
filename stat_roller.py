import random
from typing import List


def roll_single_stat() -> int:
    """
    Rolls 4d6 excluding 1s, discarding the lowest roll. The sum of the remaining three rolls is returned.

    Returns
    -------
    int
        A single generated stat value.
    """
    rolls = [random.randint(2, 6) for _ in range(4)] # Rolls 4d6, excluding 1s
    rolls.remove(min(rolls))  # The lowest value is discarded
    return sum(rolls)


def roll_stats() -> List[int]:
    """
    Rolls stats for a character by rolling 4d6 six times and dropping the lowest
    roll for each set.

    Returns
    -------
    List[int]
        A list of six stat values.
    """
    return [roll_single_stat() for _ in range(6)] # 6 stats, representing Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma in no particular order.


def display_results(stats: List[int]) -> None:
    """
    Displays the rolled stats in a readable format, including the mathematical average and the generated stat total for comparison.

    Parameters
    ----------
    stats : (List[int])
        A list of stat values to display.
    """
    print("Rolled stats:")
    for stat in stats:
        print(stat)
    
    print("Average stat total: 72") # = 6 * (3 * 4)
    print(f"Your total: {sum(stats)}")


if __name__ == "__main__":
    stats = roll_stats()
    display_results(stats)
