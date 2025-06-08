{\rtf1\ansi\ansicpg1252\cocoartf2822
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
\outl0\strokewidth0 \strokec2 # Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/ and\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   Python.org _thread library documentation at\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   https://docs.python.org/3/library/_thread.html?highlight=_thread#module-_thread\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  logging\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  _thread\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  sys\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  time\cb1 \
\
\cf5 \cb3 \strokec5 import\cf4 \strokec4  pydash \cf5 \strokec5 as\cf4 \strokec4  _\cb1 \
\
\cf5 \cb3 \strokec5 from\cf4 \strokec4  core \cf5 \strokec5 import\cf4 \strokec4  thread_function, Core\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 class\cf4 \strokec4  \cf7 \strokec7 StartNewThreadExample\cf4 \strokec4 :\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf8 \strokec8 __init__\cf4 \strokec4 (\cf9 \strokec9 self\cf4 \strokec4 ):\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .num_threads = \cf10 \strokec10 1\cf4 \cb1 \strokec4 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .args_conf_list = [[\cf11 \strokec11 '-n'\cf4 \strokec4 , \cf11 \strokec11 'num_threads'\cf4 \strokec4 , \cf10 \strokec10 1\cf4 \strokec4 , \cf11 \strokec11 'number of concurrent threads to execute'\cf4 \strokec4 ]]\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .core = Core(\cf6 \strokec6 self\cf4 \strokec4 .args_conf_list)\cb1 \
\cb3         _format = \cf11 \strokec11 "\cf6 \strokec6 %(asctime)s\cf11 \strokec11 : \cf6 \strokec6 %(message)s\cf11 \strokec11 "\cf4 \cb1 \strokec4 \
\cb3         logging.basicConfig(\cf9 \strokec9 format\cf4 \strokec4 =_format, \cf9 \strokec9 level\cf4 \strokec4 =logging.INFO,\cb1 \
\cb3                             \cf9 \strokec9 datefmt\cf4 \strokec4 =\cf11 \strokec11 "%H:%M:%S"\cf4 \strokec4 )\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf8 \strokec8 run\cf4 \strokec4 (\cf9 \strokec9 self\cf4 \strokec4 ):\cb1 \
\cb3         sleeping_time = \cf10 \strokec10 0\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 for\cf4 \strokec4  index \cf5 \strokec5 in\cf4 \strokec4  \cf8 \strokec8 range\cf4 \strokec4 (\cf6 \strokec6 self\cf4 \strokec4 .num_threads):\cb1 \
\cb3             logging.info(\cf11 \strokec11 "StartNewThreadExample run    : create and start thread \cf6 \strokec6 %d\cf11 \strokec11 ."\cf4 \strokec4 , index)\cb1 \
\cb3             _thread.start_new_thread(thread_function, (index, ))\cb1 \
\cb3             sleeping_time += \cf10 \strokec10 1\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 # sleep for what should be long enough for threads to complete\cf4 \cb1 \strokec4 \
\cb3         time.sleep(sleeping_time)\cb1 \
\cb3         logging.info(\cf11 \strokec11 "StartNewThreadExample completed running threads."\cf4 \strokec4 )\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf8 \strokec8 parse_args\cf4 \strokec4 (\cf9 \strokec9 self\cf4 \strokec4 , \cf9 \strokec9 args\cf4 \strokec4 ):\cb1 \
\cb3         namespace = \cf6 \strokec6 self\cf4 \strokec4 .core.parse_args(\cf9 \strokec9 args\cf4 \strokec4 =args)\cb1 \
\cb3         \cf5 \strokec5 if\cf4 \strokec4  namespace:\cb1 \
\cb3             \cf6 \strokec6 self\cf4 \strokec4 .num_threads = \cf7 \strokec7 int\cf4 \strokec4 (_.get(namespace, \cf11 \strokec11 'num_threads'\cf4 \strokec4 , \cf10 \strokec10 1\cf4 \strokec4 ))\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf9 \strokec9 __name__\cf4 \strokec4  == \cf11 \strokec11 "__main__"\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     start_new_thread_example = StartNewThreadExample()\cb1 \
\cb3     start_new_thread_example.parse_args(\cf9 \strokec9 args\cf4 \strokec4 =sys.argv[\cf10 \strokec10 1\cf4 \strokec4 :])\cb1 \
\cb3     start_new_thread_example.run()\cb1 \
\
}