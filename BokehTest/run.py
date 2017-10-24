import testClass
from threading import Thread

testRun = testClass.TestRun()
thread = Thread(target=testRun.run)
thread.start()