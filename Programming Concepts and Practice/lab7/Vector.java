package lab7;

public class Vector {
	private double deltaX,deltaY;

	public Vector(double deltaX, double deltaY) {
		this.deltaX = deltaX;
		this.deltaY = deltaY;
	}

	public double getDeltaX() {
		return deltaX;
	}

	public void setDeltaX(double deltaX) {
		this.deltaX = deltaX;
	}

	public double getDeltaY() {
		return deltaY;
	}

	public void setDeltaY(double deltaY) {
		this.deltaY = deltaY;
	}
	
	public double magnitude(){
		return Math.sqrt(this.deltaX*this.deltaX+this.deltaY*this.deltaY);
	}
	
	public Vector deflectX(){
		Vector vec= new Vector(-this.deltaX,this.deltaY);
		return vec;
	}
	
	public Vector deflectY(){
		Vector vec= new Vector(this.deltaX,-this.deltaY);
		return vec;
	}
	
	public Vector plus(Vector v){
		Vector vec= new Vector(this.deltaX+v.deltaX,this.deltaY+v.deltaY);
		return vec;
	}
	
	public Vector minus(Vector v){
		v=v.deflectX();v=v.deflectY();
		Vector vec= this.plus(v);
		return vec;
	}
	
	public Vector scale (double factor){
		Vector vec= new Vector(this.deltaX*factor,this.deltaY*factor);
		return vec;
	}
	
	public Vector rescale (double magnitude){
		double mag=this.magnitude();
		if(mag!=0){	
			double factor = magnitude/mag;
			Vector vec= new Vector(this.deltaX*factor,this.deltaY*factor);
			return vec;
		}
		else{
			Vector vec= new Vector(magnitude,0);
			return vec;
		}
	}
}
