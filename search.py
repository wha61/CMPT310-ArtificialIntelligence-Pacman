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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Here I use stack as my data structure
    from util import Stack
    frontier = Stack()
    # store the nodes that have been explored, in case of avoiding actions go to the explored nodes
    listOfExplored = []
    # get first node from problem and check if it is goal node
    initialNode = problem.getStartState()
    if problem.isGoalState(initialNode):
        return []
    # set up the initial frontier, with its initial action is empty
    frontier.push((initialNode, []))

    # keep update the stack until find the goal node
    while True:
        # pop the last push node
        currentNode, currentActions = frontier.pop()
        # first check if current node is the goal node, if it is, return its actions
        if problem.isGoalState(currentNode):
            return currentActions
        # else add node to explored list and expand it
        else:
            childNodes = problem.getSuccessors(currentNode)
            listOfExplored.append(currentNode)
            # use for loop to push child nodes that not in the explored list
            # push their successor and actions to stack
            for childNode in childNodes:
                successor, action, cost = childNode
                childActions = currentActions + [action]
                if successor not in listOfExplored:
                    frontier.push((successor, childActions))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Here I use queue as my data structure
    from util import Queue
    frontier = Queue()
    # store the nodes that have been explored, in case of avoiding actions go to the explored nodes
    listOfExplored = []
    # get first node from problem and check if it is goal node
    initialNode = problem.getStartState()
    if problem.isGoalState(initialNode):
        return []
    # set up the initial frontier, with its initial action is empty
    frontier.push((initialNode, []))

    # keep update the queue until find the goal node
    while True:
        # pop the last push node
        currentNode, currentActions = frontier.pop()
        # first check if current node is in the explored list, avoid situation like loops
        if currentNode not in listOfExplored:
            # check if current node is the goal node, if it is, return its actions
            if problem.isGoalState(currentNode):
                return currentActions
            # else add node to explored list and expand it
            else:
                childNodes = problem.getSuccessors(currentNode)
                listOfExplored.append(currentNode)
                # use for loop to push child nodes that not in the explored list
                # push their successor and actions to queue
                for childNode in childNodes:
                    successor, action, cost = childNode
                    childActions = currentActions + [action]
                    if successor not in listOfExplored:
                        frontier.push((successor, childActions))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Here I use PriorityQueue as my data structure
    from util import PriorityQueue
    frontier = PriorityQueue()
    # store the nodes that have been explored, in case of avoiding actions go to the explored nodes
    listOfExplored = []
    # get first node from problem and check if it is goal node
    initialNode = problem.getStartState()
    if problem.isGoalState(initialNode):
        return []
    # set up the initial frontier, with its initial action is empty, initial cost is 0
    frontier.push((initialNode, []), 0)

    # keep update the PriorityQueue until find the goal node
    while not frontier.isEmpty():
        # pop the last push node
        currentNode, currentActions = frontier.pop()
        # first check if current node is in the explored list, avoid situation like loops
        if currentNode not in listOfExplored:
            # check if current node is the goal node, if it is, return its actions
            if problem.isGoalState(currentNode):
                return currentActions
            # else add node to explored list and expand it
            else:
                childNodes = problem.getSuccessors(currentNode)
                listOfExplored.append(currentNode)
                # use for loop to push child nodes that not in the explored list
                # push their successor and actions to queue
                for childNode in childNodes:
                    successor, action, cost = childNode
                    childActions = currentActions + [action]
                    if successor not in listOfExplored:
                        actionCosts = problem.getCostOfActions(childActions)
                        frontier.update((successor, childActions), actionCosts)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Here I use queue as my data structure
    frontier = util.PriorityQueue()
    # store the nodes that have been explored, in case of avoiding actions go to the explored nodes
    listOfExplored = []
    # get first node from problem and check if it is goal node
    initialNode = problem.getStartState()
    if problem.isGoalState(initialNode):
        return []
    # set up the initial frontier, with its initial action is empty
    frontier.push((initialNode, []), heuristic(initialNode, problem) + 0)

    # keep update the queue until find the goal node
    while not frontier.isEmpty():
        # pop the last push node
        currentNode, currentActions = frontier.pop()
        # first check if current node is the goal node, if it is, return its actions
        if currentNode not in listOfExplored:
            if problem.isGoalState(currentNode):
                return currentActions
            # else add node to explored list and expand it
            else:
                childNodes = problem.getSuccessors(currentNode)
                listOfExplored.append(currentNode)
                # use for loop to push child nodes that not in the explored list
                # push their successor and actions to queue
                for childNode in childNodes:
                    successor, action, cost = childNode
                    childActions = currentActions + [action]
                    if successor not in listOfExplored:
                        actionCosts = problem.getCostOfActions(childActions)
                        heuristicCosts = heuristic(successor, problem)
                        frontier.update((successor, childActions), heuristicCosts + actionCosts)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
