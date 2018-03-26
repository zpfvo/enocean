#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from enocean.consolelogger import init_logging
import enocean.utils
from enocean.communicators.serialcommunicator import SerialCommunicator
from enocean.protocol.packet import RadioPacket
from enocean.protocol.constants import PACKET, RORG
import sys
import traceback

try:
    import queue
except ImportError:
    import Queue as queue

from collections import OrderedDict


def create_enocean_teach_in(sender):
    packet_response = RadioPacket.create(
        RORG.BS4, 0x20, 0x1, sender=sender)
    packet_response.data[1:5] = [0x40, 0x18, 0x2d, 0x80]
    packet_response.parsed = OrderedDict({})
    return packet_response


def assemble_radio_packet(transmitter_id, destination_id=None):
    return RadioPacket.create(rorg=RORG.BS4, rorg_func=0x10, rorg_type=0x03,
                              sender=transmitter_id,
                              destination=destination_id,
                              SP=255,
                              TMP=10.0,
                              learn=False)


init_logging()
communicator = SerialCommunicator(port="/dev/ttyUSB1")
communicator.start()
print('The Base ID of your module is %s.' % enocean.utils.to_hex_string(communicator.base_id))

if communicator.base_id is not None:
    print('Sending example package.')
    sender = communicator.base_id
    sender[-1] = sender[-1] + 1
    # communicator.send(create_enocean_teach_in(sender))
    communicator.send(assemble_radio_packet(sender))

# endless loop receiving radio packets
while communicator.is_alive():
    try:
        # Loop to empty the queue...
        packet = communicator.receive.get(block=True, timeout=1)

        if packet.packet_type == PACKET.RADIO and packet.rorg == RORG.BS4:
            # parse packet with given FUNC and TYPE
            for k in packet.parse_eep(0x00, 0x01):
                print('%s: %s' % (k, packet.parsed[k]))
        if packet.packet_type == PACKET.RADIO and packet.rorg == RORG.BS1:
            # alternatively you can select FUNC and TYPE explicitely
            packet.select_eep(0x00, 0x01)
            # parse it
            packet.parse_eep()
            for k in packet.parsed:
                print('%s: %s' % (k, packet.parsed[k]))
        if packet.packet_type == PACKET.RADIO and packet.rorg == RORG.RPS:
            for k in packet.parse_eep(0x02, 0x02):
                print('%s: %s' % (k, packet.parsed[k]))
    except queue.Empty:
        continue
    except KeyboardInterrupt:
        break
    except Exception:
        traceback.print_exc(file=sys.stdout)
        break

if communicator.is_alive():
    communicator.stop()
