"""
Розробіть сокет сервер з використанням бібліотеки asyncio. Сервер
повинен приймати два числа і проводити над ними прості арифметичні
функції - додавання, віднімання та множення - з використанням
користувацьких функцій, які працюють у асинхронному режимі.
"""
import asyncio
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5050))
sock.listen(5)
print('Server is running...')

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    decoded_data = data.decode('utf-8')
    numbers = decoded_data.split()
    numbers = [float(i) for i in numbers]
    print(f'Number 1: {numbers[0]}', f'Number 2: {numbers[1]}', sep='\n')

    async def add():
        print('Addition started')
        await asyncio.sleep(0)
        result = numbers[0] + numbers[1]
        print('Addition completed')
        return result

    async def sub():
        print('Subtraction started')
        await asyncio.sleep(0)
        result = numbers[0] - numbers[1]
        print('Subtraction completed')
        return result

    async def mult():
        print('Multiplication started')
        await asyncio.sleep(0)
        result = numbers[0] * numbers[1]
        print('Multiplication completed')
        return result

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(add()), ioloop.create_task(sub()), ioloop.create_task(mult())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)

    message = ['Addition: ' + str(tasks[0].result()), 'Subtraction: ' + str(tasks[1].result()),
               'Multiplication: ' + str(tasks[2].result())]
    message = '\n'.join(message)
    conn.send(bytes(message, encoding='utf-8'))
    conn.close()
