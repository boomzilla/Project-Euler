public class pythTrip{
	static int SUM = 1000;

	private static boolean checkForTriple(int a, int b, int c){
		return (a * a + b * b == c * c);
	}

	public static void main(String[] args){
		int a = 1;
		int b = -1;
		int c = -1;
		boolean triple_found = false;
		while (!triple_found){
			b = a + 1;
			c = SUM - b - a;
			while(!triple_found && b < c){
				triple_found = checkForTriple(a,b,c);
				if (!triple_found){
					b++;
					c--;
				}
			}
			if (!triple_found){
				a++;
			}
		}

		System.out.println("a= " + a);
		System.out.println("b= " + b);
		System.out.println("c= " + c);	
		System.out.println(a * b * c);
	}
}
