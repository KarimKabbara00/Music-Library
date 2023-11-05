def compile_artists(artists):
    alphabetically_sorted = {}
    for a in artists:

        if a[0] not in alphabetically_sorted.keys():
            alphabetically_sorted[a[0]] = []

        if a in alphabetically_sorted[a[0]]:
            continue

        alphabetically_sorted[a[0]].append(a)

    alphabetically_sorted = dict(sorted(alphabetically_sorted.items()))
    return alphabetically_sorted
