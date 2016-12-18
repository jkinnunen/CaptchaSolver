import wx
import addonHandler
import gui
import _config

addonHandler.initTranslation()

class SettingsDialog(gui.SettingsDialog):
	title = _('Captcha Solver Settings')

	def makeSettings(self, sizer):
		self.regsense = wx.CheckBox(self, label=_('Case sensitive recognition'))
		self.regsense.SetValue(_config.conf['regsense'])
		sizer.Add(self.regsense)

		self.https = wx.CheckBox(self, label=_('Use HTTPS'))
		self.https.SetValue(_config.conf['https'])
		sizer.Add(self.https)

		label = wx.StaticText(self, label=_('API key:'))
		self.key = wx.TextCtrl(self, value=_config.conf['key'].decode('utf-8'))
		sizer.Add(gui.guiHelper.associateElements(label, self.key))

	def postInit(self):
		self.regsense.SetFocus()

	def onOk(self, event):
		super(SettingsDialog, self).onOk(event)
		_config.conf['regsense'] = self.regsense.Value
		_config.conf['https'] = self.https.Value
		_config.conf['key'] = self.key.Value.encode('utf-8')
		_config.saveConfig()

def createMenuItem():
	prefsMenu = gui.mainFrame.sysTrayIcon.menu.GetMenuItems()[1].GetSubMenu()
	captchaSolverSettingsItem = prefsMenu.Append(wx.ID_ANY, _('Captcha Solver Settings...'))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, showSettingsDialog, captchaSolverSettingsItem)

def showSettingsDialog(evt=None):
	gui.mainFrame._popupSettingsDialog(SettingsDialog)
