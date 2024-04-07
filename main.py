import sys
from tkinter import *
from tkinter import filedialog
import DES as des

title = "Mã hóa và giải mã file bằng DES"
args = sys.argv[1:]

class App:
    plainFileLabel = "Đường dẫn file rõ"
    cipherFileLabel = "Đường dẫn file mã"
    selectCipherButtonString = "..."
    fileDialogueString = 'Chọn file rõ'
    encryptButtonString = 'Mã hóa'
    decryptButtonString = 'Giải mã'
    isEncrypting = ''
    cipher = []
    plain = []
    def __init__(self):
        root = Tk()
        root.title(title)
        self.savePath = ''
        self.createWindow(root)
        root.mainloop()

    def createWindow(self, root):
        if self.getArgs(root)<1:
            window = self.displayWindow(root)

    def getArgs(self, root):
        success = 0
        for i in range(0, len(args)):
            self.savePath = args[i]
            val = self.openSavePath(root)
            if success == 0:
                success = val
        return success

    def displayWindow(self, master):
        titleLabel = Label(text=title)
        titleLabel.grid(pady=10)

        frame = Frame(master)
        frame.grid(padx=20, column=0)

        inputLabel = Label(frame, text=self.plainFileLabel)
        inputLabel.grid(row=1, column=0, padx=10)

        self.inputPlain = Entry(frame)
        self.inputPlain.grid(row=1, column=1, columnspan=2)

        getSaveButton = Button(frame, text=self.selectCipherButtonString, command=self.getPlainFile)
        getSaveButton.grid(row=1, column=3, padx=5)

        inputLabel = Label(frame, text=self.cipherFileLabel)
        inputLabel.grid(row=2, column=0, padx=10, pady = 20)

        self.inputCipher = Entry(frame)
        self.inputCipher.grid(row=2, column=1, columnspan=2)

        getCipherButton = Button(frame, text=self.selectCipherButtonString, command=self.getCipherFile)
        getCipherButton.grid(row=2, column=3, padx=5)

        end = Frame(master)
        end.grid(padx=20, column=0)

        encryptButton = Button(end, text=self.encryptButtonString, command = self.encrypt)
        encryptButton.grid(row=0, column=0, pady=10, padx=10)

        decryptButton = Button(end, text=self.decryptButtonString, command=self.decrypt)
        decryptButton.grid(row=0, column=1, pady=10, padx=10)

    def getPlainFile(self):
        savePath = filedialog.askopenfilename(initialdir='./', title=self.fileDialogueString)
        if not savePath:
            return
        filename = savePath[savePath.rfind('/') - len(savePath) + 1:]
        if not filename.endswith(".txt"):
            FilenameWarning()
        else:
            self.inputPlain.delete(0, END)
            self.inputPlain.insert(0, savePath)
    def getCipherFile(self):
        savePath = filedialog.askopenfilename(initialdir='./', title=self.fileDialogueString)
        if not savePath:
            return
        filename = savePath[savePath.rfind('/') - len(savePath) + 1:]
        if not filename.endswith(".txt"):
            FilenameWarning()
        else:
            self.inputCipher.delete(0, END)
            self.inputCipher.insert(0, savePath)
    def encrypt(self):
        cipher = []
        self.savePath = self.inputPlain.get()
        if self.savePath != "":
            plainFile = open(self.savePath, encoding="utf8")
            plainText  = plainFile.read()
            listText = plainText.splitlines()
            for text in listText:
                cipherText = des.encrypt(text)
                cipher.append(cipherText)
            self.cipher = "\n".join(cipher)
            self.isEncrypting = "X"
            self.save()
    def decrypt(self):
        plain = []
        self.savePath = self.inputCipher.get()
        if self.savePath != "":
            plainFile = open(self.savePath, "r")
            plainText = plainFile.read()
            listText = plainText.splitlines()
            for text in listText:
                plainText = des.decrypt(text)
                plain.append(plainText)
            self.plain = "\n".join(plain)
            self.isEncrypting = ''
            self.save()
    def save(self):
        files = [('Text Documents', '*.txt')]
        file = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
        if self.isEncrypting == "X":
            file.write(self.cipher)
        else:
            file.write(self.plain)


class FilenameWarning:
    titleString = 'Warning'
    errorString = 'Chỉ mã hóa và giải mã được file txt'
    buttonString = 'OK'

    def __init__(self):
        filenameTk = Tk()
        filenameTk.title(self.titleString)
        filenameTkWindow = self.createWindow(filenameTk)

    def createWindow(self, master):
        frame = Frame(master)
        frame.grid(padx=20, pady=10)

        introLabel = Label(frame, text=self.errorString, anchor=E, justify=LEFT, wraplength=400)
        introLabel.grid(row=1, column=0, sticky='W')

        end = Frame(master)
        end.grid(padx=20, column=0)

        showHelpButton = Button(end, text=self.buttonString, command=master.destroy)
        showHelpButton.grid(row=0, column=1, padx=10, pady=10)
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
# redbutton = Button(frame, text = 'Red', fg ='red')
# redbutton.pack( side = LEFT)
# greenbutton = Button(frame, text = 'Brown', fg='brown')
# greenbutton.pack( side = LEFT )
# bluebutton = Button(frame, text ='Blue', fg ='blue')
# bluebutton.pack( side = LEFT )
# blackbutton = Button(bottomframe, text ='Black', fg ='black')
# blackbutton.pack( side = BOTTOM)

app = App()
