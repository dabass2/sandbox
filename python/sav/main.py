import csv, argparse, requests, threading
from time import sleep
from datetime import datetime
from collections import Counter

'''
Reads the given input file which is heavily assumed to be a csv.
If the file has multiple lines, it will go line by line and add each
comma seperated date to the array. Before returning it creates a frequency
dictionary of the dates.
'''
def read_file(file_name):
  try:
    with open(file_name) as f:
      reader = csv.reader(f)
      return dict(Counter([[date for date in row] for row in reader][0]))
  except FileNotFoundError:
    print("File with name '{}' not found, check spelling and try again.".format(file_name))
    return None

'''
Function used by the threads to make the API call. Since multiple dates
can exist, it has to have a for loop to run them all. Also has basic error
catching and optional debugging info.
'''
def make_call(time, n, debug):
  for _ in range(n):
    try:
      req = requests.get("https://ifconfig.co")
      if debug:
        print("Call at {} ended with code {}".format(time, req.status_code))
    except Exception as e:
      if debug:
        print("Call at {} failed with error {}".format(time, e))
  return

'''
Main body of the code. Takes a frequency dictionary of dates and checks
every second if the current time is in the dictionary. If it is, it creates
a new thread to run the API call so as to not potentially keep up the next
loop iteration and possibly skip time.
'''
def main(freq, debug):
  print("Starting timer")
  while True:
    curr_time = datetime.now().strftime('%H:%M:%S')
    if debug:
      print("Current time:", curr_time)
    if (curr_time in freq.keys()):
      t = threading.Thread(target=make_call, args=(curr_time,freq[curr_time],debug))
      t.start() # Don't wait for the thread with thread.join, just have it end itself
    sleep(1)  # Sleeping for one second isn't perfect, but without it the loop goes much too fast

if __name__ == "__main__":
  # Simple argparse that takes in the file name of dates and an optional debug flag
  parser = argparse.ArgumentParser(description = 'A simple timed API caller.')
  parser.add_argument('--file', action='store', dest='file_name', default=None, required=True)
  parser.add_argument('--debug', action='store_true')
  args = parser.parse_args()

  freq_dict = read_file(args.file_name)
  if freq_dict:
    main(freq_dict, args.debug)