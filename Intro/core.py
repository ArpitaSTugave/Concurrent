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
\outl0\strokewidth0 \strokec2 # Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  logging\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  random\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  time\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  argparse\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  pydash \cf5 \strokec5 as\cf4 \strokec4  _\cb1 \
\
\
\cf6 \cb3 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 thread_function\cf4 \strokec4 (\cf8 \strokec8 index\cf4 \strokec4 ):\cb1 \
\cb3     logging.info(\cf9 \strokec9 "Thread \cf6 \strokec6 %d\cf9 \strokec9 : starting"\cf4 \strokec4 , index)\cb1 \
\cb3     time.sleep(\cf10 \strokec10 1\cf4 \strokec4 )\cb1 \
\cb3     logging.info(\cf9 \strokec9 "Thread \cf6 \strokec6 %d\cf9 \strokec9 : finishing"\cf4 \strokec4 , index)\cb1 \
\
\
\cf6 \cb3 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 critical_section_acquire_release\cf4 \strokec4 (\cf8 \strokec8 name\cf4 \strokec4 , \cf8 \strokec8 sync_object\cf4 \strokec4 ):\cb1 \
\cb3     \cf2 \strokec2 # Add random amount of time for sleep so that execution may be random\cf4 \cb1 \strokec4 \
\cb3     time.sleep(random.randint(\cf10 \strokec10 0\cf4 \strokec4 , \cf10 \strokec10 10\cf4 \strokec4 ))\cb1 \
\cb3     sync_object.acquire()\cb1 \
\cb3     logging.info(\cf9 \strokec9 "critical_section_acquire_release thread: \cf6 \strokec6 %d\cf9 \strokec9  acquired synchronization object."\cf4 \strokec4 , name)\cb1 \
\cb3     thread_function(name)\cb1 \
\cb3     sync_object.release()\cb1 \
\cb3     logging.info(\cf9 \strokec9 "critical_section_acquire_release thread: \cf6 \strokec6 %d\cf9 \strokec9  released synchronization object."\cf4 \strokec4 , name)\cb1 \
\
\
\cf6 \cb3 \strokec6 class\cf4 \strokec4  \cf11 \strokec11 Core\cf4 \strokec4 :\cb1 \
\
\cb3     file_username = \cf6 \strokec6 None\cf4 \cb1 \strokec4 \
\cb3     username_arg = \cf6 \strokec6 None\cf4 \cb1 \strokec4 \
\cb3     num_threads = \cf10 \strokec10 1\cf4 \cb1 \strokec4 \
\cb3     part_id = \cf6 \strokec6 None\cf4 \cb1 \strokec4 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 __init__\cf4 \strokec4 (\cf8 \strokec8 self\cf4 \strokec4 , \cf8 \strokec8 args_list\cf4 \strokec4 =\cf6 \strokec6 None\cf4 \strokec4 ):\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .parser = argparse.ArgumentParser(\cf8 \strokec8 description\cf4 \strokec4 =\cf9 \strokec9 'Process command-line arguments'\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 for\cf4 \strokec4  arg \cf5 \strokec5 in\cf4 \strokec4  args_list:\cb1 \
\cb3             \cf6 \strokec6 self\cf4 \strokec4 .add_arg_parser_argument(arg)\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .read_user_file()\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 read_user_file\cf4 \strokec4 (\cf8 \strokec8 self\cf4 \strokec4 ):\cb1 \
\cb3         \cf8 \strokec8 file\cf4 \strokec4  = \cf7 \strokec7 open\cf4 \strokec4 (\cf9 \strokec9 ".user"\cf4 \strokec4 , \cf9 \strokec9 "r"\cf4 \strokec4 )\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .file_username = \cf8 \strokec8 file\cf4 \strokec4 .readline()\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 test_username_equality\cf4 \strokec4 (\cf8 \strokec8 self\cf4 \strokec4 , \cf8 \strokec8 const_username\cf4 \strokec4 ):\cb1 \
\cb3         \cf5 \strokec5 return\cf4 \strokec4  \cf6 \strokec6 self\cf4 \strokec4 .file_username == \cf6 \strokec6 self\cf4 \strokec4 .username_arg \cf6 \strokec6 and\cf4 \strokec4  \cf6 \strokec6 self\cf4 \strokec4 .file_username == const_username\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 parse_args\cf4 \strokec4 (\cf8 \strokec8 self\cf4 \strokec4 , \cf8 \strokec8 args\cf4 \strokec4 ):\cb1 \
\cb3         namespace = \cf6 \strokec6 self\cf4 \strokec4 .parser.parse_args(\cf8 \strokec8 args\cf4 \strokec4 =args)\cb1 \
\cb3         \cf5 \strokec5 if\cf4 \strokec4  namespace:\cb1 \
\cb3             \cf6 \strokec6 self\cf4 \strokec4 .num_threads = \cf11 \strokec11 int\cf4 \strokec4 (_.get(namespace, \cf9 \strokec9 'num_threads'\cf4 \strokec4 , \cf10 \strokec10 1\cf4 \strokec4 ))\cb1 \
\cb3             \cf6 \strokec6 self\cf4 \strokec4 .username_arg = \cf11 \strokec11 str\cf4 \strokec4 (_.get(namespace, \cf9 \strokec9 'user'\cf4 \strokec4 , \cf6 \strokec6 None\cf4 \strokec4 ))\cb1 \
\cb3             \cf6 \strokec6 self\cf4 \strokec4 .part_id = \cf11 \strokec11 str\cf4 \strokec4 (_.get(namespace, \cf9 \strokec9 'part_id'\cf4 \strokec4 , \cf6 \strokec6 None\cf4 \strokec4 ))\cb1 \
\
\cb3     \cf6 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 add_arg_parser_argument\cf4 \strokec4 (\cf8 \strokec8 self\cf4 \strokec4 , \cf8 \strokec8 arg\cf4 \strokec4 ):\cb1 \
\cb3         \cf6 \strokec6 self\cf4 \strokec4 .parser.add_argument(arg[\cf10 \strokec10 0\cf4 \strokec4 ], \cf8 \strokec8 dest\cf4 \strokec4 =arg[\cf10 \strokec10 1\cf4 \strokec4 ], \cf8 \strokec8 default\cf4 \strokec4 =arg[\cf10 \strokec10 2\cf4 \strokec4 ], \cf8 \strokec8 help\cf4 \strokec4 =arg[\cf10 \strokec10 3\cf4 \strokec4 ])\cb1 \
\
}