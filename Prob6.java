//25164150
public class Prob6{
	public static void main(String[] args){
		int i = 1;
		int j = 1;
		int result = 0;
		for(i = 1; i <= 100; i++){
			for(j = 1; j <= 100; j++){
				if(i != j){
					result = result + i * j;
				}
			}
		}
		
		System.out.println(result);
	}
}
