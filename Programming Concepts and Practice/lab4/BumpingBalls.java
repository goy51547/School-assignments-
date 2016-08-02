package lab4;

import cse131.ArgsProcessor;
import sedgewick.StdDraw;

public class BumpingBalls {
	
	public static void main(String[] args) {
		ArgsProcessor ap =new ArgsProcessor(args);
		int N = ap.nextInt("How many balls?");
        StdDraw.setXscale(-1.0, 1.0);
        StdDraw.setYscale(-1.0, 1.0);
		double [][] balls = new double [N][4];
		for (int i =0; i<N; i++){
			double rx = Math.round(100*(Math.random()*1.975-0.95))/100.0;
			double ry = Math.round(100*(Math.random()*1.975-0.95))/100.0;
			balls[i][0]=rx;
			balls[i][1]=ry;
			double vx = Math.round(1000*(Math.random()*0.08))/1000.0;
			double vy = Math.round(1000*(Math.random()*0.08))/1000.0;
			balls[i][2]=vx;
			balls[i][3]=vy;
		}
        double radius = 0.05;              // radius

        // main animation loop
        while (true)  { 

            // bounce off wall according to law of elastic collision
            for(int i =0 ; i<N; ++i){
                if (Math.abs(balls[i][0] + balls[i][2]) > 1.0 - radius) balls[i][2] = -balls[i][2];
                if (Math.abs(balls[i][1] + balls[i][3]) > 1.0 - radius) balls[i][3] = -balls[i][3];
                for (int j =i+1; j<N; j++){
                	double dist = Math.sqrt(Math.pow(balls[i][0] - balls[j][0],2)+Math.pow(balls[i][1] - balls[j][1],2));
                	if (dist <= 2*radius){
                		balls[i][2] = -balls[i][2];
                		balls[i][3] = -balls[i][3];
                		balls[j][2] = -balls[j][2];
                		balls[j][3] = -balls[j][3];
                	}
                }
            }


            // update position
            for(int i =0 ; i<N; ++i){
            	balls[i][0]=balls[i][0]+balls[i][2];
            	balls[i][1]=balls[i][1]+balls[i][3];
            }
            // clear the background
            StdDraw.setPenColor(StdDraw.GRAY);
            StdDraw.filledSquare(0, 0, 1.0);

            // draw ball on the screen
            StdDraw.setPenColor(StdDraw.BLACK); 
            for(int i =0 ; i<N; ++i){
            	StdDraw.filledCircle(balls[i][0], balls[i][1], radius); 
            }
            

            // display and pause for 20 ms
            StdDraw.show(20); 
        }
	}

}
