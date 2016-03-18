import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(asyncio.wait([hello(),hello(),hello(),hello(),hello(),hello()]))
loop.close()