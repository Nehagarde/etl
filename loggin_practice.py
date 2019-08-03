"""__file__ => current file
   if getlogger is notprovided with a name then by default it takes the name as root

"""
import logging
import traceback

logging.basicConfig(filename="mylog.log",filemode='a+',format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__file__)

print("logging.CRITICAL",logging.CRITICAL)
logger.setLevel(logging.WARNING)

if __name__ == '__main__':
    try:
        l = [1,23,10]
        print(l[100])
    except Exception as e:
        logger.critical(traceback.format_exc())