::::::::::::::::::::::::::::::::::::::::::::::::
:: BatScript Tutorials
::::::::::::::::::::::::::::::::::::::::::::::::

:: (1) rem/::/REM：注释
echo rem/::/REM的功能是注释

:: (2) echo off：表示在此语句后的所有命令都不显示命令本身
echo echo off或者@echo off：表示在此语句后的所有命令都不显示命令本身
echo off
:: 注意：@与echo off相象，但它是加在每个命令行的最前面，表示运行时不显示这一行的命令行（只能影响当前行）

:: (3) call：调用另一个批处理文件（如果不用call而直接调用别的批处理文件，那么执行完那个批处理文件后将无法返回当前文件并执行当前文件的后续命令）
call example1

:: (4) echo：显示此命令后的字符
echo Hello BatScript!

:: (5) pause：暂停批处理的执行程序并在屏幕上显示Press any key to continue...的提示，等待用户按任意键后继续
echo pause的功能是暂停批处理的执行程序并在屏幕上显示Press any key to continue...的提示，等待用户按任意键后继续
pause

