{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red23\green23\blue23;\red202\green202\blue202;
\red183\green111\blue179;\red70\green137\blue204;\red67\green192\blue160;\red212\green214\blue154;\red140\green211\blue254;
\red167\green197\blue152;\red194\green126\blue101;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c77255\c52549\c75294;\cssrgb\c33725\c61176\c83922;\cssrgb\c30588\c78824\c69020;\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;
\cssrgb\c70980\c80784\c65882;\cssrgb\c80784\c56863\c47059;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # https://rosettacode.org/wiki/Dining_philosophers#Python\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 import\cf4 \strokec4  threading\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  random\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  time\cb1 \
\
\cf2 \cb3 \strokec2 # Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Deadlock is avoided by never waiting for a fork while holding a fork (locked)\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Procedure is to do block while waiting to get first fork, and a nonblocking\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # acquire of second fork.  If failed to get second fork, release first fork,\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # swap which fork is first and which is second and retry until getting both.\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # See discussion page note about 'live lock'.\cf4 \cb1 \strokec4 \
\
\
\cf6 \cb3 \strokec6 class\cf4 \strokec4  \cf7 \strokec7 Philosopher\cf4 \strokec4 (\cf7 \strokec7 threading\cf4 \strokec4 .\cf7 \strokec7 Thread\cf4 \strokec4 ):\cb1 \
\
\cb3     running = \cf6 \strokec6 True\cf4 \cb1 \strokec4 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf8 \strokec8 __init__\cf4 \strokec4 (\cf9 \strokec9 self\cf4 \strokec4 , \cf9 \strokec9 xname\cf4 \strokec4 , \cf9 \strokec9 fork_on_left\cf4 \strokec4 , \cf9 \strokec9 fork_on_right\cf4 \strokec4 ):\cb1 \
\cb3         threading.Thread.\cf8 \strokec8 __init__\cf4 \strokec4 (\cf6 \strokec6 self\cf4 \strokec4 )\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .name = xname\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .fork_on_left = fork_on_left\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .fork_on_right = fork_on_right\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf8 \strokec8 run\cf4 \strokec4 (\cf9 \strokec9 self\cf4 \strokec4 ):\cb1 \
\cb3         \cf5 \strokec5 while\cf4 \strokec4  \cf6 \strokec6 self\cf4 \strokec4 .running:\cb1 \
\cb3             \cf2 \strokec2 #  Philosopher is thinking (but really is sleeping).\cf4 \cb1 \strokec4 \
\cb3             time.sleep(random.uniform(\cf10 \strokec10 3\cf4 \strokec4 , \cf10 \strokec10 13\cf4 \strokec4 ))\cb1 \
\cb3             \cf8 \strokec8 print\cf4 \strokec4 (\cf6 \strokec6 f\cf11 \strokec11 '\cf6 \strokec6 \{self\cf4 \strokec4 .name\cf6 \strokec6 \}\cf11 \strokec11  is hungry.'\cf4 \strokec4 )\cb1 \
\cb3             \cf6 \strokec6 self\cf4 \strokec4 .dine()\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf8 \strokec8 dine\cf4 \strokec4 (\cf9 \strokec9 self\cf4 \strokec4 ):\cb1 \
\cb3         fork1, fork2 = \cf6 \strokec6 self\cf4 \strokec4 .fork_on_left, \cf6 \strokec6 self\cf4 \strokec4 .fork_on_right\cb1 \
\
\cb3         \cf5 \strokec5 while\cf4 \strokec4  \cf6 \strokec6 self\cf4 \strokec4 .running:\cb1 \
\cb3             fork1.acquire(\cf6 \strokec6 True\cf4 \strokec4 )\cb1 \
\cb3             locked = fork2.acquire(\cf6 \strokec6 False\cf4 \strokec4 )\cb1 \
\cb3             \cf5 \strokec5 if\cf4 \strokec4  locked:\cb1 \
\cb3                 \cf5 \strokec5 break\cf4 \cb1 \strokec4 \
\cb3             fork1.release()\cb1 \
\cb3             \cf8 \strokec8 print\cf4 \strokec4 (\cf6 \strokec6 f\cf11 \strokec11 '\cf6 \strokec6 \{self\cf4 \strokec4 .name\cf6 \strokec6 \}\cf11 \strokec11  swaps forks'\cf4 \strokec4 )\cb1 \
\cb3             fork1, fork2 = fork2, fork1\cb1 \
\cb3         \cf5 \strokec5 else\cf4 \strokec4 :\cb1 \
\cb3             \cf5 \strokec5 return\cf4 \cb1 \strokec4 \
\
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .dining()\cb1 \
\cb3         fork2.release()\cb1 \
\cb3         fork1.release()\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf8 \strokec8 dining\cf4 \strokec4 (\cf9 \strokec9 self\cf4 \strokec4 ):\cb1 \
\cb3         \cf8 \strokec8 print\cf4 \strokec4 (\cf6 \strokec6 f\cf11 \strokec11 '\cf6 \strokec6 \{self\cf4 \strokec4 .name\cf6 \strokec6 \}\cf11 \strokec11  starts eating'\cf4 \strokec4 )\cb1 \
\cb3         time.sleep(random.uniform(\cf10 \strokec10 1\cf4 \strokec4 , \cf10 \strokec10 10\cf4 \strokec4 ))\cb1 \
\cb3         \cf8 \strokec8 print\cf4 \strokec4 (\cf6 \strokec6 f\cf11 \strokec11 '\cf6 \strokec6 \{self\cf4 \strokec4 .name\cf6 \strokec6 \}\cf11 \strokec11  finishes eating and leaves to think.'\cf4 \strokec4 )\cb1 \
\
\
\cf6 \cb3 \strokec6 def\cf4 \strokec4  \cf8 \strokec8 dining_philosophers\cf4 \strokec4 ():\cb1 \
\
\cb3     forks = [threading.Lock() \cf5 \strokec5 for\cf4 \strokec4  n \cf5 \strokec5 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (\cf10 \strokec10 5\cf4 \strokec4 )]\cb1 \
\cb3     philosopher_names = (\cf11 \strokec11 'Aristotle'\cf4 \strokec4 , \cf11 \strokec11 'Kant'\cf4 \strokec4 , \cf11 \strokec11 'Buddha'\cf4 \strokec4 , \cf11 \strokec11 'Marx'\cf4 \strokec4 , \cf11 \strokec11 'Russel'\cf4 \strokec4 )\cb1 \
\
\cb3     philosophers = [Philosopher(philosopher_names[i], forks[i % \cf10 \strokec10 5\cf4 \strokec4 ], forks[(i+\cf10 \strokec10 1\cf4 \strokec4 ) % \cf10 \strokec10 5\cf4 \strokec4 ]) \cf5 \strokec5 for\cf4 \strokec4  i \cf5 \strokec5 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (\cf10 \strokec10 5\cf4 \strokec4 )]\cb1 \
\
\cb3     random.seed(\cf10 \strokec10 507129\cf4 \strokec4 )\cb1 \
\cb3     Philosopher.running = \cf6 \strokec6 True\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 for\cf4 \strokec4  p \cf5 \strokec5 in\cf4 \strokec4  philosophers:\cb1 \
\cb3         p.start()\cb1 \
\cb3     time.sleep(\cf10 \strokec10 100\cf4 \strokec4 )\cb1 \
\cb3     Philosopher.running = \cf6 \strokec6 False\cf4 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 print\cf4 \strokec4 (\cf11 \strokec11 "Now we're finishing."\cf4 \strokec4 )\cb1 \
\
\
\cb3 dining_philosophers()\cb1 \
\
}