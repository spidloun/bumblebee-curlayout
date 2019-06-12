
import bumblebee.engine
import bumblebee.output
import bumblebee.util

class Module(bumblebee.engine.Module):
	def __init__(self, engine, config):
		super(Module, self).__init__(engine, config, bumblebee.output.Widget(full_text=self.current_layout))
		
	def current_layout(self, widget):
		try:
			result = bumblebee.util.execute("xkblayout-state print %s")
		except RuntimeError:
			return "n/a"
		return u"\uf11c  %s" % result
