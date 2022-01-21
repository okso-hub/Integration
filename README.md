# Integration

This program integrates a completely rational function for given boundaries.

After you run the project you will be asked to enter the upper and the lower border.

```
❯ python3 main.py
Enter lower border: 0
Enter upper border: 2
```

Then you will be asked to enter the factors for all variables with the power from 0 to 5.


If we wanted to enter the function *-x^4 + 2x^2 + 8* we would have to enter the following:

```
❯ python3 main.py
Enter lower border: 0
Enter upper border: 2
Factor of x^5 = 0
Factor of x^4 = -1
Factor of x^3 = 0
Factor of x^2 = 2
Factor of x^1 = 0
Factor of x^0 = 8
```

After entering the last parameter, the program will calculate the integral value and output it:

```
Your function: 
    4     2
-1 x + 2 x + 8 
Your interval: [0, 2]
The integral value is 14.93.
```
