#include <stdio.h>

int main() {
    printf("Starting the Sneklang interpreter...\n");
    return 0;
}

#include <stdio.h>

int main() {
  printf("Program in C!\n");
  return 0;
}

/* 
- A function named main is always the entry point to a C program (unlike Python, which enters at the top of the file).
- int is the return type of the function and is short for "integer". Because this is the main function, the return value is the exit code of the program. 0 means success, anything else means failure.
- You'll find a lot of abbreviations in C because 1) programmers are lazy, and 2) it used to matter how many bytes your source code was.
- The opening bracket, { is the start of the function's body (C ignores whitespace, so indentation is just for style, not for syntax)
- return 0 returns the 0 value (an integer) from the function. Again, this is the exit code because it's the main function.
- 0 represents "nothing bad happened" as a return value.
- The pesky ; at the end of return 0; is required in C to terminate statements.
- The closing bracket, } denotes the end of the function's body.
-- Print
- It feels insane coming from Python, but printing in C is done with a function called printf from the stdio.h (standard input/output) library with a lot of weird formatting rules. To use it, you need an #include at the top of your file:

#include <stdio.h>

Then you can use printf from inside a function:

printf("Hello, world!\n");

Notice the \n: it's required to print a newline character (and flush the buffer in the browser), which print() in Python does automatically.

In case you're wondering, the f in printf stands for "print formatted".
*/

/*
Basic Types
int - An integer
float - A floating point number
char - A character
char * - An array of characters (more on this later... if you think about it, sounds kinda like a string doesn't it?)
You've already seen int in the example before - it's the return value in the special main function (the entry point for every C program).
*/

#include <stdio.h>

int main() {
  int max_recursive_calls = 100;
  char io_mode = 'w';
  float throttle_speed = 0.2;

  // don't touch below this line
  printf("Max recursive calls: %d\n", max_recursive_calls);
  printf("IO mode: %c\n", io_mode);
  printf("Throttle speed: %f\n", throttle_speed);
  return 0;
}

// Strings 

/*
Most programming languages these days (even compiled ones) have a built-in string type of some sort. C... doesn't.

Instead, C strings are just arrays (like lists) of characters. We'll talk more about the specifics when we talk about arrays and pointers later, but for now know that this is how you get a "string" in C:
*/

char *msg_from_dax = "You still have 0 users";

// Very (I repeat, very) loosely speaking, char * means string. Also note that it is required to use double quotes ". Single quotes (') make char, not char *.

#include <stdio.h>

int main() {
  char *will_never_hear_again =
      "Hey TJ, when is the memory course in C gonna be done?";

  // don't touch below this line
  printf("%s\n", will_never_hear_again);
  return 0;

// Printing variables

// We have to tell C how we want particular values to be printed using "format specifiers".

/*
Common format specifiers are:

%d - digit (integer)
%c - character
%f - floating point number
%s - string (char *)
*/

char *name = "Preston Rivera";
int age = 28;
printf("Hello, %s. You're %d years old.\n", name, age);

#include <stdio.h>

int main() {
  int sneklang_default_max_threads = 8;
  char sneklang_default_perms = 'r';
  float sneklang_default_pi = 3.14159;
  char *sneklang_title = "Sneklang";
  // don't touch above this line

  printf("Default max threads: %d\nCustom perms: %c\nConstant pi value: %f\nSneklang title: %s\n", 
    sneklang_default_max_threads, sneklang_default_perms, sneklang_default_pi, sneklang_title);

  return 0;
}

// OR 

#include <stdio.h>

int main() {
  int sneklang_default_max_threads = 8;
  char sneklang_default_perms = 'r';
  float sneklang_default_pi = 3.14159;
  char *sneklang_title = "Sneklang";
  // don't touch above this line

  printf("Default max threads: %d\n", sneklang_default_max_threads);
  printf("Custom perms: %c\n", sneklang_default_perms);
  printf("Constant pi value: %f\n", sneklang_default_pi);
  printf("Sneklang title: %s\n", sneklang_title);
  return 0;
}


// Compilation: Types
// You're probably familiar with the idea of types from Python, but C does them quite a bit differently.

// In Python, it's OK (but still disgusting) to change the type of a variable:

x = 12345
x = "wow, a new type"
x = False
x = None
x = "ok a string again :'("

// In C, changing the type of an existing variable is not allowed:

int main() {
    char *max_threads = "5";

    // call badcop
    // this is illegal
    max_threads = 5;
}

// Variables
// As we talked about, variables cannot change types:

int main() {
    int x = 5;
    float x = 3.14; // error
}

// However, a variable's value can change:

int main() {
    int x = 5;
    x = 10; // this is ok
    x = 15; // still ok
}

// When updating a variable's value, you don't need to redeclare the type. In fact, you can't. Fix the code so that it updates (64 -> 32) properly.

#include <stdio.h>

int main() {
  int sneklang_int_size = 64;
  sneklang_int_size = 32;
  printf("Sneklang int size: %d bits\n", sneklang_int_size);
  return 0;
}

// Constants
// So a variable's value can change:

int main() {
    int x = 5;
    x = 10; // this is ok
}

// But what if we want to create a value that can't change? We can use the const type qualifier.

int main() {
    const int x = 5;
    x = 10; // error
}

// Functions
// In C, functions specify the types for their arguments and return value.

float add(int x, int y) {
    return (float)(x + y);
}

/*
The first type, float is the return type.
add is the name of the function.
int x, int y are the arguments to the function, and their types are specified.
x + y adds the two arguments together.
(float) casts the result to a float.
    We'll talk more about what cast means later, and the rules for casting to and from certain types.
    The simple version is that it instructs C to treat the result of x + y as a float.
*/

// Here's how you would call this function:

int main() {
    float result = add(10, 5);
    printf("result: %.f\n", result);
    // result: 15.000000
    return 0;
}

// It's nice that C functions enforce returning the same type from all return statements, isn't it? In Python, it can be a pain to realize that a function returns different types depending on the path it took.

#include <stdio.h>

int max_sneklang_memory(int max_threads, int memory_per_thread) {
  return (int)(max_threads * memory_per_thread);
}

// don't touch below this line

void init_sneklang(int max_threads, int memory_per_thread) {
  printf("Initializing Sneklang\n");
  printf("Max threads: %d\n", max_threads);
  printf("Memory per thread: %d\n", memory_per_thread);
  int max_memory = max_sneklang_memory(max_threads, memory_per_thread);
  printf("Max memory: %d\n", max_memory);
  printf("====================================\n");
}

int main() {
  init_sneklang(4, 512);
  init_sneklang(8, 1024);
  init_sneklang(16, 2048);
  return 0;
}

// Void
// In C, there's a special type for function signatures: void. There are two primary ways you'll use void:

// To explicitly state that a function takes no arguments:

int get_integer(void) {
    return 42;
}

// When a function doesn't return anything:

void print_integer(int x) {
    printf("this is an int: %d", x);
}

// It's important to note that void in C is not like None in Python. It's not a value that can be assigned to a variable. It's just a way to say that a function doesn't return anything or doesn't take any arguments.

// Assignment to get the average with the reseult being a float. 

// TIPS
/*
The + operator adds two numbers: 1 + 2 is 3.
The / operator divides two numbers, however:
if both numbers are integers, integer division is performed. The result will be an integer.
if either number is a float, floating point division is performed. The result will be a float.
*/

float get_average(int x, int y, int z) {
  return ((x + y + z) / (float)3);
}

// Math Operators
// All the same operators you'd expect exist in C:

// x + y;
// x - y;
// x * y;
// x / y;

// If you're coming from Python, +=, -=, *=, /= are all the same.

// In addition, there are also the ++ and -- operators:

// x++; // += 1
// x--; // -= 1

/*
The name of C++ is a bit of a joke by the creator, it's meant to be "incremented C" or "better C".

These increment (++) and decrement (--) operators can be used in two forms: postfix and prefix.

Postfix (x++ or x--): The value of x is used in the expression first, and then x is incremented or decremented. For example:
*/

// int a = 5;
// int b = a++; // b is assigned 5, then a becomes 6

// Prefix (++x or --x): x is incremented or decremented first, and then the new value of x is used in the expression. For example:

// int a = 5;
// int b = ++a; // a becomes 6, then b is assigned 6

// I generally avoid prefix operators. If I want to increment a variable but keep the original value, I do that in two steps. Postfix is more common, especially in loops, which we'll get to.


float snek_score(
  int num_files,
  int num_contributors,
  int num_commits,
  float avg_bug_criticality
) {
  int size_factor = num_files * num_commits;
  int complex_factor = num_contributors + size_factor;
  float final_score = (float)complex_factor * avg_bug_criticality; // You can convert an integer to a float by casting it
  return (float)final_score;
}


// If statements

if (x > 3) {
    printf("x is greater than 3\n");
}

// If/else/else if are also available:

if (x > 3) {
    printf("x is greater than 3\n");
} else if (x == 3) {
    printf("x is 3\n");
} else {
    printf("x is less than 3\n");
}

// #include "exercise.h"

char *get_temperature_status(int temp) {
  if (temp < 70) {
    return ("too cold");
  } else if (temp > 90) {
    return ("too hot");
  } else {
    return ("just right");
  }
}

// Ternary
// Like JavaScript, C has a ternary operator:
/*
int a = 5;
int b = 10;
int max = a > b ? a : b;
printf("max: %d\n", max);
*/
// max: 10
// Let's break down the syntax:

a > b ? a : b
// The entire line is a single expression that evaluates to one value. Here's how it works:

/*
a > b is the condition
a is the final value if the condition is true
b is the final value if the condition is false
The entire expression (a > b ? a : b) evaluates to either a or b, which is then assigned to max in our example.
Ternaries are a way to write a simple if/else statement in one line.
*/

/*
Type Sizes
In C, the "size" (in memory) of a type is not guaranteed to be the same on all systems. That's because the size of a type is dependent on the system's architecture. 
For example, on a 32-bit system, the size of an int is usually 4 bytes, while on a 64-bit system, the size of an int is usually 8 bytes - of course, you never know until you run sizeof with the compiler you plan on using.

However, some types are always guaranteed to be the same. Here’s a list of the basic C data types along with their typical sizes in bytes. Note that sizes can vary based on the platform (e.g., 32-bit vs. 64-bit systems):

Basic C Types and Sizes:
char

Size: 1 byte
Represents: Single character.
Notes: Always 1 byte, but can be signed or unsigned.
float

Size: 4 bytes
Represents: Single-precision floating-point number.
double

Size: 8 bytes
Represents: Double-precision floating-point number.
The actual sizes of these types can be determined using the sizeof operator in C for a specific platform, which we'll learn about next.
*/

/*
Sizeof
C gives us a way to check the size of a type or a variable: sizeof.

You can use sizeof like a function (although, technically it's a unary operator, but that distinction is generally only useful for winning super important internet arguments).

We'll use the sizeof operator in the next few lessons to give us insight into the memory layout of different types in C. This will be particularly useful as we move deeper into C, and essential for understanding pointers.

Pointers are not too bad once you understand the basics! I promise!

size_t
The size_t type is a special type that is guaranteed to be able to represent the size of the largest possible object in the target platform's address space (i.e. can fit any single, non-struct value inside of it).

It's also the type that sizeof returns.
*/


#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

int main() {
  // Use %zu is for printing `sizeof` result
  printf("sizeof(char)   = %zu\n", sizeof(char));
  printf("sizeof(bool)   = %zu\n", sizeof(bool));
  printf("sizeof(int)    = %zu\n", sizeof(int));
  printf("sizeof(float)  = %zu\n", sizeof(float));
  printf("sizeof(double) = %zu\n", sizeof(double));
  printf("sizeof(size_t) = %zu\n", sizeof(size_t));
}

// FOR LOOP

// A for loop in C is a control flow statement for repeated execution of a block of code. Very similar to Python, but with a different syntax.

/*
The syntax of a for loop in C consists of three main parts:

Initialization
Condition
Final-expression.
*/

// Instead, we have to iterate over the numbers of indices in a list, and then we can access the item using the index.

// Syntax
for (initialization; condition; final-expression) {
    // Loop Body
}

/*
Parts of a for Loop
  Initialization
    -Executed only once at the beginning of the loop.
    -Is typically used to initialize the loop counter: int i = 0; for example
  Condition
    -Checked before each iteration.
    -If true, execute the body. If false, terminate the loop
    -Often checks to ensure i is less than some value: i < 5; for example
  Final-expression
    -Executed after each iteration of the loop body.
    -Can be used to update the loop counter or run any other code: i++ for example
  Loop Body
    -The block of code that is executed while the condition is true.
*/

// BASIC FOR LOOP

#include <stdio.h>

int main() {
  for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
  }
  return 0;
}

// Prints:
// 0
// 1
// 2
// 3
// 4

// For loop used to print all the numbers from start to end inclusive
#include <stdio.h>

void print_numbers(int start, int end) {
  for (int i = start; i <= end; i++) {
    printf("%d\n", i);
  }
}

// While Loop
// A while loop in C is a control flow statement that allows code to be executed repeatedly based on a given boolean (true/false) condition. The loop continues to execute as long as the condition remains true.
/*
Syntax
while (condition) {
    // Loop Body
}
*/ 

/*
Parts of a while Loop
Condition
Checked before each iteration.
If true, execute the body. If false, terminate the loop
Loop Body
The block of code that is executed while condition is true.
*/

// Example: Basic Loop
#include <stdio.h>

int main() {
    int i = 0;
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
// Prints:
// 0
// 1
// 2
// 3
// 4

/*
Key Points
The condition is evaluated before the execution of the loop body.
If the condition is false initially, the loop body will never even start.
If the condition never becomes false, you will get an infinite loop.
*/

// Using a while loop to count down from 20 to 4. Start = 20, end = 4

#include <stdio.h>

void print_numbers_reverse(int start, int end) {
  while(start >= end) {
    printf("%d\n", start);
    start--;
  }
}

// Do While Loop
// A do while loop in C is a control flow statement that allows code to be executed repeatedly based on a given boolean condition.

// Unlike the while loop, the do while loop checks the condition after executing the loop body, so the loop body is always executed at least once.

// Syntax
do {
    // Loop Body
} while (condition);

/*
Parts of a do while Loop
Loop Body
The block of code that is executed before checking the condition, and then repeatedly as long as the condition is true.
Condition:
Checked after each iteration.
If true, execute the body again. If false, terminate the loop
*/

// Examples
#include <stdio.h>

int main() {
    int i = 0;
    do {
        printf("i = %d\n", i);
        i++;
    } while (i < 5);
    return 0;
}
// Prints:
// 0
// 1
// 2
// 3
// 4

#include <stdio.h>

int main() {
    int i = 100;
    do {
        printf("i = %d\n", i);
        i++;
    } while (i < 5);
    return 0;
}
// Prints:
// i = 100

/*
Key Points
The do while loop guarantees that the loop body is executed at least once, even if the condition is false initially.

The most common scenario you will see a do-while loop used is in C macros - they let you define a block of code and execute it exactly once in a way that is safe across different compilers, 
and ensures that the variables created/referenced within the macro do not leak to the surrounding environment.

If you end up looking at any source code for macros, you will probably see a few do-while loops. For example, here's a simplified version from our munit testing library we're using:
*/

#define munit_assert_type_full(T, fmt, a, op, b, msg)                          \
  do {                                                                         \
    T munit_tmp_a_ = (a);                                                      \
    T munit_tmp_b_ = (b);                                                      \
    if (!(munit_tmp_a_ op munit_tmp_b_)) {                                     \
      munit_errorf("assertion failed: %s %s %s (" prefix "%" fmt suffix        \
                   " %s " "%" fmt "): %s",                                     \
                   #a, #op, #b, munit_tmp_a_, #op, munit_tmp_b_, msg);         \
    }                                                                          \
  } while (0)

//It creates a do-while loop, creates a few new variables and then checks that the assertion is valid. If it is not, then it errors and formats a (complicated) error message 
// (If this code doesn't make any sense, that's fine too! I just wanted to show you where they most often occur).

// Note: there is no semi-colon after the while(0). This lets the macro be used in a block of code without causing syntax errors.

// Run the code. Notice that it prints 5 -> 1. However, it doesn't print anything from 1 -> 5 because the condition of the while loop is never true. 
// Change print_numbers_reverse to use a do-while loop so that it always at least prints the starting number.

#include <stdio.h>

void print_numbers_reverse(int start, int end) {
  do {
    printf("%d\n",start);
    start--;
  } while (start >= end);
}


// Pragma Once and Header Guards
// We saw how .h header files are used in a previous lesson, but before we go further let's talk about a potential issue you might run into: multiple inclusions. If the same header file gets included more than once, 
// you can end up with some nasty errors caused by redefining things like functions or structs.

// Pragma once
// One simple solution (and the one we'll use for the rest of this course) is #pragma once. Adding this line to the top of a header file tells the compiler to include the file only once, even if it's referenced multiple times across your program.

// The my_header.h is actually included in the code for refernece! 
// EXAMPLE:

// my_header.h

#pragma once

struct Point {
    int x;
    int y;
};

// Header Guards
// Another common way to avoid multiple inclusions is with include guards, which use preprocessor directives like this:

#ifndef MY_HEADER_H
#define MY_HEADER_H

// some cool code

#endif

// This method works by defining a unique macro for the header file. If it’s already been included, the guard prevents it from being processed again.

// Throughout this course, you’ll see #pragma once in our header files. It's quicker and less error-prone than traditional include guards, and it works well with most modern compilers.


// STRUCTS

// Syntax

struct Human {
    int age;
    char *name;
    int is_alive;
};

// Assignment creating a struct in a .h header file

#pragma once

struct Coordinate {
  int x;
  int y;
  int z;
};

// Initializers
// So now you're probably wondering: "Hey TJ, so... how do we actually make an instance of a struct"? You may have noticed in the previous lesson all we did was define the struct type.

// Unfortunately, there are a few different ways to initialize a struct, I'll give you an example of each using this struct:

struct City {
  char *name;
  int lat;
  int lon;
};

// Zero Initializer
int main() {
  struct City c = {0};
}

// This sets all the fields to 0 values.

// Positional Initializer
int main() {
  struct City c = {"San Francisco", 37, -122};
}

// Designated Initializer
// This is my (generally) preferred way to initialize a struct. Why?

// It's easier to read (has the field names)
// If the fields change, you don't have to worry about breaking the ordering
int main() {
  struct City c = {
    .name = "San Francisco",
    .lat = 37,
    .lon = -122
  };
}

// Remember, it's .name not name. If this trips you up, just remember it's .name and not name because that's how you access the field, e.g. c.name.

// Accessing Fields
// Accessing a field in a struct is done using the . operator. For example:

struct City c;
c.lat = 41; // Set the latitude
printf("Latitude: %d", c.lat); // Print the latitude

// Assignment
// Struct would be created in the coord.h file then we create a instance of that struct in the function new_coord
//#include "coord.h"

struct Coordinate new_coord(int x, int y, int z) {
  struct Coordinate coord = {
    .x = x,
    .y = y,
    .z = z
  };
  return coord;
}

// #include "coord.h" the // isnt needed in actual code

struct Coordinate new_coord(int x, int y, int z) {
  struct Coordinate coord = {.x = x, .y = y, .z = z};
  return coord;
}

struct Coordinate scale_coordinate(struct Coordinate coord, int factor) {
  struct Coordinate new_coord = {.x = coord.x, .y = coord.y, .z = coord.z};
  new_coord.x *= factor;
  new_coord.y *= factor;
  new_coord.z *= factor;
  return new_coord;
}

// Typedef

// By now, you're probably tired of typing struct Coordinate over and over again, and you're wondering "How can I make my struct types easier to write, like int?"

// Good news! C can do this with the typedef keyword.

struct Pastry {
    char *name;
    float weight;
};

// This can also be written as:

typedef struct Pastry {
    char *name;
    float weight;
} pastry_t;

// Now, you can use pastry_t wherever before you would have used struct Pastry. Note: The _t at the end is a common convention to indicate a type.

// In fact, you can optionally skip giving the struct a name:

typedef struct {
    char *name;
    float weight;
} pastry_t;

// In this case you'd only be able to refer to the type as pastry_t. In general, I do give the struct an actual name (e.g. Pastry), but I only use the typedef'd type. We'll be using this convention in this course.

/*
// coord.h file contents
#pragma once

typedef struct Coordinate {
  int x;
  int y;
  int z;
}coordinate_t;

struct Coordinate new_coord(int x, int y, int z);
struct Coordinate scale_coordinate(struct Coordinate coord, int factor);



// coord.c file contents
#include "coord.h"

coordinate_t new_coord(int x, int y, int z) {
  struct Coordinate coord = {.x = x, .y = y, .z = z};

  return coord;
}

coordinate_t scale_coordinate(struct Coordinate coord, int factor) {
  struct Coordinate scaled = coord;
  scaled.x *= factor;
  scaled.y *= factor;
  scaled.z *= factor;

  return scaled;
}
*/

