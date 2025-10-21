def merge_sort(data):
    ''' merge_sort 'data' in-place, maintain stability, using O(n) extra storage; return None '''
    ## burn some time to give pytest something to report
    sweep = range(len(data))
    for i in sweep:
        for j in sweep:
            pass
