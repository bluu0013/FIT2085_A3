from island import Island
from data_structures.bst import *

class Mode2Navigator:
    """
    ADT Used --> Binary Search Tree.
    Reasoning:
        This would allow each instance of this class to be able to sort
        and traverse through the Islands as efficiently and seemlessly
        as possible, while also adhering to the coomplexity requirements.
    
    Notes:
        A lot of the code used here is derived from the functions implemented
        in 'mode1.py'. Originally, the file was going to be imported, however
        creating an instance of 'Mode1Navigator' would prevent the complexity
        requirements from being met.

    """

    def __init__(self, n_pirates: int) -> None:
        """Initialise Navigator.
        Best / Worst Case: O(1)
            Should be constant as variables are only being set.
        """
        self.pirates = n_pirates
        self.islands = BinarySearchTree()


    def add_islands(self, islands: list[Island]):
        """Add Islands to Navigator.
        Best Case: O(I) where 'I' is the length of 'islands' list.
            This would be when there is no current Islands in the navigator.

        Worst Case: O(N * I) where 'I' is the length of 'islands' list 
        and 'N' is the number of current nodes.
            This would be when there are Islands already in the navigator,
            and each Island in 'islands' causes the BST to be resorted each time.
        """
        for i in islands:
            priority = -(i.money/i.marines)
            self.islands[priority] = i
        

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """Start the Davy Back Fight Sequence.
        Best Case: O(C*logN) where 'C' is the number of crew members 
        and 'N' is the number of current nodes.
            This would be when each pirate captain only has to visit one island
            before they run out of crewmates.

        Worst Case: O(N + C*logN) where 'C' is the number of crew members 
        and 'N' is the number of current nodes.
            This would be when each captain would need to visit each island
            given they have enough crew members to cycle through all of them.
        """
        result = []
        for _ in range(self.pirates):
            result.append(0)
        
        current_pirate = 0
        
        while current_pirate < self.pirates:

            iter = BSTInOrderIterator(self.islands.root)
            curr_crew = crew

            while curr_crew != 0:
                try:
                    node = next(iter)
                except StopIteration:
                    break
                
                island = node.item
                if island.money != 0:
                    if curr_crew >= island.marines and island.marines != 0:
                        crew_sent = island.marines
                        curr_crew -= crew_sent
                        island.marines -= crew_sent
                    elif curr_crew < island.marines and island.marines != 0:
                        crew_sent = curr_crew
                        island.marines -= crew_sent
                        curr_crew -= curr_crew
                    
                    result[current_pirate] = [island , crew_sent]    

                    if island.marines == 0:
                        island.money = 0
                        current_priority = node.key
                        updated_island = Island(island.name, island.money, island.marines)
                        del self.islands[current_priority]
                        
                    else:
                        current_priority = node.key
                        new_priority = -(island.money/island.marines)
                        updated_island = Island(island.name, island.money, island.marines)
                        del self.islands[current_priority]
                        self.islands[new_priority] = updated_island
            current_pirate += 1
        return result