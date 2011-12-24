public class Prob5{
	/*  232792560
	* Every number can be expressed as the sum of primes. Hence we
	* just need to find the lowest common multiple of all primes
	* less than 20. i.e. the higest powers less than <n> for all primes.
	* The function getLCM does this for the first <n> natural numbers.
	*/
	
	public static void main(String[] args){
		int n = 20;
		int result = getLCM(n);
		System.out.println(result);
	}
	
	private static int getLCM(int max){
		int LCM = 1;
		int mult = 1;
		for(int i = 2; i <= max; i++){
			if(isPrime(i)){
				mult = getGreatestPower(i, max);
				LCM = LCM * mult;
			}
		}
		return LCM;
	}
	
	private static int getGreatestPower(int i, int max){
		int val = i;
		while(val <= max){
			val = val * i;
		}
		val = val/i;
		return val;
	}
	
	private static boolean isPrime(int num){
		if(num == 2)
			return true;
		
		int tag = 2;
		if(num % tag == 0)
			return false;
		
		tag++;
		while(tag < num/2){
			if(num % tag == 0)
				return false;
			tag += 2;
		}
		
		return true;
	}
}
