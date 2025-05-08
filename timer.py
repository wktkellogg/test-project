# %%
import time


def count_up_timer(n):
    for i in range(1, n + 1):
        print(f"Time elapsed: {i} seconds", end="\r")
        time.sleep(1)
    print("\nTimer finished!")


# Example usage
n = 3  # Replace with the desired number of seconds
count_up_timer(n)

# %%
