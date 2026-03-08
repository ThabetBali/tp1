import time
import tkinter as tk


def main():
    runtimes = {"T1": 2, "T2": 3, "T3": 5}
    periods = {"T1": 8, "T2": 10, "T3": 15}
    deadlines_offset = {"T1": 6, "T2": 8, "T3": 11}

    remaining = {k: 0 for k in runtimes}
    deadlines = {}
    next_release = {}

    start_time = time.time()

    for task in runtimes:
        next_release[task] = start_time
        deadlines[task] = float("inf")

    quantum = 1 
    end_time = start_time + 60

    color_codes = {"T1": "#FF0000", "T2": "#0000FF", "T3": "#00FF00"}
    root = tk.Tk()
    root.title("EDF Task Colors")
    root.geometry("400x400")

    print("Starting EDF scheduling for 60 seconds\n")

    try:
        while time.time() < end_time:
            now = time.time()

            for task in runtimes:
                if now >= next_release[task]:
                    remaining[task] = runtimes[task]
                    deadlines[task] = next_release[task] + deadlines_offset[task]
                    next_release[task] += periods[task]
                    print(f"[{task}] Released (deadline at {deadlines[task] - start_time:.1f}s)")

            ready_tasks = [t for t in runtimes if remaining[t] > 0]

            if ready_tasks:
                current = min(ready_tasks, key=lambda t: deadlines[t])

                print(f"[{current}] RUNNING (time {now - start_time:.1f}s)")
                root.configure(bg=color_codes[current])
                root.update()
                time.sleep(quantum)
                root.configure(bg="white")
                root.update()
                remaining[current] -= quantum

                if time.time() > deadlines[current]:
                    print(f"⚠ DEADLINE MISSED by {current}")

            else:
                print("[IDLE]")
                time.sleep(quantum)

    except KeyboardInterrupt:
        print("Interrupted by user")

    print("\nEDF scheduling finished.")
    root.destroy()


if __name__ == "__main__":
    main()