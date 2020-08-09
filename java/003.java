/**
 * https://projecteuler.net/problem=3
 * 
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 * 
 * Status: Complete
 */

import java.util.*;

public class eulerP3 {    
    public static List<Integer> primes = new ArrayList<Integer>();
    public static boolean isPrime=true;
    public static long num = 600851475143L;
    public static int limit = 100000;
    public static int lpf = 0;

    public static void populatePrimeList(int j){
        // populates an arraylist of all prime numbers up to j
        primes.add(2);
        for (int i = 3; i <= j; i+=2){
            for (int k=2; k<i; k++) {
                if (i%k==0) {
                    isPrime=false;
                }
            }
            if (isPrime){
                primes.add(i);
            }
            isPrime = true;
        }
    }

    public static void main(String [] args) {
        populatePrimeList(limit);

        //         for (int i : primes){
        //             System.out.println(i);
        //         }
        
        for (int i = primes.size()-1; i > 0; i--){
            int j = primes.get(i);
            if (num%j==0){
                lpf = j;
                break;
            }
        }
        System.out.print("Largest prime factor = "+lpf);
    }
}
