/**
 * projecteuler.net/problem=1 : If we list all the natural numbers below 10 that are 
 * multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * 
 * Find the sum of all the multiples of 3 or 5 below 1000.
 * 
 * Answer: 233168.0
 * Submitted: 19/08/2014
 * Account: c.lorking
 */

import java.util.*;

public class eulerP1 {
    // compute sum of all multiples of 3 or 5 below 1000
    public static void main (String[] args) {
        Set<Double> nums = new HashSet<Double>();
        double total=0;
        for (double i=1; i<=999; i++) {
            // if i/3 or 1/5 has no remainder, add to set
            if (i%3 == 0 || i%5 == 0)
                nums.add(i);           
        }
        
        for (double d : nums) {
            total += d;
        }
        System.out.println("sum of all multiples of 3 and 5 below 1000 is: "+total);
    }
}
