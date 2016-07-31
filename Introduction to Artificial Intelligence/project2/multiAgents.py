# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import GameStateData
from game import Game
from game import Directions
from game import Actions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    distToFood=9999
    for foodPos in newFood.asList():
        dist=util.manhattanDistance( foodPos, newPos)
        if distToFood>dist:
            distToFood=dist
            foodPosition=foodPos
    if len(newFood.asList())>0:
        if util.manhattanDistance( foodPosition, newPos)<util.manhattanDistance( foodPosition, currentGameState.getPacmanPosition()):
            successorGameState.data.score=successorGameState.data.score+1
    distToGhost=util.manhattanDistance( newPos, newGhostStates[0].configuration.pos)
    if distToGhost>=5:
        distToGhost=5
    successorGameState.data.score=successorGameState.data.score+distToGhost
    return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    depth=self.depth
    numOfGhost = gameState.getNumAgents()-1
    def maxV(state,depth):
        if state.isWin() or state.isLose():
            return [self.evaluationFunction(state)]
        getAction=False
        depth =depth-1
        maxValue=float("-inf")
        legalMoves = state.getLegalActions(0)
        for action in legalMoves:
            successorGameState=state.generateSuccessor(0, action)
            tempValue= minV(successorGameState,depth,1)
            if tempValue>maxValue:
                maxValue =tempValue
                bestAction=action
                getAction=True
                           
            #if successorGameState.isWin() or successorGameState.isLose(): return 0
        if getAction:
            return [maxValue,bestAction]
        else:
            return [maxValue]
            
    def minV(state,depth,ghostIndex):
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)
        legalMoves = state.getLegalActions(ghostIndex)
        minValue=float("inf")
        for action in legalMoves:
            successorGameState=state.generateSuccessor(ghostIndex, action)
            if ghostIndex < numOfGhost:
                tempValue = minV(successorGameState,depth,ghostIndex+1)
                if tempValue<minValue:
                    minValue=tempValue    
            else:
                if depth >0:
                    tempValue=maxV(successorGameState,depth)[0]
                    if tempValue<minValue:
                        minValue=tempValue                    
                else:
                    tempValue=self.evaluationFunction(successorGameState)
                    if tempValue<minValue:
                        minValue=tempValue
        return minValue
    # Choose one of the best actions
    result = maxV(gameState,depth)
    bestAction=result[1]
    #else:
    #    bestAction="Stop"
    return bestAction

    "Add more of your code here if you want to"


class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    depth=self.depth
    numOfGhost = gameState.getNumAgents()-1
    def maxV(state,depth):
        if state.isWin() or state.isLose():
            return [self.evaluationFunction(state)]
        pruneRecord=0
        getAction=False
        depth =depth-1
        maxValue=float("-inf")
        legalMoves = state.getLegalActions(0)
        for action in legalMoves:
            successorGameState=state.generateSuccessor(0, action)
            tempValue= minV(successorGameState,depth,1,pruneRecord)
            pruneRecord=tempValue
            if tempValue>maxValue:
                maxValue =tempValue
                bestAction=action
                getAction=True                
            #if successorGameState.isWin() or successorGameState.isLose(): return 0
        if getAction:
            return [maxValue,bestAction]
        else:
            return [maxValue]
            
    def minV(state,depth,ghostIndex,pruneRecord):
        pruned=False
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)
        legalMoves = state.getLegalActions(ghostIndex)
        minValue=float("inf")
        for action in legalMoves:
            if pruned:
                break
            successorGameState=state.generateSuccessor(ghostIndex, action)
            if ghostIndex < numOfGhost:
                tempValue = minV(successorGameState,depth,ghostIndex+1,pruneRecord)
                if tempValue<minValue:
                    minValue=tempValue  
            else:
                if depth >0:
                    tempValue=maxV(successorGameState,depth)[0]
                    if tempValue<minValue:
                        minValue=tempValue                    
                else:
                    tempValue=self.evaluationFunction(successorGameState)
                    if tempValue<pruneRecord:
                        pruned=True
                    if tempValue<minValue:
                        minValue=tempValue
        return minValue
    # Choose one of the best actions
    result = maxV(gameState,depth)
    bestAction=result[1]
    return bestAction

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    depth=self.depth
    numOfGhost = gameState.getNumAgents()-1
    def maxV(state,depth):
        if state.isWin() or state.isLose():
            return [self.evaluationFunction(state)]
        getAction=False
        depth =depth-1
        maxValue=float("-inf")
        legalMoves = state.getLegalActions(0)
        for action in legalMoves:
            successorGameState=state.generateSuccessor(0, action)
            tempValue= expectation(successorGameState,depth,1)
            if tempValue>=maxValue:
                maxValue =tempValue
                bestAction=action
                getAction=True
                           
            #if successorGameState.isWin() or successorGameState.isLose(): return 0
        if getAction:
            return [maxValue,bestAction]
        else:
            return [maxValue]
            
    def expectation(state,depth,ghostIndex):
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)
        legalMoves = state.getLegalActions(ghostIndex)
        probability=1/float(len(legalMoves))
        minValue=0
        for action in legalMoves:
            successorGameState=state.generateSuccessor(ghostIndex, action)
            if ghostIndex < numOfGhost:
                tempValue = expectation(successorGameState,depth,ghostIndex+1)
                minValue=tempValue*probability+minValue 
            else:
                if depth >0:
                    tempValue=maxV(successorGameState,depth)[0]
                    minValue=tempValue*probability+minValue                   
                else:
                    tempValue=self.evaluationFunction(successorGameState)
                    minValue=tempValue*probability+minValue
        return minValue
    # Choose one of the best actions
    result = maxV(gameState,depth)
    bestAction=result[1]
    #else:
    #    bestAction="Stop"
    return bestAction

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: What I considered in this function is the maze distance of form pacman to the food that has
    minimum manhhatan distance to the pacman. Also the manhattandistance of the loaset ghost to pacman. 
    If one capsule is eaten, the score will be added by 15, so to encourage the pacman to eat capsules.
  """
  "*** YOUR CODE HERE ***"
  basicScore=currentGameState.getScore()
  distToFood=9999
  distToCap=9999
  distToGhost=9999
  locations=[]
  for agent in currentGameState.data.agentStates:
      locations=locations+[agent.configuration.pos]
  pacmanPos=locations[0]
  ghostPos=locations[1:]
  capsulePos=currentGameState.data.capsules
  
  for capsuleP in capsulePos:
    dist=util.manhattanDistance( capsuleP, pacmanPos)
    if distToCap>dist:
        distToCap=dist
  foodList=currentGameState.data.food.asList()
  for foodPos in foodList:
    dist=util.manhattanDistance( foodPos, pacmanPos)
    if distToFood>dist:
        distToFood=dist
        foodPosition=foodPos

  for ghostP in ghostPos:
      dist=util.manhattanDistance( ghostP , pacmanPos)
      if distToGhost>dist:
          distToGhost=dist
          ghostPosition=ghostP   
  if len(foodList)>1:
      if distToGhost>4:
          score=basicScore-0.2*mazeDistance(pacmanPos, foodPosition, currentGameState)
      else:
          score=basicScore-0.2*mazeDistance(pacmanPos, foodPosition, currentGameState)+0.3*distToGhost
  else:
      if len(foodList)==1:
          score=basicScore-0.2*mazeDistance(pacmanPos, foodPosition, currentGameState)
      else:
          score=basicScore
  score-=15*len(capsulePos)
  return score

class PositionSearchProblem():


    def __init__(self, gameState, start=None, goal=(1,1),  warn=True):
        self.walls = gameState.getWalls()
        self.startState = start
        self.goal = goal

        # For display purposes
        self._visited, self._visitedlist, self._expanded = {}, [], 0

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        isGoal = state == self.goal

        # For display purposes only
        if isGoal:
            self._visitedlist.append(state)
            import __main__
            if '_display' in dir(__main__):
                if 'drawExpandedCells' in dir(__main__._display): #@UndefinedVariable
                    __main__._display.drawExpandedCells(self._visitedlist) #@UndefinedVariable

        return isGoal

    def getSuccessors(self, state):
        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                successors.append( ( nextState, action, 1) )

        # Bookkeeping for display purposes
        self._expanded += 1
        if state not in self._visited:
            self._visited[state] = True
            self._visitedlist.append(state)

        return successors

    def getCostOfActions(self, actions):
        if actions == None: return 999999
        x,y= self.getStartState()
        cost = 0
        for action in actions:
            # Check figure out the next state and see whether its' legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
            cost += self.costFn((x,y))
        return cost

def breadthFirstSearch(problem):
    from game import Directions
    from util import Queue
    traces=[]
    StartState=problem.getStartState()
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


def mazeDistance(point1, point2, gameState):
    """
    Returns the maze distance between any two points, using the search functions
    you have already built.  The gameState can be any game state -- Pacman's position
    in that state is ignored.

    Example usage: mazeDistance( (2,4), (5,6), gameState)

    This might be a useful helper function for your ApproximateSearchAgent.
    """
    x1, y1 = point1
    x2, y2 = point2
    walls = gameState.getWalls()
    assert not walls[x1][y1], 'point1 is a wall: ' + point1
    assert not walls[x2][y2], 'point2 is a wall: ' + str(point2)
    prob = PositionSearchProblem(gameState, start=point1, goal=point2, warn=False)
    return len(breadthFirstSearch(prob))
# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

