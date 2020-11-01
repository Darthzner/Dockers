def mfrom(packet):

    if packet['IP']['src'] == "172.17.0.4" and packet['IP']['addr'] == "172.17.0.2":
        packet['XMPP']['to'] = "to='isaac@localhost'"

    # If the condition is meet
        return packet

    return None
