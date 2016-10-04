Linter for CudaLint plugin.
It adds support for Java lexer.
It uses "javac" compiler.

For Windows: you need to create file "javac.bat" in any dir of PATH.
Write into "javac.bat" one line pointing to your real "javac.exe":

"C:\Program Files (x86)\Java\jdk1.7.0_51\bin\javac.exe" %1 %2 %3 %4 %5 %6 %7
