#include <iostream>
#include <vector>

// Function to calculate the sum of proper divisors of a number
int sumOfDivisors(int num) {
    int sum = 1; // 1 is a divisor for all numbers
    for (int i = 2; i <= num / 2; ++i) {
        if (num % i == 0) {
            sum += i;
        }
    }
    return sum;
}

// Function to find and display amicable pairs up to a given limit
void findAmicablePairs(int limit) {
    std::vector<int> amicablePairs;

    for (int i = 2; i <= limit; ++i) {
        int sum1 = sumOfDivisors(i);

        if (sum1 > i && sum1 <= limit) {
            int sum2 = sumOfDivisors(sum1);

            if (sum2 == i) {
                amicablePairs.push_back(i);
                amicablePairs.push_back(sum1);
            }
        }
    }

    // Display amicable pairs
    for (size_t i = 0; i < amicablePairs.size(); i += 2) {
        std::cout << "(" << amicablePairs[i] << ", " << amicablePairs[i + 1] << ")" << std::endl;
    }
}

int main() {
    int limit;
    std::cout << "Enter the limit to find amicable pairs up to: ";
    std::cin >> limit;

    findAmicablePairs(limit);

    return 0;
}