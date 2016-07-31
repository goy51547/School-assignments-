# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
from compiler.misc import Stack

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Stack
    fringe =Stack()
    closed = set()
    fringe.push(problem.getSuccessors(problem.getStartState())[0])
    solution=[]
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    available={}
    while fringe:
        fringeAdded=False
        nodeAvailable=False
        if not fringe.list[-1][0] in closed:
                if not problem.isGoalState(fringe.list[-1][0]):
                    if not fringe.list[-1][0] in available:
                        temp= problem.getSuccessors(fringe.list[-1][0])
                        if temp==[]:
                            closed.add(fringe.list[-1][0])
                            fringe.pop()
                        else:
                            for i in temp:
                                if not i[0] in closed:
                                    if not i[0] in problem._visitedlist:
                                        if not fringeAdded:
                                            fringe.push(i)
                                            fringeAdded = True
                                        else:
                                            nodeAvailable=True 
                                            available.update({fringe.list[-2][0]:i})
                                if i==temp[-1]:
                                    if not nodeAvailable:
                                        if fringeAdded:
                                            closed.add(fringe.list[-2][0])
                                        else:
                                            closed.add(fringe.list[-1][0])
                    else:
                        temp= available[fringe.list[-1][0]]
                        del available[fringe.list[-1][0]]
                        for i in temp:
                            if isinstance(i[0], int):
                                if not temp in closed:
                                    if not temp in problem._visitedlist:
                                            closed.add(fringe.list[-1][0])
                                            fringe.push(temp)
                                break
                            else:
                                if not i[0] in closed:
                                    if not i[0] in problem._visitedlist:
                                        if not fringeAdded:
                                            fringe.push(i)
                                            fringeAdded = True
                                        else:
                                            nodeAvailable=True 
                                            available.update({fringe.list[-1][0]:i})
                                if i==temp[-1]:
                                    if not nodeAvailable:
                                        if fringeAdded:
                                            closed.add(fringe.list[-2][0])
                                        else:
                                            closed.add(fringe.list[-1][0])              
                else:
                    for i in fringe.list:
                        if i[1]=='South':
                            solution.append(s)
                        else:
                            if i[1]=='West':
                                solution.append(w)
                            else:
                                if i[1]=='North':
                                    solution.append(n)
                                else:
                                    if i[1]=='East':
                                        solution.append(e)  
                    return solution
        else:
            fringe.pop()
        

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Queue
    traces=[]
    StartState=problem.getStartState()
    'corners=problem.corners'
    fringe =Queue()
    closed = set()
    temp=problem.getSuccessors(StartState)
    for i in temp:  
        fringe.push((i,[]))
    closed.add(StartState)
    solution=[]
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    while fringe:
        node=fringe.list[-1]
        state=node[0][0]
        if not problem.isGoalState(state):
                    fringe.pop()
                    'if state in corners:'
                    'traces=traces+[node[1]+[node[0]]]'
                    if not state in closed:
                        temp= problem.getSuccessors(state)
                        if temp==[]:
                            closed.add(state)
                        else:
                            for i in temp:
                                if not i[0][0] in closed:
                                        fringe.push((i,node[1]+[node[0]]))
                            closed.add(state)
        else:
            path=node[1]+[node[0]]
            for i in path:
                if i[1]=='South':
                    solution.append(s)
                else:
                    if i[1]=='West':
                        solution.append(w)
                    else:
                        if i[1]=='North':
                            solution.append(n)
                        else:
                            if i[1]=='East':
                                solution.append(e)
            return solution
            

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    from util import PriorityQueue
    visited=set()
    StartState=problem.getStartState()
    fringe =PriorityQueue()
    visited.add(StartState)
    closed = set()
    trace=[]
    temp=problem.getSuccessors(problem.getStartState())
    for i in temp:  
        fringe.push((i,[]),i[-1]) 
        visited.add(i[0])
    solution=[]
    while fringe:
        fringe.heap.sort()
        node=fringe.heap[0]  
        fringe.pop()
        priority=node[0]  
        state=node[1][0][0]    
        if problem.isGoalState(state):
            goal=state
        if not problem.isGoalState(state):
                    if not state in closed:
                        temp= problem.getSuccessors(state)
                        if temp==[]:
                            visited.add(state)
                            closed.add(state)
                        else:
                            for i in temp:
                                if not i[0] in closed:    
                                    'if not i[0] in visited:'
                                    fringe.push((i,node[1][1]+[node[1][0]]),priority+i[-1])
                                    visited.add(i[0])
                            closed.add(state)

        else:
            path=node[1][1]+[node[1][0]]
            for i in path:
                if i[1]=='South':
                    solution.append(s)
                else:
                    if i[1]=='West':
                        solution.append(w)
                    else:
                        if i[1]=='North':
                            solution.append(n)
                        else:
                            if i[1]=='East':
                                solution.append(e)
            return solution

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def priorityFunction(priority):
    return priority

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    from util import PriorityQueue
    visited=set()
    StartState=problem.getStartState()
    fringe = PriorityQueue()
    visited.add(StartState)
    closed = set()
    temp=problem.getSuccessors(problem.getStartState())
    for i in temp:  
        fringe.push((i,[]),i[-1]+heuristic(i[0],problem))
        visited.add(i[0])
    solution=[]
    while fringe:
        fringe.heap.sort()
        node=fringe.heap[0]
        fringe.pop()
        cost=node[0]-heuristic(node[1][0][0],problem)
        state=node[1][0][0]
        if problem.isGoalState(state):
            goal=state
        if not problem.isGoalState(state):
                    if not state in closed:
                        temp= problem.getSuccessors(state)
                        if temp==[]:
                            closed.add(state)
                        else:
                            for i in temp:
                                if not i[0] in closed:
                                        fringe.push((i,node[1][1]+[node[1][0]]),cost+i[-1]+heuristic(i[0],problem))
                                        visited.add(i[0])
                            closed.add(state)
        else:
            path=node[1][1]+[node[1][0]]
            for i in path:
                if i[1]=='South':
                    solution.append(s)
                else:
                    if i[1]=='West':
                        solution.append(w)
                    else:
                        if i[1]=='North':
                            solution.append(n)
                        else:
                            if i[1]=='East':
                                solution.append(e)
            return solution


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
