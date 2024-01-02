def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # c to f is c x 9/5 + 32
    # f to c is f - 32 x 5/9


    if unit_in != "f" and unit_in != "c":
        return f"Invalid Unit {unit_in}"
    
    if unit_out != "f" and unit_out != "c":
         return f"Invalid Unit {unit_out}"

    if unit_in == "f" and unit_out == "c":
        temp = (temp - 32) * 5/9

    if unit_in == "c" and unit_out == "f":
        temp = (temp * 9 / 5) + 32

        return temp
