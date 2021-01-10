import hashlib

class OsSystem:
    password = "145678"
    hashed = "06705750d1003fe6c18ad11a77dfd4261246d3d1de8b28e5534d7c8d7fadad19"
    
    def controlHash(self):
        enterInput = input("Lütfen parolayı girin: ")
        hashedPass = hashlib.sha256(str(enterInput).encode('utf-8')).hexdigest()
        if enterInput != "exit":
            if self.hashed != hashedPass:
                print({'error' : 'Hatalı şifre girildi.'})
                return self.controlHash()
            else:
                print("Hash Pwd: {}".format(self.hashed))
        else:
            exit()

getObject = OsSystem()

getObject.controlHash()