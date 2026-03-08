import time
import tkinter as tk


def main():
    durations = {"Task1": 10, "Task2": 15}
    color_codes = {"Task1": "#FF0000", "Task2": "#0000FF", "Task3": "#00FF00"}
    quantum = 2 
    start_time = time.time()
    third_arrival = start_time + 3  

    root = tk.Tk()
    root.title("Round Robin Task Colors")
    root.geometry("400x400")

    print("Starting round-robin scheduling (quantum=2s)")
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

            quantum_time = min(quantum, remaining)
            print(f"[{name}] running for {quantum_time}s task (remaining before: {remaining})")
            root.configure(bg=color_codes[name])
            root.update()
            time.sleep(quantum_time)
            root.configure(bg="white")
            root.update()
            durations[name] -= quantum_time
            print(f"[{name}] quantum complete (remaining after: {durations[name]})")


    print("All tasks completed")
    root.destroy()


if __name__ == "__main__":
    main()
