"""
Load-balancing broker
Based on the load balancer of the zeromq guide by Brandon Carpenter
"""
import zmq


def main():
    """Load balancer main loop."""
    # Prepare context and sockets
    context = zmq.Context.instance()
    frontend = context.socket(zmq.ROUTER)
    frontend.bind("tcp://127.0.0.1:5555")
    backend = context.socket(zmq.ROUTER)
    backend.bind("tcp://127.0.0.1:5556")

    # Initialize main loop state
    workers = []
    poller = zmq.Poller()
    # Only poll for requests from backend until workers are available
    poller.register(backend, zmq.POLLIN)

    while True:
        event = dict(poller.poll())

        if backend in event:
            print("Got backend event")
            request = backend.recv_multipart()
            worker, empty, client = request[:3]

            if not workers:
                poller.register(frontend, zmq.POLLIN)

            workers.append(worker)

            if client != b'READY' and len(request) > 3:
                empty, reply = request[3:]
                frontend.send_multipart([client, b"", reply])

        if frontend in event:
            print("Got frontend event")
            client, empty, request = frontend.recv_multipart()
            worker = workers.pop(0)
            backend.send_multipart([worker, b"", client, b"", request])

            if not workers:
                poller.unregister(frontend)

    backend.close()
    frontend.close()
    context.term()

if __name__ == "__main__":
    main()
