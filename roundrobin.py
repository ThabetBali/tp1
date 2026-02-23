import threading
import time


def task(name: str, duration: float):
    """Simulate a task that runs for `duration` seconds."""
    print(f"[{name}] starting, will take {duration} seconds")
    time.sleep(duration)
    print(f"[{name}] finished")


def main():
    durations = {"Task1": 10, "Task2": 15} 
    quantum = 2 
    start_time = time.time()
    third_arrival = start_time + 3  

    print("Starting round-robin scheduling (no repetition, slice=2s)")
    try:
        while True:
            if time.time() >= third_arrival and "Task3" not in durations:
                durations["Task3"] = 12
                print("[Task3] has arrived with 12s runtime")

            if all(remaining <= 0 for remaining in durations.values()):
                break

            for name in list(durations.keys()):
                remaining = durations[name]
                if remaining <= 0:
                    continue

                slice_time = min(quantum, remaining)
                print(f"[{name}] running for {slice_time}s slice (remaining before: {remaining})")
                time.sleep(slice_time)
                durations[name] -= slice_time
                print(f"[{name}] slice complete (remaining after: {durations[name]})")

    except KeyboardInterrupt:
        print("Interrupted by user, stopping scheduling")

    print("All tasks completed")


if __name__ == "__main__":
    main()
