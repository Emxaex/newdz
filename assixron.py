import asyncio

async def green_light():
    print('Зелёный свет')
    await asyncio.sleep(2)
async def yellow_light():
    print('Жёлтый свет')
    await asyncio.sleep(1)
async def red_light():
    print('Красный свет')
    await asyncio.sleep(3)

async def main():
    await yellow_light()
    await green_light()
    await red_light()
asyncio.run(main())