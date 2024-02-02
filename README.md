# Topics-In-Comp-Sci-1
Coding Homework for TICS1

Files:

[**echo.py**](https://github.com/talhanaveed753/Assignment-1-Python-Refresher/blob/main/echo.py) - Code for echo program, simulates a echo in the mountains.<br>
[**codeAndOutputFor-echoPy (PNG)**](https://github.com/talhanaveed753/Assignment-1-Python-Refresher/blob/main/codeAndOutputFor-echoPy.png) - Contains the code and the program output for echo.py after running with inputs "echo 123" and "Helloooo".<br>
[**fib.py**](https://github.com/talhanaveed753/Assignment-1-Python-Refresher/blob/main/fib.py) - Code to calculate nth fib terms (to 100), time each consecutive calculation, and graph the data.<br>
[**codeFor-fibPy (PNG)**](https://github.com/talhanaveed753/Assignment-1-Python-Refresher/blob/main/codeFor-fibPy.png) - Contains and image for fib.py code.<br>
[**outputFor-fibPy (TXT)**](https://github.com/talhanaveed753/Assignment-1-Python-Refresher/blob/main/outputFor-fibPy.txt) - Contains the program output for fib.py with time taken to calculate each nth fib term and each nth fib value (0-100).<br>
[**graphForFibCalculations (PNG)**](https://github.com/talhanaveed753/Assignment-1-Python-Refresher/blob/main/graphForFibCalculations.png) - Graph that is output after fib.py completes successfully, contains line graph showing time relation to fib calcs.<br>

![Screenshot of the line graph for nth fibonacci number vs the fiboncci calculation time for the nth number.](https://github.com/talhanaveed753/Assignment-1-Python-Refresher/blob/main/graphForFibCalculations.png)<br>
This graph shows the nth fibonacci term, plotted on the x-axis, vs the time to calculate that term, plotted on the y-axis. I noticed the calculation time between fib terms 77 and 78 had a significant jump, I was unable to determine how to optimize the program any further. Apart from that it looks like as the nth fibonacci term gets bigger (which means the value is getting bigger) there seems to be a relatively linear time increase to calculate the value for that term.<br>

I experienced some difficulty with importing functools and matplotlib and with figuring out how to use venv.
