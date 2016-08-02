package lab6;

public class Beer {

	public static String bottlesOfBeer(int n){
		String ans="";
		if(n<1){
			return ans+="";
		}
		else return ans+=n+" bottles of beer on the wall, "+n+" bottles of beer; you take one down, pass it around, "+(n-1)+" bottles of beer on the wall."+"\n"+bottlesOfBeer(n-1);
	}
	public static void main(String[] args) {
		// FIXME Auto-generated method stub
		System.out.println(bottlesOfBeer(3));
	}

}
