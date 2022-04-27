import asyncio


async def handle_connection(reader, writer):
    writer.write("Hello user, type something ...\n".encode())

    data=await reader.readuntil(b"\n")

    writer.write("\nYou sent: ".encode() + data)
    await writer.drain()

    #closing connection
    writer.close()
    await writer.wait_closed()

async def main():
    server=await asyncio.start_server(handle_connection, "0.0.0.0", 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
