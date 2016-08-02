package lab7;

public class Point {
	private double x,y;
	public Point (double x, double y){
		this.x=x;
		this.y=y;
	}
	public double getX() {
		return x;
	}
	public void setX(double x) {
		this.x = x;
	}
	public double getY() {
		return y;
	}
	public void setY(double y) {
		this.y = y;
	}
	
	public String toString(){
		return "("+this.x+","+this.y+")";
	}
	
	public Point plus(Vector vec){
		double x=this.x+vec.getDeltaX();
		double y=this.y+vec.getDeltaY();
		Point p = new Point(x,y);
		return p;
	}
	
	public Vector minus(Point p){
		double x=this.x-p.x;
		double y=this.y-p.y;
		Vector vec = new Vector(x,y);
		return vec;
	}
	
	public double distance(Point p){
		Vector vec=this.minus(p);
		return vec.magnitude();
	}
}
