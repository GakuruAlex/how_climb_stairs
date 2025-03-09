from typing import List
def how_climb_stairs(stairs: int) -> List[int]:
    """_Find one  way to get to the top of stairs if you can only move either 1 or 2 stairs at a time_

    Args:
        stairs (int): _Number of stair to the top_

    Returns:
        List[int]: _A list of a way to get to the top_
    """
    ...

def main()-> None:
    stairs: int = 5
    one_way: List[int] = how_climb_stairs(stairs=stairs)
    print(f"One way to get to the top of {stairs} stairs is {one_way}")

if __name__ =="__main__":
    main()