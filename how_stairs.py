from typing import List
def how_climb_stairs_recur(ways: List[int], stairs: int) -> List[int]:
    """_Find one  way to get to the top of stairs if you can only move either 1 or 2 stairs at a time_

    Args:
        stairs (int): _Number of stair to the top_

    Returns:
        List[int]: _A list of a way to get to the top_
    """

    if stairs < 0:
        return None
    if stairs == 0:
        return []
    for way in ways:
        new_height: int = stairs - way
        result: List[int] = how_climb_stairs_recur(ways=ways, stairs= new_height)
        if result != None:
                return [way] + result

def main()-> None:
    ways: List[int] = [2, 1]
    stairs: int = 5
    one_way: List[int] = how_climb_stairs_recur(ways= ways, stairs=stairs)
    print(f"One way to get to the top of {stairs} stairs  to take {one_way}")

if __name__ =="__main__":
    main()