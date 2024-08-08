#include <stdio.h>

int main() {
    int i;
    int firstNumber, secondNumber;

    int firstDivisorSum = 0;
    int secondDivisorSum = 0;

    printf("Enter two numbers to check if Amicable or not : ");
    scanf("%d, %d", &firstNumber, &secondNumber);

    for(int i=0; i<firstNumber; i++){
        firstDivisorSum = firstDivisorSum + i;
        }

    for(int i=0; i<secondNumber; i++){
        secondDivisorSum = secondDivisorSum + i;
        }

    if((firstNumber == secondDivisorSum) && (secondNumber == firstDivisorSum)){
        printf("%d and %d are Amicable numbers\n", firstNumber, secondNumber);
        }
    else{
        printf("%d and %d are not Amicable numbers\n", firstNumber, secondNumber);
    };
}

#include<stdio.h>
int main(){
   int i,n1=220,n2=284,DivSum1=0,DivSum2=0;
   for(int i=1;i<n1;i++){
      if(n1 % i == 0){
         DivSum1 = DivSum1 + i;
      }
   }
   for(int i=1;i<n2;i++){
      if(n2 % i == 0){
         DivSum2= DivSum2+ i;
      }
   }
   if((n1== DivSum2) && (n2 == DivSum1)){
      printf("%d and %d are Amicable numbers\n",n1,n2);
   }else{
      printf("%d and %d are not Amicable numbers\n",n1,n2);
   }
}

int main()
{
    printf("That's all amicable pairs in range to 10000");
    int num1,num2,sum=0;
    for(num1=1; num1<=10000; num1++)
    {
        for(num2=1; num2<=10000; num2++)
            {
                if ((num1==sum_of_divisors(num2)) && (num2==sum_of_divisors(num1)) && num1!=num2)
                {
                    printf("\n%d\t\t%d", num1,num2);
                }
            }
    }
    return 0;
}

int sum_of_divisors(int n)
{
    int sum=0,i;
    for(i=1; i<n; i++)
    {
         if(n%i==0)
         {
              sum=sum+i;
         }
    }
    return sum;
}