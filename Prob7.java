public class Prob7{
	public static void main(String[] args){
		int prime = 0;
		int number = 2;
		
		while(prime < 10001){
			if(isPrime(number) == true)
				prime++;
			number++;
		}
		
		System.out.println(number);
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
