package lab9;


public class ListItem {
	//
	// Important:  Do NOT make these instance variables private
	// Our testing needs to be able to access them, so leave their
	//   declarations as you see them below.
	//
	final int number;
	ListItem next;

	/**
	 * Creates a single list item.
	 * @param number the value to be held in the item
	 * @param next a reference to the next item in the list
	 */
	ListItem(int number, ListItem next) {
		this.number = number;
		this.next   = next;
	}

	/**
	 * Return a copy of this list using recursion.  No
	 * credit if you use any iteration!  All existing lists should remain
	 * intact -- this method must not mutate anything.
	 * @return
	 */
	public ListItem duplicate() {
		if(this.next == null){
			ListItem p = new ListItem(this.number, null);
			return p;
		}
		else {
			ListItem p = new ListItem(this.number, this.next.duplicate());
			return p;
		}
		
	}

	/**
	 * Recursively compute the number of elements in the list. No
	 * credit if you use any iteration!  All existing lists should remain
	 * intact.
	 * @return
	 */
	public int length() {
		if(this.next == null){
			return 1;
		}
		else return 1 + this.next.length();
	}

	/**
	 * Return a new list, like duplicate(), but every element
	 * appears n times instead of once.  See the web page for details.
	 * You must do this method iteratively.  No credit
	 * if you use any recursion!
	 * @param n a positive (never 0) number specifying how many times to copy each element
	 * @return
	 */

	public ListItem stretch(int n) {
		ListItem x = this.duplicate();
		
		for(ListItem p = x; p != null; p = p.next){
			
			for(int i=1; i<n;i++){
				ListItem q = p.duplicate();
				p.next = q;
			}
			for(int i = 1;i<n;i++){
				p = p.next;
			}
		}
		return x;  
	}

	/**
	 * Return the first ListItem, looking from "this" forward,
	 * that contains the specified number.  No lists should be
	 * modified as a result of this call.  You may do this recursively
	 * or iteratively, as you like.
	 * @param n
	 * @return
	 */

	public ListItem find(int n) {
		for(ListItem p=this;p!=null;p=p.next){
			if(p.number==n){
				return p;
			}
		}
		return null;  
	}

	/**
	 * Return the maximum number contained in the list
	 * from this point forward.  No lists should be modified
	 * as a result of this call.  You may do this method recursively
	 * or iteratively,as you like.
	 * @return
	 */

	public int max() {
		int max = this.number;
		for(ListItem p = this.next; p != null; p = p.next){
			if(p.number > max){
				max = p.number;
			}
		}
		return max;
	}

	/**
	 * Returns a copy of the list beginning at ls, but containing
	 * only elements that are even.
	 * @param ls
	 * @return
	 */
	public static ListItem evenElements(ListItem ls) {
		
		if (ls==null) return ls;
		else{
			ListItem p= ls.duplicate();
			if(p.number%2 == 0){
				ListItem q = p.duplicate().next;
				p.next = evenElements(q);
				return  p;
			}
			else {
				p=evenElements(p.next);
				return p;
			}
		}
	}	


	/**
	 * Returns a string representation of the values reachable from
	 * this list item.  Values appear in the same order as the occur in
	 * the linked structure.  Leave this method alone so our testing will work
	 * properly.
	 */
	public String toString() {
		if (next == null)
			return ("" + number);
		else
			return (number + " " + next); // calls next.toString() implicitly
	}

}
