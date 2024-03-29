#! python3
"""
sushi go round bot
sushigoround.py - a bot program to automatically play the sushi go round flash game

"""

import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  .%(msecs)03d:%(message)s',datefmt='%H:%M:%S')

# food order constants(don't change these:the image filenames depend on these specific values)
ONIGIRI = 'onigiri'
GUNKAN_MAKI = 'gunkan_maki'
CALIFORNIA_ROLL = 'california_roll'
SALMON_ROLL = 'salmon_roll'
SHRIMP_SUSHI = 'shrimp_roll'
UNAGI_ROLL = 'unagi_roll'
DRAGON_ROLL = 'dragon_roll'
COMBO = 'combo'
ALL_ORDER_TYPES = (ONIGIRI, GUNKAN_MAKI, CALIFORNIA_ROLL, SALMON_ROLL, SHRIMP_SUSHI, UNAGI_ROLL, DRAGON_ROLL, COMBO)

# Ingredient constants (don't change these: the image filenames depend on these specific values)
SHRIMP = 'shrimp'
RICE = 'rice'
NORI = 'nori'
ROE = 'roe'
SALMON = 'salmon'
UNAGI = 'unagi'
RECIPE = {ONIGIRI:         {RICE: 2, NORI: 1},
          CALIFORNIA_ROLL: {RICE: 1, NORI: 1, ROE: 1},
          GUNKAN_MAKI:     {RICE: 1, NORI: 1, ROE: 2},
          SALMON_ROLL:     {RICE: 1, NORI: 1, SALMON: 2},
          SHRIMP_SUSHI:    {RICE: 1, NORI: 1, SHRIMP: 2},
          UNAGI_ROLL:      {RICE: 1, NORI: 1, UNAGI: 2},
          DRAGON_ROLL:     {RICE: 2, NORI: 1, ROE: 1, UNAGI: 2},
          COMBO:           {RICE: 2, NORI: 1, ROE: 1, SALMON: 1, UNAGI: 1, SHRIMP: 1},}


LEVEL_WIN_MESSAGE = 'win' # checkForGameOver() returns this value if the level has been won

# Settings
MIN_INGREDIENTS = 4 # if an ingredient gets below this value, order more
PLATE_CLEARING_FREQ = 8 # plates are cleared every this number of seconds, roughly
NORMAL_RESTOCK_TIME = 7 # the number of seconds it takes to restock inventory after ordering it (at normal speed, not express)
TIME_TO_REMAKE = 30 # if an order goes unfilled for this number of seconds, remake it

# Global variables
LEVEL = 1 # current level being played
INVENTORY = {SHRIMP: 5, RICE: 10,
             NORI: 10,  ROE: 10,
             SALMON: 5, UNAGI: 5}
GAME_REGION = () # (left, top, width, height) values coordinates of the game window
ORDERING_COMPLETE = {SHRIMP: None, RICE: None, NORI: None, ROE: None, SALMON: None, UNAGI: None} # unix timestamp when an ordered ingredient will have arrived
ROLLING_COMPLETE = 0 # unix timestamp of when the rolling of the mat will have completed
LAST_PLATE_CLEARING = 0 # unix timestamp of the last time the plates were cleared

# various coordinates of objects in the game
GAME_REGION = () # (left, top, width, height) values coordinates of the entire game window
INGRED_COORDS = None
PHONE_COORDS = None
TOPPING_COORDS = None
ORDER_BUTTON_COORDS = None
RICE1_COORDS = None
RICE2_COORDS = None
NORMAL_DELIVERY_BUTTON_COORDS = None
MAT_COORDS = None
LAST_GAME_OVER_CHECK = 0 # unix timestamp when we last checked for the Game Over or You Win messages



def main():
    """ runs the entire programe.the sushi go round game must be visible on the screen and the PLAY button visible. """
    logging.debug('Program started.press ctrl-c to abort at any time.')
    logging.debug('to interrupt mouse movement,move mouse to upper left corner.')
    getGameRegion()
    navigateStartGameMenu()
    setupCoordinates()
    startServing()

def imPath(filename):
    """a shortcut for joining the 'images/' file path,since it is used so often,return the filename with images/ prepended."""
    return os.path.join('images',filename)

def getGameRegion():
    """ Obtains the region that the Sushi Go Round game is on the screen and assigns it to GAME_REGION. The game must be at the start screen (where the PLAY button is visible)."""
     global GAME_REGION

     # identify the top-left corner
     logging.debug('finding game region...')
     region = pyautogui.locateOnScreen(imPath('top_right_corner.png'))
     if region is None:
         raise Exception('could not find game on screen.is the game visible?')

    # calculate the region of the entire game
    topRightX = region[0] + region[2]  # left + width
    topRightY = region[1]  # top
    GAME_REGION = (topRightX - 640,topRightY,640,480)  # the game screen is always 640 x 480
    logging.debug('game region found:%s' % (GAME_REGION,))


def setupCoordinates():
    """Sets several of the coordinate-related global variables, after acquiring the value for GAME_REGION."""
    global INGRED_COORDS, PHONE_COORDS, TOPPING_COORDS, ORDER_BUTTON_COORDS, RICE1_COORDS, RICE2_COORDS, NORMAL_DELIVERY_BUTTON_COORDS, MAT_COORDS, LEVEL
    INGRED_COORDS = {SHRIMP: (GAME_REGION[0] + 40, GAME_REGION[1] + 335),
                     RICE:   (GAME_REGION[0] + 95, GAME_REGION[1] + 335),
                     NORI:   (GAME_REGION[0] + 40, GAME_REGION[1] + 385),
                     ROE:    (GAME_REGION[0] + 95, GAME_REGION[1] + 385),
                     SALMON: (GAME_REGION[0] + 40, GAME_REGION[1] + 425),
                     UNAGI:  (GAME_REGION[0] + 95, GAME_REGION[1] + 425),}
    PHONE_COORDS = (GAME_REGION[0] + 560, GAME_REGION[1] + 360)
    TOPPING_COORDS = (GAME_REGION[0] + 513, GAME_REGION[1] + 269)
    ORDER_BUTTON_COORDS = {SHRIMP: (GAME_REGION[0] + 496, GAME_REGION[1] + 222),
                           UNAGI:  (GAME_REGION[0] + 578, GAME_REGION[1] + 222),
                           NORI:   (GAME_REGION[0] + 496, GAME_REGION[1] + 281),
                           ROE:    (GAME_REGION[0] + 578, GAME_REGION[1] + 281),
                           SALMON: (GAME_REGION[0] + 496, GAME_REGION[1] + 329),}
    RICE1_COORDS = (GAME_REGION[0] + 543, GAME_REGION[1] + 294)
    RICE2_COORDS = (GAME_REGION[0] + 545, GAME_REGION[1] + 269)

    NORMAL_DELIVERY_BUTTON_COORDS = (GAME_REGION[0] + 495, GAME_REGION[1] + 293)

    MAT_COORDS = (GAME_REGION[0] + 190, GAME_REGION[1] + 375)

    LEVEL = 1


def navigateStartGameMenu():
    """Performs the clicks to navigate form the start screen (where the PLAY button is visible) to the beginning of the first level."""
    # Click on everything needed to get past the menus at the start of the game.

    # click on Play
    logging.debug('Looking for Play button...')
    while True: # loop because it could be the blue or pink Play button displayed at the moment.
        pos = pyautogui.locateCenterOnScreen(imPath('play_button.png'), region=GAME_REGION)
        if pos is not None:
            break
    pyautogui.click(pos, duration=0.25)
    logging.debug('Clicked on Play button.')

    # click on Continue
    pos = pyautogui.locateCenterOnScreen(imPath('continue_button.png'), region=GAME_REGION)
    pyautogui.click(pos, duration=0.25)
    logging.debug('Clicked on Continue button.')

    # click on Skip
    logging.debug('Looking for Skip button...')
    while True: # loop because it could be the yellow or red Skip button displayed at the moment.
        pos = pyautogui.locateCenterOnScreen(imPath('skip_button.png'), region=GAME_REGION)
        if pos is not None:
            break
    pyautogui.click(pos, duration=0.25)
    logging.debug('Clicked on Skip button.')

    # click on Continue
    pos = pyautogui.locateCenterOnScreen(imPath('continue_button.png'), region=GAME_REGION)
    pyautogui.click(pos, duration=0.25)
    logging.debug('Clicked on Continue button.')


def startServing():
    """The main game playing function. This function handles all aspects of game play, including identifying orders, making orders, buying ingredients and other features."""
    global LAST_GAME_OVER_CHECK, INVENTORY, ORDERING_COMPLETE, LEVEL

    # Reset all game state variables.
    oldOrders = {}
    backOrders = {}
    remakeOrders = {}
    remakeTimes = {}
    LAST_GAME_OVER_CHECK = time.time()
    ORDERING_COMPLETE = {SHRIMP: None, RICE: None, NORI: None,
                         ROE: None, SALMON: None, UNAGI: None}
     while True:
        # Check for orders, see which are new and which are gone since last time.
        currentOrders = getOrders()
        added, removed = getOrdersDifference(currentOrders, oldOrders)
        if added != {}:
            logging.debug('New orders: %s' % (list(added.values())))
            for k in added:
                remakeTimes[k] = time.time() + TIME_TO_REMAKE
        if removed != {}:
            logging.debug('Removed orders: %s' % (list(removed.values())))
            for k in removed:
                del remakeTimes[k]
    # Check if the remake times have past, and add those to the remakeOrders dictionary.
        for k, remakeTime in copy.copy(remakeTimes).items():
            if time.time() > remakeTime:
                remakeTimes[k] = time.time() + TIME_TO_REMAKE # reset remake time
                remakeOrders[k] = currentOrders[k]
                logging.debug('%s added to remake orders.' % (currentOrders[k]))
        # Clear any finished plates.
        if random.randint(1, 10) == 1 or time.time() - PLATE_CLEARING_FREQ > LAST_PLATE_CLEARING:
            clickOnPlates()

        # Check if ingredient orders have arrived.
        updateInventory()

        # Go through and see if any back orders can be filled.
        for pos, order in copy.copy(backOrders).items():
            result = makeOrder(order)
            if result is None:
                del backOrders[pos] # remove from back orders
                logging.debug('Filled back order for %s.' % (order))

        # Go through and see if any remake orders can be filled.
        for pos, order in copy.copy(remakeOrders).items():
            if pos not in currentOrders:
                del remakeOrders[pos]
                logging.debug('Canceled remake order for %s.' % (order))
                continue
            result = makeOrder(order)
            if result is None:
                del remakeOrders[pos] # remove from remake orders
                logging.debug('Filled remake order for %s.' % (order))
        if random.randint(1, 5) == 1:
            # order any ingredients that are below the minimum amount
            for ingredient, amount in INVENTORY.items():
                if amount < MIN_INGREDIENTS:
                    orderIngredient(ingredient)
