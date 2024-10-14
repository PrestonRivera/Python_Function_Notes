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

%d or %i: int (integer)
%f: float
%lf: double (long float)
%c: char (single character)
%s: string (array of characters)
%u: unsigned int
%ld: long int
%lu: unsigned long int
%lld: long long int
%llu: unsigned long long int
%x or %X: hexadecimal (lowercase or uppercase)
%o: octal
%p: pointer address

Remember, you can also use modifiers with these specifiers. For example:

.2f will display a float with 2 decimal places
%5d will right-align an integer in a field width of 5 characters
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

/*
Struct Padding
There are a bunch of complicated rules and heuristics that different compilers use to determine how to lay out your structs. But to oversimplify:

The fields of a struct are laid out in memory contiguously (next to each other)
Structs can vary in size depending on how they are laid out.
C is a language that aims to give tight control over memory, so the fact that you can control the layout of your structs is a feature, not a bug.

Compilers + modern hardware + optimizations + skill issues means that sometimes what you think the computer is going to do isn't exactly what it actually does. That said, C is designed to get you close to the machine and allows you to dig in and figure out what's going on if you want to for a specific compiler or architecture.

As a rule of thumb, ordering your fields from largest to smallest will help the compiler minimize padding:
*/

typedef struct {
  char a;
  double b;
  char c;
  char d;
  long e;
  char f;
} poorly_aligned_t;

typedef struct {
  double b;
  long e;
  char a;
  char c;
  char d;
  char f;
} better_t;


/*
Memory
Before we talk about pointers, we should talk about variables and memory in general. Here are some useful (albeit hand-wavy) mental models:

Variables are human readable names that refer to some data in memory.

Memory is a big array of bytes, and data is stored in the array.

A variable is a human readable name that refers to an address in memory, which is an index into the big array of bytes.
*/

/*
Getting a Variable's Address
In C, you can print the address of a variable by using the address-of-operator: &. Here's an example:
*/
#include <stdio.h>

int main() {
  int age = 37;
  printf("The address of age is: %p\n", &age);
  return 0;
}
/*
// The address of age is: 0xfff8
 
Note: The %p format specifier will format a pointer (memory address) to be printed.
*/

// #include "snek.h"

unsigned long size_of_addr(long long i){
  unsigned long sizeof_snek_version = sizeof(&i);
  return sizeof_snek_version;
}

/*
Pointers
You've probably heard of pointers. You may have also seen jokes about how they are impossible to learn... Well, that's wrong.

In fact, now that you understand how memory is laid out in an array, a lot of the mystery behind pointers should be gone. Put simply: a pointer is just a variable that stores a memory address. It's called a pointer, because it "points" to the address of a variable, which stores the actual data held in that variable.

Syntax
A pointer is declared with an asterisk (*) after the type. For example, int *.
*/

int age = 37;
int *pointer_to_age = &age;

// Remember, to get the address of a variable so that we can store it in a pointer variable, we can use the address-of operator (&).

// coordinate.h
typedef struct coordinate {
  int x;
  int y;
  int z;
} coordinate_t;

void coordinate_update_x(coordinate_t coor, int new_x);
coordinate_t coordinate_update_and_return_x(coordinate_t coor, int new_x);

// coordinate.c
#include "coordinate.h"

void coordinate_update_x(coordinate_t coor, int new_x) {
  coor.x = new_x;
}

coordinate_t coordinate_update_and_return_x(coordinate_t coor, int new_x) {
  coor.x = new_x;
  return coor;
}

// Pointer Basics
// Remember, pointers are just an address (read: value) that tells the computer where to look for other values. Just like how the address to your house is not actually your house, but points you to where your house is.

// Syntax Review
// Declare a pointer to an integer:

int *pointer_to_something; // declares pointer as a pointer to an int

// Get the address of a variable:

int meaning_of_life = 42;
int *pointer_to_mol = &meaning_of_life;

// pointer_to_mol now holds the address of meaning_of_life

// New: Dereferencing Pointers
// Oftentimes we have a pointer, but we want to get access to the data that it points to. Not the address itself, but the value stored at that address.

// We can use an asterisk (*) to do it. The * operator dereferences a pointer.

int meaning_of_life = 42;
int *pointer_to_mol = &meaning_of_life;
int value_at_pointer = *pointer_to_mol;
// value_at_pointer = 42

// It can be a touch confusing, but remember that the asterisk symbol is used for two different things:

// Declaring a pointer type: int *pointer_to_thing;
// Dereferencing a pointer value: *pointer_to_thing = 20;

// excercise.c
#include "exercise.h"

codefile_t change_filetype(codefile_t *f, int new_filetype){
  codefile_t new_f = *f;
  new_f.filetype = new_filetype;
  return new_f;
}

// excercise.h
typedef struct CodeFile {
  int lines;
  int filetype;
} codefile_t;

codefile_t change_filetype(codefile_t *f, int new_filetype);


/*
Pointers to Structs
As you know, when you have a struct, you can access the fields with the dot (.) operator:
*/ 
coordinate_t point = {10, 20, 30};
printf("X: %d\n", point.x);

// However, when you're working with a pointer to a struct, you need to use the arrow (->) operator:

coordinate_t point = {10, 20, 30};
coordinate_t *ptrToPoint = &point;
printf("X: %d\n", ptrToPoint->x);

// It effectively dereferences the pointer and accesses the field in one step. To be fair, you can also use the dereference and dot operator (* and .) to achieve the same result (it's just more verbose and less common):

coordinate_t point = {10, 20, 30};
coordinate_t *ptrToPoint = &point;
printf("X: %d\n", (*ptrToPoint).x);
/*
Order of Operations
The . operator has a higher precedence than the * operator, so parentheses are necessary when using * to dereference a pointer before accessing a member... which is another reason why the arrow operator is so much more common.
*/

// C Arrays
/*
If you're used to Lists in Python, Arrays in C are similar, but a bit lower level.

An array is a fixed-size, ordered collection of elements. Like Python lists, they are indexed by integers, starting at zero. Unlike Python lists, they can only hold elements of the same type. They are stored in contiguous memory, like structs.
*/

// Integer Array
int numbers[5] = {1, 2, 3, 4, 5};
/*
Iterating Over an Array
In C, there is no for x in list: syntax. Instead, you must iterate over them using a for loop with an index (or some other conditional loop)
*/
#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};

    // Iterate and print each element
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}

// Output:

// 1 2 3 4 5

/*
Updating Values in an Array
The syntax for updating values in an array is the same as how you access them:

arr[index] = value
*/

// Using our numbers example:

#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};

    // Update some values
    numbers[1] = 20;
    numbers[3] = 40;

    // Print updated array
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}

// Output:

// 1 20 3 40 5

// Assignment updating array values:

#include "exercise.h"

void update_file(int filedata[200], int new_filetype, int new_num_lines){
  filedata[1] = new_num_lines;
  filedata[2] = new_filetype;
  filedata[199] = 0;
}

// Arrays as Pointers in C

// In C, arrays and pointers are closely related. An array name acts as a pointer to the first element of the array. That means array indexing and pointer arithmetic can be used interchangeably to access array elements. 

// Let's go through this step-by-step to understand how this works.

// Step-by-Step Walkthrough

// Array Declaration:
int numbers[5] = {1, 2, 3, 4, 5};

// Here, numbers is an array of 5 integers.

// Array as Pointer:
// The name numbers acts as a pointer to the first element of the array.

int *numbers_ptr = numbers;

// numbers_ptr is a pointer to the same place as numbers.

// Accessing Elements via Indexing:
// Access the third element (index 2)
int value = numbers[2];

// Which is the same as:

int value = *(numbers + 2);

// Here, numbers + 2 computes the address of the third element, and * dereferences it to get the value.

// Pointer Arithmetic:
// When you add an integer to a pointer, the resulting pointer is offset by that integer times the size of the data type.

int *p = numbers + 2;  // p points to the third element
int value = *p;        // value is 3

// Diagram Explanation
// Let's assume numbers is stored starting at memory address 0x1000. An integer is typically 4 bytes in C. Here's how the array elements are laid out in memory:

/*
Address	Element	Value
0x1000	numbers[0]	1
0x1004	numbers[1]	2
0x1008	numbers[2]	3
0x100C	numbers[3]	4
0x1010	numbers[4]	5
*/

// Accessing Elements Using Pointers
/*
numbers + 0 or &numbers[0] points to 0x1000
numbers + 1 or &numbers[1] points to 0x1004
numbers + 2 or &numbers[2] points to 0x1008
numbers + 3 or &numbers[3] points to 0x100C
numbers + 4 or &numbers[4] points to 0x1010
*/

// Example Code
#include <stdio.h>

int main() {
  int numbers[5] = {1, 2, 3, 4, 5};

  // Accessing elements using array indexing
  printf("numbers[2] = %d\n", numbers[2]);  // Output: 3

  // Accessing elements using pointers
  printf("*(numbers + 2) = %d\n", *(numbers + 2));  // Output: 3

  // Pointer arithmetic
  int *ptr = numbers;
  printf("Pointer ptr points to numbers[0]: %d\n", *ptr);  // Output: 1
  ptr += 2;
  printf("Pointer ptr points to numbers[2]: %d\n", *ptr);  // Output: 3

  return 0;
}

// Multibyte Arrays
// If we create an array of structs it gets crazy because we can access and manipulate the elements using either indexing or pointer arithmetic. Let's see how multi-byte width structures are managed in memory.

// First, let's say we're working with our familiar Coordinate struct:

typedef struct Coordinate {
  int x;
  int y;
  int z;
} coordinate_t;

// We can declare an array of 3 Coordinate structs like so:

coordinate_t points[3] = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
};

// Then we can print out the values of the second element in the array:

printf("points[1].x = %d, points[1].y = %d, points[1].z = %d\n",
  points[1].x, points[1].y, points[1].z
);
// 4, 5, 6

// Or we can use a pointer:

coordinate_t *ptr = points;
printf("ptr[1].x = %d, ptr[1].y = %d, ptr[1].z = %d\n",
  (ptr + 1)->x, (ptr + 1)->y, (ptr + 1)->z
);
// 4, 5, 6

// Memory Layout
// Assuming each int is 4 bytes, the Coordinate structure will be 12 bytes (3 * 4 bytes). Let's assume the points array starts at memory address 0x2000.

// Here is the memory layout:
/*
Address	Element	Value	Offset (bytes)
0x2000	points[0].x	1	0
0x2004	points[0].y	2	4
0x2008	points[0].z	3	8
0x200C	points[1].x	4	12
0x2010	points[1].y	5	16
0x2014	points[1].z	6	20
0x2018	points[2].x	7	24
0x201C	points[2].y	8	28
0x2020	points[2].z	9	32
*/

// Accessing Elements Using Pointers
// points + 0 or &points[0] points to 0x2000
// points + 1 or &points[1] points to 0x200C (next structure, offset by 12 bytes)
// points + 2 or &points[2] points to 0x2018

// Array Casting
// Let's explore a special kind of psychopathy that's possible in C. Let's assume we have this array of 3 structs where each struct holds 3 integers:

coordinate_t points[3] = {
  {5, 4, 1},
  {7, 3, 2},
  {9, 6, 8}
};

// Because arrays are basically just pointers (in most cases; more on that later), and we know that structs are contiguous in memory, we can cast the array of structs to an array of integers:

int *points_start = (int *)points;

// Then we can iterate over the known number of integers in the array of structs:

for (int i = 0; i < 9; i++) {
  printf("points_start[%d] = %d\n", i, points_start[i]);
}

/*
points_start[0] = 5
points_start[1] = 4
points_start[2] = 1
points_start[3] = 7
points_start[4] = 3
points_start[5] = 2
points_start[6] = 9
points_start[7] = 6
points_start[8] = 8
*/

// excercise.h
typedef struct Graphics {
  int fps;
  int height;
  int width;
} graphics_t;

void dump_graphics(graphics_t gsettings[10]);

// ecxercise.c # the // before include statements get removed in actual code files
//#include <stdio.h>
//#include "exercise.h"

void dump_graphics(graphics_t gsettings[10]) {
  int *ptr = (int *)gsettings;
  for (int i = 0; i < 30; i++) {
    printf("settings[%d] = %d\n", i, ptr[i]);
  }
}

//Pointer Size
/*
The size of an array depends on both the number of elements and the size of each element. An array is a contiguous block of memory where each element has a specific type, and therefore, a specific size.

In C, pointers are always the same size because they just represent memory addresses. The size of a pointer is determined by the architecture of the system (e.g., 32-bit or 64-bit). 
A pointer's size doesn't depend on the type of data it points to; it just holds the address of a memory location.
*/

// Pointer Example
int *intPtr;
char *charPtr;
double *doublePtr;
printf("Size of int pointer: %zu bytes\n", sizeof(intPtr));
printf("Size of char pointer: %zu bytes\n", sizeof(charPtr));
printf("Size of double pointer: %zu bytes\n", sizeof(doublePtr));
// Size of int pointer: 4 bytes
// Size of char pointer: 4 bytes
// Size of double pointer: 4 bytes

// They're all the same size, because they're all just 32-bit memory addresses: it doesn't matter how much memory the value at that address takes up.

// Array Example
int intArray[10];
char charArray[10];
double doubleArray[10];
printf("Size of int array: %zu bytes\n", sizeof(intArray));
printf("Size of char array: %zu bytes\n", sizeof(charArray));
printf("Size of double array: %zu bytes\n", sizeof(doubleArray));
// Size of int array: 40 bytes
// Size of char array: 10 bytes
// Size of double array: 80 bytes

/*
Now the sizes are different because the array type keeps track of the size of each element and the number of elements. 
Although an array is a pointer to the first element, it's not just a pointer: it's a block of memory that holds all the elements.
*/

// Arrays Decay to Pointers

/*
So we know that arrays are like pointers, but they're not exactly the same. Arrays allocate memory for all their elements, whereas pointers just hold the address of a memory location. In many contexts, 
arrays decay to pointers, meaning the array name becomes "just" a pointer to the first element of the array.
*/

// When arrays decay
// Arrays decay when used in expressions containing pointers:

int arr[5];
int *ptr = arr;          // 'arr' decays to 'int*'
int value = *(arr + 2);  // 'arr' decays to 'int*'

/*
And also when they're passed to functions... so they actually decay quite often in practice. That's why you can't pass an array to a function by value like you do with a struct; instead, the array name decays to a pointer.

When arrays don't decay
sizeof Operator: Returns the size of the entire array (e.g., sizeof(arr)), not just the size of a pointer.
& Operator Taking the address of an array with &arr gives you a pointer to the whole array, not just the first element. The type of &arr is a pointer to the array type, e.g., int (*)[5] for an int array with 5 elements.
Initialization: When an array is declared and initialized, it is fully allocated in memory and does not decay to a pointer.
*/

#include <stdio.h>

void core_utils_func(int core_utilization[]) {
  printf("sizeof core_utilization in core_utils_func: %zu\n", sizeof(core_utilization));
}

// don't touch below this line

int main() {
  int core_utilization[] = {43, 67, 89, 92, 71, 43, 56, 12};
  int len = sizeof(core_utilization) / sizeof(core_utilization[0]);
  printf("sizeof core_utilization in main: %zu\n", sizeof(core_utilization));
  printf("len of core_utilization: %d\n", len);
  core_utils_func(core_utilization);
  return 0;
}

// Results showing that when an array is passed to a function it decays to a pointer 

/*
sizeof core_utilization in main: 32
len of core_utilization: 8
sizeof core_utilization in core_utils_func: 4
*/

// C Strings

// Since the beginning of the course we've been doing these shenanigans to be able to print strings:

char *msg = "ssh terminal.shop for the best coffee";

// I told you not to worry about the weird char * syntax, but now that we understand a bit about pointers, let's dive into it. In the example above, 
// msg is a pointer to the first character of the string "ssh terminal.shop for the best coffee", which is a C string. C strings are:

/*
How we represent text in C programs
Any number of characters (chars) terminated by a null character ('\0').
A pointer to the first element of a character array.
It's important to understand that most string manipulation in C is done using pointers to move around the array and the null terminator is critical for determining the end of the string. In the example above, the string "ssh terminal.shop for the best coffee" is stored in memory as an array of characters, and the null terminator '\0' is automatically added at the end.

C Strings are Simple
Unlike other programming languages, C strings do not store their length.
The length of a C string is determined by the position of the null terminator ('\0').
Functions like strlen calculate the length of a string by iterating through the characters until the null terminator is encountered.
This lack of length storage requires careful management to avoid issues such as buffer overflows and off-by-one errors during string operations.
Pointers vs Arrays
You can declare strings in C using either arrays or pointers:
*/
char str1[] = "Hi";
char *str2 = "Snek";
printf("%s %s\n", str1, str2);
// Output: Hi Snek

// The output is the same. Let's break down the memory of this example:

// notice we aren't using all 50 characters
char first[50] = "Snek";
char *second = "lang!";
strcat(first, second);
printf("Hello, %s\n", first);
// Output: Hello, Sneklang!

// The strcat function appends its second argument to the first argument. In this case, it appends "lang!" to "Snek", resulting in the output Hello, Sneklang!.

// Here's what first might look like in memory:

/*
'S'	'n'	'e'	'k'	'\0'	????	...	????
0x3000	0x3001	0x3002	0x3003	0x3004	0x3005	...	0x3050
NOTE! There is a bunch of garbage memory after the end of the string.

Here's what second might look like in memory:

'l'	'a'	'n'	'g'	'!'	'\0'
0x4000	0x4001	0x4002	0x4003	0x4004	0x4005
And first after strcat:

'S'	'n'	'e'	'k'	'l'	'a'	'n'	'g'	'\0'	????	...	????
0x3000	0x3001	0x3002	0x3003	0x3004	0x3005	0x3006	0x3007	0x3008	0x3009	...	0x3050
The strcat function appends the string "lang!" to the end of the string "Snek", but smartly
*/

// excercise.h
void concat_strings(char *str1, const char *str2);

// excercise.c
#include "exercise.h"

void concat_strings(char *str1, const char *str2) {
  char *end = str1;
  while (*end != '\0') {
    *end++;
  }
  while (*str2 != '\0') {
    *end = *str2;
    *end++;
    *str2++;
  }
  *end = '\0';
}

// visualize it 
/*
Before:
str1 -> "Hello\0"
               ^
str2 -> "World\0"
         ^

After first iteration:
str1 -> "HelloW\0"
                ^
str2 -> "World\0"
          ^

After second iteration:
str1 -> "HelloWo\0"
                 ^
str2 -> "World\0"
           ^

... and so on
*/

// C String Library
// The C standard library provides a comprehensive set of functions to manipulate strings in the <string.h> header file. Here are some of the most commonly used functions:
// You can access these C string functions by adding #include <string.h> to the top of your file 

// strcpy: Copies a string to another.
char src[] = "Hello";
char dest[6];
strcpy(dest, src);
// dest now contains "Hello"

// strcat: Concatenates (appends) one string to another.
char dest[12] = "Hello";
char src[] = " World";
strcat(dest, src);
// dest now contains "Hello World"

// strlen: Returns the length of a string (excluding the null terminator).
char str[] = "Hello";
size_t len = strlen(str);
// len is 5

// strcmp: Compares two strings lexicographically.
char str1[] = "Hello";
char str2[] = "World";
int result = strcmp(str1, str2);
// result is negative since "Hello" < "World"
// To summarize, strcmp returns a negative value here because lexicographically, "Hello" would come before "World" in a dictionary.

// strncpy: Copies a specified number of characters from one string to another.
char src[] = "Hello";
char dest[6];
strncpy(dest, src, 3);
// dest now contains "Hel"
dest[3] = '\0';
// ensure null termination

// strncat: Concatenates a specified number of characters from one string to another.
char dest[12] = "Hello";
char src[] = " World";
strncat(dest, src, 3);
// dest now contains "Hello Wo"

// strchr: Finds the first occurrence of a character in a string.
char str[] = "Hello";
char *pos = strchr(str, 'l');
// pos points to the first 'l' in "Hello"

// strstr: Finds the first occurrence of a substring in a string.
char str[] = "Hello World";
char *pos = strstr(str, "World");
// pos points to "World" in "Hello World"

// using size_t for arrays indicing and getting th length of arrays 

#include <stdio.h>

void print_array(int arr[], size_t len) {
    for (size_t i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    size_t length = sizeof(numbers) / sizeof(numbers[0]);

    print_array(numbers, length);

    return 0;
}


// Assignment

// excercise.h file
#include <string.h>

typedef struct {
  char buffer[64];
  size_t length;
} TextBuffer;

int smart_append(TextBuffer* dest, const char* src);

// excercise.c file
#include <string.h>
#include "excercise.h"

int smart_append(TextBuffer* dest, const char* src) {
  if (dest == NULL || src == NULL) {
    return 1;
  }

  const size_t max_buffer_size = 64;
  size_t src_length = strlen(src);
  size_t available_space = max_buffer_size - dest->length - 1;

  if (src_length > available_space) {
    // Use strncat to append as much as possible
    strncat(dest->buffer, src, available_space);
    dest->length = max_buffer_size - 1; // Updated to max size excluding null terminator
    return 1;  // Not enough space for a full append
  } else {
    // Use strcat to append all of src
    strcat(dest->buffer, src);
    dest->length += src_length; // Increase length by src_length
    return 0;  // Successfully appended all
  }
}

// solutions function 

#include <string.h>
#include "exercise.h"

int smart_append(TextBuffer* dest, const char* src) {
  if (!dest || !src) return 1;
  const int max_buffer_size = 64;
  size_t src_len = strlen(src);
  size_t available_space = max_buffer_size - dest->length - 1;
  if (src_len > available_space) {
    strncat(dest->buffer, src, available_space);
    dest->length = max_buffer_size - 1;
    return 1;
  }
  strcat(dest->buffer, src);
  dest->length += src_len;
  return 0;
}


// Forward Declaration

// Note Declaration is done in the .h file. *creating structs*
// Sometimes you have a struct that may need to reference itself, or be used recursively.

// For example, consider a Node struct that can contain other Nodes. This might be useful for building a linked list or a tree:

typedef struct Node {
  int value;
  node_t *next;
} node_t;

// The problem here is that node_t is not defined yet, so the compiler will complain. To fix this, we can add a forward declaration:

typedef struct Node node_t;

typedef struct Node {
  int value;
  node_t *next;
} node_t;

// Note that the forward declaration must match the eventual definition, so you can't do something like this:

typedef struct Node node_t;

typedef struct BadName {
  int value;
  node_t *next;
} node_t;



// Mutual Structs
// Forward declarations can also be used when two structs reference each other (a circular reference). For example, a Person has a Computer and a Computer has a Person:

typedef struct Computer computer_t;
typedef struct Person person_t;

struct Person {
  char *name;
  computer_t *computer;
};

struct Computer {
  char *brand;
  person_t *owner;
};


// Enums

// You can define a new enum type like this:

typedef enum DaysOfWeek {
  MONDAY,
  TACO_TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
  FUNDAY,
} days_of_week_t;

/*
The typedef and its alias days_of_week_t are optional, but like with structs, they make the enum easier to use.

In the example above, days_of_week_t is a new type that can only have one of the values defined in the enum:

MONDAY, which is 0
TACO_TUESDAY, which is 1
WEDNESDAY, which is 2
THURSDAY, which is 3
FRIDAY, which is 4
SATURDAY, which is 5
FUNDAY, which is 6
*/

// You can use the enum type like this:

typedef struct Event {
  char *title;
  days_of_week_t day;
} event_t;

// Or if you don't want to use the alias:

typedef struct Event {
  char *title;
  enum DaysOfWeek day;
} event_t;

// An enum is not a collection type like a struct or an array. It's just a list of integers constrained to a new type, where each is given an explicit name.

typedef enum Color {
  RED,
  GREEN,
  BLUE,
} color_t;

// Non-Default Values
// Sometimes, you don't just want to enumerate some names (where the underlying integer constant values don't really matter)... you want to set those enumerations to specific values. 
// For example, you might want to define a program's exit status codes:

typedef enum {
  EXIT_SUCCESS = 0,
  EXIT_FAILURE = 1,
  EXIT_COMMAND_NOT_FOUND = 127,
} ExitStatus;

// Alternatively, you can define the first value and let the compiler fill in the rest (incrementing by 1):

typedef enum {
  LANE_WPM = 200,
  PRIME_WPM, // 201
  TEEJ_WPM,  // 202
} WordsPerMinute;


// Switch Case

// One of the best features of enums is that it can be used in switch statements. Enums + switch statements:

/*
Avoid "magic numbers"
Use descriptive names
With modern tooling, will give you an error/warning that you haven't handled all the cases in your switch
*/

// Here's an example:

switch (logLevel) {
  case LOG_DEBUG:
    printf("Debug logging enabled\n");
    break;
  case LOG_INFO:
    printf("Info logging enabled\n");
    break;
  case LOG_WARN:
    printf("Warning logging enabled\n");
    break;
  case LOG_ERROR:
    printf("Error logging enabled\n");
    break;
  default:
    printf("Unknown log level: %d\n", logLevel);
    break;
}

// You'll notice that we have a break after each case. If you do not have a break, the next case will still execute: it "falls through" to the next case. Many devs have written bugs when using switch statements, 
// because they forgot to add break.

// In some rare cases, you might want the fallthrough:

switch (errorCode) {
  case 1:
  case 2:
  case 3:
    // 1, 2, and 3 are all minor errors
    printf("Minor error occurred. Please try again.\n");
    break;
  case 4:
  case 5:
    // 4 and 5 are major errors
    printf("Major error occurred. Restart required.\n");
    break;
  default:
    printf("Unknown error.\n");
    break;
}

// But usually, it's a footgun. You'll almost always want a break at the end of each case statement.

// #include "http.h"

char *http_to_str(HttpErrorCode code) {
  switch (code) {
  case HTTP_BAD_REQUEST:
    return "400 Bad Request";
  case HTTP_UNAUTHORIZED:
    return "401 Unauthorized";
  case HTTP_NOT_FOUND:
    return "404 Not Found";
  case HTTP_TEAPOT:
    return "418 I AM A TEAPOT!";
  case HTTP_INTERNAL_SERVER_ERROR:
    return "500 Internal Server Error";
  default:
    return "Unknown HTTP status code";
  }
}

/*
Sizeof Enum
The same sizeof operator that we've talked about works on enums.

Generally, enums in C are the same size as an int. However, if an enum value exceeds the range of an int, the C compiler will use a larger integer type to accommodate the value, such as an unsigned int or a long.

unsigned int doesn't represent negative numbers, so it can represent larger positive numbers.
long is just a larger integer type than int, so it can represent larger numbers.
Just Fancy Integers
Enums are often used to represent the possibilities in a set. For example:

SMALL = 0
MEDIUM = 1
LARGE = 2
EXTRA_LARGE = 3
Your code probably cares a lot about which size a variable represents, but it probably doesn't care that SMALL happens to be 0 under the hood. From the compiler's perspective, enums are just fancy integers.
*/

#include <stdio.h>

typedef enum {
  BIG = 123412341234,
  BIGGER,
  BIGGEST,
} BigNumbers;

typedef enum {
  HTTP_BAD_REQUEST = 400,
  HTTP_UNAUTHORIZED = 401,
  HTTP_NOT_FOUND = 404,
  HTTP_I_AM_A_TEAPOT = 418,
  HTTP_INTERNAL_SERVER_ERROR = 500
} HttpErrorCode;

int main() {
  printf("The size of BigNumbers is %zu bytes\n", sizeof(BigNumbers));
  printf("The size of HttpErrorcode is %zu bytes\n", sizeof(HttpErrorCode));
  return 0;
}


// Union
/*
Now that we understand structs and enums, we can learn aboutunions: a combination of the two concepts.

This is not the kind of union that $300k-earning Google employees fight for because they are "underpaid" and "don't have enough oat milk in the office kitchen". 
// No, this feature is one that even Golang doesn't have (probably because they were worried about getting fired from Google for just mentioning the word!)

Unions in C can hold one of several types. They're like a less-strict sum type from the world of functional programming. Here's an example union:
*/
typedef union AgeOrName {
  int age;
  char *name;
} age_or_name_t;

// The age_or_name_t type can hold either an int or a char *, but not both at the same time (that would be a struct). 
// We provide the list of possible types so that the C compiler knows the maximum potential memory requirement, and can account for that. This is how the union is used:

age_or_name_t lane = { .age = 29 };
printf("age: %d\n", lane.age);
// age: 29

// Here's where it gets interesting. What happens if we try to access the name field (even though we set the age field)?

printf("name: %s\n", lane.name);
// name:

// We get... nothing? To be more specific, we get undefined behavior. A union only reserves enough space to hold the largest type in the union and then all of the fields use the same memory. 
// So when we set .age to 29, we are writing the integer representation of 29 to the memory of the lane union:

// 0000 0000 0000 0000 0000 0000 0001 1101

// Then if we try to access .name, we read from the same block of memory but try to interpret the bytes as a char *, which is why we get garbage (which is interpreted as nothing in this case). 
// Put simply, setting the value of .age overwrites the value of .name and vice versa, and you should only access the field that you set.

// excercise.h
typedef enum SnekObjectKind{
  INTEGER = 0,
  STRING = 1,
} snek_object_kind_t;

// don't touch below this line'

typedef union SnekObjectData {
  int v_int;
  char *v_string;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t new_integer(int);
snek_object_t new_string(char *str);
void format_object(snek_object_t obj, char *buffer);

// excercise.c
#include "exercise.h"

void format_object(snek_object_t obj, char *buffer) {
  switch (obj.kind) {
    case INTEGER:
      sprintf(buffer, "int:%d", obj.data.v_int);
      break;
    case STRING:
      sprintf(buffer, "string:%s", obj.data.v_string);
      break;
  }
}

// don't touch below this line'

snek_object_t new_integer(int i) {
  return (snek_object_t){
    .kind = INTEGER,
    .data = {.v_int = i}
  };
}

snek_object_t new_string(char *str) {
  // NOTE: We will learn how to copy this data later.
  return (snek_object_t){
    .kind = STRING,
    .data = {.v_string = str}
  };
}

// Helper Fields
// One interesting (albeit not commonly used) trick is to use unions to create "helpers" for accessing different parts of a piece of memory. Consider the following:

typedef union Color {
  struct {
    uint8_t r;
    uint8_t g;
    uint8_t b;
    uint8_t a;
  } components;
  uint32_t rgba;
} color_t;

// It results in a memory layout like this:

// Only 4 bytes are used. And, unlike in 99% of scenarios, it makes sense to both set and get values from this union through both the components and rgba fields! 
// Both fields in the union are exactly 32 bits in size, which means that we can "safely" (?) access the entire set of colors through the .rgba field, or get a single color component through the .components field.

// The convenience of additional fields, with the efficiency of a single memory location!

/*Complete the PacketHeader union. It should have two potential fields:

tcp_header: A struct. The first 2 bytes are the src_port. The next 2 bytes are the dest_port, and the last 4 bytes are the seq_num.
raw: An array of 8 bytes.
Use uint8_t, uint16_t, and uint32_t for the types of the fields, based on the number of bytes needed. Remember, 8 bits = 1 byte.*/

#include <stdint.h>

typedef union PacketHeader{
  struct {
    uint16_t src_port;
    uint16_t dest_port;
    uint32_t seq_num;
  } tcp_header;
  uint8_t raw[8]
} packet_header_t;


// The Stack
/*
Remember how I told you that memory is basically just a giant array of bytes with addresses at various offsets?

That's true, but it also has some additional structure. In particular, memory is divided into two main regions: the stack and the heap. We'll cover the heap later.

The stack is where local variables are stored. When a function is called, a new stack frame is created in memory to store the function's parameters and local variables. When the function returns, its entire stack frame is deallocated.

The stack is aptly named: it is a stack (the "Last In, First Out" data structure) of memory frames. Each time a function is called, a new frame is pushed onto the stack. When the function returns, its frame is popped off the stack.
*/

// Take a look at this example function:

void create_typist(int uses_nvim) {
  int wpm = 150;
  char name[4] = {'t', 'e', 'e', 'j'};
}

// Say we call create_typist(1). Before the call, our stack memory might look like this, with the next memory address to be used 0xFEFC:

/*
Once called, the stack pointer is moved to make room for:

The return address (to pick up execution after the function returns)
Arguments to the function
Local variables in the function body

and the local variables are stored in the stack frame:

When the function returns, the stack frame is deallocated by resetting the stack pointer to where the frame began.
*/

#include <stdio.h>
#include "exercise.h"

int main() {
  printMessageOne();
  printMessageTwo();
  printMessageThree();
  return 0;
}

void printMessageOne() {
  const char *message = "Dark mode?\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

void printMessageTwo() {
  const char *message = "More like...\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

void printMessageThree() {
  const char *message = "dark roast.\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

// don't touch below this line

void printStackPointerDiff() {
  static void *last_sp = NULL;
  void *current_sp;
  current_sp = __builtin_frame_address(0);
  long diff = (char*)last_sp - (char*)current_sp;
  if (last_sp == NULL){
    last_sp = current_sp;
    diff = 0;
  }
  printf("---------------------------------\n");
  printf("Stack pointer offset: %ld bytes\n", diff);
  printf("---------------------------------\n");
}

// Why a Stack?
// Allocating memory on the stack is preferred when possible because the stack is faster and simpler than the heap (which we'll get to, be patient):

/* 
- Efficient Pointer Management: Stack "allocation" is just a quick increment or decrement of the stack pointer, which is extremely fast. Heap allocations require more complex bookkeeping.
- Cache-Friendly Memory Access: Stack memory is stored in a contiguous block, enhancing cache performance due to spatial locality.
- Automatic Memory Management: Stack memory is managed automatically as functions are called and as they return.
- Inherent Thread Safety: Each thread has its own stack. Heap allocations require synchronization mechanisms when used concurrently, potentially introducing overhead.

One reason Go programs are efficient is that Go uses stack allocation for variables when possible, much like C. 
The Go compiler performs escape analysis to decide whether a variable can be allocated on the stack. On the other hand, 
languages like Python allocate most objects on the heap, which can impact performance.*/ 


// Stack Overflow
/* So the stack is great and all, but one of the downsides is that it has a limited size. If you keep pushing frames onto the stack without popping them off, 
you'll eventually run out of memory and get a stack overflow. (yes, that's what the famous site is named after)

That's one of the reasons recursion without tail-call optimization can be dangerous. Each recursive call pushes a new frame onto the stack, and if you have too many recursive calls, you'll run out of stack space.*/


// Fix the pool_size so that it allocates exactly 10 kibibyte
// A single kibibyte is 1024 bytes.

#include <stdio.h>

int main() {
  const int pool_size = 1024 * 10;
  char snek_pool[pool_size];
  snek_pool[0] = 's';
  snek_pool[1] = 'n';
  snek_pool[2] = 'e';
  snek_pool[3] = 'k';
  snek_pool[4] = '\0';

  printf("Size of pool: %d\n", pool_size);
  printf("Initial string: %s\n", snek_pool);
  return 0;
}


// Remember: the stack is only safe to use within the context of the current function!

/*
Fix the new_coord function so that it returns a struct, not a pointer to a struct. This will force the compiler to copy the struct to the main function's stack frame, and the memory will be safe to use. 
You'll have to update syntax in a few places to accomodate the change.
*/

#include <stdio.h>

typedef struct {
  int x;
  int y;
} coord_t;

coord_t new_coord(int x, int y) {
  coord_t c;
  c.x = x;
  c.y = y;
  return c;
}

int main() {
  coord_t c1 = new_coord(10, 20);
  coord_t c2 = new_coord(30, 40);
  coord_t c3 = new_coord(50, 60);

  printf("c1: %d, %d\n", c1.x, c1.y);
  printf("c2: %d, %d\n", c2.x, c2.y);
  printf("c3: %d, %d\n", c3.x, c3.y);
}

// The Heap
/*
"The heap", as opposed to "the stack", is a pool of long-lived memory shared across the entire program. 
Stack memory is automatically allocated and deallocated as functions are called and return, but heap memory is allocated and deallocated as-needed, independent of the burdensome shackles of function calls.

When you need to store data that outlives the function that created it, you'll send it to the heap. The heap is called "dynamic memory" because it's allocated and deallocated as needed. Take a look at new_int_array:
*/

int *new_int_array(int size) {
  int *new_arr = (int*)malloc(size * sizeof(int)); // Allocate memory
  if (new_arr == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(1); // Exit if allocation fails
  }
  return new_arr;
}


// Let's look at some code that uses new_int_array:

int* arr_of_6 = new_int_array(6);
arr_of_6[0] = 69;
arr_of_6[1] = 42;
arr_of_6[2] = 420;
arr_of_6[3] = 1337;
arr_of_6[4] = 7;
arr_of_6[5] = 0;


// When we're done with the memory, we need to manually deallocate it using the <stdlib.h>'s free function:
free(arr_of_6);


/* Because the size of the array isn't known at compile time, we can't put it on the stack. Instead, we allocate memory on the heap using the <stdlib.h>'s malloc function. 
It takes a number of bytes to allocate as an argument (size * sizeof(int)) and returns a pointer to the allocated memory (a void * that we cast to an int*).

The new_int_array function's size argument is just an integer, it's pushed onto the stack. Assuming size is 6, when malloc is called we're given enough memory to store 6 integers on the heap, and we're given the address of the start of that newly allocated memory. 
We store it in a new local variable called new_arr. The address is stored on the stack, but the data it points to is in the heap.

The data is stored in the heap:


The free function returns (deallocates) that memory for use elsewhere. It's important to note that the pointer (arr_of_6) still exists, but shouldn't be used. It's a "dangling pointer", pointing to deallocated memory
*/

#include <stdio.h>
#include <stdlib.h>
#include "exercise.h"

char *get_full_greeting(char *greeting, char *name, int size) {
  char *full_greeting = (char *)malloc(size * sizeof(char));
  snprintf(full_greeting, size, "%s %s", greeting, name);
  return full_greeting;
}

// snprintf is a useful C standard library function designed to format and store a string in a buffer, all while taking care not to overflow it. Its signature typically looks like this:

int snprintf(char *str, size_t size, const char *format, ...);

/*
Here's what each parameter does:

char *str: This is the pointer to the buffer where the formatted output will be stored.

size_t size: This specifies the maximum number of bytes to write to the buffer, including the null terminator at the end. It ensures that snprintf never writes more than size bytes, guarding against buffer overflows.

const char *format: This is the format string that specifies how the output should be formatted. It can include text, placeholders for variables, and format specifiers like %s for strings, %d for integers, etc.

... (ellipsis): These are the values to be formatted according to the format string. They represent the values that will replace the placeholders in the format string.

Here's a short example of how snprintf is used:
*/
char buffer[20];
snprintf(buffer, sizeof(buffer), "Hello, %s!", "world");

// Malloc

/*The malloc function (memory allocation) is a standard library function in C that allocates a specified number of bytes of memory on the heap and returns a pointer to the allocated memory.

This new memory is uninitialized, which means:

It contains whatever data was previously at that location.
It is the programmer's responsibility to ensure that the allocated memory is properly initialized and eventually freed using free to avoid memory leaks.
If you want to make sure that the memory is properly initialized, you can use the calloc function, which allocates the specified number of bytes of memory on the heap and returns a pointer to the allocated memory. 
This memory is initialized to zero (meaning it contains all zeroes).
*/

// Function Signature
void* malloc(size_t size);

// size: The number of bytes to allocate.
// Returns: A pointer to the allocated memory or NULL if the allocation fails.

// Example usage
// Allocates memory for an array of 4 integers
int *ptr = malloc(4 * sizeof(int));
if (ptr == NULL) {
  // Handle memory allocation failure
  printf("Memory allocation failed\n");
  exit(1);
}
// use the memory here
// ...
free(ptr);

// Assignment

// excercise.h
int *allocate_scalar_list(int size, int multiplier);

// excecise.c
#include <stdio.h>
#include <stdlib.h>

#include "exercise.h"

int *allocate_scalar_list(int size, int multiplier) {
  // Allocate memory for an array of 'size' integers
  int *int_array = (int*)malloc(size * sizeof(int));
  // Check if memory allocation failed and return NULL if so
  if (int_array == NULL) {
    return NULL;
  }
  // Iterate over each index of the array
  for (int i = 0; i < size; i++) {
    // Initialize each element to 'index * multiplier'
    int_array[i] = i * multiplier;
  }
  // Return a pointer to the allocated array
  return int_array;
}

// Purpose of calloc:
// calloc stands for "contiguous allocation". It's used to dynamically allocate memory, just like malloc, but with two key differences:

// a) It takes two arguments: the number of elements and the size of each element.
// b) It initializes all the allocated memory to zero.

// Syntax:

void* calloc(size_t num_elements, size_t element_size);

// Example:

int* numbers = (int*)calloc(5, sizeof(int));

// This allocates memory for 5 integers and initializes them all to 0.

// The main advantage of calloc over malloc is that it automatically initializes the memory to zero, which can be useful in many scenarios to avoid undefined behavior.

/*
Free
The free function deallocates memory that was previously allocated by malloc, calloc, or realloc.

IMPORTANT: free does not change the value stored in the memory, and it doesn't even change the address stored in the pointer. Instead, it simply informs the Operating System that the memory can be used again.

Forgetting to free
Forgetting to call free leads to a memory leak. This means that the allocated memory remains occupied and cannot be reused, even though the program no longer needs it. Over time, 
if a program continues to allocate memory without freeing it, the program may run out of memory and crash.

Memory leaks are one of the most common bugs in C programs, and they can be difficult to track down because the memory is still allocated and accessible, even though it is no longer needed.
*/

// Assignment using the free function to deallocate the memory 

// main.c
#include <stdio.h>
#include <stdlib.h>
#include "exercise.h"

int main(){
  const int num_lists = 500;
  for (int i = 0; i < num_lists; i++) {
    int *lst = allocate_scalar_list(50000, 2);
    if (lst == NULL) {
      printf("Failed to allocate list\n");
      return 1;
    } else {
      printf("Allocated list %d\n", i);
    }
    free(lst);
  }
  return 0;
}

// excercise.c
#include <stdlib.h>
#include "exercise.h"

int *allocate_scalar_list(int size, int multiplier) {
  int *lst = (int *)malloc(size * sizeof(int));
  if (lst == NULL) {
    return NULL;
  }
  for (int i = 0; i < size; i++) {
    lst[i] = i * multiplier;
  }
  return lst;
}

//excercise.h
int *allocate_scalar_list(int size, int multiplier);


/*Big Endian and Little Endian
While we are on the topic of memory, it's worth knowing about "endianness". Endianness is the order in which bytes are stored in memory. The two most common formats are big endian and little endian.

Big Endian
In a big-endian system, the most significant byte is stored first, at the lowest memory address. The "most significant byte" is just a fancy way of saying "the biggest part of the number".

Let’s say you have the hexadecimal number 0x12345678. Here’s how it would be stored in big-endian format:

big endian
The most significant byte (0x12) is stored at the lowest memory address.

Little Endian
In a little-endian system, the least significant byte (the "smallest" part of the number) is stored first, at the lowest memory address. This is the format used by most modern computers.

Using the same number 0x12345678, here’s how it would be stored in little-endian format:

little endian
Here, the least significant byte (0x78) is stored first.

For the most part, you won’t have to worry about endianness when writing programs. The way data is read from memory automatically handles this, so we can spend our valuable time building e-commerce shops for the terminal instead. Endianness becomes important in certain scenarios, like networking and working with binary files.

For now, just know that most modern systems use little-endian, and the compiler takes care of how data is stored and accessed.*/

// For example:

// Comparing hexadecimal 0x12345678 to decomal 0.123456:

/*decimal 0.12 has a higher value or is more significant then 0.0034 or 0.000456. thats why 0x12 if more significant then 0x78*/



// Pointer-Pointers

/*Ok, so... now we know what pointers are. So let's learn it over again! A pointer-to-pointer in C is just a pointer variable that holds the address of another pointer.

This allows you to create complex data structures like arrays of pointers, and to modify pointers indirectly. The syntax is exactly what you would expect:*/

int value;
int *pointer;
int **pointer_pointer;

/*Pointers to pointers (or pointers to pointers to pointers to pointers... you get the idea) are like a treasure map or a scavenger hunt. 
You start at one pointer and keep following the chain of addresses until you get to the final value. It's just a chain of dereferences.*/

#include "stdlib.h"

#include "exercise.h"

// This function allocates memory for an integer and assigns a value to it.
void allocate_int(int **pointer_pointer, int value) {
  // Step 1: Allocate memory on the heap for a single integer.
  int *ptr = (int*)malloc(sizeof(int));

  // Step 2: Update the pointer this pointer pointer points to,
  // so it points to the new memory location.
  *pointer_pointer = ptr;

  // Step 3: Assign the given value to the memory location now pointed to by ptr.
  *ptr = value;
}

// Array of Pointers
// Making an array of integers on the heap is pretty simple:

int *int_array = malloc(sizeof(int) * 3);
int_array[0] = 1;
int_array[1] = 2;
int_array[2] = 3;

// But we can also make an array of pointers! It's quite common to do this in C, especially considering that strings are just pointers to chars:

char **string_array = malloc(sizeof(char *) * 3);
string_array[0] = "foo";
string_array[1] = "bar";
string_array[2] = "baz";

#include <stdlib.h>

#include "exercise.h"

token_t** create_token_pointer_array(token_t* tokens, size_t count) {
  token_t** token_pointers = (token_t**)malloc(count * sizeof(token_t*));
  if (token_pointers == NULL) {
    exit(1);
  }
  
  for (size_t i = 0; i < count; i++) {
    token_pointers[i] = (token_t*)malloc(sizeof(token_t));
    if (token_pointers[i] == NULL) {
      exit(1);
    }
    token_pointers[i]->literal = tokens[i].literal;
    token_pointers[i]->line = tokens[i].line;
    token_pointers[i]->column = tokens[i].column;
  }
  return token_pointers;
}

// Void Pointers

/*We've already discussed void, which essentially means "nothing" in C. It's used in a few different contexts:

void update_soldier(soldier_t *s): means the function returns nothing
soldier_t new_soldier(void): means the function takes no arguments.
And, because C likes re-using ideas but with slightly different meanings (the genius of the design can't be understood by us mere mortals) void also has another use!

A void * "void pointer" tells the compiler that this pointer could point to anything. This is why void pointers are also known as a "generic pointer". 
Since void pointers do not have a specific data type, they cannot be directly dereferenced or used in pointer arithmetic without casting them to another pointer type first.

Casting to Void Pointers
Casting to and from void pointers in C is unique because void pointers are type-agnostic. When casting a specific type pointer to a void pointer, no type information is retained, 
allowing the void pointer to point to any data type. However, you must cast a void pointer back to its original type before dereferencing it, as direct dereferencing is not possible.*/

int number = 42;
void *generic_ptr = &number;

// This doesn't work
printf("Value of number: %d\n", *generic_ptr);

// This works: Cast to appropriate type before dereferencing
printf("Value of number: %d\n", *(int*)generic_ptr);

// A common pattern is to store generic data in one variable, and the type of that data in another variable. 
// This is useful when you need to pass data around without knowing its type at compile time.

typedef enum DATA_TYPE {
  INT,
  FLOAT
} data_type_t;

void printValue(void *ptr, data_type_t type) {
  if (type == INT) {
    printf("Value: %d\n", *(int*)ptr);
  } else if (type == FLOAT) {
    printf("Value: %f\n", *(float*)ptr);
  }
}

int number = 42;
printValue(&number, INT);

float decimal = 3.14;
printValue(&decimal, FLOAT);


/*Ah, a wise question! The void *ptr serves as a generic placeholder, able to point to any data type. In the snek_zero_out function, it allows for flexibility to handle different struct types 
(snek_int_t, snek_float_t, snek_bool_t) with a single pointer.

Here's why we use void *ptr:

Generic Pointer: void* doesn't have a type associated with it, allowing it to point to any data type. This is useful for functions that need to handle multiple data types without knowing them at compile time.

Casting: Before using void *ptr to access fields, you must cast it to the specific pointer type you're working with, such as snek_int_t*, to perform operations like accessing its fields.

When you determine the kind of object using kind, you cast ptr accordingly, so you can safely access and modify the .value field. */


#include "exercise.h"

void snek_zero_out(void *ptr, snek_object_kind_t kind){
  if (kind == INTEGER) {
    ((snek_int_t*)ptr)->value = 0;
  } else if (kind == FLOAT) {
    ((snek_float_t*)ptr)->value = 0;
  } else if (kind == BOOL) {
    ((snek_bool_t*)ptr)->value = 0;
  }
}

// Swapping Integers 

// Sneklang makes it easy to swap two values:

cool_person = "Lane"
uncool_person = "TJ"
cool_person, uncool_person = uncool_person, cool_person
print(cool_person)  # TJ
print(uncool_person)  # Lane
# (get rekt lane)

// Assignment
void swap_ints(int *a, int *b) {
  int var = *a;  // Step 1: Store the value pointed to by 'a' in a temporary variable
  *a = *b;       // Step 2: Assign the value pointed to by 'b' to the location pointed to by 'a'
  *b = var;      // Step 3: Assign the temporary value (original 'a') to the location pointed to by 'b'
}


// Swapping Strings
void swap_strings(char **a, char **b) {
  char *temp = *a;
  *a = *b;
  *b = temp;
}

