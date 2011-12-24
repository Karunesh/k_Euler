public class Prob4{
	/*
	* Start from the number 999999, the largest
	* 6-digit number, and go back by 1 at each iteration.
	* 	At each iteration, 
	*				1. check if the number is a palindrome
	*				2. if yes, for all its 3-digit factors, find the second factor
	*						i.e. if f1 = 443, find f2
	*				3. if f2 is a 3-digit number, (999999 - (the iteration we are in))
	*						is the solution
	*				* otherwise, iterate
	*/
	public static void main(String[] args){
		int num = 999999;
		int fact1 = 999;
		int fact2 = 100;
		while(num > 100000){
			if(isPalindrome(num)){
				fact1 = 999;
				while(fact1 > 99){
					if((num % fact1) == 0){
						if(getDigits((num / fact1)) == 3){
							fact2 = num / fact1;
							break;
						}
					}
				fact1--;			
				}
			}
			if(fact2 != 100)
				break;
			num--;
		}
		System.out.println(fact1 + " * " + fact2 + " = " + num);
	}
	
	//Tell whether a number is a palindrome
	public static boolean isPalindrome(int num){
		int digits = getDigits(num);
		if(digits == 1) //no use trying when a number is single digit
			return false;
		int[] digitified = new int[digits];
		int start = 0;
		int end = digits - 1;
		for(int i = (digits - 1); i >= 0; i--){
			digitified[i] = num % 10;
			num = num / 10;
		}
		while(start < end){
			if(digitified[start] != digitified[end])
				return false;
			start++;
			end--;
		}
		return true;
	}
	
	//give number of digits in a number
	public static int getDigits(int num){
		int digit = 0;
		int val = 10;
		while(num > 0){
			num = num/10;
			digit++;
		}
		return digit;
	}
}
