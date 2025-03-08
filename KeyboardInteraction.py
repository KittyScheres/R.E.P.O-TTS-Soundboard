import keyboard
import time

# Constants
T = 20
W = 17
A = 30
S = 31
D = 32
Q = 16
LSHIFT = 42
CTRL = 29
ENTER = 28
ESCAPE = 1

# Simulate the pressing of a key
def SimulateKeyPress(scanCode: int):
    keyboard.press(scanCode)
    keyboard.release(scanCode)
    time.sleep(0.01)

# Releases all currently pressed keys for the game input
def SuspendGameplayInputs():
    keyboard.block_key(W)
    keyboard.block_key(A)
    keyboard.block_key(S)
    keyboard.block_key(D)
    keyboard.block_key(Q)
    keyboard.block_key(LSHIFT)
    keyboard.block_key(CTRL)

# Get key states out of suspense
def UnSuspendGameplayInputs():
    keyboard.unblock_key(W)
    keyboard.unblock_key(A)
    keyboard.unblock_key(S)
    keyboard.unblock_key(D)
    keyboard.unblock_key(Q)
    keyboard.unblock_key(LSHIFT)
    keyboard.unblock_key(CTRL)