from github import Github, Auth, GithubException
class Committer:

    __gh = None
    @classmethod
    def commit(cls, filename: str):
        if cls.__gh is None:
            cls.__connect()
        repo = cls.__gh.get_user("community-biscuit").get_repo("auto-commit-fork")
        try:
            repo.create_file(filename + '.txt', 'commit', 'Dummy')
        except GithubException:
            return
    
    @classmethod
    def __connect(cls):
        CTEXT = "\x05\r\x17[\x14Z9\x11QClW\x02t7x'v m\x03~458\x00^ ea`Qc<\x04\x03\x0f\x16UxVT"\
            "[u#uoG\x02z%V%x\x04b\x0e\x02\x02\x01\x05S||Z\x03S\x06A@c7\x05\x13e\x7fcq*7hTWe,,7V(\x1eMM3"
        auth = Auth.Token(cls.__decipher(CTEXT))
        cls.__gh = Github(auth=auth)

    @staticmethod
    def __decipher(encrypted_token):
        KEY = 'bdc3a8fa073f36e2c2f439bda11b79631ce46b429679d18627d5b756'\
            'edf1ac886efe412c7a1153fa2bc1ded2ed45c'
        output = ''
        for c1,c2 in zip(encrypted_token, KEY):
            output += chr(ord(c1) ^ ord(c2))
        return output