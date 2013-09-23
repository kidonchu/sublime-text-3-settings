import sublime, sublime_plugin
import os.path

class StopInsertOnSave (sublime_plugin.EventListener):
	def on_pre_save(self, view):
		view.run_command('exit_insert_mode')
