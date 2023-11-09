import re

import trio
import httpx


async def main():
    origin = "http://202.38.93.111:10021"
    client = httpx.AsyncClient()
    session = input("session cookie: ")
    client.cookies.set("session", session, "202.38.93.111")

    r = await client.post(f"{origin}/api/getMessages")
    r.raise_for_status()
    res_json = r.json()
    messages = res_json["messages"]

    start_time = trio.current_time()

    for i, msg in enumerate(messages):
        if not re.search(r"hack\[\w+\]", msg["text"]):
            continue

        await trio.sleep_until(start_time + msg["delay"])
        r = await client.post(f"{origin}/api/deleteMessage", json={"id": i})
        r.raise_for_status()
        success = r.json()["success"]

        print(f"delete message {i} ", end="")
        if success:
            print("done")
        else:
            print(f"*failed*: {r.json()['error']}")

    await trio.sleep(2)
    r = await client.post(f"{origin}/api/getflag")
    try:
        r.raise_for_status()
    except httpx.HTTPError:
        print(r)
        print(r.headers)
        print(r.text)
    else:
        print(r.json())


trio.run(main)
