{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red23\green23\blue23;\red202\green202\blue202;
\red183\green111\blue179;\red167\green197\blue152;\red70\green137\blue204;\red67\green192\blue160;\red212\green214\blue154;
\red140\green211\blue254;\red194\green126\blue101;\red205\green173\blue106;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c77255\c52549\c75294;\cssrgb\c70980\c80784\c65882;\cssrgb\c33725\c61176\c83922;\cssrgb\c30588\c78824\c69020;\cssrgb\c86275\c86275\c66667;
\cssrgb\c61176\c86275\c99608;\cssrgb\c80784\c56863\c47059;\cssrgb\c84314\c72941\c49020;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Based on code from https://github.com/Nohclu/Sleeping-Barber-Python-3.6-/blob/master/barber.py\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  time\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  random\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  threading\cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  queue \cf5 \strokec5 import\cf4 \strokec4  Queue\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 CUSTOMERS_SEATS = \cf6 \strokec6 15\cf4 \strokec4         \cf2 \strokec2 # Number of seats in BarberShop\cf4 \cb1 \strokec4 \
\cb3 BARBERS = \cf6 \strokec6 3\cf4 \strokec4                 \cf2 \strokec2 # Number of Barbers working\cf4 \cb1 \strokec4 \
\cb3 EVENT = threading.Event()   \cf2 \strokec2 # Event flag, keeps track of Barber/Customer interactions\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 global\cf4 \strokec4  Earnings\cb1 \
\cf7 \cb3 \strokec7 global\cf4 \strokec4  SHOP_OPEN\cb1 \
\
\
\cf7 \cb3 \strokec7 class\cf4 \strokec4  \cf8 \strokec8 Customer\cf4 \strokec4 (\cf8 \strokec8 threading\cf4 \strokec4 .\cf8 \strokec8 Thread\cf4 \strokec4 ):       \cf2 \strokec2 # Producer Thread\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 __init__\cf4 \strokec4 (\cf10 \strokec10 self\cf4 \strokec4 , \cf10 \strokec10 queue\cf4 \strokec4 ):          \cf2 \strokec2 # Constructor passes Global Queue (all_customers) to Class\cf4 \cb1 \strokec4 \
\cb3         threading.Thread.\cf9 \strokec9 __init__\cf4 \strokec4 (\cf7 \strokec7 self\cf4 \strokec4 )\cb1 \
\cb3         \cf7 \strokec7 self\cf4 \strokec4 .queue = queue\cb1 \
\cb3         \cf7 \strokec7 self\cf4 \strokec4 .rate = \cf7 \strokec7 self\cf4 \strokec4 .what_customer()\cb1 \
\
\cb3     \cf9 \strokec9 @\cf8 \strokec8 staticmethod\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 what_customer\cf4 \strokec4 ():\cb1 \
\cb3         customer_types = [\cf11 \strokec11 "adult"\cf4 \strokec4 , \cf11 \strokec11 "senior"\cf4 \strokec4 , \cf11 \strokec11 "student"\cf4 \strokec4 , \cf11 \strokec11 "child"\cf4 \strokec4 ]\cb1 \
\cb3         customer_rates = \{\cf11 \strokec11 "adult"\cf4 \strokec4 : \cf6 \strokec6 16\cf4 \strokec4 ,\cb1 \
\cb3                           \cf11 \strokec11 "senior"\cf4 \strokec4 : \cf6 \strokec6 7\cf4 \strokec4 ,\cb1 \
\cb3                           \cf11 \strokec11 "student"\cf4 \strokec4 : \cf6 \strokec6 10\cf4 \strokec4 ,\cb1 \
\cb3                           \cf11 \strokec11 "child"\cf4 \strokec4 : \cf6 \strokec6 7\cf4 \strokec4 \}\cb1 \
\cb3         t = random.choice(customer_types)\cb1 \
\cb3         \cf9 \strokec9 print\cf4 \strokec4 (t + \cf11 \strokec11 " rate."\cf4 \strokec4 )\cb1 \
\cb3         \cf5 \strokec5 return\cf4 \strokec4  customer_rates[t]\cb1 \
\
\cb3     \cf7 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 run\cf4 \strokec4 (\cf10 \strokec10 self\cf4 \strokec4 ):\cb1 \
\cb3         \cf5 \strokec5 if\cf4 \strokec4  \cf7 \strokec7 not\cf4 \strokec4  \cf7 \strokec7 self\cf4 \strokec4 .queue.full():  \cf2 \strokec2 # Check queue size\cf4 \cb1 \strokec4 \
\cb3             EVENT.set()  \cf2 \strokec2 # Sets EVENT flag to True i.e. Customer available in the Queue\cf4 \cb1 \strokec4 \
\cb3             EVENT.clear()  \cf2 \strokec2 # A lerts Barber that their is a Customer available in the Queue\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 else\cf4 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 # If Queue is full, Customer leaves.\cf4 \cb1 \strokec4 \
\cb3             \cf9 \strokec9 print\cf4 \strokec4 (\cf11 \strokec11 "Queue full, customer has left."\cf4 \strokec4 )\cb1 \
\
\cb3     \cf7 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 trim\cf4 \strokec4 (\cf10 \strokec10 self\cf4 \strokec4 ):\cb1 \
\cb3         \cf9 \strokec9 print\cf4 \strokec4 (\cf11 \strokec11 "Customer haircut started."\cf4 \strokec4 )\cb1 \
\cb3         a = \cf6 \strokec6 3\cf4 \strokec4  * random.random()  \cf2 \strokec2 # Retrieves random number.\cf4 \cb1 \strokec4 \
\cb3         time.sleep(a)\cb1 \
\cb3         \cf2 \strokec2 # \cf7 \strokec7 TODO\cf2 \strokec2  execute the time sleep function with a, which simulates the time it takes for a barber to give a haircut.\cf4 \cb1 \strokec4 \
\cb3         payment = \cf7 \strokec7 self\cf4 \strokec4 .rate\cb1 \
\cb3         \cf2 \strokec2 # Barber finished haircut.\cf4 \cb1 \strokec4 \
\cb3         \cf9 \strokec9 print\cf4 \strokec4 (\cf11 \strokec11 "Haircut finished. Haircut took \cf7 \strokec7 \{\}\cf11 \strokec11 "\cf4 \strokec4 .format(a))\cb1 \
\cb3         \cf7 \strokec7 global\cf4 \strokec4  Earnings\cb1 \
\cb3         Earnings += payment\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 class\cf4 \strokec4  \cf8 \strokec8 Barber\cf4 \strokec4 (\cf8 \strokec8 threading\cf4 \strokec4 .\cf8 \strokec8 Thread\cf4 \strokec4 ):     \cf2 \strokec2 # Consumer Thread\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 __init__\cf4 \strokec4 (\cf10 \strokec10 self\cf4 \strokec4 , \cf10 \strokec10 queue\cf4 \strokec4 ):      \cf2 \strokec2 # Constructor passes Global Queue (all_customers) to Class\cf4 \cb1 \strokec4 \
\cb3         threading.Thread.\cf9 \strokec9 __init__\cf4 \strokec4 (\cf7 \strokec7 self\cf4 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 # \cf7 \strokec7 TODO\cf2 \strokec2  set this class's queue property to the passed value\cf4 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 self\cf4 \strokec4 .sleep = \cf7 \strokec7 True\cf4 \strokec4    \cf2 \strokec2 # No Customers in Queue therefore Barber sleeps by default\cf4 \cb1 \strokec4 \
\
\cb3     \cf7 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 is_empty\cf4 \strokec4 (\cf10 \strokec10 self\cf4 \strokec4 ):  \cf2 \strokec2 # Simple function that checks if there is a customer in the Queue and if so\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 if\cf4 \strokec4  \cf7 \strokec7 self\cf4 \strokec4 .queue.empty():\cb1 \
\cb3             \cf7 \strokec7 self\cf4 \strokec4 .sleep = \cf7 \strokec7 True\cf4 \strokec4    \cf2 \strokec2 # If nobody in the Queue Barber sleeps.\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 else\cf4 \strokec4 :\cb1 \
\cb3             \cf7 \strokec7 self\cf4 \strokec4 .sleep = \cf7 \strokec7 False\cf4 \strokec4   \cf2 \strokec2 # Else he wakes up.\cf4 \cb1 \strokec4 \
\cb3         \cf9 \strokec9 print\cf4 \strokec4 (\cf11 \strokec11 "------------------\cf12 \strokec12 \\n\cf11 \strokec11 Barber sleep \cf7 \strokec7 \{\}\cf12 \strokec12 \\n\cf11 \strokec11 ------------------"\cf4 \strokec4 .format(\cf7 \strokec7 self\cf4 \strokec4 .sleep))\cb1 \
\
\cb3     \cf7 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 run\cf4 \strokec4 (\cf10 \strokec10 self\cf4 \strokec4 ):\cb1 \
\cb3         \cf7 \strokec7 global\cf4 \strokec4  SHOP_OPEN\cb1 \
\cb3         \cf5 \strokec5 while\cf4 \strokec4  SHOP_OPEN:\cb1 \
\cb3             \cf5 \strokec5 while\cf4 \strokec4  \cf7 \strokec7 self\cf4 \strokec4 .queue.empty():\cb1 \
\cb3                 \cf2 \strokec2 # Waits for the Event flag to be set, Can be seen as the Barber Actually sleeping.\cf4 \cb1 \strokec4 \
\cb3                 EVENT.wait()\cb1 \
\cb3                 \cf9 \strokec9 print\cf4 \strokec4 (\cf11 \strokec11 "Barber is sleeping..."\cf4 \strokec4 )\cb1 \
\cb3             \cf9 \strokec9 print\cf4 \strokec4 (\cf11 \strokec11 "Barber is awake."\cf4 \strokec4 )\cb1 \
\cb3             customer = \cf7 \strokec7 self\cf4 \strokec4 .queue\cb1 \
\cb3             \cf7 \strokec7 self\cf4 \strokec4 .is_empty()\cb1 \
\cb3             \cf2 \strokec2 # FIFO Queue So first customer added is gotten.\cf4 \cb1 \strokec4 \
\cb3             customer = customer.get()\cb1 \
\cb3             customer.trim()  \cf2 \strokec2 # Customers Hair is being cut\cf4 \cb1 \strokec4 \
\cb3             customer = \cf7 \strokec7 self\cf4 \strokec4 .queue\cb1 \
\cb3             \cf2 \strokec2 # \cf7 \strokec7 TODO\cf2 \strokec2  use the task_done function to complete cutting the customer's hair\cf4 \cb1 \strokec4 \
\cb3             customer.task_done()\cb1 \
\cb3             \cf9 \strokec9 print\cf4 \strokec4 (\cf7 \strokec7 self\cf4 \strokec4 .name)    \cf2 \strokec2 # Which Barber served the Customer\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 wait\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     time.sleep(\cf6 \strokec6 1\cf4 \strokec4  * random.random())\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf10 \strokec10 __name__\cf4 \strokec4  == \cf11 \strokec11 '__main__'\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     Earnings = \cf6 \strokec6 0\cf4 \cb1 \strokec4 \
\cb3     SHOP_OPEN = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3     barbers = []\cb1 \
\cb3     all_customers = Queue(CUSTOMERS_SEATS)  \cf2 \strokec2 # A queue of size Customer Seats\cf4 \cb1 \strokec4 \
\
\cb3     \cf5 \strokec5 for\cf4 \strokec4  b \cf5 \strokec5 in\cf4 \strokec4  \cf9 \strokec9 range\cf4 \strokec4 (BARBERS):\cb1 \
\cb3         \cf2 \strokec2 # \cf7 \strokec7 TODO\cf2 \strokec2  Pass the all_customers Queue to the Barber constructor\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 # Makes the Thread a super low priority thread allowing it to be terminated easier\cf4 \cb1 \strokec4 \
\cb3         b = Barber(all_customers)\cb1 \
\cb3         b.daemon = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3         b.start()   \cf2 \strokec2 # Invokes the run method in the Barber Class\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 # Adding the Barber Thread to an array for easy referencing later on.\cf4 \cb1 \strokec4 \
\cb3         barbers.append(b)\cb1 \
\cb3     \cf5 \strokec5 for\cf4 \strokec4  c \cf5 \strokec5 in\cf4 \strokec4  \cf9 \strokec9 range\cf4 \strokec4 (\cf6 \strokec6 10\cf4 \strokec4 ):  \cf2 \strokec2 # Loop that creates infinite Customers\cf4 \cb1 \strokec4 \
\cb3         \cf9 \strokec9 print\cf4 \strokec4 (\cf11 \strokec11 "----"\cf4 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 # Simple Tracker too see the qsize (NOT RELIABLE!)\cf4 \cb1 \strokec4 \
\cb3         \cf9 \strokec9 print\cf4 \strokec4 (all_customers.qsize())\cb1 \
\cb3         wait()\cb1 \
\cb3         c = Customer(all_customers)  \cf2 \strokec2 # Passing Queue object to Customer class\cf4 \cb1 \strokec4 \
\cb3         all_customers.put(c)    \cf2 \strokec2 # Puts the Customer Thread in the Queue\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 # \cf7 \strokec7 TODO\cf2 \strokec2  Invoke the run method in the Customer Class\cf4 \cb1 \strokec4 \
\cb3         c.start()\cb1 \
\cb3     all_customers.join()    \cf2 \strokec2 # Terminates all Customer Threads\cf4 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 print\cf4 \strokec4 (\cf11 \strokec11 "\'80"\cf4 \strokec4 +\cf8 \strokec8 str\cf4 \strokec4 (Earnings))\cb1 \
\cb3     SHOP_OPEN = \cf7 \strokec7 False\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 for\cf4 \strokec4  i \cf5 \strokec5 in\cf4 \strokec4  barbers:\cb1 \
\cb3         i.join()    \cf2 \strokec2 # Terminates all Barbers\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 # Program hangs due to infinite loop in Barber Class, use ctrl-z to exit.\cf4 \cb1 \strokec4 \
}