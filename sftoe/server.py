"""
SFTOE Server — HTTP file server + WebSocket universe engine.

http://localhost:8080  → visualizer
ws://localhost:8765    → live universe data

The universe runs at the speed exact arithmetic allows.
No corners cut. Every tick is complete.
"""
import asyncio
import json
import os
import time
import http.server
import threading
from sftoe.fold_engine import FoldEngine

VISUALIZER_DIR = os.path.join(os.path.dirname(__file__), 'visualizer')


class VisualizerHTTPHandler(http.server.SimpleHTTPRequestHandler):
    """Serves the visualizer static files."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=VISUALIZER_DIR, **kwargs)

    def log_message(self, format, *args):
        pass  # Silence HTTP logs


class UniverseServer:
    def __init__(self, depth=None, ws_host='localhost', ws_port=8765,
                 http_host='localhost', http_port=8080):
        self.engine = FoldEngine(depth=depth)  # defaults to COVERING_DEPTH=5
        self.ws_host = ws_host
        self.ws_port = ws_port
        self.http_host = http_host
        self.http_port = http_port
        self.clients = set()
        self.speed = 1    # ticks per broadcast
        self.paused = False

    def start_http_server(self):
        """Start HTTP server in a background thread."""
        handler = VisualizerHTTPHandler
        httpd = http.server.HTTPServer((self.http_host, self.http_port), handler)
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        return httpd

    async def broadcast(self, message):
        if self.clients:
            dead = set()
            for ws in list(self.clients):
                try:
                    await ws.send(message)
                except Exception:
                    dead.add(ws)
            self.clients -= dead

    async def handle_ws(self, websocket):
        self.clients.add(websocket)
        print(f"[SFTOE] Client connected. Total: {len(self.clients)}")
        try:
            await websocket.send(json.dumps(self.engine.snapshot()))
            async for message in websocket:
                try:
                    cmd = json.loads(message)
                    await self.handle_command(cmd, websocket)
                except json.JSONDecodeError:
                    pass
        finally:
            self.clients.discard(websocket)
            print(f"[SFTOE] Client disconnected. Total: {len(self.clients)}")

    async def handle_command(self, cmd, websocket):
        action = cmd.get('action', '')
        if action == 'pause':
            self.paused = True
            print("[SFTOE] ⏸ Paused")
        elif action == 'play':
            self.paused = False
            print("[SFTOE] ▶ Playing")
        elif action == 'step':
            self.engine.tick()
            await self.broadcast(json.dumps(self.engine.snapshot()))
        elif action in ('set_speed', 'speed'):
            # Speed controls ticks per broadcast, capped reasonably
            self.speed = max(1, min(100, cmd.get('speed', 1)))
            print(f"[SFTOE] Speed: {self.speed} ticks/broadcast")
        elif action == 'seed':
            self.engine.seed_particles(
                cmd.get('leptons', 3), cmd.get('quarks', 6))
            await self.broadcast(json.dumps(self.engine.snapshot()))
        elif action == 'snapshot':
            await websocket.send(json.dumps(self.engine.snapshot()))

    async def engine_loop(self):
        print(f"[SFTOE] Seeding particles...")
        self.engine.seed_particles()
        n = len(self.engine.universe.alive_particles())
        print(f"[SFTOE] {n} particles ready. Universe running.")

        loop = asyncio.get_event_loop()
        tick_count = 0

        while True:
            if not self.paused:
                t0 = time.monotonic()

                # Run exactly 1 tick in a thread so the event loop
                # stays responsive for WebSocket connections/messages.
                # The physics takes as long as exact arithmetic needs.
                await loop.run_in_executor(None, self.engine.tick)

                dt = time.monotonic() - t0
                tick_count += 1

                # Log every 20 ticks
                if tick_count % 20 == 0:
                    fps = 1.0 / dt if dt > 0 else 0
                    print(f"[SFTOE] tick={self.engine.universe.tick} "
                          f"{dt*1000:.0f}ms ({fps:.1f} fps)")

                snapshot = json.dumps(self.engine.snapshot())
                await self.broadcast(snapshot)

                # Yield to process WS messages
                await asyncio.sleep(0.01)
            else:
                await asyncio.sleep(0.1)

    async def start(self):
        import websockets

        # Start HTTP server for visualizer
        self.start_http_server()

        size = self.engine.universe.size
        sites = self.engine.universe.lattice.total_sites

        print()
        print(f"  ╔═══════════════════════════════════════════╗")
        print(f"  ║     SMITHIAN FOLD UNIVERSE                ║")
        print(f"  ╠═══════════════════════════════════════════╣")
        print(f"  ║  Depth: {self.engine.universe.depth} (derived)                    ║")
        print(f"  ║  Lattice: {size}³ = {sites} sites{' '*(17-len(str(sites)))}║")
        print(f"  ║  Floor: 1/{size} = s_{self.engine.universe.depth}                       ║")
        print(f"  ║                                           ║")
        print(f"  ║  ▸ Open: http://{self.http_host}:{self.http_port}{' '*(26-len(str(self.http_port)))}║")
        print(f"  ║  ▸ WS:   ws://{self.ws_host}:{self.ws_port}{' '*(26-len(str(self.ws_port)))}║")
        print(f"  ║                                           ║")
        print(f"  ║  All arithmetic: Fraction (exact rational) ║")
        print(f"  ║  No floats. No irrationals. No zero.      ║")
        print(f"  ╚═══════════════════════════════════════════╝")
        print()

        async with websockets.serve(self.handle_ws, self.ws_host, self.ws_port):
            await self.engine_loop()


def run_server(depth=None, host='localhost', ws_port=8765, http_port=8080):
    server = UniverseServer(depth=depth, ws_host=host, ws_port=ws_port,
                            http_host=host, http_port=http_port)
    asyncio.run(server.start())


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='SFTOE Universe Server')
    parser.add_argument('--depth', type=int, default=None,
                        help='Lattice depth (default: 5, derived from covering)')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--ws-port', type=int, default=8765, help='WebSocket port')
    parser.add_argument('--http-port', type=int, default=8080, help='HTTP port')
    args = parser.parse_args()
    run_server(depth=args.depth, host=args.host,
               ws_port=args.ws_port, http_port=args.http_port)
