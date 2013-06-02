public class LargestPrimeFactor{
	
	public static void main(String args[]){

		long TO_FACTOR = 600851475143l;
		long present_factor = 2l;
		boolean factoring_done = false;
		long highest_prime = -1l;

		while(!factoring_done){
			if (TO_FACTOR % present_factor == 0l){
				TO_FACTOR /= present_factor;
				highest_prime = present_factor;
			} else {
				present_factor += 1l;
			}

			if (present_factor > TO_FACTOR){
				factoring_done = true;
			}
		}

		System.out.println(highest_prime);
		System.out.println(TO_FACTOR);

	}
}
