def idmod(packet):

    if packet['IP']['src'] == '172.17.0.2':
        packet['XMPP']['id'] = "id='wR0A4-1000'"
        print("interceptando")
    # If the condition is meet
        return packet

    return None
~                  