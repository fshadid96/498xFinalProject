"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import pmt
import numpy as np
from gnuradio import gr

class msg_block(gr.basic_block):
     def __init__(self):
         gr.basic_block.__init__(
             self,
             name="msg_block",
             in_sig=None,
             out_sig=None)
	 song_file = ("songs.txt", "w+")
         self.message_port_register_in(pmt.intern('msg_in'))
         self.set_msg_handler(pmt.intern('msg_in'), self.handle_msg)
 
     def handle_msg(self, msg):
         if(pmt.is_tuple(msg)):
            t = pmt.to_long(pmt.tuple_ref(msg, 0))
            m = pmt.symbol_to_string(pmt.tuple_ref(msg, 1))
            de = DataEvent([t, m])
            song_file.write(de); 
            del de

