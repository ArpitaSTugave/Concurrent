{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red23\green23\blue23;\red202\green202\blue202;
\red183\green111\blue179;\red70\green137\blue204;\red212\green214\blue154;\red140\green211\blue254;\red194\green126\blue101;
\red167\green197\blue152;\red67\green192\blue160;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c77255\c52549\c75294;\cssrgb\c33725\c61176\c83922;\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;\cssrgb\c80784\c56863\c47059;
\cssrgb\c70980\c80784\c65882;\cssrgb\c30588\c78824\c69020;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/ and\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   Python.org _thread library documentation at\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   https://docs.python.org/3/library/_thread.html?highlight=_thread#module-_thread\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  logging\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  random\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  sys\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  time\cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  threading \cf5 \strokec5 import\cf4 \strokec4  Thread, Lock\cb1 \
\
\cf5 \cb3 \strokec5 from\cf4 \strokec4  core \cf5 \strokec5 import\cf4 \strokec4  Core\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 execute_ticketing_system_participation\cf4 \strokec4 (\cf8 \strokec8 ticket_number\cf4 \strokec4 , \cf8 \strokec8 part_id\cf4 \strokec4 , \cf8 \strokec8 shared_variable\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     output_file_name = \cf9 \strokec9 "output-"\cf4 \strokec4  + part_id + \cf9 \strokec9 ".txt"\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 # \cf6 \strokec6 NOTE\cf2 \strokec2 : Do not remove this print statement as it is used to grade assignment,\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 # so it should be called by each thread\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 print\cf4 \strokec4 (\cf9 \strokec9 "Thread retrieved ticket number: \cf6 \strokec6 \{\}\cf9 \strokec9  started"\cf4 \strokec4 .format(ticket_number), \cf8 \strokec8 file\cf4 \strokec4 =\cf7 \strokec7 open\cf4 \strokec4 (output_file_name, \cf9 \strokec9 "a"\cf4 \strokec4 ))\cb1 \
\cb3     time.sleep(random.randint(\cf10 \strokec10 0\cf4 \strokec4 , \cf10 \strokec10 10\cf4 \strokec4 ))\cb1 \
\cb3     \cf2 \strokec2 # wait until your ticket number has been called\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 # output your ticket number and the current time\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 while\cf4 \strokec4  \cf6 \strokec6 True\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 if\cf4 \strokec4  shared_variable[\cf9 \strokec9 'ticket_number'\cf4 \strokec4 ] == ticket_number:\cb1 \
\cb3             \cf5 \strokec5 break\cf4 \cb1 \strokec4 \
\cb3         time.sleep(\cf10 \strokec10 0.1\cf4 \strokec4 )\cb1 \
\
\cb3     \cf2 \strokec2 # \cf6 \strokec6 NOTE\cf2 \strokec2 : Do not remove this print statement as it is used to grade assignment,\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 # so it should be called by each thread\cf4 \cb1 \strokec4 \
\
\cb3     \cf7 \strokec7 print\cf4 \strokec4 (\cf9 \strokec9 "Thread with ticket number: \cf6 \strokec6 \{\}\cf9 \strokec9  completed"\cf4 \strokec4 .format(ticket_number), \cf8 \strokec8 file\cf4 \strokec4 =\cf7 \strokec7 open\cf4 \strokec4 (output_file_name, \cf9 \strokec9 "a"\cf4 \strokec4 ))\cb1 \
\cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf10 \strokec10 0\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 class\cf4 \strokec4  \cf11 \strokec11 Assignment\cf4 \strokec4 (\cf11 \strokec11 Core\cf4 \strokec4 ):\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     USERNAME = \cf9 \strokec9 "ARPITA"\cf4 \cb1 \strokec4 \
\cb3     active_threads = []\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 __init__\cf4 \strokec4 (\cf8 \strokec8 self\cf4 \strokec4 , \cf8 \strokec8 args\cf4 \strokec4 ):\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .num_threads = \cf10 \strokec10 1\cf4 \cb1 \strokec4 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .args_conf_list = [[\cf9 \strokec9 '-n'\cf4 \strokec4 , \cf9 \strokec9 'num_threads'\cf4 \strokec4 , \cf10 \strokec10 1\cf4 \strokec4 , \cf9 \strokec9 'number of concurrent threads to execute'\cf4 \strokec4 ],\cb1 \
\cb3                                 [\cf9 \strokec9 '-u'\cf4 \strokec4 , \cf9 \strokec9 'user'\cf4 \strokec4 , \cf6 \strokec6 None\cf4 \strokec4 , \cf9 \strokec9 'the user who is turning in the assignment, needs  to match the '\cf4 \cb1 \strokec4 \
\cb3                                                     \cf9 \strokec9 '.user file contents'\cf4 \strokec4 ],\cb1 \
\cb3                                [\cf9 \strokec9 '-p'\cf4 \strokec4 , \cf9 \strokec9 'part_id'\cf4 \strokec4 , \cf9 \strokec9 'test'\cf4 \strokec4 , \cf9 \strokec9 'the id for the assignment, test by default'\cf4 \strokec4 ]]\cb1 \
\cb3         \cf11 \strokec11 super\cf4 \strokec4 ().\cf7 \strokec7 __init__\cf4 \strokec4 (\cf6 \strokec6 self\cf4 \strokec4 .args_conf_list)\cb1 \
\cb3         \cf11 \strokec11 super\cf4 \strokec4 ().parse_args(\cf8 \strokec8 args\cf4 \strokec4 =args)\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .current_ticket = \cf10 \strokec10 0\cf4 \cb1 \strokec4 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .lock = Lock()\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .shared_variable = \{\cf9 \strokec9 'ticket_number'\cf4 \strokec4 : \cf10 \strokec10 0\cf4 \strokec4 \}\cb1 \
\cb3         _format = \cf9 \strokec9 "\cf6 \strokec6 %(asctime)s\cf9 \strokec9 : \cf6 \strokec6 %(message)s\cf9 \strokec9 "\cf4 \cb1 \strokec4 \
\cb3         logging.basicConfig(\cf8 \strokec8 format\cf4 \strokec4 =_format, \cf8 \strokec8 level\cf4 \strokec4 =logging.INFO,\cb1 \
\cb3                             \cf8 \strokec8 datefmt\cf4 \strokec4 =\cf9 \strokec9 "%H:%M:%S"\cf4 \strokec4 )\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 run\cf4 \strokec4 (\cf8 \strokec8 self\cf4 \strokec4 ):\cb1 \
\cb3         output_file_name = \cf9 \strokec9 "output-"\cf4 \strokec4  + \cf6 \strokec6 self\cf4 \strokec4 .part_id + \cf9 \strokec9 ".txt"\cf4 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 open\cf4 \strokec4 (output_file_name, \cf9 \strokec9 'w'\cf4 \strokec4 ).close()\cb1 \
\cb3         \cf5 \strokec5 if\cf4 \strokec4  \cf6 \strokec6 self\cf4 \strokec4 .test_username_equality(\cf6 \strokec6 self\cf4 \strokec4 .USERNAME):\cb1 \
\cb3             sleeping_time = \cf10 \strokec10 0\cf4 \cb1 \strokec4 \
\cb3             \cf5 \strokec5 for\cf4 \strokec4  index \cf5 \strokec5 in\cf4 \strokec4  \cf7 \strokec7 range\cf4 \strokec4 (\cf6 \strokec6 self\cf4 \strokec4 .num_threads):\cb1 \
\cb3                 logging.info(\cf9 \strokec9 "Assignment run    : create and start thread \cf6 \strokec6 %d\cf9 \strokec9 ."\cf4 \strokec4 , index)\cb1 \
\cb3                 \cf2 \strokec2 # This is where you will start a thread that will participate in a ticketing system\cf4 \cb1 \strokec4 \
\cb3                 \cf2 \strokec2 # have the thread run the execute_ticketing_system_participation function\cf4 \cb1 \strokec4 \
\cb3                 thread = Thread(\cf8 \strokec8 target\cf4 \strokec4 =execute_ticketing_system_participation,\cb1 \
\cb3                                 \cf8 \strokec8 args\cf4 \strokec4 =(index, \cf6 \strokec6 self\cf4 \strokec4 .part_id, \cf6 \strokec6 self\cf4 \strokec4 .shared_variable))\cb1 \
\cb3                 thread.start()\cb1 \
\cb3                 \cf6 \strokec6 self\cf4 \strokec4 .active_threads.append(thread)\cb1 \
\cb3                 \cf2 \strokec2 # Threads will be given a ticket number and will wait until a shared variable is set to that number\cf4 \cb1 \strokec4 \
\
\cb3                 \cf2 \strokec2 # The code will also need to know when all threads have completed their work\cf4 \cb1 \strokec4 \
\cb3                 sleeping_time += \cf10 \strokec10 1\cf4 \cb1 \strokec4 \
\cb3             time.sleep(sleeping_time)\cb1 \
\cb3             \cf6 \strokec6 self\cf4 \strokec4 .manage_ticketing_system()\cb1 \
\cb3             logging.info(\cf9 \strokec9 "Assignment completed all running threads."\cf4 \strokec4 )\cb1 \
\cb3             \cf5 \strokec5 return\cf4 \strokec4  \cf10 \strokec10 0\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 else\cf4 \strokec4 :\cb1 \
\cb3             \cf7 \strokec7 print\cf4 \strokec4 (\cf6 \strokec6 self\cf4 \strokec4 .USERNAME)\cb1 \
\cb3             logging.error(\cf9 \strokec9 "Assignment had an error your usernames not matching. Please check code and .user file."\cf4 \strokec4 )\cb1 \
\cb3             \cf5 \strokec5 return\cf4 \strokec4  \cf10 \strokec10 1\cf4 \cb1 \strokec4 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 manage_ticketing_system\cf4 \strokec4 (\cf8 \strokec8 self\cf4 \strokec4 ):\cb1 \
\cb3         \cf2 \strokec2 # increment a ticket number shared by a number of threads and check that no active threads are running\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 for\cf4 \strokec4  ticket \cf5 \strokec5 in\cf4 \strokec4  \cf7 \strokec7 range\cf4 \strokec4 (\cf6 \strokec6 self\cf4 \strokec4 .num_threads):\cb1 \
\cb3             \cf5 \strokec5 with\cf4 \strokec4  \cf6 \strokec6 self\cf4 \strokec4 .lock:\cb1 \
\cb3                 \cf6 \strokec6 self\cf4 \strokec4 .shared_variable[\cf9 \strokec9 'ticket_number'\cf4 \strokec4 ] = ticket\cb1 \
\cb3             time.sleep(\cf10 \strokec10 1\cf4 \strokec4 )  \cf2 \strokec2 # Give time for the thread with this ticket to proceed\cf4 \cb1 \strokec4 \
\
\cb3         \cf5 \strokec5 for\cf4 \strokec4  t \cf5 \strokec5 in\cf4 \strokec4  \cf6 \strokec6 self\cf4 \strokec4 .active_threads:\cb1 \
\cb3             t.join()\cb1 \
\cb3         \cf5 \strokec5 return\cf4 \strokec4  \cf10 \strokec10 0\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf8 \strokec8 __name__\cf4 \strokec4  == \cf9 \strokec9 "__main__"\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     assignment = Assignment(\cf8 \strokec8 args\cf4 \strokec4 =sys.argv[\cf10 \strokec10 1\cf4 \strokec4 :])\cb1 \
\cb3     exit_code = assignment.run()\cb1 \
\cb3     sys.exit(exit_code)\cb1 \
\
}