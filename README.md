# sudoku
An algorithm which solves any given sudoku problem.

The basic idea of this algorithm is backtracking.
Now the reason why is works so fast even though we're kind off using brute force is that we check the validness of our solution everytime we set a new number.
So we actually conserve a lot of computation.

Here is the procedure:
* first find out the next empty cell
* then try putting every number in range 1-9 and if it is legal to put then go again to step 1(via recursion)
* if we get any solution in this path return True
* else we realize that putting that number on this position will not lead to a solution so change it to 0 again and repeat the process

