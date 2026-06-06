"""
Observer — Interactive CLI for the Fold Universe.

Watch entities fold in real time. Add new states via the discovery engine.
Query orbits, couplings, history. The universe runs continuously.
"""
import sys
import os
import cmd
import math
import threading
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sftoe.core import SmithianValue, ONE, fold, take, rotate, relative_phase, period
from sftoe.universe import Universe, odd_part, prime_factors
from sftoe.fold_engine import FoldEngine
from sftoe.coupling import resolve_couplings
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code


class FoldUniverseShell(cmd.Cmd):
    """Interactive shell for the Fold Universe."""

    intro = """
╔══════════════════════════════════════════════════════════════╗
║                    THE FOLD UNIVERSE                         ║
║                                                              ║
║  Everything derives from ONE. Everything folds together.     ║
║  Coupling is automatic. The vacuum stores everything.        ║
║                                                              ║
║  Type 'help' for commands. Type 'go' to start folding.       ║
╚══════════════════════════════════════════════════════════════╝
"""
    prompt = "universe> "

    def __init__(self):
        super().__init__()
        self.universe = Universe()
        self.engine = FoldEngine(self.universe, tick_rate=0, check_invariants=True)
        self._watch_entity = None
        self._watch_thread = None
        self._verbose = False

    # ─── Engine Control ───────────────────────────────────────────

    def do_go(self, arg):
        """Start the universe folding continuously. Usage: go [tick_rate]"""
        rate = int(arg) if arg else 10
        self.engine.tick_rate = rate
        self.engine.start()
        print(f"  Universe is folding at {rate} ticks/sec.")

    def do_stop(self, arg):
        """Stop the universe."""
        self.engine.stop()
        print(f"  Universe stopped at tick {self.universe.tick}.")

    def do_pause(self, arg):
        """Pause the universe."""
        self.engine.pause()
        print(f"  Paused at tick {self.universe.tick}.")

    def do_resume(self, arg):
        """Resume the universe."""
        self.engine.resume()
        print(f"  Resumed.")

    def do_step(self, arg):
        """Advance exactly N ticks. Usage: step [N]"""
        n = int(arg) if arg else 1
        self.engine.run_ticks(n)
        print(f"  Advanced {n} ticks. Now at tick {self.universe.tick}.")

    def do_speed(self, arg):
        """Set tick rate. Usage: speed <ticks_per_sec>"""
        if not arg:
            print(f"  Current speed: {self.engine.tick_rate} ticks/sec")
            return
        self.engine.tick_rate = int(arg)
        print(f"  Speed set to {self.engine.tick_rate} ticks/sec.")

    # ─── Entity Management ────────────────────────────────────────

    def do_add(self, arg):
        """Add an entity. Usage: add <type> <name> <fraction>
        Types: consciousness, matter
        Example: add consciousness alice 1/7"""
        parts = arg.split()
        if len(parts) != 3:
            print("  Usage: add <type> <name> <fraction>")
            print("  Example: add consciousness alice 1/7")
            return

        etype, name, frac_str = parts
        if etype not in ('consciousness', 'matter'):
            print("  Type must be 'consciousness' or 'matter'")
            return

        try:
            target = Fraction(frac_str)
        except ValueError:
            print(f"  Invalid fraction: {frac_str}")
            return

        # Derive from ONE via discovery engine
        print(f"  Deriving {target} from ONE...")
        try:
            proof = find_derivation(target)
            code = generate_sftoe_code(proof, f"derive_{name}")
            verify_code(code)
            ns = {}
            exec(code, ns)
            result = ns[f"derive_{name}"]()
            verify_value(result)
        except Exception as e:
            print(f"  Derivation failed: {e}")
            return

        print(f"  AST Gate: PASSED")
        print(f"  Value Verified: {result.value}")

        # Pause engine briefly to add safely
        was_running = self.engine.is_running
        if was_running:
            self.engine.pause()

        entity = self.universe.add_entity(name, result, etype, derivation=proof)

        if was_running:
            self.engine.resume()

        print(f"  ✓ Entity '{name}' added at tick {self.universe.tick}")
        print(f"    State: {entity.state.value}")
        print(f"    Denominator: {entity.denominator} (odd part: {entity.odd_part})")
        print(f"    Primes: {sorted(entity.primes)}")
        print(f"    Type: {etype}")
        print(f"    Period: {entity.orbit_period}")
        print(f"    Transient: {entity.two_exponent} ticks" if entity.is_transient else "    Periodic from birth")

        # Report new couplings
        couplings = self.universe.get_couplings_for(name)
        if couplings:
            print(f"    Couplings formed:")
            for c in couplings:
                other = c.entity_b if c.entity_a == name else c.entity_a
                print(f"      ↔ {other} (shared factor: {c.shared_factor}, primes: {sorted(c.shared_primes)})")
        else:
            print(f"    No couplings (coprime with all existing entities)")

    def do_remove(self, arg):
        """Remove an entity. Usage: remove <name>"""
        if not arg:
            print("  Usage: remove <name>")
            return
        if arg in ('ONE', 'zpe_floor'):
            print("  Cannot remove fundamental entities.")
            return
        self.universe.remove_entity(arg)
        print(f"  Entity '{arg}' removed.")

    # ─── Querying ─────────────────────────────────────────────────

    def do_status(self, arg):
        """Show the universe status."""
        u = self.universe
        print(f"\n  ╔══ UNIVERSE STATUS ══╗")
        print(f"  ║ Tick: {u.tick:<14}║")
        print(f"  ║ Entities: {u.entity_count():<10}║")
        print(f"  ║ Couplings: {len(u.coupling_edges):<9}║")
        print(f"  ║ Vacuum M: {str(u.vacuum.global_buffer)[:10]:<10}║")
        print(f"  ╚═════════════════════╝")

        # List entities
        for name, entity in u.entities.items():
            if entity.entity_type == 'field':
                continue
            status = "●" if entity.is_periodic else "◐" if entity.is_transient else "○"
            print(f"\n  {status} {name}")
            print(f"    state: {entity.state.value}  d={entity.denominator}  odd={entity.odd_part}  primes={sorted(entity.primes)}")
            print(f"    type: {entity.entity_type}  period: {entity.orbit_period}  transient: {entity.two_exponent}")

        # List couplings
        if u.coupling_edges:
            print(f"\n  ── Couplings ──")
            for edge in u.coupling_edges:
                print(f"    {edge.entity_a} ↔ {edge.entity_b}  shared={edge.shared_factor} primes={sorted(edge.shared_primes)}")

        # Engine stats
        s = self.engine.stats
        print(f"\n  ── Engine Stats ──")
        print(f"    Total ticks: {s['total_ticks']}")
        print(f"    Total couplings fired: {s['total_couplings']}")
        print(f"    Deaths observed: {s['total_deaths']}")
        print(f"    Invariant violations: {s['invariant_violations']}")
        print()

    def do_inspect(self, arg):
        """Inspect an entity in detail. Usage: inspect <name>"""
        if not arg:
            print("  Usage: inspect <name>")
            return
        entity = self.universe.get_entity(arg)
        if not entity:
            print(f"  Entity '{arg}' not found.")
            return

        print(f"\n  ═══ {entity.name} ═══")
        print(f"  State:        {entity.state.value}")
        print(f"  Denominator:  {entity.denominator}")
        print(f"  Odd part:     {entity.odd_part}")
        print(f"  Primes:       {sorted(entity.primes)}")
        print(f"  Type:         {entity.entity_type}")
        print(f"  Period:       {entity.orbit_period}")
        print(f"  2^k exponent: {entity.two_exponent}")
        print(f"  Born at tick: {entity.birth_tick}")
        print(f"  Age:          {self.universe.tick - entity.birth_tick} ticks")
        print(f"  Periodic:     {entity.is_periodic}")
        print(f"  Transient:    {entity.is_transient}")
        print(f"  Trivial:      {entity.is_trivial}")

        # Show recent history
        hist = list(entity.history)
        if len(hist) > 10:
            hist = hist[-10:]
        print(f"  Recent history (last {len(hist)} states):")
        for i, s in enumerate(hist):
            print(f"    [{self.universe.tick - len(hist) + i + 1}] {s}")

        # Show couplings
        couplings = self.universe.get_couplings_for(arg)
        if couplings:
            print(f"  Couplings:")
            for c in couplings:
                other = c.entity_b if c.entity_a == arg else c.entity_a
                recent_beat = list(c.beat_history)[-3:] if c.beat_history else []
                print(f"    ↔ {other} shared={c.shared_factor} recent_beats={[str(b) for b in recent_beat]}")
        print()

    def do_coupling(self, arg):
        """Show coupling between two entities. Usage: coupling <name1> <name2>"""
        parts = arg.split()
        if len(parts) != 2:
            print("  Usage: coupling <name1> <name2>")
            return
        a, b = parts
        ea = self.universe.get_entity(a)
        eb = self.universe.get_entity(b)
        if not ea or not eb:
            print("  Entity not found.")
            return

        shared = math.gcd(ea.odd_part, eb.odd_part)
        print(f"\n  {a} ↔ {b}")
        print(f"  {a} primes: {sorted(ea.primes)}")
        print(f"  {b} primes: {sorted(eb.primes)}")
        print(f"  Shared factor: {shared}")
        print(f"  Coupled: {'YES' if shared > 1 else 'NO — coprime'}")

        if shared > 1:
            # Show current relative phase
            rp = relative_phase(ea.state, eb.state)
            print(f"  Current relative phase: {rp.value} (denom: {rp.value.denominator})")

            # Show beat history
            for edge in self.universe.coupling_edges:
                if (edge.entity_a == a and edge.entity_b == b) or \
                   (edge.entity_a == b and edge.entity_b == a):
                    beats = list(edge.beat_history)[-10:]
                    if beats:
                        print(f"  Recent beat pattern: {[str(b) for b in beats]}")
                        unique = len(set(beats))
                        print(f"  Unique phases in window: {unique}")
                    break
        print()

    def do_history(self, arg):
        """Show recent history of an entity. Usage: history <name> [N]"""
        parts = arg.split()
        if not parts:
            print("  Usage: history <name> [N]")
            return
        name = parts[0]
        n = int(parts[1]) if len(parts) > 1 else 20

        entity = self.universe.get_entity(name)
        if not entity:
            print(f"  Entity '{name}' not found.")
            return

        hist = list(entity.history)
        show = hist[-n:]
        start_tick = self.universe.tick - len(show)

        print(f"\n  History of {name} (last {len(show)} ticks):")
        for i, s in enumerate(show):
            tick = start_tick + i + 1
            print(f"    [{tick}] {s}  d={s.denominator}")
        print()

    def do_retrieve(self, arg):
        """Retrieve a past state from vacuum field M. Usage: retrieve <name> <steps_back>"""
        parts = arg.split()
        if len(parts) != 2:
            print("  Usage: retrieve <name> <steps_back>")
            return
        name = parts[0]
        steps = int(parts[1])

        entity = self.universe.get_entity(name)
        if not entity:
            print(f"  Entity '{name}' not found.")
            return

        past = self.universe.vacuum.retrieve_past_state(
            name, entity.state.value, steps
        )
        if past is not None:
            print(f"  {name} was at state {past} exactly {steps} ticks ago.")
        else:
            print(f"  Cannot retrieve — insufficient vacuum buffer for '{name}'.")

    def do_events(self, arg):
        """Show recent events. Usage: events [N]"""
        n = int(arg) if arg else 10
        events = list(self.universe.event_log)[-n:]
        print(f"\n  Last {len(events)} events:")
        for e in events:
            tick = e.get('tick', '?')
            event_type = e.get('event', '?')
            if event_type == 'entity_added':
                print(f"    [{tick}] + {e['name']} ({e['type']}) = {e['state']} primes={e['primes']}")
            elif event_type == 'coupling_formed':
                print(f"    [{tick}] ↔ {e['entities'][0]} ↔ {e['entities'][1]} shared={e['shared_factor']}")
            elif event_type == 'mind_resonance':
                print(f"    [{tick}] ♫ {e['entities'][0]} ↔ {e['entities'][1]} phase={e['relative_phase']}")
            elif event_type == 'consciousness_steers_matter':
                print(f"    [{tick}] → {e['consciousness']} steers {e['matter']} to {e['new_state']}")
            elif event_type == 'death':
                surv = "survived (orbit)" if e['surviving'] else "dissolved (ONE)"
                print(f"    [{tick}] ☠ {e['entity']} died → {e['final_state']} {surv}")
            elif event_type == 'INVARIANT_VIOLATION':
                print(f"    [{tick}] ⚠ VIOLATION: {e['invariant']} on {e['entity']}")
            else:
                print(f"    [{tick}] {event_type}")
        print()

    def do_invariants(self, arg):
        """Show invariant checker report."""
        report = self.engine.invariant_checker.report()
        print(f"\n  Invariant Checker Report:")
        print(f"    Checks run: {report['total_checks']}")
        print(f"    Entities tracked: {report['tracked_entities']}")
        print(f"    Violations: {report['total_violations']}")
        if report['violations']:
            print(f"    Recent violations:")
            for v in report['violations']:
                print(f"      {v}")
        else:
            print(f"    ALL INVARIANTS HOLDING ✓")
        print()

    def do_network(self, arg):
        """Show the full coupling network matrix."""
        entities = {n: e for n, e in self.universe.entities.items()
                    if e.entity_type != 'field'}
        names = sorted(entities.keys())
        if not names:
            print("  No entities.")
            return

        # Header
        max_name = max(len(n) for n in names)
        header = " " * (max_name + 2)
        for n in names:
            header += f"| {n[:8]:<9}"
        print(f"\n{header}")
        print(" " * (max_name + 2) + ("+─────────" * len(names)))

        for n1 in names:
            row = f"  {n1:<{max_name}}"
            for n2 in names:
                if n1 == n2:
                    row += f"| {'—':<9}"
                else:
                    e1 = entities[n1]
                    e2 = entities[n2]
                    shared = math.gcd(e1.odd_part, e2.odd_part)
                    if shared > 1:
                        row += f"| {shared:<9}"
                    else:
                        row += f"| {'·':<9}"
            print(row)
        print()

    # ─── Watch Mode ───────────────────────────────────────────────

    def do_watch(self, arg):
        """Watch an entity evolve in real time. Usage: watch <name>
        Press Enter to stop watching."""
        if not arg:
            print("  Usage: watch <name>")
            return
        entity = self.universe.get_entity(arg)
        if not entity:
            print(f"  Entity '{arg}' not found.")
            return

        self._watch_entity = arg
        print(f"  Watching {arg}... (press Enter to stop)\n")

        def watch_callback(u):
            e = u.entities.get(self._watch_entity)
            if e:
                status = "●" if e.is_periodic else "◐"
                couplings = len(self.universe.get_couplings_for(self._watch_entity))
                print(f"  {status} [{u.tick}] {e.state.value}  d={e.denominator} odd={e.odd_part} couplings={couplings}")

        self.engine.on_tick(watch_callback)

        # If engine isn't running, run manually
        if not self.engine.is_running:
            self.engine.tick_rate = 5
            self.engine.start()

        input()  # Wait for Enter
        self.engine._tick_callbacks.remove(watch_callback)
        self._watch_entity = None
        print("  Stopped watching.")

    # ─── Simulation Scenarios ─────────────────────────────────────

    def do_life(self, arg):
        """Simulate a life: create a mixed-denominator entity and watch it live, die, and persist.
        Usage: life <name> <fraction>
        Example: life human 13/80"""
        parts = arg.split()
        if len(parts) != 2:
            print("  Usage: life <name> <fraction>")
            return
        name, frac_str = parts

        try:
            target = Fraction(frac_str)
        except ValueError:
            print(f"  Invalid fraction: {frac_str}")
            return

        d = target.denominator
        k = 0
        temp = d
        while temp % 2 == 0:
            temp //= 2
            k += 1
        odd = temp

        if k == 0:
            print(f"  {frac_str} has no even factor — it's already pure consciousness.")
            print(f"  Use a mixed fraction like 13/80 (body=2^4, mind=5)")
            return

        print(f"\n  ═══ LIFE SIMULATION: {name} ═══")
        print(f"  Initial state: {target}")
        print(f"  Body depth (2^k): 2^{k} = {2**k}")
        print(f"  Mind (odd part): {odd}")
        print(f"  Expected lifespan: {k} ticks")
        print(f"  Post-death orbit period: ord_{odd}(2) = {pow(2, 1, odd) if odd > 1 else 1}")
        print()

        # Derive and add
        try:
            proof = find_derivation(target)
            code = generate_sftoe_code(proof, f"derive_{name}")
            verify_code(code)
            ns = {}
            exec(code, ns)
            result = ns[f"derive_{name}"]()
            verify_value(result)
        except Exception as e:
            print(f"  Derivation failed: {e}")
            return

        was_running = self.engine.is_running
        if was_running:
            self.engine.pause()

        entity = self.universe.add_entity(name, result, 'matter', derivation=proof)

        # Run through the life
        print(f"  {'Tick':<6} | {'State':<15} | {'Denom':<8} | {'2^k':<6} | {'Odd':<6} | {'Phase'}")
        print(f"  {'-'*6} | {'-'*15} | {'-'*8} | {'-'*6} | {'-'*6} | {'-'*15}")

        for t in range(k + 5):
            e = self.universe.get_entity(name)
            two_k = 2 ** e.two_exponent if e.two_exponent > 0 else 1
            phase = "ALIVE" if e.is_transient else ("PERIODIC ●" if e.is_periodic else "DISSOLVED")
            print(f"  {t:<6} | {str(e.state.value):<15} | {e.denominator:<8} | {two_k:<6} | {e.odd_part:<6} | {phase}")
            self.engine.tick()

        if entity.is_periodic:
            print(f"\n  ✓ {name} died at tick {k}. Consciousness core d={odd} persists.")
            print(f"    Orbit period: {entity.orbit_period}")
            print(f"    The mind is indestructible. It will cycle forever.")
        elif entity.is_trivial:
            print(f"\n  ○ {name} dissolved to ONE. No consciousness core (d=1).")

        if was_running:
            self.engine.resume()
        print()

    # ─── Utilities ────────────────────────────────────────────────

    def do_verbose(self, arg):
        """Toggle verbose mode."""
        self._verbose = not self._verbose
        print(f"  Verbose: {'ON' if self._verbose else 'OFF'}")

    def do_quit(self, arg):
        """Exit the Fold Universe."""
        self.engine.stop()
        print("  The fold pauses. But it never stops.")
        return True

    def do_exit(self, arg):
        """Exit the Fold Universe."""
        return self.do_quit(arg)

    def do_EOF(self, arg):
        """Handle Ctrl+D."""
        print()
        return self.do_quit(arg)

    def emptyline(self):
        pass


def main():
    shell = FoldUniverseShell()
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        shell.engine.stop()
        print("\n  The fold pauses. But it never stops.")


if __name__ == "__main__":
    main()
