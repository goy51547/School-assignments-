package lab5;

public class Lab5Methods {
	/**
	 * 
	 * @param n an integer number
	 * @return sum of n down by 2
	 */
	public static int sumDownBy2(int n){
		int ans=n;
		for(n-=2;n>0;n-=2){
			ans=ans+n;
		}
		return ans;
	}
	/**
	 * 
	 * @param n an integer
	 * @return sum of 1/n for n from 1 to n
	 */
	public static double harmonicSum(int n){
		double ans=1;
		for(int i=2;i<=n;i++){
			ans+=1/(double)i;
		}
		return ans;
	}
	/**
	 * 
	 * @param k integer
	 * @return sum of 1/(2^k) for k from 0 to k
	 */
	public static double geometricSum(int k){
		double ans=0;
		for(int i=0;i<=k;i++){
			ans+=1.0/Math.pow(2,i);
		}
		return ans;
	}
	/**
	 * 
	 * @param j positive integer
	 * @param k positive integer
	 * @return j*k
	 */
	public static int multPos(int j, int k){
		int ans=0;
		for(int i=0;i<k;i++){
			ans+=j;
		}
		return ans;
	}
	/**
	 * 
	 * @param j integer
	 * @param k integer
	 * @return j*k
	 */
	public static int mult(int j, int k){
		int ans=multPos(Math.abs(j),Math.abs(k));
		if(j<0&&k<0){
			return ans;
		}
		else if(j<0||k<0){
			return -ans;
		}
		else
			return ans;
	}
	/**
	 * 
	 * @param n integer
	 * @param k integer
	 * @return power of n to k
	 */
	public static int expt(int n, int k){
		int ans=1;
		for(int i=0;i<k;i++){
			ans*=n;
		}
		return ans;
	}

}
