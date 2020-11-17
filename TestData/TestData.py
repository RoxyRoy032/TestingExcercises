class TestData:
    HomePage_data = {0: "Add/Remove Elements",
                           1: "Context Menu",
                           2: "Disappearing Elements",
                           3: "Entry Ad",
                           4: "File Download",
                           5: "File Upload",
                           6: "Form Authentication",
                           7: "JavaScript Alerts",
                           8: "Key Presses"}

    users_data = [  {0:"tomsmith", 1:"SuperSecretPassword!"},
                    {0:"tomsmith1", 1:"SuperS1ecretPassword!"}]

    text_data = {0: "testing"}

    pathFile_data = {0: "C://Users/alber/Downloads/some-file.txt"}

    def getHomePageData(self):
        return self.HomePage_data

    def getUsersData(self):
        return self.users_data

    def getTextData(self):
        return self.text_data

    def getPathFileData(self):
        return self.pathFile_data