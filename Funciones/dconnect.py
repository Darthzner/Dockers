def dconnect(packet):

    if packet['IP']['src'] == '172.17.0.4':
        packet['XMPP']['to'] = ""

        print("Interceptadou")

    # If the condition is meet
    return packet
~                                                                                        
~                                                                                        
~                  