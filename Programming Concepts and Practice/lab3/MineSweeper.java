package lab3;

import cse131.ArgsProcessor;

public class MineSweeper {

	public static void main (String[] args) {
		
		//
		// Do not change anything between here ...
		//
		ArgsProcessor ap = new ArgsProcessor(args);
		int cols = ap.nextInt("How many columns?");
		int rows = ap.nextInt("How many rows?");
		double percent = ap.nextDouble("What is the probability of a bomb?");
		//
		// ... and here
		//
		//  Your code goes below these comments
		//
		boolean [][] board = new boolean[rows][cols];
		int numBomb = (int)(rows*cols*percent/100);
		
		int[] boardPosition = new int[cols*rows];   
		for(int i=0;i<cols*rows;++i){
			boardPosition[i]=i;
		}

		for(int i=boardPosition.length-1;i>=cols*rows-numBomb;--i){
			int c = (int)(Math.random()*(i+1));    //randomly place a bomb
			board[boardPosition[c]/cols][boardPosition[c]%cols]=true;
			for(int j=c;j<boardPosition.length-1;j++){
				boardPosition[j]=boardPosition[j+1];
			}
		}


		
		//generate a M+2 by N+2 array
		boolean[][] largeBoard= new boolean[rows+2][cols+2];
		for(int i =0;i<rows;i++){
			for(int j =0;j<cols;j++){
				largeBoard[i+1][j+1]=board[i][j];
			}
		}
	
		//generate count board 
		String [][] countBoard = new String[rows][cols];
		int count=0;
		for(int i =1;i<rows+1;i++){
			for(int j =1;j<cols+1;j++){
				if(!largeBoard[i][j]==true){
					if(largeBoard[i-1][j]==true){
						count++;
					}
					if(largeBoard[i+1][j]==true){
						count++;
					}
					if(largeBoard[i][j+1]==true){
						count++;
					}
					if(largeBoard[i-1][j+1]==true){
						count++;
					}
					if(largeBoard[i+1][j+1]==true){
						count++;
					}
					if(largeBoard[i][j-1]==true){
						count++;
					}
					if(largeBoard[i+1][j-1]==true){
						count++;
					}
					if(largeBoard[i-1][j-1]==true){
						count++;
					}
					countBoard[i-1][j-1]=Integer.toString(count);
					count=0;
				}
				else{
					countBoard[i-1][j-1]="*";
				}
			}
		}
		
		//print boards
		String [][] printBoard = new String[rows][cols];
		for(int i =0;i<rows;i++){
			for(int j =0;j<cols;j++){
				if(board[i][j]==true){
					printBoard[i][j]="*";
				}
				else printBoard[i][j]=".";
			}
		}
		for(int i =0;i<rows;i++){
			for(int j =0;j<cols;j++){
				System.out.print(printBoard[i][j]+" ");
			}
			System.out.print("   ");
			for(int j =0;j<cols;j++){
				System.out.print(countBoard[i][j]+" ");
			}
			System.out.println();
		}
	}
	
}
