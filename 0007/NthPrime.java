class NthPrime{
	public static void main(String[] args){
		final int TARGET_PRIME = 10001;
		int[] primeArray;
		primeArray = new int[TARGET_PRIME];
		int primeCount = 0;
		int presentNumber = 2;
		while (primeCount < TARGET_PRIME){
			boolean isPrime = true;
			for (int n = 0; n < primeCount; n++){
				if (presentNumber % primeArray[n] == 0){
					isPrime = false;
				}
			}
			if (isPrime){
				primeArray[primeCount] = presentNumber;
				primeCount++;
			}
			presentNumber++;
		}
		System.out.println(primeArray[TARGET_PRIME - 1]);
	}
}
