#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 12
# 55139 Daniela Correia Coelho
# 56593 Inês Franco Calheiros



def hourToInt(time):
    """

    """
    t = time.split(":")
    return int(t[0])



def minutesToInt(time):
    """

    """
    pass #TODO
    


def intToTime(hour, minutes):
    """

    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m










