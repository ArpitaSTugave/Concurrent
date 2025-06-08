{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red23\green23\blue23;\red202\green202\blue202;
\red183\green111\blue179;\red70\green137\blue204;\red194\green126\blue101;\red67\green192\blue160;\red140\green211\blue254;
\red212\green214\blue154;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c77255\c52549\c75294;\cssrgb\c33725\c61176\c83922;\cssrgb\c80784\c56863\c47059;\cssrgb\c30588\c78824\c69020;\cssrgb\c61176\c86275\c99608;
\cssrgb\c86275\c86275\c66667;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 //\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 // Created by Chancellor Pascale on 1/29/21.\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 //\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #include\cf6 \strokec6  \cf7 \strokec7 <iostream>\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #include\cf6 \strokec6  \cf7 \strokec7 <atomic>\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #include\cf6 \strokec6  \cf7 \strokec7 <thread>\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 #ifndef\cf6 \strokec6  CPP_EXAMPLES_ATOMIC_EXAMPLE_H\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #define\cf6 \strokec6  CPP_EXAMPLES_ATOMIC_EXAMPLE_H\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8 std\cf4 \strokec4 ::\cf8 \strokec8 atomic\cf4 \strokec4 <\cf6 \strokec6 bool\cf4 \strokec4 > \cf9 \strokec9 ready\cf4 \strokec4 ;\cb1 \
\
\cf6 \cb3 \strokec6 void\cf4 \strokec4  \cf10 \strokec10 doWorkWithAtomicBoolean\cf4 \strokec4 (\cf6 \strokec6 int\cf4 \strokec4  \cf9 \strokec9 threadIndex\cf4 \strokec4 );\cb1 \
\cf6 \cb3 \strokec6 void\cf4 \strokec4  \cf10 \strokec10 executeThreadsWithAtomicBoolean\cf4 \strokec4 (\cf6 \strokec6 int\cf4 \strokec4  \cf9 \strokec9 numThreads\cf4 \strokec4 );\cb1 \
\cf6 \cb3 \strokec6 void\cf4 \strokec4  \cf10 \strokec10 doWorkWithAtomicThreadFence\cf4 \strokec4 (\cf6 \strokec6 int\cf4 \strokec4  \cf9 \strokec9 threadIndex\cf4 \strokec4 );\cb1 \
\cf6 \cb3 \strokec6 void\cf4 \strokec4  \cf10 \strokec10 executeWithAtomicThreadFence\cf4 \strokec4 (\cf6 \strokec6 int\cf4 \strokec4  \cf9 \strokec9 numThreads\cf4 \strokec4 );\cb1 \
\
\cf5 \cb3 \strokec5 #endif\cf2 \strokec2  //CPP_EXAMPLES_ATOMIC_EXAMPLE_H\cf4 \cb1 \strokec4 \
\
}