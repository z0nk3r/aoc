import os
import sys
import time
import requests
import datetime
import dateutil.tz

# ported from https://github.com/morgoth1145/advent-of-code/blob/8c17e50b4067d00a5ccc0753b1a0a7289e3f20e5/lib/aoc.py

_s = requests.Session()

_s.headers.update({
    'User-Agent': 'github.com/z0nk3r'
})

def forget_cookie():
    del _s.cookies['session']

def load_cookie(bad):
    cookie_file = "cookie.txt"
    if not os.path.exists(cookie_file) or bad == True:
        prompt = '''
    Copy/Paste Cookie from the AoC Website
    After Logging into AoC:
    Chrome: Right-click Page > Inspect > Application > Storage > Cookies > Website > Value
    (It's a SHA-512, 128 chars long) (Cookie will Cache locally, should only have to do this once per login)

    => '''
        cookie = input(prompt)
        cfile = open(cookie_file, "w")
        cfile.write(cookie)
        cfile.close()
    
    with open(cookie_file) as cfile:
        rcookie = cfile.readline().rstrip("\n")
    _s.cookies['session'] = rcookie

def session_get_file(dest, url):
    notLoggedInErr = 'Puzzle inputs differ by user.  Please log in to get your puzzle input.'
    tooEarlyErr = 'Please don\'t repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available.'
    
    destfile = open(dest, "wb")
    r = _s.get(url)
    if r.status_code != 400:
        # There isn't a client error so we *should* be logged in?
        r.raise_for_status()
        destfile.write(r.content)
        destfile.close()
        
        destfile = open(dest, "r")
        contents = destfile.readline().rstrip('\n')
        destfile.close()
        if contents != notLoggedInErr and contents != tooEarlyErr:
            # The contents are good! (I think)
            print("Download Complete!")
            return True
    
    return False

def get_input(year, day):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    dest = f'{year}/{day:02}/input'

    if not os.path.exists(f'{year}'):
        os.makedirs(f'{year}')
    if not os.path.exists(f'{year}/{day:02}'):
        os.makedirs(f'{year}/{day:02}')

    load_cookie(False)
    bad_counter = 0
    while (not session_get_file(dest, url)):
        # The session cookie may be invalid?
        os.unlink(dest) # delete file
        forget_cookie()
        load_cookie(True)
        time.sleep(2)  # avoid potential rate limit
        bad_counter += 1
        if bad_counter == 5:
            print("Bad Puzzle Input Get - Try Again Later")
            break

def time_to_release(year, day):
    # Puzzles release at midnight EST (UTC-5)
    release_time = datetime.datetime(year=year,
                                     month=12,
                                     day=day,
                                     hour=5,
                                     tzinfo=dateutil.tz.tzutc())
    now = datetime.datetime.now(dateutil.tz.tzutc())
    return release_time - now

def print_countdown(to_wait_seconds):
    days = int(to_wait_seconds//86400)
    hrs = int((to_wait_seconds - (days*86400))//3600)
    mins = int((to_wait_seconds - (days*86400) - (hrs*3600))//60)
    secs = int((to_wait_seconds - (days*86400) - (hrs*3600) - mins*60))
    print(f'\r [X] {days:4}D, {hrs:02}H, {mins:02}M, {secs:02}S until Puzzle is Available. Waiting... ', end="", flush=True)

def download_input_when_live(year, day):
    # Download 4 seconds after release
    to_wait = time_to_release(year, day) + datetime.timedelta(seconds=4)
    to_wait_seconds = int(to_wait.total_seconds())

    while to_wait_seconds > 0:
        time.sleep(1)
        to_wait_seconds -= 1
        print_countdown(to_wait_seconds)
        
        if (to_wait_seconds % 300) == 0:  # every 5 minutes
            # repeat these here for potential drift of time
            to_wait = time_to_release(year, day) + datetime.timedelta(seconds=4)
            to_wait_seconds = int(to_wait.total_seconds())

    print(f'\nDownloading Puzzle Input for {year} Day {day} to ', end="")
    print(f'\"{os.getcwd()}/{year}/{day:02}/input\"')
    get_input(year, day)

def main():
    if len(sys.argv) != 3:
        print("Not all arguments provided")
        print("\nUsage:\n\n  $> python3 aoc_get_input.py <year> <day>\n")
        return

    year = int(sys.argv[1])
    day = int(sys.argv[2])
    if (2030 > year > 2015 and 0 < day < 26):
        try:
            download_input_when_live(year, day)
        except KeyboardInterrupt:
            print("\nQuitting!")
    else:
        print(f"Invalid Year Day Arguments: {year} {day}")
        print("\nUsage:\n\n  $> python3 aoc_get_input.py <year> <day>\n")

if __name__ == "__main__":
    main()