#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read(path):
    result = []
    with open(path, "rt") as f:
        for line in f:
            result.append(int(line))
    return result

def _validate(_stdout, _input, _output, info):
    info("rollercoaster - validate %s with %s" % (_stdout, _input))

    _stdout = read(_stdout)

    _input = read(_input)
    N = _input[0]
    _input = _input[1:]

    if not sorted(_stdout) == sorted(_input):
        info("you should use the input data")
        return 0

    linenumber = 0
    value = None
    sign = None

    for found in _stdout:
        linenumber += 1

        if value is not None:
            
            _sign = 1
            if found < value:
                _sign = -1

            if _sign == sign:
                info("line %d: found %r, wrong sign" % (linenumber, found))
                return 0
            
            sign = _sign
            value = found

    return 1

def validate(_stdout, _input, _output, info):
    try:
        return _validate(_stdout, _input, _output, info)

    except OSError as err:
        info("OS error: {0}".format(err))
        return 0

    except ValueError:
        info("Could not convert data to an integer.")
        return 0

    except:
        import sys
        info("some exception happened: %s" % (sys.exc_info()[0]))
        return 0


#######

if __name__ == "__main__":
    import sys
    score = validate( sys.argv[1], sys.argv[2], sys.argv[3], print )
    print("score", score)
