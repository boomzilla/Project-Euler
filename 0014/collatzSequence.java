//collatzSequence.java, coded by Ian Ruotsala
//2013, Mar 15
//
//solution to Project Euler question 14:
//find longest Collatz sequence of all numbers starting under 1 million
import java.util.*;

public class collatzSequence{
	final static int LIMIT = 1000000;	//find Collatz sequences that are under this number
	static int[] seqLength;				//record the length of Collatz sequences for each number

	private static int generateSeq(int m){
		//pre: take an int n, to generate Collatz sequence from.
		//	   take an int array which records 
		/*ArrayList<Integer> toReturn = new ArrayList<Integer>();
		toReturn.add(n);
		while (n != 1){
			if (n % 2 == 0) {
				n = n/2;
			} else {//n is odd
				n = 3*n + 1;
			}
			toReturn.add(n);
		}*/
		///*toReturn.add(n);
		long n = m;		//this is to avoid overflow of Java's int: Collatz sequence items can grow very large

		int toReturn = 0;
		while (true){
			if (n >= LIMIT || seqLength[(int)n] == -1){
				//System.out.println("n = " + n);
				toReturn++;
				if (n == 1l){
					return toReturn;
				} else if (n % 2l == 0l){
					n = n/2l;
				} else{ //n is odd, not equal to 1
					n = 3l*n + 1l;
				}
			} else { //we have found an already-found length
				return toReturn + seqLength[(int)n];
			}
		}	

		/*
		int toReturn = 0;
		if (n >= LIMIT || seqLength[n] == -1){
			if (n == 1){
				return 1;
			} else if (n % 2 == 0) {
				toReturn = 1 + generateSeq(n/2);
			} else {//n is odd
				toReturn = 1 + generateSeq(3*n + 1);
			}
		} else {
			toReturn = seqLength[n];
		}*/
		//return toReturn;
		//return -1; //code should never get here
	}
	/*
	private static void strikeSubseq(ArrayList<Integer> sequence, int[] possibleAnswers){
		for (Integer n : sequence){
			if (n < LIMIT){
				possibleAnswers[n] = -1;
			}
		}
	}*/

	public static void main(String[] args){
		int answer = 1;	//number which produces longest sequence

		//initialize array to record which numbers already found a length of Collatz sequence for	
		seqLength = new int[LIMIT];
		for (int n = LIMIT - 1; n > 0; n--){
			seqLength[n] = -1; //since we haven't found any sequences yet, initialize everything to -1
		}

		//find Collatz sequences from 1 to LIMIT
		for (int n = 1; n < LIMIT; n++){
			int thisSeqLength = generateSeq(n);
			seqLength[n] = thisSeqLength;
			if (thisSeqLength > seqLength[answer]){
				answer = n;
			}
		}

		System.out.println(answer);	
	}

	/*
	public static void main(String[] args){
		int longestSequenceCount = 0;
		int answer = -1;	//number which produces longest sequence

		//initialize array to record which numbers have already been found within sub-sequences of other sequences
		int[] possibleAnswers = new int[LIMIT];
		for (int n = LIMIT - 1; n > 0; n--){
			possibleAnswers[n] = n;
		} 
		
		//go from low to high, generating Collatz sequences for each
		for (int n = LIMIT - 1; n > 0; n--){
			//ignore numbers already found within sub-sequences	
			if (possibleAnswers[n] != -1){
				ArrayList<Integer> sequence = new ArrayList<Integer>();
				sequence = generateSeq(n);			
				if (sequence.size() > longestSequenceCount){
					longestSequenceCount = sequence.size();
					answer = n;
				}
				strikeSubseq(sequence, possibleAnswers);
			}
		}
		System.out.println(answer);
	}*/
}
