import asyncio, time

# async def square(number: int) -> int:
#     return number*number

# async def main() -> None:

#     # result = asyncio.run(square(10))
#     x = await square(10)
#     y = await square(20)

#     print(x+y)

async def brew_coffee(delay = 10):
    print("Brewing Coffee...")
    await asyncio.sleep(delay)
    # time.sleep(delay)
    print("Coffee Brewed")

async def toast_bagel(delay = 5):
    print("Toasting Bagel...")
    await asyncio.sleep(delay)
    # time.sleep(delay)
    print("Bagel Toasted")

async def main():
    start = time.perf_counter()

    # coffee_task = brew_coffee()
    # bagel_task = toast_bagel()

    coffee_task = asyncio.create_task(brew_coffee())
    bagel_task = asyncio.create_task(toast_bagel())
    result_coffee = await coffee_task
    result_bagel = await bagel_task
    
    end = time.perf_counter()
    
    # print(result_coffee)
    # print(result_bagel)
    print(f'It took {round(end-start,0)} second(s) to complete.')

if __name__ == "__main__":
    asyncio.run(main())
    # main()