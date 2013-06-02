//find the sum of all primes below 2 million
//Project Euler challenge 10

public class sumOfPrimes{
	static int LIMIT = 2000001;

	private static void doFilter(int prime, int[] sieve){
		for (int n = prime * 2; n < LIMIT; n += prime){
			sieve[n] = -1;
		}
	}

	private static void doSieve(int[] sieve){
		long sum = 0;
		for (int n = 2; n < LIMIT; n++){
			if (sieve[n] != -1){
				doFilter(n, sieve);
				sum += n;
			}
		}
		
		System.out.println(sum);
	}

	public static void main(String[] args){
		//do sieve of Eritosthenes; each time prime found, add to sum
		int[] sieve;
		sieve = new int[LIMIT];
		//initialize array
		for (int n = 0; n < LIMIT; n++){
			sieve[n] = n;
		}
		
		doSieve(sieve);
	}
}
