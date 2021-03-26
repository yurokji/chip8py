from renderer import Renderer

renderer = Renderer(10)

loop = True
fps = 60
fpsInterval = startTime = now = then = elapsed = 0

def TimestampMillisec64():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)

def init():
    fpsInterval = 1000 / fps
    then = TimestampMillisec64()
    startTime = then
    loop = True

def step():
    now = TimestampMillisec64()
    elapted = now - then
    if elapsed > fpsInterval:
        pass

    loop = True