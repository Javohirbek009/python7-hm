# import threading

# def func():
#     for x in range(100):
#         print("salom")
# def func2():
#     for x in range(100):
#         print("javohir")

# func()
# func2()

# foo1 = threading.Thread(target=func)
# foo2 = threading.Thread(target=func2)


# foo1.start()
# foo2.start()



# def func():
#     for x in range(800):
#         print("hayr")
# def func2():
#     for x in range(65):
#         print("nematov")

# func()
# func2()

# foo3 = threading.Thread(target=func)
# foo4 = threading.Thread(target=func2)


# foo3.start()
# foo4.start()



# def func():
#     for x in range(40):
#         print("name")
# def func2():
#     for x in range(85):
#         print("lastname")

# func()
# func2()

# foo5 = threading.Thread(target=func)
# foo6 = threading.Thread(target=func2)


# foo5.start()
# foo6.start()



# import threading as jn

# event = jn.Event()

# def jarayon():
#     print("dastur o'rnatilsinmi")
#     event.wait()
#     print("dastur o'rnatilishi boshlandi")

# t1 = jn.Thread(target=jarayon)
# t1.start()

# sorov = input("dastur o'rnatilishiga rozimisiz?: ").lower()

# if sorov == 'ha':
#     event.set()


import time

def poyga():
    print("tayyorlaning...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("START")

poyga()