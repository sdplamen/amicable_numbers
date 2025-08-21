# Amicable Numbers

a and b are integers where the sum of the proper divisors of a is equal to the sum of the proper divisors of b and vice versa. The proper divisors of a are the positive integers that divide into a evenly (without leaving a remainder) but exclude the number itself.

This project provides a web-based calculator to find amicable number pairs up to a specified limit. Additionally, it includes command-line implementations in Python, C, and C++.

## Features

-   **Web Interface:** A user-friendly web page to enter a number and view the amicable pairs.
-   **Efficient Calculation:** The backend uses an optimized algorithm to find amicable pairs up to the given limit.
-   **Multiple Implementations:** Includes command-line versions in Python, C, and C++ for comparison and different use cases.

### C

```bash
gcc amicable_numbers.c -o amicable_c
./amicable_c
```

### C++

```bash
g++ amicable_numbers.c++ -o amicable_cpp
./amicable_cpp
```