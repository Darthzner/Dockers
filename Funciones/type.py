def type(packet):

    if packet['IP']['src'] == '172.17.0.4':
        packet['XMPP']['type'] = "None"

        print("Interceptadou")

    # If the condition is meet
        return packet

    return packet
