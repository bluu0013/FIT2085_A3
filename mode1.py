from island import Island
from data_structures.bst import *

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case

        """
        self.islands = BinarySearchTree()
        for i in range(len(islands)):
            ratio = -(islands[i].money/islands[i].marines)
            self.islands[ratio] = islands[i]
        
        self.crew = crew

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        result = []
        order = BSTInOrderIterator(self.islands)

        for i in order.stack:
            if self.crew >= #island marines: 
                crew_sent = self.crew - #island marines
                self.crew -= #island marines
            elif self.crew < #island marines:
                crew_sent = self.crew
                self.crew -= self.crew
            result.append([#island , crew_sent])
        
        return result
        #raise NotImplementedError()

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """

        #raise NotImplementedError()

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        Best & Worst Case: O(logN)

        """
        old_ratio = -(island.money/island.marines)
        new_ratio = -(new_money/new_marines)

        island.money = new_money
        island.marines = new_marines

        self.islands[old_ratio] = None
        self.islands[new_ratio] = island
