package lab8;

import java.util.Iterator;
import java.util.LinkedList;

public class Polynomial {

	final private LinkedList<Double> list;

	/**
	 * Constructs a Polynomial with no terms yet.
	 */
	public Polynomial() {
		//
		// Set the instance variable (list) to be a new linked list of Double type
		//
		list = new LinkedList<Double>();   // FIXME
	}

	public String toString() {
		String s="";
		if (this.list.size()!=0){
			for(int i=this.list.size()-1; i>=0;i--){
				double coeff=this.list.get(i);
				if(coeff!=0){
					if(i==this.list.size()-1) s+= coeff+"x^"+i;
					else if (i==1){
						if(coeff>0) s+=" + "+coeff+"x";
						else s+=" - "+Math.abs(coeff)+"x";
					}
					else if(i==0){
						if(coeff>0) s+=" + "+coeff;
						else s+=" - "+Math.abs(coeff);
					}
					else {
						if(coeff>0) s+=" + "+coeff+"x^"+i;
						else s+=" - "+Math.abs(coeff)+"x^"+i;
					}
				}
			}
			return s; // FIXME
		}
		else return "0";
	}

	public Polynomial addTerm(double coeff) {
		this.list.add(coeff);
		return this;  // required by lab spec
	}

	public double evaluate(double x) {
		if(this.list.size()>=2){
			Iterator<Double> iter = this.list.iterator();
			iter.next();
			double result = calc(this.list.size(),iter,x);
			result+= this.list.getFirst();
			return result;  // FIXME
		}
		else if(this.list.size()==1){
			return this.list.getFirst();
		}
		else return 0.0;
	}
	
	public static double calc(int n, Iterator<Double> iter,double x){
		double result;
		if (n==2){
			result=x*iter.next().doubleValue();
			return result;
		}
		else {
			result = x*(iter.next().doubleValue()+calc(n-1, iter, x));
			return result;
		}
	}
	
	public Polynomial derivative() {
		Polynomial poly = new Polynomial();
		for(int i=1; i<this.list.size();i++){
			poly.addTerm(this.list.get(i)*i);
		}
		return poly;   // FIXME
	}
	
	public Polynomial sum(Polynomial another) {
		Polynomial poly = new Polynomial();
		int diff= this.list.size()-another.list.size();
		if(diff>0){
			for(int i=0; i < another.list.size();i++){
				poly.list.add(this.list.get(i)+another.list.get(i));
			}
			for(int i =0; i< diff; i++){
				poly.list.add(this.list.get(i+another.list.size()));
			}
		}
		else if (diff<0){
			for(int i=0; i < this.list.size();i++){
				poly.list.add(this.list.get(i)+another.list.get(i));
			}
			for(int i =0; i< Math.abs(diff); i++){
				poly.list.add(another.list.get(i+this.list.size()));
			}
		}
		else{
			for(int i=0; i < another.list.size();i++){
				poly.list.add(this.list.get(i)+another.list.get(i));
			}
		}
		return poly;   // FIXME
	}

	/**
	 * This is the "equals" method that is called by
	 *    assertEquals(...) from your JUnit test code.
	 *    It must be prepared to compare this Polynomial
	 *    with any other kind of Object (obj).  Eclipse
	 *    automatically generated the code for this method,
	 *    after I told it to use the contained list as the basis
	 *    of equality testing.  I have annotated the code to show
	 *    what is going on.
	 */

	public boolean equals(Object obj) {
		// If the two objects are exactly the same object,
		//    we are required to return true.  The == operator
		//    tests whether they are exactly the same object.
		if (this == obj)
			return true;
		// "this" object cannot be null (or we would have
		//    experienced a null-pointer exception by now), but
		//    obj can be null.  We are required to say the two
		//    objects are not the same if obj is null.
		if (obj == null)
			return false;

		//  The two objects must be Polynomials (or better) to
		//     allow meaningful comparison.
		if (!(obj instanceof Polynomial))
			return false;

		// View the obj reference now as the Polynomial we know
		//   it to be.  This works even if obj is a BetterPolynomial.
		Polynomial other = (Polynomial) obj;

		//
		// If we get here, we have two Polynomial objects,
		//   this and other,
		//   and neither is null.  Eclipse generated code
		//   to make sure that the Polynomial's list references
		//   are non-null, but we can prove they are not null
		//   because the constructor sets them to some object.
		//   I cleaned up that code to make this read better.


		// A LinkedList object is programmed to compare itself
		//   against any other LinkedList object by checking
		//   that the elements in each list agree.

		return this.list.equals(other.list);
	}

}
