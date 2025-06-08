{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red23\green23\blue23;\red70\green137\blue204;
\red194\green126\blue101;\red202\green202\blue202;\red212\green214\blue154;\red140\green211\blue254;\red67\green192\blue160;
\red205\green173\blue106;\red89\green138\blue67;\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c11765\c11765\c11765;\cssrgb\c33725\c61176\c83922;
\cssrgb\c80784\c56863\c47059;\cssrgb\c83137\c83137\c83137;\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;\cssrgb\c30588\c78824\c69020;
\cssrgb\c84314\c72941\c49020;\cssrgb\c41569\c60000\c33333;\cssrgb\c70980\c80784\c65882;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #include\cf4 \strokec4  \cf5 \strokec5 "thread_example.h"\cf6 \cb1 \strokec6 \
\
\cf4 \cb3 \strokec4 void\cf6 \strokec6  \cf7 \strokec7 doWork\cf6 \strokec6 (\cf4 \strokec4 int\cf6 \strokec6  \cf8 \strokec8 threadIndex\cf6 \strokec6 )\{\cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf8 \strokec8 cout\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "Performing work for thread: "\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf8 \strokec8 threadIndex\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "\cf10 \strokec10 \\n\cf5 \strokec5 "\cf6 \strokec6 ;\cb1 \
\cb3 \}\cb1 \
\
\cf4 \cb3 \strokec4 void\cf6 \strokec6  \cf7 \strokec7 executeThreads\cf6 \strokec6 ()\{\cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf8 \strokec8 cout\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "Starting threads\cf10 \strokec10 \\n\cf5 \strokec5 "\cf6 \strokec6 ;\cb1 \
\
\cf11 \cb3 \strokec11     // Create threads\cf6 \cb1 \strokec6 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf9 \strokec9 thread\cf6 \strokec6  \cf8 \strokec8 zeroth\cf6 \strokec6 (\cf7 \strokec7 doWork\cf6 \strokec6 , \cf12 \strokec12 0\cf6 \strokec6 );\cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf9 \strokec9 thread\cf6 \strokec6  \cf8 \strokec8 first\cf6 \strokec6 (\cf7 \strokec7 doWork\cf6 \strokec6 , \cf12 \strokec12 1\cf6 \strokec6 );\cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf9 \strokec9 thread\cf6 \strokec6  \cf8 \strokec8 second\cf6 \strokec6 (\cf7 \strokec7 doWork\cf6 \strokec6 , \cf12 \strokec12 2\cf6 \strokec6 );\cb1 \
\
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf8 \strokec8 cout\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "Press a key to let program proceed\cf10 \strokec10 \\n\cf5 \strokec5 "\cf6 \strokec6 ;\cb1 \
\cb3     \cf7 \strokec7 getchar\cf6 \strokec6 ();\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf8 \strokec8 cout\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "Joining threads\cf10 \strokec10 \\n\cf5 \strokec5 "\cf6 \strokec6 ;\cb1 \
\cb3     \cb1 \
\cf11 \cb3 \strokec11     // Wait for threads to complete\cf6 \cb1 \strokec6 \
\cb3     \cf8 \strokec8 second\cf6 \strokec6 .\cf7 \strokec7 join\cf6 \strokec6 ();\cb1 \
\cb3     \cf8 \strokec8 zeroth\cf6 \strokec6 .\cf7 \strokec7 join\cf6 \strokec6 ();\cb1 \
\cb3     \cf8 \strokec8 first\cf6 \strokec6 .\cf7 \strokec7 join\cf6 \strokec6 ();\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf8 \strokec8 cout\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "Completed all threads\cf10 \strokec10 \\n\cf5 \strokec5 "\cf6 \strokec6 ;\cb1 \
\cb3 \}\cb1 \
\
\cf4 \cb3 \strokec4 void\cf6 \strokec6  \cf7 \strokec7 executeAndDetachThread\cf6 \strokec6 () \{\cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf9 \strokec9 thread\cf6 \strokec6  \cf8 \strokec8 thread\cf6 \strokec6 (\cf7 \strokec7 doWork\cf6 \strokec6 , \cf12 \strokec12 0\cf6 \strokec6 );\cb1 \
\cb3     \cf8 \strokec8 thread\cf6 \strokec6 .\cf7 \strokec7 detach\cf6 \strokec6 ();\cb1 \
\cb3 \}\cb1 \
\
\cf4 \cb3 \strokec4 int\cf6 \strokec6  \cf7 \strokec7 main\cf6 \strokec6 ()\{\cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf8 \strokec8 cout\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "Pay attention to the fact that newlines will not always be added at the end of lines if multiple <<'s\cf10 \strokec10 \\n\cf5 \strokec5 "\cf6 \strokec6 ;\cb1 \
\cb3     \cf7 \strokec7 executeThreads\cf6 \strokec6 ();\cb1 \
\
\cb3     \cf7 \strokec7 executeAndDetachThread\cf6 \strokec6 ();\cb1 \
\
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf8 \strokec8 cout\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "Sleeping for 1 second\cf10 \strokec10 \\n\cf5 \strokec5 "\cf6 \strokec6 ;\cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf9 \strokec9 this_thread\cf6 \strokec6 ::\cf7 \strokec7 sleep_for\cf6 \strokec6  (\cf9 \strokec9 std\cf6 \strokec6 ::\cf9 \strokec9 chrono\cf6 \strokec6 ::\cf9 \strokec9 seconds\cf6 \strokec6 (\cf12 \strokec12 1\cf6 \strokec6 ));\cb1 \
\cb3     \cb1 \
\cb3     \cf9 \strokec9 std\cf6 \strokec6 ::\cf8 \strokec8 cout\cf6 \strokec6  \cf7 \strokec7 <<\cf6 \strokec6  \cf5 \strokec5 "Press a key to let program proceed\cf10 \strokec10 \\n\cf5 \strokec5 "\cf6 \strokec6 ;\cb1 \
\cb3     \cf7 \strokec7 getchar\cf6 \strokec6 ();\cb1 \
\cb3     \cf2 \strokec2 return\cf6 \strokec6  \cf12 \strokec12 0\cf6 \strokec6 ;\cb1 \
\cb3 \}\cb1 \
}