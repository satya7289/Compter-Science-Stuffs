# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    import time
    from collections import defaultdict

    # directions is udes to store the direction list
    directions = []
    Dic = defaultdict(list)

    # initialize a stack from util.stack
    stack = util.Stack()
   
    # visited node or not
    visited = []
    # start the dfs algorithm
    start_state = problem.getStartState()
    
    stack.push(list((start_state, 'Start', 0)))
    
    while not stack.isEmpty(): 
        poped_state = stack.pop()
        
        if poped_state[0] not in visited:
            visited.append(poped_state[0])
            # print poped_state
            
            if problem.isGoalState(poped_state[0]):
                break
            successors = problem.getSuccessors(poped_state[0])
            
            
            for successor in successors:
                if successor[0] not in visited:
                    stack.push(successor)
                    Dic[successor].append(poped_state)
                    # time.sleep(1)
            
            # print directions 

    # backtracking start..
    for i in Dic:
        if visited[-1] in i:
            backtrack_state = i
    # print visited[-1], backtrack_state, tuple(Dic[backtrack_state][0])
    
    return BacktrackUtil(problem,backtrack_state,Dic)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    import time
    from collections import defaultdict

    # directions is udes to store the direction list
    directions = []
    Dic = defaultdict(list)

    # initialize a Queue from util.stack
    queue = util.Queue()
   
    # visited node or not
    visited = []
    # start the dfs algorithm
    start_state = problem.getStartState()
    
    queue.push(list((start_state, 'Start', 0)))
    
    while not queue.isEmpty(): 
        poped_state = queue.pop()
        
        if poped_state[0] not in visited:
            visited.append(poped_state[0])
        
            if problem.isGoalState(poped_state[0]):
                break
            successors = problem.getSuccessors(poped_state[0])
            
            
            for successor in successors:
                if successor[0] not in visited:
                    queue.push(successor)
                    Dic[successor].append(poped_state)
                    # time.sleep(1)
        
        # print directions 

    # print problem.getExpandedStates()
    # backtracking start..
    print visited,"satya", visited[-1]
    for i in Dic:
        if visited[-1] in i:
            backtrack_state = i
    # print visited[-1], backtrack_state, tuple(Dic[backtrack_state][0])

    for i in Dic:
        print i,Dic[i]

    directions = BacktrackUtil(problem,backtrack_state,Dic)

    return directions

def BacktrackUtil(problem, backtrack_state, Dic):
    directions = []
    while True:
        if problem.getStartState() in backtrack_state:
            break
        directions.append(backtrack_state[1])
        # print type(backtrack_state), backtrack_state
        backtrack_state = tuple(Dic[backtrack_state][0])
    # print directions
    return directions[::-1]

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    from collections import defaultdict

    # directions is used to store the direction list
    directions = []
    Dic = defaultdict(list)

    # initialize a Queue from util.stack
    priorityQueue = util.PriorityQueue()
   
    # visited node or not
    visited = []
    # start the dfs algorithm
    start_state = problem.getStartState()
    
    priorityQueue.push(list((start_state, 'Start', 0)),1)
    
    while not priorityQueue.isEmpty(): 
        poped_state = priorityQueue.pop()
        
        if poped_state[0] not in visited:
            visited.append(poped_state[0])
        
            if problem.isGoalState(poped_state[0]):
                break
            successors = problem.getSuccessors(poped_state[0])
            
            
            for successor in successors:
                if successor[0] not in visited:
                    Dic[successor].append(poped_state)
                    prioty_backtrack = BacktrackUtil(problem,successor,Dic)
                    priorityQueue.update(successor,problem.getCostOfActions(prioty_backtrack))
                    
                    # time.sleep(1)
                
        
        # print directions 

    # print problem.getExpandedStates()
    # backtracking start..
    for i in Dic:
        if visited[-1] in i:
            backtrack_state = i
    # print visited[-1], backtrack_state, tuple(Dic[backtrack_state][0])
    
    return BacktrackUtil(problem,backtrack_state,Dic)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from collections import defaultdict

    # directions is used to store the direction list
    directions = []
    Dic = defaultdict(list)

    # initialize a Queue from util.stack
    priorityQueue = util.PriorityQueue()
   
    # visited node or not
    visited = []
    # start the dfs algorithm
    start_state = problem.getStartState()
    
    priorityQueue.push(list((start_state, 'Start', 0)),1)
    
    while not priorityQueue.isEmpty(): 
        poped_state = priorityQueue.pop()
        
        if poped_state[0] not in visited:
            visited.append(poped_state[0])
        
            if problem.isGoalState(poped_state[0]):
                break
            successors = problem.getSuccessors(poped_state[0])
            
            
            for successor in successors:
                if successor[0] not in visited:
                    Dic[successor].append(poped_state)
                    prioty_backtrack = BacktrackUtil(problem,successor,Dic)
                    total_cost = problem.getCostOfActions(prioty_backtrack) + heuristic(successor[0],problem)
                    priorityQueue.update(successor, total_cost)
                    
                    # time.sleep(1)
                
        
        # print directions 

    # print problem.getExpandedStates()
    # backtracking start..
    for i in Dic:
        if visited[-1] in i:
            backtrack_state = i
    # print visited[-1], backtrack_state, tuple(Dic[backtrack_state][0])
    
    return BacktrackUtil(problem,backtrack_state,Dic)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
