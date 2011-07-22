#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, QtNetwork
from PyQt4.uic import loadUi, loadUiType
import re

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class TelnetDisplay(QtGui.QTextBrowser):
    """The TelnetDisplay will show a telnet session."""
    _ioDevice = None
    def __init__(self, parent=None):
        QtGui.QTextBrowser.__init__(self, parent)

        # Use monospace and a black background
        self.setStyleSheet("""
            background-color: #000;
            color: #ccc;
            font-family: Courier,"Nimbus Mono",monospace; 
        """)

        self._out_buffer = ''

    def setIODevice(self, ioDevice):
        if self._ioDevice:
            self._ioDevice.readyRead.disconnect(self._readyRead)
        self._ioDevice = ioDevice
        self._ioDevice.readyRead.connect(self._readyRead)


    def ioDevice(self):
        return self._ioDevice

    def _readyRead(self):
        """Call this when there is more data to display"""
        print "readyRead"
        data = ''
        while self._ioDevice.bytesAvailable() > 0:
            print "Data: "+data
            data += self._ioDevice.read(1024)

        self.addData(data)

    def _flush(self):
        """Flushes the characters stored in the out buffer to the
        QTextBrowser."""
        self.insertPlainText(self._out_buffer)
        self._out_buffer = ''
        

    def addData(self, data):
        """Add more telnet commands to this session."""
        dit = self._dit = iter(data)

        for char in dit:
            o = ord(char)
            if o == 0:
                pass

            elif o == 8:
                self.apply_backspace()

            elif o > 240:
                self.apply_TELNET(char, dit)

            elif o == 0x1b:
                self.apply_ANSI(dit)

            else:
                self._out_buffer += char
            
            #if char == '\xff':
                
            #if char
            #text, esc, self.data = self.data.partition('\x1b')

            #text = text.replace('\xff\xf9', '')
            #print repr(text),
            #self.insertPlainText(repr(text)+'---')
            #if esc:
            #    m = re.match(r'^\[(\d+(?:;\d+)*)m', self.data)
            ###    if m:
            #        self.data = self.data[m.end():]
            #        for cmd in m.group(1).split(';'):
            #            self.apply_cmd(int(cmd))
            #        continue

             #   print '<ESC>',
             #   self.mudOutput.insertPlainText('<ESC>')

    
        self._flush()

    def apply_backspace(self):
        self._flush()
        self.moveCursor(QtGui.QTextCursor.PreviousCharacter)

    def apply_TELNET(self, char, dit):
        self._out_buffer += '<TELNET {}>'.format(ord(char))

    def apply_ANSI(self, dit):
        char = dit.next()

        if char == '[':  # CSI
            code = ''
            char = dit.next()

            while not '@' <= char <= '~':
                code += char
                char = dit.next()

            self.apply_ANSI_CSI(code, char)

        elif '@' <= char <= '_':
            self.apply_ANSI_ESC(char)

        else:
            self._out_buffer += '<ANSI ESC-{}?>'.format(ord(char))

    def apply_ANSI_ESC(self, code):
        self._out_buffer += '<ANSI ESC-{} IGNORED>'.format(code)

    def apply_ANSI_CSI(self, code, char):
        if char == 'm':
            self.apply_ANSI_color(code)
        else:
            self._out_buffer += '<ANSI ESC-{}-{} IGNORED>'.format(code, char)

    def apply_ANSI_color(self, colors):
        for color in (int(color) for color in colors.split(';')):
            if color == 0:
                self.set_bold(False)
                self.set_color(7)
                self.set_bgcolor(0)
            elif color == 1:
                self.set_bold(True)
            elif 30 <= color <= 37:
                self.set_color(color-30)
            elif 40 <= color <= 47:
                self.set_bgcolor(color-40)
            else:
                self._out_buffer += '<ANSI COLOR {} IGNORED>'.format(color)

    def set_bold(self, bold):
        if bold:
            self.setFontWeight(QtGui.QFont.Bold)
        else:
            self.setFontWeight(QtGui.QFont.Normal)

    def ansi_color(self, color, bright):
        return getattr(QtCore.Qt, [
            'black',    'darkRed',      'darkGreen',    'darkYellow',
            'darkBlue', 'darkMagenta',  'darkCyan',     'gray',

            'darkGray', 'red',          'green',        'yellow',
            'blue',     'magenta',      'cyan',         'white',
        ][color + 8*(1 if bright else 0)])

    def set_color(self, color):
        self.setTextColor(self.ansi_color(
            color,
            self.fontWeight() == QtGui.QFont.Bold))

    def set_bgcolor(self, color):
        self.setTextBackgroundColor(self.ansi_color(
            color,
            self.fontWeight() == QtGui.QFont.Bold))

class Main(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.resize(800, 640)

        self.centralWidget = QtGui.QWidget(self)
        self.centralWidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralWidget)

        layout = QtGui.QVBoxLayout(self.centralWidget)

        self.mudOutput = TelnetDisplay(self)
        layout.addWidget(self.mudOutput)

        self.mudInput = QtGui.QLineEdit(self)
        self.mudInput.returnPressed.connect(self.mudInputDone)
        layout.addWidget(self.mudInput)

        self.sock = None

        self.connect('midkemiaonline.com')


    def connect(self, hostname):
        if ':' in hostname:
            hostname, port = hostname.split(':',1)
        else:
            port = 23

        self.sock = QtNetwork.QTcpSocket(self)
        self.sock.connectToHost(hostname, port)

        self.sock.connected.connect(self.connection_connected)
        self.sock.disconnected.connect(self.connection_disconnected)

        self.mudOutput.setIODevice(self.sock)

    def connection_connected(self):
        self.mudOutput.insertPlainText("\nConnected.\n")

    def connection_disconnected(self):
        self.mudOutput.insertPlainText("\nDisconnected.\n")

    def connection_readyRead(self):
        data = str(self.sock.readAll())
        self.processTelnetCommands(data)

    def mudInputDone(self):
        cmd = str(self.mudInput.text()).strip()
        self.doMudInput(cmd)
        self.mudInput.setText('')

    def doMudInput(self, cmd):
        if cmd[:1] == '!':
            self.doConsoleInput(cmd[1:])
        elif self.sock:
            self.sock.write(cmd+'\r\n')
        else:
            self.mudOutput.insertPlainText("Please connect before issuing commands.")

    def consoleInputDone(self):
        cmd = str(self.consoleInput.text()).strip()
        self.doConsoleInput(cmd)
        self.consoleInput.setText('')

    def doConsoleInput(self, cmd):
        #self.consoleOutput.insertPlainText(">>> "+cmd+"\n")
        print ">>> {}".format(cmd)
        pass
        try:
            result = eval(cmd, globals(), locals())
        except Exception as e:
            print e
            #self.consoleOutput.insertPlainText(repr(e)+'\n')
            pass
        else:
            if result is not None:
                #self.consoleOutput.insertPlainText(repr(result)+'\n')
                print repr(result)
                pass
        



        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    main = Main()
    main.show()
    sys.exit(app.exec_())
