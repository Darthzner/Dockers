def delay(packet):


    import time
    packet.global_var('ack1',0)   
    if packet['IP']['src']=='172.17.0.4' and packet['IP']['ttl']== 63:        
        packet.global_var('delay_max',0)
        packet.global_var1('time1', time.time())
        packet.global_var1('ack1', int(packet['TCP']['seq'],0)+int(packet['TCP']['len'],0))        
    elif packet['IP']['src']=='172.17.0.3' and int(packet['TCP']['ack'],0) == packet.ack1:
        timeT=time.time()-packet.time1        
        if timeT>packet.delay_max:
            packet.global_var1('delay_max', timeT)
            print("El delay maximo hasta el momento es: " + str(packet.delay_max))

    return packet
                                                               