from typing import *

DEFAULT_COUNT = -1
DEFAULT_PATH = []
DEFAULT_FIRST = "0000"

class OpenLock:
    """
    Class to solve the Open Lock Problem in a numeric wheel game.
    """

    def __init__(self, deadends:List[str], target: str, first=DEFAULT_FIRST):
        """
        Initializes an instance of the OpenLock class.

        Args:
            deadends (List[str]): A list of strings representing the states of blocked locks.
            target (str): A string representing the target state of the lock.
        """
        self.deadends = set(deadends)
        self.target = target
        self.first = first
        self.level, self.paths = self._bfs()


    def get_level(self):
        return self.level
    
    
    def get_paths(self):
        return self.paths
    
    
    def get_deadends(self):
        return self.deadends
    
    
    def get_target(self):
        return self.target
    

    def get_first(self):
        return self.first

    
    def neighbors(self, state: str) -> List[str]:
        """
        Returns a list of possible neighboring states for the lock by turning the wheels.

        Args:
            state (str): A string representing the current state of the lock.

        Returns:
            List[str]: A list of strings representing possible neighboring states.
        """
        lock = [char for char in state]
        n = len(lock)
        out = []
        
        for i in range(n):
            digit = int(lock[i])

            wheel_up = str((digit + 1) % 10)
            lock[i] = wheel_up
            state_up = ''.join(lock)

            wheel_down = str((digit - 1 ) % 10)
            lock[i] = wheel_down
            state_down = ''.join(lock)

            lock[i] = str(digit)
            
            if state_up not in self.deadends:
                out.append(state_up)
            if state_down not in self.deadends:
                out.append(state_down)

        return out
    

    def _bfs(self):
        """
        Breadth-First Search (BFS) algorithm to find the minimum number of moves required
        to reach the target state of the lock from the initial state.

        Returns:
            level (int): Minimum number of moves if not result return DEFAULT_COUNT 
            paths (List[str]): list of strings representing path if not path return DEFAULT_PATH
        """
        queue = [(self.first, 0)]
        visited = {self.first: self.first}

        while queue:
            lock, level = queue.pop(0)
            
            if lock == self.target:
                self.count = level
                step = self.target
                paths = [step]
                
                while step != self.first:
                    paths.insert(0, visited[step])
                    step = visited[step]
                return level, paths
            
            neighbors_locks = self.neighbors(lock)
            for code  in neighbors_locks:
                if code not in visited:
                    visited[code] = lock
                    queue.append((code, level+1))
        
        return DEFAULT_COUNT, DEFAULT_PATH