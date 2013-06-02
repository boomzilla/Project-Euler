/**
 *solution to Project Euler prompt 15
 *
 * @author Ian Ruotsala
 * @see http://projecteuler.net/problem=15
 *
 * Starting at position 0-0, traverse an n-by-n lattice using only "down" and "right" transitions (i.e. only adding to coordinates).
 * Find out how many paths can be found for a 20-by-20 lattice.
 */

class latticePaths{
	final static int LATTICE_SIZE = 20;	//size of the n by n lattice

	private static void buildSubLattice(long[][] pathCounts, int n){
		//pre: take a matrix of path counts for each coordinate;
		//     n is the n-by-n coordinate of sub-lattice we are evaluating
		//
		//post:	find the path counts for this slice of the pathCounts matrix

		//basically I want to evaluate the L-shaped sub-lattice staring at the ends of the 'L' 
		//and moving toward the "bend" of the L (i.e. coordinate at pathCounts[n][n] 
		for (int sub = LATTICE_SIZE; sub >= n; sub--){
			evaluateCoordinate(n, sub, pathCounts);
			evaluateCoordinate(sub, n, pathCounts);
		}
	}

	private static void evaluateCoordinate(int x, int y, long[][] pathCounts){
		//pre: take x, y coordinates within lattice; take pathCounts matrix
		//
		//post: set the pathCounts and x, y to the number of paths you can take from this coordinate in the lattice
		
		if (x == LATTICE_SIZE || y == LATTICE_SIZE){
			pathCounts[x][y] = 1l;
		} else {
			pathCounts[x][y] = pathCounts[x][y+1] + pathCounts[x+1][y];
		}
	}

	private static long findPathCount(){
		//post: return path count for lattice of LATTICE_SIZE

		long[][] pathCounts;	//this will store the count of paths that can be had from each coordinate
		pathCounts = new long[LATTICE_SIZE + 1][LATTICE_SIZE + 1]; 
		
		//find the path counts for sub-lattices
		for (int n = LATTICE_SIZE; n >= 0; n--){
			buildSubLattice(pathCounts, n);
		}	

		return pathCounts[0][0];
	}

	public static void main(String[] args){
		long pathCount = findPathCount();
		System.out.println(pathCount);	
	}
}
