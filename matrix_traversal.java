/* package whatever; // don't place package name! */  
 
import java.util.*;
import java.lang.*;
 
class Guvi
{
  	private int rows;
    private int cols;
    private int[][] grid;
  	public Guvi(int n, int m, int[][] grid) {
        this.rows = n;
        this.cols = m; 
        this.grid = grid;
    }
  	public boolean isValid (int x, int y) {
        // Returns false if:
        //  1. x or y is out of matrix's bounds
        //  2. cell [x][y] was already visited (contains a -1) or is not filled (contains a 0)
        if (    x < 0 
            ||  y < 0 
            ||  x >= rows 
            ||  y >= cols 
            ||  grid[x][y] < 1
           ) {
            return false;
        }
        else {
            // Current cell is valid (i.e., exists in matrix, is filled and not yet visited)
            return true;
        }
    }
  	public int dfs(int x, int y) {
        if (isValid(x, y) == false) {
            return 0;
        }

        int count = 1;
        int newX = x;
        int newY = y;
        grid[x][y] = -1;
        
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                newX = x + i;
                newY = y + j;
                
                count = count + dfs(newX, newY);
            }
        }

        return count;
    }
  	public int solve() {
        // Stores size of current largest region
        int maxVal = 0;
        // Stores size of region currently being checked
        int tempVal = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Find the number of filled connected cells (if any) for this potential region
                tempVal = dfs(i, j);
                
                // If the current region is larger than any previously checked region, set new maxVal
                if(tempVal > maxVal) {
                    maxVal = tempVal; 
                }
            }
        }
        
        return maxVal;
    }
public static void main (String[] args) throws java.lang.Exception 
  {  
  	Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[][] matrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {          
                matrix[i][j] = scanner.nextInt();
            }
        }
  	scanner.close();
        
        Guvi solution = new Guvi(n, m, matrix);
        System.out.println(solution.solve());
   } 
 }; 
