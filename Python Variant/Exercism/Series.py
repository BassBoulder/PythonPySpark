def slices(series, length):

    if length == 0:
        raise ValueError("slice length cannot be zero")
        return

    elif length < 0:
        raise ValueError("slice length cannot be negative")
        return        

    elif series is "":
        raise ValueError("series cannot be empty")
        return        

    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")
        return        

    result = []

    for start in range(0, len(series) - length + 1):
        end = start + length
        result.append(series[start:end])

    return result
        