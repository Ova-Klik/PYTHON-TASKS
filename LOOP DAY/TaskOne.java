import java.util.Scanner;


public class TaskOne{
public static void main(String [] args){

    Scanner input = new Scanner(System.in);
    
    
int sumOfNumbers = 0;
int sumOfEven = 0;
int sumOfOdd = 0;
int squareOfAllNumbers = 0;
int squareOfEven = 0;
int squareOfOdd = 0;
int sumOfSquareOdd = 0;
int sumOfSquareEven = 0;
int SumOfAllSquareNumber = 0;



    for (int num = 1; num <= 10; num ++){
        System.out.print("Enter a number: ");
        int number = input.nextInt();
        System.out.println();
        
        sumOfNumbers += number;
        squareOfAllNumbers = sumOfNumbers * sumOfNumbers;
        SumOfAllSquareNumber += squareOfAllNumbers;
        
        if (number % 2 == 0){
            System.out.printf("This is an even number %d", number);
            System.out.println();
            sumOfEven += number;
            squareOfEven = number * number;
            System.out.printf("The square of even numbers: %d",squareOfEven);
            System.out.println();
            sumOfSquareEven += squareOfEven;
        
        }
        else {
            System.out.print(number);
            System.out.println();     
            sumOfOdd += number;
            squareOfOdd = number * number;
            System.out.printf("The square of odd numbers: %d",squareOfOdd);
            System.out.println();
            sumOfSquareOdd += squareOfOdd;          
        }
    
    }
    
    System.out.printf("The total number of even numbers are: %d",sumOfEven);
    System.out.println();
    System.out.printf("The total number of odd numbers are: %d",sumOfOdd);
    System.out.println();
    System.out.printf("The total number of all the numbers: %d",sumOfNumbers);
    System.out.println();
    System.out.printf("The total number of square Of All Numbers: %d",squareOfAllNumbers);
    System.out.println();
    System.out.printf("The total sum of square Of Odd Numbers: %d",sumOfSquareOdd);
    System.out.println();
    System.out.printf("The total sum of square Of Even Numbers: %d",sumOfSquareEven);
    System.out.println();
    System.out.printf("The total sum of square Of All Numbers: %d",SumOfAllSquareNumber);
    System.out.println();



}

}

