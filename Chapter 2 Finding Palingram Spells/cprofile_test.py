# profile_my_method.py
import cProfile
import pstats
from palingrams import find_palingrams


def profile_method():
    find_palingrams()


if __name__ == "__main__":
    # Create a profile object
    profiler = cProfile.Profile()

    # Start profiling
    profiler.enable()

    # Run the method you want to profile
    profile_method()

    # Stop profiling
    profiler.disable()

    # Create a Stats object and print the results
    stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)
    stats.print_stats()
