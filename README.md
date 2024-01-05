We need python 3.6 environment, we can use Conda to config.

# Creating a Conda Environment

Run the following command.

    conda create --name cmpt310 python=3.6
    conda activate cmpt310

### Pacman Problem

ThispartisadaptedfromUCBerkeleyandUW.

#### Introduction

Inthisproject,yourPacmanagentwillfindpathsthroughhismazeworld,bothtoreach
a particular location and to collect food efficiently. You will build general search algo-
rithmsandapplythemtoPacmanscenarios.

As in Project 0, this project includes an autograder for you to grade your answers on
yourmachine. Thiscanberunwiththecommand:

python autograder.py

SeetheautogradertutorialinProject0formoreinformationaboutusingtheautograder.

The code for this project consists of several Python files, some of which you will need
to read and understand in order to complete the assignment, and some of which you
can ignore. You can download all the code and supporting files as a zip archive from
Files/Assignment 1/search.zip.

Filesyou’lledit:

- search.py→Whereallofyoursearchalgorithmswillreside.
- searchAgents.py→Whereallofyoursearch-basedagentswillreside.

Filesyoumightwanttolookat:

- pacman.py→ThemainfilethatrunsPacmangames. ThisfiledescribesaPacman
    GameStatetype,whichyouuseinthisproject.
- game.py→The logic behind how the Pacman world works. This file describes
    severalsupportingtypeslikeAgentState,Agent,Direction,andGrid.
- util.py→Usefuldatastructuresforimplementingsearchalgorithms.

Supportingfilesyoucanignore:

- graphicsDisplay.py→GraphicsforPacman
- graphicsUtils.py→SupportforPacmangraphics
- textDisplay.py→ASCIIgraphicsforPacman


- ghostAgents.py→Agentstocontrolghosts
- keyboardAgents.py→KeyboardinterfacestocontrolPacman
- layout.py→Codeforreadinglayoutfilesandstoringtheircontents
- autograder.py→Projectautograder
- testParser.py→Parsesautogradertestandsolutionfiles
- testClasses.py→Generalautogradingtestclasses
- test_cases/Directorycontainingthetestcasesforeachquestion
- searchTestClasses.py→Project1specificautogradingtestclasses

### Welcome to Pacman

```
After downloading the code (search.zip), unzipping it, and changing to the directory,
youshouldbeabletoplayagameofPacmanbytypingthefollowingatthecommand
line:
```
```
python pacman.py
```
Pacmanlivesinashinyblueworldoftwistingcorridorsandtastyroundtreats. Navigat-
ingthisworldefficientlywillbePacman’sfirststepinmasteringhisdomain.
Thesimplest agentinsearchAgents.pyiscalled theGoWestAgent, whichalways goes
West(atrivialreflexagent). Thisagentcanoccasionallywin:

```
python pacman.py --layout testMaze --pacman GoWestAgent
```
```
But,thingsgetuglyforthisagentwhenturningisrequired:
```
```
python pacman.py --layout tinyMaze --pacman GoWestAgent
```
```
IfPacmangetsstuck,youcanexitthegamebytypingCTRL-cintoyourterminal.
Soon,youragentwillsolvenotonlytinyMaze,butanymazeyouwant.
Notethatpacman.pysupportsanumberofoptionsthatcaneachbeexpressedinalong
way(e.g.,--layout)orashortway(e.g.,-l). Youcanseethelistofalloptionsandtheir
defaultvaluesvia:
```
```
python pacman.py -h
```

Also, all of the commands that appear in this project also appear incommands.txt, for
easycopyingandpasting. InUNIX/MacOSX,youcanevenrunallthesecommandsin
orderwithbashcommands.txt.

Files to Edit and Submit: You will fill in portions ofsearch.pyandsearchAgents.py
during the assignment. You should submit these files with your code and comments.
Please do not change the other files in this distribution or submit any of our original
filesotherthanthesefiles.

Evaluation: Your code will be autograded for technical correctness. Please do not
change the names of any provided functions or classes within the code, or you will
wreak havoc on the autograder. However, the correctness of your implementation –
nottheautograder’sjudgements–willbethefinaljudgeofyourscore. Ifnecessary,we
willreviewandgradeassignmentsindividuallytoensurethatyoureceiveduecreditfor
yourwork.

### Question 1 (3 points)

Finding a Fixed Food Dot using Depth First Search. InsearchAgents.py, you’ll find a
fully implementedSearchAgent, which plans out a path through Pacman’s world and
thenexecutesthatpathstep-by-step. Thesearchalgorithmsforformulatingaplanare
notimplemented–that’syourjob.

First,testthattheSearchAgentisworkingcorrectlybyrunning:

python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

The command above tells theSearchAgentto usetinyMazeSearchas its search algo-
rithm, which is implemented insearch.py. Pacman should navigate the maze success-
fully.

Nowit’stimetowritefull-fledgedgenericsearchfunctionstohelpPacmanplanroutes!
Pseudocode for the search algorithms you’ll write can be found in the lecture slides.
Remember that a search node must contain not only a state but also the information
necessarytoreconstructthepath(plan)whichgetstothatstate.

Importantnote:Allofyoursearchfunctionsneedtoreturnalistofactionsthatwilllead
the agent from the start to the goal. These actions all have to be legal moves (valid
directions,nomovingthroughwalls).

Importantnote:Make sure to use the Stack, Queue and PriorityQueue data structures
providedtoyouinutil.py! Thesedatastructureimplementationshaveparticularprop-
ertieswhicharerequiredforcompatibilitywiththeautograder.

Hint:Each algorithm is very similar. Algorithms for DFS, BFS, UCS, and A* differ only
in the details of how the frontier is managed. So, concentrate on getting DFS right
andtherestshouldberelativelystraightforward. Indeed,onepossibleimplementation
requires only a single generic search method which is configured with an algorithm-


```
specificqueuingstrategy. (Yourimplementationneednotbeofthisformtoreceivefull
credit).
Implement the depth-first search (DFS) algorithm in thedepthFirstSearchfunction in
search.py. To make your algorithm complete, write the graph search version of DFS,
whichavoidsexpandinganyalreadyvisitedstates.
Yourcodeshouldquicklyfindasolutionfor:
```
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
```
The Pacman board will show an overlay of the states explored, and the order in which
they were explored (brighter red means earlier exploration). Is the exploration order
what you would have expected? Does Pacman actually go to all the explored squares
onhiswaytothegoal?
Hint:IfyouuseaStackasyourdatastructure,thesolutionfoundbyyourDFSalgorithm
formediumMazeshould have a length of 130 (provided you push successors onto the
frontier in the order provided bygetSuccessors; you might get 246 if you push them
in the reverse order). Is this a least cost solution? If not, think about what depth-first
searchisdoingwrong.
```
### Question 2 (3 points): Breadth First Search

```
Implement the breadth-first search (BFS) algorithm in the breadthFirstSearch function
insearch.py. Again,writeagraphsearchalgorithmthatavoidsexpandinganyalready
visitedstates. Testyourcodethesamewayyoudidfordepth-firstsearch.
```
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z.
```
```
DoesBFSfindaleastcostsolution? Ifnot,checkyourimplementation.
Hint:IfPacmanmovestooslowlyforyou,trytheoption–frameTime0.
Note: If you’ve written your search code generically, your code should work equally
wellfortheeight-puzzlesearchproblemwithoutanychanges.
```
```
python eightpuzzle.py
```
### Question 3 (3 points): Varying the Cost Function

While BFS will find a fewest-actions path to the goal, we might want to find paths that
are”best”inothersenses. ConsidermediumDottedMazeandmediumScaryMaze.


Bychangingthecostfunction,wecanencouragePacmantofinddifferentpaths. Forex-
ample,wecanchargemorefordangerousstepsinghost-riddenareasorlessforsteps
infood-richareas,andarationalPacmanagentshouldadjustitsbehaviorinresponse.

Implementtheuniform-costgraphsearchalgorithmintheuniformCostSearchfunction
insearch.py. We encourage you to look through util.py for some data structures that
maybeusefulinyourimplementation. Youshouldnowobservesuccessfulbehaviorin
allthreeofthefollowinglayouts,wheretheagentsbelowareallUCSagentsthatdiffer
onlyinthecostfunctiontheyuse(theagentsandcostfunctionsarewrittenforyou):

python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

Note:You should get very low and very high path costs for theStayEastSearchAgent
andStayWestSearchAgentrespectively,duetotheirexponentialcostfunctions(seesearchAgents.py
fordetails).

### Question 4 (3 points): A* search

ImplementA*graphsearchintheemptyfunctionaStarSearchinsearch.py. A*takesa
heuristicfunctionasanargument. Heuristicstaketwoarguments: astateinthesearch
problem (the main argument), and the problem itself (for reference information). The
nullHeuristicheuristicfunctioninsearch.pyisatrivialexample.

YoucantestyourA*implementationontheoriginalproblemoffindingapaththrough
amazetoafixedpositionusingtheManhattandistanceheuristic(implementedalready
asmanhattanHeuristicinsearchAgents.py).

python pacman.py -l bigMaze -z .5 -p SearchAgent
-a fn=astar,heuristic=manhattanHeuristic

(Note:Writethecommandinasingleline)

YoushouldseethatA*findstheoptimalsolutionslightlyfasterthanuniformcostsearch
(about 549 vs. 620 search nodes expanded in our implementation, but ties in priority
may make your numbers differ slightly). What happens onopenMazefor the various
searchstrategies?

### Question 5 (3 points): Finding All the Corners

The real power of A* will only be apparent with a more challenging search problem.
Now,it’stimetoformulateanewproblemanddesignaheuristicforit.

In corner mazes, there are four dots, one in each corner. Our new search problem is
to find the shortest path through the maze that touches all four corners (whether the


maze actually has food there or not). Note that for some mazes liketinyCorners, the
shortestpathdoesnotalwaysgototheclosestfoodfirst! Hint: theshortestpaththrough
tinyCornerstakes28steps.

Note:MakesuretocompleteQuestion2beforeworkingonQuestion5,becauseQues-
tion5buildsuponyouranswerforQuestion2.

Implement theCornersProblemsearch problem insearchAgents.py. You will need to
chooseastaterepresentationthatencodesalltheinformationnecessarytodetectwhether
allfourcornershavebeenreached. Now,yoursearchagentshouldsolve:

python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

Toreceivefullcredit,youneedtodefineanabstractstaterepresentationthatdoesnot
encode irrelevant information (like the position of ghosts, where extra food is, etc.). In
particular,donotuseaPacmanGameStateasasearchstate. Yourcodewillbevery,very
slowifyoudo(andalsowrong).

Hint:The only parts of the game state you need to reference in your implementation
arethestartingPacmanpositionandthelocationofthefourcorners.

OurimplementationofbreadthFirstSearchexpandsjustunder2000searchnodeson
mediumCorners. However, heuristics (used with A* search) can reduce the amount of
searchingrequired.

### Question 6 (3 points): Corners Problem: Heuristic

Note:MakesuretocompleteQuestion4beforeworkingonQuestion6,becauseQues-
tion6buildsuponyouranswerforQuestion4.

Implementanon-trivial,consistentheuristicfortheCornersProblemincornersHeuristic.

python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.

Note:AStarCornersAgentisashortcutfor

-p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic

Admissibility vs. Consistency: Remember, heuristics are just functions that take search
statesandreturnnumbersthatestimatethecosttoanearestgoal. Moreeffectiveheuris-
tics will return values closer to the actual goal costs. To be admissible, the heuristic
values must be lower bounds on the actual shortest path cost to the nearest goal (and
non-negative). To be consistent, it must additionally hold that if an action has cost c,
thentakingthatactioncanonlycauseadropinheuristicofatmost𝑐.


```
Numberofnodesexpanded Grade
morethan2000 0/
atmost2000 1/
atmost1600 2/
atmost1200 3/
```
```
Table1: Gradingbasedonqualityoftheproposedheuristic.
```
Remember that admissibility isn’t enough to guarantee correctness in graph search –
you need the stronger condition of consistency. However, admissible heuristics are
usually also consistent, especially if they are derived from problem relaxations. There-
fore it is usually easiest to start out by brainstorming admissible heuristics. Once you
haveanadmissibleheuristicthatworkswell,youcancheckwhetheritisindeedconsis-
tent,too. Theonlywaytoguaranteeconsistencyiswithaproof. However,inconsistency
canoftenbedetectedbyverifyingthatforeachnodeyouexpand,itssuccessornodes
areequalorhigherininf-value. Moreover,ifUCSand𝐴∗everreturnpathsofdifferent
lengths,yourheuristicisinconsistent. Thisstuffistricky!

Non-Trivial Heuristics: The trivial heuristics are the ones that return zero everywhere
(UCS) and the heuristic which computes the true completion cost. The former won’t
save you any time, while the latter will timeout theautograder. You want a heuristic
whichreducestotalcomputetime,thoughforthisassignmenttheautograderwillonly
checknodecounts(asidefromenforcingareasonabletimelimit).

Grading: Your heuristic must be a non-trivial non-negative consistent heuristic to re-
ceive any points. Make sure that your heuristic returns 0 at every goal state and never
returns a negative value. Depending on how few nodes your heuristic expands, you’ll
begradedbasedontable 1.

Remember:Ifyourheuristicisinconsistent,youwillreceivenocredit,sobecareful!

### Question 7 (4 points): Eating All The Dots

Now we’ll solve a hard search problem: eating all the Pacman food in as few steps as
possible. For this, we’ll need a new search problem definition which formalizes the
food-clearingproblem:FoodSearchProbleminsearchAgents.py(implementedforyou).
A solution is defined to be a path that collects all of the food in the Pacman world. For
the present project, solutions do not take into account any ghosts or power pellets;
solutionsonlydependontheplacementofwalls,regularfoodandPacman. (Ofcourse
ghostscanruintheexecutionofasolution! We’llgettothatinthenextproject.) Ifyou
havewrittenyourgeneralsearchmethodscorrectly,𝐴∗withanullheuristic(equivalent
to uniform-cost search) should quickly find an optimal solution totestSearchwith no
codechangeonyourpart(totalcostof7).

python pacman.py -l testSearch -p AStarFoodSearchAgent


```
Numberofnodesexpanded Grade
morethan15000 1/
atmost15000 2/
atmost12000 3/
atmost9000 4/4 (fullcredit;medium)
atmost7000 5/4 (optionalextracredit;hard)
```
```
Table2: Gradingbasedonqualityoftheproposedheuristic.
```
Note:AStarFoodSearchAgentisashortcutfor
-p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic

```
YoushouldfindthatUCSstartstoslowdownevenfortheseeminglysimpletinySearch.
As a reference, our implementation takes2.5seconds to find a path of length 27 after
expanding 5057 searchnodes.
Note:MakesuretocompleteQuestion4beforeworkingonQuestion7,becauseQues-
tion7buildsuponyouranswerforQuestion4.
FillinfoodHeuristicinsearchAgents.pywithaconsistentheuristicfortheFoodSearchProblem.
TryyouragentonthetrickySearchboard:
```
```
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```
```
Our UCS agent finds the optimal solution in about 13 seconds, exploring over16,
nodes.
Anynon-trivialnon-negativeconsistentheuristicwillreceive1point. Makesurethatyour
heuristic returns 0 at every goal state and never returns a negative value. Depending
onhowfewnodesyourheuristicexpands,you’llbegradedbasedontable 2.
Remember: If your heuristic is inconsistent, you will receive no credit, so be careful!
CanyousolvemediumSearchinashorttime? Ifso,we’reeithervery,veryimpressed,or
yourheuristicisinconsistent.
```
### Question 8 (3 points): Suboptimal Search

```
Sometimes,evenwith𝐴∗andagoodheuristic,findingtheoptimalpaththroughallthe
dotsishard. Inthesecases,we’dstillliketofindareasonablygoodpath,quickly. Inthis
section,you’llwriteanagentthatalwaysgreedilyeatstheclosestdot.ClosestDotSearchAgent
is implemented for you insearchAgents.py, but it’s missing a key function that finds a
pathtotheclosestdot.
Implement the functionfindPathToClosestDotinsearchAgents.py. Our agent solves
thismaze(suboptimally!) inunderasecondwithapathcostof 350 :
```
```
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z.
```

Hint:ThequickestwaytocompletefindPathToClosestDotistofillintheAnyFoodSearchProblem,
whichismissingitsgoaltest. Then,solvethatproblemwithanappropriatesearchfunc-
tion. Thesolutionshouldbeveryshort!

YourClosestDotSearchAgentwon’t always find the shortest possible path through the
maze. Make sure you understand why and try to come up with a small example where
repeatedlygoingtotheclosestdotdoesnotresultinfindingtheshortestpathforeating
allthedots.

### Submission

Inordertosubmityourproject,pleaseuploadthefollowingfilestoCanvas:search.py
andsearchAgents.py. Pleasedonotuploadthefilesinazipfileoradirectory.


