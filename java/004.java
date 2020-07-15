/**
 * https://projecteuler.net/problem=4
 * 
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 
 * 10 without any remainder.
 * What is the smallest positive number that is evenly divisible by all of the
 * numbers from 1 to 20?
 * 
 * Answer: 232792560
 * Submitted: 22/08/2014
 * Account: c.lorking
 */

import java.util.*;

public class eulerP5 {
    static int goal;
    static int max=20;
    static int min=1;
    static int test=((max-1)*max)-max;
    //     static int test=12252240;

    static boolean badNum = true;
    public static void main(String [] args) {
        while (badNum == true) {
            badNum = false;
            test += max;
            goal = test;
            //             System.out.println("test num = "+test);

            if (test%(max-1) == 0 && test%(max-2) == 0){
                for (int i = min; i<max-2; i++) {
                    if (test%i != 0)
                        badNum = true;
                }
            }
            else {
                badNum = true;
            }
        }
        System.out.println("Goal number = "+goal);
    }
}
