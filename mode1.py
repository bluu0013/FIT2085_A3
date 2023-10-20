from island import Island
from data_structures.bst import *

class Mode1Navigator:
    """
    ADT Used --> Binary Search Tree.
    Reasoning:
        This would allow each instance of this class to be able to sort
        and traverse through the Islands as efficiently and seemlessly
        as possible, while also adhering to the coomplexity requirements.
        
    
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """Initialise Navigator.
        Best Case: O(N) where 'N' is the number of Islands.
            This would be when the list of Islands is already sorted, 
            meaning it just needs to be inserted without any 
            other modifications.
        
        Worst Case: O(NlogN) where 'N' is the number of Islands.
            This would be when the list of Islands is in a random order,
            meaning when each Island is inserted, the list need to be 
            re-ordered.
        """
        self.crew = crew
        self.plunder = 0
        self.islands = BinarySearchTree()
        for i in islands:
            priority = -(i.money/i.marines)
            self.islands[priority] = i


    def select_islands(self) -> list[tuple[Island, int]]:
        """Return List of Islands with the number of crew sent.
        Best Case: O(logN) where 'N' is the number of Islands.
            This would be when not all Islands would need to be visited as
            the number of crew mates would be 0 at any given point.

        Worst Case: O(N) where 'N' is the number of Islands.
            This would be when each Island would need to be visited due to a
            more than sufficient number of crew members.
        """
        self.plunder = 0
        result = []
        iter = BSTInOrderIterator(self.islands.root)
        curr_crew = self.crew
        while curr_crew > 0:
            try:
                node = next(iter)
            except StopIteration:
                break

            island = node.item
            if curr_crew >= island.marines:
                crew_sent = island.marines
                curr_crew -= crew_sent
                self.plunder += crew_sent * (island.money / island.marines)
            else:
                crew_sent = curr_crew
                curr_crew -= curr_crew
                self.plunder += crew_sent * (island.money / island.marines)

            result.append([island , crew_sent])

        return result


    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """Return the Plunder for each different sized crews.
        Best Case: O(C*logN) where 'C' is the length of 'crew_members' and 
        'N' is the number of Islands.
            This would be when each of the items in 'crew_numbers' are not
            enough to reach all Islands.

        Worst Case: O(C*N) where 'C' is the length of 'crew_members' and 
        'N' is the number of Islands.
            This would be when each of the items in 'crew_numbers' are able
            to go to each Islands.
        """
        result = []
        for i in crew_numbers:
            self.crew = i
            self.select_islands()
            result.append(self.plunder)

        return result

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """Update the Island's Money and Marines.
        Best Case: O(1)
            If the Island in question is the first node, then this would be the best case.
        
        Worst Case: O(N) where 'N' is the number of Islands.
            This can be attributed to the fact that searching through a bst 
            would have to search throught the whole tree before finding it.
        """
        current_priority = -(island.money/island.marines)
        new_priority = -(new_money/new_marines)
        new_island = Island(island.name,new_money,new_marines)

        del self.islands[current_priority]
        self.islands[new_priority] = new_island
