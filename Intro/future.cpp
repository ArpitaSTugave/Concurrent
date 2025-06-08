{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red23\green23\blue23;\red202\green202\blue202;
\red183\green111\blue179;\red70\green137\blue204;\red194\green126\blue101;\red212\green214\blue154;\red67\green192\blue160;
\red140\green211\blue254;\red205\green173\blue106;\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c77255\c52549\c75294;\cssrgb\c33725\c61176\c83922;\cssrgb\c80784\c56863\c47059;\cssrgb\c86275\c86275\c66667;\cssrgb\c30588\c78824\c69020;
\cssrgb\c61176\c86275\c99608;\cssrgb\c84314\c72941\c49020;\cssrgb\c70980\c80784\c65882;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 //\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 // Created by Chancellor Pascale on 1/30/21.\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 // Code based on http://www.cplusplus.com/reference/future/promise/\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 //\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #include\cf6 \strokec6  \cf7 \strokec7 "future_example.h"\cf4 \cb1 \strokec4 \
\
\cf6 \cb3 \strokec6 void\cf4 \strokec4  \cf8 \strokec8 doWorkWithFutures\cf4 \strokec4 (\cf9 \strokec9 std\cf4 \strokec4 ::\cf9 \strokec9 future\cf4 \strokec4 <\cf6 \strokec6 int\cf4 \strokec4 >\cf6 \strokec6 &\cf4 \strokec4  \cf10 \strokec10 fut\cf4 \strokec4 )\{\cb1 \
\cb3     \cf6 \strokec6 int\cf4 \strokec4  \cf10 \strokec10 x\cf4 \strokec4  = \cf10 \strokec10 fut\cf4 \strokec4 .\cf8 \strokec8 get\cf4 \strokec4 ();\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Future index: "\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf10 \strokec10 x\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 " executing\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3 \}\cb1 \
\
\cf6 \cb3 \strokec6 void\cf4 \strokec4  \cf8 \strokec8 executeThreadsWithFutures\cf4 \strokec4 ()\{\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Starting a threads to use futures\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf9 \strokec9 promise\cf4 \strokec4 <\cf6 \strokec6 int\cf4 \strokec4 > \cf10 \strokec10 prom\cf4 \strokec4 ;\cf2 \strokec2                       // create promise\cf4 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf9 \strokec9 future\cf4 \strokec4 <\cf6 \strokec6 int\cf4 \strokec4 > \cf10 \strokec10 fut\cf4 \strokec4  = \cf10 \strokec10 prom\cf4 \strokec4 .\cf8 \strokec8 get_future\cf4 \strokec4 ();\cf2 \strokec2     // engagement with future\cf4 \cb1 \strokec4 \
\cb3     \cb1 \
\cf2 \cb3 \strokec2     // spawn a threads\cf4 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf9 \strokec9 thread\cf4 \strokec4  \cf10 \strokec10 th1\cf4 \strokec4 (\cf8 \strokec8 doWorkWithFutures\cf4 \strokec4 , \cf9 \strokec9 std\cf4 \strokec4 ::\cf8 \strokec8 ref\cf4 \strokec4 (\cf10 \strokec10 fut\cf4 \strokec4 ));\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Press a key to let program proceed\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cf8 \strokec8 getchar\cf4 \strokec4 ();\cb1 \
\cb3     \cb1 \
\cb3     \cf10 \strokec10 prom\cf4 \strokec4 .\cf8 \strokec8 set_value\cf4 \strokec4 (\cf12 \strokec12 1\cf4 \strokec4 );\cb1 \
\cb3     \cf10 \strokec10 th1\cf4 \strokec4 .\cf8 \strokec8 join\cf4 \strokec4 ();\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Press a key to let program proceed\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cf8 \strokec8 getchar\cf4 \strokec4 ();\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Completed all threads\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3 \}\cb1 \
\
\cf6 \cb3 \strokec6 int\cf4 \strokec4  \cf8 \strokec8 doWorkWithAsync\cf4 \strokec4 (\cf6 \strokec6 int\cf4 \strokec4  \cf10 \strokec10 x\cf4 \strokec4 )\{\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Squaring "\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf10 \strokec10 x\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 ". Please, wait...\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf10 \strokec10 x\cf4 \strokec4 *\cf10 \strokec10 x\cf4 \strokec4 ;\cb1 \
\cb3 \}\cb1 \
\
\cf6 \cb3 \strokec6 void\cf4 \strokec4  \cf8 \strokec8 executeWithAsync\cf4 \strokec4 (\cf6 \strokec6 int\cf4 \strokec4  \cf10 \strokec10 numFutures\cf4 \strokec4 )\{\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Using future with async to asynchronously execute squaring of values"\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf9 \strokec9 future\cf4 \strokec4 <\cf6 \strokec6 int\cf4 \strokec4 > \cf10 \strokec10 first\cf4 \strokec4  = \cf9 \strokec9 std\cf4 \strokec4 ::\cf8 \strokec8 async\cf4 \strokec4  (\cf8 \strokec8 doWorkWithAsync\cf4 \strokec4 , \cf12 \strokec12 1\cf4 \strokec4 );\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf9 \strokec9 future\cf4 \strokec4 <\cf6 \strokec6 int\cf4 \strokec4 > \cf10 \strokec10 second\cf4 \strokec4  = \cf9 \strokec9 std\cf4 \strokec4 ::\cf8 \strokec8 async\cf4 \strokec4  (\cf8 \strokec8 doWorkWithAsync\cf4 \strokec4 , \cf12 \strokec12 2\cf4 \strokec4 );\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf9 \strokec9 future\cf4 \strokec4 <\cf6 \strokec6 int\cf4 \strokec4 > \cf10 \strokec10 third\cf4 \strokec4  = \cf9 \strokec9 std\cf4 \strokec4 ::\cf8 \strokec8 async\cf4 \strokec4  (\cf8 \strokec8 doWorkWithAsync\cf4 \strokec4 , \cf12 \strokec12 3\cf4 \strokec4 );\cb1 \
\cb3     \cb1 \
\cb3     \cf6 \strokec6 int\cf4 \strokec4  \cf10 \strokec10 firstResult\cf4 \strokec4  = \cf10 \strokec10 first\cf4 \strokec4 .\cf8 \strokec8 get\cf4 \strokec4 ();\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Future first squared value: "\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf10 \strokec10 firstResult\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cf6 \strokec6 int\cf4 \strokec4  \cf10 \strokec10 secondResult\cf4 \strokec4  = \cf10 \strokec10 second\cf4 \strokec4 .\cf8 \strokec8 get\cf4 \strokec4 ();\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Future second squared value: "\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf10 \strokec10 secondResult\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cf6 \strokec6 int\cf4 \strokec4  \cf10 \strokec10 thirdResult\cf4 \strokec4  = \cf10 \strokec10 third\cf4 \strokec4 .\cf8 \strokec8 get\cf4 \strokec4 ();\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Future third squared value: "\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf10 \strokec10 thirdResult\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cb1 \
\cb3 \}\cb1 \
\
\cf6 \cb3 \strokec6 int\cf4 \strokec4  \cf8 \strokec8 main\cf4 \strokec4 (\cf6 \strokec6 int\cf4 \strokec4  \cf10 \strokec10 argc\cf4 \strokec4 , \cf6 \strokec6 char\cf4 \strokec4  \cf6 \strokec6 *\cf10 \strokec10 argv\cf4 \strokec4 [])\{\cb1 \
\cb3     \cf6 \strokec6 int\cf4 \strokec4  \cf10 \strokec10 numFutures\cf4 \strokec4  = \cf12 \strokec12 3\cf4 \strokec4 ;\cb1 \
\cb3     \cf5 \strokec5 if\cf4 \strokec4 (\cf10 \strokec10 argc\cf4 \strokec4  > \cf12 \strokec12 1\cf4 \strokec4 )\{\cb1 \
\cb3         \cf10 \strokec10 numFutures\cf4 \strokec4  = \cf8 \strokec8 atoi\cf4 \strokec4 (\cf10 \strokec10 argv\cf4 \strokec4 [\cf12 \strokec12 1\cf4 \strokec4 ]);\cb1 \
\cb3     \}\cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Pay attention to the fact that newlines will not always be added at the end of lines if multiple <<'s\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cf8 \strokec8 executeThreadsWithFutures\cf4 \strokec4 ();\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Press a key to let program proceed\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cf8 \strokec8 getchar\cf4 \strokec4 ();\cb1 \
\cb3     \cb1 \
\cb3     \cf8 \strokec8 executeWithAsync\cf4 \strokec4 (\cf10 \strokec10 numFutures\cf4 \strokec4 );\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf4 \strokec4 ::\cf10 \strokec10 cout\cf4 \strokec4  \cf8 \strokec8 <<\cf4 \strokec4  \cf7 \strokec7 "Press a key to let program proceed\cf11 \strokec11 \\n\cf7 \strokec7 "\cf4 \strokec4 ;\cb1 \
\cb3     \cf8 \strokec8 getchar\cf4 \strokec4 ();\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf12 \strokec12 0\cf4 \strokec4 ;\cb1 \
\cb3 \}\cb1 \
}